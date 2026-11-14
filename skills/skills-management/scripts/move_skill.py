#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Move a Claude Code skill between user and project scopes."""

import sys

if sys.version_info < (3, 11):
    sys.exit(
        f"{__file__} needs Python 3.11+, but runs on {sys.version.split()[0]}.\n"
        f"Run it with uv instead: uv run {__file__}"
    )

import argparse
from pathlib import Path

from fs_ops import move_into_place, path_present, same_location


def get_user_skills_dir() -> Path:
    """Get the user-level skills directory."""
    return Path.home() / ".claude" / "skills"


def get_project_skills_dir() -> Path:
    """Get the project-level skills directory (current working directory)."""
    return Path.cwd() / ".claude" / "skills"


def find_skill(name: str) -> tuple[Path | None, str | None]:
    """Find a skill by name in either scope.

    Returns:
        Tuple of (skill_path, scope_name) or (None, None) if not found
    """
    for scope_name, skills_dir in [("user", get_user_skills_dir()), ("project", get_project_skills_dir())]:
        skill_path = skills_dir / name
        if skill_path.is_symlink() or (skill_path / "SKILL.md").exists():
            return skill_path, scope_name
    return None, None


def move_skill(name: str, to_scope: str, force: bool = False) -> bool:
    """Move a skill to a different scope.

    Args:
        name: Skill name (directory name)
        to_scope: Target scope ("user" or "project")
        force: Overwrite if exists in target scope

    Returns:
        True if moved, False otherwise
    """
    skill_path, from_scope = find_skill(name)

    if not skill_path:
        print(f"Error: Skill '{name}' not found in user or project scope.")
        return False

    if from_scope == to_scope:
        print(f"Skill '{name}' is already in {to_scope} scope; nothing to do.")
        return True

    # Determine target path
    if to_scope == "user":
        target_dir = get_user_skills_dir()
    else:
        target_dir = get_project_skills_dir()

    target_path = target_dir / name

    if path_present(target_path) and same_location(skill_path, target_path):
        print(f"Error: '{skill_path}' and '{target_path}' are the same directory "
              f"({target_path.resolve()}); one is a symlink to the other.")
        link_scope = from_scope if skill_path.is_symlink() else to_scope
        print(f"To drop the alias, delete the symlink instead: "
              f"uv run scripts/delete_skill.py {name} -s {link_scope} --force")
        return False

    if path_present(target_path):
        if not force:
            print(f"Error: Skill '{name}' already exists in {to_scope} scope.")
            print("Use --force to overwrite.")
            return False
        print(f"Overwriting existing skill in {to_scope} scope...")

    try:
        move_into_place(skill_path, target_path)
        print(f"Moved skill '{name}': {from_scope} -> {to_scope}")
        print(f"  From: {skill_path}")
        print(f"  To:   {target_path}")
        return True
    except Exception as e:
        print(f"Error moving skill: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Move a Claude Code skill between scopes")
    parser.add_argument("name", help="Name of the skill to move")
    parser.add_argument(
        "to_scope",
        choices=["user", "project"],
        help="Target scope to move the skill to"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Overwrite if skill exists in target scope"
    )
    args = parser.parse_args()

    success = move_skill(args.name, args.to_scope, args.force)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
