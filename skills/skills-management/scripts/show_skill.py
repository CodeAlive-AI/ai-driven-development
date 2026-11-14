#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Show detailed information about a Claude Code skill."""

import sys

if sys.version_info < (3, 11):
    sys.exit(
        f"{__file__} needs Python 3.11+, but runs on {sys.version.split()[0]}.\n"
        f"Run it with uv instead: uv run {__file__}"
    )

import argparse
import json
from pathlib import Path

from claude_scopes import find_skill
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

    return {
        "name": metadata.get("name", skill_path.name),
        "directory": skill_path.name,
        "scope": scope,
        "path": str(skill_path),
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


def show_skill(name: str, scope: str | None = None, output_format: str = "text", show_files: bool = False) -> bool:
    """Show information about a skill.

    Args:
        name: Skill name
        scope: Optional scope filter
        output_format: "text" or "json"
        show_files: Include file listing

    Returns:
        True if skill found, False otherwise
    """
    skill_path, found_scope = find_skill(name, scope)

    if not skill_path:
        if scope:
            print(f"Error: Skill '{name}' not found in {scope} scope.")
        else:
            print(f"Error: Skill '{name}' not found in user or project scope.")
        return False

    try:
        info = get_skill_info(skill_path, found_scope)
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
    print(f"Scope:       {info['scope']}")
    print(f"Path:        {info['path']}")
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
    parser = argparse.ArgumentParser(description="Show information about a Claude Code skill")
    parser.add_argument("name", help="Name of the skill to show")
    parser.add_argument(
        "--scope", "-s",
        choices=["user", "project"],
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

    success = show_skill(args.name, args.scope, args.format, args.files)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
