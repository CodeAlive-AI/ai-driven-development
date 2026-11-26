#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Audit skill discovery roots for duplicate frontmatter names.

The audit is read-only. It distinguishes aliases to one real directory, identical
cross-agent replicas, obvious backup copies, plugin-namespaced copies, and divergent
implementations that require a canonical-source decision.
"""

from __future__ import annotations

import sys

if sys.version_info < (3, 11):
    sys.exit(
        f"{__file__} needs Python 3.11+, but runs on {sys.version.split()[0]}.\n"
        f"Run it with uv instead: uv run {__file__}"
    )

import argparse
import json
import re
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path

from agents import AGENTS, get_all_global_skills_dirs
from skill_md import read_skill_md, skill_name
from skill_topology import (
    AGY_DOT_DIRS,
    AGY_PLUGIN_MANIFESTS,
    BACKUP_RE,
    IGNORED_PARTS,
    _codex_openai_yaml_meta,
    active_codex_plugin_skill_roots,
    agy_plugin_skill_dirs as _agy_plugin_skill_dirs,
    antigravity_manifest_skill_roots,
    classify_invocation_mode,
    find_agy_plugin_manifest as _find_agy_plugin_manifest,
    find_repo_root,
    hash_skill_directory,
    load_jsonc as _load_jsonc,
    strip_jsonc as _strip_jsonc,
)


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
    invocation_mode: str = "auto"
    content_hash: str | None = None


def add_root(
    roots: dict[str, tuple[Path, str]], root: Path, root_kind: str
) -> None:
    """Add an existing skill root once, using its lexical path as identity."""
    expanded = root.expanduser()
    if not expanded.is_dir():
        return
    if expanded.is_symlink():
        target = expanded.resolve()
        if any(existing.resolve() == target for existing, _ in roots.values()):
            return
    roots.setdefault(str(expanded.absolute()), (expanded, root_kind))


def active_claude_plugin_skill_roots() -> list[Path]:
    """Return skill roots for enabled Claude plugins, excluding historical caches."""
    try:
        result = subprocess.run(
            ["claude", "plugin", "list", "--json"],
            capture_output=True,
            check=True,
            text=True,
            encoding="utf-8",
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


def active_antigravity_plugin_skill_roots(
    home: Path | None = None, *, query_cli: bool = True
) -> list[Path]:
    """Return skill roots for enabled Antigravity plugins (config dir + ``agy`` CLI)."""
    home = home or Path.home()
    config_data = _load_jsonc(home / ".gemini" / "config" / "config.json")
    plugins_state = (
        config_data.get("plugins", {})
        if isinstance(config_data, dict) and isinstance(config_data.get("plugins"), dict)
        else {}
    )

    roots: list[Path] = []
    seen_resolved: set[Path] = set()

    def _append_dirs(paths: list[Path]) -> None:
        for path in paths:
            resolved = path.resolve()
            if resolved not in seen_resolved:
                seen_resolved.add(resolved)
                roots.append(path)

    plugins_dir = home / ".gemini" / "config" / "plugins"
    if plugins_dir.is_dir():
        for plugin_dir in sorted(plugins_dir.iterdir()):
            if not plugin_dir.is_dir():
                continue
            manifest = _find_agy_plugin_manifest(plugin_dir)
            state = plugins_state.get(plugin_dir.name)
            if isinstance(state, dict) and "enabled" in state:
                enabled = bool(state["enabled"])
            else:
                enabled = not bool((manifest or {}).get("disabled", False))
            if enabled:
                _append_dirs(_agy_plugin_skill_dirs(plugin_dir, manifest))

    if query_cli:
        try:
            result = subprocess.run(
                ["agy", "plugin", "list", "--json"],
                capture_output=True,
                check=True,
                text=True,
                encoding="utf-8",
                timeout=10,
            )
            cli_plugins = json.loads(result.stdout)
        except (FileNotFoundError, subprocess.SubprocessError, json.JSONDecodeError):
            cli_plugins = []
        if isinstance(cli_plugins, list):
            for entry in cli_plugins:
                if not isinstance(entry, dict) or entry.get("enabled") is not True:
                    continue
                raw_path = entry.get("path")
                if not raw_path:
                    continue
                plugin_dir = Path(str(raw_path))
                if plugin_dir.is_dir():
                    _append_dirs(
                        _agy_plugin_skill_dirs(plugin_dir, _find_agy_plugin_manifest(plugin_dir))
                    )

    return roots


def default_roots(cwd: Path, anchors: list[Path] | None = None) -> list[tuple[Path, str]]:
    """Return bounded global, repository, local-plugin, and plugin-cache roots."""
    roots: dict[str, tuple[Path, str]] = {}
    home = Path.home()

    add_root(roots, home / ".agents" / "skills", "canonical-user")
    for agent_id in AGENTS:
        for global_dir in get_all_global_skills_dirs(agent_id):
            add_root(roots, global_dir, "agent-user")

    search_anchors = [cwd, *(anchors or [])]
    seen_repos: set[Path] = set()
    project_dirs = {
        d
        for config in AGENTS.values()
        for d in (config["project_dir"], *config.get("extra_project_dirs", []))
    }
    for anchor in search_anchors:
        repo = find_repo_root(anchor)
        if repo is None or repo in seen_repos:
            continue
        seen_repos.add(repo)
        is_plugin_repo = (repo / ".claude-plugin" / "plugin.json").is_file() or any(
            (repo / manifest).is_file() for manifest in AGY_PLUGIN_MANIFESTS
        )
        if is_plugin_repo:
            add_root(roots, repo / "skills", "plugin-source")
        for project_dir in project_dirs:
            add_root(roots, repo / project_dir, "repo")
        for dot_dir in AGY_DOT_DIRS:
            ws_plugins = repo / dot_dir / "plugins"
            if ws_plugins.is_dir():
                for plugin_dir in sorted(ws_plugins.iterdir()):
                    if plugin_dir.is_dir():
                        manifest = _find_agy_plugin_manifest(plugin_dir)
                        for skill_dir in _agy_plugin_skill_dirs(plugin_dir, manifest):
                            add_root(roots, skill_dir, "plugin-workspace")

    for manifest_root, manifest_kind in antigravity_manifest_skill_roots(home, list(seen_repos)):
        add_root(roots, manifest_root, manifest_kind)

    # Codex owns and namespaces its cache. Only plugins enabled in config.toml
    # (and their active version dir) are loaded at runtime.
    for skill_root in active_codex_plugin_skill_roots(home):
        add_root(roots, skill_root, "plugin-cache")
    for skill_root in active_claude_plugin_skill_roots():
        add_root(roots, skill_root, "plugin-cache-active")
    for skill_root in active_antigravity_plugin_skill_roots(home):
        add_root(roots, skill_root, "plugin-antigravity")

    return list(roots.values())


def record_for_directory(skill_dir: Path, root: Path, root_kind: str) -> SkillRecord | None:
    """Build an inventory record for one skill directory."""
    parsed = read_skill_md(skill_dir)
    if parsed is None:
        return None
    metadata, _ = parsed
    name = skill_name(metadata, skill_dir)
    path_text = str(skill_dir.absolute())
    resolved = skill_dir.resolve()
    disable_model_invocation = (
        metadata.get("disable-model-invocation", "").strip().lower() == "true"
    )
    codex_allow_implicit, _ = _codex_openai_yaml_meta(resolved)
    invocation_mode = classify_invocation_mode(
        disable_model_invocation, codex_allow_implicit
    )
    return SkillRecord(
        name=name,
        path=path_text,
        real_path=str(resolved),
        root=str(root.absolute()),
        root_kind=root_kind,
        version=metadata.get("version"),
        is_symlink=skill_dir.is_symlink(),
        is_plugin=root_kind.startswith("plugin"),
        is_backup=bool(BACKUP_RE.search(skill_dir.name)),
        invocation_mode=invocation_mode,
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
        modes = {record.invocation_mode for record in group_records}
        groups.append({
            "name": name,
            "status": status,
            "requires_decision": status in {"stale-backup", "namespaced-divergent", "divergent"},
            "invocation_mode_mismatch": len(modes) > 1,
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
        cand_mode = (
            f" [{candidate['invocation_mode']}]"
            if candidate.get("invocation_mode", "auto") != "auto"
            else ""
        )
        lines.append(f"Candidate: {candidate['name']}{cand_mode} ({candidate['path']})")
        if not candidate_result["matches"]:
            lines.append("No existing skill with this name was found.")
        for match in candidate_result["matches"]:
            record = match["record"]
            rec_mode = (
                f" [{record['invocation_mode']}]"
                if record.get("invocation_mode", "auto") != "auto"
                else ""
            )
            lines.append(f"- {match['relation']}: {record['path']} [{record['root_kind']}]{rec_mode}")
        return "\n".join(lines)

    if not groups:
        return "No duplicate skill names found."
    for group in groups:
        mismatch = " [mode mismatch]" if group.get("invocation_mode_mismatch") else ""
        lines.append(f"{group['name']}: {group['status']}{mismatch}")
        for record in group["records"]:
            link = f" -> {record['real_path']}" if record["is_symlink"] else ""
            rec_mode = (
                f" [{record['invocation_mode']}]"
                if record.get("invocation_mode", "auto") != "auto"
                else ""
            )
            lines.append(f"  - {record['path']} [{record['root_kind']}]{rec_mode}{link}")
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
