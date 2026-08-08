#!/usr/bin/env python3
"""Extract and strictly validate a Consilium judge verdict document."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ALLOWED_VERDICTS = {"VALID", "DUPLICATE", "FALSE_POSITIVE", "DOWNGRADE"}
ALLOWED_SEVERITIES = {"critical", "high", "medium", "low"}


def fail(message: str) -> None:
    raise ValueError(message)


def extract_json(raw: str) -> Any:
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    candidate = fence.group(1) if fence else raw
    if not fence:
        start = candidate.find("{")
        if start < 0:
            fail("no JSON object found in judge output")
        depth = 0
        in_string = False
        escaped = False
        end = None
        for index, char in enumerate(candidate[start:], start=start):
            if in_string:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    in_string = False
                continue
            if char == '"':
                in_string = True
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end = index + 1
                    break
        if end is None:
            fail("unbalanced braces in judge output")
        candidate = candidate[start:end]
    try:
        return json.loads(candidate)
    except Exception as exc:
        fail(f"json parse failed: {exc}")


def validate(obj: Any, findings_text: str) -> dict[str, Any]:
    if not isinstance(obj, dict):
        fail("judge output must be a JSON object")
    finding_indices = [
        int(value)
        for value in re.findall(r'<finding\b[^>]*\bindex="(\d+)"', findings_text)
    ]
    expected = set(finding_indices)
    finding_severity: dict[int, str] = {}
    for attributes in re.findall(r"<finding\b([^>]*)>", findings_text):
        parsed = dict(re.findall(r'(\w[\w-]*)\s*=\s*"([^"]*)"', attributes))
        try:
            index = int(parsed.get("index", ""))
        except ValueError:
            continue
        severity = parsed.get("severity", "").lower()
        if severity:
            finding_severity[index] = severity
    if len(expected) != len(finding_indices):
        fail("findings input contains duplicate indices")
    if not isinstance(obj.get("total_findings_parsed"), int):
        fail("judge output missing integer total_findings_parsed")
    if obj["total_findings_parsed"] != len(finding_indices):
        fail("judge total_findings_parsed does not match input")
    verdicts = obj.get("verdicts")
    if not isinstance(verdicts, list):
        fail("judge output missing verdicts array")

    seen: set[int] = set()
    counts = {"valid": 0, "duplicate": 0, "false_positive": 0, "downgrade": 0}
    kept: list[int] = []
    verdict_by_index: dict[int, dict[str, Any]] = {}
    for position, verdict in enumerate(verdicts):
        if not isinstance(verdict, dict):
            fail(f"verdict {position} is not an object")
        index = verdict.get("finding_idx")
        kind = verdict.get("verdict")
        if not isinstance(index, int) or index not in expected or index in seen:
            fail(f"invalid or duplicate finding_idx: {index!r}")
        if kind not in ALLOWED_VERDICTS:
            fail(f"invalid verdict for finding {index}: {kind!r}")
        rationale = verdict.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            fail(f"missing rationale for finding {index}")
        if kind == "DUPLICATE":
            duplicate_of = verdict.get("duplicate_of")
            if (
                not isinstance(duplicate_of, int)
                or duplicate_of not in expected
                or duplicate_of == index
            ):
                fail(f"invalid duplicate_of for finding {index}")
        if kind == "DOWNGRADE" and verdict.get("new_severity") not in ALLOWED_SEVERITIES:
            fail(f"invalid new_severity for finding {index}")
        if kind == "DOWNGRADE":
            order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
            old = finding_severity.get(index)
            new = verdict.get("new_severity")
            if old not in order or order[new] <= order[old]:
                fail(f"new_severity does not downgrade finding {index}")
        seen.add(index)
        verdict_by_index[index] = verdict
        counts[kind.lower()] += 1
        if kind in {"VALID", "DOWNGRADE"}:
            kept.append(index)

    if seen != expected:
        fail(f"judge omitted findings: {sorted(expected - seen)}")
    for index, verdict in verdict_by_index.items():
        if verdict["verdict"] != "DUPLICATE":
            continue
        canonical = verdict["duplicate_of"]
        canonical_verdict = verdict_by_index.get(canonical, {}).get("verdict")
        if canonical >= index or canonical_verdict not in {"VALID", "DOWNGRADE"}:
            fail(f"duplicate_of for finding {index} is not a prior kept finding")
    summary = obj.get("summary")
    if not isinstance(summary, dict):
        fail("judge output missing summary object")
    for key, value in counts.items():
        if summary.get(key) != value:
            fail(f"judge summary count mismatch for {key}")
    summary_kept = summary.get("kept_findings_idx")
    if (
        not isinstance(summary_kept, list)
        or any(not isinstance(index, int) for index in summary_kept)
        or len(summary_kept) != len(set(summary_kept))
        or set(summary_kept) != set(kept)
    ):
        fail("judge kept_findings_idx mismatch")
    return obj


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-output", required=True)
    parser.add_argument("--findings", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    try:
        obj = extract_json(Path(args.raw_output).read_text(encoding="utf-8"))
        validated = validate(
            obj,
            Path(args.findings).read_text(encoding="utf-8", errors="replace"),
        )
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    Path(args.out).write_text(json.dumps(validated, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
