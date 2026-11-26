#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Read-only revision of Agent Skills across global and local harnesses.

Surfaces broken symlinks, ghost directories, orphaned lockfile entries,
cross-root duplicates/drift, startup context budgets, Discovery-Pool matrix,
and optional porch-aware usage telemetry.
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
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

from agents import (
    AGENTS,
    canonical_agent_id,
    detect_installed_agents,
)
from skill_topology import (
    POOL_COLUMNS,
    LockfileIssue,
    ManifestIssue,
    SkillEntry,
    _home_path,
    cell_status_for_pool,
    classify_groups,
    compute_agent_context_budgets,
    discover_roots,
    find_repo_root,
    resolve_porch_agents_list,
    scan_topology,
)
from skill_usage import collect_usage_deep, collect_usage_fast, parse_since


def _parse_agents_arg(raw_list: list[str] | None, *, porch_harnesses: bool = False) -> list[str] | None:
    if porch_harnesses:
        return resolve_porch_agents_list()
    if not raw_list:
        return None
    out: list[str] = []
    for item in raw_list:
        for part in item.split(","):
            part = part.strip()
            if not part:
                continue
            canon = canonical_agent_id(part)
            if canon not in AGENTS:
                raise ValueError(f"Unknown agent/harness '{part}'. Valid IDs: {', '.join(sorted(AGENTS))}")
            if canon not in out:
                out.append(canon)
    return out or None


