#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Move a skill between AI coding agents."""

import sys

if sys.version_info < (3, 11):
    sys.exit(
        f"{__file__} needs Python 3.11+, but runs on {sys.version.split()[0]}.\n"
        f"Run it with uv instead: uv run {__file__}"
    )

import argparse
from pathlib import Path

from fs_ops import move_into_place, path_present, same_location
from agents import (
    agents_sharing_dir,
    AGENTS,
    find_skill_in_agent,
    get_agent_config,
    get_skills_dir,
    validate_agent,
)


def move_skill(
    name: str,
    from_agent: str,
    to_agent: str,
    from_scope: str | None = None,
    to_scope: str = "project",
    force: bool = False,
    cwd: Path | None = None
) -> tuple[bool, str]:
    """Move a skill from one agent to another.

    Args:
        name: Skill name (directory name)
        from_agent: Source agent ID
        to_agent: Target agent ID
        from_scope: Source scope (None to auto-detect)
        to_scope: Target scope
        force: Overwrite if exists
        cwd: Working directory for project scope

    Returns:
        Tuple of (success, message)
    """
    # Find source skill
    source_path, found_scope = find_skill_in_agent(name, from_agent, from_scope, cwd)
    if not source_path:
        scope_msg = f" in {from_scope} scope" if from_scope else ""
        return False, f"Skill '{name}' not found in {from_agent}{scope_msg}"

    # Get target path
    target_base = get_skills_dir(to_agent, to_scope, cwd)
    if not target_base:
        return False, f"Could not determine skills directory for {to_agent}"

    target_path = target_base / name

    if path_present(target_path) and same_location(source_path, target_path):
        return False, (
            f"Source and target are the same directory ({source_path.resolve()}); "
            "one of them is a symlink to the other, so there is nothing to do."
        )

    if path_present(target_path) and not force:
        return False, f"Skill '{name}' already exists at {target_path}. Use --force to overwrite."

    # Move (copy + delete)
    try:
        sharing = [a for a in agents_sharing_dir(source_path.parent, cwd) if a != from_agent]
        kind = "symlink" if source_path.is_symlink() else "directory"
        move_into_place(source_path, target_path)

        from_config = get_agent_config(from_agent)
        to_config = get_agent_config(to_agent)

        return True, (
            f"Moved '{name}': {from_config['display_name']} ({found_scope}) -> "
            f"{to_config['display_name']} ({to_scope})\n"
            f"  From: {source_path} (removed)\n"
            f"  To:   {target_path} ({kind})"
            + (
                f"\n  Note: {source_path.parent} is shared, so the skill is also gone for: "
                + ", ".join(sharing)
                if sharing else ""
            )
        )
    except Exception as e:
        return False, f"Error moving skill: {e}"


def main():
    parser = argparse.ArgumentParser(
        description="Move a skill between AI coding agents"
    )
    parser.add_argument(
        "name",
        help="Name of the skill to move (directory name)"
    )
    parser.add_argument(
        "--from",
        dest="from_agent",
        required=True,
        help="Source agent ID (e.g., claude-code)"
    )
    parser.add_argument(
        "--to",
        dest="to_agent",
        required=True,
        help="Target agent ID (e.g., cursor)"
    )
    parser.add_argument(
        "--from-scope",
        choices=["project", "global"],
        help="Source scope (default: auto-detect)"
    )
    parser.add_argument(
        "--to-scope",
        choices=["project", "global"],
        default="project",
        help="Target scope (default: project)"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Overwrite if skill exists in target"
    )
    args = parser.parse_args()

    # Validate agents
    if not validate_agent(args.from_agent):
        print(f"Error: Unknown source agent '{args.from_agent}'")
        print(f"Valid agents: {', '.join(sorted(AGENTS.keys()))}")
        return 1

    if not validate_agent(args.to_agent):
        print(f"Error: Unknown target agent '{args.to_agent}'")
        print(f"Valid agents: {', '.join(sorted(AGENTS.keys()))}")
        return 1

    # Move skill
    success, message = move_skill(
        args.name,
        args.from_agent,
        args.to_agent,
        args.from_scope,
        args.to_scope,
        args.force
    )

    print(message)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
