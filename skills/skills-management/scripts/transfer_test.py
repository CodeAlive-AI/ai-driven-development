#!/usr/bin/env python3
"""Verify a skill transfers correctly to other agent directories.

Inspired by Microsoft's SkillOpt paper (arXiv 2605.23904) §4.3, which
demonstrates that optimised skills carry across models and harnesses. This
script provides a lightweight structural check: per target agent it asks
whether the skill artefact lands at the expected path and parses cleanly.
Optionally, with --copy, it can copy the skill from the source location into
the target's skills directory first.
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

# Reuse the agent registry from sibling scripts.
sys.path.insert(0, str(Path(__file__).parent))

from agents import (  # noqa: E402
    AGENTS,
    detect_installed_agents,
    get_agent_config,
    get_skills_dir,
    validate_agent,
)


def get_user_skills_dir() -> Path:
    """Get the Claude Code user-level skills directory (the source default)."""
    return Path.home() / ".claude" / "skills"


def get_project_skills_dir() -> Path:
    """Get the Claude Code project-level skills directory."""
    return Path.cwd() / ".claude" / "skills"


def find_source_skill(name: str) -> tuple[Path | None, str | None]:
    """Find the source skill in the standard claude-code locations.

    Returns (path, scope) or (None, None).
    """
    for scope_name, skills_dir in (
        ("user", get_user_skills_dir()),
        ("project", get_project_skills_dir()),
    ):
        candidate = skills_dir / name
        if candidate.exists() and (candidate / "SKILL.md").exists():
            return candidate, scope_name
    return None, None


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from SKILL.md content."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}

    frontmatter = match.group(1)
    metadata = {}

    current_key = None
    current_value = []

    for line in frontmatter.split("\n"):
        key_match = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if key_match:
            if current_key:
                value = "\n".join(current_value).strip()
                metadata[current_key] = value.strip('"\'')
            current_key = key_match.group(1)
            current_value = [key_match.group(2)]
        elif current_key and line.startswith("  "):
            current_value.append(line.strip())

    if current_key:
        value = "\n".join(current_value).strip()
        metadata[current_key] = value.strip('"\'')

    return metadata


def extract_body(content: str) -> str:
    """Return everything after the YAML frontmatter."""
    match = re.match(r"^---\s*\n.*?\n---\s*\n(.*)$", content, re.DOTALL)
    return match.group(1).strip() if match else content


def check_agent_target(
    agent_id: str,
    skill_name: str,
    scope: str,
) -> dict:
    """Check whether the skill is present and structurally valid for agent.

    Returns a dict with keys: agent, agent_display, scope, status, reason,
    path, description_len, body_tokens.
    """
    config = get_agent_config(agent_id)
    info: dict = {
        "agent": agent_id,
        "agent_display": config["display_name"] if config else agent_id,
        "scope": scope,
        "status": "missing",
        "reason": "",
        "path": "",
        "description_len": 0,
        "body_tokens": 0,
    }

    if not config:
        info["status"] = "agent-dir-missing"
        info["reason"] = f"unknown agent id '{agent_id}'"
        return info

    skills_dir = get_skills_dir(agent_id, scope)
    if not skills_dir or not skills_dir.exists():
        info["status"] = "agent-dir-missing"
        info["reason"] = f"agent skills dir not found: {skills_dir}"
        info["path"] = str(skills_dir) if skills_dir else ""
        return info

    skill_path = skills_dir / skill_name
    skill_md = skill_path / "SKILL.md"
    info["path"] = str(skill_path)

    if not skill_md.exists():
        info["status"] = "missing"
        info["reason"] = f"SKILL.md not found at {skill_md}"
        return info

    try:
        content = skill_md.read_text()
    except OSError as exc:
        info["status"] = "present-invalid"
        info["reason"] = f"cannot read SKILL.md: {exc}"
        return info

    metadata = parse_frontmatter(content)

    fm_name = metadata.get("name", "")
    description = metadata.get("description", "")

    if not metadata:
        info["status"] = "present-invalid"
        info["reason"] = "no parseable YAML frontmatter"
        return info

    if fm_name != skill_name:
        info["status"] = "present-invalid"
        info["reason"] = (
            f"frontmatter name '{fm_name}' does not match directory '{skill_name}'"
        )
        info["description_len"] = len(description)
        return info

    if not description.strip():
        info["status"] = "present-invalid"
        info["reason"] = "empty description"
        return info

    for field in ("name", "description"):
        value = metadata.get(field, "")
        if "<" in value or ">" in value:
            info["status"] = "present-invalid"
            info["reason"] = f"field '{field}' contains angle brackets"
            info["description_len"] = len(description)
            return info

    body = extract_body(content)
    info["status"] = "present-valid"
    info["description_len"] = len(description)
    info["body_tokens"] = len(body.split())
    return info


def copy_skill_into_target(
    source_path: Path,
    agent_id: str,
    scope: str,
    skill_name: str,
) -> tuple[bool, str]:
    """Copy a skill from source_path to the target agent's skills dir.

    Creates the destination skills dir if needed. Refuses to overwrite an
    existing skill at the destination.
    """
    skills_dir = get_skills_dir(agent_id, scope)
    if not skills_dir:
        return False, f"unknown agent or scope: {agent_id}/{scope}"

    skills_dir.mkdir(parents=True, exist_ok=True)
    dest = skills_dir / skill_name

    if dest.exists():
        return False, f"destination already exists: {dest}"

    try:
        shutil.copytree(source_path, dest)
    except OSError as exc:
        return False, f"copy failed: {exc}"

    return True, f"copied to {dest}"


def format_text(skill_name: str, source_path: Path, results: list[dict]) -> str:
    """Format text-mode report."""
    lines = [
        f"Transfer test: {skill_name} (source: {source_path})",
        "=" * 60,
    ]
    for r in results:
        label = f"{r['agent_display']} ({r['scope']})"
        status = r["status"]
        if status == "present-valid":
            extra = (
                f"description-len={r['description_len']}  "
                f"body-tokens={r['body_tokens']}"
            )
            lines.append(f"{label:<25} {status:<18} {extra}")
        elif status == "present-invalid":
            lines.append(
                f"{label:<25} {status:<18} reason: {r['reason']}"
            )
        elif status == "missing":
            lines.append(f"{label:<25} {status}")
        elif status == "agent-dir-missing":
            lines.append(f"{label:<25} {status:<18} {r['reason']}")
        else:
            lines.append(f"{label:<25} {status:<18} {r['reason']}")
    return "\n".join(lines)


def resolve_targets(
    targets_arg: list[str] | None,
    all_flag: bool,
    to_arg: str | None,
) -> tuple[list[str], str | None]:
    """Resolve the target agent list and any error message.

    Returns (target_ids, error). On error, target_ids is empty.
    """
    if to_arg:
        if not validate_agent(to_arg):
            return [], f"unknown agent '{to_arg}'"
        return [to_arg], None

    if all_flag:
        detected = detect_installed_agents()
        if not detected:
            return [], "no agents detected on this system"
        return detected, None

    if not targets_arg:
        return [], "either --targets, --all, or --to is required"

    for t in targets_arg:
        if not validate_agent(t):
            return [], (
                f"unknown agent '{t}'. "
                f"Valid: {', '.join(sorted(AGENTS.keys()))}"
            )
    return targets_arg, None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify a skill transfers cleanly to other agents"
    )
    parser.add_argument("name", help="Name of the skill to verify")
    parser.add_argument(
        "--targets",
        nargs="+",
        help="Target agent IDs to check (e.g. cursor amp codex)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Check every detected agent",
    )
    parser.add_argument(
        "--copy",
        action="store_true",
        help="Copy the skill from the source into the target first",
    )
    parser.add_argument(
        "--to",
        help="Single target agent ID (used with --copy)",
    )
    parser.add_argument(
        "--scope",
        choices=["project", "global"],
        default="project",
        help="Scope to check on the target (default: project)",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    args = parser.parse_args()

    source_path, source_scope = find_source_skill(args.name)
    if not source_path:
        print(
            f"Error: source skill '{args.name}' not found in "
            f"{get_user_skills_dir()} or {get_project_skills_dir()}",
            file=sys.stderr,
        )
        return 1

    target_ids, error = resolve_targets(args.targets, args.all, args.to)
    if error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    # Copy step: only meaningful for a single explicit target via --to or
    # when --copy is given with --targets.
    copy_log: list[dict] = []
    if args.copy:
        for target in target_ids:
            check = check_agent_target(target, args.name, args.scope)
            if check["status"] == "missing":
                ok, reason = copy_skill_into_target(
                    source_path, target, args.scope, args.name
                )
                copy_log.append({
                    "agent": target,
                    "ok": ok,
                    "reason": reason,
                })
            else:
                copy_log.append({
                    "agent": target,
                    "ok": False,
                    "reason": f"skip copy: target status is '{check['status']}'",
                })

    results = [
        check_agent_target(t, args.name, args.scope) for t in target_ids
    ]

    if args.format == "json":
        out = {
            "skill": args.name,
            "source_path": str(source_path),
            "source_scope": source_scope,
            "scope": args.scope,
            "copy_log": copy_log,
            "results": results,
        }
        print(json.dumps(out, indent=2))
    else:
        if copy_log:
            print("Copy log:")
            for entry in copy_log:
                marker = "OK  " if entry["ok"] else "SKIP"
                print(f"  [{marker}] {entry['agent']}: {entry['reason']}")
            print("")
        print(format_text(args.name, source_path, results))

    ok = all(r["status"] == "present-valid" for r in results)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
