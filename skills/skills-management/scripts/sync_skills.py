#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Quarantine-backed skill topology reconciler (`--dry-run` default, explicit `--apply`).

Safely prunes broken symlinks, ghost dirs, and orphaned `.skill-lock.json` entries;
collapses 2-hop/relative symlinks into direct 1-hop links; converges identical copy
replicas; and syncs canonical skills across agents with full `--undo <tx-id>`.
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
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

from agents import (
    AGENTS,
    NON_INSTALLABLE_HARNESSES,
    SHARED_GLOBAL,
    canonical_agent_id,
    detect_installed_agents,
    expand_path,
    expand_path_for_home,
    hermes_reads_shared_global,
    inspect_agent_installations,
)
from fs_ops import link_into_place, path_present
from skill_md import read_skill_text
from skill_topology import (
    SkillEntry,
    _agent_readable_dirs,
    classify_groups,
    compute_stale_agent_diagnostics,
    discover_roots,
    find_repo_root,
    load_jsonc,
    scan_topology,
)


def default_trash_root(home: Path | None = None) -> Path:
    base = home or Path.home()
    xdg = os.environ.get("XDG_CACHE_HOME", "").strip()
    cache_root = Path(xdg).expanduser() if (xdg and home is None) else (base / ".cache")
    return cache_root / "skills-management" / "trash"


def _agent_global_dir(aid: str, home: Path) -> Path:
    cfg = AGENTS[aid]
    raw = cfg["global_dir"]
    if home != Path.home() and raw.startswith("~/"):
        return home / raw[2:]
    return expand_path(raw, cfg)


def _affected_reload_notices(paths: list[Path], home: Path) -> list[str]:
    notices: list[str] = []
    joined = " ".join(str(p) for p in paths)
    edited_skill_files = any(p.name in ("SKILL.md", "openai.yaml") for p in paths)
    if edited_skill_files or ".gemini/config/skills" in joined or ".agents/skills" in joined:
        notices.append("Antigravity (App/IDE/agy): run /skills reload or start a new session")
    if edited_skill_files or ".claude/skills" in joined:
        notices.append("Claude Code: existing dirs hot-reload; restart session if top-level dirs changed")
    if edited_skill_files or ".codex" in joined or ".agents/skills" in joined:
        notices.append("Codex / OpenCode / Cursor / Gemini CLI: start a new task/session to reload skill catalog")
    if ".hermes/skills" in joined:
        notices.append("Hermes Agent: restart active session to refresh skills")
    if ".qwen/skills" in joined:
        notices.append("Qwen Code: restart session to refresh ~/.qwen/skills")
    if ".omp/" in joined:
        notices.append("Oh My Pi (omp): restart session to re-index ~/.omp/agent/skills")
    return notices


def set_frontmatter_bool_field(content: str, key: str, enabled: bool) -> tuple[bool, str]:
    """Set or remove a top-level boolean field inside SKILL.md YAML frontmatter, preserving formatting."""
    bom = "\ufeff" if content.startswith("\ufeff") else ""
    text = content[len(bom):]
    eol = "\r\n" if "\r\n" in text else "\n"
    lines = text.splitlines(keepends=True)

    if not lines or not re.match(r"^---[ \t]*$", lines[0].rstrip("\r\n")):
        raise ValueError("SKILL.md is missing YAML frontmatter (--- ... ---).")

    end_idx: int | None = None
    for idx in range(1, len(lines)):
        if re.match(r"^(?:---|\.\.\.)[ \t]*$", lines[idx].rstrip("\r\n")):
            end_idx = idx
            break
    if end_idx is None:
        raise ValueError("SKILL.md has unclosed YAML frontmatter.")

    key_re = re.compile(rf"^{re.escape(key)}[ \t]*:[ \t]*(.*?)[ \t]*$")
    matches: list[tuple[int, str, str]] = []
    for idx in range(1, end_idx):
        raw_line = lines[idx]
        no_eol = raw_line.rstrip("\r\n")
        line_eol = raw_line[len(no_eol):]
        m = key_re.match(no_eol)
        if not m:
            continue
        raw_val = m.group(1)
        if not (raw_val.startswith('"') or raw_val.startswith("'")):
            raw_val = raw_val.split("#", 1)[0].strip()
        val_clean = raw_val.strip("'\"").strip().lower()
        matches.append((idx, val_clean, line_eol or eol))

    if enabled:
        if len(matches) == 1 and matches[0][1] == "true":
            return False, content
        if matches:
            keep_idx, _, keep_eol = matches[-1]
            drop_indices = {idx for idx, _, _ in matches[:-1]}
            new_lines: list[str] = []
            for idx, line in enumerate(lines):
                if idx in drop_indices:
                    continue
                if idx == keep_idx:
                    new_lines.append(f"{key}: true{keep_eol}")
                else:
                    new_lines.append(line)
            return True, bom + "".join(new_lines)

        new_lines = list(lines)
        if end_idx > 0 and not new_lines[end_idx - 1].endswith(("\n", "\r")):
            new_lines[end_idx - 1] += eol
        new_lines.insert(end_idx, f"{key}: true{eol}")
        return True, bom + "".join(new_lines)

    if not matches:
        return False, content
    drop_indices = {idx for idx, _, _ in matches}
    new_lines = [line for idx, line in enumerate(lines) if idx not in drop_indices]
    return True, bom + "".join(new_lines)


