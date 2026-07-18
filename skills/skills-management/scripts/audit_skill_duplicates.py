#!/usr/bin/env python3
"""Audit skill discovery roots for duplicate frontmatter names.

The audit is read-only. It distinguishes aliases to one real directory, identical
cross-agent replicas, obvious backup copies, plugin-namespaced copies, and divergent
implementations that require a canonical-source decision.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from agents import AGENTS


IGNORED_PARTS = {".git", ".DS_Store", "__pycache__", ".pytest_cache"}
BACKUP_RE = re.compile(r"(?:^|[._-])(backup|bak|old|copy)(?:$|[._-])", re.IGNORECASE)


@dataclass
class SkillRecord:
    name: str
    path: str
    real_path: str
    root: str
    root_kind: str
    version: str | None
    is_symlink: bool
    is_plugin: bool
    is_backup: bool
    content_hash: str | None = None


def parse_frontmatter(skill_dir: Path) -> dict[str, str]:
    """Read simple scalar fields from a SKILL.md frontmatter block."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return {}

    text = skill_md.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {"name": skill_dir.name}

    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^(name|version):\s*(.*?)\s*$", line)
        if field:
            result[field.group(1)] = field.group(2).strip("\"'")
    result.setdefault("name", skill_dir.name)
    return result


def hash_skill_directory(skill_dir: Path) -> str:
    """Hash relevant files and relative paths for deterministic comparisons."""
    digest = hashlib.sha256()
    real_dir = skill_dir.resolve()
    for item in sorted(real_dir.rglob("*"), key=lambda path: path.as_posix()):
        relative = item.relative_to(real_dir)
        if any(part in IGNORED_PARTS for part in relative.parts) or not item.is_file():
            continue
        digest.update(relative.as_posix().encode())
        digest.update(b"\0")
        digest.update(item.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def find_repo_root(start: Path) -> Path | None:
    """Return the closest repository root containing start, if any."""
    current = start.resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def add_root(
    roots: dict[str, tuple[Path, str]], root: Path, root_kind: str
) -> None:
    """Add an existing skill root once, using its lexical path as identity."""
    expanded = root.expanduser()
    if expanded.is_dir():
        roots.setdefault(str(expanded.absolute()), (expanded, root_kind))


def active_claude_plugin_skill_roots() -> list[Path]:
    """Return skill roots for enabled Claude plugins, excluding historical caches."""
    try:
        result = subprocess.run(
            ["claude", "plugin", "list", "--json"],
            capture_output=True,
            check=True,
            text=True,
            timeout=15,
        )
        plugins = json.loads(result.stdout)
    except (FileNotFoundError, subprocess.SubprocessError, json.JSONDecodeError):
        return []

    roots: list[Path] = []
    for plugin in plugins:
        install_path = plugin.get("installPath")
        if plugin.get("enabled") is True and install_path:
            roots.append(Path(install_path) / "skills")
    return roots


def default_roots(cwd: Path, anchors: list[Path] | None = None) -> list[tuple[Path, str]]:
    """Return bounded global, repository, local-plugin, and plugin-cache roots."""
    roots: dict[str, tuple[Path, str]] = {}
    home = Path.home()

    add_root(roots, home / ".agents" / "skills", "canonical-user")
    for config in AGENTS.values():
        add_root(roots, Path(config["global_dir"]), "agent-user")

    search_anchors = [cwd, *(anchors or [])]
    seen_repos: set[Path] = set()
    project_dirs = {config["project_dir"] for config in AGENTS.values()}
    for anchor in search_anchors:
        repo = find_repo_root(anchor)
        if repo is None or repo in seen_repos:
            continue
        seen_repos.add(repo)
        for project_dir in project_dirs:
            add_root(roots, repo / project_dir, "repo")
        if (repo / ".claude-plugin" / "plugin.json").is_file():
            add_root(roots, repo / "skills", "plugin-source")

    # Codex owns and namespaces its cache. Multiple cached versions are inventory
    # information, not user-install conflicts. Claude exposes enabled state through
    # its plugin CLI, so omit disabled/historical Claude cache versions by default.
    codex_cache = home / ".codex" / "plugins" / "cache"
    if codex_cache.is_dir():
        for skill_root in codex_cache.rglob("skills"):
            add_root(roots, skill_root, "plugin-cache")
    for skill_root in active_claude_plugin_skill_roots():
        add_root(roots, skill_root, "plugin-cache-active")

    return list(roots.values())


def record_for_directory(skill_dir: Path, root: Path, root_kind: str) -> SkillRecord | None:
    """Build an inventory record for one skill directory."""
    metadata = parse_frontmatter(skill_dir)
    name = metadata.get("name")
    if not name:
        return None
    path_text = str(skill_dir.absolute())
    return SkillRecord(
        name=name,
        path=path_text,
        real_path=str(skill_dir.resolve()),
        root=str(root.absolute()),
        root_kind=root_kind,
        version=metadata.get("version"),
        is_symlink=skill_dir.is_symlink(),
        is_plugin=root_kind.startswith("plugin"),
        is_backup=bool(BACKUP_RE.search(skill_dir.name)),
    )


def scan_roots(roots: list[tuple[Path, str]]) -> list[SkillRecord]:
    """Inventory direct child skill directories under each discovery root."""
    records: list[SkillRecord] = []
    seen_locations: set[str] = set()
    for root, root_kind in roots:
        candidates = [root] if (root / "SKILL.md").is_file() else sorted(root.iterdir())
        for candidate in candidates:
            if not candidate.is_dir() or not (candidate / "SKILL.md").is_file():
                continue
            location = str(candidate.absolute())
            if location in seen_locations:
                continue
            seen_locations.add(location)
            record = record_for_directory(candidate, root, root_kind)
            if record:
                records.append(record)
    return records


def ensure_hash(record: SkillRecord) -> str:
    """Compute a record's directory hash lazily."""
    if record.content_hash is None:
        record.content_hash = hash_skill_directory(Path(record.path))
    return record.content_hash


def classify_group(records: list[SkillRecord]) -> str:
    """Classify multiple locations sharing one frontmatter name."""
    if len({record.real_path for record in records}) == 1:
        return "alias"
    if any(record.is_backup for record in records):
        return "stale-backup"
    hashes = {ensure_hash(record) for record in records}
    if all(record.is_plugin for record in records):
        return "managed-plugin-replica" if len(hashes) == 1 else "managed-plugin-divergent"
    if len(hashes) == 1:
        return "replica"
    if any(record.is_plugin for record in records):
        return "namespaced-divergent"
    return "divergent"


def duplicate_groups(records: list[SkillRecord]) -> list[dict]:
    """Return classified groups that have more than one lexical location."""
    by_name: dict[str, list[SkillRecord]] = {}
    for record in records:
        by_name.setdefault(record.name, []).append(record)

    groups = []
    for name, group_records in sorted(by_name.items()):
        if len(group_records) < 2:
            continue
        status = classify_group(group_records)
        groups.append({
            "name": name,
            "status": status,
            "requires_decision": status in {"stale-backup", "namespaced-divergent", "divergent"},
            "records": [asdict(record) for record in group_records],
        })
    return groups


def audit_candidate(
    source: Path,
    cwd: Path | None = None,
    roots: list[tuple[Path, str]] | None = None,
) -> dict:
    """Compare a candidate skill with every bounded discovery root."""
    source = source.resolve()
    candidate = record_for_directory(source, source.parent, "candidate")
    if candidate is None:
        raise ValueError(f"Candidate does not contain a readable SKILL.md: {source}")

    records = scan_roots(roots or default_roots(cwd or Path.cwd(), [source]))
    matches = [record for record in records if record.name == candidate.name]
    relations = []
    candidate_hash: str | None = None
    for existing in matches:
        if existing.real_path == candidate.real_path:
            relation = "already-discoverable"
        else:
            candidate_hash = candidate_hash or ensure_hash(candidate)
            relation = "identical" if ensure_hash(existing) == candidate_hash else "divergent"
        relations.append({"relation": relation, "record": asdict(existing)})

    return {
        "candidate": asdict(candidate),
        "matches": relations,
        "blocked": bool(relations),
    }


def format_text(groups: list[dict], candidate_result: dict | None = None) -> str:
    """Render an audit in a compact human-readable form."""
    lines: list[str] = []
    if candidate_result is not None:
        candidate = candidate_result["candidate"]
        lines.append(f"Candidate: {candidate['name']} ({candidate['path']})")
        if not candidate_result["matches"]:
            lines.append("No existing skill with this name was found.")
        for match in candidate_result["matches"]:
            record = match["record"]
            lines.append(f"- {match['relation']}: {record['path']} [{record['root_kind']}]")
        return "\n".join(lines)

    if not groups:
        return "No duplicate skill names found."
    for group in groups:
        lines.append(f"{group['name']}: {group['status']}")
        for record in group["records"]:
            link = f" -> {record['real_path']}" if record["is_symlink"] else ""
            lines.append(f"  - {record['path']} [{record['root_kind']}]{link}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit skill names across discovery roots")
    parser.add_argument("--candidate", type=Path, help="Preflight a skill directory before installation")
    parser.add_argument("--root", action="append", type=Path, default=[], help="Additional skill root")
    parser.add_argument("--name", help="Only report this frontmatter name")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--fail-on-conflict", action="store_true")
    args = parser.parse_args()

    if args.candidate:
        result = audit_candidate(args.candidate)
        print(json.dumps(result, indent=2) if args.format == "json" else format_text([], result))
        return 2 if args.fail_on_conflict and result["blocked"] else 0

    roots = default_roots(Path.cwd())
    roots.extend((root, "explicit") for root in args.root if root.is_dir())
    groups = duplicate_groups(scan_roots(roots))
    if args.name:
        groups = [group for group in groups if group["name"] == args.name]
    print(json.dumps(groups, indent=2) if args.format == "json" else format_text(groups))
    has_conflict = any(group["requires_decision"] for group in groups)
    return 2 if args.fail_on_conflict and has_conflict else 0


if __name__ == "__main__":
    sys.exit(main())
