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
import hashlib
import json
import re
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path

from agents import AGENTS, get_all_global_skills_dirs
from skill_md import read_skill_md, skill_name


IGNORED_PARTS = {".git", ".DS_Store", "__pycache__", ".pytest_cache"}
BACKUP_RE = re.compile(r"(?:^|[._-])(backup|bak|old|copy)(?:$|[._-])", re.IGNORECASE)
AGY_DOT_DIRS = (".agents", ".agent", "_agents", "_agent")
AGY_PLUGIN_MANIFESTS = (
    "plugin.json",
    ".antigravity-plugin/plugin.json",
    ".gemini-plugin/plugin.json",
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
    content_hash: str | None = None


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
    """Add an existing skill root once, using its lexical path as identity.

    A root that is a symlink to a root already added (for example the legacy
    ``~/.gemini/antigravity/skills`` -> ``~/.gemini/config/skills``) is skipped:
    it holds the same entries and would only list each skill twice.
    """
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


def _strip_jsonc(text: str) -> str:
    """Strip ``//`` / ``/* ... */`` comments and trailing commas outside JSON strings."""
    out: list[str] = []
    i = 0
    n = len(text)
    in_string = False
    escaped = False

    while i < n:
        ch = text[i]
        if in_string:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            i += 1
            continue

        if ch == '"':
            in_string = True
            out.append(ch)
            i += 1
        elif ch == "/" and i + 1 < n and text[i + 1] == "/":
            i += 2
            while i < n and text[i] not in ("\n", "\r"):
                i += 1
        elif ch == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
        else:
            out.append(ch)
            i += 1

    # Remove trailing commas before closing } or ] outside strings.
    cleaned: list[str] = []
    no_comments = "".join(out)
    in_string = False
    escaped = False
    m = len(no_comments)
    for idx, ch in enumerate(no_comments):
        if in_string:
            cleaned.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
            cleaned.append(ch)
            continue
        if ch == ",":
            j = idx + 1
            while j < m and no_comments[j] in " \t\r\n":
                j += 1
            if j < m and no_comments[j] in "}]":
                continue
        cleaned.append(ch)
    return "".join(cleaned)


def _load_jsonc(path: Path) -> dict | list | None:
    """Parse a JSON or JSONC file (with optional UTF-8 BOM), returning None on error."""
    try:
        raw = path.read_text(encoding="utf-8-sig")
        return json.loads(_strip_jsonc(raw))
    except (OSError, json.JSONDecodeError):
        return None


def _find_agy_plugin_manifest(plugin_dir: Path) -> dict | None:
    """Return the parsed Antigravity plugin manifest dict if present."""
    for rel in AGY_PLUGIN_MANIFESTS:
        candidate = plugin_dir / rel
        if candidate.is_file():
            data = _load_jsonc(candidate)
            if isinstance(data, dict):
                return data
    return None


def _agy_plugin_skill_dirs(plugin_dir: Path, manifest: dict | None) -> list[Path]:
    """Return skill directories declared or conventionally placed inside a plugin."""
    dirs: list[Path] = []
    plugin_real = plugin_dir.resolve()
    default_skills = plugin_dir / "skills"
    if default_skills.is_dir() and default_skills.resolve().is_relative_to(plugin_real):
        dirs.append(default_skills)

    if isinstance(manifest, dict) and "skills" in manifest:
        raw_skills = manifest["skills"]
        entries: list[str] = []
        if isinstance(raw_skills, str):
            entries = [raw_skills]
        elif isinstance(raw_skills, list):
            entries = [item for item in raw_skills if isinstance(item, str)]
        for entry in entries:
            rel = Path(entry)
            if rel.is_absolute():
                continue
            candidate = (plugin_dir / rel).resolve()
            if not candidate.is_relative_to(plugin_real):
                continue
            if candidate.is_dir() and candidate not in [d.resolve() for d in dirs]:
                dirs.append(plugin_dir / rel)
    return dirs


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


def _resolve_manifest_entry(
    raw_path: str, base_dir: Path, repo_root: Path | None
) -> Path | None:
    """Resolve an entry or inherit path from a skills.json/plugins.json manifest."""
    if not raw_path or not isinstance(raw_path, str):
        return None
    if repo_root is not None:
        if raw_path.startswith("~") or Path(raw_path).is_absolute():
            return None
        repo_real = repo_root.resolve()
        candidate = (base_dir / raw_path).resolve()
        if not candidate.exists():
            fallback = (repo_root / raw_path).resolve()
            if fallback.exists():
                candidate = fallback
        if not candidate.is_relative_to(repo_real):
            return None
        return candidate

    expanded = Path(raw_path).expanduser()
    if expanded.is_absolute():
        return expanded.resolve()
    return (base_dir / expanded).resolve()


def _expand_manifest(
    manifest_path: Path,
    *,
    kind: str,
    repo_root: Path | None,
    visited: set[Path],
    is_plugins: bool,
) -> list[tuple[Path, str]]:
    """Recursively expand an Antigravity ``skills.json`` or ``plugins.json`` manifest."""
    resolved_manifest = manifest_path.resolve()
    if resolved_manifest in visited or not resolved_manifest.is_file():
        return []
    if repo_root is not None and not resolved_manifest.is_relative_to(repo_root.resolve()):
        return []
    visited.add(resolved_manifest)

    data = _load_jsonc(resolved_manifest)
    if not isinstance(data, dict):
        return []

    base_dir = manifest_path.parent.parent if repo_root is not None else manifest_path.parent
    results: list[tuple[Path, str]] = []

    inherits = data.get("inherits")
    if isinstance(inherits, list):
        for item in inherits:
            if not isinstance(item, dict):
                continue
            inherited = _resolve_manifest_entry(item.get("path", ""), base_dir, repo_root)
            if inherited is not None:
                results.extend(
                    _expand_manifest(
                        inherited,
                        kind=kind,
                        repo_root=repo_root,
                        visited=visited,
                        is_plugins=is_plugins,
                    )
                )

    entries = data.get("entries")
    if isinstance(entries, list):
        for item in entries:
            if not isinstance(item, dict):
                continue
            target = _resolve_manifest_entry(item.get("path", ""), base_dir, repo_root)
            if target is None or not target.is_dir():
                continue
            if not is_plugins:
                results.append((target, kind))
                continue
            for child in sorted(target.iterdir()):
                if not child.is_dir():
                    continue
                if repo_root is not None and not child.resolve().is_relative_to(repo_root.resolve()):
                    continue
                manifest = _find_agy_plugin_manifest(child)
                if manifest is not None or (child / "skills").is_dir():
                    for skill_dir in _agy_plugin_skill_dirs(child, manifest):
                        if repo_root is None or skill_dir.resolve().is_relative_to(repo_root.resolve()):
                            results.append((skill_dir, "plugin-manifest"))

    return results


def antigravity_manifest_skill_roots(
    home: Path, repos: list[Path]
) -> list[tuple[Path, str]]:
    """Return skill roots declared in global and workspace ``skills.json`` / ``plugins.json``."""
    results: list[tuple[Path, str]] = []
    visited: set[Path] = set()

    global_root = home / ".gemini" / "config"
    results.extend(
        _expand_manifest(
            global_root / "skills.json",
            kind="manifest-global",
            repo_root=None,
            visited=visited,
            is_plugins=False,
        )
    )
    results.extend(
        _expand_manifest(
            global_root / "plugins.json",
            kind="plugin-manifest",
            repo_root=None,
            visited=visited,
            is_plugins=True,
        )
    )

    for repo in repos:
        for dot_dir in AGY_DOT_DIRS:
            dot_path = repo / dot_dir
            results.extend(
                _expand_manifest(
                    dot_path / "skills.json",
                    kind="manifest-workspace",
                    repo_root=repo,
                    visited=visited,
                    is_plugins=False,
                )
            )
            results.extend(
                _expand_manifest(
                    dot_path / "plugins.json",
                    kind="plugin-manifest",
                    repo_root=repo,
                    visited=visited,
                    is_plugins=True,
                )
            )

    return results


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

    # Codex owns and namespaces its cache. Multiple cached versions are inventory
    # information, not user-install conflicts. Claude and Antigravity expose enabled
    # state, so omit disabled/historical cache versions by default.
    codex_cache = home / ".codex" / "plugins" / "cache"
    if codex_cache.is_dir():
        for skill_root in codex_cache.rglob("skills"):
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
