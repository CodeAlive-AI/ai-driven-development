"""Claude Code steerable adapter: stream-json stdin + replay-user-messages."""
from __future__ import annotations

import json
import queue
import subprocess
import threading
import time
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional

from ..util import kill_process_group
from .base import AdapterEvent, BackendAdapter, DeliveryClass, SteerResult


class ClaudeAdapter(BackendAdapter):
    backend_name = "claude-code"
    auto_delivery = DeliveryClass.SAME_TURN

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.proc: Optional[subprocess.Popen] = None
        self._events: "queue.Queue[AdapterEvent]" = queue.Queue()
        self._stdin_lock = threading.Lock()
        self._reader: Optional[threading.Thread] = None
        self._stderr_reader: Optional[threading.Thread] = None
        self._pending_steers: Dict[str, Dict[str, Any]] = {}
        self._raw_path = Path(self.artifacts_dir) / "raw" / f"{self.agent_id or 'claude'}.jsonl"
        self._norm_path = Path(self.artifacts_dir) / "normalized" / f"{self.agent_id or 'claude'}.jsonl"
        self._result_text: Optional[str] = None
        self._cancelled = False
        self._result_seen = False
        self._lock = threading.Lock()

    def _argv(self) -> List[str]:
        cmd = [
            self.binary,
            "--dangerously-skip-permissions",
            "--model",
            self.model,
        ]
        if self.effort:
            cmd += ["--effort", self.effort]
        cmd += [
            "--output-format",
            "stream-json",
            "--input-format",
            "stream-json",
            "--replay-user-messages",
            "--verbose",
            "-p",
        ]
        return cmd

    def start(self, task: str) -> None:
        self._raw_path.parent.mkdir(parents=True, exist_ok=True)
        self._norm_path.parent.mkdir(parents=True, exist_ok=True)
        self.proc = subprocess.Popen(
            self._argv(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.cwd,
            text=True,
            bufsize=1,
            start_new_session=True,
        )
        self._reader = threading.Thread(target=self._read_loop, daemon=True)
        self._reader.start()
        # Always drain stderr so a chatty process cannot block on a full pipe.
        self._stderr_reader = threading.Thread(target=self._read_stderr, daemon=True)
        self._stderr_reader.start()
        self._write_user(task, client_id="initial")

    def _write_user(self, text: str, client_id: str) -> None:
        msg = {
            "type": "user",
            "message": {
                "role": "user",
                "content": [{"type": "text", "text": text}],
            },
            "uuid": client_id,
            "parent_tool_use_id": None,
        }
        line = json.dumps(msg, ensure_ascii=False) + "\n"
        assert self.proc and self.proc.stdin
        with self._stdin_lock:
            self.proc.stdin.write(line)
            self.proc.stdin.flush()
        with open(self._raw_path, "a", encoding="utf-8") as f:
            f.write(">> " + line)

    def _read_stderr(self) -> None:
        assert self.proc and self.proc.stderr
        try:
            for line in self.proc.stderr:
                with open(self._raw_path, "a", encoding="utf-8") as f:
                    f.write("stderr: " + line)
        except Exception:
            pass

    def _read_loop(self) -> None:
        assert self.proc and self.proc.stdout
        for line in self.proc.stdout:
            line = line.rstrip("\n")
            if not line:
                continue
            with open(self._raw_path, "a", encoding="utf-8") as f:
                f.write(line + "\n")
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                self._events.put(AdapterEvent(kind="raw", data=line))
                continue
            self._handle_obj(obj)
        # stdout closed — wait for process, but result may already have marked done
        rc = self.proc.wait()
        with self._lock:
            if self._exit_code is None:
                self._exit_code = rc
            if not self._done:
                self._done = True
                self._events.put(AdapterEvent(kind="done", data=str(rc)))

    def _handle_obj(self, obj: Dict[str, Any]) -> None:
        typ = obj.get("type")
        if typ == "user" or typ == "user_message" or obj.get("role") == "user":
            uuid = obj.get("uuid") or ""
            content_preview = ""
            msg = obj.get("message") or obj
            content = msg.get("content") if isinstance(msg, dict) else None
            if isinstance(content, list):
                parts = []
                for c in content:
                    if isinstance(c, dict) and c.get("type") == "text":
                        parts.append(c.get("text") or "")
                    elif isinstance(c, str):
                        parts.append(c)
                content_preview = "".join(parts)
            elif isinstance(content, str):
                content_preview = content
            self._events.put(
                AdapterEvent(
                    kind="user_replay",
                    data=content_preview,
                    raw={"uuid": uuid, "obj": obj},
                )
            )
            for cid, pending in list(self._pending_steers.items()):
                if uuid == cid or (pending.get("content") and pending["content"] in content_preview):
                    pending["replayed"] = True
            return
        if typ == "content_block_delta":
            d = obj.get("delta") or {}
            if d.get("type") == "text_delta":
                t = d.get("text") or ""
                if t:
                    self._final_parts.append(t)
                    self._events.put(AdapterEvent(kind="text", data=t, raw=obj))
            return
        if typ in ("result", "result_success"):
            # Authoritative result completes the adapter even if stdin stays open.
            result = obj.get("result")
            if isinstance(result, str):
                self._result_text = result
                self._final_parts = [result]
            is_error = bool(obj.get("is_error") or obj.get("error"))
            with self._lock:
                self._result_seen = True
                self._done = True
                if is_error:
                    self._exit_code = 1
                    self._error = str(obj.get("error") or result or "result_error")
                else:
                    self._exit_code = 0
            self._events.put(AdapterEvent(kind="done", data="result", raw=obj))
            return
        if typ == "assistant":
            msg = obj.get("message") or obj
            content = msg.get("content") if isinstance(msg, dict) else None
            if isinstance(content, list):
                for c in content:
                    if isinstance(c, dict) and c.get("type") == "text" and c.get("text"):
                        self._final_parts.append(c["text"])
                        self._events.put(AdapterEvent(kind="text", data=c["text"], raw=obj))
            return
        if typ == "error" or obj.get("error"):
            self._error = str(obj.get("error") or obj)
            self._events.put(AdapterEvent(kind="error", data=self._error, raw=obj))
            return
        self._events.put(AdapterEvent(kind="progress", data=typ or "event", raw=obj))

    def poll_events(self) -> Iterator[AdapterEvent]:
        while True:
            try:
                yield self._events.get_nowait()
            except queue.Empty:
                break
        if self.proc and self.proc.poll() is not None and not self._done:
            self._done = True
            self._exit_code = self.proc.returncode

    def _queue_class(self) -> DeliveryClass:
        # Claude has no separate queue; same-turn inject is the honest class.
        return DeliveryClass.SAME_TURN

    def _interrupt_class(self) -> DeliveryClass:
        raise NotImplementedError(
            "claude-code steerable does not support interrupt mode "
            "(same_turn only; refuse silent downgrade)"
        )

    def steer(self, content: str, mode: str, client_id: str) -> SteerResult:
        if self._done:
            return SteerResult(
                ok=False,
                delivery_class=self.auto_delivery,
                status="rejected",
                error="backend already completed",
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
        self._pending_steers[client_id] = {"content": content, "replayed": False}
        try:
            self._write_user(content, client_id=client_id)
        except Exception as e:
            return SteerResult(
                ok=False,
                delivery_class=dclass,
                status="failed",
                error=str(e),
            )
        # Brief wait for replay ack (protocol applied evidence).
        # Same-turn steers remain possible until authoritative result is seen.
        deadline = time.time() + 5.0
        applied = False
        while time.time() < deadline:
            for ev in self.poll_events():
                if ev.kind == "user_replay":
                    raw = ev.raw or {}
                    if raw.get("uuid") == client_id or content in (ev.data or ""):
                        applied = True
            if applied or self._pending_steers.get(client_id, {}).get("replayed"):
                applied = True
                break
            if self._done:
                break
            time.sleep(0.05)
        if applied:
            return SteerResult(
                ok=True,
                delivery_class=dclass,
                status="applied",
                evidence="user_message_replay",
            )
        return SteerResult(
            ok=True,
            delivery_class=dclass,
            status="request_sent",
            evidence="stdin_write",
        )

    def child_pid(self) -> Optional[int]:
        return self.proc.pid if self.proc else None

    def cancel(self) -> None:
        self._cancelled = True
        if self.proc and self.proc.poll() is None:
            try:
                if self.proc.stdin:
                    self.proc.stdin.close()
            except Exception:
                pass
            kill_process_group(self.proc.pid, timeout=3.0)
        self._done = True

    def final_text(self) -> str:
        if self._result_text is not None:
            return self._result_text
        return "".join(self._final_parts)

    def close(self) -> None:
        self.cancel()
