"""Client-side steer / status / cancel / wait / watch / list against the mailbox."""
from __future__ import annotations

import argparse
import json
import os
import signal
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional

from .mailbox import Mailbox, MailboxError
from .registry import Registry, RegistryError, TERMINAL_STATUSES
from .util import preview_text, progress, utc_now_iso
from .waiter import (
    EXIT_NO_FINAL_TEXT,
    EXIT_WAIT_TIMEOUT,
    WaitTimeout,
    derive_exit_code,
    poll_once,
    read_final_text,
    wait_for_terminal,
)


def cmd_steer(args: argparse.Namespace) -> int:
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    content = args.guidance or ""
    if args.prompt_file:
        path = Path(args.prompt_file)
        if not path.is_file():
            sys.stderr.write(f"Error: prompt file not found: {path}\n")
            return 5
        content = path.read_text(encoding="utf-8")
    if not content and not sys.stdin.isatty():
        content = sys.stdin.read()
    if not content:
        sys.stderr.write("Error: no guidance provided\n")
        return 5

    mode = args.mode or "auto"
    if mode not in ("auto", "queue", "interrupt"):
        sys.stderr.write("Error: --mode must be auto|queue|interrupt\n")
        return 5

    client_id = args.client_id or None
    # Serialize validate_active + enqueue with supervisor terminal transition.
    try:
        with reg.with_run_lock(args.run_id):
            reg.validate_active(args.run_id)
            run_dir = reg.run_path(args.run_id)
            mb = Mailbox(run_dir)
            if mb.is_closed():
                raise RegistryError(
                    f"run is terminal (mailbox closed); cannot steer: {args.run_id}",
                    exit_code=5,
                )
            msg = mb.enqueue(
                kind="steer",
                content=content,
                mode=mode,
                client_id=client_id,
            )
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code
    except MailboxError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code

    progress(
        "steer",
        f"run_id={args.run_id}",
        f"mailbox_accepted client_id={msg['client_id']}",
        f"seq={msg['seq']}",
        f"mode={mode}",
        f"status={msg['status']}",
    )
    # Distinguish mailbox accepted from protocol delivery (status still accepted)
    out = {
        "run_id": args.run_id,
        "client_id": msg["client_id"],
        "client_id_safe": msg.get("client_id_safe"),
        "seq": msg["seq"],
        "mailbox_status": msg["status"],
        "mode": mode,
        "content_hash": msg.get("content_hash"),
        "note": "mailbox accepted only; poll status for delivery_class/protocol ack",
    }
    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(
            f"accepted client_id={msg['client_id']} seq={msg['seq']} "
            f"mailbox_status={msg['status']} (not yet protocol-delivered)"
        )
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    try:
        meta = reg.load_meta(args.run_id)
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code
    try:
        state = reg.load_state(args.run_id)
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code

    run_dir = reg.run_path(args.run_id)
    mb = Mailbox(run_dir)
    messages = mb.list_messages(after_seq=0)
    steers = []
    for m in messages:
        if m.get("kind") == "steer" or m.get("kind") == "invalid":
            msg_meta = m.get("meta") if isinstance(m.get("meta"), dict) else {}
            steers.append(
                {
                    "seq": m.get("seq"),
                    "client_id": m.get("client_id"),
                    "client_id_safe": m.get("client_id_safe"),
                    "mailbox_status": m.get("status"),
                    "delivery_class": m.get("delivery_class"),
                    "backend_ack": m.get("backend_ack"),
                    "error": m.get("error"),
                    "mode": m.get("mode"),
                    "content_hash": m.get("content_hash"),
                    "updated_at": m.get("updated_at"),
                    "prompt_id": msg_meta.get("promptId"),
                    "merged_into_prompt_id": msg_meta.get("mergedIntoPromptId"),
                    "superseded_by_prompt_id": msg_meta.get("supersededByPromptId"),
                    "cancel_trigger": msg_meta.get("cancelTrigger"),
                }
            )

    payload: Dict[str, Any] = {
        "run_id": args.run_id,
        "status": meta.get("status"),
        "agent_id": meta.get("agent_id"),
        "backend": meta.get("backend"),
        "model": meta.get("model"),
        "effort": meta.get("effort"),
        "pid": meta.get("pid"),
        "child_pid": meta.get("child_pid"),
        "exit_code": meta.get("exit_code"),
        "error": meta.get("error"),
        "started_at": meta.get("started_at"),
        "updated_at": meta.get("updated_at"),
        "finished_at": meta.get("finished_at"),
        "registry_recovered": bool(meta.get("recovery_count")),
        "registry_recovery_count": int(meta.get("recovery_count") or 0),
        "registry_recovery_reason": meta.get("recovery_reason"),
        "mailbox_closed": mb.is_closed(),
        "steers": steers,
        "state": state,
    }
    if meta.get("status") in TERMINAL_STATUSES:
        final = run_dir / "final.txt"
        if final.is_file():
            # Explicit preview label — full body remains in final.txt artifact
            payload["final_preview"] = preview_text(
                final.read_text(encoding="utf-8"), 500
            )
            payload["final_preview_note"] = "truncated status preview only; full text in final.txt"

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(
            f"run_id={args.run_id} status={meta.get('status')} backend={meta.get('backend')} "
            f"model={meta.get('model')} effort={meta.get('effort')}"
        )
        print(f"agent={meta.get('agent_id')} pid={meta.get('pid')} child={meta.get('child_pid')}")
        if meta.get("error"):
            print(f"error={meta.get('error')}")
        for s in steers:
            print(
                f"  steer seq={s.get('seq')} client_id={s.get('client_id')} "
                f"mailbox={s.get('mailbox_status')} class={s.get('delivery_class')} "
                f"ack={s.get('backend_ack')} err={s.get('error')}"
            )
    return 0


