"""OpenCode steerable adapter: ephemeral serve + SSE + prompt_async.

Contracts:
- step_inject while session is busy (prompt_async accepted mid-run)
- terminal when session goes idle for this delegate-run (not a permanent idle session)
- SSE read uses buffered chunks (never byte-at-a-time) without frame loss
- base_url must be loopback after URL parse (no external exfiltration)
- HTTP redirects re-validated to loopback only (custom opener)
- OPENCODE_SERVER_PASSWORD + Basic auth on every request (password never logged)
- message.part.updated is a cumulative snapshot per part id (not append-delta)
- message.part.delta remains incremental
"""
from __future__ import annotations

import base64
import json
import queue
import re
import secrets
import subprocess
import threading
import time
import urllib.error
import urllib.request
from http.client import HTTPResponse
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional
from urllib.parse import quote, urlparse

from ..util import is_loopback_url, kill_process_group
from .base import AdapterEvent, BackendAdapter, DeliveryClass, SteerResult

# Default OpenCode basic-auth username when OPENCODE_SERVER_USERNAME is unset.
_DEFAULT_SERVER_USERNAME = "opencode"


class _LoopbackRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Follow redirects only when every hop stays on loopback."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        if not is_loopback_url(newurl):
            raise urllib.error.HTTPError(
                newurl,
                code,
                f"refusing non-loopback redirect target: {newurl}",
                headers,
                fp,
            )
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _build_loopback_opener() -> urllib.request.OpenerDirector:
    return urllib.request.build_opener(_LoopbackRedirectHandler)


