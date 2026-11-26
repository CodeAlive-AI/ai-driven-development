#!/usr/bin/env python3
"""Shared skill discovery, health inspection, lockfile audit, and topology graph.

Single source of truth consumed by ``revise_skills.py``, ``sync_skills.py``, and
``audit_skill_duplicates.py``. Stdlib-only Python 3.11+.
"""

from __future__ import annotations

import errno
import hashlib
import json
import os
import re
import subprocess
import tomllib
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable

from agents import (
    AGENTS,
    PORCH_HARNESS_AGENTS,
    SHARED_GLOBAL,
    canonical_agent_id,
    detect_installed_agents,
    expand_path,
    expand_path_for_home,
    get_agent_config,
    get_all_global_skills_dirs,
    get_all_project_skills_dirs,
    get_readable_global_skills_dirs,
    hermes_reads_shared_global,
)
from skill_md import parse_skill_md, read_skill_text, skill_name

IGNORED_PARTS = {".git", ".DS_Store", "__pycache__", ".pytest_cache"}
SKIP_CHILD_NAMES = {
    ".git",
    ".DS_Store",
    "__pycache__",
    ".pytest_cache",
    ".skill-lock.json",
    "skills-lock.json",
    ".bundled_manifest",
    ".system",
}
SKIP_SCAN_DIRS = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    "dist",
    "build",
    "target",
    ".workspaces",
    ".next",
    ".turbo",
}
BACKUP_RE = re.compile(r"(?:^|[._-])(backup|bak|old|copy)(?:$|[._-])", re.IGNORECASE)
AGY_DOT_DIRS = (".agents", ".agent", "_agents", "_agent")
AGY_PLUGIN_MANIFESTS = (
    "plugin.json",
    ".antigravity-plugin/plugin.json",
    ".gemini-plugin/plugin.json",
)
# Trojan Source / invisible Unicode control characters
TROJAN_UNICODE_RE = re.compile(
    r"[\u200b-\u200f\u202a-\u202e\u2060-\u206f\u00ad\ufeff]"
)
_LOCAL_MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
_EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "customization://", "skill://", "#")

# Known startup catalog / description caps (chars unless marked tokens)
AGENT_CONTEXT_CAPS: dict[str, dict[str, int | str]] = {
    "claude-code": {"per_skill_chars": 1536, "catalog_chars": 16000, "note": "Claude Code truncates descriptions >1,536 chars and budgets ~2% context (~16k chars)"},
    "codex": {
        "per_skill_chars": 1024,
        "catalog_tokens": 5440,
        "max_configurable_tokens": 10000,
        "note": "Codex budgets 2% of model context window (~5,440 tok on 272k; 8,000-char fallback only when unknown), configurable via [skills].max_context_tokens up to 10,000",
    },
    "antigravity": {"catalog_tokens": 20000, "note": "Antigravity combined customization budget (~20,000 tokens)"},
    "antigravity-cli": {"catalog_tokens": 20000, "note": "Antigravity CLI combined customization budget (~20,000 tokens)"},
}

# Compact pool order for Discovery-Pool matrix
POOL_COLUMNS: list[tuple[str, str, list[str]]] = [
    ("shared", "Shared(~/.agents)", ["codex", "opencode", "cursor", "gemini-cli", "kimi-code-cli", "pi", "antigravity-cli"]),
    ("antigravity", "AGY", ["antigravity"]),
    ("claude-code", "Claude", ["claude-code"]),
    ("qwen-code", "Qwen", ["qwen-code"]),
    ("hermes-agent", "Hermes", ["hermes-agent"]),
    ("grok", "Grok", ["grok"]),
    ("devin", "Devin", ["devin"]),
    ("omp", "OMP", ["omp"]),
]


@dataclass
class DiscoveryRoot:
    path: Path
    root_kind: str  # canonical-user | agent-user | repo | plugin-source | plugin-workspace | plugin-cache | plugin-cache-active | plugin-antigravity | manifest-global | manifest-workspace | plugin-manifest | builtin | source-warehouse
    scope: str  # global | local | warehouse
    agent_ids: list[str] = field(default_factory=list)
    supports_nested_categories: bool = False
    is_primary: bool = True


@dataclass
class SkillEntry:
    name: str
    dir_name: str
    path: str
    real_path: str | None
    root: str
    root_kind: str
    scope: str
    agent_ids: list[str]
    category: str | None = None
    version: str | None = None
    description: str = ""
    meta_chars: int = 0
    is_symlink: bool = False
    raw_target: str | None = None
    is_relative_symlink: bool = False
    hop_count: int = 0
    is_broken: bool = False
    broken_reason: str | None = None
    is_loop: bool = False
    is_ghost: bool = False
    is_plugin: bool = False
    is_bundled: bool = False
    is_builtin: bool = False
    is_backup: bool = False
    content_hash: str | None = None
    body_lines: int = 0
    issues: list[dict] = field(default_factory=list)
    provenance: str = "local-unmanaged"
    git_repo: str | None = None
    git_dirty: bool | None = None
    repoint_candidates: list[dict] = field(default_factory=list)
    rename_hint: str | None = None


@dataclass
class LockfileIssue:
    lockfile: str
    skill: str
    source: str
    source_url: str
    kind: str  # orphaned-lock-entry | invalid-lockfile


@dataclass
class ManifestIssue:
    manifest: str
    entry_path: str
    kind: str  # missing-target | workspace-escape | parse-error


def strip_jsonc(text: str) -> str:
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


def load_jsonc(path: Path) -> dict | list | None:
    """Parse a JSON or JSONC file (with optional UTF-8 BOM), returning None on error."""
    try:
        raw = path.read_text(encoding="utf-8-sig")
        return json.loads(strip_jsonc(raw))
    except (OSError, json.JSONDecodeError):
        return None


def find_repo_root(start: Path) -> Path | None:
    """Return the closest repository root containing start, if any."""
    try:
        current = start.resolve()
    except OSError:
        current = start.absolute()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def ancestor_chain(cwd: Path, stop_at: Path | None) -> list[Path]:
    """Return directories from resolved ``cwd`` up to ``stop_at`` (inclusive), child-first."""
    try:
        cur = cwd.resolve()
    except OSError:
        cur = cwd.absolute()
    if cur.is_file():
        cur = cur.parent
    if stop_at is None:
        return [cur]
    try:
        stop = stop_at.resolve()
    except OSError:
        stop = stop_at.absolute()
    chain: list[Path] = []
    for node in (cur, *cur.parents):
        chain.append(node)
        if node == stop:
            break
    return chain


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


def normalized_slug(name: str) -> str:
    """Normalize punctuation and common gerund/plural suffixes for near-match grouping."""
    tokens = [t for t in re.split(r"[-_.\s]+", name.lower().strip()) if t]
    stems: list[str] = []
    for tok in tokens:
        if len(tok) > 5 and tok.endswith("ing"):
            tok = tok[:-3]
        elif len(tok) > 4 and tok.endswith("s") and not tok.endswith("ss"):
            tok = tok[:-1]
        stems.append(tok)
    return "".join(stems)


def walk_symlink_chain(entry: Path, max_hops: int = 16) -> tuple[bool, int, Path | None, str | None, bool, str | None]:
    """Inspect a path without masking symlink hops or ELOOP.

    Returns ``(is_symlink, hop_count, resolved_path, raw_target, is_broken, broken_reason)``.
    """
    if not entry.is_symlink():
        return False, 0, entry.resolve(), None, False, None

    try:
        first_raw = os.readlink(entry)
    except OSError as exc:
        return True, 1, None, None, True, f"unreadable symlink ({exc})"

    hops = 0
    cur = entry
    visited: set[Path] = set()
    while cur.is_symlink():
        hops += 1
        if hops > max_hops:
            return True, hops, None, first_raw, True, "symlink loop (too many levels)"
        try:
            abs_cur = Path(os.path.abspath(cur))
        except OSError:
            abs_cur = cur
        if abs_cur in visited:
            return True, hops, None, first_raw, True, "symlink loop"
        visited.add(abs_cur)
        try:
            raw = os.readlink(cur)
        except OSError as exc:
            return True, hops, None, first_raw, True, f"unreadable symlink ({exc})"
        target = Path(raw)
        if not target.is_absolute():
            cur = Path(os.path.normpath(cur.parent / target))
        else:
            cur = target

    try:
        cur.stat()
        return True, hops, cur.resolve(), first_raw, False, None
    except OSError as exc:
        if exc.errno == errno.ELOOP:
            return True, hops, None, first_raw, True, "symlink loop"
        reason = "relative target missing" if not Path(first_raw).is_absolute() else "target missing"
        return True, hops, None, first_raw, True, reason


