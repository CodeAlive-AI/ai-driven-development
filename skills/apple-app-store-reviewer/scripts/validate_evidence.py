#!/usr/bin/env python3
"""Validate agent/human evidence and enforce semantic evidence invariants."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping

from common import ReviewInputError, dump_json, load_json, make_check, make_evidence, make_finding, now_iso, sha256_file

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "assets" / "manual-evidence.schema.json"
HASH_RE = re.compile(r"^[a-f0-9]{64}$")
SECRET_KEY_RE = re.compile(r"(?:password|passwd|secret|token|api[_-]?key|authorization|credential|private[_-]?key)", re.I)
SECRET_VALUE_RES = [
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def _schema_errors(data: Any, schema_path: Path) -> tuple[list[str], str]:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        errors = []
        if not isinstance(data, Mapping):
            return ["/: root must be an object"], "manual"
        for key in ("schema_version", "reviewer", "reviewed_at", "checks", "findings"):
            if key not in data:
                errors.append(f"/{key}: required property is missing")
        return errors, "manual"
    schema = load_json(schema_path)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.absolute_path)):
        pointer = "/" + "/".join(str(part) for part in error.absolute_path)
        errors.append(f"{pointer}: {error.message}")
    return errors, "jsonschema"


def _walk(value: Any, path: str = "$") -> Iterable[tuple[str, str | None, Any]]:
    if isinstance(value, Mapping):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            yield child_path, str(key), child
            yield from _walk(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            child_path = f"{path}[{index}]"
            yield child_path, None, child
            yield from _walk(child, child_path)


def _secret_issues(data: Any) -> list[str]:
    issues: list[str] = []
    for path, key, value in _walk(data):
        if key and SECRET_KEY_RE.search(key):
            # Environment-variable names and explicit redaction markers are safe.
            if key.lower().endswith("_env") or value in (None, "", "<redacted>"):
                continue
            if isinstance(value, str) and re.fullmatch(r"[A-Z][A-Z0-9_]{2,127}", value):
                continue
            issues.append(f"{path}: secret-shaped key contains a value")
        if isinstance(value, str):
            for pattern in SECRET_VALUE_RES:
                if pattern.search(value):
                    issues.append(f"{path}: secret-shaped value detected")
                    break
    return issues


def validate_evidence_data(
    data: Mapping[str, Any],
    *,
    evidence_path: str | Path,
    schema_path: str | Path = DEFAULT_SCHEMA,
    screenshots_root: str | Path | None = None,
    required_checks: Iterable[str] = (),
) -> dict[str, Any]:
    evidence_path = Path(evidence_path).resolve()
    schema_path = Path(schema_path).resolve()
    root = Path(screenshots_root).resolve() if screenshots_root else None
    findings: list[dict[str, Any]] = []
    checks_out: list[dict[str, Any]] = []
    facts: dict[str, Any] = {}

    schema_errors, schema_tool = _schema_errors(data, schema_path)
    if schema_errors:
        for index, error in enumerate(schema_errors, 1):
            findings.append(make_finding(
                id=f"EVIDENCE-SCHEMA-{index:03d}",
                title="Manual/agent evidence does not match its schema",
                severity="BLOCKER",
                category="evidence-integrity",
                guideline="Release evidence",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="validation", location=str(evidence_path), detail=error)],
                rationale="Unstructured or malformed evidence cannot satisfy a release gate.",
                remediation="Correct the evidence using assets/manual-evidence.schema.json.",
                verification=["validate_evidence.py exits 0"],
                sources=[str(schema_path)],
                automation="deterministic-validation",
            ))
        checks_out.append(make_check("evidence.schema", "Manual/agent evidence schema", "ERROR", mandatory=True, tool=schema_tool, detail=f"{len(schema_errors)} schema error(s)"))
    else:
        checks_out.append(make_check("evidence.schema", "Manual/agent evidence schema", "PASS", mandatory=True, tool=schema_tool, detail="Evidence matches schema"))

    raw_checks = data.get("checks", []) if isinstance(data.get("checks"), list) else []
    check_map: dict[str, Mapping[str, Any]] = {}
    duplicates: list[str] = []
    for item in raw_checks:
        if not isinstance(item, Mapping):
            continue
        check_id = str(item.get("id", "")).strip()
        if not check_id:
            continue
        if check_id in check_map:
            duplicates.append(check_id)
        else:
            check_map[check_id] = item
    if duplicates:
        findings.append(make_finding(
            id="EVIDENCE-DUPLICATE-CHECKS",
            title="Evidence contains duplicate check identifiers",
            severity="HIGH",
            category="evidence-integrity",
            guideline="Release evidence",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="file", location=str(evidence_path), detail="Duplicate check IDs", value=sorted(set(duplicates)))],
            rationale="Duplicate states can mask a failing or unreviewed mandatory check.",
            remediation="Keep one unambiguous check record per identifier.",
            verification=["No duplicate check identifiers remain"],
            sources=[str(schema_path)],
            automation="deterministic-validation",
        ))

    missing_required = sorted({str(x) for x in required_checks if str(x)} - set(check_map))
    if missing_required:
        findings.append(make_finding(
            id="EVIDENCE-REQUIRED-CHECK-MISSING",
            title="Required exact evidence check is missing",
            severity="HIGH",
            category="evidence-integrity",
            guideline="Release evidence",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="file", location=str(evidence_path), detail="Missing exact check IDs", value=missing_required)],
            rationale="A generic evidence object cannot substitute for each mandatory claim.",
            remediation="Add the exact required check records with observed status and evidence.",
            verification=["Every --require-check identifier is present"],
            sources=[str(schema_path)],
            automation="deterministic-validation",
        ))

    screens = data.get("screens", []) if isinstance(data.get("screens"), list) else []
    screen_paths: set[str] = set()
    screen_failures: list[str] = []
    hash_mismatches: list[dict[str, str]] = []
    missing_files: list[str] = []
    for index, item in enumerate(screens):
        if not isinstance(item, Mapping):
            continue
        path_value = str(item.get("path", ""))
        if path_value in screen_paths:
            screen_failures.append(f"duplicate path: {path_value}")
        screen_paths.add(path_value)
        if item.get("verdict") != "PASS":
            screen_failures.append(f"{path_value}: verdict={item.get('verdict')}")
        expected_hash = str(item.get("sha256", ""))
        if expected_hash and not HASH_RE.fullmatch(expected_hash):
            screen_failures.append(f"{path_value}: invalid sha256 syntax")
        if root and path_value:
            candidate = Path(path_value)
            if not candidate.is_absolute():
                candidate = root / candidate
            candidate = candidate.resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                screen_failures.append(f"{path_value}: escapes screenshots root")
                continue
            if not candidate.is_file():
                missing_files.append(path_value)
            elif expected_hash:
                actual = sha256_file(candidate)
                if actual != expected_hash:
                    hash_mismatches.append({"path": path_value, "expected": expected_hash, "actual": actual})
    facts["screens_reviewed"] = len(screens)
    facts["screen_paths_unique"] = len(screen_paths)

    visual = check_map.get("screenshots.visual")
    if visual and visual.get("status") == "PASS":
        visual_facts = data.get("facts", {}) if isinstance(data.get("facts"), Mapping) else {}
        visual_problems = list(screen_failures)
        if not screens:
            visual_problems.append("screens array is empty")
        if visual_facts.get("all_originals_reviewed") is not True:
            visual_problems.append("facts.all_originals_reviewed is not true")
        if visual_facts.get("all_locales_reviewed") is not True:
            visual_problems.append("facts.all_locales_reviewed is not true")
        if missing_files:
            visual_problems.append(f"{len(missing_files)} referenced screenshot file(s) are missing")
        if hash_mismatches:
            visual_problems.append(f"{len(hash_mismatches)} screenshot hash mismatch(es)")
        if visual_problems:
            findings.append(make_finding(
                id="EVIDENCE-VISUAL-PASS-UNSUPPORTED",
                title="screenshots.visual PASS is not supported by complete immutable evidence",
                severity="BLOCKER",
                category="evidence-integrity",
                guideline="2.3 Accurate Metadata",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="validation", location=str(evidence_path), detail="Visual PASS invariant failures", value=visual_problems[:50])],
                rationale="A visual pass requires every original and locale to be reviewed with matching final hashes and no unresolved screen verdict.",
                remediation="Review every final original at full resolution, correct the facts/hashes/verdicts, and rerun validation.",
                verification=["validate_evidence.py reports no visual invariant failure"],
                sources=["references/screenshot-review.md"],
                automation="deterministic-validation",
            ))

    secret_issues = _secret_issues(data)
    if secret_issues:
        findings.append(make_finding(
            id="EVIDENCE-SECRET-MATERIAL",
            title="Evidence appears to contain secret material",
            severity="BLOCKER",
            category="evidence-integrity",
            guideline="1.6 Data Security",
            confidence="HIGH",
            evidence=[make_evidence(kind="validation", location=str(evidence_path), detail="Secret-shaped values", value=secret_issues[:30])],
            rationale="Review artifacts may be shared or retained and must not expose credentials or private keys.",
            remediation="Remove the values, rotate any exposed credential, and use environment-variable names or redacted references.",
            verification=["No secret-shaped material is detected"],
            sources=["references/privacy-security.md"],
            automation="deterministic-validation",
        ))

    unresolved = [f for f in findings if f.get("status") in {"OPEN", "NEEDS_REVIEW", "ERROR"}]
    checks_out.append(make_check(
        "evidence.invariants",
        "Manual/agent evidence integrity invariants",
        "PASS" if not unresolved else "ERROR",
        mandatory=True,
        tool="validate_evidence.py",
        detail="All invariants passed" if not unresolved else f"{len(unresolved)} unresolved evidence finding(s)",
    ))
    return {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "valid": not schema_errors and not unresolved,
        "checks": checks_out,
        "findings": findings,
        "facts": {
            **facts,
            "schema": str(schema_path),
            "evidence": str(evidence_path),
            "required_checks": sorted({str(x) for x in required_checks if str(x)}),
            "missing_files": missing_files,
            "hash_mismatches": hash_mismatches,
        },
        "tools": [{"name": "validate_evidence.py", "status": "PASS" if not schema_errors else "ERROR", "detail": f"schema={schema_tool}"}],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate agent/human review evidence and its supporting hashes/invariants.")
    parser.add_argument("--evidence", required=True, help="Evidence JSON matching manual-evidence.schema.json")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA), help="Evidence JSON schema")
    parser.add_argument("--screenshots-root", help="Optional root used to verify referenced screenshot files and SHA-256")
    parser.add_argument("--require-check", action="append", default=[], help="Exact check ID that must exist; repeatable")
    parser.add_argument("--output", help="Write structured validation result")
    parser.add_argument("--strict", action="store_true", help="Return 2 when evidence is invalid")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        data = load_json(args.evidence)
        if not isinstance(data, Mapping):
            raise ReviewInputError("Evidence root must be an object")
        result = validate_evidence_data(
            data,
            evidence_path=args.evidence,
            schema_path=args.schema,
            screenshots_root=args.screenshots_root,
            required_checks=args.require_check,
        )
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"validate_evidence: {exc}\n")
        return 3
    text = dump_json(result, args.output) if args.output else dump_json(result)
    if not args.output:
        sys.stdout.write(text)
    return 2 if args.strict and not result.get("valid") else 0


if __name__ == "__main__":
    raise SystemExit(main())
