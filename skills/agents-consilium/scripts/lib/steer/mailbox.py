"""Atomic filesystem mailbox with portable locking and monotonic ordering."""
from __future__ import annotations

import fcntl
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .util import (
    DIR_MODE,
    atomic_write_json,
    content_hash,
    ensure_dir,
    new_id,
    safe_client_filename,
    secure_touch,
    utc_now_iso,
)

# Terminal / already-processed mailbox statuses (protocol or lifecycle).
TERMINAL_MSG_STATUSES = frozenset(
    {
        "delivered",
        "applied",
        "failed",
        "rejected",
        "queued",
        "request_sent",
    }
)
OPEN_MSG_STATUSES = frozenset({None, "accepted", "delivering"})


class MailboxError(Exception):
    def __init__(self, message: str, exit_code: int = 5):
        super().__init__(message)
        self.exit_code = exit_code


class Mailbox:
    """
    One supervisor is sole consumer. Concurrent writers serialize via flock.
    Messages are atomically written as msg-NNNNNN.json after claiming a seq.

    Steer records under steers/ use a SHA-256-based safe filename derived from
    client_id; the original client_id is preserved inside the JSON body.
    """

    def __init__(self, run_dir: Path):
        self.run_dir = Path(run_dir)
        self.dir = ensure_dir(self.run_dir / "mailbox", DIR_MODE)
        self.lock_path = self.dir / "lock"
        self.seq_path = self.dir / "seq"
        self.closed_path = self.dir / "closed"
        if not self.seq_path.exists():
            atomic_write_json(self.seq_path, {"next": 1})
        secure_touch(self.lock_path)

    def _with_lock(self):
        secure_touch(self.lock_path)
        return open(self.lock_path, "a+", encoding="utf-8")

    def is_closed(self) -> bool:
        return self.closed_path.is_file()

    def close(self, reason: str = "run_terminal") -> None:
        """Stop accepting new messages. Idempotent."""
        atomic_write_json(
            self.closed_path,
            {"closed_at": utc_now_iso(), "reason": reason},
        )

    def enqueue(
        self,
        *,
        kind: str,
        content: str,
        mode: str = "auto",
        client_id: Optional[str] = None,
        meta: Optional[Dict[str, Any]] = None,
        allow_when_closed: bool = False,
    ) -> Dict[str, Any]:
        if kind not in ("steer", "cancel"):
            raise MailboxError(f"unknown mailbox kind: {kind}")
        if mode not in ("auto", "queue", "interrupt"):
            raise MailboxError(f"unsupported mode: {mode}")
        client_id = client_id or new_id("steer_")
        if not isinstance(client_id, str) or not client_id:
            raise MailboxError("client_id must be a non-empty string")
        chash = content_hash(content) if content else content_hash("")
        with self._with_lock() as lf:
            fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
            try:
                if self.is_closed() and not allow_when_closed:
                    raise MailboxError(
                        "mailbox closed (run is terminal); cannot accept new messages",
                        exit_code=5,
                    )

                # Idempotency / conflict on same client_id
                existing = self._find_by_client_id_unlocked(client_id)
                if existing is not None:
                    same = (
                        existing.get("content_hash") == chash
                        and existing.get("mode") == mode
                        and existing.get("kind") == kind
                    )
                    if same:
                        return existing
                    raise MailboxError(
                        "client_id conflict: same client_id already used with different "
                        f"content_hash/mode/kind "
                        f"(existing kind={existing.get('kind')} mode={existing.get('mode')} "
                        f"hash={existing.get('content_hash')}; "
                        f"new kind={kind} mode={mode} hash={chash})",
                        exit_code=5,
                    )

                seq_obj = json.loads(self.seq_path.read_text(encoding="utf-8"))
                seq = int(seq_obj.get("next", 1))
                safe_name = safe_client_filename(client_id)
                msg = {
                    "seq": seq,
                    "client_id": client_id,  # original, may contain path chars
                    "client_id_safe": safe_name,
                    "kind": kind,
                    "content": content,
                    "content_hash": chash,
                    "mode": mode,
                    "status": "accepted",  # mailbox acceptance only
                    "created_at": utc_now_iso(),
                    "updated_at": utc_now_iso(),
                    "delivery_class": None,
                    "backend_ack": None,
                    "error": None,
                }
                if meta:
                    msg["meta"] = meta
                msg_path = self.dir / f"msg-{seq:06d}.json"
                atomic_write_json(msg_path, msg)
                # Durable steers record — never use raw client_id as path component
                if kind == "steer":
                    steers_dir = ensure_dir(self.run_dir / "steers", DIR_MODE)
                    steer_path = steers_dir / f"{safe_name}.json"
                    atomic_write_json(steer_path, msg)
                atomic_write_json(self.seq_path, {"next": seq + 1})
                return msg
            finally:
                fcntl.flock(lf.fileno(), fcntl.LOCK_UN)

    def _steer_path_for(self, client_id: str) -> Path:
        return self.run_dir / "steers" / f"{safe_client_filename(client_id)}.json"

    def _find_by_client_id_unlocked(self, client_id: str) -> Optional[Dict[str, Any]]:
        steer_path = self._steer_path_for(client_id)
        if steer_path.is_file():
            try:
                obj = json.loads(steer_path.read_text(encoding="utf-8"))
                if obj.get("client_id") == client_id:
                    return obj
            except json.JSONDecodeError:
                pass
        for p in sorted(self.dir.glob("msg-*.json")):
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            if obj.get("client_id") == client_id:
                return obj
        return None

    def _find_by_client_id(self, client_id: str) -> Optional[Dict[str, Any]]:
        with self._with_lock() as lf:
            fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
            try:
                return self._find_by_client_id_unlocked(client_id)
            finally:
                fcntl.flock(lf.fileno(), fcntl.LOCK_UN)

    def list_messages(self, *, after_seq: int = 0) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        for p in sorted(self.dir.glob("msg-*.json")):
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError) as e:
                # Malformed: surface as synthetic failed message
                out.append(
                    {
                        "seq": -1,
                        "client_id": f"malformed_{p.name}",
                        "kind": "invalid",
                        "content": "",
                        "status": "failed",
                        "error": f"malformed mailbox data: {e}",
                        "path": str(p),
                    }
                )
                continue
            if int(obj.get("seq", 0)) > after_seq:
                out.append(obj)
        out.sort(key=lambda m: int(m.get("seq", 0)))
        return out

    def update_message(self, seq: int, **fields: Any) -> Dict[str, Any]:
        with self._with_lock() as lf:
            fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
            try:
                path = self.dir / f"msg-{seq:06d}.json"
                if not path.is_file():
                    raise MailboxError(f"message seq not found: {seq}")
                try:
                    msg = json.loads(path.read_text(encoding="utf-8"))
                except json.JSONDecodeError as e:
                    raise MailboxError(f"malformed mailbox data seq={seq}: {e}") from e
                msg.update(fields)
                msg["updated_at"] = utc_now_iso()
                atomic_write_json(path, msg)
                cid = msg.get("client_id")
                if cid and msg.get("kind") == "steer":
                    atomic_write_json(self._steer_path_for(cid), msg)
                return msg
            finally:
                fcntl.flock(lf.fileno(), fcntl.LOCK_UN)

    def get_by_client_id(self, client_id: str) -> Optional[Dict[str, Any]]:
        return self._find_by_client_id(client_id)

    def fail_open_messages(self, reason: str) -> List[Dict[str, Any]]:
        """
        Mark every still-open message (accepted/delivering) as failed.
        Must be called while run-level lock + mailbox lock hold the terminal transition.
        """
        updated: List[Dict[str, Any]] = []
        with self._with_lock() as lf:
            fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
            try:
                for p in sorted(self.dir.glob("msg-*.json")):
                    try:
                        msg = json.loads(p.read_text(encoding="utf-8"))
                    except (json.JSONDecodeError, OSError):
                        continue
                    status = msg.get("status")
                    if status not in (None, "accepted", "delivering"):
                        continue
                    msg["status"] = "failed"
                    msg["error"] = reason
                    msg["updated_at"] = utc_now_iso()
                    atomic_write_json(p, msg)
                    cid = msg.get("client_id")
                    if cid and msg.get("kind") == "steer":
                        atomic_write_json(self._steer_path_for(cid), msg)
                    updated.append(msg)
            finally:
                fcntl.flock(lf.fileno(), fcntl.LOCK_UN)
        return updated
