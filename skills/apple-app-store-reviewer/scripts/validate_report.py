#!/usr/bin/env python3
"""Validate structural and semantic invariants of a preflight report."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping

from common import (
    SECRET_KEY_RE,
    SECRET_VALUE_RES,
    ReviewInputError,
    compute_gate,
    dump_json,
    load_json,
)

DEFAULT_SCHEMA = Path(__file__).resolve().parents[1] / "assets" / "review-report.schema.json"


def _schema_errors(report: Any, schema: Mapping[str, Any]) -> tuple[list[str], str]:
    try:
        import jsonschema
    except ImportError:
        return [], "jsonschema unavailable; semantic validation only"
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(report), key=lambda item: list(item.absolute_path)):
        pointer = "/" + "/".join(str(part) for part in error.absolute_path)
        errors.append(f"{pointer or '/'}: {error.message}")
    return errors, "jsonschema"


def _walk(value: Any, pointer: str = "") -> Iterable[tuple[str, str | None, Any]]:
    if isinstance(value, Mapping):
        for key, child in value.items():
            child_pointer = f"{pointer}/{key}"
            yield child_pointer, str(key), child
            yield from _walk(child, child_pointer)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            child_pointer = f"{pointer}/{index}"
            yield child_pointer, None, child
            yield from _walk(child, child_pointer)


def _secret_errors(report: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    allowed_secret_keys = {"username_env", "password_env", "token_env", "api_key_env", "credential_env"}
    for pointer, key, value in _walk(report):
        if key and SECRET_KEY_RE.search(key) and key.casefold() not in allowed_secret_keys:
            if value not in (None, "", "<redacted>"):
                # Descriptive keys such as "secrets_detected" contain counts/booleans,
                # not credentials. Only reject string-like material.
                if isinstance(value, str) and not value.startswith("<redacted"):
                    errors.append(f"{pointer}: possible credential stored under a secret-shaped key")
        if isinstance(value, str):
            for pattern in SECRET_VALUE_RES:
                if pattern.search(value):
                    errors.append(f"{pointer}: possible unredacted credential-shaped value")
                    break
            if "-----BEGIN PRIVATE KEY-----" in value or "-----BEGIN RSA PRIVATE KEY-----" in value:
                errors.append(f"{pointer}: private key material is forbidden")
    return sorted(set(errors))


def validate_report(report: Mapping[str, Any], *, schema_path: str | Path = DEFAULT_SCHEMA, strict: bool = False) -> dict[str, Any]:
    schema = load_json(schema_path)
    if not isinstance(schema, Mapping):
        raise ReviewInputError("Report schema root must be an object")
    schema_errors, schema_engine = _schema_errors(report, schema)
    semantic_errors: list[str] = []
    warnings: list[str] = []

    for collection in ("findings", "checks"):
        ids = [str(item.get("id", "")) for item in report.get(collection, []) if isinstance(item, Mapping)]
        duplicates = sorted({item for item in ids if ids.count(item) > 1})
        if duplicates:
            semantic_errors.append(f"/{collection}: duplicate IDs: {', '.join(duplicates)}")

    expected_gate = compute_gate(report.get("findings", []), report.get("checks", []), strict=bool(report.get("gate", {}).get("strict", strict)))
    actual_state = report.get("gate", {}).get("state")
    if actual_state != expected_gate["state"]:
        semantic_errors.append(f"/gate/state: {actual_state!r} does not match computed {expected_gate['state']!r}")
    if sorted(report.get("gate", {}).get("mandatory_unverified", [])) != sorted(expected_gate["mandatory_unverified"]):
        semantic_errors.append("/gate/mandatory_unverified: does not match mandatory check inventory")

    ready = actual_state == "READY FOR SUBMISSION"
    freshness = report.get("policy", {}).get("freshness")
    if ready and freshness != "CURRENT":
        semantic_errors.append("/policy/freshness: READY FOR SUBMISSION requires CURRENT")
    if ready and not report.get("findings") and not report.get("checks"):
        semantic_errors.append("/: an empty report cannot be READY FOR SUBMISSION")

    for index, finding in enumerate(report.get("findings", [])):
        if not isinstance(finding, Mapping):
            continue
        pointer = f"/findings/{index}"
        if finding.get("status") in {"OPEN", "NEEDS_REVIEW", "ERROR"} and not finding.get("evidence"):
            semantic_errors.append(f"{pointer}/evidence: unresolved finding requires evidence")
        if not finding.get("sources"):
            warnings.append(f"{pointer}/sources: no source is recorded")
        if finding.get("confidence") == "CERTAIN" and finding.get("automation") in {"heuristic", "community-signal"}:
            semantic_errors.append(f"{pointer}/confidence: heuristic/community evidence cannot be CERTAIN")
        if finding.get("severity") == "BLOCKER" and finding.get("confidence") == "LOW":
            warnings.append(f"{pointer}: low-confidence blocker should be recalibrated or verified")
        if any("reddit.com" in str(source) or "x.com" in str(source) for source in finding.get("sources", [])):
            if finding.get("automation") != "community-signal" and "community" not in set(finding.get("tags", [])):
                warnings.append(f"{pointer}: community source should be labeled anecdotal/community")

    for index, check in enumerate(report.get("checks", [])):
        if not isinstance(check, Mapping):
            continue
        if check.get("mandatory") and check.get("status") == "PASS" and not check.get("detail"):
            warnings.append(f"/checks/{index}: mandatory PASS has no detail")

    secret_errors = _secret_errors(report)
    semantic_errors.extend(secret_errors)

    if strict:
        for index, finding in enumerate(report.get("findings", [])):
            if isinstance(finding, Mapping) and finding.get("status") in {"OPEN", "NEEDS_REVIEW", "ERROR"} and finding.get("severity") == "MEDIUM":
                warnings.append(f"/findings/{index}: strict mode leaves an open MEDIUM finding")

    errors = schema_errors + semantic_errors
    return {
        "valid": not errors,
        "schema_engine": schema_engine,
        "schema_path": str(Path(schema_path).resolve()),
        "errors": errors,
        "warnings": sorted(set(warnings)),
        "computed_gate": expected_gate,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a review-output/report.json against schema and gate invariants.")
    parser.add_argument("report", help="Path to report.json")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA), help="Report JSON Schema")
    parser.add_argument("--strict", action="store_true", help="Enable strict consistency warnings")
    parser.add_argument("--output", help="Write validation result JSON to this file")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        report = load_json(args.report)
        if not isinstance(report, Mapping):
            raise ReviewInputError("Report root must be a JSON object")
        result = validate_report(report, schema_path=args.schema, strict=args.strict)
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"validate_report: {exc}\n")
        return 3
    if args.output:
        dump_json(result, args.output)
    else:
        sys.stdout.write(dump_json(result))
    return 0 if result["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
