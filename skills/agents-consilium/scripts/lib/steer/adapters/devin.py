"""Devin steerable adapter: `devin acp` concurrent same-turn prompts + cancel.

Wire facts verified against devin 3000.10.27 (/tmp probe transcripts):
- A second `session/prompt` sent while a turn runs is accepted and merged into
  the SAME turn; both request ids get their response when that turn ends.
  There is no promptId echo — correlate by JSON-RPC request id only.
- `session/cancel` resolves in-flight prompts with stopReason "cancelled" and
  the session stays usable (interrupt = cancel_and_send).
- Final text is the concatenation of `agent_message_chunk` updates only;
  `agent_thought_chunk` is observable but never part of the answer.
- `ACP_BACKEND` must be stripped from the child env (inside Devin Desktop it
  is inherited as "windsurf" and the CLI reports "Not logged in").

Honest ack ladder: `request_sent` when the JSON-RPC request is in flight;
`completed` / `cancelled` / `failed` once the request's own response resolves.
No Devin transport event proves semantic compliance, so this adapter never
claims `applied` — it reports only wire-observable lifecycle facts.
"""
from __future__ import annotations

import os
import queue
import threading
import time
import uuid
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional

from ..jsonrpc import JsonRpcProcess
from ..util import kill_process_group
from .base import AdapterEvent, BackendAdapter, DeliveryClass, SteerResult

_CANCEL_STOP_REASONS = frozenset({"cancelled", "canceled"})
_SUCCESS_STOP_REASONS = frozenset({"end_turn", "endturn"})
_INTERRUPT_WAIT_S = 30.0


def _normalize_stop_reason(value: Any) -> str:
    return str(value or "").strip().replace("-", "_").lower()


def _content_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, dict):
        if content.get("type") == "text" or "text" in content:
            return str(content.get("text") or "")
        if "content" in content:
            return _content_text(content["content"])
    if isinstance(content, list):
        return "".join(_content_text(c) for c in content)
    return ""