def set_openai_yaml_implicit(existing: str | None, allow_implicit: bool) -> tuple[str, str | None]:
    """Update or remove ``policy.allow_implicit_invocation`` in ``agents/openai.yaml``."""
    if not allow_implicit:
        if existing is None:
            return "create", "policy:\n  allow_implicit_invocation: false\n"

        bom = "\ufeff" if existing.startswith("\ufeff") else ""
        text = existing[len(bom):]
        eol = "\r\n" if "\r\n" in text else "\n"
        lines = text.splitlines(keepends=True)
        if not text.strip():
            return "write", f"{bom}policy:{eol}  allow_implicit_invocation: false{eol}"

        section: str | None = None
        policy_hdr_idx: int | None = None
        policy_insert_idx: int | None = None
        policy_child_indent = "  "
        matches: list[tuple[int, str, str, str]] = []

        for idx, raw_line in enumerate(lines):
            no_eol = raw_line.rstrip("\r\n")
            line_eol = raw_line[len(no_eol):] or eol
            stripped = no_eol.strip()
            if not stripped or stripped.startswith("#"):
                continue
            indent = len(no_eol) - len(no_eol.lstrip(" "))
            if indent == 0 and stripped.endswith(":"):
                section = stripped[:-1].strip().lower()
                if section == "policy" and policy_hdr_idx is None:
                    policy_hdr_idx = idx
                    policy_insert_idx = idx + 1
                continue
            if section == "policy" and indent > 0:
                if policy_child_indent == "  ":
                    policy_child_indent = no_eol[:indent]
                policy_insert_idx = idx + 1
            if ":" in stripped and (section == "policy" or (section is None and indent == 0)):
                k, v = stripped.split(":", 1)
                if k.strip().lower() == "allow_implicit_invocation":
                    v_clean = v if (v.strip().startswith('"') or v.strip().startswith("'")) else v.split("#", 1)[0]
                    matches.append((idx, no_eol[:indent], v_clean.strip().strip("'\"").lower(), line_eol))

        if len(matches) == 1 and matches[0][2] == "false":
            return "noop", existing

        if matches:
            keep_idx, indent_str, _, line_eol = matches[-1]
            drop_indices = {idx for idx, _, _, _ in matches[:-1]}
            new_lines: list[str] = []
            for idx, line in enumerate(lines):
                if idx in drop_indices:
                    continue
                if idx == keep_idx:
                    new_lines.append(f"{indent_str}allow_implicit_invocation: false{line_eol}")
                else:
                    new_lines.append(line)
            return "write", bom + "".join(new_lines)

        if policy_hdr_idx is not None and policy_insert_idx is not None:
            new_lines = list(lines)
            if policy_insert_idx > 0 and not new_lines[policy_insert_idx - 1].endswith(("\n", "\r")):
                new_lines[policy_insert_idx - 1] += eol
            new_lines.insert(policy_insert_idx, f"{policy_child_indent}allow_implicit_invocation: false{eol}")
            return "write", bom + "".join(new_lines)

        new_lines = list(lines)
        if not new_lines[-1].endswith(("\n", "\r")):
            new_lines[-1] += eol
        if new_lines[-1].strip():
            new_lines.append(eol)
        new_lines.append(f"policy:{eol}")
        new_lines.append(f"  allow_implicit_invocation: false{eol}")
        return "write", bom + "".join(new_lines)

    # allow_implicit is True -> revert to auto
    if existing is None:
        return "noop", None

    bom = "\ufeff" if existing.startswith("\ufeff") else ""
    text = existing[len(bom):]
    eol = "\r\n" if "\r\n" in text else "\n"
    lines = text.splitlines(keepends=True)

    section = None
    policy_hdr_idx = None
    policy_children_other = 0
    remove_indices: set[int] = set()

    for idx, raw_line in enumerate(lines):
        no_eol = raw_line.rstrip("\r\n")
        stripped = no_eol.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(no_eol) - len(no_eol.lstrip(" "))
        if indent == 0 and stripped.endswith(":"):
            section = stripped[:-1].strip().lower()
            if section == "policy" and policy_hdr_idx is None:
                policy_hdr_idx = idx
            continue
        if ":" in stripped and (section == "policy" or (section is None and indent == 0)):
            k, _ = stripped.split(":", 1)
            if k.strip().lower() == "allow_implicit_invocation":
                remove_indices.add(idx)
                continue
        if section == "policy" and indent > 0:
            policy_children_other += 1

    if not remove_indices:
        return "noop", existing

    if policy_hdr_idx is not None and policy_children_other == 0:
        remove_indices.add(policy_hdr_idx)

    cleaned = [line for idx, line in enumerate(lines) if idx not in remove_indices]
    has_real_content = any(
        ln.strip() and not ln.lstrip().startswith("#") for ln in cleaned
    )
    if not has_real_content:
        return "delete", None

    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    if cleaned and not cleaned[-1].endswith(("\n", "\r")):
        cleaned[-1] += eol
    return "write", bom + "".join(cleaned)


def _choose_canonical_source(entries: list[SkillEntry], canonical_root: Path | None = None) -> SkillEntry | None:
    """Rank live entries for replica convergence without touching divergent copies."""
    candidates = [e for e in entries if not e.is_broken and not e.is_ghost and not e.is_plugin and not e.is_builtin]
    if not candidates:
        return None

    def score(e: SkillEntry) -> tuple[int, int, str]:
        p = e.real_path or e.path
        in_canonical = 0
        if canonical_root is not None:
            try:
                if Path(p).resolve().is_relative_to(canonical_root.resolve()):
                    in_canonical = 1
            except OSError:
                pass
        is_git = 1 if e.git_repo else 0
        is_shared = 1 if e.root_kind == "canonical-user" else 0
        is_warehouse = 1 if e.root_kind == "source-warehouse" else 0
        return (in_canonical, is_warehouse + is_git, is_shared, -len(p))

    return max(candidates, key=score)


def _under_quarantined_root(path_str: str, quarantined_roots: list[str]) -> bool:
    """Lexical ancestor check that works safely even on broken symlinks."""
    if not quarantined_roots:
        return False
    norm = os.path.abspath(path_str)
    return any(norm == root or norm.startswith(root + os.sep) for root in quarantined_roots)


