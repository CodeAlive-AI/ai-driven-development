#!/usr/bin/env python3
"""Normalize backend CLI streams into consilium event JSONL.

Reads newline-delimited JSON (or plain text) from stdin or a file.
Writes normalized events to stdout (one JSON object per line).

When used mid-flight (stdin from a live backend pipe):
  - each raw line is persisted immediately via --raw-out (flushed)
  - each event is normalized and emitted immediately (flushed)
  - with --progress, compact semantic progress is written to stderr immediately

Normalized event schema (stable):
  {"ts": ISO8601, "backend": str, "agent_id": str, "type": str, "data": str|null, "raw": object|null}

Supported backends:
  - grok-build streaming-json: types thought|text|end|error|*
  - codex --json: passthrough map of known types
  - claude stream-json: content_block_delta etc.
  - opencode --format json: message/part events
  - plain: each line becomes type=text

Exit codes:
  0 — success (for grok: requires end event, no error event, unless --no-validate)
  1 — grok validation failure (error event or missing end)
  2 — usage
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from typing import Any, Dict, Optional, TextIO


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def emit(out: TextIO, backend: str, agent_id: str, typ: str, data: Any = None, raw: Any = None) -> None:
    evt = {
        "ts": utc_now(),
        "backend": backend,
        "agent_id": agent_id,
        "type": typ,
        "data": data,
        "raw": raw,
    }
    out.write(json.dumps(evt, ensure_ascii=False) + "\n")
    out.flush()


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

        # The first line appears quickly enough to prove liveness; later lines
        # are larger so token-by-token streams remain compact and readable.
        threshold = 12 if not self.emitted else 72
        sentence_boundary = (
            len(self.buffer) >= 24
            and self.buffer.rstrip().endswith((".", "!", "?", ":"))
        )
        if "\n" in chunk or len(self.buffer) >= threshold or sentence_boundary:
            self.flush()


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


def normalize_grok(obj: Dict[str, Any]) -> tuple[str, Any]:
    typ = obj.get("type") or "unknown"
    if typ == "text":
        return "text", obj.get("data", "")
    if typ == "thought":
        return "thought", obj.get("data", "")
    if typ == "end":
        return "end", obj.get("stopReason") or "end"
    if typ == "error":
        return "error", obj.get("message") or obj.get("data") or json.dumps(obj)
    return typ, obj.get("data")


def normalize_codex(obj: Dict[str, Any]) -> tuple[str, Any]:
    typ = obj.get("type") or obj.get("msg", {}).get("type") or "event"
    # Common shapes: item.completed, agent_message, etc.
    msg = obj.get("msg") if isinstance(obj.get("msg"), dict) else obj
    if typ in ("agent_message", "item.completed", "message"):
        text = msg.get("text") or msg.get("message") or obj.get("text")
        if text:
            return "text", text
    if typ in ("error", "turn.failed"):
        return "error", msg.get("message") or json.dumps(obj)
    if typ in ("turn.completed", "task_complete", "done"):
        return "end", typ
    return "event", typ


def normalize_claude(obj: Dict[str, Any]) -> tuple[str, Any]:
    typ = obj.get("type") or "event"
    if typ == "content_block_delta":
        delta = obj.get("delta") or {}
        if delta.get("type") == "text_delta":
            return "text", delta.get("text", "")
        if delta.get("type") == "thinking_delta":
            return "thought", delta.get("thinking", "")
    if typ == "assistant" and isinstance(obj.get("message"), dict):
        parts = obj["message"].get("content") or []
        texts = []
        for p in parts:
            if isinstance(p, dict) and p.get("type") == "text":
                texts.append(p.get("text", ""))
        if texts:
            return "text", "".join(texts)
    if typ in ("result", "result_success"):
        # Final result carries the complete answer. Emit as type=result (not
        # text) so extract-text can prefer it over streamed deltas without
        # concatenating both into a duplicated final answer. Live progress
        # still comes from content_block_delta text events.
        result = obj.get("result")
        if isinstance(result, str):
            return "result", result
        return "end", typ
    if typ == "error":
        return "error", obj.get("error") or json.dumps(obj)
    return "event", typ


def normalize_opencode(obj: Dict[str, Any]) -> tuple[str, Any]:
    typ = obj.get("type") or "event"
    if typ in ("text", "message.part.updated", "message.part.delta"):
        part = obj.get("part") or obj
        text = part.get("text") or obj.get("text") or obj.get("delta")
        if text:
            return "text", text
    if typ in ("session.idle", "session.complete", "done"):
        return "end", typ
    if typ == "error" or obj.get("error"):
        return "error", obj.get("error") or json.dumps(obj)
    return "event", typ


def main() -> int:
    ap = argparse.ArgumentParser(description="Normalize backend streams to consilium JSONL")
    ap.add_argument("--backend", required=True, choices=[
        "codex-cli", "claude-code", "opencode", "gemini-cli", "grok-build", "plain"
    ])
    ap.add_argument("--agent-id", required=True)
    ap.add_argument("--input", default="-")
    ap.add_argument("--raw-out", default="",
                    help="Append each raw input line immediately (for concurrent capture)")
    ap.add_argument("--progress", action="store_true",
                    help="Emit compact semantic progress to stderr as events arrive")
    ap.add_argument("--extract-text", action="store_true",
                    help="Also print concatenated text events to a side file via --text-out")
    ap.add_argument("--text-out", default="")
    ap.add_argument("--no-validate", action="store_true")
    args = ap.parse_args()

    inp: TextIO
    if args.input == "-":
        # Line-buffered when possible so mid-flight pipes advance promptly
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
        # Stream final text to disk as it arrives. This avoids buffering an
        # arbitrarily long model response in the normalizer's memory.
        text_out_f = open(args.text_out, "w", encoding="utf-8")

    saw_end = False
    saw_error = False
    error_msg = ""
    # Claude (and similar) may stream text deltas then emit a final `result`
    # with the complete answer. Prefer result for --extract-text so the answer
    # appears exactly once, while still streaming deltas until result arrives.
    final_result_text: Optional[str] = None
    reporter = ProgressReporter(args.agent_id) if args.progress else None

    try:
        for line in inp:
            if raw_out_f is not None:
                raw_out_f.write(line if line.endswith("\n") else line + "\n")
                raw_out_f.flush()

            obj = parse_line(line)
            if not obj:
                continue

            if "_plain" in obj and len(obj) <= 2:
                typ, data = "text", obj["_plain"]
                raw: Any = None
            else:
                raw = obj
                if args.backend == "grok-build":
                    typ, data = normalize_grok(obj)
                elif args.backend == "codex-cli":
                    typ, data = normalize_codex(obj)
                elif args.backend == "claude-code":
                    typ, data = normalize_claude(obj)
                elif args.backend == "opencode":
                    typ, data = normalize_opencode(obj)
                else:
                    # gemini / plain: treat as text lines or pass-through
                    if "_plain" in obj:
                        typ, data = "text", obj["_plain"]
                    else:
                        typ = obj.get("type") or "event"
                        data = obj.get("data") or obj.get("text") or obj.get("message")

            emit(sys.stdout, args.backend, args.agent_id, typ, data, raw if isinstance(raw, dict) else None)

            if reporter is not None and typ in ("text", "thought", "end", "error", "result"):
                # Progress for result is a short notice, not the full answer body
                if typ == "result":
                    reporter.feed("end", "result")
                else:
                    reporter.feed(typ, data)

            if typ == "text" and data is not None:
                # Stream deltas only until a definitive result overrides them.
                if text_out_f is not None and final_result_text is None:
                    text_out_f.write(str(data))
                    text_out_f.flush()
            elif typ == "result":
                # Authoritative final answer: replace any streamed deltas.
                if data is not None:
                    final_result_text = str(data)
                    if text_out_f is not None:
                        text_out_f.seek(0)
                        text_out_f.truncate()
                        text_out_f.write(final_result_text)
                        text_out_f.flush()
                saw_end = True
            elif typ == "end":
                saw_end = True
            elif typ == "error":
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
