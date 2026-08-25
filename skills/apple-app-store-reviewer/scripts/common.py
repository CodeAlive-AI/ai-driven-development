#!/usr/bin/env python3
"""Shared primitives for the Apple App Store Reviewer skill."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

SCHEMA_VERSION = "1.0"
SKILL_VERSION = "1.2.0"
POLICY_BASELINE = "2026-08-25"
GUIDELINES_LAST_UPDATED = "2026-06-08"

SEVERITIES = ("BLOCKER", "HIGH", "MEDIUM", "LOW", "INFO")
STATUSES = ("OPEN", "PASS", "SKIPPED", "NEEDS_REVIEW", "FIXED", "ACCEPTED_RISK", "ERROR")
CONFIDENCES = ("CERTAIN", "HIGH", "MEDIUM", "LOW")
SEVERITY_ORDER = {name: index for index, name in enumerate(reversed(SEVERITIES))}

SECRET_KEY_RE = re.compile(
    r"(?:password|passwd|secret|token|api[_-]?key|authorization|credential|private[_-]?key)",
    re.IGNORECASE,
)
SECRET_VALUE_RES = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._~+/=-]{16,}"),
]


class ReviewInputError(ValueError):
    """Raised when the review input cannot be interpreted safely."""


@dataclass(frozen=True)
class Finding:
    id: str
    title: str
    severity: str
    status: str
    category: str
    guideline: str
    confidence: str
    evidence: list[dict[str, Any]]
    rationale: str
    remediation: str
    verification: list[str]
    sources: list[str]
    automation: str = "deterministic"
    tags: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["tags"] = list(self.tags)
        return data


def now_iso() -> str:
    """Return a reproducible UTC timestamp when SOURCE_DATE_EPOCH is set."""
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        try:
            dt = datetime.fromtimestamp(int(epoch), tz=timezone.utc)
        except (TypeError, ValueError, OSError):
            dt = datetime.now(timezone.utc)
    else:
        dt = datetime.now(timezone.utc)
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: str | Path) -> Any:
    path = Path(path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise ReviewInputError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ReviewInputError(f"Invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc


def dump_json(data: Any, path: str | Path | None = None) -> str:
    text = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if path is not None:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    return text


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_path(value: str | Path | None, base_dir: str | Path) -> Path | None:
    if value in (None, ""):
        return None
    path = Path(os.path.expandvars(os.path.expanduser(str(value))))
    if not path.is_absolute():
        path = Path(base_dir) / path
    return path.resolve()


def resolve_config_paths(config: Mapping[str, Any], config_path: str | Path) -> dict[str, Any]:
    """Resolve known path fields relative to the config without mutating input."""
    resolved = copy.deepcopy(dict(config))
    base = Path(config_path).resolve().parent
    paths = resolved.setdefault("paths", {})
    for key in (
        "project",
        "archive",
        "metadata",
        "screenshots",
        "privacy_export",
        "iap_export",
        "review_notes",
        "runtime_results",
        "ai_results",
        "visual_results",
        "native_value_dossier",
    ):
        if paths.get(key):
            paths[key] = str(normalize_path(paths[key], base))
    runtime = resolved.setdefault("runtime", {})
    for key in ("workspace", "project", "result_bundle"):
        if runtime.get(key):
            runtime[key] = str(normalize_path(runtime[key], base))
    return resolved


def redact(value: Any, key: str | None = None) -> Any:
    """Recursively redact credentials and common secret-shaped values."""
    if key and SECRET_KEY_RE.search(key):
        if value in (None, ""):
            return value
        if key.lower().endswith("_env") or key.lower().endswith("env"):
            return value
        return "<redacted>"
    if isinstance(value, dict):
        return {k: redact(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(item) for item in value]
    if isinstance(value, tuple):
        return [redact(item) for item in value]
    if isinstance(value, str):
        text = value
        for pattern in SECRET_VALUE_RES:
            text = pattern.sub("<redacted>", text)
        return text
    return value


def make_evidence(
    *,
    kind: str,
    location: str,
    detail: str,
    line: int | None = None,
    value: Any | None = None,
) -> dict[str, Any]:
    evidence: dict[str, Any] = {"kind": kind, "location": location, "detail": redact(detail)}
    if line is not None:
        evidence["line"] = int(line)
    if value is not None:
        evidence["value"] = redact(value)
    return evidence


def make_finding(
    *,
    id: str,
    title: str,
    severity: str,
    category: str,
    guideline: str,
    evidence: Iterable[dict[str, Any]],
    rationale: str,
    remediation: str,
    verification: Iterable[str],
    sources: Iterable[str],
    confidence: str = "HIGH",
    status: str = "OPEN",
    automation: str = "deterministic",
    tags: Iterable[str] = (),
) -> dict[str, Any]:
    severity = severity.upper()
    status = status.upper()
    confidence = confidence.upper()
    if severity not in SEVERITIES:
        raise ValueError(f"Unknown severity: {severity}")
    if status not in STATUSES:
        raise ValueError(f"Unknown status: {status}")
    if confidence not in CONFIDENCES:
        raise ValueError(f"Unknown confidence: {confidence}")
    finding = Finding(
        id=id,
        title=title,
        severity=severity,
        status=status,
        category=category,
        guideline=guideline,
        confidence=confidence,
        evidence=list(evidence),
        rationale=rationale,
        remediation=remediation,
        verification=list(verification),
        sources=list(sources),
        automation=automation,
        tags=tuple(tags),
    )
    return finding.to_dict()


def make_check(
    id: str,
    title: str,
    status: str,
    *,
    mandatory: bool,
    detail: str = "",
    tool: str = "",
    evidence: Iterable[dict[str, Any]] = (),
) -> dict[str, Any]:
    status = status.upper()
    if status not in STATUSES:
        raise ValueError(f"Unknown check status: {status}")
    return {
        "id": id,
        "title": title,
        "status": status,
        "mandatory": bool(mandatory),
        "detail": detail,
        "tool": tool,
        "evidence": list(evidence),
    }


def dedupe_findings(findings: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Deduplicate by stable ID, keeping the stronger unresolved variant."""
    selected: dict[str, dict[str, Any]] = {}
    status_rank = {"OPEN": 5, "NEEDS_REVIEW": 4, "ERROR": 3, "FIXED": 2, "ACCEPTED_RISK": 1, "PASS": 0, "SKIPPED": 0}
    for raw in findings:
        item = redact(copy.deepcopy(raw))
        key = str(item.get("id", "")).strip()
        if not key:
            continue
        current = selected.get(key)
        if current is None:
            selected[key] = item
            continue
        incoming_score = (SEVERITY_ORDER.get(item.get("severity", "INFO"), 0), status_rank.get(item.get("status", "OPEN"), 0))
        current_score = (SEVERITY_ORDER.get(current.get("severity", "INFO"), 0), status_rank.get(current.get("status", "OPEN"), 0))
        if incoming_score > current_score:
            selected[key] = item
        elif incoming_score == current_score:
            current_evidence = current.setdefault("evidence", [])
            seen = {json.dumps(e, sort_keys=True, ensure_ascii=False) for e in current_evidence}
            for evidence in item.get("evidence", []):
                encoded = json.dumps(evidence, sort_keys=True, ensure_ascii=False)
                if encoded not in seen:
                    current_evidence.append(evidence)
                    seen.add(encoded)
    return sorted(
        selected.values(),
        key=lambda f: (
            -SEVERITY_ORDER.get(f.get("severity", "INFO"), 0),
            f.get("category", ""),
            f.get("id", ""),
        ),
    )