def build_plan(
    *,
    home: Path | None = None,
    cwd: Path | None = None,
    prune_broken: bool = False,
    repoint_broken: bool = False,
    collapse_hops: bool = False,
    converge_replicas: bool = False,
    prune_stale_agents: bool = False,
    prune_agents: list[str] | None = None,
    sync_agents: list[str] | None = None,
    from_agents: list[str] | None = None,
    set_mode: str | None = None,
    skills_filter: set[str] | None = None,
    source_roots: list[Path] | None = None,
    canonical_root: Path | None = None,
    which_fn=None,
    app_dirs: list[Path] | None = None,
    extension_dirs: list[Path] | None = None,
) -> dict:
    """Compute a declarative reconciliation plan (`diff(current, desired)`)."""
    home = home or Path.home()
    cwd = (cwd or Path.cwd()).resolve()

    if set_mode not in (None, "manual", "auto"):
        raise ValueError(f"Unsupported --set-mode '{set_mode}'. Choose 'manual' or 'auto'.")
    if set_mode is not None and not skills_filter:
        raise ValueError("--set-mode requires explicit --skills <name1,name2,...> so skills are never switched in bulk unintentionally.")

    if sync_agents:
        for raw_a in sync_agents:
            if raw_a.strip().lower() in NON_INSTALLABLE_HARNESSES:
                raise ValueError(NON_INSTALLABLE_HARNESSES[raw_a.strip().lower()])
            canon = canonical_agent_id(raw_a)
            if canon not in AGENTS:
                raise ValueError(f"Unknown agent '{raw_a}'. Valid: {', '.join(sorted(AGENTS))}")

    canon_from_agents: list[str] = []
    if from_agents:
        for raw_a in from_agents:
            if raw_a.strip().lower() in NON_INSTALLABLE_HARNESSES:
                raise ValueError(NON_INSTALLABLE_HARNESSES[raw_a.strip().lower()])
            canon = canonical_agent_id(raw_a)
            if canon not in AGENTS:
                raise ValueError(f"Unknown agent '{raw_a}'. Valid: {', '.join(sorted(AGENTS))}")
            if canon not in canon_from_agents:
                canon_from_agents.append(canon)

    canon_prune_agents: list[str] = []
    if prune_agents:
        for raw_a in prune_agents:
            if raw_a.strip().lower() in NON_INSTALLABLE_HARNESSES:
                raise ValueError(NON_INSTALLABLE_HARNESSES[raw_a.strip().lower()])
            canon = canonical_agent_id(raw_a)
            if canon not in AGENTS:
                raise ValueError(f"Unknown agent '{raw_a}'. Valid: {', '.join(sorted(AGENTS))}")
            if canon not in canon_prune_agents:
                canon_prune_agents.append(canon)

    roots = discover_roots(
        scope="all",
        cwd=cwd,
        home=home,
        source_roots=source_roots,
        include_plugins=True,
        include_builtins=False,
        query_cli=False,
    )
    entries, lock_issues = scan_topology(roots, home=home, cwd=cwd)
    analysis = classify_groups(entries)

    ops: list[dict] = []
    skipped: list[dict] = []
    planned_paths: set[str] = set()
    skipped_paths: set[str] = set()
    quarantined_roots: list[str] = []

    def _want_skill(name: str) -> bool:
        return not skills_filter or name in skills_filter

    # 0. Opt-in quarantine of stale / uninstalled agent skill directories (or stubs)
    if prune_stale_agents or canon_prune_agents:
        if home == Path.home():
            detected_ids = detect_installed_agents(cwd=cwd)
        else:
            detected_ids = [
                aid for aid, cfg in AGENTS.items()
                if any(
                    expand_path_for_home(p, home, cfg).exists()
                    for p in cfg["detect_paths"]
                    if not p.startswith("/")
                )
                or any((cwd / m).exists() for m in cfg.get("detect_project_markers", []))
            ]
        inspect_ids = list(dict.fromkeys([*detected_ids, *canon_prune_agents]))
        agent_health = inspect_agent_installations(
            inspect_ids,
            cwd=cwd,
            home=home,
            which_fn=which_fn,
            app_dirs=app_dirs,
            extension_dirs=extension_dirs,
        )
        stale_diags = compute_stale_agent_diagnostics(agent_health, entries, home=home)
        stale_by_id = {d["agent_id"]: d for d in stale_diags}

        def _stage_quarantine_dir(raw_path: str, *, agent_id: str, reason: str) -> None:
            norm = os.path.abspath(raw_path)
            if norm in planned_paths or not Path(norm).exists() or Path(norm).is_symlink():
                return
            ops.append({
                "op": "quarantine_dir",
                "skill": f"agent:{agent_id}",
                "agent": agent_id,
                "path": norm,
                "reason": reason,
            })
            planned_paths.add(norm)
            quarantined_roots.append(norm)

        def _record_protected(prot_path: str, reason: str) -> None:
            norm = os.path.abspath(prot_path)
            if norm in skipped_paths:
                return
            skipped.append({"path": norm, "reason": reason})
            skipped_paths.add(norm)

        if prune_stale_agents:
            for diag in stale_diags:
                aid = diag["agent_id"]
                kind_label = "skills-only stub" if diag["status"] == "skills-only-stub" else "stale uninstalled agent"
                for p in diag["prunable_paths"]:
                    _stage_quarantine_dir(p, agent_id=aid, reason=f"{kind_label} ({aid}): {diag['reason']}")
                for pp in diag["protected_paths"]:
                    readers = ", ".join(pp["active_readers"]) if pp["active_readers"] else "shared pool"
                    _record_protected(pp["path"], f"Protected path still read by active {readers}")

        if canon_prune_agents:
            shared_never_prune = {
                os.path.abspath(home / ".agents" / "skills"),
                os.path.abspath(home / ".config" / "agents" / "skills"),
            }
            for aid in canon_prune_agents:
                if aid in stale_by_id:
                    diag = stale_by_id[aid]
                    kind_label = "skills-only stub" if diag["status"] == "skills-only-stub" else "stale uninstalled agent"
                    for p in diag["prunable_paths"]:
                        _stage_quarantine_dir(p, agent_id=aid, reason=f"explicit --prune-agent ({kind_label} {aid})")
                    for pp in diag["protected_paths"]:
                        readers = ", ".join(pp["active_readers"]) if pp["active_readers"] else "shared pool"
                        _record_protected(pp["path"], f"Protected path still read by active {readers}")
                    continue

                info = agent_health.get(aid, {})
                # Protection map from all OTHER active/unverified agents + shared pools
                other_readers: dict[str, list[str]] = {sp: [] for sp in shared_never_prune}
                for other_id, other_info in agent_health.items():
                    if other_id == aid or other_info.get("status") not in ("active", "unverified"):
                        continue
                    for sd in _agent_readable_dirs(other_id, home):
                        other_readers.setdefault(os.path.abspath(sd), []).append(other_id)

                candidates = (
                    info.get("stub_roots", [])
                    if info.get("status") == "skills-only-stub" and info.get("stub_roots")
                    else info.get("dedicated_skill_dirs", [])
                )
                for raw_p in candidates:
                    norm = os.path.abspath(raw_p)
                    check_key = os.path.abspath(Path(norm) / "skills") if info.get("status") == "skills-only-stub" else norm
                    if norm in shared_never_prune or check_key in other_readers or norm in other_readers:
                        readers = ", ".join(sorted(set(other_readers.get(check_key) or other_readers.get(norm) or []))) or "shared pool"
                        _record_protected(norm, f"Refused --prune-agent {aid}: path still read by active {readers}")
                    else:
                        _stage_quarantine_dir(norm, agent_id=aid, reason=f"explicit --prune-agent ({aid})")

    # 1. Repoint broken symlinks safely when requested (before pruning)
    repointed_paths: set[str] = set()
    if repoint_broken:
        for e in entries:
            if not e.is_broken or not _want_skill(e.dir_name) or _under_quarantined_root(e.path, quarantined_roots):
                continue
            if e.rename_hint:
                skipped.append({"path": e.path, "reason": f"Rename/consolidation detected ({e.rename_hint}); refusing blind repoint"})
                continue
            cands = e.repoint_candidates
            if len(cands) == 1:
                target = cands[0]["path"]
                ops.append({
                    "op": "repoint_symlink",
                    "skill": e.dir_name,
                    "path": e.path,
                    "target": target,
                    "reason": f"Unique exact-name canonical match ({cands[0]['provenance']})",
                })
                repointed_paths.add(e.path)
                planned_paths.add(e.path)
            elif len(cands) > 1:
                skipped.append({"path": e.path, "reason": f"Ambiguous repoint: {len(cands)} live matches for '{e.dir_name}'"})

    # 2. Prune broken symlinks, ghost dirs, and orphaned lockfile keys
    removed_from_shared: set[str] = set()
    if prune_broken:
        shared_prefix = str((home / ".agents" / "skills").absolute())
        for e in entries:
            if e.path in repointed_paths or _under_quarantined_root(e.path, quarantined_roots):
                continue
            if e.is_broken and _want_skill(e.name):
                ops.append({
                    "op": "remove_symlink",
                    "skill": e.name,
                    "path": e.path,
                    "reason": e.broken_reason or "broken symlink",
                })
                planned_paths.add(e.path)
            elif e.is_ghost and _want_skill(e.dir_name):
                ops.append({
                    "op": "quarantine_dir",
                    "skill": e.dir_name,
                    "path": e.path,
                    "reason": "ghost directory without SKILL.md",
                })
                planned_paths.add(e.path)
                if e.path.startswith(shared_prefix):
                    removed_from_shared.add(e.dir_name)

        # Clean orphaned .skill-lock.json entries cleanly
        orphans_by_lock: dict[str, list[str]] = {}
        for li in lock_issues:
            if li.kind == "orphaned-lock-entry" and _want_skill(li.skill):
                orphans_by_lock.setdefault(li.lockfile, []).append(li.skill)
        for lockfile_path, skill_keys in sorted(orphans_by_lock.items()):
            ops.append({
                "op": "clean_lockfile",
                "lockfile": lockfile_path,
                "remove_keys": sorted(skill_keys),
                "reason": f"{len(skill_keys)} orphaned lockfile entries absent from skills dir",
            })

    # 3. Collapse 2-hop / relative symlinks into direct 1-hop absolute symlinks
    if collapse_hops:
        for e in entries:
            if e.is_broken or e.is_ghost or e.path in planned_paths or not e.is_symlink or _under_quarantined_root(e.path, quarantined_roots):
                continue
            if not _want_skill(e.name) or not e.real_path:
                continue
            if e.hop_count >= 2 or e.is_relative_symlink:
                # Never overwrite a real_path with a symlink to itself
                if e.path == e.real_path:
                    continue
                ops.append({
                    "op": "repoint_symlink",
                    "skill": e.name,
                    "path": e.path,
                    "target": e.real_path,
                    "reason": f"collapse {e.hop_count}-hop/relative symlink to canonical 1-hop target",
                })
                planned_paths.add(e.path)

    # 4. Converge identical copy replicas (NEVER divergent copies!)
    if converge_replicas:
        for grp in analysis["by_name"]:
            if not _want_skill(grp["name"]):
                continue
            if grp["status"] == "divergent" or grp["requires_decision"]:
                skipped.append({"skill": grp["name"], "reason": f"Status is '{grp['status']}' (requires owner decision)"})
                continue
            if grp["status"] != "replica":
                continue
            # Rebuild SkillEntry list from entries
            grp_entries = [
                e for e in entries
                if e.name == grp["name"]
                and not e.is_broken
                and not e.is_ghost
                and not e.is_plugin
                and not _under_quarantined_root(e.path, quarantined_roots)
            ]
            canon = _choose_canonical_source(grp_entries, canonical_root)
            if not canon or not canon.real_path:
                continue
            for e in grp_entries:
                if e.path in planned_paths or e.path == canon.real_path:
                    continue
                if e.is_symlink and e.real_path == canon.real_path:
                    continue
                if not e.is_symlink:
                    ops.append({
                        "op": "converge_copy_to_symlink",
                        "skill": e.name,
                        "path": e.path,
                        "target": canon.real_path,
                        "reason": f"byte-identical replica -> 1-hop symlink to {canon.real_path}",
                    })
                    planned_paths.add(e.path)

    # 5. Sync canonical skills across target agents
    if sync_agents:
        canon_agents = [canonical_agent_id(a) for a in sync_agents]
        hermes_shared = hermes_reads_shared_global(home=home)
        shared_dir = home / ".agents" / "skills"

        allowed_roots: set[str] | None = None
        if canon_from_agents:
            allowed_roots = {os.path.abspath(_agent_global_dir(a, home)) for a in canon_from_agents}
            if any(
                bool(AGENTS[a].get("reads_shared_global"))
                or AGENTS[a]["global_dir"] == SHARED_GLOBAL
                or (a == "hermes-agent" and hermes_shared)
                for a in canon_from_agents
            ):
                allowed_roots.add(os.path.abspath(shared_dir))

        # Index live canonical sources by skill name (excluding bundled/plugin/builtin/local-unless-warehouse)
        by_name: dict[str, list[SkillEntry]] = {}
        for e in entries:
            if e.is_broken or e.is_ghost or e.is_plugin or e.is_builtin or e.is_bundled:
                continue
            if not canon_from_agents and e.scope == "local" and e.root_kind != "source-warehouse":
                continue
            if allowed_roots is not None and os.path.abspath(e.root) not in allowed_roots:
                continue
            by_name.setdefault(e.name, []).append(e)

        for sname, grp_entries in sorted(by_name.items()):
            if not _want_skill(sname):
                continue
            if any(g["name"] == sname and g["requires_decision"] for g in analysis["by_name"]):
                skipped.append({"skill": sname, "reason": "Divergent copies exist; resolve conflict before syncing"})
                continue
            canon = _choose_canonical_source(grp_entries, canonical_root)
            if not canon or not canon.real_path:
                continue
            real_target = canon.real_path
            slot_name = canon.dir_name

            # Ensure ~/.agents/skills has it if any target agent relies on shared global
            needs_shared = any(
                bool(AGENTS[a].get("reads_shared_global"))
                or AGENTS[a]["global_dir"] == SHARED_GLOBAL
                or (a == "hermes-agent" and hermes_shared)
                for a in canon_agents
            )
            shared_dir_abs = os.path.abspath(shared_dir)
            shared_slot = shared_dir / slot_name
            shared_already = any(
                os.path.abspath(Path(e.path).parent) == shared_dir_abs and e.real_path == real_target
                for e in grp_entries
            )
            if needs_shared and not shared_already and str(shared_slot.absolute()) not in planned_paths:
                if not path_present(shared_slot):
                    ops.append({
                        "op": "create_symlink",
                        "skill": slot_name,
                        "path": str(shared_slot.absolute()),
                        "target": real_target,
                        "reason": "populate canonical shared ~/.agents/skills pool",
                    })
                    planned_paths.add(str(shared_slot.absolute()))

            for aid in canon_agents:
                cfg = AGENTS[aid]
                # Skip dedicated link if agent reads ~/.agents/skills automatically
                if cfg["global_dir"] == SHARED_GLOBAL or cfg.get("reads_shared_global") or (aid == "hermes-agent" and hermes_shared):
                    continue
                target_dir = _agent_global_dir(aid, home)
                target_dir_abs = os.path.abspath(target_dir)
                target_slot = target_dir / slot_name
                slot_str = str(target_slot.absolute())
                if slot_str in planned_paths or slot_str == real_target or _under_quarantined_root(slot_str, quarantined_roots):
                    continue
                if any(os.path.abspath(Path(e.path).parent) == target_dir_abs and e.real_path == real_target and not (e.hop_count >= 2 or e.is_relative_symlink) for e in grp_entries):
                    continue
                if target_slot.exists():
                    try:
                        if str(target_slot.resolve()) == real_target and not (target_slot.is_symlink() and not Path(os.readlink(target_slot)).is_absolute()):
                            continue
                    except OSError:
                        pass
                    if not target_slot.is_symlink():
                        skipped.append({"skill": slot_name, "path": slot_str, "reason": f"Real directory exists at {aid}; pass --converge-replicas to link"})
                        continue
                ops.append({
                    "op": "repoint_symlink" if target_slot.is_symlink() else "create_symlink",
                    "skill": slot_name,
                    "path": slot_str,
                    "target": real_target,
                    "reason": f"sync 1-hop link for {aid}",
                })
                planned_paths.add(slot_str)

    # 6. Toggle cross-agent invocation mode (manual | auto)
    if set_mode is not None and skills_filter:
        by_name_live: dict[str, list[SkillEntry]] = {}
        by_dir_live: dict[str, list[SkillEntry]] = {}
        for e in entries:
            if e.is_broken or e.is_ghost or _under_quarantined_root(e.path, quarantined_roots):
                continue
            by_name_live.setdefault(e.name, []).append(e)
            by_dir_live.setdefault(e.dir_name, []).append(e)

        requires_decision_names = {
            g["name"] for g in analysis["by_name"] if g.get("requires_decision")
        }
        manual_target = set_mode == "manual"
        seen_real_paths: set[str] = set()

        for req_name in sorted(skills_filter):
            matched = by_name_live.get(req_name) or by_dir_live.get(req_name) or []
            if not matched:
                skipped.append({"skill": req_name, "reason": "Skill not found in discovered roots"})
                continue
            editable = [
                e for e in matched
                if not e.is_plugin and not e.is_bundled and not e.is_builtin
            ]
            if not editable:
                skipped.append({"skill": req_name, "reason": "Plugin/bundled/builtin skill is read-only"})
                continue
            if any(e.name in requires_decision_names for e in editable):
                skipped.append({
                    "skill": req_name,
                    "reason": "Divergent copies exist; resolve conflict before changing invocation mode",
                })
                continue

            for entry in editable:
                if not entry.real_path or entry.real_path in seen_real_paths:
                    continue
                seen_real_paths.add(entry.real_path)
                real_dir = Path(entry.real_path)
                git_note = f" [git: {entry.git_repo}]" if entry.git_repo else ""

                skill_md_path = real_dir / "SKILL.md"
                md_str = str(skill_md_path.absolute())
                if skill_md_path.is_file() and md_str not in planned_paths:
                    old_md = read_skill_text(skill_md_path)
                    changed_md, new_md = set_frontmatter_bool_field(
                        old_md, "disable-model-invocation", manual_target
                    )
                    if changed_md:
                        ops.append({
                            "op": "edit_file",
                            "skill": entry.name,
                            "path": md_str,
                            "existed": True,
                            "content": new_md,
                            "reason": (
                                f"set SKILL.md disable-model-invocation: true{git_note}"
                                if manual_target
                                else f"remove SKILL.md disable-model-invocation (auto mode){git_note}"
                            ),
                        })
                        planned_paths.add(md_str)

                yaml_path = real_dir / "agents" / "openai.yaml"
                yaml_str = str(yaml_path.absolute())
                if yaml_str not in planned_paths:
                    old_yaml = (
                        yaml_path.read_text(encoding="utf-8", errors="replace")
                        if yaml_path.is_file()
                        else None
                    )
                    yaml_action, new_yaml = set_openai_yaml_implicit(
                        old_yaml, allow_implicit=not manual_target
                    )
                    if yaml_action in ("create", "write") and new_yaml is not None:
                        verb = "create" if yaml_action == "create" else "update"
                        ops.append({
                            "op": "edit_file",
                            "skill": entry.name,
                            "path": yaml_str,
                            "existed": yaml_action == "write",
                            "content": new_yaml,
                            "reason": (
                                f"{verb} agents/openai.yaml allow_implicit_invocation: false{git_note}"
                                if manual_target
                                else f"{verb} agents/openai.yaml (remove allow_implicit_invocation){git_note}"
                            ),
                        })
                        planned_paths.add(yaml_str)
                    elif yaml_action == "delete":
                        ops.append({
                            "op": "delete_file",
                            "skill": entry.name,
                            "path": yaml_str,
                            "remove_empty_parent": True,
                            "reason": f"remove pure-policy agents/openai.yaml (auto mode){git_note}",
                        })
                        planned_paths.add(yaml_str)

    return {
        "schema_version": 1,
        "state": "staged",
        "ops": ops,
        "skipped": skipped,
        "op_count": len(ops),
    }


