"""Grok Build steerable adapter: native ACP concurrent prompt queue + sendNow.

Source-backed semantics (grok-build SOURCE_REV verified):
- `MvpAgent::prompt` takes a per-session dispatch lock only long enough to enqueue
  SessionCommand::Prompt, then drops the guard before awaiting the oneshot.
  A second concurrent ACP PromptRequest is therefore legal while the first is
  still in flight.
- Normal prompts append to the session FIFO (queue_next_turn).
- `_meta.sendNow: true` marks cancel-and-send: insert near front and cancel the
  running turn when appropriate.
- `_meta.promptId` is echoed on SessionNotification meta and on
  `x.ai/session/prompt_complete` / `_x.ai/session/prompt_complete` for durable
  attribution. Queue state arrives via `_x.ai/queue/changed` (entries[].id /
  runningPromptId).
- Do NOT hold queued prompts outside ACP until first completion.

Ack ladder (honest statuses):
- `request_sent` / `queued`: JSON-RPC request written and/or in-flight only —
  NOT "delivered". Backend-confirmed queue (`_x.ai/queue/changed` entries)
  upgrades evidence while staying `queued`.
- `applied`: promptId seen as running, on session/update meta (agent chunks),
  prompt_complete, or matching session/prompt result.
- Late acks after steer() returns are emitted as `steer_ack` events so the
  supervisor can reconcile mailbox status asynchronously.
"""
from __future__ import annotations

import queue
import threading
import time
import uuid
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple

from ..jsonrpc import JsonRpcProcess
from ..util import kill_process_group, new_id
from .base import AdapterEvent, BackendAdapter, DeliveryClass, SteerResult

# sessionUpdate values that contribute agent-visible final text.
_AGENT_MESSAGE_TYPES = frozenset(
    {
        "agent_message_chunk",
        "agentMessageChunk",
        "agent_message",
        "agentMessage",
    }
)
_AGENT_THOUGHT_TYPES = frozenset(
    {
        "agent_thought_chunk",
        "agentThoughtChunk",
        "agent_thought",
        "agentThought",
    }
)
_USER_MESSAGE_TYPES = frozenset(
    {
        "user_message_chunk",
        "userMessageChunk",
        "user_message",
        "userMessage",
    }
)


def _normalize_acp_method(method: str) -> str:
    """Map `_x.ai/foo` → `x.ai/foo` for stable matching of real wire shapes."""
    m = method or ""
    if m.startswith("_x.ai/"):
        return "x.ai/" + m[len("_x.ai/") :]
    return m


