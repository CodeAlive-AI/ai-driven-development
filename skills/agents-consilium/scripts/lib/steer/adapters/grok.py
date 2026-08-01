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
- `running`: promptId seen as running or on an attributed agent/tool update.
- `completed`: the prompt turn ended without a cancellation/error stop reason.
- `cancelled`: a turn that had started was cancelled.
- `dropped`: a cancelled JSON-RPC result for a prompt that was never observed
  running (Grok Build's RemovedFromQueue / combined-follower path).
- `failed`: prompt_complete/result reported error or rate_limit.

No Grok transport event can prove semantic compliance, so this adapter never
claims `applied`. It reports only wire-observable lifecycle facts.
- Late acks after steer() returns are emitted as `steer_ack` events so the
  supervisor can reconcile mailbox status asynchronously.
"""
from __future__ import annotations

import queue
import threading
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

_CANCEL_STOP_REASONS = frozenset({"cancelled", "canceled"})
_FAIL_STOP_REASONS = frozenset({"error", "rate_limit", "ratelimit"})
_SUCCESS_STOP_REASONS = frozenset({"end_turn", "endturn"})
_INCOMPLETE_STOP_REASONS = frozenset({"max_tokens", "maxtokens"})


def _normalize_stop_reason(value: Any) -> str:
    return str(value or "").strip().replace("-", "_").lower()


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
        self._prompt_content: Dict[str, str] = {}
        self._prompt_merged_into: Dict[str, str] = {}
        self._prompt_cancelled_pending: Dict[str, int] = {}
        self._queue_change_seq = 0
        self._current_running_prompt_id: Optional[str] = None
        self._superseded_by: Dict[str, str] = {}
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
            self._emit_steer_ack(prompt_id, status="running", evidence=evidence)

    def _on_queue_changed(self, params: Dict[str, Any]) -> None:
        """Backend FIFO observability: entries[].id / runningPromptId correlate to promptId."""
        with self._lock:
            self._queue_change_seq += 1
            queue_change_seq = self._queue_change_seq
        entries = params.get("entries") or []
        entry_ids: Set[str] = set()
        if isinstance(entries, list):
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                eid = entry.get("id") or ""
                if not eid:
                    continue
                entry_ids.add(eid)
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
                self._current_running_prompt_id = running
                first_run = running not in self._prompt_running
                self._prompt_running.add(running)
                # Running is stronger confirmation than mere queue membership.
                self._prompt_seen_meta[running] = True
            if first_run:
                self._emit_steer_ack(
                    running,
                    status="running",
                    evidence="running_prompt_id",
                    raw={"runningPromptId": running, "params": params},
                )
            combined = params.get("runningCombinedTexts") or []
            if isinstance(combined, list) and len(combined) >= 2:
                combined_texts = [str(x) for x in combined]
                with self._lock:
                    candidates: Dict[str, List[str]] = {}
                    for candidate, text in self._prompt_content.items():
                        if (
                            candidate != running
                            and candidate in self._prompt_queue_confirmed
                            and candidate not in self._prompt_complete
                            and (
                                candidate not in self._prompt_result
                                or candidate in self._prompt_cancelled_pending
                            )
                            and text in combined_texts
                        ):
                            candidates.setdefault(text, []).append(candidate)
                    merged = [ids[0] for ids in candidates.values() if len(ids) == 1]
                    fresh = [pid for pid in merged if pid not in self._prompt_merged_into]
                    for pid in fresh:
                        self._prompt_merged_into[pid] = running
                for pid in fresh:
                    self._emit_steer_ack(
                        pid,
                        status="merged",
                        evidence="running_combined_texts",
                        raw={
                            "mergedIntoPromptId": running,
                            "runningCombinedTexts": combined_texts,
                        },
                    )
        else:
            with self._lock:
                self._current_running_prompt_id = None
        cleared_pending = False
        with self._lock:
            dropped = []
            for pid, seen_seq in list(self._prompt_cancelled_pending.items()):
                if seen_seq >= queue_change_seq:
                    continue
                if pid in self._prompt_merged_into:
                    self._prompt_cancelled_pending.pop(pid, None)
                    cleared_pending = True
                    continue
                if pid == running or pid in entry_ids:
                    continue
                self._prompt_cancelled_pending.pop(pid, None)
                dropped.append(pid)
                cleared_pending = True
        for pid in dropped:
            self._emit_steer_ack(
                pid,
                status="dropped",
                evidence="queue_reconciled_cancelled_never_ran",
                raw={"queueChangedSeq": queue_change_seq, "params": params},
            )
        self._events.put(
            AdapterEvent(kind="progress", data="queue/changed", raw=params)
        )
        # After never-ran cancels resolve (drop or merge clear), re-enter
        # completion accounting so an all-cancelled lineage cannot hang waiting
        # for a prompt_complete/result that will never arrive.
        if cleared_pending or dropped:
            with self._lock:
                target = self._final_prompt_id or self._initial_prompt_id
                if not target:
                    known = set(self._prompt_result) | set(self._prompt_complete)
                    target = next(iter(known), None)
                if not target and dropped:
                    target = dropped[-1]
            if target:
                self._maybe_mark_done(target)

    def _on_prompt_complete(self, params: Dict[str, Any]) -> None:
        pid = params.get("promptId") or ""
        stop = _normalize_stop_reason(params.get("stopReason"))
        with self._lock:
            self._prompt_complete[pid] = dict(params)
            self._prompt_cancelled_pending.pop(pid, None)
            if stop not in _CANCEL_STOP_REASONS:
                self._completed_prompt_ids.append(pid)
        self._events.put(
            AdapterEvent(
                kind="prompt_complete",
                data=str(params.get("stopReason") or ""),
                raw=params,
            )
        )
        if pid:
            status, evidence = self._terminal_outcome(
                pid,
                stop_reason=stop,
                source="prompt_complete",
                cancel_trigger=params.get("cancelTrigger"),
            )
            ack_raw = dict(params)
            if status == "superseded":
                with self._lock:
                    successor = self._superseded_by.get(pid) or self._current_running_prompt_id
                if successor and successor != pid:
                    ack_raw["supersededByPromptId"] = successor
            self._emit_steer_ack(
                pid,
                status=status,
                evidence=evidence,
                raw=ack_raw,
            )
            with self._lock:
                merged_followers = [
                    follower
                    for follower, front in self._prompt_merged_into.items()
                    if front == pid
                ]
            for follower in merged_followers:
                self._emit_steer_ack(
                    follower,
                    status=status,
                    evidence=f"merged_{evidence}",
                    raw={"mergedIntoPromptId": pid, "frontCompletion": ack_raw},
                )
        # prompt_complete is authoritative for run completion accounting.
        if pid:
            self._maybe_mark_done(pid)

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
        with self._lock:
            self._prompt_content[prompt_id] = text
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
            stop = result.get("stopReason") if isinstance(result, dict) else ""
            result_meta = result.get("_meta") if isinstance(result, dict) else {}
            if not isinstance(result_meta, dict):
                result_meta = {}
            if _normalize_stop_reason(stop) in _CANCEL_STOP_REASONS:
                with self._lock:
                    started = prompt_id in self._prompt_running or bool(
                        self._prompt_seen_meta.get(prompt_id)
                    )
                    merged = prompt_id in self._prompt_merged_into
                    if not started and not merged:
                        self._prompt_cancelled_pending[prompt_id] = self._queue_change_seq
            status, evidence = self._terminal_outcome(
                prompt_id,
                stop_reason=stop,
                source="prompt_result",
                cancel_trigger=(
                    result.get("cancelTrigger") if isinstance(result, dict) else None
                )
                or result_meta.get("cancelTrigger"),
            )
            ack_raw: Dict[str, Any] = {"promptId": prompt_id, "result": result}
            if status == "superseded":
                with self._lock:
                    successor = self._superseded_by.get(prompt_id)
                if successor:
                    ack_raw["supersededByPromptId"] = successor
            self._emit_steer_ack(
                prompt_id,
                status=status,
                evidence=evidence,
                raw=ack_raw,
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
        final prompt lineage has an authoritative stopReason from
        prompt_complete or prompt_result.

        Rules (honest):
          - missing stop is never success
          - end_turn → exit 0
          - max_tokens → incomplete / non-success exit
          - error / rate_limit / unknown / cancelled → non-zero even with partial text
          - all-cancelled lineages terminate honestly (no hang)
          - never-ran cancel stays awaiting_queue_resolution until queue evidence
            resolves (do not force-drop here before runningCombinedTexts)
          - never emit duplicate done events once already terminal
        """
        with self._lock:
            if self._done:
                return
            if self._in_flight:
                return
            # Do NOT force-drop awaiting_queue_resolution prompts here — that
            # races before runningCombinedTexts can arrive. Bounded grace is
            # handled by queue snapshots / supervisor; only clear when we have
            # advanced queue evidence (seq moved) or cancel of whole run.
            if self._cancelled:
                # Force-resolve any still-pending never-ran cancels on hard cancel.
                unresolved = list(self._prompt_cancelled_pending)
                self._prompt_cancelled_pending.clear()
                for pid in unresolved:
                    self._emit_steer_ack(
                        pid,
                        status="dropped",
                        evidence="run_finished_cancelled_never_ran",
                        raw={"promptId": pid},
                    )
                self._done = True
                self._exit_code = 130
                self._events.put(
                    AdapterEvent(kind="done", data="cancelled", raw={"promptId": completed_prompt_id})
                )
                return

            # Prefer authoritative complete, then prompt_result.
            pc = self._prompt_complete.get(completed_prompt_id) or {}
            pr = self._prompt_result.get(completed_prompt_id)
            stop = _normalize_stop_reason(pc.get("stopReason"))
            source = "prompt_complete"
            if not stop and isinstance(pr, dict):
                stop = _normalize_stop_reason(pr.get("stopReason"))
                source = "prompt_result"
            if not stop:
                # Missing stop is never success. If other prompts remain open in
                # cancelled-pending, wait; if the whole lineage is cancelled,
                # terminate honestly.
                if self._prompt_cancelled_pending:
                    return
                # All settled with no authoritative stop on this id — try final lineage.
                final = self._final_prompt_id
                if final and final != completed_prompt_id:
                    pc = self._prompt_complete.get(final) or {}
                    pr = self._prompt_result.get(final)
                    stop = _normalize_stop_reason(pc.get("stopReason"))
                    source = "prompt_complete"
                    if not stop and isinstance(pr, dict):
                        stop = _normalize_stop_reason(pr.get("stopReason"))
                        source = "prompt_result"
                    completed_prompt_id = final or completed_prompt_id
                if not stop:
                    # All-cancelled lineage: every known prompt cancelled, none succeeded.
                    all_ids = set(self._prompt_result) | set(self._prompt_complete)
                    if all_ids and all(
                        _normalize_stop_reason(
                            (self._prompt_complete.get(pid) or {}).get("stopReason")
                            or (
                                self._prompt_result.get(pid).get("stopReason")
                                if isinstance(self._prompt_result.get(pid), dict)
                                else ""
                            )
                        )
                        in _CANCEL_STOP_REASONS
                        for pid in all_ids
                    ):
                        self._done = True
                        self._exit_code = 130
                        self._events.put(
                            AdapterEvent(
                                kind="done",
                                data="all_cancelled",
                                raw={"promptId": completed_prompt_id},
                            )
                        )
                        return
                    # Still missing stop — do not succeed on partial text alone.
                    return

            if stop in _CANCEL_STOP_REASONS:
                # Prefer latest non-cancelled completion for final lineage.
                if self._completed_prompt_ids:
                    completed_prompt_id = self._completed_prompt_ids[-1]
                    pc = self._prompt_complete.get(completed_prompt_id) or {}
                    pr = self._prompt_result.get(completed_prompt_id)
                    stop = _normalize_stop_reason(pc.get("stopReason"))
                    source = "prompt_complete"
                    if not stop and isinstance(pr, dict):
                        stop = _normalize_stop_reason(pr.get("stopReason"))
                        source = "prompt_result"
                    if not stop or stop in _CANCEL_STOP_REASONS:
                        # All cancelled — terminate honestly.
                        self._done = True
                        self._exit_code = 130
                        self._events.put(
                            AdapterEvent(
                                kind="done",
                                data="cancelled",
                                raw=pc or {"promptId": completed_prompt_id},
                            )
                        )
                        return
                else:
                    # No successful completion recorded; hang only while queue
                    # resolution is still pending for never-ran cancels.
                    if self._prompt_cancelled_pending:
                        return
                    self._done = True
                    self._exit_code = 130
                    self._events.put(
                        AdapterEvent(
                            kind="done",
                            data="cancelled",
                            raw={"promptId": completed_prompt_id},
                        )
                    )
                    return

            final = self._final_prompt_id
            final_done = (
                final is None
                or final in self._prompt_complete
                or final in self._prompt_result
                or completed_prompt_id == final
            )
            if not final_done:
                return

            # Map stopReason → exit code. Partial text never upgrades errors to 0.
            if stop in _SUCCESS_STOP_REASONS:
                exit_code = 0
                done_data = stop
            elif stop in _INCOMPLETE_STOP_REASONS:
                exit_code = 1
                done_data = stop
            elif stop in _FAIL_STOP_REASONS:
                exit_code = 1
                done_data = stop
            else:
                # unknown stop — non-success
                exit_code = 1
                done_data = f"unknown_stop:{stop}"

            self._done = True
            self._exit_code = exit_code
            self._events.put(
                AdapterEvent(
                    kind="done",
                    data=done_data,
                    raw=pc or (pr if isinstance(pr, dict) else {"promptId": completed_prompt_id, "source": source}),
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

    def _ever_started(self, prompt_id: str) -> bool:
        with self._lock:
            return prompt_id in self._prompt_running or bool(
                self._prompt_seen_meta.get(prompt_id)
            )

    def _terminal_outcome(
        self,
        prompt_id: str,
        *,
        stop_reason: Any,
        source: str,
        cancel_trigger: Any = None,
    ) -> Tuple[str, str]:
        """Classify only facts Grok exposes; never infer instruction compliance."""
        stop = _normalize_stop_reason(stop_reason)
        trigger = _normalize_stop_reason(cancel_trigger)
        started = self._ever_started(prompt_id)
        if stop in _CANCEL_STOP_REASONS:
            with self._lock:
                merged = prompt_id in self._prompt_merged_into
            if merged:
                return "merged", "running_combined_texts"
            if trigger == "send_now":
                return "superseded", f"{source}_superseded"
            if source == "prompt_result" and not started:
                return "awaiting_queue_resolution", "prompt_result_cancelled_unresolved"
            return "cancelled", f"{source}_cancelled"
        if stop in _FAIL_STOP_REASONS:
            return "failed", f"{source}_{stop}"
        if stop in _INCOMPLETE_STOP_REASONS:
            return "incomplete", f"{source}_{stop}"
        if stop == "refusal":
            return "rejected", f"{source}_refusal"
        if stop in _SUCCESS_STOP_REASONS:
            return "completed", source
        return "failed", f"{source}_unknown_stop:{stop or 'missing'}"

    def _observed_for(self, prompt_id: str) -> Optional[Tuple[str, str]]:
        """Return the strongest wire-observable lifecycle state for promptId."""
        with self._lock:
            complete = self._prompt_complete.get(prompt_id)
            result = self._prompt_result.get(prompt_id)
            if prompt_id in self._prompt_running:
                running = True
            else:
                running = False
            seen_meta = bool(self._prompt_seen_meta.get(prompt_id))
        if complete is not None:
            status, evidence = self._terminal_outcome(
                prompt_id,
                stop_reason=complete.get("stopReason"),
                source="prompt_complete",
                cancel_trigger=complete.get("cancelTrigger"),
            )
            return status, evidence
        if result is not None:
            status, evidence = self._terminal_outcome(
                prompt_id,
                stop_reason=result.get("stopReason") if isinstance(result, dict) else "",
                source="prompt_result",
                cancel_trigger=(
                    result.get("cancelTrigger")
                    or ((result.get("_meta") or {}).get("cancelTrigger"))
                    if isinstance(result, dict)
                    else None
                ),
            )
            return status, evidence
        if running:
            return "running", "running_prompt_id"
        if seen_meta:
            return "running", "promptId_notification_meta"
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
        # Final-text lineage: interrupt/sendNow may replace the whole result with
        # the new prompt's answer. queue/auto guidance must NOT replace lineage
        # with a tiny follower answer — keep the existing final prompt id.
        if send_now:
            self._final_prompt_id = prompt_id
            with self._lock:
                interrupted = self._current_running_prompt_id
                if interrupted and interrupted != prompt_id:
                    self._superseded_by.setdefault(interrupted, prompt_id)
        # else: leave _final_prompt_id on initial / last interrupt lineage
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
        # Do not wait here: steer() runs on the supervisor's mailbox loop.
        # Blocking would delay later guidance and prevent event reconciliation.
        # Callback-maintained state may already contain an observation; otherwise
        # return transport state and let async steer_ack events advance it.
        observed = self._observed_for(prompt_id)
        if observed:
            status, evidence = observed
            return SteerResult(
                ok=True,
                delivery_class=dclass,
                status=status,
                evidence=evidence,
                meta={
                    "promptId": prompt_id,
                    "sendNow": send_now,
                    "client_id": client_id,
                },
            )
        with self._lock:
            in_flight = prompt_id in self._in_flight
        # JSON-RPC write / in-flight is NOT "delivered" — only request_sent/queued.
        q_ev = self._queue_confirmed_for(prompt_id)
        if in_flight or q_ev:
            status = "queued" if q_ev else "request_sent"
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
        observed = self._observed_for(prompt_id)
        if observed:
            status, evidence = observed
            return SteerResult(
                ok=True,
                delivery_class=dclass,
                status=status,
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
        """Hard-cancel the run: exit 130, resolve pending never-ran honestly.

        Emits at most one done event. Pending never-ran cancels become dropped
        with run_finished_cancelled_never_ran evidence (no duplicate acks if
        already resolved by queue reconciliation).
        """
        with self._lock:
            already_done = self._done
            self._cancelled = True
            unresolved = list(self._prompt_cancelled_pending)
            self._prompt_cancelled_pending.clear()
            # Drop in-flight bookkeeping so completion accounting can finish.
            self._in_flight.clear()
        for pid in unresolved:
            self._emit_steer_ack(
                pid,
                status="dropped",
                evidence="run_finished_cancelled_never_ran",
                raw={"promptId": pid},
            )
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
        with self._lock:
            if not already_done and not self._done:
                self._done = True
                self._exit_code = 130
                self._events.put(
                    AdapterEvent(
                        kind="done",
                        data="cancelled",
                        raw={"promptId": self._final_prompt_id or self._initial_prompt_id},
                    )
                )
            else:
                self._done = True
                if self._exit_code is None:
                    self._exit_code = 130

    def final_text(self) -> str:
        """Assemble final answer from the authoritative lineage.

        Prefer the final prompt id (initial task, or last interrupt/sendNow).
        queue/auto followers do not become the sole lineage, so a tiny follower
        answer cannot replace a full primary result.

        After interrupt/sendNow, an empty successor lineage must not resurrect
        superseded initial or concatenated all-text fragments.
        """
        with self._lock:
            lineage = self._final_prompt_id or self._initial_prompt_id
            if lineage and lineage in self._text_by_prompt:
                text = "".join(self._text_by_prompt[lineage])
                if text.strip():
                    return text
            # Interrupt/sendNow replaced the lineage: empty successor wins over
            # any superseded initial or pre-interrupt all_text fragments.
            if (
                self._final_prompt_id
                and self._initial_prompt_id
                and self._final_prompt_id != self._initial_prompt_id
            ):
                return "".join(self._text_by_prompt.get(self._final_prompt_id, []))
            # Merged followers may have contributed only via the front prompt;
            # fall back to initial, then all agent_message text (same lineage only).
            if (
                self._initial_prompt_id
                and self._initial_prompt_id != lineage
                and self._initial_prompt_id in self._text_by_prompt
            ):
                text = "".join(self._text_by_prompt[self._initial_prompt_id])
                if text.strip():
                    return text
            if self._all_text:
                return "".join(self._all_text)
        return ""

    def close(self) -> None:
        self.cancel()


def _looks_like_uuid(s: str) -> bool:
    try:
        uuid.UUID(s)
        return True
    except Exception:
        return False
