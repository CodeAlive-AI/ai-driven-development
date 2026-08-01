#!/usr/bin/env python3
"""Bounded debug event tape for Consilium observability.

Opt-in only (disabled by default). Records a sequence-numbered JSONL tape
across pipeline stages:

  RAW → PARSED → NORMALIZED → RENDERED → FINAL

Does not write event content to normal stderr progress. Storage is bounded
and configurable for long runs; overflow is reported honestly.

Activation:
  --debug-events [PATH]          (CLI; path optional)
  CONSILIUM_DEBUG_EVENTS=1       (enable, default path under run dir / tmp)
  CONSILIUM_DEBUG_EVENTS_PATH=   (explicit path)
  CONSILIUM_DEBUG_EVENTS_MAX=    (max records; default 10000)
  CONSILIUM_DEBUG_EVENTS_MAX_BYTES= (max file bytes; default 32 MiB)

Coverage (implementation truth):
  - one-shot: normalize_stream.py records RAW/PARSED/NORMALIZED/RENDERED/FINAL
  - steerable: supervisor records NORMALIZED adapter events + FINAL; adapters
    may record RAW when the tape is active
  - shell workflow stages may record RENDERED progress lines when enabled
"""
from __future__ import annotations

import json
import os
import threading
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


STAGES = frozenset({"RAW", "PARSED", "NORMALIZED", "RENDERED", "FINAL"})

DEFAULT_MAX_RECORDS = 10_000
DEFAULT_MAX_BYTES = 32 * 1024 * 1024


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def env_enabled() -> bool:
    v = os.environ.get("CONSILIUM_DEBUG_EVENTS", "").strip().lower()
    return v in ("1", "true", "yes", "on")


def default_path() -> str:
    explicit = os.environ.get("CONSILIUM_DEBUG_EVENTS_PATH", "").strip()
    if explicit:
        return explicit
    run_dir = os.environ.get("CONSILIUM_RUN_DIR", "").strip()
    if run_dir:
        return str(Path(run_dir) / "debug-events.jsonl")
    return str(
        Path(os.environ.get("TMPDIR", "/tmp"))
        / f"consilium-debug-events-{os.getpid()}.jsonl"
    )


def max_records() -> int:
    raw = os.environ.get("CONSILIUM_DEBUG_EVENTS_MAX", "").strip()
    if not raw:
        return DEFAULT_MAX_RECORDS
    try:
        n = int(raw)
        return max(1, n)
    except ValueError:
        return DEFAULT_MAX_RECORDS


def max_bytes() -> int:
    raw = os.environ.get("CONSILIUM_DEBUG_EVENTS_MAX_BYTES", "").strip()
    if not raw:
        return DEFAULT_MAX_BYTES
    try:
        n = int(raw)
        return max(1024, n)
    except ValueError:
        return DEFAULT_MAX_BYTES


