"""Blocking observation of a steerable run: poll, liveness, final text.

Shared by `delegate wait` and `delegate watch`. Every guarantee this module
makes rests on two properties of the producer side:

  * all registry writes go through atomic_write_json / atomic_write_text
    (mkstemp + os.replace), so a reader never observes a torn file and needs
    no lock to read one; and
  * Supervisor._finalize writes the artifacts copies of the answer BEFORE the
    terminal meta transition, and run_dir/final.txt AFTER releasing the run
    lock. Seeing a terminal status therefore does NOT imply the authoritative
    final.txt exists yet — hence the settle window in read_final_text.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Tuple

from .registry import Registry, RegistryError, TERMINAL_STATUSES
from .util import pid_alive

# How long a terminal run is allowed to take to publish its final text.
TERMINAL_SETTLE_SECONDS = 3.0
# Grace given to an in-flight _finalize before we declare the supervisor dead.
DEAD_PID_GRACE_SECONDS = 0.75
# Adaptive poll schedule: tight at first (short runs), relaxed afterwards.
_FAST_POLL_SECONDS = 0.2
_FAST_POLL_WINDOW = 5.0
_SLOW_POLL_SECONDS = 1.0
_MAX_POLL_SECONDS = 2.0
# Exit codes owned by this module. common.sh already claims 0-6 and the
# supervisor uses 130 for cancelled, so these come from the sysexits band.
EXIT_SUPERVISOR_DEAD = 70
EXIT_NO_FINAL_TEXT = 74
EXIT_CANCELLED = 130
EXIT_WAIT_TIMEOUT = 124


@dataclass
class Snapshot:
    meta: Dict[str, Any] = field(default_factory=dict)
    state: Dict[str, Any] = field(default_factory=dict)
    status: str = ""
    terminal: bool = False
    pid: int = 0
    dead: bool = False


def poll_once(reg: Registry, run_id: str) -> Snapshot:
    """One consistent read of meta + state. No locks, no writes."""
    meta = reg.load_meta(run_id)
    try:
        state = reg.load_state(run_id)
    except RegistryError:
        # state.json is derived data; meta alone is enough to decide terminality.
        state = {}
    status = str(meta.get("status") or "")
    return Snapshot(
        meta=meta,
        state=state,
        status=status,
        terminal=status in TERMINAL_STATUSES,
        pid=int(meta.get("pid") or 0),
    )


def _reap_dead(reg: Registry, run_id: str) -> Snapshot:
    """Flip a run whose supervisor vanished to failed/supervisor_dead.

    This is the only place an observer mutates the registry, so it runs under
    the run lock: without it a slow _finalize holding the lock could have its
    legitimate `completed` overwritten by this reap.
    """
    try:
        with reg.with_run_lock(run_id, blocking=False):
            reg.validate_active(run_id)
    except BlockingIOError:
        # Another control/finalization operation owns the lock. Retry on the
        # next scan without holding up other targets or the observer deadline.
        return poll_once(reg, run_id)
    except RegistryError:
        pass
    snap = poll_once(reg, run_id)
    snap.dead = True
    return snap


def wait_for_any(
    reg: Registry,
    run_ids: list[str],
    *,
    timeout: Optional[float] = None,
    poll_interval: float = 0.0,
    on_event: Optional[Callable[[Snapshot], None]] = None,
) -> Tuple[Dict[str, Snapshot], bool]:
    """Observe all targets until any is terminal; timeout never cancels work.

    Validate every target before accepting a ready result. Liveness grace is
    tracked per target without sleeping inside the scan, so a slow/dead first
    worker cannot hide a later completion. A zero timeout is a pure snapshot.
    """
    if not run_ids:
        raise ValueError("at least one run is required")
    started = time.monotonic()
    deadline = None if timeout is None else started + timeout
    dead_since: Dict[str, float] = {}
    while True:
        snapshots = {rid: poll_once(reg, rid) for rid in run_ids}
        now = time.monotonic()
        for rid, snap in snapshots.items():
            if not snap.terminal and not pid_alive(snap.pid):
                first = dead_since.setdefault(rid, now)
                if now - first >= DEAD_PID_GRACE_SECONDS:
                    snapshots[rid] = _reap_dead(reg, rid)
            else:
                dead_since.pop(rid, None)
        if on_event:
            for snap in snapshots.values():
                on_event(snap)
        if any(s.terminal for s in snapshots.values()):
            return snapshots, False
        if deadline is not None and now >= deadline:
            return snapshots, True
        elapsed = now - started
        step = poll_interval if poll_interval > 0 else (
            _FAST_POLL_SECONDS if elapsed < _FAST_POLL_WINDOW else
            min(_SLOW_POLL_SECONDS * (1 + elapsed / 60.0), _MAX_POLL_SECONDS)
        )
        if deadline is not None:
            step = min(step, max(0.0, deadline - time.monotonic()))
        time.sleep(step)


def wait_for_terminal(
    reg: Registry,
    run_id: str,
    *,
    poll_interval: float = 0.0,
    timeout: Optional[float] = None,
    on_event: Optional[Callable[[Snapshot], None]] = None,
) -> Snapshot:
    """Return terminal state, or a still-active snapshot at the wait deadline."""
    snapshots, _ = wait_for_any(
        reg, [run_id], timeout=timeout, poll_interval=poll_interval, on_event=on_event
    )
    return snapshots[run_id]


def final_text_candidates(reg: Registry, run_id: str, meta: Dict[str, Any]) -> list:
    """Where the final answer may live, most authoritative first."""
    candidates = []
    try:
        candidates.append(reg.run_path(run_id) / "final.txt")
    except RegistryError:
        pass
    artifacts_dir = str(meta.get("artifacts_dir") or "")
    if artifacts_dir:
        base = Path(artifacts_dir)
        candidates.append(base / "final.txt")
        agent_id = str(meta.get("agent_id") or "")
        if agent_id:
            candidates.append(base / "final" / f"{agent_id}.txt")
    return candidates


def read_final_text(
    reg: Registry,
    run_id: str,
    meta: Dict[str, Any],
    *,
    settle: float = TERMINAL_SETTLE_SECONDS,
) -> Optional[Tuple[str, str]]:
    """Return (text, source_path) for a terminal run, or None if unavailable.

    run_dir/final.txt is written after the terminal transition, so it is polled
    for up to `settle` seconds before falling back to the artifacts copies —
    those are written strictly earlier and survive a degraded registry (see
    Supervisor._finalize). An empty answer is legitimate for a cancelled run
    and returns ("", path), which is not the same as None.
    """
    candidates = final_text_candidates(reg, run_id, meta)
    if not candidates:
        return None
    deadline = time.time() + max(settle, 0.0)
    while True:
        for path in candidates:
            try:
                if path.is_file():
                    return path.read_text(encoding="utf-8"), str(path)
            except OSError:
                continue
        if time.time() >= deadline:
            return None
        time.sleep(0.05)


def derive_exit_code(meta: Dict[str, Any]) -> int:
    """Map a terminal run onto the exit code the caller should observe."""
    status = str(meta.get("status") or "")
    if status == "completed":
        return 0
    if status == "cancelled":
        return EXIT_CANCELLED
    if status == "failed":
        if str(meta.get("error") or "") == "supervisor_dead":
            return EXIT_SUPERVISOR_DEAD
        try:
            code = int(meta.get("exit_code") or 0)
        except (TypeError, ValueError):
            code = 0
        return code or 1
    # Non-terminal should never reach here; treat as a generic failure.
    return 1