def compute_gate(findings: Iterable[dict[str, Any]], checks: Iterable[dict[str, Any]], *, strict: bool = False) -> dict[str, Any]:
    findings = list(findings)
    checks = list(checks)
    unresolved = [f for f in findings if f.get("status") in {"OPEN", "NEEDS_REVIEW", "ERROR"}]
    blockers = [f for f in unresolved if f.get("severity") == "BLOCKER"]
    highs = [f for f in unresolved if f.get("severity") == "HIGH"]
    mediums = [f for f in unresolved if f.get("severity") == "MEDIUM"]
    mandatory_unverified = [
        c for c in checks if c.get("mandatory") and c.get("status") in {"SKIPPED", "NEEDS_REVIEW", "ERROR"}
    ]

    if blockers:
        state = "NOT READY"
        reasons = [f"{len(blockers)} open blocker finding(s)"]
    elif highs or mandatory_unverified or (strict and mediums):
        state = "CONDITIONALLY READY"
        reasons = []
        if highs:
            reasons.append(f"{len(highs)} open high-severity finding(s)")
        if mandatory_unverified:
            reasons.append(f"{len(mandatory_unverified)} mandatory check(s) unverified")
        if strict and mediums:
            reasons.append(f"{len(mediums)} open medium finding(s) under strict mode")
    else:
        state = "READY FOR SUBMISSION"
        reasons = ["No open blocker/high findings and no mandatory checks are unverified"]

    counts = {severity: 0 for severity in SEVERITIES}
    for finding in unresolved:
        severity = finding.get("severity", "INFO")
        counts[severity] = counts.get(severity, 0) + 1
    return {
        "state": state,
        "reasons": reasons,
        "unresolved_counts": counts,
        "mandatory_unverified": [c.get("id") for c in mandatory_unverified],
        "strict": bool(strict),
        "disclaimer": "Apple makes the final decision; this gate is evidence-based and does not guarantee approval.",
    }


