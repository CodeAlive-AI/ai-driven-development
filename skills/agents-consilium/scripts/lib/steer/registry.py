"""Atomic filesystem registry for steerable runs."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, Optional

from .util import (
    DIR_MODE,
    atomic_write_json,
    ensure_dir,
    flock_exclusive,
    new_id,
    path_owner_uid,
    pid_alive,
    progress,
    read_json,
    utc_now_iso,
)

TERMINAL_STATUSES = frozenset({"completed", "failed", "cancelled"})


def default_registry_root() -> Path:
    override = os.environ.get("CONSILIUM_STEER_DIR")
    if override:
        return Path(override).expanduser()
    xdg = os.environ.get("XDG_CACHE_HOME")
    if xdg:
        return Path(xdg) / "agents-consilium" / "steer"
    # macOS-friendly user cache default
    home = Path.home()
    mac_cache = home / "Library" / "Caches"
    if mac_cache.is_dir() or os.uname().sysname == "Darwin":
        return mac_cache / "agents-consilium" / "steer"
    return home / ".cache" / "agents-consilium" / "steer"


class RegistryError(Exception):
    def __init__(self, message: str, exit_code: int = 5):
        super().__init__(message)
        self.exit_code = exit_code


class Registry:
    def __init__(self, root: Optional[Path] = None):
        self.root = (root or default_registry_root()).expanduser()
        self.runs_dir = self.root / "runs"

    def ensure_root(self) -> None:
        ensure_dir(self.root, DIR_MODE)
        ensure_dir(self.runs_dir, DIR_MODE)

    def run_path(self, run_id: str) -> Path:
        if not run_id or "/" in run_id or "\\" in run_id or ".." in run_id or run_id.startswith("."):
            raise RegistryError(f"invalid run id: {run_id!r}")
        # Never follow / accept symlink run dirs
        candidate = self.runs_dir / run_id
        if candidate.is_symlink():
            raise RegistryError(f"run path is a symlink (rejected): {run_id}", exit_code=5)
        if not self.runs_dir.exists():
            # create before resolve checks when path not yet created
            ensure_dir(self.runs_dir, DIR_MODE)
        try:
            path = candidate.resolve(strict=False)
            path.relative_to(self.runs_dir.resolve())
        except ValueError as e:
            raise RegistryError(f"run path escapes registry: {run_id}") from e
        return candidate

    def run_lock_path(self, run_id: str) -> Path:
        return self.run_path(run_id) / "control" / "run.lock"

    def create_run(
        self,
        *,
        agent_id: str,
        backend: str,
        model: str,
        cwd: str,
        artifacts_dir: str,
        owner_uid: Optional[int] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> str:
        self.ensure_root()
        run_id = new_id("run_")
        rdir = self.runs_dir / run_id
        if rdir.exists() or rdir.is_symlink():
            raise RegistryError(f"run id collision: {run_id}", exit_code=1)
        ensure_dir(rdir, DIR_MODE)
        for sub in ("mailbox", "control", "steers", "turns"):
            ensure_dir(rdir / sub, DIR_MODE)
        uid = owner_uid if owner_uid is not None else os.getuid()
        if uid is None:
            raise RegistryError("owner_uid is required", exit_code=5)
        meta = {
            "run_id": run_id,
            "agent_id": agent_id,
            "backend": backend,
            "model": model,
            "cwd": cwd,
            "artifacts_dir": artifacts_dir,
            "status": "starting",
            "pid": os.getpid(),
            "owner_uid": int(uid),
            "started_at": utc_now_iso(),
            "updated_at": utc_now_iso(),
            "version": 1,
        }
        if extra:
            meta.update(extra)
        # owner_uid is mandatory after merge too
        if meta.get("owner_uid") is None:
            raise RegistryError("owner_uid is required in meta", exit_code=5)
        atomic_write_json(rdir / "meta.json", meta)
        atomic_write_json(
            rdir / "state.json",
            {
                "run_id": run_id,
                "status": "starting",
                "active_turn": None,
                "steers": {},
                "updated_at": utc_now_iso(),
            },
        )
        return run_id

    def _assert_run_dir_safe(self, run_id: str, rdir: Path) -> None:
        if rdir.is_symlink():
            raise RegistryError(f"run path is a symlink (rejected): {run_id}", exit_code=5)
        if not rdir.is_dir():
            raise RegistryError(f"unknown run: {run_id}", exit_code=5)
        # Actual owner of the run directory must match current uid (and meta).
        try:
            dir_uid = path_owner_uid(rdir)
        except OSError as e:
            raise RegistryError(f"cannot stat run dir: {run_id}: {e}", exit_code=5) from e
        if dir_uid != os.getuid():
            raise RegistryError(
                f"run dir owner uid {dir_uid} != current uid {os.getuid()}: {run_id}",
                exit_code=5,
            )

    def load_meta(self, run_id: str) -> Dict[str, Any]:
        rdir = self.run_path(run_id)
        self._assert_run_dir_safe(run_id, rdir)
        meta = read_json(rdir / "meta.json")
        if not isinstance(meta, dict):
            raise RegistryError(f"corrupt meta for run: {run_id}", exit_code=1)
        # Mandatory owner_uid field
        if "owner_uid" not in meta or meta.get("owner_uid") is None:
            raise RegistryError(f"meta missing owner_uid for run: {run_id}", exit_code=5)
        owner = int(meta["owner_uid"])
        if owner != os.getuid():
            raise RegistryError(f"run owned by different uid: {run_id}", exit_code=5)
        # Cross-check directory owner
        dir_uid = path_owner_uid(rdir)
        if dir_uid != owner:
            raise RegistryError(
                f"run dir owner {dir_uid} != meta owner_uid {owner}: {run_id}",
                exit_code=5,
            )
        return meta

    def update_meta(self, run_id: str, **fields: Any) -> Dict[str, Any]:
        rdir = self.run_path(run_id)
        meta = self.load_meta(run_id)
        meta.update(fields)
        # Never drop owner_uid
        if meta.get("owner_uid") is None:
            meta["owner_uid"] = os.getuid()
        meta["updated_at"] = utc_now_iso()
        atomic_write_json(rdir / "meta.json", meta)
        return meta

    def load_state(self, run_id: str) -> Dict[str, Any]:
        rdir = self.run_path(run_id)
        self._assert_run_dir_safe(run_id, rdir)
        state = read_json(rdir / "state.json", default={})
        if not isinstance(state, dict):
            raise RegistryError(f"corrupt state for run: {run_id}", exit_code=1)
        return state

    def update_state(self, run_id: str, **fields: Any) -> Dict[str, Any]:
        rdir = self.run_path(run_id)
        state = self.load_state(run_id)
        state.update(fields)
        state["updated_at"] = utc_now_iso()
        atomic_write_json(rdir / "state.json", state)
        return state

    def validate_active(self, run_id: str, *, allow_terminal: bool = False) -> Dict[str, Any]:
        meta = self.load_meta(run_id)
        status = meta.get("status", "")
        if status in TERMINAL_STATUSES and not allow_terminal:
            raise RegistryError(
                f"run is terminal ({status}); cannot steer/cancel: {run_id}",
                exit_code=5,
            )
        pid = int(meta.get("pid") or 0)
        if status not in TERMINAL_STATUSES and not pid_alive(pid):
            # Mark dead
            self.update_meta(run_id, status="failed", error="supervisor_dead")
            raise RegistryError(
                f"supervisor pid {pid} is dead for run: {run_id}",
                exit_code=5,
            )
        return meta

    def request_cancel(self, run_id: str) -> None:
        meta = self.validate_active(run_id)
        rdir = self.run_path(run_id)
        atomic_write_json(
            rdir / "control" / "cancel",
            {"requested_at": utc_now_iso(), "by_pid": os.getpid()},
        )
        progress("steer", f"run_id={run_id}", "cancel_requested")

    def cancel_requested(self, run_id: str) -> bool:
        return (self.run_path(run_id) / "control" / "cancel").is_file()

    def with_run_lock(self, run_id: str):
        """Exclusive run-level lock (serialize terminal transition vs enqueue)."""
        return flock_exclusive(self.run_lock_path(run_id))
