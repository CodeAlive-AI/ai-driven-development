"""Codex app-server steerable adapter: turn/steer with expectedTurnId.

Field names verified against installed `codex app-server generate-json-schema`:
- thread/start: cwd, model, sandbox, approvalPolicy, ephemeral, ...
- turn/start: threadId (req), input (req), model, approvalPolicy, cwd, effort,
  clientUserMessageId, ...
- turn/steer: threadId, expectedTurnId, input (req), clientUserMessageId
- turn/interrupt: threadId, turnId (req)
"""
from __future__ import annotations

import queue
import threading
import time
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional

from ..jsonrpc import JsonRpcProcess
from ..util import kill_process_group
from .base import AdapterEvent, BackendAdapter, DeliveryClass, SteerResult


# Bounded local protocol handshake timeout (not a global run timeout).
INTERRUPT_ACK_TIMEOUT = 15.0


class CodexAdapter(BackendAdapter):
    backend_name = "codex-cli"
    auto_delivery = DeliveryClass.SAME_TURN

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rpc: Optional[JsonRpcProcess] = None
        self._events: "queue.Queue[AdapterEvent]" = queue.Queue()
        self._thread_id: Optional[str] = None
        self._active_turn_id: Optional[str] = None
        self._raw_path = Path(self.artifacts_dir) / "raw" / f"{self.agent_id or 'codex'}.jsonl"
        # Final answer only from a natural completed turn (never interrupted).
        self._result_text: Optional[str] = None
        # Per-turn streamed deltas (reset on each replacement turn).
        self._text_parts: List[str] = []
        # Per-turn full item text captured from item/completed (not mixed with deltas).
        self._item_text_parts: List[str] = []
        self._pending_user_ids: Dict[str, bool] = {}
        self._lock = threading.Lock()
        self._cancelled = False
        # turn_id -> status for completed turns (protocol-ack tracking)
        self._completed_turns: Dict[str, str] = {}
        self._completed_cv = threading.Condition(self._lock)

    def _reset_turn_text_buffers(self) -> None:
        """Clear per-turn text so a replacement turn cannot inherit partial OLD."""
        self._text_parts = []
        self._item_text_parts = []
        # Never keep a frozen partial from an interrupted/cancelled turn.
        self._result_text = None

    def _argv(self) -> List[str]:
        # YOLO via config overrides on app-server (no sandbox, never approve)
        return [
            self.binary,
            "app-server",
            "--stdio",
            "-c",
            "sandbox_mode=\"danger-full-access\"",
            "-c",
            "approval_policy=\"never\"",
        ]

    def _on_notification(self, msg: Dict[str, Any]) -> None:
        method = msg.get("method") or ""
        params = msg.get("params") or {}
        if method == "turn/started":
            turn = params.get("turn") or {}
            tid = turn.get("id")
            if tid:
                with self._lock:
                    self._active_turn_id = tid
                    # New turn replaces any partial text from a prior interrupted turn.
                    self._reset_turn_text_buffers()
            self._events.put(AdapterEvent(kind="turn_started", data=str(tid or ""), raw=msg))
            return
        if method == "turn/completed":
            turn = params.get("turn") or {}
            status = turn.get("status") or ""
            tid = turn.get("id")
            with self._completed_cv:
                if tid:
                    self._completed_turns[str(tid)] = str(status)
                if tid and tid == self._active_turn_id:
                    self._active_turn_id = None
                self._completed_cv.notify_all()
            self._events.put(
                AdapterEvent(kind="turn_completed", data=str(status), raw=msg)
            )
            # Collect completed-turn items (may include full agentMessage).
            # Do NOT also re-append streamed deltas — single source of truth below.
            item_texts: List[str] = []
            for item in turn.get("items") or []:
                if not isinstance(item, dict):
                    continue
                # User echo for clientId tracking (no final-text contribution).
                self._ingest_item(item, record_agent_text=False)
                extracted = self._extract_agent_text(item)
                if extracted:
                    item_texts.append(extracted)

            if status == "completed":
                # Prefer completed turn items when present; else streamed deltas only.
                # Never concatenate deltas + full item (would double the answer).
                if item_texts:
                    self._result_text = "".join(item_texts)
                elif self._item_text_parts:
                    self._result_text = "".join(self._item_text_parts)
                elif self._text_parts:
                    self._result_text = "".join(self._text_parts)
                self._done = True
                self._exit_code = 0
                self._events.put(AdapterEvent(kind="done", data="completed", raw=msg))
            elif status in ("interrupted", "cancelled"):
                # Do not freeze partial OLD into _result_text. Replacement turn
                # will reset buffers on turn/started / before turn/start.
                if status == "cancelled" and self._cancelled:
                    self._done = True
                    self._exit_code = 130
                # else: interrupt path continues with a new turn
            elif status == "failed":
                self._done = True
                self._exit_code = 1
                self._events.put(AdapterEvent(kind="error", data="turn_failed", raw=msg))
            return
        if method in ("item/completed", "item/agentMessage/delta", "item/agentMessage/completed"):
            item = params.get("item") or params
            delta = params.get("delta")
            if delta and isinstance(delta, str):
                self._text_parts.append(delta)
                self._events.put(AdapterEvent(kind="text", data=delta, raw=msg))
            else:
                # Full item events: track item text separately from deltas.
                self._ingest_item(item if isinstance(item, dict) else {}, record_agent_text=True)
            return
        if method == "error":
            self._error = str(params)
            self._events.put(AdapterEvent(kind="error", data=self._error, raw=msg))
            return
        self._events.put(AdapterEvent(kind="progress", data=method, raw=msg))

    def _extract_agent_text(self, item: Dict[str, Any]) -> str:
        if not item:
            return ""
        typ = item.get("type") or item.get("itemType") or ""
        if typ in ("userMessage", "user_message"):
            return ""
        if item.get("role") not in (None, "assistant"):
            return ""
        if typ and typ not in ("agentMessage", "agent_message", "message"):
            return ""
        text = item.get("text") or item.get("content") or ""
        if isinstance(text, list):
            parts = []
            for c in text:
                if isinstance(c, dict) and c.get("text"):
                    parts.append(c["text"])
                elif isinstance(c, str):
                    parts.append(c)
            text = "".join(parts)
        return str(text) if text else ""

    def _ingest_item(self, item: Dict[str, Any], *, record_agent_text: bool = True) -> None:
        if not item:
            return
        typ = item.get("type") or item.get("itemType") or ""
        # user message with clientId echo
        client_id = item.get("clientId") or item.get("clientUserMessageId")
        if client_id and client_id in self._pending_user_ids:
            self._pending_user_ids[client_id] = True
            self._events.put(
                AdapterEvent(kind="user_replay", data=str(client_id), raw=item)
            )
        if not record_agent_text:
            return
        text = self._extract_agent_text(item)
        if text:
            # Store on the item channel only (not _text_parts) so completed can
            # choose items XOR deltas without doubling.
            self._item_text_parts.append(text)
            self._events.put(AdapterEvent(kind="text", data=text, raw=item))

    def _on_server_request(self, msg: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        # Auto-approve any approval requests (YOLO)
        method = msg.get("method") or ""
        rid = msg.get("id")
        if "approval" in method.lower() or method.endswith("Approval"):
            return {
                "jsonrpc": "2.0",
                "id": rid,
                "result": {"decision": "accept", "approved": True},
            }
        # Best-effort accept
        if method.startswith("item/") or "request" in method.lower():
            return {"jsonrpc": "2.0", "id": rid, "result": {}}
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
        # initialize
        self.rpc.request(
            "initialize",
            {
                "clientInfo": {
                    "name": "agents-consilium-steer",
                    "version": "1.0.0",
                }
            },
            timeout=60.0,
        )
        # thread/start with YOLO sandbox (schema: ThreadStartParams)
        thread_params: Dict[str, Any] = {
            "cwd": self.cwd,
            "model": self.model,
            "sandbox": "danger-full-access",
            "approvalPolicy": "never",
            "ephemeral": True,
        }
        result = self.rpc.request("thread/start", thread_params, timeout=60.0)
        thread = (result or {}).get("thread") or result or {}
        self._thread_id = thread.get("id") or (result or {}).get("threadId")
        if not self._thread_id:
            raise RuntimeError(f"codex thread/start missing thread id: {result}")
        # turn/start with initial task (schema: TurnStartParams — threadId + input required)
        turn_params: Dict[str, Any] = {
            "threadId": self._thread_id,
            "input": [{"type": "text", "text": task}],
            "model": self.model,
            "approvalPolicy": "never",
            "cwd": self.cwd,
        }
        if self.effort:
            turn_params["effort"] = self.effort
        turn_result = self.rpc.request("turn/start", turn_params, timeout=60.0)
        turn = (turn_result or {}).get("turn") or {}
        tid = turn.get("id") or (turn_result or {}).get("turnId")
        if tid:
            with self._lock:
                self._active_turn_id = tid
            self._events.put(AdapterEvent(kind="turn_started", data=str(tid), raw=turn_result))

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
                    self._error = f"codex exited {rc}"
                self._events.put(AdapterEvent(kind="done", data=str(rc)))
        while True:
            try:
                yield self._events.get_nowait()
            except queue.Empty:
                break

    def _queue_class(self) -> DeliveryClass:
        return DeliveryClass.SAME_TURN

    def _interrupt_class(self) -> DeliveryClass:
        return DeliveryClass.ABORT_AND_PROMPT

    def _wait_turn_completed(self, turn_id: str, timeout: float) -> Optional[str]:
        """Wait for turn/completed for a specific turn id. Rejects stale/other acks."""
        deadline = time.time() + timeout
        with self._completed_cv:
            while time.time() < deadline:
                status = self._completed_turns.get(turn_id)
                if status is not None:
                    return status
                remaining = deadline - time.time()
                if remaining <= 0:
                    break
                self._completed_cv.wait(timeout=min(0.2, remaining))
        return None

    def steer(self, content: str, mode: str, client_id: str) -> SteerResult:
        if self._done or not self.rpc or not self._thread_id:
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
            return self._interrupt_and_prompt(content, client_id)

        with self._lock:
            expected = self._active_turn_id
        if not expected:
            return SteerResult(
                ok=False,
                delivery_class=dclass,
                status="rejected",
                error="no active turn for turn/steer (stale or idle)",
                evidence="missing_expectedTurnId",
            )
        self._pending_user_ids[client_id] = False
        params = {
            "threadId": self._thread_id,
            "expectedTurnId": expected,
            "clientUserMessageId": client_id,
            "input": [{"type": "text", "text": content}],
        }
        try:
            result = self.rpc.request("turn/steer", params, timeout=30.0)
        except RuntimeError as e:
            err = str(e)
            if "expectedTurnId" in err or "active turn" in err.lower() or "stale" in err.lower():
                return SteerResult(
                    ok=False,
                    delivery_class=dclass,
                    status="rejected",
                    error=f"stale expectedTurnId: {err}",
                    evidence="stale_turn_id",
                )
            if "not steerable" in err.lower() or "activeTurnNotSteerable" in err:
                return SteerResult(
                    ok=False,
                    delivery_class=dclass,
                    status="rejected",
                    error=err,
                    evidence="active_turn_not_steerable",
                )
            return SteerResult(
                ok=False,
                delivery_class=dclass,
                status="failed",
                error=err,
            )
        except Exception as e:
            return SteerResult(
                ok=False,
                delivery_class=dclass,
                status="failed",
                error=str(e),
            )
        turn_id = (result or {}).get("turnId") or expected
        # Wait briefly for user item echo with clientId
        deadline = time.time() + 3.0
        while time.time() < deadline:
            list(self.poll_events())
            if self._pending_user_ids.get(client_id):
                return SteerResult(
                    ok=True,
                    delivery_class=dclass,
                    status="applied",
                    evidence="turn_steer_clientUserMessageId",
                    meta={"turnId": turn_id},
                )
            time.sleep(0.05)
        return SteerResult(
            ok=True,
            delivery_class=dclass,
            status="request_sent",
            evidence="turn_steer_rpc_ok",
            meta={"turnId": turn_id, "result": result},
        )

    def _interrupt_and_prompt(self, content: str, client_id: str) -> SteerResult:
        """
        Interrupt handshake:
          1) turn/interrupt for the active turn
          2) wait for turn/completed of *that* turn (bounded protocol-ack wait)
          3) only then turn/start with the new content
        Do not accept a completed notification for a different turn as the ack.
        """
        assert self.rpc and self._thread_id
        with self._lock:
            turn_id = self._active_turn_id
            # Snapshot completed set so we only accept *new* acks for this turn
            already = set(self._completed_turns.keys())

        if turn_id:
            try:
                self.rpc.request(
                    "turn/interrupt",
                    {"threadId": self._thread_id, "turnId": turn_id},
                    timeout=15.0,
                )
            except Exception as e:
                return SteerResult(
                    ok=False,
                    delivery_class=DeliveryClass.ABORT_AND_PROMPT,
                    status="failed",
                    error=f"turn/interrupt failed: {e}",
                    evidence="interrupt_rpc_failed",
                )
            # Drain events while waiting so notifications are processed
            deadline = time.time() + INTERRUPT_ACK_TIMEOUT
            status = None
            while time.time() < deadline:
                list(self.poll_events())
                with self._lock:
                    status = self._completed_turns.get(turn_id)
                if status is not None:
                    # Only accept if this is the turn we interrupted (not stale)
                    if turn_id not in already or status in (
                        "interrupted",
                        "cancelled",
                        "completed",
                        "failed",
                    ):
                        break
                time.sleep(0.05)
            if status is None:
                return SteerResult(
                    ok=False,
                    delivery_class=DeliveryClass.ABORT_AND_PROMPT,
                    status="failed",
                    error=(
                        f"protocol-ack timeout waiting for turn/completed of "
                        f"interrupted turn {turn_id} (within {INTERRUPT_ACK_TIMEOUT}s)"
                    ),
                    evidence="interrupt_ack_timeout",
                    meta={"interruptedTurnId": turn_id},
                )
            # Do not start a new turn if the old one completed successfully as
            # the natural end of the run (race: interrupt after natural complete).
            if status == "completed" and self._done:
                return SteerResult(
                    ok=False,
                    delivery_class=DeliveryClass.ABORT_AND_PROMPT,
                    status="rejected",
                    error="run already completed before interrupt could restart",
                    evidence="stale_interrupt_after_complete",
                    meta={"interruptedTurnId": turn_id, "status": status},
                )

        self._pending_user_ids[client_id] = False
        # Clear done if we interrupted a non-completed turn so the new turn can run
        if self._done and not self._cancelled:
            # Natural completion already won — reject
            return SteerResult(
                ok=False,
                delivery_class=DeliveryClass.ABORT_AND_PROMPT,
                status="rejected",
                error="backend already completed",
            )
        # New turn after interrupt is a continuation of the same steerable run only
        # when the prior turn was interrupted (not natural completed).
        self._done = False
        # Drop partial OLD text before replacement turn (turn/started also resets).
        self._reset_turn_text_buffers()
        params: Dict[str, Any] = {
            "threadId": self._thread_id,
            "input": [{"type": "text", "text": content}],
            "clientUserMessageId": client_id,
            "approvalPolicy": "never",
        }
        try:
            result = self.rpc.request("turn/start", params, timeout=30.0)
        except Exception as e:
            return SteerResult(
                ok=False,
                delivery_class=DeliveryClass.ABORT_AND_PROMPT,
                status="failed",
                error=str(e),
            )
        turn = (result or {}).get("turn") or {}
        tid = turn.get("id")
        if tid:
            with self._lock:
                self._active_turn_id = tid
        return SteerResult(
            ok=True,
            delivery_class=DeliveryClass.ABORT_AND_PROMPT,
            status="request_sent",
            evidence="turn_interrupt_ack_then_start",
            meta={
                "turnId": tid,
                "interruptedTurnId": turn_id,
                "interruptStatus": status if turn_id else None,
            },
        )

    def child_pid(self) -> Optional[int]:
        return self.rpc.pid() if self.rpc else None

    def cancel(self) -> None:
        self._cancelled = True
        if self.rpc:
            with self._lock:
                turn_id = self._active_turn_id
            if turn_id and self._thread_id:
                try:
                    self.rpc.request(
                        "turn/interrupt",
                        {"threadId": self._thread_id, "turnId": turn_id},
                        timeout=5.0,
                    )
                except Exception:
                    pass
            pid = self.rpc.pid()
            self.rpc.terminate()
            if pid:
                kill_process_group(pid, timeout=3.0)
        self._done = True

    def final_text(self) -> str:
        if self._result_text is not None:
            return self._result_text
        return "".join(self._text_parts) or "".join(self._final_parts)

    def close(self) -> None:
        self.cancel()