def apply_plan(
    plan: dict,
    *,
    home: Path | None = None,
    trash_root: Path | None = None,
    cli_args: list[str] | None = None,
) -> dict:
    """Execute a staged plan atomically, quarantining replaced items for `--undo`."""
    home = home or Path.home()
    ops = plan.get("ops", [])
    if not ops:
        return {**plan, "state": "done", "tx_id": None, "applied": 0, "errors": [], "reload_notices": []}

    troot = trash_root or default_trash_root(home)
    tx_id = datetime.now(timezone.utc).strftime("tx-%Y%m%d-%H%M%S-%f")
    tx_dir = troot / tx_id
    files_dir = tx_dir / "files"
    files_dir.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(troot, 0o700)
    except OSError:
        pass

    undo_records: list[dict] = []
    errors: list[dict] = []
    touched_paths: list[Path] = []

    for idx, op in enumerate(ops):
        kind = op["op"]
        try:
            if kind in ("remove_symlink", "repoint_symlink", "create_symlink"):
                target_path = Path(op["path"])
                was_present = path_present(target_path)
                prev_raw = os.readlink(target_path) if target_path.is_symlink() else None
                if kind == "remove_symlink":
                    if target_path.is_symlink():
                        target_path.unlink()
                    undo_records.append({
                        "undo": "restore_symlink" if prev_raw is not None else "noop",
                        "path": str(target_path),
                        "raw_target": prev_raw,
                    })
                else:
                    link_into_place(Path(op["target"]), target_path)
                    undo_records.append({
                        "undo": "restore_symlink" if prev_raw is not None else ("noop" if was_present else "remove_new_symlink"),
                        "path": str(target_path),
                        "raw_target": prev_raw,
                    })
                touched_paths.append(target_path)

            elif kind in ("quarantine_dir", "converge_copy_to_symlink"):
                target_path = Path(op["path"])
                backup_rel = f"files/{idx}_{target_path.name}"
                backup_dst = tx_dir / backup_rel
                if target_path.exists() and not target_path.is_symlink():
                    shutil.move(str(target_path), str(backup_dst))
                    if kind == "converge_copy_to_symlink":
                        link_into_place(Path(op["target"]), target_path)
                    undo_records.append({
                        "undo": "restore_dir",
                        "path": str(target_path),
                        "backup_rel": backup_rel,
                        "remove_link_first": (kind == "converge_copy_to_symlink"),
                    })
                    touched_paths.append(target_path)

            elif kind == "clean_lockfile":
                lock_path = Path(op["lockfile"])
                data = load_jsonc(lock_path)
                if not isinstance(data, dict) or not isinstance(data.get("skills"), dict):
                    raise ValueError(f"Unreadable lockfile JSON: {lock_path}")
                backup_rel = f"files/{idx}_{lock_path.name}"
                shutil.copy2(str(lock_path), str(tx_dir / backup_rel))
                skills_map = data["skills"]
                for key in op["remove_keys"]:
                    skills_map.pop(key, None)
                tmp = lock_path.with_suffix(".tmp")
                tmp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
                tmp.replace(lock_path)
                undo_records.append({
                    "undo": "restore_file",
                    "path": str(lock_path),
                    "backup_rel": backup_rel,
                })
                touched_paths.append(lock_path)

            elif kind == "edit_file":
                target_path = Path(op["path"])
                if target_path.is_file():
                    backup_rel = f"files/{idx}_{target_path.name}"
                    shutil.copy2(str(target_path), str(tx_dir / backup_rel))
                    undo_records.append({
                        "undo": "restore_file",
                        "path": str(target_path),
                        "backup_rel": backup_rel,
                    })
                else:
                    undo_records.append({
                        "undo": "remove_new_file",
                        "path": str(target_path),
                        "remove_empty_parent": target_path.parent.name == "agents",
                    })
                target_path.parent.mkdir(parents=True, exist_ok=True)
                tmp = target_path.with_name(f".{target_path.name}.tmp.{os.getpid()}")
                tmp.write_text(op["content"], encoding="utf-8")
                tmp.replace(target_path)
                touched_paths.append(target_path)

            elif kind == "delete_file":
                target_path = Path(op["path"])
                if target_path.is_file():
                    backup_rel = f"files/{idx}_{target_path.name}"
                    shutil.copy2(str(target_path), str(tx_dir / backup_rel))
                    target_path.unlink()
                    if op.get("remove_empty_parent") and target_path.parent.is_dir():
                        try:
                            target_path.parent.rmdir()
                        except OSError:
                            pass
                    undo_records.append({
                        "undo": "restore_file",
                        "path": str(target_path),
                        "backup_rel": backup_rel,
                    })
                    touched_paths.append(target_path)
        except Exception as exc:
            errors.append({"op": op, "error": str(exc)})

    manifest = {
        "tx_id": tx_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "cli_args": cli_args or [],
        "undo_records": undo_records,
    }
    (tx_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    state = "done" if not errors else ("partial" if undo_records else "failed")
    return {
        "schema_version": 1,
        "state": state,
        "tx_id": tx_id,
        "trash_dir": str(tx_dir),
        "applied": len(undo_records),
        "errors": errors,
        "skipped": plan.get("skipped", []),
        "reload_notices": _affected_reload_notices(touched_paths, home),
    }


def undo_transaction(tx_id: str, *, home: Path | None = None, trash_root: Path | None = None) -> dict:
    """Restore filesystem and lockfile state from a quarantine transaction."""
    home = home or Path.home()
    troot = trash_root or default_trash_root(home)
    tx_dir = troot / tx_id
    manifest_file = tx_dir / "manifest.json"
    if not manifest_file.is_file():
        raise FileNotFoundError(f"Transaction not found: {tx_id} ({manifest_file})")

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    records = list(reversed(manifest.get("undo_records", [])))
    restored = 0
    errors: list[dict] = []

    for rec in records:
        action = rec.get("undo")
        target_path = Path(rec["path"])
        try:
            if action == "restore_symlink":
                target_path.parent.mkdir(parents=True, exist_ok=True)
                if target_path.is_symlink() or target_path.is_file():
                    target_path.unlink()
                elif target_path.is_dir():
                    raise FileExistsError(f"Real directory now occupies {target_path}")
                target_path.symlink_to(rec["raw_target"], target_is_directory=True)
                restored += 1
            elif action == "remove_new_symlink":
                if target_path.is_symlink():
                    target_path.unlink()
                restored += 1
            elif action == "restore_dir":
                if rec.get("remove_link_first") and target_path.is_symlink():
                    target_path.unlink()
                if path_present(target_path):
                    raise FileExistsError(f"Path already occupied at {target_path}")
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(tx_dir / rec["backup_rel"]), str(target_path))
                restored += 1
            elif action == "restore_file":
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(str(tx_dir / rec["backup_rel"]), str(target_path))
                restored += 1
            elif action == "remove_new_file":
                if target_path.is_file():
                    target_path.unlink()
                if rec.get("remove_empty_parent") and target_path.parent.is_dir():
                    try:
                        target_path.parent.rmdir()
                    except OSError:
                        pass
                restored += 1
        except Exception as exc:
            errors.append({"record": rec, "error": str(exc)})

    state = "done" if not errors else "partial"
    return {
        "schema_version": 1,
        "state": state,
        "tx_id": tx_id,
        "restored": restored,
        "errors": errors,
    }