def find_agy_plugin_manifest(plugin_dir: Path) -> dict | None:
    """Return the parsed Antigravity plugin manifest dict if present."""
    for rel in AGY_PLUGIN_MANIFESTS:
        candidate = plugin_dir / rel
        if candidate.is_file():
            data = load_jsonc(candidate)
            if isinstance(data, dict):
                return data
    return None


def agy_plugin_skill_dirs(plugin_dir: Path, manifest: dict | None) -> list[Path]:
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


_SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?(?:\+.*)?$")


def codex_home_dir(home: Path | None = None) -> Path:
    """Return Codex home directory, honoring ``CODEX_HOME`` when using the default home."""
    base = home or Path.home()
    if home is None or home == Path.home():
        if override := os.environ.get("CODEX_HOME", "").strip():
            return Path(override).expanduser()
    return base / ".codex"


def load_codex_config(home: Path | None = None) -> dict:
    """Parse ``config.toml`` under Codex home via ``tomllib``, returning ``{}`` if missing/invalid."""
    cfg_path = codex_home_dir(home) / "config.toml"
    if not cfg_path.is_file():
        return {}
    try:
        data = tomllib.loads(cfg_path.read_text(encoding="utf-8", errors="replace"))
        return data if isinstance(data, dict) else {}
    except (OSError, tomllib.TOMLDecodeError):
        return {}


def _codex_version_sort_key(ver: str) -> tuple[int, tuple[int, int, int, int, str], str]:
    """Rank cached Codex plugin version names cleanly (semver before arbitrary strings)."""
    if m := _SEMVER_RE.match(ver):
        major, minor, patch, pre = m.groups()
        # Stable release (no pre-release) sorts higher than pre-release of same tuple
        return (1, (int(major), int(minor), int(patch), 0 if pre else 1, pre or ""), ver)
    return (0, (0, 0, 0, 0, ver), ver)


def active_codex_plugin_skill_roots(home: Path | None = None) -> list[Path]:
    """Return skill roots for enabled Codex plugins (matching ``codex-rs`` selection rules)."""
    home = home or Path.home()
    cache = codex_home_dir(home) / "plugins" / "cache"
    if not cache.is_dir():
        return []

    cfg = load_codex_config(home)
    plugins_tbl = cfg.get("plugins") if isinstance(cfg, dict) else None
    if not isinstance(plugins_tbl, dict):
        # Fallback for synthetic fixtures without config.toml [plugins]
        return [p for p in sorted(cache.rglob("skills")) if p.is_dir()]

    roots: list[Path] = []
    seen_resolved: set[Path] = set()
    for plugin_id, pconf in sorted(plugins_tbl.items()):
        if not isinstance(pconf, dict) or pconf.get("enabled") is not True:
            continue
        if "@" not in plugin_id:
            continue
        plugin_name, marketplace = plugin_id.rsplit("@", 1)
        plugin_base = cache / marketplace / plugin_name
        if not plugin_base.is_dir():
            continue

        local_dir = plugin_base / "local"
        if local_dir.is_dir():
            chosen = local_dir
        else:
            candidates = [d for d in plugin_base.iterdir() if d.is_dir() and not d.name.startswith(".")]
            if not candidates:
                continue
            chosen = max(candidates, key=lambda d: _codex_version_sort_key(d.name))

        skills_dir = chosen / "skills"
        if skills_dir.is_dir():
            try:
                resolved = skills_dir.resolve()
            except OSError:
                resolved = skills_dir
            if resolved not in seen_resolved:
                seen_resolved.add(resolved)
                roots.append(skills_dir)
    return roots


def _codex_openai_yaml_meta(skill_dir: Path) -> tuple[bool, str | None]:
    """Read ``policy.allow_implicit_invocation`` and ``interface.short_description`` from ``agents/openai.yaml``."""
    cfg_file = skill_dir / "agents" / "openai.yaml"
    if not cfg_file.is_file():
        return True, None
    try:
        lines = cfg_file.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return True, None

    allow_implicit = True
    short_desc: str | None = None
    section: str | None = None
    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if indent == 0 and stripped.endswith(":"):
            section = stripped[:-1].strip().lower()
            continue
        if ":" not in stripped:
            continue
        key, val = stripped.split(":", 1)
        key = key.strip().lower()
        val = val.split("#", 1)[0].strip() if not (val.strip().startswith('"') or val.strip().startswith("'")) else val.strip()
        if (section == "policy" or section is None) and key == "allow_implicit_invocation":
            low = val.strip("'\"").lower()
            if low == "false":
                allow_implicit = False
            elif low == "true":
                allow_implicit = True
        elif section == "interface" and key == "short_description":
            if len(val) >= 2 and val[0] == val[-1] and val[0] in ('"', "'"):
                val = val[1:-1]
            if val:
                short_desc = val
    return allow_implicit, short_desc


def _codex_disabled_skill_names(codex_cfg: dict, visible: dict[str, SkillEntry], home: Path) -> set[str]:
    """Evaluate ordered ``[[skills.config]]`` rules and return skill names disabled for Codex."""
    skills_tbl = codex_cfg.get("skills") if isinstance(codex_cfg, dict) else None
    if not isinstance(skills_tbl, dict):
        return set()
    rules = skills_tbl.get("config")
    if not isinstance(rules, list):
        return set()

    paths_by_name: dict[str, set[str]] = {}
    for sname, e in visible.items():
        cand = {os.path.abspath(e.path), os.path.abspath(Path(e.path) / "SKILL.md")}
        if e.real_path:
            cand.add(os.path.abspath(e.real_path))
            cand.add(os.path.abspath(Path(e.real_path) / "SKILL.md"))
        paths_by_name[sname] = cand

    disabled: set[str] = set()
    for rule in rules:
        if not isinstance(rule, dict):
            continue
        enabled = bool(rule.get("enabled", True))
        raw_path = rule.get("path")
        raw_name = rule.get("name")
        matched: list[str] = []
        if raw_path:
            r_str = str(raw_path).strip()
            if r_str.startswith("~/"):
                exp = str(home / r_str[2:])
            elif r_str == "~":
                exp = str(home)
            else:
                exp = os.path.expanduser(r_str)
            norm = os.path.abspath(exp)
            matched = [sname for sname, cands in paths_by_name.items() if norm in cands]
        elif raw_name:
            name_str = str(raw_name).strip()
            if name_str in visible:
                matched = [name_str]
        for sname in matched:
            if enabled:
                disabled.discard(sname)
            else:
                disabled.add(sname)
    return disabled


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
    config_data = load_jsonc(home / ".gemini" / "config" / "config.json")
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
            manifest = find_agy_plugin_manifest(plugin_dir)
            state = plugins_state.get(plugin_dir.name)
            if isinstance(state, dict) and "enabled" in state:
                enabled = bool(state["enabled"])
            else:
                enabled = not bool((manifest or {}).get("disabled", False))
            if enabled:
                _append_dirs(agy_plugin_skill_dirs(plugin_dir, manifest))

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
                        agy_plugin_skill_dirs(plugin_dir, find_agy_plugin_manifest(plugin_dir))
                    )

    return roots


