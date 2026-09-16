"""Session reflection/analytics layer over lib/sessions.py fragments.

Adds three read-only commands to `consilium sessions`:

  turns  — one JSONL row per user-triggered turn (TraceLab definition: from
           the triggering human prompt to the last agent output before the
           next triggering prompt), with per-turn metrics and locator pairs.
  flags  — deterministic anti-pattern detections, each with evidence
           locators back into the raw store (retry_loop, search_loop,
           edit_without_read, correction(_burst), abandoned,
           permission_friction, context_pressure, interrupted, error_burst,
           failed_run).
  stats  — grouped aggregates (--by model|harness|cwd|day) plus honest
           coverage: dedup rule, sessions without model, malformed counts.

The tool never issues verdicts: it prepares evidence-linked aggregates;
the calling LLM synthesizes "top insights" by reading `show --around` on
flagged locators.
"""
from __future__ import annotations

import json
import re
import statistics
import sys
from pathlib import Path
from typing import Any, Iterator

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sessions as S  # noqa: E402

# A prompt starts a new turn only when the current turn already contains a
# non-prompt fragment — adjacent prompts are steering/multi-message input or
# store-internal mirrors of the same submission (codex event_msg.user_message
# is mirrored by response_item.user).
TRIGGER_AUTHORSHIP = {"human", "unknown"}

SEARCH_TOOLS = {
    "read", "grep", "glob", "search", "websearch", "webfetch", "view",
    "file_search", "list_dir", "find", "ls", "rg", "codebase_search",
}
MUTATION_TOOLS = {
    "edit", "write", "multiedit", "apply_patch", "str_replace", "create",
    "notebookedit", "writefile", "editfile",
}
PATH_KEYS = ("file_path", "filepath", "path", "notebook_path", "target_file",
             "filename", "file")

# Lexical correction markers — deliberately simple and explainable; the flag
# carries `basis` so a reader can verify rather than trust the classifier.
CORRECTION_MARKERS = (
    "that's not", "not what i", "wrong", "you didn't", "you forgot",
    "revert", "undo", "stop,", "instead", "actually,", "не так", "не то",
    "отмени", "верни", "зачем ты", "ты не ", "остановись", "нет,", "не надо",
    "неправильн", "ошибка", "сломал",
)

RETRY_MIN_RUN = 3          # identical tool calls in a row
SEARCH_LOOP_MIN = 5        # consecutive search-type calls without mutation
ERROR_BURST_WINDOW = 10    # fragments
ERROR_BURST_MIN = 3
CORRECTION_BURST_MIN = 3
PERMISSION_FRICTION_MIN = 3

# Usage semantics differ per harness: claude/gemini/opencode emit per-request
# usage (sum to get session total); codex token_count is a cumulative snapshot
# within a turn (max, not sum — summing double-counts).
CUMULATIVE_USAGE = {"codex"}


def _tool_info(f: dict[str, Any]) -> tuple[str | None, dict[str, Any]]:
    """(tool name, input dict) from a tool_call fragment's rel/text."""
    tool = (f.get("rel") or {}).get("tool")
    text = f.get("text")
    data = None
    if isinstance(text, str) and text.startswith("{"):
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = None
    if isinstance(data, dict):
        tool = tool or data.get("name") or data.get("tool")
        inp = data.get("input") or data.get("arguments") or data.get("args") \
            or data.get("params") or {}
        if isinstance(inp, str):
            try:
                inp = json.loads(inp)
            except json.JSONDecodeError:
                inp = {"_raw": inp}
        return (str(tool).lower() if tool else None,
                inp if isinstance(inp, dict) else {"_raw": inp})
    return (str(tool).lower() if tool else None), {}


def _tool_path(inp: dict[str, Any]) -> str | None:
    for k in PATH_KEYS:
        v = inp.get(k)
        if isinstance(v, str) and v:
            return v
    return None


def _is_correction(text: Any) -> bool:
    if not isinstance(text, str):
        return False
    low = text.lower()
    return any(m in low for m in CORRECTION_MARKERS)