class OpenCodeAdapter(BackendAdapter):
    backend_name = "opencode"
    auto_delivery = DeliveryClass.STEP_INJECT

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.proc: Optional[subprocess.Popen] = None
        self.base_url: Optional[str] = None
        self.session_id: Optional[str] = None
        self._events: "queue.Queue[AdapterEvent]" = queue.Queue()
        self._raw_path = Path(self.artifacts_dir) / "raw" / f"{self.agent_id or 'opencode'}.jsonl"
        self._sse_thread: Optional[threading.Thread] = None
        self._stderr_thread: Optional[threading.Thread] = None
        self._stdout_thread: Optional[threading.Thread] = None
        self._busy = False
        # Incremental delta pieces (message.part.delta).
        self._text_parts: List[str] = []
        # Cumulative snapshot text keyed by part id (message.part.updated).
        self._part_snapshots: Dict[str, str] = {}
        self._lock = threading.Lock()
        self._cancelled = False
        # Per-run Basic auth — generated here, passed only to child env.
        self._server_username = _DEFAULT_SERVER_USERNAME
        self._server_password = secrets.token_urlsafe(32)
        self._opener = _build_loopback_opener()

    def _auth_header_value(self) -> str:
        token = base64.b64encode(
            f"{self._server_username}:{self._server_password}".encode("utf-8")
        ).decode("ascii")
        return f"Basic {token}"

    def _auth_headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = dict(extra or {})
        headers["Authorization"] = self._auth_header_value()
        return headers

    def _argv(self) -> List[str]:
        # port 0 = ephemeral loopback
        return [
            self.binary,
            "serve",
            "--hostname",
            "127.0.0.1",
            "--port",
            "0",
            "--print-logs",
        ]

    def _child_env(self) -> Dict[str, str]:
        """Env for opencode serve only — never log or persist the password."""
        import os

        env = os.environ.copy()
        env["OPENCODE_SERVER_PASSWORD"] = self._server_password
        env["OPENCODE_SERVER_USERNAME"] = self._server_username
        return env

    def start(self, task: str) -> None:
        self._raw_path.parent.mkdir(parents=True, exist_ok=True)
        # Note: password is in child env only — never written to raw/meta.
        self._log_raw(
            {
                "event": "server_start",
                "auth": "basic",
                "username": self._server_username,
                # password intentionally omitted
            }
        )
        self.proc = subprocess.Popen(
            self._argv(),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.cwd,
            env=self._child_env(),
            text=True,
            bufsize=1,
            start_new_session=True,
        )
        # Drain both pipes so a chatty serve process cannot block on a full buffer.
        self._stderr_thread = threading.Thread(
            target=self._read_stdio_for_url, args=("stderr",), daemon=True
        )
        self._stderr_thread.start()
        self._stdout_thread = threading.Thread(
            target=self._read_stdio_for_url, args=("stdout",), daemon=True
        )
        self._stdout_thread.start()
        deadline = time.time() + 30.0
        while time.time() < deadline and not self.base_url:
            if self.proc.poll() is not None:
                raise RuntimeError("opencode serve exited early before publishing URL")
            time.sleep(0.05)
        if not self.base_url:
            raise RuntimeError("opencode serve did not print listening URL")
        self._log_raw({"event": "server_url", "url": self.base_url})
        self._http_json("GET", "/global/health", timeout=10.0)
        body: Dict[str, Any] = {}
        path = f"/session?directory={quote(self.cwd, safe='')}"
        sess = self._http_json("POST", path, body=body, timeout=30.0)
        self.session_id = (sess or {}).get("id") or (sess or {}).get("sessionID")
        if not self.session_id:
            self.session_id = (
                (sess or {}).get("data", {}).get("id") if isinstance(sess, dict) else None
            )
        if not self.session_id:
            raise RuntimeError(f"opencode session create failed: {sess}")
        self._sse_thread = threading.Thread(target=self._sse_loop, daemon=True)
        self._sse_thread.start()
        time.sleep(0.05)
        self._prompt_async(task, client_id="initial")

    def _read_stdio_for_url(self, stream_name: str) -> None:
        assert self.proc
        stream = self.proc.stderr if stream_name == "stderr" else self.proc.stdout
        assert stream is not None
        for line in stream:
            line = line.rstrip("\n")
            # Redact password if a log line ever echoed the env value.
            safe = line
            if self._server_password and self._server_password in safe:
                safe = safe.replace(self._server_password, "<redacted>")
            self._log_raw({stream_name: safe})
            self._maybe_set_url(line)

    def _maybe_set_url(self, line: str) -> None:
        if self.base_url:
            return
        candidate = None
        m = re.search(r"listening on (https?://[^\s]+)", line, re.I)
        if m:
            candidate = m.group(1).rstrip("/")
        else:
            m2 = re.search(r"https?://127\.0\.0\.1:(\d+)", line)
            if m2:
                candidate = f"http://127.0.0.1:{m2.group(1)}"
            else:
                m3 = re.search(r"https?://\[?::1\]?:(\d+)", line)
                if m3:
                    candidate = f"http://127.0.0.1:{m3.group(1)}"
        if not candidate:
            return
        # Validate loopback *after* parsing — reject external hosts.
        if not is_loopback_url(candidate):
            self._log_raw({"rejected_url": candidate, "reason": "not_loopback"})
            self._events.put(
                AdapterEvent(
                    kind="error",
                    data=f"opencode URL is not loopback (rejected): {candidate}",
                )
            )
            return
        # Normalize host to 127.0.0.1 for consistency
        parsed = urlparse(candidate)
        port = parsed.port
        if port:
            self.base_url = f"http://127.0.0.1:{port}"
        else:
            self.base_url = "http://127.0.0.1"

    def _log_raw(self, obj: Any) -> None:
        # Never persist the server password into raw artifacts.
        if isinstance(obj, dict):
            scrubbed = dict(obj)
            for key in ("password", "OPENCODE_SERVER_PASSWORD", "Authorization", "authorization"):
                scrubbed.pop(key, None)
            body = scrubbed.get("body")
            if isinstance(body, dict):
                body = dict(body)
                body.pop("password", None)
                scrubbed["body"] = body
            obj = scrubbed
        with open(self._raw_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")

    def _assert_loopback_url(self, url: str) -> None:
        if not is_loopback_url(url):
            raise RuntimeError(f"refusing non-loopback OpenCode URL: {url}")

    def _http_json(
        self,
        method: str,
        path: str,
        body: Optional[Dict[str, Any]] = None,
        timeout: float = 60.0,
        expect_empty: bool = False,
    ) -> Any:
        assert self.base_url
        self._assert_loopback_url(self.base_url)
        url = self.base_url + path
        self._assert_loopback_url(url)
        data = None
        headers = self._auth_headers({"Accept": "application/json"})
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        # Log without Authorization header.
        self._log_raw({"http": method, "url": url, "body": body, "auth": "basic"})
        try:
            with self._opener.open(req, timeout=timeout) as resp:
                raw = resp.read()
                if expect_empty or not raw:
                    return {"status": resp.status}
                try:
                    return json.loads(raw.decode("utf-8"))
                except json.JSONDecodeError:
                    return {
                        "raw": raw.decode("utf-8", errors="replace"),
                        "status": resp.status,
                    }
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            self._log_raw({"http_error": e.code, "body": err_body, "url": url})
            raise RuntimeError(f"HTTP {e.code} {method} {path}: {err_body}") from e

    def _prompt_async(self, text: str, client_id: str) -> None:
        assert self.session_id
        payload: Dict[str, Any] = {
            "parts": [{"type": "text", "text": text}],
            "agent": "build",
        }
        if self.model:
            # OpenCode 1.x prompt_async expects model.modelID (not model.id).
            if "/" in self.model:
                provider, mid = self.model.split("/", 1)
                payload["model"] = {"providerID": provider, "modelID": mid}
            else:
                payload["model"] = {"modelID": self.model}
        payload["metadata"] = {"clientId": client_id}
        path = f"/session/{quote(self.session_id, safe='')}/prompt_async"
        if self.cwd:
            path += f"?directory={quote(self.cwd, safe='')}"
        self._http_json("POST", path, body=payload, timeout=30.0, expect_empty=True)
        with self._lock:
            self._busy = True

    def _abort(self) -> None:
        if not self.session_id:
            return
        path = f"/session/{quote(self.session_id, safe='')}/abort"
        try:
            self._http_json("POST", path, body={}, timeout=15.0, expect_empty=True)
        except Exception as e:
            self._log_raw({"abort_error": str(e)})

    def _sse_loop(self) -> None:
        assert self.base_url
        self._assert_loopback_url(self.base_url)
        url = self.base_url + "/global/event"
        self._assert_loopback_url(url)
        req = urllib.request.Request(
            url, headers=self._auth_headers({"Accept": "text/event-stream"})
        )
        try:
            resp: HTTPResponse = self._opener.open(req, timeout=30.0)  # type: ignore[assignment]
            try:
                resp.fp.raw._sock.settimeout(0.5)  # type: ignore[attr-defined]
            except Exception:
                pass
        except Exception as e:
            self._events.put(AdapterEvent(kind="error", data=f"sse_connect_failed: {e}"))
            return
        # Buffered line reader (not read(1)): assemble SSE frames on blank-line
        # boundaries. readline returns as soon as a line is available; incomplete
        # frames stay in the line buffer until the blank separator arrives.
        event_lines: List[str] = []
        try:
            while not self._done:
                try:
                    # HTTPResponse is a binary/text file-like; prefer fp.readline
                    fp = getattr(resp, "fp", resp)
                    raw_line = fp.readline(65536)
                except Exception:
                    if self._done:
                        break
                    time.sleep(0.05)
                    continue
                if raw_line == b"" or raw_line == "":
                    # True EOF from server
                    break
                if isinstance(raw_line, bytes):
                    line = raw_line.decode("utf-8", errors="replace")
                else:
                    line = str(raw_line)
                # Strip only the line terminator; preserve payload spaces
                if line.endswith("\r\n"):
                    line = line[:-2]
                elif line.endswith("\n"):
                    line = line[:-1]
                elif line.endswith("\r"):
                    line = line[:-1]
                if line == "":
                    # End of one SSE event
                    if event_lines:
                        self._handle_sse_block("\n".join(event_lines))
                        event_lines = []
                else:
                    event_lines.append(line)
        except Exception as e:
            if not self._done:
                self._events.put(AdapterEvent(kind="error", data=f"sse_error: {e}"))
        finally:
            if event_lines:
                self._handle_sse_block("\n".join(event_lines))
            try:
                resp.close()
            except Exception:
                pass
            if not self._done and (self._text_parts or self._part_snapshots):
                self._done = True
                self._exit_code = 0
                self._events.put(AdapterEvent(kind="done", data="sse_eof"))

    def _handle_sse_block(self, block: str) -> None:
        data_lines = []
        for line in block.split("\n"):
            if line.startswith("data:"):
                # Accept both "data:" and "data: " prefixes
                data_lines.append(line[5:].lstrip() if line.startswith("data: ") else line[5:].lstrip())
        if not data_lines:
            return
        payload = "\n".join(data_lines)
        # Full SSE payload in raw artifacts — never truncate.
        self._log_raw({"sse": payload})
        try:
            obj = json.loads(payload)
        except json.JSONDecodeError:
            # Full malformed payload too
            self._events.put(AdapterEvent(kind="raw", data=payload))
            return
        self._handle_event(obj)

    def _handle_event(self, obj: Dict[str, Any]) -> None:
        # Real OpenCode 1.18 SSE wraps events as:
        #   { "directory": "...", "project": "...", "payload": { "type": "...", "properties": {...} } }
        # Fake transports and some older shapes put type at the top level.
        if (
            isinstance(obj.get("payload"), dict)
            and (obj.get("type") is None or obj.get("type") == "sync")
            and obj["payload"].get("type")
        ):
            # Prefer the inner event; keep outer for raw audit already logged.
            obj = obj["payload"]
        # Nested syncEvent envelope (type=sync)
        if obj.get("type") == "sync" and isinstance(obj.get("syncEvent"), dict):
            # syncEvent.type looks like "session.updated.1" — strip trailing version
            se = obj["syncEvent"]
            se_type = str(se.get("type") or "")
            if se_type.endswith(".1") or se_type.endswith(".0"):
                se_type = se_type.rsplit(".", 1)[0]
            if se_type:
                # Rebuild a normal event from syncEvent for idle/text handling
                data = se.get("data") if isinstance(se.get("data"), dict) else {}
                obj = {
                    "type": se_type,
                    "properties": data if data else se,
                }
        typ = obj.get("type") or obj.get("event") or ""
        props = obj.get("properties") or obj.get("payload") or obj
        if not isinstance(props, dict):
            props = {}
        if typ == "message.part.delta":
            # Incremental append.
            part = props.get("part") or props
            delta = props.get("delta") or ""
            text = delta or (part.get("text") if isinstance(part, dict) else "") or ""
            if text:
                self._text_parts.append(str(text))
                self._final_parts.append(str(text))
                self._events.put(AdapterEvent(kind="text", data=str(text), raw=obj))
            return
        if typ == "message.part.updated":
            # Cumulative snapshot per part id — store latest, do not append H+He+Hello.
            part = props.get("part") if isinstance(props.get("part"), dict) else props
            if not isinstance(part, dict):
                part = {}
            part_id = (
                part.get("id")
                or part.get("partID")
                or part.get("partId")
                or props.get("partID")
                or props.get("id")
                or ""
            )
            text = part.get("text") if isinstance(part.get("text"), str) else ""
            if text == "" and isinstance(props.get("delta"), str) and not part.get("text"):
                # Some emitters still put a full snapshot in delta-less updated.
                text = ""
            if text:
                key = str(part_id) if part_id else "_default"
                with self._lock:
                    prev = self._part_snapshots.get(key, "")
                    self._part_snapshots[key] = text
                # Emit only the newly extended suffix for live progress (if any).
                if text.startswith(prev) and len(text) > len(prev):
                    suffix = text[len(prev) :]
                    self._events.put(AdapterEvent(kind="text", data=suffix, raw=obj))
                elif text != prev:
                    # Non-prefix replacement: surface full snapshot as progress text
                    self._events.put(AdapterEvent(kind="text", data=text, raw=obj))
            return
        if typ in ("session.idle", "session.status", "session.completed", "session.complete"):
            status = props.get("status") or typ
            status_l = str(status).lower()
            if (
                "idle" in status_l
                or "complete" in status_l
                or typ in ("session.completed", "session.complete", "session.idle")
            ):
                with self._lock:
                    self._busy = False
                self._events.put(AdapterEvent(kind="turn_completed", data=str(status), raw=obj))
                # Idle/complete for *this* delegate-run ends the adapter.
                # Further steers must arrive before this event; supervisor
                # drains the mailbox between events.
                if not self._done:
                    self._done = True
                    self._exit_code = 0
                    self._events.put(AdapterEvent(kind="done", data="idle", raw=obj))
            return
        if typ in ("session.error", "error"):
            self._error = str(props)
            self._events.put(AdapterEvent(kind="error", data=self._error, raw=obj))
            # Provider/stream errors should end the steerable run (not hang forever).
            if not self._done:
                self._done = True
                self._exit_code = 1
                self._events.put(AdapterEvent(kind="done", data="session_error", raw=obj))
            return
        if "message" in typ or "session" in typ or "part" in typ:
            self._events.put(AdapterEvent(kind="progress", data=typ, raw=obj))
            return
        self._events.put(AdapterEvent(kind="progress", data=typ or "event", raw=obj))

    def poll_events(self) -> Iterator[AdapterEvent]:
        if self.proc and self.proc.poll() is not None and not self._done:
            self._done = True
            rc = self.proc.returncode
            self._exit_code = 0 if rc == 0 else (rc if rc is not None else 1)
            if (self._text_parts or self._part_snapshots) and self._exit_code != 0:
                self._exit_code = 0
            self._events.put(AdapterEvent(kind="done", data=str(rc)))
        while True:
            try:
                yield self._events.get_nowait()
            except queue.Empty:
                break

    def is_busy(self) -> bool:
        with self._lock:
            return self._busy and not self._done

    def _queue_class(self) -> DeliveryClass:
        return DeliveryClass.STEP_INJECT

    def _interrupt_class(self) -> DeliveryClass:
        return DeliveryClass.ABORT_AND_PROMPT

    def steer(self, content: str, mode: str, client_id: str) -> SteerResult:
        if self._done or not self.session_id:
            return SteerResult(
                ok=False,
                delivery_class=self.auto_delivery,
                status="rejected",
                error="backend not ready or already completed",
            )
        try:
            dclass = self.map_mode(mode)
        except NotImplementedError as e:
            return SteerResult(
                ok=False,
                delivery_class=self.auto_delivery,
                status="rejected",
                error=str(e),
            )
        if mode == "interrupt" or dclass == DeliveryClass.ABORT_AND_PROMPT:
            self._abort()
            try:
                self._prompt_async(content, client_id=client_id)
            except Exception as e:
                return SteerResult(
                    ok=False,
                    delivery_class=dclass,
                    status="failed",
                    error=str(e),
                )
            return SteerResult(
                ok=True,
                delivery_class=DeliveryClass.ABORT_AND_PROMPT,
                status="request_sent",
                evidence="abort_then_prompt_async",
            )
        # step_inject while busy is the intended OpenCode contract
        try:
            self._prompt_async(content, client_id=client_id)
        except Exception as e:
            return SteerResult(
                ok=False,
                delivery_class=dclass,
                status="failed",
                error=str(e),
            )
        with self._lock:
            busy = self._busy
        return SteerResult(
            ok=True,
            delivery_class=DeliveryClass.STEP_INJECT,
            status="request_sent",
            evidence="prompt_async_accepted" + ("_while_busy" if busy else ""),
            meta={"busy": busy},
        )

    def child_pid(self) -> Optional[int]:
        return self.proc.pid if self.proc else None

    def cancel(self) -> None:
        self._cancelled = True
        try:
            self._abort()
        except Exception:
            pass
        if self.proc and self.proc.poll() is None:
            kill_process_group(self.proc.pid, timeout=3.0)
        self._done = True

    def final_text(self) -> str:
        # Prefer cumulative snapshots when present (join stable part-id order),
        # else incremental deltas.
        with self._lock:
            snaps = dict(self._part_snapshots)
        if snaps:
            # Deterministic: sort keys so multi-part is stable.
            return "".join(snaps[k] for k in sorted(snaps.keys()))
        return "".join(self._text_parts) or "".join(self._final_parts)

    def close(self) -> None:
        self.cancel()
