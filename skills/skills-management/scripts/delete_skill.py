#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Delete a skill from AI coding agents."""

import sys

if sys.version_info < (3, 11):
    sys.exit(
        f"{__file__} needs Python 3.11+, but runs on {sys.version.split()[0]}.\n"
        f"Run it with uv instead: uv run {__file__}"
    )

import argparse
import os
from dataclasses import dataclass, field
from pathlib import Path

from agents import (
    AGENTS,
    detect_installed_agents,
    get_agent_config,
    get_all_global_skills_dirs,
    get_skills_dir,
    validate_agent,
)
from fs_ops import remove_path

SCRIPT = "uv run scripts/delete_skill.py"


@dataclass
class Location:
    """One filesystem entry holding a skill, and every agent scope that reads it."""

    path: Path
    readers: list[tuple[str, str, str]] = field(default_factory=list)  # (agent_id, display, scope)

    @property
    def is_link(self) -> bool:
        return self.path.is_symlink()

    def describe(self) -> str:
        readers = ", ".join(f"{display} ({agent_id}) [{scope}]" for agent_id, display, scope in self.readers)
        if self.is_link:
            kind = f"symlink -> {os.readlink(self.path)}"
            if not self.path.exists():
                kind += " (broken)"
        else:
            kind = "directory"
        return f"{self.path} ({kind})" + (f"\n      read by: {readers}" if readers else "")


def get_user_skills_dir() -> Path:
    """Get the user-level skills directory."""
    return Path.home() / ".claude" / "skills"


def get_project_skills_dir() -> Path:
    """Get the project-level skills directory (current working directory)."""
    return Path.cwd() / ".claude" / "skills"


def has_skill_entry(path: Path) -> bool:
    """A skill directory, a symlink to one, or a broken symlink left behind."""
    return path.is_symlink() or (path / "SKILL.md").is_file()


def find_skill(name: str, scope: str | None = None) -> tuple[Path | None, str | None]:
    """Find a skill by name in Claude Code scopes.

    Returns:
        Tuple of (skill_path, scope_name) or (None, None) if not found
    """
    scopes_to_check = []
    if scope is None or scope == "user":
        scopes_to_check.append(("user", get_user_skills_dir()))
    if scope is None or scope == "project":
        scopes_to_check.append(("project", get_project_skills_dir()))

    for scope_name, skills_dir in scopes_to_check:
        skill_path = skills_dir / name
        if has_skill_entry(skill_path):
            return skill_path, scope_name

    return None, None


def collect_locations(name: str, agent_ids: list[str]) -> list[Location]:
    """Every distinct entry for ``name`` in the given agents' scopes.

    Entries are keyed by their own path, not by the directory they resolve to, so a
    canonical directory and each symlink to it are separate locations, while agents
    that share one skills directory are readers of the same location.
    """
    by_path: dict[str, Location] = {}
    for agent_id in agent_ids:
        config = get_agent_config(agent_id)
        if not config:
            continue
        scoped_dirs = [("global", d) for d in get_all_global_skills_dirs(agent_id)]
        if project_dir := get_skills_dir(agent_id, "project"):
            scoped_dirs.append(("project", project_dir))
        for scope, skills_dir in scoped_dirs:
            skill_path = skills_dir / name
            if not has_skill_entry(skill_path):
                continue
            key = os.path.abspath(skill_path)
            location = by_path.setdefault(key, Location(Path(key)))
            location.readers.append((agent_id, config["display_name"], scope))
    return list(by_path.values())


def find_skill_in_agents(name: str) -> list[Location]:
    """Find a skill across all detected agents."""
    return collect_locations(name, detect_installed_agents())


def links_left_dangling(name: str, deleting: list[Location]) -> list[Location]:
    """Symlinks outside ``deleting`` that point at a real directory about to be deleted."""
    doomed_real = {loc.path.resolve() for loc in deleting if not loc.is_link}
    if not doomed_real:
        return []
    doomed_paths = {loc.path for loc in deleting}
    candidates = find_skill_in_agents(name)
    for scope in ("user", "project"):
        path, _ = find_skill(name, scope)
        if path and path.is_symlink():
            candidates.append(Location(Path(os.path.abspath(path)), [("claude-code", "Claude Code", scope)]))
    return [
        loc for loc in candidates
        if loc.is_link and loc.path not in doomed_paths and loc.path.resolve() in doomed_real
    ]


def refuse_dangling(name: str, dangling: list[Location]) -> bool:
    print("\nRefusing: these symlinks point at the directory being deleted and would break:")
    for loc in dangling:
        print(f"  - {loc.describe()}")
    print("Next step, after confirming with the user, one of:")
    print(f"  {SCRIPT} {name} --all-agents --force   # delete the directory and every link to it")
    print("  or delete only the links by naming their agents with --agent.")
    return False