def _resolve_manifest_entry(
    raw_path: str, base_dir: Path, repo_root: Path | None
) -> tuple[Path | None, str | None]:
    """Resolve an entry or inherit path from a skills.json/plugins.json manifest.

    Returns ``(resolved_path, error_kind)``.
    """
    if not raw_path or not isinstance(raw_path, str):
        return None, "missing-target"
    if repo_root is not None:
        if raw_path.startswith("~") or Path(raw_path).is_absolute():
            return None, "workspace-escape"
        repo_real = repo_root.resolve()
        candidate = (base_dir / raw_path).resolve()
        if not candidate.exists():
            fallback = (repo_root / raw_path).resolve()
            if fallback.exists():
                candidate = fallback
        if not candidate.is_relative_to(repo_real):
            return None, "workspace-escape"
        if not candidate.exists():
            return None, "missing-target"
        return candidate, None

    expanded = Path(raw_path).expanduser()
    target = expanded.resolve() if expanded.is_absolute() else (base_dir / expanded).resolve()
    if not target.exists():
        return None, "missing-target"
    return target, None


def _expand_manifest(
    manifest_path: Path,
    *,
    kind: str,
    repo_root: Path | None,
    visited: set[Path],
    is_plugins: bool,
    issues: list[ManifestIssue] | None = None,
) -> list[tuple[Path, str]]:
    """Recursively expand an Antigravity ``skills.json`` or ``plugins.json`` manifest."""
    if not manifest_path.is_file():
        return []
    resolved_manifest = manifest_path.resolve()
    if resolved_manifest in visited:
        return []
    if repo_root is not None and not resolved_manifest.is_relative_to(repo_root.resolve()):
        if issues is not None:
            issues.append(ManifestIssue(str(manifest_path), str(manifest_path), "workspace-escape"))
        return []
    visited.add(resolved_manifest)

    data = load_jsonc(resolved_manifest)
    if not isinstance(data, dict):
        if issues is not None:
            issues.append(ManifestIssue(str(manifest_path), "", "parse-error"))
        return []

    base_dir = manifest_path.parent.parent if repo_root is not None else manifest_path.parent
    results: list[tuple[Path, str]] = []

    inherits = data.get("inherits")
    if isinstance(inherits, list):
        for item in inherits:
            if not isinstance(item, dict):
                continue
            raw = item.get("path", "")
            inherited, err = _resolve_manifest_entry(raw, base_dir, repo_root)
            if err and issues is not None:
                issues.append(ManifestIssue(str(manifest_path), str(raw), err))
            if inherited is not None:
                results.extend(
                    _expand_manifest(
                        inherited,
                        kind=kind,
                        repo_root=repo_root,
                        visited=visited,
                        is_plugins=is_plugins,
                        issues=issues,
                    )
                )

    entries = data.get("entries")
    if isinstance(entries, list):
        for item in entries:
            if not isinstance(item, dict):
                continue
            raw = item.get("path", "")
            target, err = _resolve_manifest_entry(raw, base_dir, repo_root)
            if err and issues is not None:
                issues.append(ManifestIssue(str(manifest_path), str(raw), err))
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
                manifest = find_agy_plugin_manifest(child)
                if manifest is not None or (child / "skills").is_dir():
                    for skill_dir in agy_plugin_skill_dirs(child, manifest):
                        if repo_root is None or skill_dir.resolve().is_relative_to(repo_root.resolve()):
                            results.append((skill_dir, "plugin-manifest"))

    return results


def antigravity_manifest_skill_roots(
    home: Path,
    repos: list[Path],
    issues: list[ManifestIssue] | None = None,
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
            issues=issues,
        )
    )
    results.extend(
        _expand_manifest(
            global_root / "plugins.json",
            kind="plugin-manifest",
            repo_root=None,
            visited=visited,
            is_plugins=True,
            issues=issues,
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
                    issues=issues,
                )
            )
            results.extend(
                _expand_manifest(
                    dot_path / "plugins.json",
                    kind="plugin-manifest",
                    repo_root=repo,
                    visited=visited,
                    is_plugins=True,
                    issues=issues,
                )
            )

    return results


def _add_discovery_root(
    roots: dict[str, DiscoveryRoot],
    root: Path,
    root_kind: str,
    scope: str,
    *,
    agent_ids: Iterable[str] = (),
    supports_nested_categories: bool = False,
    is_primary: bool = True,
) -> None:
    """Register an existing root once per resolved directory, merging reader agent IDs."""
    expanded = root.expanduser()
    if not expanded.is_dir():
        return
    if expanded.is_symlink():
        try:
            target = expanded.resolve()
        except OSError:
            target = None
        if target is not None:
            for existing in roots.values():
                try:
                    if existing.path.resolve() == target:
                        for aid in agent_ids:
                            if aid not in existing.agent_ids:
                                existing.agent_ids.append(aid)
                        if supports_nested_categories:
                            existing.supports_nested_categories = True
                        return
                except OSError:
                    continue

    key = str(expanded.absolute())
    if key not in roots:
        roots[key] = DiscoveryRoot(
            path=expanded,
            root_kind=root_kind,
            scope=scope,
            agent_ids=list(dict.fromkeys(agent_ids)),
            supports_nested_categories=supports_nested_categories,
            is_primary=is_primary,
        )
    else:
        existing = roots[key]
        for aid in agent_ids:
            if aid not in existing.agent_ids:
                existing.agent_ids.append(aid)
        if supports_nested_categories:
            existing.supports_nested_categories = True


def _home_path(raw: str, home: Path, agent_cfg: dict | None = None) -> Path:
    """Expand a path honoring a custom ``home`` cleanly in tests and live runs."""
    if home != Path.home():
        if raw == "~/.config" or raw.startswith("~/.config/"):
            xdg = os.environ.get("XDG_CONFIG_HOME", "").strip()
            if xdg:
                return Path(xdg + raw[len("~/.config"):])
        if agent_cfg and (home_env := agent_cfg.get("home_env")):
            env_var, default_home = home_env
            override = os.environ.get(env_var, "").strip()
            if override and (raw == default_home or raw.startswith(default_home + "/")):
                return Path(override + raw[len(default_home):])
        if raw.startswith("~/"):
            return home / raw[2:]
        if raw == "~":
            return home
        return Path(raw)
    return expand_path(raw, agent_cfg)


