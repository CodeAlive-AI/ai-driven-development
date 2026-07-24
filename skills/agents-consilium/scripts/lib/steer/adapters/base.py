"""Backend adapter interface for steerable delegate."""
from __future__ import annotations

import enum
from dataclasses import dataclass, field
from typing import Any, Dict, Iterator, List, Optional


class DeliveryClass(str, enum.Enum):
    """Honest protocol delivery class (not mailbox acceptance)."""

    SAME_TURN = "same_turn"
    STEP_INJECT = "step_inject"
    QUEUE_NEXT_TURN = "queue_next_turn"
    NEXT_TURN = "next_turn"  # legacy alias; prefer QUEUE_NEXT_TURN
    ABORT_AND_PROMPT = "abort_and_prompt"
    CANCEL_AND_SEND = "cancel_and_send"


@dataclass
class SteerResult:
    ok: bool
    delivery_class: DeliveryClass
    status: str  # request_sent|queued|delivered|applied|failed|rejected|delivering
    evidence: str = ""
    error: str = ""
    meta: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AdapterEvent:
    kind: str  # text|thought|tool|error|done|raw|progress|user_replay|turn_started|turn_completed|prompt_complete|steer_ack
    data: str = ""
    raw: Optional[Dict[str, Any]] = None


class BackendAdapter:
    backend_name: str = "base"
    auto_delivery: DeliveryClass = DeliveryClass.SAME_TURN

    def __init__(
        self,
        *,
        binary: str,
        model: str,
        effort: str = "",
        cwd: str,
        artifacts_dir: str,
        agent_id: str = "",
    ):
        self.binary = binary
        self.model = model
        self.effort = effort
        self.cwd = cwd
        self.artifacts_dir = artifacts_dir
        self.agent_id = agent_id
        self._final_parts: List[str] = []
        self._done = False
        self._error: Optional[str] = None
        self._exit_code: Optional[int] = None

    def start(self, task: str) -> None:
        raise NotImplementedError

    def poll_events(self) -> Iterator[AdapterEvent]:
        """Yield newly available events without long blocking."""
        raise NotImplementedError
        yield  # pragma: no cover

    def map_mode(self, mode: str) -> DeliveryClass:
        if mode == "auto":
            return self.auto_delivery
        if mode == "queue":
            return self._queue_class()
        if mode == "interrupt":
            return self._interrupt_class()
        raise ValueError(f"unsupported mode: {mode}")

    def _queue_class(self) -> DeliveryClass:
        return DeliveryClass.QUEUE_NEXT_TURN

    def _interrupt_class(self) -> DeliveryClass:
        raise NotImplementedError(f"{self.backend_name} does not support interrupt")

    def supports_mode(self, mode: str) -> bool:
        try:
            self.map_mode(mode)
            return True
        except NotImplementedError:
            return False

    def steer(self, content: str, mode: str, client_id: str) -> SteerResult:
        raise NotImplementedError

    def cancel(self) -> None:
        raise NotImplementedError

    def is_busy(self) -> bool:
        return not self._done

    def is_done(self) -> bool:
        return self._done

    def final_text(self) -> str:
        return "".join(self._final_parts)

    def exit_code(self) -> int:
        if self._exit_code is not None:
            return self._exit_code
        return 1 if self._error else 0

    def child_pid(self) -> Optional[int]:
        return None

    def close(self) -> None:
        pass