def _new_turn(seq_key: tuple[str, str, str]) -> dict[str, Any]:
    return {
        "seq_key": seq_key, "turn": 1, "ts_start": None, "ts_end": None,
        "models": set(), "user_msgs": 0, "prompts": [], "tool_calls": 0,
        "tool_errors": 0, "retries": 0, "assistant_msgs": 0, "reasoning": 0,
        "compactions": 0, "permissions": 0, "interrupted": 0,
        "usage": {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0, "total": 0},
        "usage_max": {},
        "has_final": False, "first_locator": None, "last_locator": None,
        "first_seq": None, "last_seq": None, "agent_output": False,
    }


def _canon_key(store: S.Store, ref: S.SessionRef) -> tuple[str, str]:
    """Dedup identity across layered stores of the same conversation."""
    if store.harness == "claude-desktop" and ref.extra.get("cli_session_id"):
        return ("claude", str(ref.extra["cli_session_id"]))
    if store.harness == "claude-code":
        return ("claude", Path(ref.session_id).name)
    return (store.harness, ref.session_id)


def iter_dedup_sessions(stores: list[S.Store], args: Any,
                        stats: dict[str, int]) -> Iterator[tuple[S.Store, S.SessionRef, list[dict[str, Any]]]]:
    """Yield (store, ref, fragments) once per canonical conversation.

    Layered stores repeat a thread (codex rollout vs state index vs catalog;
    claude-desktop manifest vs linked claude transcript; consilium run vs the
    agent's own session). First occurrence wins — stores arrive in canonical
    order from selected_stores(). Metadata-only layers still yield a session
    (their own fragments) but never fabricate turns: a turn needs a trigger.
    """
    seen: set[tuple[str, str]] = set()
    seen_native: set[str] = set()
    since, until = S.parse_time_bound(args.since), S.parse_time_bound(args.until)
    for store in stores:
        if store.status != "ok":
            continue
        for ref in S.iter_all_sessions(store, args.cwd, since, until):
            stats["sessions_scanned"] = stats.get("sessions_scanned", 0) + 1
            key = _canon_key(store, ref)
            native = ref.extra.get("native_session")
            if key in seen or (native and str(native) in seen_native):
                stats["deduped"] = stats.get("deduped", 0) + 1
                continue
            seen.add(key)
            seen_native.add(key[1])
            frags = list(S.iter_all_fragments(store, ref, args.max_chars, stats))
            yield store, ref, frags