def cmd_cancel(args: argparse.Namespace) -> int:
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    try:
        with reg.with_run_lock(args.run_id):
            reg.request_cancel(args.run_id)
            run_dir = reg.run_path(args.run_id)
            mb = Mailbox(run_dir)
            # Cancel may still be useful while closing; allow when not fully closed yet.
            if not mb.is_closed():
                mb.enqueue(kind="cancel", content="", mode="auto", allow_when_closed=False)
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code
    except MailboxError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code
    progress("steer", f"run_id={args.run_id}", "cancel_enqueued")
    if args.json:
        print(json.dumps({"run_id": args.run_id, "cancel": "requested"}, indent=2))
    else:
        print(f"cancel requested for {args.run_id}")
    return 0


class _Interrupted(Exception):
    """SIGINT/SIGTERM reached the observer, not the run."""


def _install_observer_signals() -> None:
    """Ctrl-C on a watcher must never be mistaken for cancelling the run.

    wait/watch exit with the timeout code, leaving the supervisor untouched;
    `delegate cancel` remains the only way to stop actual work.
    """

    def _handler(signum, _frame):
        raise _Interrupted(str(signum))

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            signal.signal(sig, _handler)
        except (ValueError, OSError):
            pass


def _resolve_run(reg: Registry, run_id: str) -> Dict[str, Any]:
    """Fail fast on a bad id instead of spinning in a poll loop."""
    return reg.load_meta(run_id)


def _duration_seconds(meta: Dict[str, Any]) -> Optional[float]:
    started, finished = meta.get("started_at"), meta.get("finished_at")
    if not started or not finished:
        return None
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    try:
        return max(
            0.0,
            time.mktime(time.strptime(finished, fmt)) - time.mktime(time.strptime(started, fmt)),
        )
    except (ValueError, TypeError):
        return None