def discover_roots(
    *,
    scope: str = "all",
    cwd: Path | None = None,
    home: Path | None = None,
    agents_filter: list[str] | None = None,
    source_roots: list[Path] | None = None,
    include_plugins: bool = True,
    include_builtins: bool = False,
    query_cli: bool = False,
    scan_skills_dirs: bool = False,
    scan_depth: int = 3,
    manifest_issues: list[ManifestIssue] | None = None,
) -> list[DiscoveryRoot]:
    """Build bounded discovery roots for global, local, plugin, manifest, and warehouse layers."""
    home = home or Path.home()
    cwd = (cwd or Path.cwd()).resolve()
    roots: dict[str, DiscoveryRoot] = {}

    if agents_filter:
        active_agents = [canonical_agent_id(a) for a in agents_filter if canonical_agent_id(a) in AGENTS]
    else:
        # When home is default, rely on detect_installed_agents + always include universal/porch installed dirs
        active_agents = list(AGENTS.keys())

    # Attach only agents whose canonical global_dir IS ~/.agents/skills; agents with
    # reads_shared_global=True (antigravity-cli, grok, devin, omp, optional hermes)
    # resolve shared visibility as "shrd" without misreporting ~/.agents/skills as their own copy.
    primary_shared_agents = [
        aid for aid in active_agents if AGENTS[aid]["global_dir"] == SHARED_GLOBAL
    ]

    repo = find_repo_root(cwd)
    repos = [repo] if repo is not None else []

    if scope in ("global", "all"):
        _add_discovery_root(
            roots,
            home / ".agents" / "skills",
            "canonical-user",
            "global",
            agent_ids=primary_shared_agents,
        )
        for aid in active_agents:
            cfg = AGENTS[aid]
            primary = _home_path(cfg["global_dir"], home, cfg)
            _add_discovery_root(
                roots,
                primary,
                "canonical-user" if cfg["global_dir"] == SHARED_GLOBAL else "agent-user",
                "global",
                agent_ids=[aid],
                supports_nested_categories=bool(cfg.get("supports_nested_categories")),
                is_primary=True,
            )
            for extra in cfg.get("extra_global_dirs", []):
                ep = _home_path(extra, home, cfg)
                _add_discovery_root(
                    roots,
                    ep,
                    "agent-user",
                    "global",
                    agent_ids=[aid],
                    supports_nested_categories=bool(cfg.get("supports_nested_categories")),
                    is_primary=False,
                )

        if include_plugins:
            for skill_root in active_codex_plugin_skill_roots(home):
                _add_discovery_root(roots, skill_root, "plugin-cache", "global", agent_ids=["codex"])
            if query_cli:
                for skill_root in active_claude_plugin_skill_roots():
                    _add_discovery_root(roots, skill_root, "plugin-cache-active", "global", agent_ids=["claude-code"])
            for skill_root in active_antigravity_plugin_skill_roots(home, query_cli=query_cli):
                _add_discovery_root(
                    roots,
                    skill_root,
                    "plugin-antigravity",
                    "global",
                    agent_ids=["antigravity", "antigravity-cli"],
                )

        if include_builtins:
            agy_builtin = home / ".gemini" / "antigravity" / "builtin" / "skills"
            if agy_builtin.is_dir():
                _add_discovery_root(
                    roots,
                    agy_builtin,
                    "builtin",
                    "global",
                    agent_ids=["antigravity", "antigravity-cli"],
                )

    if scope in ("local", "all"):
        ancestors = ancestor_chain(cwd, repo)
        for anc in ancestors:
            seen_rel: set[str] = set()
            for aid in active_agents:
                cfg = AGENTS[aid]
                rel_dirs = [cfg["project_dir"], *cfg.get("extra_project_dirs", [])]
                for rel in rel_dirs:
                    readers = [
                        a for a in active_agents
                        if rel in (AGENTS[a]["project_dir"], *AGENTS[a].get("extra_project_dirs", []))
                    ]
                    if rel in seen_rel:
                        continue
                    seen_rel.add(rel)
                    # Only include openclaw-style bare "skills" at repo/plugin roots explicitly below
                    if rel == "skills":
                        continue
                    _add_discovery_root(
                        roots,
                        anc / rel,
                        "repo",
                        "local",
                        agent_ids=readers,
                        supports_nested_categories=any(AGENTS[r].get("supports_nested_categories") for r in readers),
                    )
            for dot_dir in AGY_DOT_DIRS:
                ws_plugins = anc / dot_dir / "plugins"
                if ws_plugins.is_dir():
                    for plugin_dir in sorted(ws_plugins.iterdir()):
                        if plugin_dir.is_dir():
                            manifest = find_agy_plugin_manifest(plugin_dir)
                            for skill_dir in agy_plugin_skill_dirs(plugin_dir, manifest):
                                _add_discovery_root(
                                    roots,
                                    skill_dir,
                                    "plugin-workspace",
                                    "local",
                                    agent_ids=["antigravity", "antigravity-cli"],
                                )

        if repo is not None:
            is_plugin_repo = (repo / ".claude-plugin" / "plugin.json").is_file() or any(
                (repo / manifest).is_file() for manifest in AGY_PLUGIN_MANIFESTS
            )
            if (repo / "SKILL.md").is_file():
                _add_discovery_root(roots, repo, "repo-single-skill", "local", agent_ids=[])
            if is_plugin_repo or (repo / "skills").is_dir():
                _add_discovery_root(
                    roots,
                    repo / "skills",
                    "plugin-source" if is_plugin_repo else "repo-skills-dir",
                    "local",
                    agent_ids=["openclaw"] if "openclaw" in active_agents else [],
                )
        elif (cwd / "SKILL.md").is_file():
            _add_discovery_root(roots, cwd, "repo-single-skill", "local", agent_ids=[])
        elif (cwd / "skills").is_dir():
            _add_discovery_root(roots, cwd / "skills", "repo-skills-dir", "local", agent_ids=[])

        if scan_skills_dirs:
            _scan_nested_skills_dirs(cwd, roots, max_depth=scan_depth)

    # Antigravity manifests
    manifest_roots = antigravity_manifest_skill_roots(
        home if scope in ("global", "all") else Path("/__nonexistent__"),
        repos if scope in ("local", "all") else [],
        issues=manifest_issues,
    )
    for m_root, m_kind in manifest_roots:
        m_scope = "local" if m_kind in ("manifest-workspace", "plugin-manifest") and repo and m_root.resolve().is_relative_to(repo.resolve()) else "global"
        if scope != "all" and m_scope != scope:
            continue
        _add_discovery_root(roots, m_root, m_kind, m_scope, agent_ids=["antigravity", "antigravity-cli"])

    # Optional warehouse / project source roots (for provenance & repoint recovery)
    for src_root in source_roots or []:
        _scan_warehouse_roots(src_root.expanduser(), roots)

    return list(roots.values())


def _scan_nested_skills_dirs(base: Path, roots: dict[str, DiscoveryRoot], *, max_depth: int = 3) -> None:
    """Find bounded ``skills/`` or ``.agents/skills/`` dirs inside a workspace without descending into junk."""
    base = base.resolve()

    def _walk(cur: Path, depth: int) -> None:
        if depth > max_depth:
            return
        try:
            children = sorted(cur.iterdir())
        except OSError:
            return
        for child in children:
            if not child.is_dir() or child.name in SKIP_SCAN_DIRS or child.is_symlink():
                continue
            if child.name == "skills" and depth >= 1:
                _add_discovery_root(roots, child, "repo-skills-dir", "local", agent_ids=[])
                continue
            _walk(child, depth + 1)

    _walk(base, 0)


def _scan_warehouse_roots(warehouse: Path, roots: dict[str, DiscoveryRoot]) -> None:
    """Bounded discovery of canonical source skills under a projects directory (depth <= 2)."""
    if not warehouse.is_dir():
        return
    if (warehouse / "SKILL.md").is_file():
        _add_discovery_root(roots, warehouse, "source-warehouse", "warehouse", agent_ids=[])
    if (warehouse / "skills").is_dir():
        _add_discovery_root(roots, warehouse / "skills", "source-warehouse", "warehouse", agent_ids=[])
    try:
        children = sorted(warehouse.iterdir())
    except OSError:
        return
    for child in children:
        if not child.is_dir() or child.name.startswith(".") or child.name in SKIP_SCAN_DIRS:
            continue
        if (child / "SKILL.md").is_file():
            _add_discovery_root(roots, child, "source-warehouse", "warehouse", agent_ids=[])
        for sub in ("skills", ".agents/skills", ".claude/skills"):
            cand = child / sub
            if cand.is_dir():
                _add_discovery_root(roots, cand, "source-warehouse", "warehouse", agent_ids=[])


def load_skill_locks(home: Path, cwd: Path) -> tuple[dict[str, dict], list[LockfileIssue]]:
    """Load ``~/.agents/.skill-lock.json`` and workspace lockfiles, detecting orphans."""
    locks: dict[str, dict] = {}
    issues: list[LockfileIssue] = []

    user_lock = home / ".agents" / ".skill-lock.json"
    user_skills_dir = home / ".agents" / "skills"
    if user_lock.is_file():
        data = load_jsonc(user_lock)
        if not isinstance(data, dict):
            issues.append(LockfileIssue(str(user_lock), "", "", "", "invalid-lockfile"))
        else:
            skills = data.get("skills", {})
            if isinstance(skills, dict):
                for sname, meta in sorted(skills.items()):
                    if not isinstance(meta, dict):
                        continue
                    locks[sname] = {**meta, "_lockfile": str(user_lock)}
                    if not (user_skills_dir / sname).exists():
                        issues.append(
                            LockfileIssue(
                                lockfile=str(user_lock),
                                skill=sname,
                                source=str(meta.get("source", "")),
                                source_url=str(meta.get("sourceUrl", "")),
                                kind="orphaned-lock-entry",
                            )
                        )

    repo = find_repo_root(cwd)
    local_lock_candidates = [cwd / "skills-lock.json"]
    if repo and repo != cwd:
        local_lock_candidates.append(repo / "skills-lock.json")
    for loc_lock in local_lock_candidates:
        if not loc_lock.is_file():
            continue
        data = load_jsonc(loc_lock)
        if not isinstance(data, dict):
            issues.append(LockfileIssue(str(loc_lock), "", "", "", "invalid-lockfile"))
            continue
        skills = data.get("skills", {})
        if isinstance(skills, dict):
            base_agents = loc_lock.parent / ".agents" / "skills"
            for sname, meta in sorted(skills.items()):
                if not isinstance(meta, dict):
                    continue
                locks.setdefault(sname, {**meta, "_lockfile": str(loc_lock)})
                if not (base_agents / sname).exists():
                    issues.append(
                        LockfileIssue(
                            lockfile=str(loc_lock),
                            skill=sname,
                            source=str(meta.get("source", "")),
                            source_url=str(meta.get("sourceUrl", "")),
                            kind="orphaned-lock-entry",
                        )
                    )
    return locks, issues