def list_transactions(*, home: Path | None = None, trash_root: Path | None = None) -> list[dict]:
    troot = trash_root or default_trash_root(home)
    if not troot.is_dir():
        return []
    out: list[dict] = []
    for sub in sorted(troot.iterdir(), reverse=True):
        mf = sub / "manifest.json"
        if mf.is_file():
            try:
                data = json.loads(mf.read_text(encoding="utf-8"))
                out.append({
                    "tx_id": data.get("tx_id", sub.name),
                    "created_at": data.get("created_at"),
                    "ops_recorded": len(data.get("undo_records", [])),
                })
            except json.JSONDecodeError:
                continue
    return out


def format_sync_output(result: dict, output_format: str = "text") -> str:
    if output_format == "json":
        return json.dumps(result, indent=2)

    lines: list[str] = []
    state = result.get("state", "staged").upper()
    if "ops" in result:
        lines.append(f"[{state}] Planned operations: {result['op_count']}")
        for op in result["ops"][:50]:
            target_info = f" -> {op['target']}" if "target" in op else ""
            if op["op"] == "clean_lockfile":
                lines.append(f"  - {op['op']}: {op['lockfile']} remove {len(op['remove_keys'])} keys ({op['reason']})")
            else:
                lines.append(f"  - {op['op']}: {op['path']}{target_info} ({op['reason']})")
        if result["op_count"] > 50:
            lines.append(f"  ... +{result['op_count'] - 50} more operations")
        if result.get("skipped"):
            lines.append(f"Skipped ({len(result['skipped'])}):")
            for sk in result["skipped"][:15]:
                lines.append(f"  - {sk.get('path') or sk.get('skill')}: {sk['reason']}")
        if result["op_count"] > 0:
            lines.append("\nDry-run complete (no files changed). Re-run with --apply to execute with quarantine undo.")
        return "\n".join(lines)

    if "restored" in result:
        lines.append(f"[{state}] Undo {result['tx_id']}: restored {result['restored']} item(s)")
        for err in result.get("errors", []):
            lines.append(f"  [ERR] {err['error']}")
        return "\n".join(lines)

    lines.append(f"[{state}] Applied {result.get('applied', 0)} operation(s)")
    if result.get("tx_id"):
        lines.append(f"Undo transaction: uv run scripts/sync_skills.py --undo {result['tx_id']}")
    for err in result.get("errors", []):
        lines.append(f"  [ERR] {err['op'].get('path', '')}: {err['error']}")
    if notices := result.get("reload_notices"):
        lines.append("Reload / restart open sessions for changes to take effect:")
        for n in notices:
            lines.append(f"  - {n}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Quarantine-backed skill topology reconciler (--dry-run by default)"
    )
    parser.add_argument("--apply", action="store_true", help="Apply staged changes (default is dry-run preview)")
    parser.add_argument("--prune-broken", action="store_true", help="Remove broken symlinks, ghost dirs, and orphaned .skill-lock.json entries")
    parser.add_argument("--repoint-broken", action="store_true", help="Repoint broken symlinks to unique exact-name matches in --source-root")
    parser.add_argument("--collapse-hops", action="store_true", help="Convert 2-hop/relative symlinks into direct 1-hop absolute symlinks")
    parser.add_argument("--converge-replicas", action="store_true", help="Replace byte-identical independent copies with 1-hop symlinks")
    parser.add_argument("--prune-stale-agents", action="store_true", help="Quarantine skill dirs (or skills-only stub roots) of uninstalled CLIs/apps")
    parser.add_argument("--prune-agent", action="append", dest="prune_agents", help="Quarantine dedicated skill dir for specific agent(s) (never shared ~/.agents/skills)")
    parser.add_argument("--sync-agents", action="append", help="Agents/aliases to bring to canonical parity (comma-separated or repeatable)")
    parser.add_argument("--from-agents", action="append", help="Restrict --sync-agents canonical source discovery to these agents' primary global dirs (comma-separated or repeatable)")
    parser.add_argument("--set-mode", choices=["manual", "auto"], help="Switch invocation mode for --skills across SKILL.md (disable-model-invocation) and agents/openai.yaml (allow_implicit_invocation)")
    parser.add_argument("--skills", action="append", help="Limit sync/remediation to specific skill names (comma-separated or repeatable)")
    parser.add_argument("--source-root", action="append", type=Path, default=[], help="Canonical project/warehouse directory")
    parser.add_argument("--canonical-root", type=Path, help="Preferred canonical source directory when converging replicas")
    parser.add_argument("--cwd", type=Path, default=Path.cwd())
    parser.add_argument("--undo", metavar="TX_ID", help="Restore a previous --apply transaction from quarantine")
    parser.add_argument("--list-transactions", action="store_true", help="List available quarantine transactions")
    parser.add_argument("--format", "-f", choices=["text", "json"], default="text")
    args = parser.parse_args()

    if args.list_transactions:
        txs = list_transactions()
        print(json.dumps(txs, indent=2) if args.format == "json" else "\n".join(f"{t['tx_id']}  {t['created_at']}  ops={t['ops_recorded']}" for t in txs) or "No transactions recorded.")
        return 0

    if args.undo:
        try:
            res = undo_transaction(args.undo)
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
        print(format_sync_output(res, args.format))
        return 0 if res["state"] == "done" else 1

    if not any([args.prune_broken, args.repoint_broken, args.collapse_hops, args.converge_replicas, args.prune_stale_agents, args.prune_agents, args.sync_agents, args.set_mode]):
        parser.error("Specify at least one action (--prune-broken, --repoint-broken, --collapse-hops, --converge-replicas, --prune-stale-agents, --prune-agent, --sync-agents, --set-mode) or --undo / --list-transactions")

    sync_list: list[str] = []
    if args.sync_agents:
        for item in args.sync_agents:
            sync_list.extend(p.strip() for p in item.split(",") if p.strip())

    from_list: list[str] = []
    if args.from_agents:
        for item in args.from_agents:
            from_list.extend(p.strip() for p in item.split(",") if p.strip())

    prune_agent_list: list[str] = []
    if args.prune_agents:
        for item in args.prune_agents:
            prune_agent_list.extend(p.strip() for p in item.split(",") if p.strip())

    skills_set: set[str] | None = None
    if args.skills:
        skills_set = {p.strip() for item in args.skills for p in item.split(",") if p.strip()}

    try:
        plan = build_plan(
            cwd=args.cwd,
            prune_broken=args.prune_broken,
            repoint_broken=args.repoint_broken,
            collapse_hops=args.collapse_hops,
            converge_replicas=args.converge_replicas,
            prune_stale_agents=args.prune_stale_agents,
            prune_agents=prune_agent_list or None,
            sync_agents=sync_list or None,
            from_agents=from_list or None,
            set_mode=args.set_mode,
            skills_filter=skills_set,
            source_roots=args.source_root,
            canonical_root=args.canonical_root,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not args.apply:
        print(format_sync_output(plan, args.format))
        return 0

    res = apply_plan(plan, cli_args=sys.argv[1:])
    print(format_sync_output(res, args.format))
    return 0 if res["state"] in ("done", "staged") else 1


if __name__ == "__main__":
    sys.exit(main())