def analyze_session(store: S.Store, ref: S.SessionRef,
                    frags: list[dict[str, Any]],
                    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Build turn rows + flag rows for one session's fragment list."""
    seq_key = (ref.harness, store.name, ref.session_id)
    turns: list[dict[str, Any]] = []
    flags: list[dict[str, Any]] = []
    cur = _new_turn(seq_key)
    corrections = 0
    perm_count = 0
    compactions = 0
    interruptions = 0
    session_had_output = False
    read_paths: set[str] = set()
    seen_call_ids: set[str] = set()   # devin node forest replays the same call_id per branch
    call_run: list[tuple[str, str]] = []   # consecutive identical tool_call sigs across steps
    search_run: list[dict[str, Any]] = []  # consecutive search-type steps
    last_call_step: str | None = None      # locator key of previous tool_call
    err_window: list[dict[str, Any]] = []
    err_burst_emitted = False
    failed_boundary = False

    def flag(pattern: str, turn: int, evidence: list[dict[str, Any]],
             quote: str | None = None, basis: str = "") -> None:
        # evidence items: fragments (carry seq+locator) or bare locators —
        # `show --around` wants seq, so always include it when known
        ev = []
        for e in evidence:
            item = {"seq": e["seq"], "locator": e["locator"]} if "seq" in e and "locator" in e else e
            if item not in ev:
                ev.append(item)
            if len(ev) >= 4:
                break
        flags.append({
            "pattern": pattern, "harness": ref.harness, "store": store.name,
            "session_id": ref.session_id, "turn": turn,
            "evidence": ev, "quote": (quote or "")[:160] or None,
            "basis": basis,
        })

    def close_turn() -> None:
        nonlocal cur
        if not cur["user_msgs"]:
            return  # no triggering prompt → not a turn (prelude folds forward)
        turns.append(cur)
        cur = _new_turn(seq_key)
        cur["turn"] = len(turns) + 1

    for f in frags:
        kind = f.get("kind")
        auth = f.get("authorship") or "unknown"  # frag() omits the key for "unknown"
        trigger = kind == "prompt" and auth in TRIGGER_AUTHORSHIP
        if trigger and cur["user_msgs"] and not cur["agent_output"]:
            # adjacent prompt with no agent output in between → same request
            cur["user_msgs"] += 1
            cur["prompts"].append(f.get("text"))
            cur["last_locator"] = f.get("locator")
            cur["last_seq"] = f.get("seq")
            continue
        if trigger:
            if cur["user_msgs"] and cur["agent_output"]:
                close_turn()
            cur["user_msgs"] += 1
            cur["prompts"].append(f.get("text"))
            if cur["first_locator"] is None:
                cur["first_locator"] = f.get("locator")
                cur["first_seq"] = f.get("seq")
                cur["ts_start"] = f.get("ts")
            cur["last_locator"] = f.get("locator")
            cur["last_seq"] = f.get("seq")
            if _is_correction(f.get("text")) and turns:
                corrections += 1
                flag("correction", cur["turn"], [f],
                     quote=f.get("text"),
                     basis="prompt matches lexical correction markers — verify by reading context")
            continue

        if cur["first_locator"] is None:
            cur["first_locator"] = f.get("locator")
            cur["first_seq"] = f.get("seq")
            cur["ts_start"] = f.get("ts")
        cur["last_locator"] = f.get("locator")
        cur["last_seq"] = f.get("seq")
        if f.get("ts"):
            cur["ts_end"] = f["ts"]
        if f.get("model"):
            cur["models"].add(f["model"])
        u = f.get("usage") or {}
        for k in cur["usage"]:
            if u.get(k):
                cur["usage"][k] += u[k]
                cur["usage_max"][k] = max(cur["usage_max"].get(k, 0), u[k])
        if kind in ("assistant", "tool_call", "reasoning"):
            cur["agent_output"] = True
            session_had_output = True
        if kind == "assistant":
            cur["assistant_msgs"] += 1
            cur["has_final"] = True
        elif kind == "reasoning":
            cur["reasoning"] += 1
        elif kind == "tool_call":
            cid = (f.get("rel") or {}).get("call_id")
            if ref.harness == "devin" and cid and cid in seen_call_ids:
                continue  # node-forest branch replay of the same tool call
            if cid:
                seen_call_ids.add(cid)
            cur["tool_calls"] += 1
            cur["has_final"] = False
            tool, inp = _tool_info(f)
            if f.get("error"):
                cur["tool_errors"] += 1
            if tool:
                p = _tool_path(inp)
                if tool in SEARCH_TOOLS and p:
                    read_paths.add(p)
                if tool in MUTATION_TOOLS and p and p not in read_paths:
                    flag("edit_without_read", cur["turn"], [f],
                         quote=p,
                         basis="mutation on a path with no earlier Read call in this session")
                # Calls fanned out from one raw record (same locator) are one
                # parallel step, not N sequential calls — collapse them for
                # run detection. When `input` fails to parse (e.g. text was
                # truncated by --max-chars), fall back to the raw text so
                # different args still differ — an empty sig would collapse
                # every same-named call into one fake "identical" run.
                step = json.dumps(f.get("locator"), sort_keys=True, default=str)
                same_step = bool(step == last_call_step)
                if inp:
                    sig = json.dumps(inp, sort_keys=True, ensure_ascii=False)[:200]
                else:
                    sig = (f.get("text") or "")[:200]
                if not same_step:
                    last_call_step = step
                    if call_run and call_run[-1] == (tool, sig):
                        call_run.append((tool, sig))
                        if len(call_run) == RETRY_MIN_RUN:
                            flag("retry_loop", cur["turn"],
                                 [f], quote=tool,
                                 basis=f"≥{RETRY_MIN_RUN} identical {tool} calls across consecutive steps")
                        elif len(call_run) > RETRY_MIN_RUN:
                            cur["retries"] += 1
                    else:
                        call_run = [(tool, sig)]
                    if tool in SEARCH_TOOLS:
                        search_run.append(f)
                        if len(search_run) == SEARCH_LOOP_MIN:
                            flag("search_loop", cur["turn"],
                                 search_run[:2] + [search_run[-1]],
                                 basis=f"≥{SEARCH_LOOP_MIN} consecutive search/read steps without a mutation")
                    elif tool in MUTATION_TOOLS:
                        search_run.clear()
            else:
                call_run.clear()
                search_run.clear()
                last_call_step = None
        elif kind == "tool_result":
            if f.get("error"):
                cur["tool_errors"] += 1
        elif kind == "permission":
            perm_count += 1
            cur["permissions"] += 1
        elif kind == "compaction":
            compactions += 1
            cur["compactions"] += 1
        elif kind == "boundary" and f.get("status") in ("failed", "error"):
            failed_boundary = True
        if f.get("interrupted"):
            interruptions += 1
            cur["interrupted"] += 1
        if f.get("error"):
            err_window.append(f)
            err_window = err_window[-ERROR_BURST_WINDOW:]
            if len(err_window) >= ERROR_BURST_MIN and not err_burst_emitted:
                err_burst_emitted = True
                flag("error_burst", cur["turn"],
                     err_window[:3],
                     basis=f"≥{ERROR_BURST_MIN} error fragments within {ERROR_BURST_WINDOW}")
        elif kind in ("prompt", "assistant"):
            err_window.clear()

    close_turn()

    # session-level flags
    last = turns[-1] if turns else None
    if last and not last["has_final"] and not last["agent_output"] and session_had_output:
        flag("abandoned", last["turn"],
             [{"seq": last["first_seq"], "locator": last["first_locator"]},
              {"seq": last["last_seq"], "locator": last["last_locator"]}],
             quote=(last["prompts"] or [None])[-1],
             basis="session ends on an unanswered human prompt after earlier agent activity")
    if corrections >= CORRECTION_BURST_MIN:
        flag("correction_burst", 0, [{"seq": t["first_seq"], "locator": t["first_locator"]} for t in turns if t],
             basis=f"{corrections} correction prompts in one session")
    if perm_count >= PERMISSION_FRICTION_MIN:
        flag("permission_friction", 0, [],
             basis=f"{perm_count} permission events in one session")
    if compactions:
        flag("context_pressure", 0, [], basis=f"{compactions} compaction event(s)")
    if interruptions:
        flag("interrupted", 0, [], basis=f"{interruptions} interrupt record(s)")
    if failed_boundary:
        flag("failed_run", 0, [], basis="terminal boundary status=failed/error")

    rows = []
    for i, t in enumerate(turns):
        t["turn"] = i + 1
        dur = None
        a, b = S.ts_epoch(t["ts_start"]), S.ts_epoch(t["ts_end"])
        if a is not None and b is not None and b >= a:
            dur = round(b - a, 1)
        src = t["usage_max"] if ref.harness in CUMULATIVE_USAGE else t["usage"]
        usage = {k: v for k, v in src.items() if v}
        rows.append({
            "harness": ref.harness, "store": store.name,
            "session_id": ref.session_id, "turn": t["turn"],
            "ts_start": t["ts_start"], "ts_end": t["ts_end"],
            "duration_s": dur, "cwd": ref.cwd,
            "models": sorted(t["models"]) or ([ref.models[0]] if ref.models else []),
            "user_msgs": t["user_msgs"], "tool_calls": t["tool_calls"],
            "tool_errors": t["tool_errors"], "retries": t["retries"],
            "assistant_msgs": t["assistant_msgs"], "reasoning": t["reasoning"],
            "compactions": t["compactions"], "permissions": t["permissions"],
            "interrupted": t["interrupted"], "has_final": t["has_final"],
            "usage": usage or None,
            "first_locator": t["first_locator"], "last_locator": t["last_locator"],
        })
    # flag rows reference turn numbers — already assigned sequentially above
    return rows, flags


def _emit(o: dict[str, Any]) -> None:
    print(json.dumps(o, ensure_ascii=False, default=str), flush=True)


def _session_meta(ref: S.SessionRef) -> dict[str, Any]:
    d = ref.as_dict()
    return {k: d[k] for k in ("title", "cwd", "models", "created") if k in d}


def cmd_turns(args: Any) -> int:
    stores = S.selected_stores(S.resolve_harnesses(args.agent), getattr(args, "store", None))
    stats: dict[str, int] = {}
    emitted = 0
    for store, ref, frags in iter_dedup_sessions(stores, args, stats):
        rows, _flags = analyze_session(store, ref, frags)
        for r in rows:
            r["session"] = _session_meta(ref)
            _emit(r)
            emitted += 1
            if args.limit and emitted >= args.limit:
                break
        if args.limit and emitted >= args.limit:
            break
    _emit(_summary(stores, stats, emitted))
    return S.EXIT_OK


def cmd_flags(args: Any) -> int:
    stores = S.selected_stores(S.resolve_harnesses(args.agent), getattr(args, "store", None))
    stats: dict[str, int] = {}
    emitted = 0
    wanted = getattr(args, "kind", None)
    for store, ref, frags in iter_dedup_sessions(stores, args, stats):
        _rows, flags = analyze_session(store, ref, frags)
        for fl in flags:
            if wanted and fl["pattern"] != wanted:
                continue
            fl["session"] = _session_meta(ref)
            _emit(fl)
            emitted += 1
            if args.limit and emitted >= args.limit:
                break
        if args.limit and emitted >= args.limit:
            break
    _emit(_summary(stores, stats, emitted))
    return S.EXIT_OK


def cmd_stats(args: Any) -> int:
    stores = S.selected_stores(S.resolve_harnesses(args.agent), getattr(args, "store", None))
    stats: dict[str, int] = {}
    by = getattr(args, "by", "model")
    groups: dict[str, dict[str, Any]] = {}

    def bucket(ref: S.SessionRef, row: dict[str, Any]) -> str:
        if by == "model":
            return (row.get("models") or ref.models or ["<unknown>"])[0]
        if by == "harness":
            return ref.harness
        if by == "cwd":
            return ref.cwd or "<none>"
        if by == "day":
            return (row.get("ts_start") or "")[:10] or "<unknown>"
        return ref.harness

    flagged_sessions: dict[str, int] = {}
    flag_sessions: dict[str, set[str]] = {}   # pattern -> distinct session keys
    for store, ref, frags in iter_dedup_sessions(stores, args, stats):
        rows, flags = analyze_session(store, ref, frags)
        # per-session token total: per-request harnesses sum turns; cumulative
        # snapshot harnesses (codex) take the last/max turn value
        sess_tokens: dict[str, int] = {}
        for r in rows:
            for k, v in (r.get("usage") or {}).items():
                if ref.harness in CUMULATIVE_USAGE:
                    sess_tokens[k] = max(sess_tokens.get(k, 0), v)
                else:
                    sess_tokens[k] = sess_tokens.get(k, 0) + v
        if not rows:
            # session without turns (metadata-only layer or empty) still counts
            key = bucket(ref, {})
            g = groups.setdefault(key, _new_group())
            g["sessions"] += 1
            if not ref.models:
                g["sessions_no_model"] += 1
            continue
        skey = f"{ref.harness}:{ref.session_id}"
        flagged_sessions[skey] = flagged_sessions.get(skey, 0) + len(flags)
        for fl in flags:
            key = bucket(ref, rows[0])
            g = groups.setdefault(key, _new_group())
            g["flags"][fl["pattern"]] = g["flags"].get(fl["pattern"], 0) + 1
            g["flag_sessions"].setdefault(fl["pattern"], set()).add(skey)
            flag_sessions.setdefault(fl["pattern"], set()).add(skey)
        for r in rows:
            key = bucket(ref, r)
            g = groups.setdefault(key, _new_group())
            if r["turn"] == 1:
                g["sessions"] += 1
                g["sessions_with_turns"] += 1
                if not r["models"] and not ref.models:
                    g["sessions_no_model"] += 1
            g["turns"] += 1
            g["user_msgs"] += r["user_msgs"]
            g["tool_calls"] += r["tool_calls"]
            g["tool_errors"] += r["tool_errors"]
            g["corrections"] += 0  # counted via flags below
            g["compactions"] += r["compactions"]
            g["interrupted"] += r["interrupted"]
            if r["duration_s"] is not None:
                g["durations"].append(r["duration_s"])
        if rows and sess_tokens:
            g = groups.setdefault(bucket(ref, rows[0]), _new_group())
            for k, v in sess_tokens.items():
                g["tokens"][k] = g["tokens"].get(k, 0) + v
    out = []
    for key, g in sorted(groups.items(), key=lambda kv: -kv[1]["turns"]):
        turns = g["turns"] or 1
        out.append({
            "group": key, "by": by,
            "sessions": g["sessions"], "sessions_with_turns": g["sessions_with_turns"],
            "sessions_no_model": g["sessions_no_model"],
            "turns": g["turns"], "user_msgs": g["user_msgs"],
            "tool_calls": g["tool_calls"], "tool_errors": g["tool_errors"],
            "tool_error_rate": round(g["tool_errors"] / max(g["tool_calls"], 1), 3),
            "compactions": g["compactions"], "interrupted": g["interrupted"],
            "median_turn_duration_s": (round(statistics.median(g["durations"]), 1)
                                       if g["durations"] else None),
            "durations_n": len(g["durations"]),
            "tokens": g["tokens"] or None,
            "flags": g["flags"] or None,
            "flag_sessions": ({p: len(v) for p, v in g["flag_sessions"].items()}
                              if g["flag_sessions"] else None),
        })
    for o in out:
        _emit(o)
    top = [(k, v) for k, v in flagged_sessions.items() if v > 0]
    top.sort(key=lambda kv: -kv[1])
    top = top[:10]
    if top:
        _emit({"_top_flagged": [{"session": k, "flags": v} for k, v in top]})
    _emit(_summary(stores, stats, sum(o["turns"] for o in out)))
    return S.EXIT_OK


def _new_group() -> dict[str, Any]:
    return {"sessions": 0, "sessions_with_turns": 0, "sessions_no_model": 0,
            "turns": 0, "user_msgs": 0, "tool_calls": 0, "tool_errors": 0,
            "corrections": 0, "compactions": 0, "interrupted": 0,
            "durations": [], "tokens": {}, "flags": {}, "flag_sessions": {}}


def _summary(stores: list[S.Store], stats: dict[str, int], emitted: int) -> dict[str, Any]:
    return {
        "_summary": True,
        "stores": [{"harness": s.harness, "store": s.name, "path": str(s.path),
                    "status": s.status, "error": s.error} for s in stores],
        "sessions_scanned": stats.get("sessions_scanned", 0),
        "deduped_layers": stats.get("deduped", 0),
        "emitted": emitted,
        "malformed_records": stats.get("malformed", 0),
        "unreadable_files": stats.get("unreadable", 0),
        "dedup_rule": "first canonical layer wins (rollout/transcript > index/catalog); "
                      "claude-desktop code-sessions keyed by cliSessionId; "
                      "consilium runs deduped by native_session",
        "note": "flags/turns are deterministic heuristics with evidence locators — "
                "verify a claim via `sessions show <harness:id> --around SEQ` before quoting it",
    }