def confirm(prompt: str) -> bool:
    """Ask on a terminal; refuse with the next command when there is none."""
    if not sys.stdin.isatty():
        print("\nNo terminal to confirm on. Confirm with the user, then rerun with --force.")
        return False
    response = input(prompt).strip().lower()
    if response != "y":
        print("Cancelled.")
        return False
    return True


def delete_skill_default(name: str, scope: str | None = None, force: bool = False) -> bool:
    """Delete a skill from Claude Code scopes (default behavior).

    Args:
        name: Skill name (directory name)
        scope: "user", "project", or None to search both
        force: Skip confirmation prompt

    Returns:
        True if deleted, False otherwise
    """
    skill_path, found_scope = find_skill(name, scope)

    if not skill_path:
        if scope:
            print(f"Error: Skill '{name}' not found in {scope} scope.")
        else:
            print(f"Error: Skill '{name}' not found in user or project scope.")
        return False

    target = Location(Path(os.path.abspath(skill_path)))
    print(f"Found skill '{name}' at: {target.describe()}")
    print(f"Scope: {found_scope}")

    dangling = links_left_dangling(name, [target])
    if dangling:
        return refuse_dangling(name, dangling)

    if not force:
        if not target.is_link:
            file_count = sum(1 for f in skill_path.rglob("*") if f.is_file())
            print(f"Contains {file_count} file(s)")
        if not confirm("\nDelete this skill? [y/N]: "):
            return False

    try:
        remove_path(skill_path)
        print(f"Deleted skill '{name}' from {found_scope} scope.")
    except OSError as e:
        print(f"Error deleting skill: {e}")
        return False

    remaining = find_skill_in_agents(name)
    if remaining:
        print(f"\nNote: '{name}' still exists in {len(remaining)} other location(s):")
        for loc in remaining:
            print(f"  - {loc.describe()}")
        print(f"To delete them too: {SCRIPT} {name} --all-agents --force")

    return True


def delete_skill_agents(
    name: str,
    agents: list[str] | None = None,
    all_agents: bool = False,
    force: bool = False,
) -> bool:
    """Delete a skill from specific agents or all detected agents.

    Args:
        name: Skill name (directory name)
        agents: Specific agent IDs to delete from
        all_agents: Delete from all detected agents
        force: Skip confirmation prompt

    Returns:
        True if all deletions succeeded, False otherwise
    """
    if all_agents:
        locations = find_skill_in_agents(name)
        if not locations:
            print(f"Error: Skill '{name}' not found in any detected agent.")
            return False
    else:
        locations = collect_locations(name, agents or [])
        if not locations:
            print(f"Error: Skill '{name}' not found in: {', '.join(agents or [])}")
            return False

    print(f"Found '{name}' in {len(locations)} location(s):")
    for loc in locations:
        print(f"  - {loc.describe()}")

    dangling = links_left_dangling(name, locations)
    if dangling:
        return refuse_dangling(name, dangling)

    if not force and not confirm(f"\nDelete all {len(locations)} location(s)? [y/N]: "):
        return False

    # Links first, so a failure never leaves links pointing at a deleted directory.
    ordered = sorted(locations, key=lambda loc: not loc.is_link)
    results = []
    for loc in ordered:
        try:
            remove_path(loc.path)
            results.append((loc, True, "Deleted"))
        except OSError as e:
            results.append((loc, False, str(e)))

    print("\n=== DELETE RESULTS ===\n")
    for loc, success, message in results:
        print(f"[{'OK' if success else 'FAILED'}] {message}: {loc.describe()}")
    success_count = sum(1 for _, success, _ in results if success)
    print(f"\nDeleted {success_count}/{len(results)} location(s).")
    return success_count == len(results)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Delete a skill. Without --agent/--all-agents only Claude Code scopes are touched. "
            "Refuses to delete a directory that other agents' symlinks still point at."
        )
    )
    parser.add_argument("name", help="Name of the skill to delete")
    parser.add_argument(
        "--scope", "-s",
        choices=["user", "project"],
        help="Claude Code scope to search (default: both, user takes precedence)"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Skip the confirmation prompt (required in non-interactive shells)"
    )
    parser.add_argument(
        "--agent", "-a",
        action="append",
        dest="agents",
        help="Target agent(s) to delete from (can be repeated)"
    )
    parser.add_argument(
        "--all-agents",
        action="store_true",
        help="Delete every copy and symlink in all detected agents"
    )
    args = parser.parse_args()

    if args.agents and args.all_agents:
        parser.error("Cannot use both --agent and --all-agents")

    if (args.agents or args.all_agents) and args.scope:
        parser.error("Cannot use --scope with --agent or --all-agents")

    if args.agents:
        for agent in args.agents:
            if not validate_agent(agent):
                print(f"Error: Unknown agent '{agent}'")
                print(f"Valid agents: {', '.join(sorted(AGENTS.keys()))}")
                return 1

    if args.agents or args.all_agents:
        success = delete_skill_agents(args.name, args.agents, args.all_agents, args.force)
    else:
        success = delete_skill_default(args.name, args.scope, args.force)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
