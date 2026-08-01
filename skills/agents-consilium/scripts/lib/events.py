#!/usr/bin/env python3
"""Closed ConsiliumEvent schema for one-shot and steerable paths.

Normalized artifacts must only persist event types from KNOWN_EVENT_TYPES.
Unknown types are rejected (protocol drift), not silently written.
Backend-specific raw payloads remain on the optional ``raw`` field.

Progress rendering may still use display aliases (thought/text/end/error);
those aliases are mapped here and never invent new persisted types.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


# Closed set of normalized event types. Extend deliberately; tests assert drift.
KNOWN_EVENT_TYPES = frozenset(
    {
        "run_started",
        "thinking_delta",
        "answer_delta",
        "tool_started",
        "tool_completed",
        "retry_scheduled",
        # Steer lifecycle (honest protocol states; not semantic compliance).
        "steer_accepted",
        "steer_delivering",
        "steer_request_sent",
        "steer_queued",
        "steer_awaiting_queue_resolution",
        "steer_merged",
        "steer_running",
        "steer_completed",
        "steer_incomplete",
        "steer_applied",
        "steer_cancelled",
        "steer_superseded",
        "steer_dropped",
        "steer_abandoned",
        "steer_failed",
        "steer_rejected",
        "run_completed",
        "run_failed",
        # Structural / observability helpers that are still first-class.
        "result",  # authoritative complete answer (Claude); not concatenated with deltas
        "progress",  # non-content structural progress
        "user_replay",
        "turn_started",
        "turn_completed",
        "prompt_complete",
    }
)

# Backend / adapter stream names → closed ConsiliumEvent types.
STREAM_TO_EVENT: Dict[str, str] = {
    "text": "answer_delta",
    "thought": "thinking_delta",
    "thinking": "thinking_delta",
    "end": "run_completed",
    "done": "run_completed",
    "error": "run_failed",
    "result": "result",
    "result_success": "result",
    "tool": "tool_started",
    "tool_start": "tool_started",
    "tool_started": "tool_started",
    "tool_end": "tool_completed",
    "tool_complete": "tool_completed",
    "tool_completed": "tool_completed",
    "retry": "retry_scheduled",
    "retry_scheduled": "retry_scheduled",
    "run_started": "run_started",
    "run_completed": "run_completed",
    "run_failed": "run_failed",
    "progress": "progress",
    "user_replay": "user_replay",
    "turn_started": "turn_started",
    "turn_completed": "turn_completed",
    "prompt_complete": "prompt_complete",
    "steer_ack": "steer_request_sent",  # default; refine via status when present
}

# Progress display aliases (stderr). Keep existing full/compact vocabulary.
EVENT_TO_PROGRESS_TYPE: Dict[str, str] = {
    "thinking_delta": "thought",
    "answer_delta": "text",
    "run_completed": "end",
    "run_failed": "error",
    "result": "end",
    "progress": "progress",
}

# Final-text assembly: which types contribute answer body.
TEXT_DELTA_TYPES = frozenset({"answer_delta"})
AUTHORITATIVE_RESULT_TYPES = frozenset({"result"})
TERMINAL_TYPES = frozenset({"run_completed", "run_failed", "result"})


class EventValidationError(ValueError):
    """Raised when a normalized event fails the closed-schema check."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def map_stream_type(stream_type: str, *, steer_status: str = "") -> Optional[str]:
    """Map a backend/adapter stream name to a closed ConsiliumEvent type.

    Returns None for unknown names (callers must not persist them).
    """
    if not stream_type:
        return None
    if stream_type in KNOWN_EVENT_TYPES:
        # Already a closed type (including steer_*).
        if stream_type.startswith("steer_") or stream_type in KNOWN_EVENT_TYPES:
            return stream_type
    if stream_type == "steer_ack" and steer_status:
        candidate = f"steer_{steer_status}"
        if candidate in KNOWN_EVENT_TYPES:
            return candidate
        return "steer_request_sent"
    return STREAM_TO_EVENT.get(stream_type)


