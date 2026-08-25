#!/usr/bin/env python3
"""Validate this Agent Skill package without requiring external tooling.

This complements, rather than replaces, ``skills-ref validate``. It checks the
portable Agent Skills contract plus package-specific integrity invariants that
are useful in CI and constrained agent runtimes.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from common import dump_json, now_iso, sha256_file

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCAL_REF_RE = re.compile(r"(?<![A-Za-z0-9_.-])((?:scripts|references|assets)/[A-Za-z0-9_./-]+)")
REQUIRED_FRONTMATTER = {"name", "description"}
STRING_FRONTMATTER = {"name", "description", "license", "compatibility", "allowed-tools"}


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        try:
            parsed = ast.literal_eval(value)
            return str(parsed)
        except (SyntaxError, ValueError):
            return value[1:-1]
    return value


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str, list[str]]:
    errors: list[str] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, ["SKILL.md must begin with YAML frontmatter delimited by ---"]
    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration:
        return {}, text, ["SKILL.md frontmatter has no closing --- delimiter"]

    front: dict[str, Any] = {}
    active_map: str | None = None
    for number, raw in enumerate(lines[1:end], start=2):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")):
            if active_map != "metadata":
                errors.append(f"line {number}: unexpected nested frontmatter field")
                continue
            nested = raw.strip()
            if ":" not in nested:
                errors.append(f"line {number}: malformed metadata entry")
                continue
            key, value = nested.split(":", 1)
            key = key.strip()
            if not key or not value.strip():
                errors.append(f"line {number}: metadata keys and values must be non-empty strings")
                continue
            metadata = front.setdefault("metadata", {})
            if key in metadata:
                errors.append(f"line {number}: duplicate metadata key {key!r}")
            metadata[key] = _unquote(value)
            continue

        active_map = None
        if ":" not in raw:
            errors.append(f"line {number}: malformed frontmatter field")
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        if key in front:
            errors.append(f"line {number}: duplicate frontmatter key {key!r}")
            continue
        if key == "metadata":
            if value.strip() not in {"", "{}"}:
                errors.append(f"line {number}: metadata must be a YAML mapping")
            front[key] = {}
            active_map = key
        else:
            front[key] = _unquote(value)
    return front, "\n".join(lines[end + 1 :]), errors


def validate_skill(root: str | Path) -> dict[str, Any]:
    root = Path(root).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    checks: list[dict[str, Any]] = []
    facts: dict[str, Any] = {"root": str(root)}

    skill_path = root / "SKILL.md"
    if not root.is_dir():
        errors.append(f"Skill directory does not exist: {root}")
        text = ""
        front: dict[str, Any] = {}
        body = ""
    elif not skill_path.is_file():
        errors.append("SKILL.md is missing")
        text = ""
        front = {}
        body = ""
    else:
        text = skill_path.read_text(encoding="utf-8")
        front, body, parse_errors = _parse_frontmatter(text)
        errors.extend(parse_errors)

    missing = sorted(REQUIRED_FRONTMATTER - set(front))
    errors.extend(f"Missing required frontmatter field: {field}" for field in missing)
    for key in STRING_FRONTMATTER & set(front):
        if not isinstance(front[key], str):
            errors.append(f"Frontmatter {key!r} must be a string")

    name = str(front.get("name", ""))
    description = str(front.get("description", ""))
    compatibility = front.get("compatibility")
    if name:
        if not 1 <= len(name) <= 64:
            errors.append("name must contain 1-64 characters")
        if not NAME_RE.fullmatch(name):
            errors.append("name must use lowercase a-z, 0-9, and single hyphens; it cannot start/end with a hyphen")
        if name != root.name:
            errors.append(f"name {name!r} must match parent directory {root.name!r}")
    if not 1 <= len(description) <= 1024:
        errors.append("description must contain 1-1024 characters")
    if compatibility is not None and not 1 <= len(str(compatibility)) <= 500:
        errors.append("compatibility must contain 1-500 characters when present")
    metadata = front.get("metadata")
    if metadata is not None:
        if not isinstance(metadata, dict):
            errors.append("metadata must be a mapping")
        else:
            for key, value in metadata.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    errors.append("metadata must map string keys to string values")
                    break

    line_count = len(text.splitlines()) if text else 0
    token_proxy = len(re.findall(r"\S+", body))
    facts.update({
        "name": name or None,
        "description_characters": len(description),
        "compatibility_characters": len(str(compatibility)) if compatibility is not None else 0,
        "skill_md_lines": line_count,
        "body_word_proxy": token_proxy,
    })
    if line_count > 500:
        warnings.append(f"SKILL.md has {line_count} lines; progressive-disclosure guidance recommends fewer than 500")
    if token_proxy > 5000:
        warnings.append(f"SKILL.md body has approximately {token_proxy} whitespace tokens; guidance recommends a compact core")

    refs = sorted({match.rstrip(".,;:)]}") for match in LOCAL_REF_RE.findall(text)})
    missing_refs: list[str] = []
    deep_refs: list[str] = []
    for ref in refs:
        target = (root / ref).resolve()
        try:
            target.relative_to(root)
        except ValueError:
            missing_refs.append(ref + " (escapes skill root)")
            continue
        if not target.exists():
            missing_refs.append(ref)
        if len(Path(ref).parts) > 2:
            deep_refs.append(ref)
    if missing_refs:
        errors.append("Referenced local files are missing: " + ", ".join(missing_refs))
    if deep_refs:
        warnings.append("Deep file references reduce progressive disclosure: " + ", ".join(deep_refs))
    facts["referenced_local_files"] = refs

    python_files = sorted((root / "scripts").glob("*.py")) if (root / "scripts").is_dir() else []
    compile_errors: list[str] = []
    non_executable: list[str] = []
    for path in python_files:
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except (SyntaxError, UnicodeError) as exc:
            compile_errors.append(f"{path.relative_to(root)}: {exc}")
        if path.read_bytes().startswith(b"#!") and not os.access(path, os.X_OK):
            non_executable.append(str(path.relative_to(root)))
    if compile_errors:
        errors.append("Python syntax errors: " + "; ".join(compile_errors))
    if non_executable:
        warnings.append("Shebang scripts are not executable: " + ", ".join(non_executable))

    json_files = sorted(path for path in root.rglob("*.json") if "__pycache__" not in path.parts)
    json_errors: list[str] = []
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeError) as exc:
            json_errors.append(f"{path.relative_to(root)}: {exc}")
    if json_errors:
        errors.append("Invalid JSON: " + "; ".join(json_errors))

    symlinks = [str(path.relative_to(root)) for path in root.rglob("*") if path.is_symlink()]
    if symlinks:
        warnings.append("Package contains symlinks; verify portability: " + ", ".join(symlinks))

    checks.extend([
        {"id": "skill.frontmatter", "status": "PASS" if not any("frontmatter" in item or item.startswith(("Missing required", "name ", "description ", "compatibility ", "metadata ")) for item in errors) else "FAIL"},
        {"id": "skill.references", "status": "PASS" if not missing_refs else "FAIL"},
        {"id": "skill.python-syntax", "status": "PASS" if not compile_errors else "FAIL"},
        {"id": "skill.json-syntax", "status": "PASS" if not json_errors else "FAIL"},
    ])
    file_hashes = {
        str(path.relative_to(root)): sha256_file(path)
        for path in sorted(root.rglob("*"))
        if path.is_file() and "__pycache__" not in path.parts
    } if root.is_dir() else {}
    facts.update({
        "python_files": len(python_files),
        "json_files": len(json_files),
        "symlinks": symlinks,
        "file_count": len(file_hashes),
        "package_sha256_manifest": file_hashes,
    })
    return {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "checks": checks,
        "facts": facts,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate Agent Skills frontmatter, references, scripts, JSON, and portability.")
    parser.add_argument("skill", nargs="?", default=str(Path(__file__).resolve().parents[1]), help="Skill root (default: this package)")
    parser.add_argument("--output", help="Write structured JSON result")
    parser.add_argument("--strict-warnings", action="store_true", help="Treat warnings as a non-zero result")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = validate_skill(args.skill)
    if args.output:
        dump_json(result, args.output)
    else:
        sys.stdout.write(dump_json(result))
    if not result["valid"]:
        return 2
    if args.strict_warnings and result["warnings"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