def run_revision(
    *,
    scope: str = "auto",
    cwd: Path | None = None,
    home: Path | None = None,
    agents_filter: list[str] | None = None,
    porch_harnesses: bool = False,
    expand_agents: bool = False,
    usage_mode: str = "fast",
    since: str | None = None,
    source_roots: list[Path] | None = None,
    scan_skills_dirs: bool = False,
    include_plugins: bool = True,
    include_builtins: bool = False,
    query_cli: bool = False,
    no_cache: bool = False,
    cache_path: Path | None = None,
) -> dict:
    """Execute a complete read-only revision and return structured diagnostics."""
    home = home or Path.home()
    cwd = (cwd or Path.cwd()).resolve()
    repo_root = find_repo_root(cwd)

    effective_scope = scope
    if scope == "auto":
        has_local_dir = bool(repo_root) or any(
            (cwd / d).is_dir() for d in (".agents/skills", ".claude/skills", ".agent/skills", "skills")
        )
        effective_scope = "all" if has_local_dir else "global"

    selected_agents = _parse_agents_arg(agents_filter, porch_harnesses=porch_harnesses)
    if home == Path.home():
        detected = detect_installed_agents(cwd=cwd)
    else:
        detected = [
            aid for aid, cfg in AGENTS.items()
            if any(_home_path(p, home, cfg).exists() for p in cfg["detect_paths"])
            or any((cwd / m).exists() for m in cfg.get("detect_project_markers", []))
        ]
    eval_agents = selected_agents or (detected or resolve_porch_agents_list())

    manifest_issues: list[ManifestIssue] = []
    roots = discover_roots(
        scope=effective_scope,
        cwd=cwd,
        home=home,
        agents_filter=selected_agents,
        source_roots=source_roots,
        include_plugins=include_plugins,
        include_builtins=include_builtins,
        query_cli=query_cli,
        scan_skills_dirs=scan_skills_dirs,
        manifest_issues=manifest_issues,
    )
    entries, lock_issues = scan_topology(roots, home=home, cwd=cwd)
    analysis = classify_groups(entries)

    # Filter entries by name for user-visible skills (exclude warehouse-only entries)
    active_entries = [e for e in entries if e.root_kind != "source-warehouse"]
    broken_entries = [e for e in active_entries if e.is_broken]
    ghost_entries = [e for e in active_entries if e.is_ghost]
    integrity_errors = [
        e for e in active_entries
        if not e.is_broken and not e.is_ghost and any(i["severity"] == "error" for i in e.issues)
    ]
    integrity_warnings = [
        e for e in active_entries
        if not e.is_broken and not e.is_ghost and any(i["severity"] == "warning" for i in e.issues)
    ]

    logical_names = sorted({e.name for e in active_entries if not e.is_builtin})
    budgets = compute_agent_context_budgets(active_entries, eval_agents, home=home)

    usage_data: dict | None = None
    if usage_mode != "off":
        skill_set = set(logical_names)
        if usage_mode == "fast":
            since_ts = parse_since(since) if since else None
            usage_data = collect_usage_fast(skill_set, since_ts=since_ts, home=home)
        else:
            since_ts = parse_since(since, default_days=30)
            usage_data = collect_usage_deep(
                skill_set,
                since_ts=since_ts,
                home=home,
                cache_path=cache_path,
                no_cache=no_cache,
            )

    # Build Discovery-Pool matrix rows
    entries_by_name: dict[str, list[SkillEntry]] = defaultdict(list)
    for e in active_entries:
        entries_by_name[e.name].append(e)

    group_status_by_name = {g["name"]: g["status"] for g in analysis["by_name"]}
    shared_dir = home / ".agents" / "skills"
    shared_entries: set[str] = set()
    if shared_dir.is_dir():
        for item in shared_dir.iterdir():
            if not item.name.startswith(".") and (item / "SKILL.md").is_file():
                shared_entries.add(item.name)

    if expand_agents:
        matrix_cols = [(aid, aid, [aid]) for aid in eval_agents]
    else:
        matrix_cols = []
        eval_set = set(eval_agents)
        for col_id, label, col_agents in POOL_COLUMNS:
            # Show pool column only when at least one of its agents is in eval_agents
            if any(a in eval_set for a in col_agents):
                matrix_cols.append((col_id, label, col_agents))
    has_local_entries = any(e.scope == "local" for e in active_entries)
    if has_local_entries and effective_scope in ("local", "all"):
        matrix_cols.append(("local", "Local", []))
    pool_covered = {a for _, _, col_agents in matrix_cols for a in col_agents}
    has_other_agents = any(
        any(a not in pool_covered for a in e.agent_ids)
        for e in active_entries
        if not e.is_builtin
    )
    if not expand_agents and has_other_agents:
        other_agents = [a for a in AGENTS if a not in pool_covered]
        matrix_cols.append(("other", "Other", other_agents))

    matrix_rows: list[dict] = []
    usage_skills = (usage_data or {}).get("skills", {})
    for sname in sorted(entries_by_name):
        elist = entries_by_name[sname]
        if all(e.is_builtin for e in elist):
            continue
        g_status = group_status_by_name.get(sname)
        cells: dict[str, str] = {}
        for col_id, _, col_agents in matrix_cols:
            if col_id == "local":
                loc_entries = [e for e in elist if e.scope == "local"]
                if not loc_entries:
                    cells[col_id] = "—"
                elif any(e.is_broken for e in loc_entries):
                    cells[col_id] = "BRKN"
                elif any(e.is_ghost for e in loc_entries):
                    cells[col_id] = "GHST"
                elif g_status and "local-shadows-global" in g_status:
                    cells[col_id] = "SHDW"
                else:
                    cells[col_id] = "locl"
            else:
                cells[col_id] = cell_status_for_pool(
                    sname,
                    elist,
                    col_agents,
                    g_status,
                    home=home,
                    shared_dir_entries=shared_entries,
                )

        has_anomaly = (
            any(e.is_broken or e.is_ghost for e in elist)
            or any(i["severity"] in ("error", "warning") for e in elist for i in e.issues)
            or (g_status in {
                "divergent", "namespaced-divergent", "stale-backup",
                "local-shadows-global-divergent", "local-shadows-global-identical",
                "replica", "chained-hop",
            })
        )
        u_stat = usage_skills.get(sname)
        matrix_rows.append({
            "name": sname,
            "group_status": g_status or "unique",
            "has_anomaly": has_anomaly,
            "has_local": any(e.scope == "local" for e in elist),
            "cells": cells,
            "usage": u_stat,
        })

    cold_skills = []
    if usage_data is not None:
        for sname in logical_names:
            st = usage_skills.get(sname, {})
            if st.get("total_sessions", 0) == 0:
                cold_skills.append(sname)

    actionable_groups = [g for g in analysis["by_name"] if g["requires_decision"]]
    error_count = (
        len(broken_entries)
        + len(ghost_entries)
        + len(integrity_errors)
        + len(actionable_groups)
        + len(manifest_issues)
    )
    warning_count = (
        len(lock_issues)
        + len(integrity_warnings)
        + len([g for g in analysis["by_name"] if g["status"] in ("chained-hop", "replica", "local-shadows-global-identical")])
        + len(analysis["by_dir_mismatch"])
        + len(analysis["by_hash_renamed_clone"])
    )

    return {
        "schema_version": 1,
        "scope": effective_scope,
        "cwd": str(cwd),
        "repo_root": str(repo_root) if repo_root else None,
        "evaluated_agents": eval_agents,
        "summary": {
            "logical_skills": len(logical_names),
            "discovered_entries": len(active_entries),
            "broken_symlinks": len(broken_entries),
            "ghost_dirs": len(ghost_entries),
            "orphaned_lock_entries": len([l for l in lock_issues if l.kind == "orphaned-lock-entry"]),
            "manifest_issues": len(manifest_issues),
            "divergent_or_shadowed": len(actionable_groups),
            "errors": error_count,
            "warnings": warning_count,
            "has_actionable_issues": (error_count + len(lock_issues)) > 0,
        },
        "triage": {
            "broken_symlinks": [asdict(e) for e in broken_entries],
            "ghost_dirs": [asdict(e) for e in ghost_entries],
            "lockfile_issues": [asdict(l) for l in lock_issues],
            "manifest_issues": [asdict(m) for m in manifest_issues],
            "integrity_errors": [asdict(e) for e in integrity_errors],
            "integrity_warnings": [asdict(e) for e in integrity_warnings],
            "duplicates": analysis,
        },
        "context_budgets": budgets,
        "usage": usage_data,
        "cold_skills": cold_skills,
        "matrix": {
            "columns": [{"id": cid, "label": lbl} for cid, lbl, _ in matrix_cols],
            "rows": matrix_rows,
        },
    }