def is_known_event_type(typ: str) -> bool:
    return typ in KNOWN_EVENT_TYPES


@dataclass
class ConsiliumEvent:
    """Validated internal event shared by one-shot normalization and steerable adapters."""

    type: str
    ts: str = ""
    backend: str = ""
    agent_id: str = ""
    data: Any = None
    raw: Any = None
    # Optional structured fields for tool / steer / retry.
    tool_name: str = ""
    tool_id: str = ""
    steer_client_id: str = ""
    steer_status: str = ""
    delivery_class: str = ""
    seq: Optional[int] = None
    meta: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.ts:
            self.ts = utc_now()
        if self.type not in KNOWN_EVENT_TYPES:
            raise EventValidationError(
                f"unknown ConsiliumEvent type {self.type!r}; "
                f"refusing to construct (protocol drift)"
            )

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {
            "ts": self.ts,
            "backend": self.backend,
            "agent_id": self.agent_id,
            "type": self.type,
            "data": self.data,
            "raw": self.raw,
        }
        if self.tool_name:
            d["tool_name"] = self.tool_name
        if self.tool_id:
            d["tool_id"] = self.tool_id
        if self.steer_client_id:
            d["steer_client_id"] = self.steer_client_id
        if self.steer_status:
            d["steer_status"] = self.steer_status
        if self.delivery_class:
            d["delivery_class"] = self.delivery_class
        if self.seq is not None:
            d["seq"] = self.seq
        if self.meta:
            d["meta"] = self.meta
        return d

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> "ConsiliumEvent":
        typ = obj.get("type")
        if not isinstance(typ, str) or typ not in KNOWN_EVENT_TYPES:
            raise EventValidationError(
                f"unknown or missing event type in artifact: {typ!r}"
            )
        known = {
            "type",
            "ts",
            "backend",
            "agent_id",
            "data",
            "raw",
            "tool_name",
            "tool_id",
            "steer_client_id",
            "steer_status",
            "delivery_class",
            "seq",
            "meta",
        }
        meta = dict(obj.get("meta") or {})
        for k, v in obj.items():
            if k not in known:
                meta.setdefault(k, v)
        return cls(
            type=typ,
            ts=str(obj.get("ts") or ""),
            backend=str(obj.get("backend") or ""),
            agent_id=str(obj.get("agent_id") or ""),
            data=obj.get("data"),
            raw=obj.get("raw"),
            tool_name=str(obj.get("tool_name") or ""),
            tool_id=str(obj.get("tool_id") or ""),
            steer_client_id=str(obj.get("steer_client_id") or ""),
            steer_status=str(obj.get("steer_status") or ""),
            delivery_class=str(obj.get("delivery_class") or ""),
            seq=obj.get("seq") if isinstance(obj.get("seq"), int) else None,
            meta=meta,
        )

    def progress_type(self) -> str:
        return EVENT_TO_PROGRESS_TYPE.get(self.type, self.type)


def make_event(
    *,
    stream_type: str,
    backend: str = "",
    agent_id: str = "",
    data: Any = None,
    raw: Any = None,
    steer_status: str = "",
    **kwargs: Any,
) -> Optional[ConsiliumEvent]:
    """Build a ConsiliumEvent from a backend stream name, or None if unknown."""
    typ = map_stream_type(stream_type, steer_status=steer_status)
    if typ is None:
        return None
    if steer_status and typ.startswith("steer_"):
        kwargs.setdefault("steer_status", steer_status)
    try:
        return ConsiliumEvent(
            type=typ,
            backend=backend,
            agent_id=agent_id,
            data=data,
            raw=raw,
            **kwargs,
        )
    except EventValidationError:
        return None


def validate_normalized_record(obj: Dict[str, Any]) -> ConsiliumEvent:
    """Validate a JSON object before writing to normalized artifacts."""
    return ConsiliumEvent.from_dict(obj)


