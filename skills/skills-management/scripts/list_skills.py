#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""List all Claude Code skills from user and project scopes."""

import sys

if sys.version_info < (3, 11):
    sys.exit(
        f"{__file__} needs Python 3.11+, but runs on {sys.version.split()[0]}.\n"
        f"Run it with uv instead: uv run {__file__}"
    )

import argparse
import json

from claude_scopes import get_project_skills_dir, get_user_skills_dir, scope_dirs
from skill_md import skill_summary


def list_skills(scope: str | None = None, output_format: str = "text") -> list[dict]:
    """List skills from specified scope(s).

    Args:
        scope: "user", "project", or None for both
        output_format: "text", "json", or "table"

    Returns:
        List of skill info dicts
    """
    skills = []

    for scope_name, skills_dir in scope_dirs(scope):
        if not skills_dir.exists():
            continue

        for item in sorted(skills_dir.iterdir()):
            if item.is_dir() and (item / "SKILL.md").exists():
                metadata = skill_summary(item)
                if metadata:
                    skills.append({
                        "name": metadata["name"],
                        "directory": item.name,
                        "scope": scope_name,
                        "path": str(item),
                        "description": metadata["description"],
                    })

    return skills


def format_output(skills: list[dict], output_format: str) -> str:
    """Format skills list for output."""
    if output_format == "json":
        return json.dumps(skills, indent=2)

    if not skills:
        return "No skills found."

    if output_format == "table":
        # Simple table format
        lines = ["NAME | SCOPE | DESCRIPTION", "-" * 60]
        for s in skills:
            desc = s["description"][:40] + "..." if len(s["description"]) > 40 else s["description"]
            lines.append(f"{s['name']} | {s['scope']} | {desc}")
        return "\n".join(lines)

    # Default text format
    lines = []
    current_scope = None
    for s in skills:
        if s["scope"] != current_scope:
            if current_scope is not None:
                lines.append("")
            lines.append(f"=== {s['scope'].upper()} SKILLS ({get_user_skills_dir() if s['scope'] == 'user' else get_project_skills_dir()}) ===")
            current_scope = s["scope"]

        lines.append(f"\n  {s['name']}")
        if s["description"]:
            # Wrap description
            desc = s["description"]
            lines.append(f"    {desc[:80]}")
            if len(desc) > 80:
                lines.append(f"    {desc[80:160]}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="List Claude Code skills")
    parser.add_argument(
        "--scope", "-s",
        choices=["user", "project"],
        help="Filter by scope (default: show both)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["text", "json", "table"],
        default="text",
        help="Output format (default: text)"
    )
    args = parser.parse_args()

    skills = list_skills(args.scope, args.format)
    print(format_output(skills, args.format))

    return 0 if skills else 1


if __name__ == "__main__":
    sys.exit(main())
