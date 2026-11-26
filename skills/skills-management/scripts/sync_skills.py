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
import shutil
from datetime import datetime, timezone
from pathlib import Path

from agents import (
    AGENTS,
    NON_INSTALLABLE_HARNESSES,
    SHARED_GLOBAL,
    canonical_agent_id,
    expand_path,
    hermes_reads_shared_global,
)
from fs_ops import link_into_place, path_present
from skill_topology import (
    SkillEntry,
    classify_groups,
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
    home_str = str(home)
    joined = " ".join(str(p) for p in paths)
    if ".gemini/config/skills" in joined or ".agents/skills" in joined:
        notices.append("Antigravity (App/IDE/agy): run /skills reload or start a new session")
    if ".claude/skills" in joined:
        notices.append("Claude Code: existing dirs hot-reload; restart session if top-level dirs changed")
    if ".codex" in joined or ".agents/skills" in joined:
        notices.append("Codex / OpenCode / Cursor / Gemini CLI: start a new task/session to reload skill catalog")
    if ".hermes/skills" in joined:
        notices.append("Hermes Agent: restart active session to refresh skills")
    if ".qwen/skills" in joined:
        notices.append("Qwen Code: restart session to refresh ~/.qwen/skills")
    if ".omp/" in joined:
        notices.append("Oh My Pi (omp): restart session to re-index ~/.omp/agent/skills")
    return notices


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


def build_plan(
    *,
    home: Path | None = None,
    cwd: Path | None = None,
    prune_broken: bool = False,
    repoint_broken: bool = False,
    collapse_hops: bool = False,
    converge_replicas: bool = False,
    sync_agents: list[str] | None = None,
    skills_filter: set[str] | None = None,
    source_roots: list[Path] | None = None,
    canonical_root: Path | None = None,
) -> dict:
    """Compute a declarative reconciliation plan (`diff(current, desired)`)."""
    home = home or Path.home()
    cwd = (cwd or Path.cwd()).resolve()

    if sync_agents:
        for raw_a in sync_agents:
            if raw_a.strip().lower() in NON_INSTALLABLE_HARNESSES:
                raise ValueError(NON_INSTALLABLE_HARNESSES[raw_a.strip().lower()])
            canon = canonical_agent_id(raw_a)
            if canon not in AGENTS:
                raise ValueError(f"Unknown agent '{raw_a}'. Valid: {', '.join(sorted(AGENTS))}")

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

    def _want_skill(name: str) -> bool:
        return not skills_filter or name in skills_filter

    # 1. Repoint broken symlinks safely when requested (before pruning)
    repointed_paths: set[str] = set()
    if repoint_broken:
        for e in entries:
            if not e.is_broken or not _want_skill(e.dir_name):
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
            if e.path in repointed_paths:
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
            if e.is_broken or e.is_ghost or e.path in planned_paths or not e.is_symlink:
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
            grp_entries = [e for e in entries if e.name == grp["name"] and not e.is_broken and not e.is_ghost and not e.is_plugin]
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
        # Index live canonical sources by skill name (include warehouse sources!)
        by_name: dict[str, list[SkillEntry]] = {}
        for e in entries:
            if not e.is_broken and not e.is_ghost and not e.is_plugin and not e.is_builtin:
                by_name.setdefault(e.name, []).append(e)

        shared_dir = home / ".agents" / "skills"
        hermes_shared = hermes_reads_shared_global(home=home)

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

            # Ensure ~/.agents/skills has it if any target agent relies on shared global
            needs_shared = any(
                bool(AGENTS[a].get("reads_shared_global"))
                or AGENTS[a]["global_dir"] == SHARED_GLOBAL
                or (a == "hermes-agent" and hermes_shared)
                for a in canon_agents
            )
            shared_slot = shared_dir / sname
            if needs_shared and str(shared_slot.absolute()) not in planned_paths:
                if not path_present(shared_slot):
                    ops.append({
                        "op": "create_symlink",
                        "skill": sname,
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
                target_slot = _agent_global_dir(aid, home) / sname
                slot_str = str(target_slot.absolute())
                if slot_str in planned_paths or slot_str == real_target:
                    continue
                if target_slot.exists():
                    try:
                        if str(target_slot.resolve()) == real_target and not (target_slot.is_symlink() and not Path(os.readlink(target_slot)).is_absolute()):
                            continue
                    except OSError:
                        pass
                    if not target_slot.is_symlink():
                        skipped.append({"skill": sname, "path": slot_str, "reason": f"Real directory exists at {aid}; pass --converge-replicas to link"})
                        continue
                ops.append({
                    "op": "repoint_symlink" if target_slot.is_symlink() else "create_symlink",
                    "skill": sname,
                    "path": slot_str,
                    "target": real_target,
                    "reason": f"sync 1-hop link for {aid}",
                })
                planned_paths.add(slot_str)

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
    parser.add_argument("--sync-agents", action="append", help="Agents/aliases to bring to canonical parity (comma-separated or repeatable)")
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

    if not any([args.prune_broken, args.repoint_broken, args.collapse_hops, args.converge_replicas, args.sync_agents]):
        parser.error("Specify at least one action (--prune-broken, --repoint-broken, --collapse-hops, --converge-replicas, --sync-agents) or --undo / --list-transactions")

    sync_list: list[str] = []
    if args.sync_agents:
        for item in args.sync_agents:
            sync_list.extend(p.strip() for p in item.split(",") if p.strip())

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
            sync_agents=sync_list or None,
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