def load_hermes_bundled_manifest(home: Path) -> dict[str, str]:
    """Read ``~/.hermes/skills/.bundled_manifest`` if present (``skill_rel -> hash``)."""
    manifest = home / ".hermes" / "skills" / ".bundled_manifest"
    if not manifest.is_file():
        return {}
    entries: dict[str, str] = {}
    try:
        for line in manifest.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                k, v = line.split(":", 1)
                entries[k.strip()] = v.strip()
            elif "=" in line:
                k, v = line.split("=", 1)
                entries[k.strip()] = v.strip()
            else:
                parts = line.split()
                entries[parts[0]] = parts[1] if len(parts) > 1 else ""
    except OSError:
        return {}
    return entries


def _git_repo_info(path: Path, cache: dict[Path, tuple[str | None, bool | None]]) -> tuple[str | None, bool | None]:
    """Return cached ``(repo_dir_name@branch, None)`` via pure-Python ``.git/HEAD`` read."""
    repo = find_repo_root(path)
    if repo is None:
        return None, None
    if repo in cache:
        return cache[repo]
    branch = None
    try:
        head = (repo / ".git" / "HEAD")
        if head.is_file():
            txt = head.read_text(encoding="utf-8", errors="replace").strip()
            if txt.startswith("ref: refs/heads/"):
                branch = txt[len("ref: refs/heads/"):]
            else:
                branch = txt[:8]
    except OSError:
        pass
    label = f"{repo.name}@{branch}" if branch else repo.name
    cache[repo] = (label, None)
    return cache[repo]


def _check_skill_md_integrity(skill_dir: Path, content: str, metadata: dict[str, str], body: str) -> list[dict]:
    """Run fast, zero-false-positive integrity and security checks on SKILL.md."""
    issues: list[dict] = []
    # Check frontmatter presence
    if not content.lstrip("\ufeff").startswith("---"):
        issues.append({"severity": "error", "rule": "missing-frontmatter", "message": "SKILL.md has no YAML frontmatter"})
    else:
        raw_name = metadata.get("name", "").strip()
        raw_desc = metadata.get("description", "").strip()
        if not raw_name:
            issues.append({"severity": "error", "rule": "name-required", "message": "Frontmatter 'name' is missing or empty"})
        elif raw_name != skill_dir.name:
            issues.append({"severity": "warning", "rule": "name-dir-mismatch", "message": f"Frontmatter name '{raw_name}' != folder '{skill_dir.name}'"})
        if not raw_desc:
            issues.append({"severity": "warning", "rule": "description-required", "message": "Frontmatter 'description' is empty"})
        elif len(raw_desc) > 1024:
            issues.append({"severity": "warning", "rule": "description-length", "message": f"Description is {len(raw_desc)} chars (>1024 spec cap)"})
        for field_name in ("name", "description"):
            if re.search(r"[<>]", metadata.get(field_name, "")):
                issues.append({"severity": "error", "rule": "xml-in-frontmatter", "message": f"Field '{field_name}' contains forbidden '<' or '>'"})

    # Invisible / BiDi Trojan Source characters (allow optional BOM at byte 0 only)
    check_text = content[1:] if content.startswith("\ufeff") else content
    bad_unicode = TROJAN_UNICODE_RE.search(check_text)
    if bad_unicode:
        cp = f"U+{ord(bad_unicode.group(0)):04X}"
        issues.append({"severity": "error", "rule": "trojan-unicode", "message": f"Hidden or BiDi Unicode control char ({cp}) in SKILL.md"})

    # Broken local markdown links
    in_fence = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in _LOCAL_MD_LINK_RE.finditer(line):
            target = match.group(1).strip()
            if not target or target.startswith(_EXTERNAL_SCHEMES) or target.startswith("<"):
                continue
            rel = target.split("#", 1)[0].split("?", 1)[0].strip()
            if not rel or " " in rel:
                continue
            resolved = skill_dir / rel
            if not resolved.exists():
                issues.append({"severity": "warning", "rule": "broken-internal-ref", "message": f"Broken link '{rel}' in SKILL.md"})

    return issues


def scan_entry(
    entry_path: Path,
    root: DiscoveryRoot,
    *,
    category: str | None = None,
    locks: dict[str, dict] | None = None,
    hermes_bundled: dict[str, str] | None = None,
    git_cache: dict[Path, tuple[str | None, bool | None]] | None = None,
) -> SkillEntry:
    """Build a complete ``SkillEntry`` for one skill directory or broken symlink."""
    locks = locks or {}
    hermes_bundled = hermes_bundled or {}
    git_cache = git_cache if git_cache is not None else {}

    is_sym, hops, resolved, raw_target, is_broken, broken_reason = walk_symlink_chain(entry_path)
    is_rel_sym = bool(is_sym and raw_target and not Path(raw_target).is_absolute())
    is_loop = bool(broken_reason and "loop" in broken_reason)
    issues: list[dict] = []

    if is_broken:
        issues.append({"severity": "error", "rule": "broken-symlink", "message": f"Broken symlink -> {raw_target or '?'} ({broken_reason})"})
        return SkillEntry(
            name=entry_path.name,
            dir_name=entry_path.name,
            path=str(entry_path.absolute()),
            real_path=None,
            root=str(root.path.absolute()),
            root_kind=root.root_kind,
            scope=root.scope,
            agent_ids=list(root.agent_ids),
            category=category,
            is_symlink=is_sym,
            raw_target=raw_target,
            is_relative_symlink=is_rel_sym,
            hop_count=hops,
            is_broken=True,
            broken_reason=broken_reason,
            is_loop=is_loop,
            is_plugin=root.root_kind.startswith("plugin") and root.root_kind != "plugin-source",
            is_builtin=root.root_kind == "builtin",
            is_backup=bool(BACKUP_RE.search(entry_path.name)),
            issues=issues,
        )

    assert resolved is not None
    skill_md = resolved / "SKILL.md"
    if not skill_md.is_file():
        issues.append({"severity": "error", "rule": "ghost-dir", "message": "Directory has no SKILL.md (zombie/ghost directory)"})
        return SkillEntry(
            name=entry_path.name,
            dir_name=entry_path.name,
            path=str(entry_path.absolute()),
            real_path=str(resolved),
            root=str(root.path.absolute()),
            root_kind=root.root_kind,
            scope=root.scope,
            agent_ids=list(root.agent_ids),
            category=category,
            is_symlink=is_sym,
            raw_target=raw_target,
            is_relative_symlink=is_rel_sym,
            hop_count=hops,
            is_ghost=True,
            is_plugin=root.root_kind.startswith("plugin") and root.root_kind != "plugin-source",
            is_builtin=root.root_kind == "builtin",
            is_backup=bool(BACKUP_RE.search(entry_path.name)),
            issues=issues,
        )

    content = read_skill_text(skill_md)
    metadata, body = parse_skill_md(content)
    sname = skill_name(metadata, entry_path)
    desc = metadata.get("description", "").strip()
    issues.extend(_check_skill_md_integrity(resolved, content, metadata, body))

    if hops >= 2:
        issues.append({"severity": "warning", "rule": "chained-symlink", "message": f"Chained {hops}-hop symlink -> {raw_target} -> {resolved}"})
    elif is_rel_sym:
        issues.append({"severity": "info", "rule": "relative-symlink", "message": f"Relative symlink -> {raw_target}"})

    # Provenance & bundle checks
    is_bundled = False
    provenance = "local-unmanaged"
    git_label, git_dirty = _git_repo_info(resolved, git_cache)
    hermes_key = f"{category}/{entry_path.name}" if category else entry_path.name
    if root.root_kind == "builtin":
        provenance = "builtin:antigravity"
    elif "hermes-agent" in root.agent_ids and (hermes_key in hermes_bundled or entry_path.name in hermes_bundled):
        is_bundled = True
        provenance = "bundled:hermes"
    elif root.root_kind.startswith("plugin") and root.root_kind != "plugin-source":
        provenance = f"plugin:{root.path.parent.name}"
    elif git_label:
        provenance = f"git:{git_label}{'*' if git_dirty else ''}"
    elif sname in locks:
        provenance = f"skills-lock:{locks[sname].get('source', '?')}"

    return SkillEntry(
        name=sname,
        dir_name=entry_path.name,
        path=str(entry_path.absolute()),
        real_path=str(resolved),
        root=str(root.path.absolute()),
        root_kind=root.root_kind,
        scope=root.scope,
        agent_ids=list(root.agent_ids),
        category=category,
        version=metadata.get("version"),
        description=desc,
        meta_chars=len(sname) + len(desc),
        is_symlink=is_sym,
        raw_target=raw_target,
        is_relative_symlink=is_rel_sym,
        hop_count=hops,
        is_plugin=root.root_kind.startswith("plugin") and root.root_kind != "plugin-source",
        is_bundled=is_bundled,
        is_builtin=root.root_kind == "builtin",
        is_backup=bool(BACKUP_RE.search(entry_path.name)),
        body_lines=len(body.splitlines()) if body else 0,
        issues=issues,
        provenance=provenance,
        git_repo=git_label,
        git_dirty=git_dirty,
    )


