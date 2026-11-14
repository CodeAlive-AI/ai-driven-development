#!/usr/bin/env python3
"""File and logging helpers shared by the SkillOpt scripts.

optimize_skill.py and blind_comparator.py write run artifacts; aggregate_runs.py and
eval_viewer.py read them back. Readers that tolerate damaged artifacts warn on stderr
instead of skipping them silently.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def log(msg: str) -> None:
    """Log to stderr so stdout stays clean for piping."""
    print(msg, file=sys.stderr, flush=True)


def approx_tokens(text: str) -> int:
    """Approximate token count (English-ish, ~4 chars/token)."""
    return len(text) // 4


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def load_jsonl(path: Path) -> list[dict]:
    """Rows of a JSONL input file; an invalid line raises ValueError naming it."""
    items: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for i, raw in enumerate(fh, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                items.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}: line {i}: invalid JSON: {exc}") from exc
    return items


def read_jsonl(path: Path) -> list[dict]:
    """Rows of a JSONL run artifact; invalid lines are skipped with a warning."""
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                log(f"  [warn] {path}: line {i}: invalid JSON ({exc})")
    return rows


def safe_read_text(path: Path) -> str | None:
    """Text of an optional artifact; None if it is missing or unreadable (with a warning)."""
    if not path.exists():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        log(f"  [warn] could not read {path}: {exc}")
        return None