def format_report(report: dict, *, output_format: str = "text", show_all: bool = False) -> str:
    """Format revision results cleanly for humans (``text``/``md``) and agents (``json``)."""
    if output_format == "json":
        return json.dumps(report, indent=2)

    s = report["summary"]
    t = report["triage"]
    lines: list[str] = []

    if output_format == "md":
        lines.append("# Skill Revision Report")
    else:
        lines.append("=" * 72)
        lines.append("SKILL REVISION & TOPOLOGY DOCTOR")
        lines.append("=" * 72)

    lines.append(f"Scope: {report['scope']} | CWD: {report['cwd']}")
    if report["repo_root"]:
        lines.append(f"Repo:  {report['repo_root']}")
    lines.append(
        f"Summary: {s['logical_skills']} logical skills across {s['discovered_entries']} entries | "
        f"{s['broken_symlinks']} broken links | {s['ghost_dirs']} ghost dirs | "
        f"{s['orphaned_lock_entries']} orphaned lock entries | {s['divergent_or_shadowed']} divergent/shadowed"
    )
    if report.get("usage"):
        cov = report["usage"].get("coverage", {})
        lines.append(
            f"Usage ({report['usage']['mode']}, since {report['usage']['since']}): "
            f"{cov.get('note', '')} | sources={','.join(cov.get('sources', cov.get('stores', {}).keys()))}"
        )
    else:
        lines.append("Usage: off (pass --usage fast or --usage deep --since 30d)")

    # Bucket 1: Broken & Orphaned
    b1_count = (
        len(t["broken_symlinks"])
        + len(t["ghost_dirs"])
        + len(t["lockfile_issues"])
        + len(t["manifest_issues"])
    )
    lines.append("")
    lines.append(f"## 1. Broken & Orphaned ({b1_count})")
    if b1_count == 0:
        lines.append("  None.")
    else:
        if t["broken_symlinks"]:
            lines.append(f"  Broken symlinks ({len(t['broken_symlinks'])}):")
            shown = t["broken_symlinks"] if show_all else t["broken_symlinks"][:12]
            for e in shown:
                extra = ""
                if e.get("rename_hint"):
                    extra = f" [NOTE: {e['rename_hint']}]"
                elif e.get("repoint_candidates"):
                    extra = f" [repoint match: {e['repoint_candidates'][0]['path']}]"
                lines.append(f"    - BRKN {e['path']} -> {e.get('raw_target')} ({e.get('broken_reason')}){extra}")
            if not show_all and len(t["broken_symlinks"]) > 12:
                lines.append(f"    ... +{len(t['broken_symlinks']) - 12} more (pass --all to list all)")
        if t["ghost_dirs"]:
            lines.append(f"  Ghost directories without SKILL.md ({len(t['ghost_dirs'])}):")
            for e in t["ghost_dirs"]:
                lines.append(f"    - GHST {e['path']}")
        if t["lockfile_issues"]:
            lines.append(f"  Lockfile orphans ({len(t['lockfile_issues'])}):")
            shown = t["lockfile_issues"] if show_all else t["lockfile_issues"][:10]
            for l in shown:
                lines.append(f"    - LOCK {l['skill']} ({l['source']}) in {l['lockfile']}")
            if not show_all and len(t["lockfile_issues"]) > 10:
                lines.append(f"    ... +{len(t['lockfile_issues']) - 10} more orphans in .skill-lock.json")
        if t["manifest_issues"]:
            lines.append(f"  Manifest issues ({len(t['manifest_issues'])}):")
            for m in t["manifest_issues"]:
                lines.append(f"    - MANF {m['manifest']}: {m['entry_path']} ({m['kind']})")
        lines.append("  Next (dry-run): uv run scripts/sync_skills.py --prune-broken")

    # Bucket 2: Divergent, Shadowed & Integrity
    dups = t["duplicates"]
    actionable = [g for g in dups["by_name"] if g["requires_decision"]]
    b2_count = (
        len(actionable)
        + len(t["integrity_errors"])
        + len(dups["by_dir_mismatch"])
        + len(dups["by_hash_renamed_clone"])
    )
    lines.append("")
    lines.append(f"## 2. Divergent, Shadowed & Integrity ({b2_count})")
    if b2_count == 0:
        lines.append("  None.")
    else:
        for g in actionable:
            diff_txt = ""
            if d := g.get("diff"):
                diff_txt = f" | modified={len(d.get('modified_files', []))}, line_delta={d.get('body_lines_delta', 0)}"
            lines.append(f"  - {g['status'].upper()} {g['name']}{diff_txt}")
            for rec in g["entries"]:
                lines.append(f"      {rec['path']} [{rec['scope']}/{rec['root_kind']}] ({rec['provenance']})")
        for e in t["integrity_errors"]:
            msgs = "; ".join(i["message"] for i in e["issues"] if i["severity"] == "error")
            lines.append(f"  - ERR {e['name']} ({e['path']}): {msgs}")
        for m in dups["by_dir_mismatch"]:
            lines.append(f"  - DIR_MISMATCH folder '{m['dir_name']}' holds different names: {', '.join(m['names'])}")
        for r in dups["by_hash_renamed_clone"]:
            lines.append(f"  - IDENTICAL_CLONE hash {r['hash']} shared by names: {', '.join(r['names'])}")
        lines.append("  Security deep scan: use skill 'skill-inspector' on third-party skills if provenance is unknown.")

    # Bucket 3: Topology, Context Budget & Usage
    chained = [g for g in dups["by_name"] if g["status"] == "chained-hop"]
    replicas = [g for g in dups["by_name"] if g["status"] in ("replica", "local-shadows-global-identical")]
    lines.append("")
    lines.append(f"## 3. Topology & Startup Context Budget (chained={len(chained)}, replicas={len(replicas)})")
    if chained:
        lines.append("  Chained / relative symlinks (collapse cleanly with sync_skills.py --collapse-hops):")
        hop_lines: list[tuple[int, str]] = []
        for g in chained:
            for rec in g["entries"]:
                hops = rec.get("hop_count", 0)
                if hops >= 2 or rec.get("is_relative_symlink"):
                    tag = f"hop{hops}" if hops >= 2 else "rel1"
                    hop_lines.append((-hops, f"    - {tag} {rec['path']} -> {rec.get('raw_target')} -> {rec.get('real_path')}"))
        hop_lines.sort(key=lambda item: item[0])
        shown_hops = hop_lines if show_all else hop_lines[:10]
        for _, hl in shown_hops:
            lines.append(hl)
        if not show_all and len(hop_lines) > 10:
            lines.append(f"    ... +{len(hop_lines) - 10} more chained/relative links (pass --all for full list)")
    if replicas:
        lines.append("  Identical copy replicas (converge with sync_skills.py --converge-replicas):")
        for g in replicas[:8]:
            lines.append(f"    - {g['name']}: {', '.join(r['path'] for r in g['entries'])}")

    # Startup context budget table
    lines.append("")
    lines.append("  Startup Context Budget (name + description):")
    for aid, b in report["context_budgets"].items():
        warn = f" [!] {'; '.join(b['warnings'])}" if b["warnings"] else ""
        lines.append(f"    - {aid:16s}: {b['skill_count']:3d} skills | {b['total_chars']:6d} chars (~{b['est_tokens']:5d} tok){warn}")

    if report.get("usage") is not None:
        cold = report["cold_skills"]
        lines.append(
            f"  Cold skills (0 observed sessions since {report['usage']['since']}): {len(cold)}"
            + (f" — sample: {', '.join(cold[:10])}" if cold else "")
        )

    # Discovery-Pool Matrix
    cols = report["matrix"]["columns"]
    rows = report["matrix"]["rows"] if show_all else [r for r in report["matrix"]["rows"] if r["has_anomaly"] or r["has_local"]]
    lines.append("")
    lines.append(
        f"## 4. Availability Matrix ({len(rows)}/{len(report['matrix']['rows'])} skills shown"
        + ("" if show_all else "; anomalies/local only — pass --all for full table")
        + ")"
    )
    lines.append("  Legend: link=1-hop | hop2=chained/rel | copy=dir | shrd=via ~/.agents | plug=plugin | bndl=Hermes | locl=project | BRKN/GHST/DRFT/SHDW=issue | —=absent")
    if rows:
        has_usage = report.get("usage") is not None
        header_cols = [c["label"] for c in cols]
        name_w = max(24, min(36, max(len(r["name"]) for r in rows) + 2))
        col_widths = [max(4, min(14, len(lbl))) for lbl in header_cols]
        hdr = f"  {'Skill':<{name_w}} " + " ".join(f"{lbl:<{w}}" for lbl, w in zip(header_cols, col_widths))
        if has_usage:
            hdr += "  Used"
        lines.append(hdr)
        lines.append("  " + "-" * (len(hdr) - 2))
        for r in rows:
            nm = r["name"][:name_w]
            vals = " ".join(f"{r['cells'].get(c['id'], '—'):<{w}}" for c, w in zip(cols, col_widths))
            u_txt = ""
            if has_usage:
                u = r.get("usage") or {}
                tot = u.get("total_sessions", 0)
                exp = u.get("explicit_sessions", 0)
                agt = u.get("agent_sessions", 0)
                u_txt = f"  {tot} ({exp}e/{agt}a)" if tot else "  0"
            lines.append(f"  {nm:<{name_w}} {vals}{u_txt}")
    else:
        lines.append("  No anomalies found in evaluated scope. Pass --all to view every skill.")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only skill revision, topology check, startup budget, and usage doctor"
    )
    parser.add_argument("--scope", choices=["auto", "global", "local", "all"], default="auto")
    parser.add_argument("--cwd", type=Path, default=Path.cwd(), help="Working directory for local/monorepo discovery")
    parser.add_argument("--agent", "-a", "--agents", action="append", dest="agents", help="Agent(s) or porch harness aliases (comma-separated or repeatable)")
    parser.add_argument("--porch-harnesses", action="store_true", help="Evaluate all skill-consuming harnesses supported by porch")
    parser.add_argument("--expand-agents", action="store_true", help="Expand Shared(~/.agents) pool into individual agent columns")
    parser.add_argument("--all", action="store_true", help="Show healthy rows too (default is anomaly-first triage)")
    parser.add_argument("--usage", choices=["off", "fast", "deep"], default="fast", help="Usage telemetry mode (default: fast)")
    parser.add_argument("--since", help="Time window for usage telemetry (e.g. 14d, 30d, 2026-11-01, all)")
    parser.add_argument("--source-root", action="append", type=Path, default=[], help="Bounded canonical source/warehouse directory for repoint hints")
    parser.add_argument("--scan-skills-dirs", action="store_true", help="Bounded local scan of nested */skills/* inside --cwd")
    parser.add_argument("--no-plugins", action="store_true", help="Skip plugin cache/install roots")
    parser.add_argument("--include-builtins", action="store_true", help="Include read-only builtin skill layers")
    parser.add_argument("--query-cli", action="store_true", help="Query `agy plugin list` / `claude plugin list` subprocesses")
    parser.add_argument("--no-cache", action="store_true", help="Bypass usage cache in --usage deep")
    parser.add_argument("--format", "-f", choices=["text", "md", "json"], default="text")
    parser.add_argument("--fail-on-issues", action="store_true", help="Exit 2 when errors, broken links, orphans, or divergent skills exist")
    args = parser.parse_args()

    try:
        report = run_revision(
            scope=args.scope,
            cwd=args.cwd,
            agents_filter=args.agents,
            porch_harnesses=args.porch_harnesses,
            expand_agents=args.expand_agents,
            usage_mode=args.usage,
            since=args.since,
            source_roots=args.source_root,
            scan_skills_dirs=args.scan_skills_dirs,
            include_plugins=not args.no_plugins,
            include_builtins=args.include_builtins,
            query_cli=args.query_cli,
            no_cache=args.no_cache,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(format_report(report, output_format=args.format, show_all=args.all))
    if args.fail_on_issues and report["summary"]["has_actionable_issues"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