def _is_claude_synced_dir(child: Path, root: DiscoveryRoot) -> bool:
    """True for Claude Code's download-only cloud-synced skills container (~/.claude/skills/synced)."""
    return (
        "claude-code" in root.agent_ids
        and child.name == "synced"
        and not child.is_symlink()
        and child.is_dir()
        and not (child / "SKILL.md").is_file()
    )


def scan_topology(
    roots: list[DiscoveryRoot],
    *,
    home: Path | None = None,
    cwd: Path | None = None,
) -> tuple[list[SkillEntry], list[LockfileIssue]]:
    """Scan every child across ``roots`` (honoring Hermes depth-2 categories & ghost dirs)."""
    home = home or Path.home()
    cwd = cwd or Path.cwd()
    locks, lock_issues = load_skill_locks(home, cwd)
    hermes_bundled = load_hermes_bundled_manifest(home)
    git_cache: dict[Path, tuple[str | None, bool | None]] = {}

    entries: list[SkillEntry] = []
    seen_paths: set[str] = set()

    for root in roots:
        if not root.path.is_dir():
            continue
        if (root.path / "SKILL.md").is_file():
            loc = str(root.path.absolute())
            if loc not in seen_paths:
                seen_paths.add(loc)
                entries.append(
                    scan_entry(root.path, root, locks=locks, hermes_bundled=hermes_bundled, git_cache=git_cache)
                )
            continue

        try:
            children = sorted(root.path.iterdir())
        except OSError:
            continue
        for child in children:
            if child.name in SKIP_CHILD_NAMES or child.name.startswith("."):
                continue
            if _is_claude_synced_dir(child, root):
                continue
            if not (child.is_symlink() or child.is_dir()):
                continue

            # Hermes depth-2 category folders (only for non-symlink dirs lacking SKILL.md)
            if (
                root.supports_nested_categories
                and not child.is_symlink()
                and child.is_dir()
                and not (child / "SKILL.md").is_file()
            ):
                nested_found = 0
                try:
                    subchildren = sorted(child.iterdir())
                except OSError:
                    subchildren = []
                for sub in subchildren:
                    if sub.name in SKIP_CHILD_NAMES or sub.name.startswith("."):
                        continue
                    if sub.is_symlink() or (sub.is_dir() and (sub / "SKILL.md").is_file()):
                        loc = str(sub.absolute())
                        if loc not in seen_paths:
                            seen_paths.add(loc)
                            entries.append(
                                scan_entry(
                                    sub,
                                    root,
                                    category=child.name,
                                    locks=locks,
                                    hermes_bundled=hermes_bundled,
                                    git_cache=git_cache,
                                )
                            )
                            nested_found += 1
                if nested_found > 0:
                    continue

            loc = str(child.absolute())
            if loc in seen_paths:
                continue
            seen_paths.add(loc)
            entries.append(
                scan_entry(child, root, locks=locks, hermes_bundled=hermes_bundled, git_cache=git_cache)
            )

    _annotate_broken_hints(entries)
    return entries, lock_issues


def _repo_deleted_renamed_map(repo: Path, repo_index_cache: dict[Path, dict[str, str]]) -> dict[str, str]:
    """Run at most one batched git log query per repo to map deleted/renamed skill dirs."""
    if repo in repo_index_cache:
        return repo_index_cache[repo]
    mapping: dict[str, str] = {}
    try:
        res = subprocess.run(
            ["git", "-C", str(repo), "log", "-n", "40", "--diff-filter=DR", "--name-status", "--format="],
            capture_output=True,
            text=True,
            timeout=3,
        )
        if res.returncode == 0 and res.stdout:
            for line in res.stdout.splitlines():
                parts = line.split("\t")
                if not parts:
                    continue
                status = parts[0]
                if status.startswith("R") and len(parts) >= 3:
                    old_p, new_p = parts[1], parts[2]
                    if old_p.endswith("/SKILL.md"):
                        old_dir = old_p[:-len("/SKILL.md")]
                        new_dir = new_p[:-len("/SKILL.md")] if new_p.endswith("/SKILL.md") else new_p
                        mapping.setdefault(old_dir, f"renamed in {repo.name} -> {new_dir}")
                elif status == "D" and len(parts) >= 2 and parts[1].endswith("/SKILL.md"):
                    old_dir = parts[1][:-len("/SKILL.md")]
                    mapping.setdefault(old_dir, f"removed or consolidated in {repo.name} git history")
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    repo_index_cache[repo] = mapping
    return mapping


def _git_rename_hint(raw_target: str, repo_index_cache: dict[Path, dict[str, str]]) -> str | None:
    """Check if a broken symlink's target inside a local git repo was deleted or renamed."""
    target_path = Path(raw_target)
    if not target_path.is_absolute():
        return None
    repo = find_repo_root(target_path.parent)
    if repo is None:
        return None
    try:
        rel = target_path.relative_to(repo).as_posix().rstrip("/")
    except ValueError:
        return None
    return _repo_deleted_renamed_map(repo, repo_index_cache).get(rel)


def _annotate_broken_hints(entries: list[SkillEntry]) -> None:
    """Attach safe repoint candidates (exact name match) or rename warnings to broken symlinks."""
    live_by_name: dict[str, list[SkillEntry]] = defaultdict(list)
    seen_real: dict[str, set[str]] = defaultdict(set)
    for e in entries:
        if e.is_broken or e.is_ghost or e.is_builtin or not e.real_path:
            continue
        if e.real_path in seen_real[e.name]:
            continue
        seen_real[e.name].add(e.real_path)
        live_by_name[e.name].append(e)

    repo_index_cache: dict[Path, dict[str, str]] = {}
    for e in entries:
        if not e.is_broken:
            continue
        for cand in live_by_name.get(e.dir_name, []):
            e.repoint_candidates.append({
                "path": cand.real_path,
                "root_kind": cand.root_kind,
                "provenance": cand.provenance,
            })
        if e.raw_target:
            e.rename_hint = _git_rename_hint(e.raw_target, repo_index_cache)