class GrokAdapter(BackendAdapter):
    backend_name = "grok-build"
    auto_delivery = DeliveryClass.QUEUE_NEXT_TURN

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rpc: Optional[JsonRpcProcess] = None
        self.session_id: Optional[str] = None
        self._events: "queue.Queue[AdapterEvent]" = queue.Queue()
        self._raw_path = Path(self.artifacts_dir) / "raw" / f"{self.agent_id or 'grok'}.jsonl"
        self._text_by_prompt: Dict[str, List[str]] = {}
        self._prompt_complete: Dict[str, Dict[str, Any]] = {}
        self._prompt_seen_meta: Dict[str, bool] = {}
        self._prompt_queue_confirmed: Set[str] = set()
        self._prompt_running: Set[str] = set()
        self._prompt_result: Dict[str, Any] = {}
        self._in_flight: Dict[str, Tuple[Any, "queue.Queue[Dict[str, Any]]"]] = {}
        self._initial_prompt_id: Optional[str] = None
        self._final_prompt_id: Optional[str] = None
        self._lock = threading.Lock()
        self._all_text: List[str] = []
        self._cancelled = False
        # Completion accounting: how many non-cancelled user prompts finished
        self._completed_prompt_ids: List[str] = []

    def _argv(self) -> List[str]:
        cmd = [self.binary, "agent", "--always-approve"]
        if self.model:
            cmd += ["--model", self.model]
        if self.effort:
            cmd += ["--effort", self.effort]
        cmd += ["stdio"]
        return cmd

    def _emit_steer_ack(
        self,
        prompt_id: str,
        *,
        status: str,
        evidence: str,
        raw: Optional[Dict[str, Any]] = None,
    ) -> None:
        if not prompt_id:
            return
        payload: Dict[str, Any] = {
            "promptId": prompt_id,
            "status": status,
            "evidence": evidence,
        }
        if raw is not None:
            payload["raw"] = raw
        self._events.put(
            AdapterEvent(
                kind="steer_ack",
                data=f"{status}:{evidence}",
                raw=payload,
            )
        )

    def _note_prompt_meta(self, prompt_id: str, *, evidence: str = "promptId_notification_meta") -> None:
        if not prompt_id:
            return
        with self._lock:
            first = not self._prompt_seen_meta.get(prompt_id)
            self._prompt_seen_meta[prompt_id] = True
        if first:
            self._emit_steer_ack(prompt_id, status="applied", evidence=evidence)

    def _on_queue_changed(self, params: Dict[str, Any]) -> None:
        """Backend FIFO observability: entries[].id / runningPromptId correlate to promptId."""
        entries = params.get("entries") or []
        if isinstance(entries, list):
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                eid = entry.get("id") or ""
                if not eid:
                    continue
                with self._lock:
                    first = eid not in self._prompt_queue_confirmed
                    self._prompt_queue_confirmed.add(eid)
                if first:
                    self._emit_steer_ack(
                        eid,
                        status="queued",
                        evidence="backend_queue_entry",
                        raw={"entry": entry, "params": params},
                    )
        running = params.get("runningPromptId") or ""
        if running:
            with self._lock:
                first_run = running not in self._prompt_running
                self._prompt_running.add(running)
                # Running is stronger confirmation than mere queue membership.
                self._prompt_seen_meta[running] = True
            if first_run:
                self._emit_steer_ack(
                    running,
                    status="applied",
                    evidence="running_prompt_id",
                    raw={"runningPromptId": running, "params": params},
                )
        self._events.put(
            AdapterEvent(kind="progress", data="queue/changed", raw=params)
        )

    def _on_prompt_complete(self, params: Dict[str, Any]) -> None:
        pid = params.get("promptId") or ""
        with self._lock:
            self._prompt_complete[pid] = dict(params)
            stop = params.get("stopReason") or ""
            if stop != "Cancelled":
                self._completed_prompt_ids.append(pid)
            if pid:
                self._prompt_seen_meta[pid] = True
        self._events.put(
            AdapterEvent(
                kind="prompt_complete",
                data=str(params.get("stopReason") or ""),
                raw=params,
            )
        )
        if pid:
            self._emit_steer_ack(
                pid,
                status="applied",
                evidence="prompt_complete",
                raw=params,
            )

    def _on_notification(self, msg: Dict[str, Any]) -> None:
        method = msg.get("method") or ""
        norm = _normalize_acp_method(method)
        params = msg.get("params") or {}
        if norm == "x.ai/session/prompt_complete":
            self._on_prompt_complete(params if isinstance(params, dict) else {})
            return
        if norm == "x.ai/queue/changed":
            self._on_queue_changed(params if isinstance(params, dict) else {})
            return
        if method == "session/update" or norm == "session/update":
            self._on_session_update(params if isinstance(params, dict) else {})
            return
        if method == "session/request_permission":
            return
        self._events.put(AdapterEvent(kind="progress", data=method or norm, raw=msg))

    def _on_session_update(self, params: Dict[str, Any]) -> None:
        update = params.get("update") or {}
        if not isinstance(update, dict):
            update = {}
        meta = params.get("_meta") or params.get("meta") or {}
        if not isinstance(meta, dict):
            meta = {}
        # Some builds nest _meta under update; prefer params-level, fall back.
        nested_meta = update.get("_meta") if isinstance(update.get("_meta"), dict) else {}
        prompt_id = meta.get("promptId") or nested_meta.get("promptId") or ""
        utype = update.get("sessionUpdate") or update.get("type") or ""

        # --- Strict type split: only agent_message* enters final text ---
        if utype in _AGENT_MESSAGE_TYPES or "agentMessageChunk" in update:
            if prompt_id:
                self._note_prompt_meta(prompt_id)
            content = update.get("agentMessageChunk") or update.get("content")
            if content is None and "agentMessageChunk" in update:
                content = update.get("agentMessageChunk")
            text = self._content_text(content) if content is not None else ""
            if not text:
                text = self._extract_loose_text(update)
            if text:
                with self._lock:
                    self._all_text.append(text)
                    if prompt_id:
                        self._text_by_prompt.setdefault(prompt_id, []).append(text)
                self._events.put(
                    AdapterEvent(
                        kind="text",
                        data=text,
                        raw={"promptId": prompt_id, "update": update, "params": params},
                    )
                )
            else:
                self._events.put(
                    AdapterEvent(
                        kind="progress",
                        data=utype or "agent_message_chunk",
                        raw={"promptId": prompt_id, "update": update, "params": params},
                    )
                )
            return

        if utype in _AGENT_THOUGHT_TYPES or "agentThoughtChunk" in update:
            if prompt_id:
                self._note_prompt_meta(prompt_id, evidence="promptId_notification_meta")
            content = update.get("agentThoughtChunk") or update.get("content")
            text = self._content_text(content) if content is not None else ""
            if not text:
                text = self._extract_loose_text(update)
            # Observable, never final.
            self._events.put(
                AdapterEvent(
                    kind="thought",
                    data=text,
                    raw={"promptId": prompt_id, "update": update, "params": params},
                )
            )
            return

        if utype in _USER_MESSAGE_TYPES or "userMessageChunk" in update:
            # Replay / progress only — not final output. promptId here is queue
            # echo on some fakes; do not treat as applied (real wire often omits it).
            content = update.get("userMessageChunk") or update.get("content")
            text = self._content_text(content) if content is not None else ""
            if not text:
                text = self._extract_loose_text(update)
            self._events.put(
                AdapterEvent(
                    kind="user_replay",
                    data=text,
                    raw={"promptId": prompt_id, "update": update, "params": params},
                )
            )
            return

        # Other session updates (tool_call, turn_completed, …): progress only.
        # If a promptId is present on non-message updates, still correlate applied
        # (backend has associated this notification with the prompt).
        if prompt_id and utype not in (
            "available_commands_update",
            "model_changed",
            "session_summary_generated",
        ):
            # Tool calls / turn markers with promptId count as confirmation.
            if utype in (
                "tool_call",
                "tool_call_update",
                "tool_call_delta_chunk",
                "turn_completed",
                "turn_started",
                "hook_execution",
                "pending_interaction",
                "interaction_resolved",
            ):
                self._note_prompt_meta(prompt_id)

        self._events.put(
            AdapterEvent(
                kind="progress",
                data=utype or "session/update",
                raw={"promptId": prompt_id, "update": update, "params": params},
            )
        )

    def _extract_loose_text(self, update: Dict[str, Any]) -> str:
        for key in ("text", "message", "data"):
            if isinstance(update.get(key), str):
                return update[key]
        content_block = update.get("content")
        if isinstance(content_block, dict):
            if content_block.get("type") in (None, "text") and "text" in content_block:
                return str(content_block.get("text") or "")
        return ""

    def _content_text(self, content: Any) -> str:
        if isinstance(content, str):
            return content
        if isinstance(content, dict):
            if content.get("type") == "text" or "text" in content:
                return str(content.get("text") or "")
            if "content" in content:
                return self._content_text(content["content"])
        if isinstance(content, list):
            return "".join(self._content_text(c) for c in content)
        return ""

    def _on_server_request(self, msg: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        method = msg.get("method") or ""
        rid = msg.get("id")
        if method == "session/request_permission":
            params = msg.get("params") or {}
            options = params.get("options") or []
            option_id = None
            for o in options:
                kind = (o.get("kind") or "").lower()
                if "allow" in kind:
                    option_id = o.get("optionId") or o.get("option_id")
                    break
            if option_id is None and options:
                option_id = options[0].get("optionId") or options[0].get("option_id")
            return {
                "jsonrpc": "2.0",
                "id": rid,
                "result": {
                    "outcome": {
                        "outcome": "selected",
                        "optionId": option_id or "allow",
                    }
                },
            }
        if method in ("fs/read_text_file", "fs/write_text_file"):
            return {
                "jsonrpc": "2.0",
                "id": rid,
                "error": {"code": -32601, "message": "fs not provided"},
            }
        return None

    def start(self, task: str) -> None:
        self._raw_path.parent.mkdir(parents=True, exist_ok=True)
        self.rpc = JsonRpcProcess(
            self._argv(),
            cwd=self.cwd,
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
                "clientInfo": {
                    "name": "agents-consilium-steer",
                    "version": "1.0.0",
                },
                "_meta": {
                    "startupHints": {
                        "nonInteractive": True,
                        "skipGitStatus": True,
                        "skipProjectLayout": True,
                    },
                    "clientType": "agents-consilium",
                    "clientVersion": "1.0.0",
                },
            },
            timeout=60.0,
        )
        new_params: Dict[str, Any] = {
            "cwd": self.cwd,
            "mcpServers": [],
        }
        if self.model:
            new_params["_meta"] = {"modelId": self.model}
        result = self.rpc.request("session/new", new_params, timeout=60.0)
        self.session_id = (result or {}).get("sessionId") or (result or {}).get("session_id")
        if not self.session_id:
            raise RuntimeError(f"grok session/new missing sessionId: {result}")
        self._initial_prompt_id = new_id("prompt_")
        self._final_prompt_id = self._initial_prompt_id
        self._send_prompt(task, prompt_id=self._initial_prompt_id, send_now=False, wait=False)

    def _send_prompt(
        self,
        text: str,
        *,
        prompt_id: str,
        send_now: bool,
        wait: bool,
        wait_timeout: Optional[float] = None,
    ) -> Any:
        assert self.rpc and self.session_id
        params: Dict[str, Any] = {
            "sessionId": self.session_id,
            "prompt": [{"type": "text", "text": text}],
            "_meta": {
                "promptId": prompt_id,
                "sendNow": bool(send_now),
            },
        }
        rid, q = self.rpc.start_request("session/prompt", params)
        with self._lock:
            self._in_flight[prompt_id] = (rid, q)
        if not wait:
            t = threading.Thread(
                target=self._wait_prompt,
                args=(prompt_id, rid, q),
                kwargs={"timeout": wait_timeout},
                daemon=True,
            )
            t.start()
            return None
        return self._wait_prompt(prompt_id, rid, q, timeout=wait_timeout)

    def _wait_prompt(
        self,
        prompt_id: str,
        rid: Any,
        q: "queue.Queue[Dict[str, Any]]",
        timeout: Optional[float] = None,
    ) -> Any:
        assert self.rpc
        try:
            result = self.rpc.await_response(
                rid, q, timeout=timeout, method="session/prompt"
            )
            with self._lock:
                self._prompt_result[prompt_id] = result
                self._prompt_seen_meta[prompt_id] = True
            self._emit_steer_ack(
                prompt_id,
                status="applied",
                evidence="prompt_result",
                raw={"promptId": prompt_id, "result": result},
            )
            return result
        except Exception as e:
            with self._lock:
                self._in_flight.pop(prompt_id, None)
            self._events.put(
                AdapterEvent(
                    kind="error",
                    data=f"prompt {prompt_id}: {e}",
                    raw={"promptId": prompt_id},
                )
            )
            return None
        finally:
            with self._lock:
                self._in_flight.pop(prompt_id, None)
            self._maybe_mark_done(prompt_id)

    def _maybe_mark_done(self, completed_prompt_id: str) -> None:
        """
        Mark the steerable run done when no prompts remain in-flight and the
        latest non-cancelled completion belongs to the final prompt lineage.
        Multiple concurrent in-flight prompts: only finish when all settled.
        """
        with self._lock:
            if self._in_flight:
                return
            if self._cancelled:
                self._done = True
                self._exit_code = 130
                return
            pc = self._prompt_complete.get(completed_prompt_id) or {}
            stop = pc.get("stopReason") or ""
            if stop == "Cancelled":
                # If everything cancelled and nothing left, still may wait
                if not self._completed_prompt_ids and not self._all_text:
                    return
                # Prefer latest non-cancelled completion
                if self._completed_prompt_ids:
                    completed_prompt_id = self._completed_prompt_ids[-1]
                    pc = self._prompt_complete.get(completed_prompt_id) or {}
                    stop = pc.get("stopReason") or ""
                else:
                    return
            if completed_prompt_id == self._final_prompt_id or (
                self._final_prompt_id in self._prompt_complete
                or self._final_prompt_id in self._prompt_result
            ):
                if self._all_text or stop in (
                    "end_turn",
                    "EndTurn",
                    "endTurn",
                    "max_tokens",
                    "MaxTokens",
                    "",
                ):
                    # Only terminal if final prompt itself completed (not just any)
                    final = self._final_prompt_id
                    final_done = (
                        final in self._prompt_complete
                        or final in self._prompt_result
                        or completed_prompt_id == final
                    )
                    if final_done and not self._in_flight:
                        self._done = True
                        self._exit_code = 0
                        self._events.put(
                            AdapterEvent(
                                kind="done",
                                data=stop or "end",
                                raw=pc or {"promptId": completed_prompt_id},
                            )
                        )

    def poll_events(self) -> Iterator[AdapterEvent]:
        if self.rpc:
            for n in self.rpc.drain_notifications():
                if n.get("method") == "_non_json":
                    self._events.put(AdapterEvent(kind="raw", data=str(n.get("params"))))
            rc = self.rpc.poll_exit()
            if rc is not None and not self._done:
                self._done = True
                self._exit_code = rc
                if rc != 0:
                    self._error = f"grok exited {rc}"
                self._events.put(AdapterEvent(kind="done", data=str(rc)))
        while True:
            try:
                yield self._events.get_nowait()
            except queue.Empty:
                break

    def _queue_class(self) -> DeliveryClass:
        return DeliveryClass.QUEUE_NEXT_TURN

    def _interrupt_class(self) -> DeliveryClass:
        return DeliveryClass.CANCEL_AND_SEND

    def _applied_for(self, prompt_id: str) -> Optional[str]:
        """Return evidence string if backend confirmed this promptId as applied."""
        with self._lock:
            if prompt_id in self._prompt_complete:
                return "prompt_complete"
            if prompt_id in self._prompt_result:
                return "prompt_result"
            if prompt_id in self._prompt_running:
                return "running_prompt_id"
            if self._prompt_seen_meta.get(prompt_id):
                return "promptId_notification_meta"
        return None

    def _queue_confirmed_for(self, prompt_id: str) -> Optional[str]:
        with self._lock:
            if prompt_id in self._prompt_queue_confirmed:
                return "backend_queue_entry"
        return None

    def steer(self, content: str, mode: str, client_id: str) -> SteerResult:
        if not self.rpc or not self.session_id:
            return SteerResult(
                ok=False,
                delivery_class=self.auto_delivery,
                status="rejected",
                error="backend not ready",
            )
        # After adapter is done with nothing in-flight, reject every mode
        # (including interrupt) — no false accept during final drain.
        if self._done:
            with self._lock:
                if not self._in_flight:
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
        send_now = dclass == DeliveryClass.CANCEL_AND_SEND or mode == "interrupt"
        # Stable attribution: prefer client_id when UUID-shaped, else new UUID,
        # but always store client_id in meta for correlation.
        prompt_id = client_id if client_id and _looks_like_uuid(client_id) else str(uuid.uuid4())
        self._final_prompt_id = prompt_id
        try:
            # Concurrent send — do not wait for prior prompt JSON-RPC response
            self._send_prompt(content, prompt_id=prompt_id, send_now=send_now, wait=False)
        except Exception as e:
            return SteerResult(
                ok=False,
                delivery_class=dclass,
                status="failed",
                error=str(e),
            )
        # Wait briefly for backend confirmation (promptId on notification / complete)
        deadline = time.time() + 5.0
        while time.time() < deadline:
            list(self.poll_events())
            evidence = self._applied_for(prompt_id)
            if evidence:
                return SteerResult(
                    ok=True,
                    delivery_class=dclass,
                    status="applied",
                    evidence=evidence,
                    meta={
                        "promptId": prompt_id,
                        "sendNow": send_now,
                        "client_id": client_id,
                    },
                )
            time.sleep(0.05)

        with self._lock:
            in_flight = prompt_id in self._in_flight
        # JSON-RPC write / in-flight is NOT "delivered" — only request_sent/queued.
        q_ev = self._queue_confirmed_for(prompt_id)
        if in_flight or q_ev:
            status = "queued" if not send_now else "request_sent"
            return SteerResult(
                ok=True,
                delivery_class=dclass,
                status=status,
                evidence=q_ev or "concurrent_prompt_request_in_flight",
                meta={
                    "promptId": prompt_id,
                    "sendNow": send_now,
                    "client_id": client_id,
                },
            )
        evidence = self._applied_for(prompt_id)
        if evidence:
            return SteerResult(
                ok=True,
                delivery_class=dclass,
                status="applied",
                evidence=evidence,
                meta={
                    "promptId": prompt_id,
                    "sendNow": send_now,
                    "client_id": client_id,
                },
            )
        return SteerResult(
            ok=True,
            delivery_class=dclass,
            status="request_sent",
            evidence="prompt_request_written",
            meta={
                "promptId": prompt_id,
                "sendNow": send_now,
                "client_id": client_id,
            },
        )

    def child_pid(self) -> Optional[int]:
        return self.rpc.pid() if self.rpc else None

    def cancel(self) -> None:
        self._cancelled = True
        if self.rpc and self.session_id:
            try:
                try:
                    self.rpc.request(
                        "session/cancel",
                        {"sessionId": self.session_id},
                        timeout=3.0,
                    )
                except Exception:
                    self.rpc.notify("session/cancel", {"sessionId": self.session_id})
            except Exception:
                pass
            pid = self.rpc.pid()
            self.rpc.terminate()
            if pid:
                kill_process_group(pid, timeout=3.0)
        self._done = True

    def final_text(self) -> str:
        with self._lock:
            if self._final_prompt_id and self._final_prompt_id in self._text_by_prompt:
                return "".join(self._text_by_prompt[self._final_prompt_id])
            if self._all_text:
                return "".join(self._all_text)
        return "".join(self._final_parts)

    def close(self) -> None:
        self.cancel()


def _looks_like_uuid(s: str) -> bool:
    try:
        uuid.UUID(s)
        return True
    except Exception:
        return False
