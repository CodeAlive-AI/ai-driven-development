#!/usr/bin/env python3
"""Run a streaming CLI and stop it after an authoritative terminal event.

Some OpenCode providers emit ``session.complete`` but keep the CLI process
alive.  The completed event is the protocol boundary; waiting forever for an
unrelated process shutdown turns a successful review into a hung fan-out.
This guard forwards stdout unchanged and gives the process a short grace period
after that boundary before terminating its process group.
"""

from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import sys
import threading
from typing import Any


OPENCODE_TERMINAL_TYPES = {
    "session.complete",
    "session.completed",
    "done",
}


def unwrap_event(value: Any) -> Any:
    if not isinstance(value, dict):
        return value
    payload = value.get("payload")
    if isinstance(payload, dict) and payload.get("type"):
        value = payload
    if value.get("type") == "sync" and isinstance(value.get("syncEvent"), dict):
        sync = value["syncEvent"]
        event_type = str(sync.get("type") or "")
        if event_type.endswith((".0", ".1")):
            event_type = event_type.rsplit(".", 1)[0]
        return {"type": event_type, "properties": sync.get("data") or sync}
    return value


def is_terminal(line: bytes, backend: str) -> bool:
    if backend != "opencode":
        return False
    try:
        event = unwrap_event(json.loads(line.decode("utf-8", errors="replace")))
    except Exception:
        return False
    return isinstance(event, dict) and str(event.get("type") or "") in OPENCODE_TERMINAL_TYPES


IS_WINDOWS = os.name == "nt"


def detached_popen_kwargs() -> dict[str, Any]:
    """Detach the child from the caller's signal delivery.

    POSIX uses a new session; Windows has no sessions, and start_new_session
    raises there, so the equivalent is a new process group.
    """
    if IS_WINDOWS:
        return {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP}
    return {"start_new_session": True}


def _taskkill(pid: int, force: bool) -> None:
    """Terminate a whole Windows process tree.

    Absolute path: resolving "taskkill" through the executable search order
    would let a taskkill.exe in the working directory run instead.
    """
    system_root = os.environ.get("SystemRoot", r"C:\Windows")
    exe = os.path.join(system_root, "System32", "taskkill.exe")
    if not os.path.isfile(exe):
        exe = "taskkill"
    argv = [exe, "/T", "/PID", str(pid)]
    if force:
        argv.insert(1, "/F")
    subprocess.run(argv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def signal_tree(proc: subprocess.Popen[bytes], *, force: bool) -> None:
    """Signal the child's whole process tree, best effort.

    Windows has no process groups in the POSIX sense and no SIGTERM/SIGKILL
    distinction for another process, so both levels map onto taskkill; only
    /F differs.
    """
    if IS_WINDOWS:
        _taskkill(proc.pid, force=force)
        return
    try:
        os.killpg(proc.pid, signal.SIGKILL if force else signal.SIGTERM)
    except ProcessLookupError:
        pass


def termination_signals() -> tuple[int, ...]:
    """Signals that mean "shut down" on this platform.

    SIGHUP does not exist on Windows; SIGBREAK is its closest analogue.
    """
    if IS_WINDOWS:
        extra = getattr(signal, "SIGBREAK", None)
        return (signal.SIGTERM,) + ((extra,) if extra is not None else ())
    return (signal.SIGTERM, signal.SIGHUP)


def stop_process_group(proc: subprocess.Popen[bytes]) -> None:
    if proc.poll() is not None:
        return
    signal_tree(proc, force=False)


def terminate_and_reap(proc: subprocess.Popen[bytes], timeout: float = 1.0) -> None:
    """Terminate the entire child session and do not leave an orphan behind."""
    if proc.poll() is not None:
        proc.wait()
        return
    stop_process_group(proc)
    try:
        proc.wait(timeout=timeout)
        return
    except subprocess.TimeoutExpired:
        pass
    signal_tree(proc, force=True)
    proc.wait()


class TerminationRequested(Exception):
    def __init__(self, signum: int):
        super().__init__(signum)
        self.signum = signum


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", required=True, choices=("opencode",))
    parser.add_argument("--terminal-grace", type=float, default=2.0)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("command required after --")
    if args.terminal_grace < 0:
        parser.error("--terminal-grace must be non-negative")

    proc = subprocess.Popen(
        command,
        stdin=sys.stdin.buffer,
        stdout=subprocess.PIPE,
        stderr=None,
        **detached_popen_kwargs(),
    )
    assert proc.stdout is not None

    def request_termination(signum: int, _frame: Any) -> None:
        raise TerminationRequested(signum)

    previous_handlers: dict[int, Any] = {}
    for signum in termination_signals():
        previous_handlers[signum] = signal.signal(signum, request_termination)
    forced_shutdown = threading.Event()
    terminal_timer: threading.Timer | None = None
    kill_timer: threading.Timer | None = None

    def kill_if_still_running() -> None:
        if proc.poll() is None:
            signal_tree(proc, force=True)

    def expire_terminal_grace() -> None:
        nonlocal kill_timer
        if proc.poll() is not None:
            return
        forced_shutdown.set()
        print(
            f"[consilium] {args.backend} emitted a terminal event but did not exit; "
            "terminating the completed CLI process",
            file=sys.stderr,
        )
        stop_process_group(proc)
        kill_timer = threading.Timer(1.0, kill_if_still_running)
        kill_timer.daemon = True
        kill_timer.start()

    try:
        for line in iter(proc.stdout.readline, b""):
            sys.stdout.buffer.write(line)
            sys.stdout.buffer.flush()
            if is_terminal(line, args.backend) and terminal_timer is None:
                # Keep draining after the protocol boundary: providers may
                # flush final text after the completion record. The timer only
                # bounds process shutdown; it never makes us abandon stdout.
                terminal_timer = threading.Timer(
                    args.terminal_grace,
                    expire_terminal_grace,
                )
                terminal_timer.daemon = True
                terminal_timer.start()
        return_code = proc.wait()
        return 0 if forced_shutdown.is_set() else return_code
    except KeyboardInterrupt:
        terminate_and_reap(proc)
        return 130
    except TerminationRequested as exc:
        terminate_and_reap(proc)
        return 128 + exc.signum
    finally:
        if terminal_timer is not None:
            terminal_timer.cancel()
        if kill_timer is not None:
            kill_timer.cancel()
        if proc.poll() is None:
            terminate_and_reap(proc)
        for signum, handler in previous_handlers.items():
            signal.signal(signum, handler)


if __name__ == "__main__":
    raise SystemExit(main())
