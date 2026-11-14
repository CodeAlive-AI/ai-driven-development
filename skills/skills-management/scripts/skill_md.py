#!/usr/bin/env python3
"""SKILL.md parsing shared by every skills-management script.

One reader for the YAML frontmatter and the body, so install, audit, list, show and
review agree on a skill's ``name``. Stdlib only, so it covers the YAML subset that
SKILL.md files use rather than full YAML:

- top-level ``key: value`` pairs; a key ends at the first ``:`` followed by a space;
- plain values, with ``#`` comments after whitespace removed and indented
  continuation lines folded into one line with single spaces;
- single- and double-quoted values, which may also span lines;
- block scalars ``|`` (lines kept) and ``>`` (lines folded); chomping indicators
  are accepted, and every value is returned without a trailing line break;
- a nested block (a mapping or a list under a key with no value) is kept as its
  dedented source text, since a skill's metadata fields are read as strings.

The frontmatter is the text between a first line ``---`` and the next line that is
exactly ``---``; the body is what follows, without leading blank lines. A file without
frontmatter has no metadata and is all body. When a key repeats, the last one wins.
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_FILE = "SKILL.md"

_FRONTMATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)^---[ \t]*(?:\r?\n|\Z)", re.DOTALL | re.MULTILINE)
_KEY_RE = re.compile(r"^([A-Za-z_][\w.-]*)[ \t]*:[ \t]*(.*?)[ \t]*$")
_NESTED_KEY_RE = re.compile(r"^[A-Za-z_][\w.-]*[ \t]*:(?:[ \t]|$)")
_BLOCK_HEADER_RE = re.compile(r"^([|>])[+-]?[1-9]?[+-]?(?:[ \t]+#.*)?$")
_DOUBLE_QUOTE_ESCAPES = {
    "n": "\n", "t": "\t", "r": "\r", "0": "\0", '"': '"', "\\": "\\", "/": "/", " ": " ",
}


def split_frontmatter(content: str) -> tuple[str | None, str]:
    """Split SKILL.md text into (frontmatter text, body); frontmatter is None if absent."""
    match = _FRONTMATTER_RE.match(content)
    if not match:
        return None, content
    body = re.sub(r"\A(?:[ \t]*\r?\n)+", "", content[match.end():])
    return match.group(1), body


def extract_body(content: str) -> str:
    """Everything after the frontmatter, or the whole text if there is none."""
    return split_frontmatter(content)[1]


def parse_frontmatter(content: str) -> dict[str, str]:
    """Top-level frontmatter fields of SKILL.md text as strings ({} if none)."""
    frontmatter, _ = split_frontmatter(content)
    if frontmatter is None:
        return {}
    return _parse_mapping(frontmatter.splitlines())


def parse_skill_md(content: str) -> tuple[dict[str, str], str]:
    """(frontmatter fields, body) of SKILL.md text."""
    frontmatter, body = split_frontmatter(content)
    metadata = _parse_mapping(frontmatter.splitlines()) if frontmatter is not None else {}
    return metadata, body


def read_skill_text(skill_md: Path) -> str:
    """SKILL.md text; undecodable bytes are replaced, so every script reads the same name."""
    return skill_md.read_text(encoding="utf-8", errors="replace")


def read_skill_md(skill_dir: Path) -> tuple[dict[str, str], str] | None:
    """(fields, body) of ``skill_dir/SKILL.md``, or None if the directory has no SKILL.md."""
    skill_md = skill_dir / SKILL_FILE
    if not skill_md.is_file():
        return None
    return parse_skill_md(read_skill_text(skill_md))


def skill_name(metadata: dict[str, str], skill_dir: Path) -> str:
    """The frontmatter ``name``, or the directory name when the field is missing or empty."""
    return metadata.get("name", "").strip() or skill_dir.name


def skill_summary(skill_dir: Path) -> dict[str, str] | None:
    """``name`` and ``description`` for skill listings, or None without SKILL.md.

    A listing shows one unreadable or frontmatter-less skill in place instead of failing.
    """
    skill_md = skill_dir / SKILL_FILE
    if not skill_md.is_file():
        return None
    try:
        frontmatter, _ = split_frontmatter(read_skill_text(skill_md))
    except OSError as exc:
        return {"name": skill_dir.name, "description": f"(error reading: {exc})"}
    if frontmatter is None:
        return {"name": skill_dir.name, "description": "(no frontmatter)"}
    metadata = _parse_mapping(frontmatter.splitlines())
    return {"name": skill_name(metadata, skill_dir), "description": metadata.get("description", "")}


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _parse_mapping(lines: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    index = 0
    while index < len(lines):
        line = lines[index]
        index += 1
        if not line.strip() or line.lstrip().startswith("#") or line[0] in " \t":
            continue
        match = _KEY_RE.match(line)
        if not match:
            continue
        key, value = match.group(1), match.group(2)
        block: list[str] = []
        while index < len(lines) and (not lines[index].strip() or lines[index][0] in " \t"):
            block.append(lines[index])
            index += 1
        while block and not block[-1].strip():
            block.pop()
        result[key] = _parse_value(value, block).rstrip("\n")
    return result


def _parse_value(value: str, block: list[str]) -> str:
    if value.startswith("#"):
        value = ""
    header = _BLOCK_HEADER_RE.match(value)
    if header:
        return _block_scalar(block, folded=header.group(1) == ">")
    if not value and block:
        first = next(line for line in block if line.strip()).strip()
        if first.startswith("- ") or first == "-" or _NESTED_KEY_RE.match(first):
            return _dedent(block)
        if first[:1] in ("'", '"'):
            return _quoted(" ".join(line.strip() for line in block if line.strip()))
    if value[:1] in ("'", '"'):
        return _quoted(" ".join([value, *(line.strip() for line in block)]) if block else value)
    return _plain(value, block)


def _plain(value: str, block: list[str]) -> str:
    parts = [_strip_comment(value)] if value else []
    for line in block:
        text = line.strip()
        if text.startswith("#"):
            break
        parts.append(_strip_comment(text) if text else "\n")
    return _fold(parts)


def _strip_comment(text: str) -> str:
    return re.split(r"[ \t]+#", text, maxsplit=1)[0].rstrip()


def _fold(parts: list[str]) -> str:
    """Join line fragments with spaces; an empty line becomes a newline."""
    out = ""
    for part in parts:
        if part == "\n":
            out = out.rstrip(" ") + "\n"
        elif not out or out.endswith("\n"):
            out += part
        else:
            out += " " + part
    return out.strip()


def _quoted(text: str) -> str:
    quote = text[0]
    end = _closing_quote(text, quote)
    if end is None:
        return text
    inner = text[1:end]
    if quote == "'":
        return inner.replace("''", "'")
    return re.sub(r"\\(.)", lambda m: _DOUBLE_QUOTE_ESCAPES.get(m.group(1), m.group(0)), inner)


def _closing_quote(text: str, quote: str) -> int | None:
    index = 1
    while index < len(text):
        char = text[index]
        if quote == '"' and char == "\\":
            index += 2
            continue
        if char == quote:
            if quote == "'" and text[index + 1:index + 2] == "'":
                index += 2
                continue
            return index
        index += 1
    return None


def _dedent(block: list[str]) -> str:
    indent = min(_indent(line) for line in block if line.strip())
    return "\n".join(line[indent:] for line in block)


def _block_scalar(block: list[str], folded: bool) -> str:
    if not block:
        return ""
    indent = min(_indent(line) for line in block if line.strip())
    lines = [line[indent:] if line.strip() else "" for line in block]
    if not folded:
        text = "\n".join(lines)
    else:
        text = ""
        previous_more_indented = False
        for i, line in enumerate(lines):
            more_indented = line[:1] in (" ", "\t")
            if i == 0:
                text = line
            elif not line:
                text += "\n"
            elif text.endswith("\n") or more_indented or previous_more_indented:
                text += ("" if text.endswith("\n") else "\n") + line
            else:
                text += " " + line
            previous_more_indented = more_indented
    return text.rstrip("\n")