def filter_persistable(
    events: Iterable[Dict[str, Any]],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Split records into (valid, rejected) for protocol-drift handling."""
    ok: List[Dict[str, Any]] = []
    rejected: List[Dict[str, Any]] = []
    for obj in events:
        if not isinstance(obj, dict):
            rejected.append({"error": "not_a_dict", "raw": obj})
            continue
        try:
            evt = validate_normalized_record(obj)
            ok.append(evt.to_dict())
        except EventValidationError as e:
            rejected.append({"error": str(e), "raw": obj})
    return ok, rejected


def _nonempty_text(data: Any) -> Optional[str]:
    """Return str(data) when it has non-whitespace content; else None."""
    if data is None:
        return None
    s = str(data)
    if not s.strip():
        return None
    return s


def assemble_final_text(events: Sequence[ConsiliumEvent | Dict[str, Any]]) -> str:
    """Assemble final answer text using backend-agnostic completeness rules.

    Preference order:
      1. Last non-empty authoritative ``result`` (complete answer, e.g. Claude).
      2. Concatenation of ``answer_delta`` chunks.
    Empty/whitespace-only authoritative results must not erase non-empty deltas.
    Thinking, tools, steer, and progress never contribute.
    """
    deltas: List[str] = []
    result_text: Optional[str] = None
    for item in events:
        if isinstance(item, ConsiliumEvent):
            typ = item.type
            data = item.data
        else:
            typ = item.get("type")
            data = item.get("data")
        if typ in AUTHORITATIVE_RESULT_TYPES:
            # Only non-empty/non-whitespace results become authoritative.
            candidate = _nonempty_text(data)
            if candidate is not None:
                result_text = candidate
        elif typ in TEXT_DELTA_TYPES and data is not None:
            # Always collect deltas; result wins only when non-empty above.
            if result_text is None:
                deltas.append(str(data))
    if result_text is not None:
        return result_text
    return "".join(deltas)


def adapter_kind_to_event(
    kind: str,
    *,
    backend: str = "",
    agent_id: str = "",
    data: str = "",
    raw: Any = None,
) -> Optional[ConsiliumEvent]:
    """Map steerable AdapterEvent.kind into a ConsiliumEvent."""
    steer_status = ""
    if isinstance(raw, dict):
        steer_status = str(raw.get("status") or raw.get("mailbox_status") or "")
    return make_event(
        stream_type=kind,
        backend=backend,
        agent_id=agent_id,
        data=data,
        raw=raw if isinstance(raw, dict) else None,
        steer_status=steer_status,
    )


# CLI for shell tests / offline checks
def _main() -> int:
    import argparse
    import sys

    ap = argparse.ArgumentParser(description="ConsiliumEvent validation helpers")
    ap.add_argument(
        "command",
        choices=["validate-line", "known-types", "map", "assemble"],
        help="validate-line: read JSONL stdin, print only valid events; "
        "known-types: list closed types; map: map stream name; "
        "assemble: assemble final text from JSONL stdin",
    )
    ap.add_argument("arg", nargs="?", default="")
    args = ap.parse_args()

    if args.command == "known-types":
        for t in sorted(KNOWN_EVENT_TYPES):
            print(t)
        return 0
    if args.command == "map":
        mapped = map_stream_type(args.arg)
        if mapped is None:
            print("UNKNOWN", file=sys.stderr)
            return 1
        print(mapped)
        return 0
    if args.command == "validate-line":
        rejected = 0
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                evt = validate_normalized_record(obj)
                print(evt.to_json())
            except Exception as e:
                rejected += 1
                print(f"REJECT: {e}", file=sys.stderr)
        return 1 if rejected else 0
    if args.command == "assemble":
        events = []
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                events.append(validate_normalized_record(json.loads(line)))
            except EventValidationError:
                continue
        sys.stdout.write(assemble_final_text(events))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(_main())