def ensure_hash(entry: SkillEntry) -> str | None:
    """Compute SHA-256 directory hash lazily for live skill directories."""
    if entry.is_broken or entry.is_ghost or not entry.real_path:
        return None
    if entry.content_hash is None:
        entry.content_hash = hash_skill_directory(Path(entry.real_path))
    return entry.content_hash


def _diff_summary(a: SkillEntry, b: SkillEntry) -> dict:
    """Compute compact deterministic diff between two divergent skill directories."""
    if not a.real_path or not b.real_path:
        return {}
    pa, pb = Path(a.real_path), Path(b.real_path)
    fa = {p.relative_to(pa).as_posix(): p for p in pa.rglob("*") if p.is_file() and not any(part in IGNORED_PARTS for part in p.relative_to(pa).parts)}
    fb = {p.relative_to(pb).as_posix(): p for p in pb.rglob("*") if p.is_file() and not any(part in IGNORED_PARTS for part in p.relative_to(pb).parts)}
    only_a = sorted(set(fa) - set(fb))
    only_b = sorted(set(fb) - set(fa))
    changed = [k for k in sorted(set(fa) & set(fb)) if fa[k].read_bytes() != fb[k].read_bytes()]
    return {
        "only_in_first": only_a[:10],
        "only_in_second": only_b[:10],
        "modified_files": changed[:10],
        "body_lines_delta": abs(a.body_lines - b.body_lines),
    }


def classify_groups(entries: list[SkillEntry]) -> dict:
    """Run 4-axis deterministic duplicate/drift analysis across live (non-warehouse) entries."""
    active = [
        e for e in entries
        if not e.is_broken and not e.is_ghost and not e.is_builtin and e.root_kind != "source-warehouse"
    ]

    by_name: dict[str, list[SkillEntry]] = defaultdict(list)
    by_dir: dict[str, list[SkillEntry]] = defaultdict(list)
    by_slug: dict[str, list[SkillEntry]] = defaultdict(list)
    by_md_hash: dict[str, list[SkillEntry]] = defaultdict(list)

    for e in active:
        by_name[e.name].append(e)
        by_dir[e.dir_name].append(e)
        by_slug[normalized_slug(e.name)].append(e)
        if e.real_path:
            try:
                md_bytes = (Path(e.real_path) / "SKILL.md").read_bytes()
                by_md_hash[hashlib.sha256(md_bytes).hexdigest()].append(e)
            except OSError:
                pass

    name_groups: list[dict] = []
    for sname, grp in sorted(by_name.items()):
        if len(grp) < 2:
            # Single entry, check if chained hop
            e0 = grp[0]
            if e0.hop_count >= 2 or e0.is_relative_symlink:
                name_groups.append({
                    "name": sname,
                    "status": "chained-hop",
                    "requires_decision": False,
                    "entries": [asdict(e0)],
                })
            continue

        reals = {e.real_path for e in grp}
        if len(reals) == 1:
            has_hop = any(e.hop_count >= 2 or e.is_relative_symlink for e in grp)
            status = "chained-hop" if has_hop else "alias"
            name_groups.append({
                "name": sname,
                "status": status,
                "requires_decision": False,
                "entries": [asdict(e) for e in grp],
            })
            continue

        if any(e.is_backup for e in grp):
            status = "stale-backup"
        else:
            hashes = {ensure_hash(e) for e in grp}
            scopes = {e.scope for e in grp}
            if all(e.is_plugin for e in grp):
                status = "managed-plugin-replica" if len(hashes) == 1 else "managed-plugin-divergent"
            elif "local" in scopes and "global" in scopes:
                status = "local-shadows-global-identical" if len(hashes) == 1 else "local-shadows-global-divergent"
            elif len(hashes) == 1:
                status = "replica"
            elif any(e.is_plugin for e in grp):
                status = "namespaced-divergent"
            else:
                status = "divergent"

        diff_info = {}
        if "divergent" in status:
            # Compare distinct real paths (first two)
            distinct: list[SkillEntry] = []
            seen_r: set[str] = set()
            for e in grp:
                if e.real_path and e.real_path not in seen_r:
                    seen_r.add(e.real_path)
                    distinct.append(e)
            if len(distinct) >= 2:
                diff_info = _diff_summary(distinct[0], distinct[1])

        name_groups.append({
            "name": sname,
            "status": status,
            "requires_decision": status in {
                "stale-backup",
                "namespaced-divergent",
                "divergent",
                "local-shadows-global-divergent",
            },
            "diff": diff_info,
            "entries": [asdict(e) for e in grp],
        })

    # Axis 2: folder name matches with different frontmatter names
    dir_conflicts: list[dict] = []
    for dname, grp in sorted(by_dir.items()):
        distinct_names = {e.name for e in grp}
        if len(distinct_names) > 1:
            dir_conflicts.append({
                "dir_name": dname,
                "names": sorted(distinct_names),
                "paths": [e.path for e in grp],
            })

    # Axis 3: normalized slug matches across different exact names
    slug_collisions: list[dict] = []
    for slug, grp in sorted(by_slug.items()):
        distinct_names = sorted({e.name for e in grp})
        if len(distinct_names) > 1:
            slug_collisions.append({
                "slug": slug,
                "names": distinct_names,
                "paths": sorted({e.path for e in grp}),
            })

    # Axis 4: exact content hash matches with different frontmatter names
    # (pre-filtered by identical SKILL.md bytes so unique skills avoid full tree hashing)
    renamed_clones: list[dict] = []
    by_full_hash: dict[str, list[SkillEntry]] = defaultdict(list)
    for _, md_grp in sorted(by_md_hash.items()):
        if len({e.name for e in md_grp}) <= 1:
            continue
        for e in md_grp:
            h = ensure_hash(e)
            if h:
                by_full_hash[h].append(e)
    for h, grp in sorted(by_full_hash.items()):
        distinct_names = sorted({e.name for e in grp})
        if len(distinct_names) > 1:
            renamed_clones.append({
                "hash": h[:12],
                "names": distinct_names,
                "paths": sorted({e.path for e in grp}),
            })

    return {
        "by_name": name_groups,
        "by_dir_mismatch": dir_conflicts,
        "by_slug_collision": slug_collisions,
        "by_hash_renamed_clone": renamed_clones,
    }


