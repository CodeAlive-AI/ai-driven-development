#!/usr/bin/env python3
"""Claude Code's two skill scopes, shared by the single-agent scripts.

``user`` is the Claude Code global skills directory (``$CLAUDE_CONFIG_DIR/skills``,
by default ``~/.claude/skills``) and ``project`` is ``.claude/skills`` under the
working directory. Both come from the agent registry in ``agents.py``, so these
scripts look where install_skill.py writes.
"""

from __future__ import annotations

from pathlib import Path

from agents import get_global_skills_dir, get_project_skills_dir as agent_project_skills_dir

AGENT = "claude-code"
SCOPES = ("user", "project")


def get_user_skills_dir() -> Path:
    """Claude Code user-level skills directory."""
    return get_global_skills_dir(AGENT)


def get_project_skills_dir(cwd: Path | None = None) -> Path:
    """Claude Code project-level skills directory under ``cwd`` (default: the working directory)."""
    return agent_project_skills_dir(AGENT, cwd)


def scope_dirs(scope: str | None = None) -> list[tuple[str, Path]]:
    """(scope, skills directory) pairs for one scope, or for both, user first."""
    dirs = {"user": get_user_skills_dir, "project": get_project_skills_dir}
    return [(name, dirs[name]()) for name in SCOPES if scope is None or scope == name]


def find_skill(
    name: str, scope: str | None = None, *, include_links: bool = False
) -> tuple[Path | None, str | None]:
    """Find a skill directory by name, user scope first.

    A match is a directory with a SKILL.md. With ``include_links`` any symlink also
    matches, broken ones included, so delete and move can act on the link itself.

    Returns:
        (skill_path, scope_name), or (None, None) if not found
    """
    for scope_name, skills_dir in scope_dirs(scope):
        skill_path = skills_dir / name
        if (skill_path / "SKILL.md").is_file() or (include_links and skill_path.is_symlink()):
            return skill_path, scope_name
    return None, None
