#!/usr/bin/env python3
"""Normalize backend CLI streams into consilium event JSONL.

Reads newline-delimited JSON (or plain text) from stdin or a file.
Writes validated ConsiliumEvent records to stdout (one JSON object per line).

When used mid-flight (stdin from a live backend pipe):
  - each raw line is persisted immediately via --raw-out (flushed)
  - each event is normalized and emitted immediately (flushed)
  - with --progress, compact semantic progress is written to stderr immediately
  - unknown stream types are rejected for normalized artifacts (protocol drift)

Normalized event schema (closed ConsiliumEvent types — see events.py):
  {"ts": ISO8601, "backend": str, "agent_id": str, "type": str, "data": str|null, "raw": object|null}

  type ∈ {run_started, thinking_delta, answer_delta, tool_started, tool_completed,
          retry_scheduled, steer_*, result, progress, user_replay, turn_*,
          prompt_complete, run_completed, run_failed}

Supported backends:
  - grok-build streaming-json: types thought|text|end|error|*
  - codex --json: passthrough map of known types
  - claude stream-json: content_block_delta etc.
  - opencode --format json: message/part events
  - plain: each line becomes answer_delta

Exit codes:
  0 — success (for grok: requires run_completed/end, no run_failed/error, unless --no-validate)
  1 — grok validation failure (error event or missing end)
  2 — usage
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from typing import Any, Dict, Optional, TextIO, Tuple

from events import (
    EventValidationError,
    assemble_final_text,
    make_event,
    map_stream_type,
)
from debug_tape import close_global_tape, init_global_tape, tape_record


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def emit_event(out: TextIO, evt) -> None:
    """Persist a validated ConsiliumEvent; never write unknown types."""
    out.write(evt.to_json() + "\n")
    out.flush()
    tape_record(
        "NORMALIZED",
        {"type": evt.type, "backend": evt.backend, "agent_id": evt.agent_id},
        content_preview=str(evt.data) if evt.data is not None else "",
    )


def progress_event(agent_id: str, typ: str, data: Any = None) -> None:
    """Compact semantic progress → stderr (matches progress.sh format)."""
    preview = ""
    if data is not None:
        preview = str(data).replace("\n", " ")
        if len(preview) > 80:
            preview = preview[:77] + "..."
    if preview:
        sys.stderr.write(f"[consilium] event agent={agent_id} type={typ} data={preview}\n")
    else:
        sys.stderr.write(f"[consilium] event agent={agent_id} type={typ}\n")
    sys.stderr.flush()
    tape_record(
        "RENDERED",
        {"agent_id": agent_id, "progress_type": typ},
        content_preview=preview,
    )


class ProgressReporter:
    """Coalesce token-sized deltas into readable live progress lines."""

    def __init__(self, agent_id: str) -> None:
        self.agent_id = agent_id
        self.typ = ""
        self.buffer = ""
        self.emitted = False

    def flush(self) -> None:
        if self.buffer:
            progress_event(self.agent_id, self.typ, self.buffer)
            self.buffer = ""
            self.emitted = True

    def feed(self, typ: str, data: Any = None) -> None:
        if typ not in ("text", "thought"):
            self.flush()
            progress_event(self.agent_id, typ, data)
            self.typ = ""
            return

        if self.typ and typ != self.typ:
            self.flush()
        self.typ = typ
        chunk = "" if data is None else str(data)
        self.buffer += chunk

        threshold = 12 if not self.emitted else 72
        sentence_boundary = (
            len(self.buffer) >= 24
            and self.buffer.rstrip().endswith((".", "!", "?", ":"))
        )
        if "\n" in chunk or len(self.buffer) >= threshold or sentence_boundary:
            self.flush()


class CompactProgressReporter:
    """Content-free liveness progress for model output and tool activity."""

    LABEL = {
        "thought": "thinking",
        "text": "answering",
        "tool_started": "tool",
        "tool_completed": "tool",
        "progress": "tool",
    }

    def __init__(self, agent_id: str, interval: float = 10.0) -> None:
        self.agent_id = agent_id
        self.interval = interval
        self.phase = ""
        self.chunks = 0
        self.chars = 0
        self.started = time.monotonic()
        self.last_emit = 0.0
        self.emitted_in_phase = False
        self.pending = False

    def _emit(self) -> None:
        if not self.phase or self.chunks == 0 or not self.pending:
            return
        self.pending = False
        self.last_emit = time.monotonic()
        self.emitted_in_phase = True
        elapsed = int(self.last_emit - self.started)
        line = (
            f"[consilium] event agent={self.agent_id} type={self.phase} "
            f"chunks={self.chunks} chars={self.chars} elapsed={elapsed}s\n"
        )
        sys.stderr.write(line)
        sys.stderr.flush()
        tape_record(
            "RENDERED",
            {
                "agent_id": self.agent_id,
                "progress_type": self.phase,
                "chunks": self.chunks,
                "chars": self.chars,
            },
        )

    def feed(self, typ: str, data: Any = None) -> None:
        if typ in self.LABEL:
            label = self.LABEL[typ]
            if label != self.phase:
                self._emit()
                self.phase = label
                self.chunks = 0
                self.chars = 0
                self.emitted_in_phase = False
            self.chunks += 1
            self.chars += len("" if data is None else str(data))
            self.pending = True
            if not self.emitted_in_phase or (time.monotonic() - self.last_emit) >= self.interval:
                self._emit()
            return
        self._emit()
        self.phase = ""
        progress_event(self.agent_id, typ, data)

    def flush(self) -> None:
        self._emit()


def parse_line(line: str) -> Dict[str, Any]:
    line = line.strip()
    if not line:
        return {}
    try:
        obj = json.loads(line)
    except json.JSONDecodeError:
        return {"_plain": line}
    if isinstance(obj, dict):
        return obj
    return {"_plain": line, "_value": obj}


def _normalize_grok_stop_reason(value: Any) -> str:
    return str(value or "").strip().replace("-", "_").lower()


# One-shot streaming-json `end.stopReason` values that are non-success even when
# the CLI process exits 0 and partial text exists. Real Grok headless emits
# stopReason on end (e.g. EndTurn / Error / MaxTokens); map those here so
# validation does not treat every end as success.
_GROK_FAIL_STOP = frozenset({"error", "rate_limit", "ratelimit", "cancelled", "canceled"})
_GROK_INCOMPLETE_STOP = frozenset({"max_tokens", "maxtokens"})
_GROK_SUCCESS_STOP = frozenset({"end_turn", "endturn", ""})


def normalize_grok(obj: Dict[str, Any]) -> tuple[str, Any]:
    typ = obj.get("type") or "unknown"
    if typ == "text":
        return "text", obj.get("data", "")
    if typ == "thought":
        return "thought", obj.get("data", "")
    if typ == "end":
        stop_raw = obj.get("stopReason")
        stop = _normalize_grok_stop_reason(stop_raw)
        # Non-success stopReasons fail closed even without a separate error event.
        if stop in _GROK_FAIL_STOP or stop in _GROK_INCOMPLETE_STOP:
            return "error", stop_raw or stop
        if stop in _GROK_SUCCESS_STOP:
            return "end", stop_raw or "end"
        # Unknown stopReason is non-success (matches steerable honesty).
        return "error", f"unknown_stop:{stop_raw or stop or 'missing'}"
    if typ == "error":
        return "error", obj.get("message") or obj.get("data") or json.dumps(obj)
    if typ in ("tool_start", "tool_use", "tool_call"):
        return "tool_started", (
            obj.get("toolName")
            or obj.get("name")
            or obj.get("kind")
            or "tool"
        )
    if typ == "tool_call_update":
        status = str(obj.get("status") or "in_progress")
        if status in {"completed", "complete", "done", "failed", "error"}:
            return "tool_completed", status
        return "progress", status
    if typ in ("tool_end", "tool_result"):
        return "tool_completed", obj.get("name") or obj.get("data") or typ
    if typ in ("available_commands", "usage"):
        return "progress", typ
    return typ, obj.get("data")


def _codex_item_text(item: Dict[str, Any]) -> str:
    """Extract agent message text from a codex exec --json item payload."""
    if not isinstance(item, dict):
        return ""
    typ = str(item.get("type") or item.get("item_type") or item.get("itemType") or "")
    # Tool items never contribute final text.
    if typ in (
        "command_execution",
        "commandExecution",
        "file_change",
        "fileChange",
        "mcp_tool_call",
        "mcpToolCall",
        "web_search",
        "webSearch",
        "tool",
        "function_call",
        "functionCall",
    ):
        return ""
    if typ in ("userMessage", "user_message"):
        return ""
    role = item.get("role")
    if role not in (None, "assistant"):
        return ""
    # Nested production shape: item.completed → item: {type: agent_message, text|content}
    if typ and typ not in (
        "agent_message",
        "agentMessage",
        "message",
        "agent_message_item",
        "",
    ):
        # Unknown item types: try text fields only when role is assistant-like.
        if role != "assistant" and "message" not in typ.lower():
            return ""
    text = item.get("text") or item.get("message")
    if isinstance(text, str) and text:
        return text
    content = item.get("content")
    if isinstance(content, str) and content:
        return content
    if isinstance(content, list):
        parts = []
        for c in content:
            if isinstance(c, dict):
                if c.get("text"):
                    parts.append(str(c["text"]))
                elif c.get("type") in ("output_text", "text") and c.get("text"):
                    parts.append(str(c["text"]))
            elif isinstance(c, str):
                parts.append(c)
        return "".join(parts)
    return ""


def normalize_codex(obj: Dict[str, Any]) -> tuple[str, Any]:
    """Map codex exec --json events, including nested item.completed shapes."""
    typ = obj.get("type") or ""
    msg = obj.get("msg") if isinstance(obj.get("msg"), dict) else None
    if not typ and msg:
        typ = msg.get("type") or ""
    body = msg if isinstance(msg, dict) else obj

    # Production nested shape: {"type":"item.completed","item":{...}}
    if typ in ("item.completed", "item_completed", "item/completed"):
        item = obj.get("item") or body.get("item") or body
        if isinstance(item, dict):
            item_typ = str(item.get("type") or item.get("itemType") or "")
            if item_typ in (
                "command_execution",
                "commandExecution",
                "file_change",
                "fileChange",
                "mcp_tool_call",
                "mcpToolCall",
                "web_search",
                "webSearch",
                "function_call",
                "functionCall",
                "tool",
            ):
                name = (
                    item.get("command")
                    or item.get("name")
                    or item.get("tool")
                    or item_typ
                )
                return "tool_completed", name
            text = _codex_item_text(item)
            if text:
                return "text", text
        return "progress", typ

    if typ in ("item.started", "item_started", "item/started"):
        item = obj.get("item") or body.get("item") or body
        if isinstance(item, dict):
            item_typ = str(item.get("type") or "")
            if "command" in item_typ.lower() or "tool" in item_typ.lower() or "mcp" in item_typ.lower():
                return "tool_started", item.get("name") or item.get("command") or item_typ
        return "progress", typ

    if typ in ("agent_message", "agentMessage", "message"):
        text = body.get("text") or body.get("message") or obj.get("text")
        if not text and isinstance(obj.get("item"), dict):
            text = _codex_item_text(obj["item"])
        if text:
            return "text", text
    if typ in ("agent_message_delta", "agentMessageDelta", "message.delta"):
        delta = body.get("delta") or body.get("text") or obj.get("delta") or ""
        if delta:
            return "text", delta
    if typ in ("error", "turn.failed", "turn_failed"):
        return "error", body.get("message") or obj.get("message") or json.dumps(obj)
    if typ in ("turn.completed", "turn_completed", "task_complete", "done", "thread.completed"):
        return "end", typ
    if typ in ("tool",) or (isinstance(typ, str) and typ.startswith("item.") and "tool" in typ.lower()):
        return "tool_started", typ
    # Unknown codex stream types: reject for normalized persistence.
    return "event", typ


def normalize_claude(obj: Dict[str, Any]) -> tuple[str, Any]:
    typ = obj.get("type") or "event"
    if typ == "content_block_delta":
        delta = obj.get("delta") or {}
        if delta.get("type") == "text_delta":
            return "text", delta.get("text", "")
        if delta.get("type") == "thinking_delta":
            return "thought", delta.get("thinking", "")
        # Other deltas (input_json_delta, etc.) are structural progress only.
        return "progress", delta.get("type") or typ
    if typ == "content_block_start":
        block = obj.get("content_block") or {}
        if block.get("type") == "tool_use":
            return "tool_started", block.get("name") or "tool"
        if block.get("type") in ("text", "thinking"):
            return "progress", block.get("type")
        return "progress", typ
    if typ == "content_block_stop":
        # Do NOT map every stop to tool_completed — only actual tool blocks
        # tracked via content_block_start. Without open-tool context this is
        # structural progress (text/thinking block ends).
        block = obj.get("content_block") or {}
        if isinstance(block, dict) and block.get("type") == "tool_use":
            return "tool_completed", block.get("name") or "tool"
        # Some streams only put index on stop; treat as progress.
        return "progress", "block_stop"
    if typ == "assistant" and isinstance(obj.get("message"), dict):
        parts = obj["message"].get("content") or []
        texts = []
        for p in parts:
            if isinstance(p, dict) and p.get("type") == "text":
                texts.append(p.get("text", ""))
        if texts:
            return "text", "".join(texts)
    if typ in ("result", "result_success"):
        is_error = bool(obj.get("is_error") or obj.get("error"))
        result = obj.get("result")
        if is_error:
            return "error", obj.get("error") or result or "result_error"
        if isinstance(result, str):
            # Empty/whitespace result still emits a result event; assembly
            # rules refuse to let it erase non-empty deltas.
            return "result", result
        return "end", typ
    if typ == "error":
        return "error", obj.get("error") or json.dumps(obj)
    return "event", typ


def _opencode_unwrap(obj: Dict[str, Any]) -> Dict[str, Any]:
    """Unwrap production payload / syncEvent envelopes (same as steerable)."""
    if (
        isinstance(obj.get("payload"), dict)
        and (obj.get("type") is None or obj.get("type") == "sync")
        and obj["payload"].get("type")
    ):
        obj = obj["payload"]
    if obj.get("type") == "sync" and isinstance(obj.get("syncEvent"), dict):
        se = obj["syncEvent"]
        se_type = str(se.get("type") or "")
        if se_type.endswith(".1") or se_type.endswith(".0"):
            se_type = se_type.rsplit(".", 1)[0]
        if se_type:
            data = se.get("data") if isinstance(se.get("data"), dict) else {}
            obj = {"type": se_type, "properties": data if data else se}
    return obj


def normalize_opencode(obj: Dict[str, Any]) -> tuple[str, Any]:
    """One-shot OpenCode JSONL.

    message.part.updated is a cumulative snapshot per part id (not append-delta).
    The live extract-text path in main() applies part-id last-write-wins; this
    mapper still returns the full snapshot text so progress/normalized events
    remain observable. Callers must not concatenate successive snapshots.
    """
    obj = _opencode_unwrap(obj)
    typ = obj.get("type") or obj.get("event") or "event"
    props = obj.get("properties") if isinstance(obj.get("properties"), dict) else None
    part = None
    if props and isinstance(props.get("part"), dict):
        part = props["part"]
    elif isinstance(obj.get("part"), dict):
        part = obj["part"]
    else:
        part = obj

    if typ in ("text", "message.part.delta"):
        text = ""
        if props and isinstance(props.get("delta"), str):
            text = props["delta"]
        if not text and isinstance(part, dict):
            # Genuine deltas only — do not treat full snapshot text on delta events
            # as incremental when a delta field is present elsewhere.
            if isinstance(part.get("delta"), str):
                text = part["delta"]
            elif not (props and isinstance(props.get("delta"), str)):
                text = part.get("text") or ""
        if not text:
            text = obj.get("text") or obj.get("delta") or ""
        if text:
            return "text", text
    if typ == "message.part.updated":
        # Cumulative snapshot — return full text; main() last-write-wins for
        # extract-text. Backend post-pass also reassembles from raw.
        text = ""
        if isinstance(part, dict) and isinstance(part.get("text"), str):
            text = part["text"]
        if text:
            return "text", text
    if typ == "session.idle":
        # Idle is a turn-liveness signal, not proof that the one-shot process
        # has emitted all answer bytes or completed its lifecycle.
        return "progress", typ
    if typ in ("session.complete", "session.completed", "done"):
        return "end", typ
    if typ == "error" or obj.get("error"):
        return "error", obj.get("error") or json.dumps(obj)
    return "event", typ


def normalize_gemini(obj: Dict[str, Any]) -> tuple[str, Any]:
    """Gemini CLI typically emits plain text; JSON objects map when present."""
    if "_plain" in obj:
        return "text", obj["_plain"]
    typ = obj.get("type") or ""
    if typ in ("text", "response", "content"):
        return "text", obj.get("data") or obj.get("text") or obj.get("content") or ""
    if typ in ("end", "done", "complete"):
        return "end", typ
    if typ == "error":
        return "error", obj.get("message") or obj.get("error") or json.dumps(obj)
    text = obj.get("text") or obj.get("response") or obj.get("data")
    if isinstance(text, str) and text:
        return "text", text
    return "event", typ


def stream_to_progress_type(stream_type: str) -> str:
    """Map backend stream names to progress vocabulary (thought/text/end/error)."""
    if stream_type in ("text", "thought", "end", "error", "result"):
        if stream_type == "result":
            return "end"
        return stream_type
    mapped = map_stream_type(stream_type)
    if mapped == "thinking_delta":
        return "thought"
    if mapped == "answer_delta":
        return "text"
    if mapped == "run_completed":
        return "end"
    if mapped == "run_failed":
        return "error"
    if mapped == "result":
        return "end"
    return stream_type


def main() -> int:
    ap = argparse.ArgumentParser(description="Normalize backend streams to consilium JSONL")
    ap.add_argument("--backend", required=True, choices=[
        "codex-cli", "claude-code", "opencode", "gemini-cli", "grok-build", "plain"
    ])
    ap.add_argument("--agent-id", required=True)
    ap.add_argument("--model", default="")
    ap.add_argument("--effort", default="")
    ap.add_argument("--access-policy", default="")
    ap.add_argument("--input", default="-")
    ap.add_argument("--raw-out", default="",
                    help="Append each raw input line immediately (for concurrent capture)")
    ap.add_argument("--progress", action="store_true",
                    help="Emit compact semantic progress to stderr as events arrive")
    ap.add_argument("--progress-style", default="full", choices=["full", "compact", "none"],
                    help="full: preview text/thought content. "
                         "compact: counters only, never model content. "
                         "none: no progress at all.")
    ap.add_argument("--progress-id", default="",
                    help="Identity used in progress lines only (defaults to --agent-id).")
    ap.add_argument("--progress-interval", type=float, default=10.0,
                    help="Seconds between compact-style heartbeat lines")
    ap.add_argument("--extract-text", action="store_true",
                    help="Also print concatenated text events to a side file via --text-out")
    ap.add_argument("--text-out", default="")
    ap.add_argument("--no-validate", action="store_true")
    ap.add_argument("--debug-events", nargs="?", const="__default__", default="",
                    help="Opt-in debug event tape path (or default when flag alone)")
    args = ap.parse_args()

    debug_path = ""
    if args.debug_events:
        debug_path = "" if args.debug_events == "__default__" else args.debug_events
        init_global_tape(debug_path)
    else:
        # Env fallback consistent with project (CONSILIUM_DEBUG_EVENTS=1)
        init_global_tape("")

    tape_record(
        "FINAL",
        {
            "event": "run_started",
            "backend": args.backend,
            "agent_id": args.agent_id,
            "model": args.model,
            "effort": args.effort,
            "access_policy": args.access_policy,
        },
    )

    inp: TextIO
    if args.input == "-":
        try:
            sys.stdin.reconfigure(line_buffering=True)  # type: ignore[attr-defined]
        except Exception:
            pass
        inp = sys.stdin
    else:
        inp = open(args.input, "r", encoding="utf-8", errors="replace")

    raw_out_f: Optional[TextIO] = None
    if args.raw_out:
        raw_out_f = open(args.raw_out, "a", encoding="utf-8", errors="replace")

    text_out_f: Optional[TextIO] = None
    if args.text_out:
        text_out_f = open(args.text_out, "w", encoding="utf-8")

    saw_end = False
    saw_error = False
    error_msg = ""
    final_result_text: Optional[str] = None  # non-empty authoritative only
    collected_for_final = []  # ConsiliumEvent-like for assembly
    rejected_count = 0
    rejected_types: Dict[str, int] = {}
    # OpenCode message.part.updated: part-id last-write-wins (not H+He+Hello).
    # Live extract-text path must use this always, not only when empty.
    oc_part_snaps: Dict[str, str] = {}
    oc_part_order: list = []
    oc_delta_parts: list = []
    # Cap how many distinct unknown types we name on the bounded stderr signal.
    REJECTED_SIGNAL_MAX = 8
    reporter: Any = None
    if args.progress and args.progress_style != "none":
        progress_id = args.progress_id or args.agent_id
        if args.progress_style == "compact":
            reporter = CompactProgressReporter(progress_id, args.progress_interval)
        else:
            reporter = ProgressReporter(progress_id)

    # Emit run_started into normalized stream
    started = make_event(
        stream_type="run_started",
        backend=args.backend,
        agent_id=args.agent_id,
        data="start",
        raw={
            "model": args.model,
            "effort": args.effort,
            "access_policy": args.access_policy,
        },
    )
    if started is not None:
        emit_event(sys.stdout, started)

    try:
        for line in inp:
            tape_record("RAW", {"backend": args.backend}, content_preview=line[:200])
            if raw_out_f is not None:
                raw_out_f.write(line if line.endswith("\n") else line + "\n")
                raw_out_f.flush()

            obj = parse_line(line)
            if not obj:
                continue

            tape_record(
                "PARSED",
                {
                    "keys": list(obj.keys())[:20] if isinstance(obj, dict) else [],
                    "plain": "_plain" in obj,
                },
            )

            raw: Any = None
            if "_plain" in obj and len(obj) <= 2:
                stream_typ, data = "text", obj["_plain"]
            else:
                raw = obj
                if args.backend == "grok-build":
                    stream_typ, data = normalize_grok(obj)
                elif args.backend == "codex-cli":
                    stream_typ, data = normalize_codex(obj)
                elif args.backend == "claude-code":
                    stream_typ, data = normalize_claude(obj)
                elif args.backend == "opencode":
                    stream_typ, data = normalize_opencode(obj)
                elif args.backend == "gemini-cli":
                    stream_typ, data = normalize_gemini(obj)
                else:
                    # plain backend: each line is answer text
                    if "_plain" in obj:
                        stream_typ, data = "text", obj["_plain"]
                    else:
                        stream_typ = obj.get("type") or "event"
                        data = obj.get("data") or obj.get("text") or obj.get("message")

            # Map stream name "event" (generic unknown) → reject, not persist.
            if stream_typ == "event":
                evt = None
            else:
                evt = make_event(
                    stream_type=stream_typ,
                    backend=args.backend,
                    agent_id=args.agent_id,
                    data=data,
                    raw=raw if isinstance(raw, dict) else None,
                )
            if evt is None:
                # Protocol drift: never persist unknown types (artifact fail-closed
                # for the record; process continues — see finalize signal).
                rejected_count += 1
                key = str(stream_typ or "unknown")[:80]
                rejected_types[key] = rejected_types.get(key, 0) + 1
                tape_record(
                    "PARSED",
                    {
                        "event": "rejected_unknown_type",
                        "stream_type": stream_typ,
                    },
                    content_preview=str(data)[:80] if data is not None else "",
                )
                continue

            emit_event(sys.stdout, evt)
            collected_for_final.append(evt)

            # OpenCode cumulative part snapshots: track part-id last-write-wins
            # for extract-text. Still emit answer_delta events for observability.
            if args.backend == "opencode" and isinstance(raw, dict):
                oc_obj = _opencode_unwrap(dict(raw))
                oc_typ = oc_obj.get("type") or oc_obj.get("event") or ""
                oc_props = (
                    oc_obj.get("properties")
                    if isinstance(oc_obj.get("properties"), dict)
                    else oc_obj
                )
                if not isinstance(oc_props, dict):
                    oc_props = {}
                oc_part = (
                    oc_props.get("part")
                    if isinstance(oc_props.get("part"), dict)
                    else (oc_obj.get("part") if isinstance(oc_obj.get("part"), dict) else None)
                )
                if oc_typ == "message.part.updated" and isinstance(oc_part, dict):
                    pid = str(
                        oc_part.get("id")
                        or oc_part.get("partID")
                        or oc_part.get("partId")
                        or "_default"
                    )
                    t = oc_part.get("text")
                    if isinstance(t, str) and t:
                        if pid not in oc_part_snaps and pid not in oc_part_order:
                            oc_part_order.append(pid)
                        oc_part_snaps[pid] = t
                elif oc_typ in ("message.part.delta", "text") and evt.type == "answer_delta":
                    if data is not None:
                        oc_delta_parts.append(str(data))

            # Progress uses legacy display vocabulary for BC.
            prog_typ = stream_to_progress_type(stream_typ)
            progress_types = {
                "text",
                "thought",
                "end",
                "error",
                "result",
                "tool_started",
                "tool_completed",
            }
            if isinstance(reporter, CompactProgressReporter):
                progress_types.add("progress")
            if reporter is not None and prog_typ in progress_types:
                if prog_typ == "result":
                    reporter.feed("end", "result")
                else:
                    reporter.feed(prog_typ, data)

            if evt.type == "answer_delta" and data is not None:
                # Stream deltas only until a non-empty authoritative result arrives.
                # OpenCode snapshots: rewrite text-out from last-write-wins parts
                # rather than appending H+He+Hello.
                if text_out_f is not None and final_result_text is None:
                    if args.backend == "opencode" and oc_part_snaps:
                        assembled_oc = "".join(
                            oc_part_snaps[k] for k in oc_part_order if k in oc_part_snaps
                        )
                        text_out_f.seek(0)
                        text_out_f.truncate()
                        text_out_f.write(assembled_oc)
                        text_out_f.flush()
                    else:
                        text_out_f.write(str(data))
                        text_out_f.flush()
            elif evt.type == "result":
                # Empty/whitespace authoritative result must NOT erase deltas.
                if data is not None and str(data).strip():
                    final_result_text = str(data)
                    if text_out_f is not None:
                        text_out_f.seek(0)
                        text_out_f.truncate()
                        text_out_f.write(final_result_text)
                        text_out_f.flush()
                saw_end = True
            elif evt.type == "run_completed":
                saw_end = True
            elif evt.type == "run_failed":
                saw_error = True
                error_msg = str(data or "")
    finally:
        if reporter is not None:
            reporter.flush()
        if args.input != "-":
            inp.close()
        if raw_out_f is not None:
            raw_out_f.close()
        if text_out_f is not None:
            text_out_f.close()

    # Re-assemble final text.
    if args.text_out:
        assembled = ""
        if args.backend == "opencode" and oc_part_snaps:
            # Always prefer part-id last-write-wins over concatenated deltas.
            assembled = "".join(
                oc_part_snaps[k] for k in oc_part_order if k in oc_part_snaps
            )
        elif args.backend == "opencode" and oc_delta_parts:
            assembled = "".join(oc_delta_parts)
        elif collected_for_final:
            assembled = assemble_final_text(collected_for_final)
        if assembled and (
            final_result_text is None or assembled != final_result_text
            or args.backend == "opencode"
        ):
            try:
                with open(args.text_out, "w", encoding="utf-8") as f:
                    f.write(assembled)
            except Exception:
                pass
        elif assembled and final_result_text is None:
            try:
                with open(args.text_out, "w", encoding="utf-8") as f:
                    f.write(assembled)
            except Exception:
                pass

    tape_record(
        "FINAL",
        {
            "event": "normalize_finished",
            "saw_end": saw_end,
            "saw_error": saw_error,
            "rejected_unknown": rejected_count,
        },
    )
    stats = close_global_tape()
    if stats and (stats.get("dropped") or stats.get("overflow") or stats.get("sequence_gaps")):
        # Honest report on stderr only when debug tape is active — still not
        # event content, only gap/overflow counters.
        sys.stderr.write(
            f"[consilium] debug-events "
            f"dropped={stats.get('dropped', 0)} "
            f"overflow={str(stats.get('overflow', False)).lower()} "
            f"gaps={stats.get('sequence_gaps', 0)} "
            f"path={stats.get('path', '')}\n"
        )
        sys.stderr.flush()

    # Visible bounded protocol-drift signal (no event bodies). Artifact path is
    # fail-closed (unknown types never written); process is not fail-closed so
    # backends that emit mixed progressive types still complete when known
    # events are enough for a final answer.
    if rejected_count > 0:
        names = sorted(rejected_types.keys(), key=lambda k: (-rejected_types[k], k))
        shown = names[:REJECTED_SIGNAL_MAX]
        extra = len(names) - len(shown)
        summary = ",".join(f"{n}×{rejected_types[n]}" for n in shown)
        if extra > 0:
            summary += f",+{extra}_more"
        sys.stderr.write(
            f"[consilium] protocol-drift rejected_unknown={rejected_count} "
            f"types={summary}\n"
        )
        sys.stderr.flush()

    if args.backend == "grok-build" and not args.no_validate:
        if saw_error:
            print(f"grok stream error: {error_msg}", file=sys.stderr)
            return 1
        if not saw_end:
            print("grok stream missing end event", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