def compute_agent_context_budgets(
    entries: list[SkillEntry],
    agent_ids: list[str],
    *,
    home: Path | None = None,
) -> dict[str, dict]:
    """Estimate startup catalog footprint (`name + description`) per agent."""
    home = home or Path.home()
    codex_cfg = load_codex_config(home) if "codex" in agent_ids else {}
    budgets: dict[str, dict] = {}
    for aid in agent_ids:
        cfg = get_agent_config(aid)
        if not cfg:
            continue
        # Deduplicate effective skills visible to this agent by name (highest priority first)
        visible: dict[str, SkillEntry] = {}
        readable_dirs = {str(p.expanduser().absolute()) for p in _agent_readable_dirs(aid, home)}
        for e in entries:
            if e.is_broken or e.is_ghost or e.root_kind == "source-warehouse":
                continue
            if aid in e.agent_ids or e.root in readable_dirs:
                visible.setdefault(e.name, e)

        disabled_count = 0
        explicit_only_count = 0
        eff_desc_by_name: dict[str, int] = {}
        eff_meta_by_name: dict[str, int] = {}

        if aid == "codex":
            codex_disabled = _codex_disabled_skill_names(codex_cfg, visible, home)
            disabled_count = len(codex_disabled)
            kept: dict[str, SkillEntry] = {}
            for sname, e in visible.items():
                if sname in codex_disabled:
                    continue
                allow_impl = True
                short_desc: str | None = None
                if e.real_path:
                    allow_impl, short_desc = _codex_openai_yaml_meta(Path(e.real_path))
                if not allow_impl:
                    explicit_only_count += 1
                    continue
                d_len = len(short_desc) if short_desc is not None else len(e.description)
                eff_desc_by_name[sname] = d_len
                eff_meta_by_name[sname] = len(e.name) + d_len
                kept[sname] = e
            items = list(kept.values())
        else:
            items = list(visible.values())
            for e in items:
                eff_desc_by_name[e.name] = len(e.description)
                eff_meta_by_name[e.name] = e.meta_chars

        total_chars = sum(eff_meta_by_name[e.name] for e in items)
        est_tokens = total_chars // 4
        caps = AGENT_CONTEXT_CAPS.get(aid, {})
        warnings: list[str] = []
        if per_cap := caps.get("per_skill_chars"):
            over = [e.name for e in items if eff_desc_by_name[e.name] > int(per_cap)]
            if over:
                warnings.append(f"{len(over)} skill(s) exceed {per_cap}-char description truncation cap: {', '.join(over[:4])}")
        if cat_chars := caps.get("catalog_chars"):
            if total_chars > int(cat_chars):
                warnings.append(f"Total metadata {total_chars} chars exceeds ~{cat_chars}-char budget")
        if cat_toks := caps.get("catalog_tokens"):
            tok_limit = int(cat_toks)
            if aid == "codex":
                skills_tbl = codex_cfg.get("skills") if isinstance(codex_cfg, dict) else None
                if isinstance(skills_tbl, dict) and isinstance(skills_tbl.get("max_context_tokens"), int) and skills_tbl["max_context_tokens"] > 0:
                    max_cfg = int(caps.get("max_configurable_tokens", 10000))
                    tok_limit = min(int(skills_tbl["max_context_tokens"]), max_cfg)
            if est_tokens > tok_limit:
                if aid == "codex":
                    warnings.append(
                        f"Total metadata ~{est_tokens} tok ({total_chars} chars) exceeds ~{tok_limit}-tok budget "
                        "(set [skills] max_context_tokens = 10000, [[skills.config]] enabled = false, or agents/openai.yaml allow_implicit_invocation: false)"
                    )
                else:
                    warnings.append(f"Total metadata ~{est_tokens} tokens exceeds ~{tok_limit}-token budget")
        top_heavy = sorted(items, key=lambda x: eff_meta_by_name[x.name], reverse=True)[:5]
        row_data: dict = {
            "display_name": cfg["display_name"],
            "skill_count": len(items),
            "total_chars": total_chars,
            "est_tokens": est_tokens,
            "warnings": warnings,
            "top_heaviest": [{"name": e.name, "chars": eff_meta_by_name[e.name]} for e in top_heavy],
        }
        if aid == "codex":
            row_data["disabled_count"] = disabled_count
            row_data["explicit_only_count"] = explicit_only_count
        budgets[aid] = row_data
    return budgets


def _agent_readable_dirs(aid: str, home: Path) -> list[Path]:
    """Return global readable skill dirs for ``aid`` respecting custom ``home``."""
    cfg = AGENTS.get(aid)
    if not cfg:
        return []
    dirs: list[Path] = [_home_path(cfg["global_dir"], home, cfg)]
    for extra in cfg.get("extra_global_dirs", []):
        p = _home_path(extra, home, cfg)
        if p not in dirs:
            dirs.append(p)
    reads_shared = bool(cfg.get("reads_shared_global"))
    if aid == "hermes-agent" and hermes_reads_shared_global(home=home):
        reads_shared = True
    if reads_shared:
        shared = home / ".agents" / "skills"
        if shared not in dirs:
            dirs.append(shared)
    return dirs


def cell_status_for_pool(
    skill_name_key: str,
    entries_for_skill: list[SkillEntry],
    agent_ids: list[str],
    group_status: str | None,
    *,
    home: Path | None = None,
    shared_dir_entries: set[str] | None = None,
) -> str:
    """Compute a short, color-independent matrix cell status for one agent/pool."""
    home = home or Path.home()
    relevant = [e for e in entries_for_skill if any(aid in e.agent_ids for aid in agent_ids)]
    shared_dir_entries = shared_dir_entries or set()

    if not relevant:
        # Check if any agent in this pool inherits from ~/.agents/skills
        for aid in agent_ids:
            cfg = AGENTS.get(aid)
            if not cfg:
                continue
            reads_shared = bool(cfg.get("reads_shared_global")) or cfg["global_dir"] == SHARED_GLOBAL
            if aid == "hermes-agent":
                reads_shared = hermes_reads_shared_global(home=home)
            if reads_shared and skill_name_key in shared_dir_entries:
                return "shrd"
        return "—"

    if any(e.is_broken for e in relevant):
        return "BRKN"
    if any(e.is_ghost for e in relevant):
        return "GHST"
    if group_status and "local-shadows-global" in group_status and any(e.scope == "local" for e in relevant):
        return "SHDW"
    if group_status and ("divergent" in group_status or group_status == "stale-backup"):
        return "DRFT"
    if any(e.is_bundled for e in relevant):
        return "bndl"
    if any(e.is_builtin for e in relevant):
        return "bltn"
    if any(e.is_plugin for e in relevant):
        return "plug"
    if any(e.scope == "local" for e in relevant):
        return "locl"
    if any(e.hop_count >= 2 for e in relevant):
        return "hop2"
    if any(e.is_symlink for e in relevant):
        return "link"
    return "copy"


def resolve_porch_agents_list() -> list[str]:
    """Return canonical IDs matching porch's skill-consuming harnesses."""
    return list(PORCH_HARNESS_AGENTS)


def _norm_abs(path: str | Path) -> str:
    """Normalize a path lexically without dereferencing symlinks."""
    return os.path.abspath(str(path))


def compute_stale_agent_diagnostics(
    agent_health: dict[str, dict],
    entries: list[SkillEntry],
    *,
    home: Path | None = None,
) -> list[dict]:
    """Identify uninstalled/stub agent directories and safe prunable vs protected paths."""
    home = home or Path.home()
    protected_readers: dict[str, list[str]] = defaultdict(list)

    for shared_rel in (".agents/skills", ".config/agents/skills"):
        protected_readers[_norm_abs(home / shared_rel)]  # reserve as shared-never-prune

    active_detect_roots: set[str] = set()
    for aid, info in agent_health.items():
        if info.get("status") not in ("active", "unverified"):
            continue
        for mp in info.get("matched_paths", []):
            active_detect_roots.add(_norm_abs(mp))
        for raw_sd in _agent_readable_dirs(aid, home):
            protected_readers[_norm_abs(raw_sd)].append(aid)

    stale_rows: list[dict] = []
    for aid in sorted(agent_health):
        info = agent_health[aid]
        status = info.get("status")
        if status not in ("skills-only-stub", "orphaned-agent"):
            continue

        ded_dirs = [_norm_abs(p) for p in info.get("dedicated_skill_dirs", [])]
        ded_set = set(ded_dirs)

        entries_count = 0
        broken_count = 0
        ghost_count = 0
        for e in entries:
            if _norm_abs(e.root) in ded_set:
                entries_count += 1
                if e.is_broken:
                    broken_count += 1
                elif e.is_ghost:
                    ghost_count += 1

        protected_paths: list[dict] = []
        prunable_paths: list[str] = []

        stub_roots = [_norm_abs(p) for p in info.get("stub_roots", [])]
        stub_skills_safe = bool(stub_roots) and status == "skills-only-stub"
        if stub_skills_safe:
            for sr in stub_roots:
                sr_skills = _norm_abs(Path(sr) / "skills")
                if sr in active_detect_roots or sr_skills in protected_readers:
                    stub_skills_safe = False
                    break

        if stub_skills_safe:
            prunable_paths = list(stub_roots)
        else:
            for ddir in ded_dirs:
                if ddir in protected_readers:
                    protected_paths.append({
                        "path": ddir,
                        "active_readers": sorted(set(protected_readers[ddir])),
                    })
                else:
                    prunable_paths.append(ddir)

        stale_rows.append({
            "agent_id": aid,
            "display_name": info.get("display_name", aid),
            "status": status,
            "reason": info.get("reason", ""),
            "matched_paths": info.get("matched_paths", []),
            "dedicated_skill_dirs": ded_dirs,
            "prunable_paths": prunable_paths,
            "protected_paths": protected_paths,
            "entries_count": entries_count,
            "broken_count": broken_count,
            "ghost_count": ghost_count,
        })

    return stale_rows
