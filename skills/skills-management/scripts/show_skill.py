#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Show detailed information about an Agent Skill."""

import sys

if sys.version_info < (3, 11):
    sys.exit(
        f"{__file__} needs Python 3.11+, but runs on {sys.version.split()[0]}.\n"
        f"Run it with uv instead: uv run {__file__}"
    )

import argparse
import json
import os
from pathlib import Path

from agents import resolve_skill
from skill_md import extract_body, parse_frontmatter, read_skill_text


def get_skill_info(skill_path: Path, scope: str) -> dict:
    """Get comprehensive information about a skill."""
    skill_md = skill_path / "SKILL.md"
    content = read_skill_text(skill_md)

    # Parse frontmatter
    metadata = parse_frontmatter(content)

    body = extract_body(content).strip()

    # Count body lines/words
    body_lines = len(body.split("\n"))
    body_words = len(body.split())

    # Get directory structure
    files = []
    dirs = set()
    total_size = 0

    for item in skill_path.rglob("*"):
        rel_path = item.relative_to(skill_path)
        if item.is_file():
            size = item.stat().st_size
            total_size += size
            files.append({
                "path": str(rel_path),
                "size": size,
                "type": item.suffix or "(no extension)"
            })
        elif item.is_dir():
            dirs.add(str(rel_path))

    # Check for standard directories
    has_scripts = (skill_path / "scripts").exists()
    has_references = (skill_path / "references").exists()
    has_assets = (skill_path / "assets").exists()

    is_symlink = skill_path.is_symlink()
    symlink_target = os.readlink(skill_path) if is_symlink else None

    return {
        "name": metadata.get("name", skill_path.name),
        "directory": skill_path.name,
        "scope": scope,
        "path": str(skill_path),
        "is_symlink": is_symlink,
        "symlink_target": symlink_target,
        "description": metadata.get("description", ""),
        "metadata": metadata,
        "body_lines": body_lines,
        "body_words": body_words,
        "file_count": len(files),
        "total_size": total_size,
        "files": files,
        "directories": list(dirs),
        "has_scripts": has_scripts,
        "has_references": has_references,
        "has_assets": has_assets,
    }


def format_size(size: int) -> str:
    """Format size in human-readable form."""
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    else:
        return f"{size / (1024 * 1024):.1f} MB"


def show_skill(
    name: str | None = None,
    scope: str | None = None,
    output_format: str = "text",
    show_files: bool = False,
    *,
    agent: str | None = None,
    path: Path | str | None = None,
) -> bool:
    """Show information about a skill.

    Args:
        name: Skill name
        scope: Optional scope filter
        output_format: "text" or "json"
        show_files: Include file listing
        agent: Optional agent ID
        path: Explicit skill directory or SKILL.md path

    Returns:
        True if skill found, False otherwise
    """
    skill_path, found_scope, error = resolve_skill(
        name,
        agent=agent,
        scope=scope,
        path=Path(path) if path is not None else None,
    )

    if not skill_path:
        print(f"Error: {error or f'Skill {name!r} not found.'}")
        return False

    try:
        info = get_skill_info(skill_path, found_scope or "unknown")
        if agent:
            info["agent"] = agent
    except Exception as e:
        print(f"Error reading skill: {e}")
        return False

    if output_format == "json":
        print(json.dumps(info, indent=2))
        return True

    # Text format
    print(f"{'=' * 60}")
    print(f"Skill: {info['name']}")
    print(f"{'=' * 60}")
    if agent:
        print(f"Agent:       {agent}")
    print(f"Scope:       {info['scope']}")
    print(f"Path:        {info['path']}")
    if info["is_symlink"]:
        print(f"Symlink:     -> {info['symlink_target']}")
    print("")
    print("Description:")
    print(f"  {info['description']}")
    print("")

    # Metadata
    if info['metadata']:
        other_meta = {k: v for k, v in info['metadata'].items() if k not in ('name', 'description')}
        if other_meta:
            print("Other Metadata:")
            for k, v in other_meta.items():
                print(f"  {k}: {v}")
            print("")

    # Stats
    print("Statistics:")
    print(f"  SKILL.md body: {info['body_lines']} lines, {info['body_words']} words")
    print(f"  Total files:   {info['file_count']}")
    print(f"  Total size:    {format_size(info['total_size'])}")
    print("")

    # Structure
    print("Structure:")
    print(f"  scripts/:    {'Yes' if info['has_scripts'] else 'No'}")
    print(f"  references/: {'Yes' if info['has_references'] else 'No'}")
    print(f"  assets/:     {'Yes' if info['has_assets'] else 'No'}")

    if show_files and info['files']:
        print("")
        print("Files:")
        for f in sorted(info['files'], key=lambda x: x['path']):
            print(f"  {f['path']} ({format_size(f['size'])})")

    return True


def main():
    parser = argparse.ArgumentParser(description="Show information about an Agent Skill")
    parser.add_argument("name", nargs="?", help="Name of the skill to show")
    parser.add_argument(
        "--agent", "-a",
        help="Agent ID whose scopes to search (e.g., antigravity, cursor, codex)"
    )
    parser.add_argument(
        "--path", "-p",
        help="Explicit path to a skill directory or SKILL.md"
    )
    parser.add_argument(
        "--scope", "-s",
        choices=["user", "global", "project"],
        help="Scope to search (default: search both)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )
    parser.add_argument(
        "--files",
        action="store_true",
        help="Include file listing"
    )
    args = parser.parse_args()

    if not args.name and not args.path:
        parser.error("Either skill name or --path is required")

    success = show_skill(
        args.name,
        args.scope,
        args.format,
        args.files,
        agent=args.agent,
        path=args.path,
    )
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