def cmd_wait(args: argparse.Namespace) -> int:
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    try:
        meta = _resolve_run(reg, args.run_id)
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code

    progress("wait", f"run_id={args.run_id}", "attached", f"status={meta.get('status')}")
    _install_observer_signals()

    started = time.time()
    last_beat = [started]

    def _heartbeat(snap) -> None:
        now = time.time()
        if snap.terminal or now - last_beat[0] < 15:
            return
        last_beat[0] = now
        progress(
            "wait",
            f"run_id={args.run_id}",
            f"status={snap.status}",
            f"elapsed={int(now - started)}s",
        )

    try:
        snap = wait_for_terminal(
            reg,
            args.run_id,
            timeout=args.timeout,
            poll_interval=args.poll_interval,
            on_event=_heartbeat,
        )
    except WaitTimeout as e:
        sys.stderr.write(
            f"Error: {e}. Resume with: consilium delegate wait {args.run_id}\n"
        )
        return EXIT_WAIT_TIMEOUT
    except _Interrupted:
        sys.stderr.write(
            f"Error: interrupted; run {args.run_id} is untouched. "
            f"Resume with: consilium delegate wait {args.run_id}\n"
        )
        return EXIT_WAIT_TIMEOUT
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code

    meta = snap.meta
    code = derive_exit_code(meta)
    found = read_final_text(reg, args.run_id, meta)
    progress(
        "done",
        f"run_id={args.run_id}",
        f"status={meta.get('status')}",
        f"exit={code}",
        f"final={'ok' if found is not None else 'missing'}",
    )

    if found is None:
        sys.stderr.write(
            f"Error: final text unavailable for {args.run_id} (status={meta.get('status')})\n"
        )
        # A failed run has no answer by construction; its own code says more
        # than "no text". 74 is reserved for the surprising case: the run
        # claims success yet produced nothing.
        return code or EXIT_NO_FINAL_TEXT
    text, final_path = found

    if args.quiet:
        return code
    if args.json:
        payload = {
            "run_id": args.run_id,
            "status": meta.get("status"),
            "exit_code": code,
            "run_exit_code": meta.get("exit_code"),
            "error": meta.get("error"),
            "agent_id": meta.get("agent_id"),
            "backend": meta.get("backend"),
            "model": meta.get("model"),
            "cwd": meta.get("cwd"),
            "artifacts_dir": meta.get("artifacts_dir"),
            "detach_log": meta.get("detach_log"),
            "started_at": meta.get("started_at"),
            "finished_at": meta.get("finished_at"),
            "duration_s": _duration_seconds(meta),
            "final_path": final_path,
            # Deliberately the FULL body — this is what `status --json` truncates.
            "final_text": text,
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return code

    # Byte-identical to what a foreground delegate prints on stdout.
    if text:
        sys.stdout.write(text)
        if not text.endswith("\n"):
            sys.stdout.write("\n")
        sys.stdout.flush()
    return code


# audit.jsonl gets one record per streamed chunk, so a raw tail would cost one
# model turn per token. Only lifecycle-bearing adapter events survive.
_AUDIT_KEEP_KINDS = frozenset(
    {"turn_started", "turn_completed", "prompt_complete", "error", "done"}
)
# Pure bookkeeping; the same information reaches the caller via state.steers.
_AUDIT_DROP_EVENTS = frozenset({"steer_ack_reconcile"})


class _AuditTail:
    """Byte-offset tail over run_dir/audit.jsonl. Never buffers the whole file."""

    def __init__(self, path: Path):
        self.path = path
        self.offset = 0
        self._partial = ""

    def read_new(self) -> list:
        records = []
        try:
            size = self.path.stat().st_size
        except OSError:
            return records
        if size < self.offset:  # truncated/replaced — restart cleanly
            self.offset = 0
            self._partial = ""
        if size == self.offset:
            return records
        try:
            with self.path.open("r", encoding="utf-8", errors="replace") as fh:
                fh.seek(self.offset)
                chunk = fh.read()
                self.offset = fh.tell()
        except OSError:
            return records
        buf = self._partial + chunk
        lines = buf.split("\n")
        self._partial = lines.pop()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(rec, dict):
                records.append(rec)
        return records


def cmd_watch(args: argparse.Namespace) -> int:
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    try:
        meta = _resolve_run(reg, args.run_id)
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code

    _install_observer_signals()
    started = time.time()
    state = {
        "last_emit": 0.0,
        "last_line": "",
        "status": None,
        "steers": {},
    }

    def emit(event: str, **fields: Any) -> None:
        now = time.time()
        if args.json:
            line = json.dumps(
                {"run_id": args.run_id, "ts": utc_now_iso(), "event": event, **fields},
                ensure_ascii=False,
            )
        else:
            parts = [f"[consilium] watch run_id={args.run_id}", f"ts={utc_now_iso()}", f"event={event}"]
            parts.extend(f"{k}={v}" for k, v in fields.items() if v is not None and v != "")
            line = " ".join(parts).replace("\n", " ")
        if line == state["last_line"] and now - state["last_emit"] < 1.0:
            return
        state["last_line"] = line
        state["last_emit"] = now
        print(line, flush=True)

    tail = _AuditTail(reg.run_path(args.run_id) / "audit.jsonl")

    emit(
        "attached",
        status=meta.get("status"),
        agent=meta.get("agent_id"),
        backend=meta.get("backend"),
        model=meta.get("model"),
        started_at=meta.get("started_at"),
    )
    state["status"] = meta.get("status")

    def on_event(snap) -> None:
        if snap.status != state["status"]:
            state["status"] = snap.status
            if not snap.terminal:
                emit("status", status=snap.status)

        steers = snap.state.get("steers") if isinstance(snap.state.get("steers"), dict) else {}
        for cid, cur in (steers or {}).items():
            if not isinstance(cur, dict):
                continue
            fingerprint = (cur.get("status"), cur.get("delivery_class"), cur.get("error"))
            if state["steers"].get(cid) == fingerprint:
                continue
            state["steers"][cid] = fingerprint
            emit(
                "steer",
                client_id=cid,
                status=cur.get("status"),
                delivery_class=cur.get("delivery_class"),
                error=preview_text(cur.get("error"), 120) if cur.get("error") else None,
            )

        for rec in tail.read_new():
            ev = str(rec.get("event") or "")
            if ev in _AUDIT_DROP_EVENTS:
                continue
            if ev == "adapter_event":
                kind = str(rec.get("kind") or "")
                if kind not in _AUDIT_KEEP_KINDS:
                    continue
                emit("turn", kind=kind, data=preview_text(rec.get("data_preview"), 120))
                continue
            emit(
                ev or "audit",
                client_id=rec.get("client_id"),
                status=rec.get("status"),
                error=preview_text(rec.get("error"), 120) if rec.get("error") else None,
            )

        if not snap.terminal and time.time() - state["last_emit"] >= args.heartbeat:
            emit("alive", status=snap.status, elapsed=f"{int(time.time() - started)}s")

    try:
        snap = wait_for_terminal(
            reg,
            args.run_id,
            timeout=args.timeout,
            poll_interval=args.poll_interval,
            on_event=on_event,
        )
    except WaitTimeout as e:
        emit("timeout", status=e.status, elapsed=f"{int(e.elapsed)}s")
        return EXIT_WAIT_TIMEOUT
    except _Interrupted:
        emit("detached", elapsed=f"{int(time.time() - started)}s")
        return EXIT_WAIT_TIMEOUT
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code

    code = derive_exit_code(snap.meta)
    found = read_final_text(reg, args.run_id, snap.meta)
    emit(
        "terminal",
        status=snap.meta.get("status"),
        exit=code,
        error=snap.meta.get("error"),
        final_bytes=len(found[0].encode("utf-8")) if found else 0,
        final_path=found[1] if found else None,
    )
    return code


def cmd_list(args: argparse.Namespace) -> int:
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    try:
        runs = reg.list_runs()
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code

    if args.reap:
        for meta in runs:
            if meta.get("effective_status") != "stale":
                continue
            run_id = str(meta.get("run_id") or "")
            try:
                with reg.with_run_lock(run_id):
                    reg.validate_active(run_id)
            except RegistryError:
                pass
        runs = reg.list_runs()

    if not args.all:
        runs = [
            m
            for m in runs
            if m.get("unreadable") or m.get("status") not in TERMINAL_STATUSES
        ]
    if args.limit > 0:
        runs = runs[: args.limit]

    if args.json:
        payload = [
            {
                "run_id": m.get("run_id"),
                "unreadable": m.get("unreadable"),
                "status": m.get("status"),
                "effective_status": m.get("effective_status"),
                "agent_id": m.get("agent_id"),
                "backend": m.get("backend"),
                "model": m.get("model"),
                "cwd": m.get("cwd"),
                "artifacts_dir": m.get("artifacts_dir"),
                "detach_log": m.get("detach_log"),
                "pid": m.get("pid"),
                "pid_alive": m.get("pid_alive"),
                "started_at": m.get("started_at"),
                "finished_at": m.get("finished_at"),
                "exit_code": m.get("exit_code"),
                "error": m.get("error"),
            }
            for m in runs
        ]
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    if not runs:
        return 0
    # Header on stderr so stdout stays machine-parseable without --json.
    sys.stderr.write(
        f"{'RUN_ID':<26} {'STATUS':<10} {'AGENT':<20} {'STARTED':<21} CWD\n"
    )
    for m in runs:
        if m.get("unreadable"):
            print(f"{str(m.get('run_id')):<26} {'unreadable':<10} {preview_text(m.get('unreadable'), 60)}")
            continue
        print(
            f"{str(m.get('run_id')):<26} {str(m.get('effective_status')):<10} "
            f"{str(m.get('agent_id')):<20} {str(m.get('started_at')):<21} {m.get('cwd')}"
        )
    return 0


def main(argv: Optional[list] = None) -> int:
    p = argparse.ArgumentParser(prog="consilium-steer-control")
    p.add_argument("--registry-root", default=os.environ.get("CONSILIUM_STEER_DIR", ""))
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("steer")
    s.add_argument("run_id")
    s.add_argument("guidance", nargs="?", default="")
    s.add_argument("--mode", default="auto", choices=["auto", "queue", "interrupt"])
    s.add_argument("--prompt-file", default="")
    s.add_argument("--client-id", default="")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_steer)

    st = sub.add_parser("status")
    st.add_argument("run_id")
    st.add_argument("--json", action="store_true")
    st.set_defaults(func=cmd_status)

    c = sub.add_parser("cancel")
    c.add_argument("run_id")
    c.add_argument("--json", action="store_true")
    c.set_defaults(func=cmd_cancel)

    w = sub.add_parser("wait")
    w.add_argument("run_id")
    w.add_argument("--timeout", type=float, default=0.0, help="seconds; 0 = unlimited")
    w.add_argument("--poll-interval", type=float, default=0.0, help="seconds; 0 = adaptive")
    w.add_argument("--json", action="store_true")
    w.add_argument("--quiet", action="store_true")
    w.set_defaults(func=cmd_wait)

    wt = sub.add_parser("watch")
    wt.add_argument("run_id")
    wt.add_argument("--timeout", type=float, default=0.0, help="seconds; 0 = unlimited")
    wt.add_argument("--poll-interval", type=float, default=0.0, help="seconds; 0 = adaptive")
    wt.add_argument("--heartbeat", type=float, default=60.0, help="seconds between alive lines")
    wt.add_argument("--json", action="store_true")
    wt.set_defaults(func=cmd_watch)

    ls = sub.add_parser("list")
    scope = ls.add_mutually_exclusive_group()
    scope.add_argument("--active", action="store_true", help="non-terminal runs (default)")
    scope.add_argument("--all", action="store_true", help="every run in the registry")
    ls.add_argument("--limit", type=int, default=50)
    ls.add_argument("--reap", action="store_true", help="mark dead-supervisor runs failed")
    ls.add_argument("--json", action="store_true")
    ls.set_defaults(func=cmd_list)

    args = p.parse_args(argv)
    if not args.registry_root:
        args.registry_root = ""
    # empty --client-id → None so mailbox generates one
    if hasattr(args, "client_id") and args.client_id == "":
        args.client_id = None
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