class DevinAdapter(BackendAdapter):
    backend_name = "devin-cli"
    auto_delivery = DeliveryClass.SAME_TURN

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rpc: Optional[JsonRpcProcess] = None
        self.session_id: Optional[str] = None
        self._events: "queue.Queue[AdapterEvent]" = queue.Queue()
        self._raw_path = Path(self.artifacts_dir) / "raw" / f"{self.agent_id or 'devin'}.jsonl"
        self._lock = threading.Lock()
        # rid -> (prompt client_id, waiter thread)
        self._in_flight: Dict[Any, Dict[str, Any]] = {}
        self._prompt_result: Dict[Any, Dict[str, Any]] = {}
        self._resolution_order: List[Any] = []
        self._initial_rid: Optional[Any] = None
        self._all_text: List[str] = []
        self._cancelled = False
        # Interrupt steers in flight between session/cancel and the successor
        # prompt: the cancelled turn resolving must not terminalize the run.
        self._pending_interrupt = 0

    def _argv(self) -> List[str]:
        cmd = [self.binary, "acp"]
        if self.model:
            cmd += ["--model", self.model]
        return cmd

    def _emit_steer_ack(self, prompt_id: str, *, status: str, evidence: str,
                        raw: Optional[Dict[str, Any]] = None) -> None:
        if not prompt_id:
            return
        payload: Dict[str, Any] = {
            "promptId": prompt_id,
            "status": status,
            "evidence": evidence,
        }
        if raw is not None:
            payload["raw"] = raw
        self._events.put(AdapterEvent(kind="steer_ack", data=f"{status}:{evidence}", raw=payload))

    # ---- wire callbacks -------------------------------------------------

    def _on_notification(self, msg: Dict[str, Any]) -> None:
        method = msg.get("method") or ""
        params = msg.get("params") or {}
        if method == "session/update":
            self._on_session_update(params if isinstance(params, dict) else {})
            return
        if method == "_cognition.ai/agent_stopped":
            cause = str(params.get("cause") or "") if isinstance(params, dict) else ""
            if cause and cause != "complete":
                self._events.put(AdapterEvent(kind="progress", data=f"agent_stopped:{cause}", raw=msg))
            else:
                self._events.put(AdapterEvent(kind="progress", data="agent_stopped", raw=msg))
            return
        self._events.put(AdapterEvent(kind="progress", data=method or "notification", raw=msg))

    def _on_session_update(self, params: Dict[str, Any]) -> None:
        update = params.get("update") or {}
        if not isinstance(update, dict):
            update = {}
        utype = update.get("sessionUpdate") or update.get("type") or ""
        if utype == "agent_message_chunk":
            text = _content_text(update.get("content"))
            if text:
                with self._lock:
                    self._all_text.append(text)
                self._events.put(AdapterEvent(kind="text", data=text,
                                              raw={"update": update, "params": params}))
            else:
                self._events.put(AdapterEvent(kind="progress", data=utype,
                                              raw={"update": update, "params": params}))
            return
        if utype == "agent_thought_chunk":
            self._events.put(AdapterEvent(kind="thought",
                                          data=_content_text(update.get("content")),
                                          raw={"update": update, "params": params}))
            return
        if utype == "tool_call":
            self._events.put(AdapterEvent(
                kind="tool",
                data=str(update.get("title") or update.get("kind") or "tool"),
                raw={"update": update, "params": params}))
            return
        self._events.put(AdapterEvent(kind="progress", data=utype or "session/update",
                                      raw={"update": update, "params": params}))

    def _on_server_request(self, msg: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        method = msg.get("method") or ""
        rid = msg.get("id")
        if method == "session/request_permission":
            options = (msg.get("params") or {}).get("options") or []
            option_id = None
            fallback = None
            for o in options:
                if not isinstance(o, dict):
                    continue
                kind = str(o.get("kind") or "")
                if kind == "allow_once":
                    option_id = str(o.get("optionId") or "allow_once")
                    break
                if kind.startswith("allow") and fallback is None:
                    fallback = str(o.get("optionId") or "")
            option_id = option_id or fallback
            if option_id is None:
                return None
            return {
                "jsonrpc": "2.0",
                "id": rid,
                "result": {"outcome": {"outcome": "selected", "optionId": option_id}},
            }
        if method == "elicitation/create":
            return {"jsonrpc": "2.0", "id": rid, "result": {"action": "cancel"}}
        return None

    # ---- lifecycle ------------------------------------------------------

    def start(self, task: str) -> None:
        self._raw_path.parent.mkdir(parents=True, exist_ok=True)
        env = dict(os.environ)
        env.pop("ACP_BACKEND", None)
        self.rpc = JsonRpcProcess(
            self._argv(),
            cwd=self.cwd,
            env=env,
            on_notification=self._on_notification,
            on_server_request=self._on_server_request,
        )
        self.rpc.set_raw_out(str(self._raw_path))
        self.rpc.start()
        self.rpc.request(
            "initialize",
            {
                "protocolVersion": 1,
                "clientCapabilities": {
                    "fs": {"readTextFile": False, "writeTextFile": False},
                    "terminal": False,
                },
                "clientInfo": {"name": "agents-consilium", "version": "1.0.0"},
            },
            timeout=60.0,
        )
        result = self.rpc.request(
            "session/new", {"cwd": self.cwd, "mcpServers": []}, timeout=60.0
        )
        self.session_id = (result or {}).get("sessionId")
        if not self.session_id:
            raise RuntimeError(f"devin session/new missing sessionId: {result}")
        # Steerable delegate is yolo: bypass so exec/permissions never block.
        try:
            self.rpc.request(
                "session/set_mode",
                {"sessionId": self.session_id, "modeId": "bypass"},
                timeout=30.0,
            )
        except Exception as e:
            self._events.put(
                AdapterEvent(kind="progress", data=f"set_mode_bypass_failed:{e}")
            )
        self._send_prompt(task, client_id="initial")

    def _send_prompt(self, text: str, *, client_id: str) -> Any:
        assert self.rpc and self.session_id
        rid, q = self.rpc.start_request(
            "session/prompt",
            {
                "sessionId": self.session_id,
                "prompt": [{"type": "text", "text": text}],
            },
        )
        with self._lock:
            self._in_flight[rid] = {"client_id": client_id}
            if self._initial_rid is None:
                self._initial_rid = rid
        t = threading.Thread(target=self._wait_prompt, args=(rid, q, client_id), daemon=True)
        t.start()
        return rid

    def _wait_prompt(self, rid: Any, q: "queue.Queue[Dict[str, Any]]", client_id: str) -> None:
        assert self.rpc
        try:
            # Poll the response queue so a dead child cannot hang the waiter
            # forever. await_response pops the pending entry on timeout, so
            # wait on the queue directly instead of looping over it.
            result: Any = None
            while True:
                try:
                    resp = q.get(timeout=1.0)
                except queue.Empty:
                    if self.rpc.poll_exit() is not None or self._cancelled:
                        self.rpc.drop_pending(rid)
                        raise RuntimeError("devin acp exited before prompt response")
                    continue
                self.rpc.drop_pending(rid)
                if "error" in resp:
                    raise RuntimeError(f"JSON-RPC error: {resp['error']}")
                result = resp.get("result")
                break
        except Exception as e:
            with self._lock:
                self._in_flight.pop(rid, None)
                self._prompt_result.setdefault(rid, {})
                self._resolution_order.append(rid)
            self._events.put(AdapterEvent(kind="error", data=f"prompt {client_id}: {e}",
                                          raw={"promptId": client_id}))
            self._emit_steer_ack(client_id, status="failed", evidence="prompt_request_error",
                                 raw={"promptId": client_id, "error": str(e)})
            self._maybe_mark_done(rid)
            return
        stop = _normalize_stop_reason(
            result.get("stopReason") if isinstance(result, dict) else ""
        )
        with self._lock:
            self._in_flight.pop(rid, None)
            self._prompt_result[rid] = result if isinstance(result, dict) else {}
            self._resolution_order.append(rid)
        if stop in _SUCCESS_STOP_REASONS:
            status, evidence = "completed", "prompt_result_end_turn"
        elif stop in _CANCEL_STOP_REASONS:
            status, evidence = "cancelled", "prompt_result_cancelled"
        else:
            status, evidence = "failed", f"prompt_result_{stop or 'missing'}"
        self._emit_steer_ack(client_id, status=status, evidence=evidence,
                             raw={"promptId": client_id, "result": result})
        self._maybe_mark_done(rid)

    def _maybe_mark_done(self, resolved_rid: Any) -> None:
        with self._lock:
            if self._done:
                return
            if self._in_flight:
                return
            if self._pending_interrupt:
                return
            if resolved_rid != self._initial_rid and self._initial_rid not in self._prompt_result:
                # The initial prompt has not resolved yet.
                return
            last_rid = self._resolution_order[-1] if self._resolution_order else resolved_rid
            last_stop = _normalize_stop_reason(
                (self._prompt_result.get(last_rid) or {}).get("stopReason")
            )
            if self._cancelled:
                exit_code, data = 130, "cancelled"
            elif last_stop in _SUCCESS_STOP_REASONS:
                exit_code, data = 0, "end_turn"
            elif last_stop in _CANCEL_STOP_REASONS:
                exit_code, data = 130, "cancelled"
            else:
                exit_code, data = 1, f"stop:{last_stop or 'missing'}"
            self._done = True
            self._exit_code = exit_code
        self._events.put(AdapterEvent(kind="done", data=data,
                                      raw={"promptId": last_rid}))

    def poll_events(self) -> Iterator[AdapterEvent]:
        if self.rpc:
            rc = self.rpc.poll_exit()
            if rc is not None and not self._done:
                with self._lock:
                    self._done = True
                    self._exit_code = 130 if self._cancelled else (rc or 1)
                    if rc != 0 and not self._error:
                        self._error = f"devin exited {rc}"
                self._events.put(AdapterEvent(kind="done", data=str(rc)))
        while True:
            try:
                yield self._events.get_nowait()
            except queue.Empty:
                break

    def _queue_class(self) -> DeliveryClass:
        return DeliveryClass.SAME_TURN

    def _interrupt_class(self) -> DeliveryClass:
        return DeliveryClass.CANCEL_AND_SEND

    def steer(self, content: str, mode: str, client_id: str) -> SteerResult:
        if not self.rpc or not self.session_id:
            return SteerResult(ok=False, delivery_class=self.auto_delivery,
                               status="rejected", error="backend not ready")
        with self._lock:
            if self._done and not self._in_flight:
                return SteerResult(ok=False, delivery_class=self.auto_delivery,
                                   status="rejected", error="backend already completed")
        try:
            dclass = self.map_mode(mode)
        except NotImplementedError as e:
            return SteerResult(ok=False, delivery_class=self.auto_delivery,
                               status="rejected", error=str(e))
        prompt_id = client_id or str(uuid.uuid4())
        if dclass == DeliveryClass.CANCEL_AND_SEND:
            with self._lock:
                self._pending_interrupt += 1
            try:
                try:
                    self.rpc.notify("session/cancel", {"sessionId": self.session_id})
                except Exception as e:
                    return SteerResult(ok=False, delivery_class=dclass, status="failed",
                                       error=f"session/cancel: {e}")
                # Wait (bounded) for in-flight prompts to resolve before sending
                # the successor — otherwise it would merge into the still-running
                # turn. _pending_interrupt keeps _maybe_mark_done from
                # terminalizing on the cancelled turn's resolution.
                deadline = time.time() + _INTERRUPT_WAIT_S
                while time.time() < deadline:
                    with self._lock:
                        if not self._in_flight:
                            break
                    time.sleep(0.05)
                try:
                    self._send_prompt(content, client_id=prompt_id)
                except Exception as e:
                    return SteerResult(ok=False, delivery_class=dclass, status="failed", error=str(e))
            finally:
                with self._lock:
                    self._pending_interrupt -= 1
        else:
            try:
                self._send_prompt(content, client_id=prompt_id)
            except Exception as e:
                return SteerResult(ok=False, delivery_class=dclass, status="failed", error=str(e))
        evidence = ("acp_cancel_then_prompt" if dclass == DeliveryClass.CANCEL_AND_SEND
                    else "acp_concurrent_prompt")
        return SteerResult(
            ok=True,
            delivery_class=dclass,
            status="request_sent",
            evidence=evidence,
            meta={"promptId": prompt_id, "client_id": client_id},
        )

    def child_pid(self) -> Optional[int]:
        return self.rpc.pid() if self.rpc else None

    def cancel(self) -> None:
        with self._lock:
            already_done = self._done
            self._cancelled = True
        if self.rpc and self.session_id:
            try:
                self.rpc.notify("session/cancel", {"sessionId": self.session_id})
            except Exception:
                pass
            pid = self.rpc.pid()
            self.rpc.terminate()
            if pid:
                kill_process_group(pid, timeout=3.0)
        with self._lock:
            if not already_done and not self._done:
                self._done = True
                self._exit_code = 130
                self._events.put(AdapterEvent(kind="done", data="cancelled"))
            else:
                self._done = True
                if self._exit_code is None:
                    self._exit_code = 130

    def final_text(self) -> str:
        with self._lock:
            return "".join(self._all_text)

    def close(self) -> None:
        self.cancel()