@dataclass
class DebugTape:
    path: str
    max_records: int = DEFAULT_MAX_RECORDS
    max_bytes: int = DEFAULT_MAX_BYTES
    _seq: int = 0
    _count: int = 0
    _bytes: int = 0
    _dropped: int = 0
    _overflow: bool = False
    _gaps: int = 0
    _last_seq_written: int = 0
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)
    _fh: Any = field(default=None, repr=False)
    enabled: bool = True

    @classmethod
    def from_env(cls, path: str = "") -> Optional["DebugTape"]:
        if not path and not env_enabled():
            return None
        p = path or default_path()
        tape = cls(path=p, max_records=max_records(), max_bytes=max_bytes())
        tape.open()
        return tape

    def open(self) -> None:
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        # Append mode so parent/child can share a path carefully; each process
        # still owns its sequence space and reports gaps honestly.
        self._fh = open(self.path, "a", encoding="utf-8")
        # Marker record so consumers know a session started.
        self.record(
            "FINAL",
            {
                "event": "debug_tape_opened",
                "max_records": self.max_records,
                "max_bytes": self.max_bytes,
                "pid": os.getpid(),
            },
            content_preview="",
        )

    def close(self) -> None:
        with self._lock:
            if self._fh is not None:
                summary = {
                    "event": "debug_tape_closed",
                    "records_written": self._count,
                    "dropped": self._dropped,
                    "overflow": self._overflow,
                    "sequence_gaps": self._gaps,
                    "last_seq": self._last_seq_written,
                }
                try:
                    self._write_unlocked(
                        "FINAL", summary, content_preview="", force=True
                    )
                except Exception:
                    pass
                try:
                    self._fh.close()
                except Exception:
                    pass
                self._fh = None

    def next_seq(self) -> int:
        with self._lock:
            self._seq += 1
            return self._seq

    def record(
        self,
        stage: str,
        payload: Dict[str, Any],
        *,
        content_preview: str = "",
        seq: Optional[int] = None,
        force: bool = False,
    ) -> Optional[int]:
        if not self.enabled:
            return None
        stage = stage.upper()
        if stage not in STAGES:
            stage = "PARSED"
        with self._lock:
            return self._write_unlocked(
                stage, payload, content_preview=content_preview, seq=seq, force=force
            )

    def _write_unlocked(
        self,
        stage: str,
        payload: Dict[str, Any],
        *,
        content_preview: str = "",
        seq: Optional[int] = None,
        force: bool = False,
    ) -> Optional[int]:
        if self._fh is None:
            return None
        if not force and (self._overflow or self._count >= self.max_records):
            self._dropped += 1
            self._overflow = True
            return None
        if seq is None:
            self._seq += 1
            seq = self._seq
        else:
            self._seq = max(self._seq, seq)

        if self._last_seq_written and seq > self._last_seq_written + 1:
            self._gaps += seq - self._last_seq_written - 1

        rec = {
            "seq": seq,
            "ts": utc_now(),
            "stage": stage,
            "payload": payload,
        }
        # Bounded preview only — full bodies stay in raw/normalized artifacts.
        if content_preview:
            preview = content_preview.replace("\n", " ")
            if len(preview) > 160:
                preview = preview[:157] + "..."
            rec["content_preview"] = preview

        line = json.dumps(rec, ensure_ascii=False) + "\n"
        encoded = line.encode("utf-8")
        if not force and (self._bytes + len(encoded)) > self.max_bytes:
            self._dropped += 1
            self._overflow = True
            # One honest overflow marker (force) if possible.
            if self._count < self.max_records:
                marker = {
                    "seq": seq,
                    "ts": utc_now(),
                    "stage": "FINAL",
                    "payload": {
                        "event": "debug_tape_overflow",
                        "dropped": self._dropped,
                        "max_bytes": self.max_bytes,
                        "max_records": self.max_records,
                    },
                }
                mline = json.dumps(marker, ensure_ascii=False) + "\n"
                try:
                    self._fh.write(mline)
                    self._fh.flush()
                    self._bytes += len(mline.encode("utf-8"))
                    self._count += 1
                    self._last_seq_written = seq
                except Exception:
                    pass
            return None

        try:
            self._fh.write(line)
            self._fh.flush()
        except Exception:
            self._dropped += 1
            return None

        self._bytes += len(encoded)
        self._count += 1
        self._last_seq_written = seq
        return seq

    def stats(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "records_written": self._count,
            "dropped": self._dropped,
            "overflow": self._overflow,
            "sequence_gaps": self._gaps,
            "last_seq": self._last_seq_written,
            "max_records": self.max_records,
            "max_bytes": self.max_bytes,
        }

    def report_gaps(self) -> Dict[str, Any]:
        """Return an honest gap/overflow report for callers/tests."""
        s = self.stats()
        s["ok"] = s["dropped"] == 0 and s["sequence_gaps"] == 0 and not s["overflow"]
        return s


# Process-wide optional tape (set by normalize_stream / supervisor).
_GLOBAL: Optional[DebugTape] = None
_GLOBAL_LOCK = threading.Lock()


def get_global_tape() -> Optional[DebugTape]:
    return _GLOBAL


def init_global_tape(path: str = "") -> Optional[DebugTape]:
    global _GLOBAL
    with _GLOBAL_LOCK:
        if _GLOBAL is not None:
            return _GLOBAL
        _GLOBAL = DebugTape.from_env(path)
        return _GLOBAL


def close_global_tape() -> Optional[Dict[str, Any]]:
    global _GLOBAL
    with _GLOBAL_LOCK:
        if _GLOBAL is None:
            return None
        stats = _GLOBAL.report_gaps()
        _GLOBAL.close()
        _GLOBAL = None
        return stats


def tape_record(
    stage: str,
    payload: Dict[str, Any],
    *,
    content_preview: str = "",
) -> None:
    t = _GLOBAL
    if t is not None:
        t.record(stage, payload, content_preview=content_preview)


def _main() -> int:
    import argparse
    import sys

    ap = argparse.ArgumentParser(description="Consilium debug event tape")
    ap.add_argument("--path", default="")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("stage", nargs="?", default="")
    ap.add_argument("payload_json", nargs="?", default="{}")
    args = ap.parse_args()

    if args.stats:
        path = args.path or default_path()
        if not Path(path).is_file():
            print(json.dumps({"error": "no tape", "path": path}))
            return 1
        seqs = []
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    seqs.append(json.loads(line).get("seq"))
                except Exception:
                    pass
        gaps = 0
        prev = None
        for s in seqs:
            if isinstance(s, int) and prev is not None and s > prev + 1:
                gaps += s - prev - 1
            if isinstance(s, int):
                prev = s
        print(
            json.dumps(
                {
                    "path": path,
                    "records": len(seqs),
                    "sequence_gaps": gaps,
                    "last_seq": prev,
                }
            )
        )
        return 0

    tape = DebugTape.from_env(args.path)
    if tape is None:
        print("debug tape disabled", file=sys.stderr)
        return 1
    if args.stage:
        try:
            payload = json.loads(args.payload_json)
        except json.JSONDecodeError:
            payload = {"data": args.payload_json}
        tape.record(args.stage, payload)
    print(json.dumps(tape.report_gaps()))
    tape.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