def base_report(config: Mapping[str, Any], *, strict: bool = False) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "skill": {"name": "apple-app-store-reviewer", "version": SKILL_VERSION},
        "generated_at": now_iso(),
        "policy": {
            "baseline_date": POLICY_BASELINE,
            "guidelines_last_updated": GUIDELINES_LAST_UPDATED,
            "freshness": "NOT_CHECKED",
        },
        "app": redact(config.get("app", {})),
        "scope": redact(config.get("scope", {})),
        "inputs": {},
        "tools": [],
        "checks": [],
        "facts": {},
        "findings": [],
        "gate": {"state": "CONDITIONALLY READY", "strict": bool(strict)},
    }


def finalize_report(report: dict[str, Any], *, strict: bool = False) -> dict[str, Any]:
    report = redact(copy.deepcopy(report))
    report["findings"] = dedupe_findings(report.get("findings", []))
    report["checks"] = sorted(report.get("checks", []), key=lambda c: c.get("id", ""))
    report["gate"] = compute_gate(report["findings"], report["checks"], strict=strict)
    return report


def report_exit_code(report: Mapping[str, Any]) -> int:
    state = report.get("gate", {}).get("state")
    if state == "READY FOR SUBMISSION":
        return 0
    if state == "CONDITIONALLY READY":
        return 1
    if state == "NOT READY":
        return 2
    return 3


def markdown_report(report: Mapping[str, Any]) -> str:
    gate = report.get("gate", {})
    findings = list(report.get("findings", []))
    checks = list(report.get("checks", []))
    lines = [
        "# App Store preflight review",
        "",
        f"**Gate:** {gate.get('state', 'UNKNOWN')}",
        f"**Generated:** {report.get('generated_at', '')}",
        f"**Policy baseline:** {report.get('policy', {}).get('baseline_date', '')}",
        f"**Apple guideline update pinned:** {report.get('policy', {}).get('guidelines_last_updated', '')}",
        "",
        gate.get("disclaimer", ""),
        "",
        "## Gate reasons",
        "",
    ]
    for reason in gate.get("reasons", []):
        lines.append(f"- {reason}")
    lines.extend(["", "## Findings", ""])
    if not findings:
        lines.append("No findings were emitted.")
    for finding in findings:
        lines.extend(
            [
                f"### [{finding.get('severity')}] {finding.get('id')}: {finding.get('title')}",
                "",
                f"- **Status:** {finding.get('status')}",
                f"- **Confidence:** {finding.get('confidence')}",
                f"- **Category:** {finding.get('category')}",
                f"- **Guideline:** {finding.get('guideline')}",
                f"- **Automation:** {finding.get('automation')}",
                "",
                finding.get("rationale", ""),
                "",
                "**Evidence**",
                "",
            ]
        )
        for evidence in finding.get("evidence", []):
            loc = evidence.get("location", "")
            line = f":{evidence['line']}" if evidence.get("line") is not None else ""
            lines.append(f"- `{loc}{line}` — {evidence.get('detail', '')}")
        lines.extend(["", "**Remediation**", "", finding.get("remediation", ""), "", "**Verify**", ""])
        for step in finding.get("verification", []):
            lines.append(f"- {step}")
        if finding.get("sources"):
            lines.extend(["", "**Sources**", ""])
            for source in finding["sources"]:
                lines.append(f"- {source}")
        lines.append("")

    lines.extend(["## Check inventory", ""])
    for check in checks:
        mandatory = "mandatory" if check.get("mandatory") else "optional"
        lines.append(f"- `{check.get('id')}` — **{check.get('status')}** ({mandatory}): {check.get('detail', '')}")
    lines.extend(["", "## Tool inventory", ""])
    for tool in report.get("tools", []):
        lines.append(f"- `{tool.get('name', '')}` — {tool.get('status', '')}: {tool.get('detail', '')}")
    lines.append("")
    return "\n".join(lines)


def print_json(data: Any) -> None:
    sys.stdout.write(dump_json(data))
