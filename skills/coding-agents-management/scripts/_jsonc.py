#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Shared JSON / JSONC / UTF-8 BOM parsing helpers for config validators."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def strip_jsonc(raw: str) -> str:
    """Strip UTF-8 BOM, // and /* */ comments, and trailing commas from JSONC."""
    if raw.startswith("\ufeff"):
        raw = raw[1:]

    out: list[str] = []
    i = 0
    n = len(raw)
    in_str = False
    escaped = False

    while i < n:
        ch = raw[i]
        if in_str:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_str = False
            i += 1
            continue

        if ch == '"':
            in_str = True
            out.append(ch)
            i += 1
        elif raw.startswith("//", i):
            nl = raw.find("\n", i)
            i = n if nl == -1 else nl
        elif raw.startswith("/*", i):
            end = raw.find("*/", i + 2)
            if end == -1:
                break
            i = end + 2
        else:
            out.append(ch)
            i += 1

    text = "".join(out)
    # Remove trailing commas outside strings safely via character scan
    cleaned: list[str] = []
    i = 0
    m = len(text)
    in_str = False
    escaped = False
    while i < m:
        ch = text[i]
        if in_str:
            cleaned.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_str = False
            i += 1
            continue
        if ch == '"':
            in_str = True
            cleaned.append(ch)
            i += 1
            continue
        if ch == ",":
            j = i + 1
            while j < m and text[j] in " \t\r\n":
                j += 1
            if j < m and text[j] in "}]":
                i += 1
                continue
        cleaned.append(ch)
        i += 1

    return "".join(cleaned)


def load_jsonc(path: Path) -> Any:
    """Read and parse a JSON or JSONC file (handling UTF-8 BOM)."""
    content = path.read_text(encoding="utf-8-sig")
    if not content.strip():
        return {}
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return json.loads(strip_jsonc(content))


def is_kebab_case(name: str) -> bool:
    """Return True if name is valid lowercase kebab-case without consecutive dashes."""
    if not name or "--" in name:
        return False
    return bool(re.match(r"^[a-z][a-z0-9-]*[a-z0-9]$|^[a-z]$", name))
