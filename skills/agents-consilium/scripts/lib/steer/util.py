"""Shared utilities: atomic IO, hashing, process groups, secure modes, time helpers."""
from __future__ import annotations

import fcntl
import hashlib
import json
import os
import signal
import sys
import tempfile
import time
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Iterator, Optional

# Private-by-default modes for steerable registry state.
DIR_MODE = 0o700
FILE_MODE = 0o600


def utc_now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def new_id(prefix: str = "") -> str:
    u = uuid.uuid4().hex
    return f"{prefix}{u}" if prefix else u


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def safe_client_filename(client_id: str) -> str:
    """
    Stable filesystem-safe name for a client_id.
    Never use raw client_id as a path component (path traversal).
    """
    digest = hashlib.sha256(client_id.encode("utf-8")).hexdigest()
    return f"cid_{digest}"


def ensure_dir(path: Path, mode: int = DIR_MODE) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True, mode=mode)
    try:
        os.chmod(path, mode)
    except OSError:
        pass
    return path


def secure_touch(path: Path, mode: int = FILE_MODE) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    if not path.exists():
        fd = os.open(str(path), os.O_CREAT | os.O_WRONLY, mode)
        os.close(fd)
    try:
        os.chmod(path, mode)
    except OSError:
        pass


def _chmod_path(path: Path, mode: int) -> None:
    try:
        os.chmod(path, mode)
    except OSError:
        pass


def atomic_write_json(path: Path, obj: Any, indent: int = 2, mode: int = FILE_MODE) -> None:
    """Write JSON atomically via temp file + replace. No partial JSON on target."""
    path = Path(path)
    ensure_dir(path.parent)
    data = json.dumps(obj, indent=indent, ensure_ascii=False, sort_keys=True) + "\n"
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(tmp_name, mode)
        os.replace(tmp_name, path)
        _chmod_path(path, mode)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def atomic_write_text(path: Path, text: str, mode: int = FILE_MODE) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(tmp_name, mode)
        os.replace(tmp_name, path)
        _chmod_path(path, mode)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def read_json(path: Path, default: Optional[Any] = None) -> Any:
    path = Path(path)
    if not path.is_file():
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def append_jsonl(path: Path, obj: Dict[str, Any], mode: int = FILE_MODE) -> None:
    """Append one full JSON object as a line. Payloads are never truncated here."""
    path = Path(path)
    ensure_dir(path.parent)
    line = json.dumps(obj, ensure_ascii=False, sort_keys=True) + "\n"
    # Open with restrictive mode if creating
    flags = os.O_APPEND | os.O_WRONLY | os.O_CREAT
    fd = os.open(str(path), flags, mode)
    try:
        with os.fdopen(fd, "a", encoding="utf-8") as f:
            f.write(line)
            f.flush()
    except Exception:
        try:
            os.close(fd)
        except OSError:
            pass
        raise
    _chmod_path(path, mode)


def progress(scope: str, *parts: str) -> None:
    """Live progress on stderr only. Callers must pass previews, not full bodies."""
    msg = " ".join(str(p) for p in parts if p is not None and p != "")
    if msg:
        sys.stderr.write(f"[consilium] {scope} {msg}\n")
    else:
        sys.stderr.write(f"[consilium] {scope}\n")
    sys.stderr.flush()


def preview_text(s: Optional[str], n: int) -> str:
    """Explicitly labeled short preview for stderr/status (not for artifacts)."""
    s = s or ""
    s = s.replace("\n", " ")
    if len(s) <= n:
        return s
    return s[: max(0, n - 1)] + "…"


def pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def kill_process_group(pid: int, timeout: float = 5.0) -> None:
    """Deterministic process-group cancellation. Best-effort, no orphans preferred."""
    if pid <= 0:
        return
    try:
        pgid = os.getpgid(pid)
    except OSError:
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError:
            pass
        return
    try:
        os.killpg(pgid, signal.SIGTERM)
    except OSError:
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError:
            pass
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not pid_alive(pid):
            return
        time.sleep(0.05)
    try:
        os.killpg(pgid, signal.SIGKILL)
    except OSError:
        try:
            os.kill(pid, signal.SIGKILL)
        except OSError:
            pass


def resolve_under_root(root: Path, candidate: Path) -> Path:
    """
    Resolve candidate and ensure it stays under root.
    Rejects symlink escapes. Raises ValueError on unsafe paths.
    """
    root = root.resolve()
    candidate = Path(candidate)
    if not candidate.is_absolute():
        candidate = root / candidate

    # Walk component-by-component; reject symlink that escapes root
    acc = Path(candidate.anchor) if candidate.is_absolute() else Path.cwd()
    parts = candidate.parts[1:] if candidate.is_absolute() else candidate.parts
    for part in parts:
        nxt = acc / part
        if nxt.is_symlink():
            target = nxt.resolve()
            try:
                target.relative_to(root)
            except ValueError as e:
                raise ValueError(f"symlink escapes registry root: {nxt} -> {target}") from e
        acc = nxt

    resolved = candidate.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as e:
        raise ValueError(f"path escapes registry root: {candidate}") from e
    return resolved


def path_owner_uid(path: Path) -> int:
    return path.stat().st_uid


def is_loopback_url(url: str) -> bool:
    """
    Return True only for http(s) URLs whose host is loopback after parsing.

    Accepts exact hostname ``localhost`` and any address where
    ``ipaddress.ip_address(...).is_loopback`` is true (127.0.0.0/8, ::1).
    Rejects prefix tricks like ``127.evil.example`` (host.startswith is unsafe).
    """
    import ipaddress
    from urllib.parse import urlparse

    try:
        parsed = urlparse(url)
    except Exception:
        return False
    if parsed.scheme not in ("http", "https"):
        return False
    host = (parsed.hostname or "").lower().strip()
    if not host:
        return False
    if host == "localhost":
        return True
    # Strip brackets from IPv6 literals if present via hostname already.
    try:
        return bool(ipaddress.ip_address(host).is_loopback)
    except ValueError:
        return False


@contextmanager
def flock_exclusive(lock_path: Path) -> Iterator[None]:
    """Exclusive flock around a run-level critical section."""
    ensure_dir(lock_path.parent)
    secure_touch(lock_path)
    with open(lock_path, "a+", encoding="utf-8") as lf:
        fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lf.fileno(), fcntl.LOCK_UN)


def eprint(msg: str) -> None:
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()
