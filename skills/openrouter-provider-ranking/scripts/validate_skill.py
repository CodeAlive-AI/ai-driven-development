#!/usr/bin/env python3
"""Validate the bundled Agent Skill without third-party dependencies."""

from __future__ import annotations

import json
import py_compile
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def fail(message: str) -> None:
    raise ValueError(message)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        _, raw, body = text.split("---", 2)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, body.strip()


def validate_skill() -> list[str]:
    checks: list[str] = []
    text = SKILL.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    name = fields.get("name", "")
    description = fields.get("description", "")
    compatibility = fields.get("compatibility", "")

    if name != ROOT.name:
        fail(f"frontmatter name {name!r} must match directory {ROOT.name!r}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("name must contain lowercase letters, digits, and single hyphens only")
    if not 1 <= len(name) <= 64:
        fail("name must be 1..64 characters")
    if not 1 <= len(description) <= 1024:
        fail("description must be 1..1024 characters")
    if compatibility and len(compatibility) > 500:
        fail("compatibility must be at most 500 characters")
    if not body:
        fail("SKILL.md body is empty")
    if len(text.splitlines()) >= 500:
        fail("SKILL.md must remain under 500 lines")
    checks.append("frontmatter and SKILL.md size")

    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        if "://" in target or target.startswith("#"):
            continue
        resolved = ROOT / target
        if not resolved.exists():
            fail(f"broken relative link in SKILL.md: {target}")
    checks.append("relative file links")

    json_files = [
        ROOT / "assets" / "config.example.json",
        ROOT / "assets" / "observations.example.json",
        ROOT / "tests" / "fixture-endpoints.json",
        ROOT / "tests" / "fixture-observations.json",
        ROOT / "tests" / "trigger-evals.json",
    ]
    parsed = {}
    for path in json_files:
        parsed[path.name] = json.loads(path.read_text(encoding="utf-8"))
    evals = parsed["trigger-evals.json"]
    if not isinstance(evals, list) or len(evals) < 16:
        fail("trigger-evals.json must contain at least 16 queries")
    labels = {item.get("should_trigger") for item in evals if isinstance(item, dict)}
    if labels != {True, False}:
        fail("trigger evals must include positive and negative examples")
    checks.append("JSON assets and trigger evals")

    ranker = ROOT / "scripts" / "rank_providers.py"
    py_compile.compile(str(ranker), doraise=True)
    checks.append("ranker syntax")

    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        sys.stderr.write(completed.stdout)
        sys.stderr.write(completed.stderr)
        fail("unit tests failed")
    checks.append("unit tests")
    return checks


def main() -> int:
    try:
        checks = validate_skill()
    except (OSError, ValueError, json.JSONDecodeError, py_compile.PyCompileError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    print("Validation passed:")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
