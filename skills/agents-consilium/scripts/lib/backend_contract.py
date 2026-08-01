#!/usr/bin/env python3
"""Shared backend contract for one-shot and steerable Consilium paths.

Centralizes:
  - backend identity and binary resolution
  - model / effort resolution (config + env overrides)
  - capability differences (steer, interrupt, live queue, transport)
  - final-text completeness / assembly rules

Does not own argv construction for every flag (backend_run.sh and steerable
adapters still build argv), but is the single place shell and Python agree on
identity, resolution, and capability truth.
"""
from __future__ import annotations

import json
import os
import shutil
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from events import (
    AUTHORITATIVE_RESULT_TYPES,
    TEXT_DELTA_TYPES,
    assemble_final_text,
    make_event,
)
from mode_policy import ModeCapabilities, access_policy_for, get_mode_capabilities


BACKEND_IDS = (
    "codex-cli",
    "claude-code",
    "opencode",
    "grok-build",
    "gemini-cli",
)

BACKEND_BINS = {
    "codex-cli": "codex",
    "claude-code": "claude",
    "opencode": "opencode",
    "grok-build": "grok",
    "gemini-cli": "gemini",
}

BIN_ENV = {
    "codex-cli": "CONSILIUM_BIN_CODEX",
    "claude-code": "CONSILIUM_BIN_CLAUDE",
    "opencode": "CONSILIUM_BIN_OPENCODE",
    "grok-build": "CONSILIUM_BIN_GROK",
    "gemini-cli": "CONSILIUM_BIN_GEMINI",
}

MODEL_ENV = {
    "codex-cli": "CODEX_MODEL",
    "claude-code": "CLAUDE_MODEL",
    "opencode": "OPENCODE_MODEL",
    "grok-build": "GROK_MODEL",
    "gemini-cli": "GEMINI_MODEL",
}

EFFORT_ENV = {
    "codex-cli": "CODEX_EFFORT",
    "claude-code": "CLAUDE_EFFORT",
    "opencode": "OPENCODE_EFFORT",
    "grok-build": "GROK_EFFORT",
}


@dataclass(frozen=True)
class BackendCapabilities:
    """Actual capability differences — do not pretend uniform semantics."""

    backend: str
    # Primary transport label (legacy single field). Prefer oneshot_transport /
    # steerable_transport when they differ.
    transport: str
    oneshot_transport: str
    steerable_transport: str  # "" when not steerable
    steerable: bool
    steer_auto: str  # delivery class name or ""
    steer_queue: str
    steer_interrupt: str  # "" if unsupported
    live_queue: bool  # backend has a real concurrent prompt queue
    oneshot: bool
    supports_delegate: bool
    final_text_rule: str  # assembly strategy id
    # Honest notes about capabilities that cannot be fully enforced via argv.
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# Honest matrix — mirrors SKILL.md delivery matrix and one-shot streams.
# One-shot and steerable transports are represented distinctly when they differ.
_BACKEND_CAPS: Dict[str, BackendCapabilities] = {
    "codex-cli": BackendCapabilities(
        backend="codex-cli",
        transport="exec-json",  # one-shot primary
        oneshot_transport="exec-json",
        steerable_transport="app-server",
        steerable=True,
        steer_auto="same_turn",
        steer_queue="same_turn",
        steer_interrupt="abort_and_prompt",
        live_queue=False,
        oneshot=True,
        supports_delegate=True,
        final_text_rule="codex_last_message_or_deltas",
        notes=(
            "One-shot: codex exec --json + -o last-message. "
            "Steerable: app-server JSON-RPC (distinct transport). "
            "Final text: -o last-message when non-empty, else answer deltas."
        ),
    ),
    "claude-code": BackendCapabilities(
        backend="claude-code",
        transport="stream-json",
        oneshot_transport="stream-json",
        steerable_transport="stream-json",
        steerable=True,
        steer_auto="queue_next_turn",
        steer_queue="queue_next_turn",
        steer_interrupt="",  # rejected; no silent downgrade
        live_queue=False,
        oneshot=True,
        supports_delegate=True,
        final_text_rule="claude_result_over_deltas",
        notes=(
            "Authoritative result preferred over streamed deltas; "
            "empty/whitespace result must not erase non-empty deltas. "
            "Interrupt mode is rejected (no silent downgrade)."
        ),
    ),
    "opencode": BackendCapabilities(
        backend="opencode",
        transport="http-sse",
        oneshot_transport="run-json",
        steerable_transport="http-sse",
        steerable=True,
        steer_auto="step_inject",
        steer_queue="step_inject",
        steer_interrupt="abort_and_prompt",
        live_queue=False,
        oneshot=True,
        supports_delegate=True,
        final_text_rule="opencode_part_snapshots",
        notes=(
            "One-shot: opencode run --format json. "
            "Steerable: loopback HTTP + SSE; message.part.updated is cumulative "
            "per part id (not append-delta); session.idle is turn-idle, not "
            "automatic permanent run completion while a prompt/steer is in flight. "
            "auto/queue = step_inject (prompt_async); interrupt = abort_and_prompt."
        ),
    ),
    "grok-build": BackendCapabilities(
        backend="grok-build",
        transport="streaming-json",
        oneshot_transport="streaming-json",
        steerable_transport="acp-stdio",
        steerable=True,
        steer_auto="queue_next_turn",
        steer_queue="queue_next_turn",
        steer_interrupt="cancel_and_send",
        live_queue=True,
        oneshot=True,
        supports_delegate=True,
        final_text_rule="grok_text_events_require_end",
        notes=(
            "One-shot: streaming-json (end required, no error). "
            "Steerable: native ACP stdio concurrent queue (distinct transport; "
            "no other backend is migrated to ACP). "
            "stopReason end_turn → success; max_tokens → incomplete; "
            "error/rate_limit/unknown/cancelled are never exit 0 solely due to partial text."
        ),
    ),
    "gemini-cli": BackendCapabilities(
        backend="gemini-cli",
        transport="oneshot-cli",
        oneshot_transport="oneshot-cli",
        steerable_transport="",
        steerable=False,
        steer_auto="",
        steer_queue="",
        steer_interrupt="",
        live_queue=False,
        oneshot=True,
        supports_delegate=False,
        final_text_rule="plain_stdout",
        notes="Review-only; plain-text stdout behavior with backend identity gemini-cli.",
    ),
}


@dataclass
class ResolvedBackend:
    agent_id: str
    backend: str
    model: str
    effort: str
    binary: str
    label: str = ""
    role: str = ""
    supports_delegate: bool = True
    review_instructions: str = ""
    capabilities: BackendCapabilities = field(default_factory=lambda: _BACKEND_CAPS["codex-cli"])
    mode_capabilities: Optional[ModeCapabilities] = None
    access_class: str = "readonly"

    def to_dict(self) -> Dict[str, Any]:
        d = {
            "agent_id": self.agent_id,
            "backend": self.backend,
            "model": self.model,
            "effort": self.effort,
            "binary": self.binary,
            "label": self.label,
            "role": self.role,
            "supports_delegate": self.supports_delegate,
            "review_instructions": self.review_instructions,
            "access_class": self.access_class,
            "capabilities": self.capabilities.to_dict(),
        }
        if self.mode_capabilities is not None:
            d["mode_capabilities"] = self.mode_capabilities.to_dict()
        return d


def skill_root() -> Path:
    return Path(__file__).resolve().parents[2]


def config_path() -> Path:
    env = os.environ.get("CONSILIUM_CONFIG")
    if env:
        return Path(env)
    return skill_root() / "config.json"


def load_config() -> Dict[str, Any]:
    path = config_path()
    if not path.is_file():
        raise FileNotFoundError(f"consilium config not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_agent(agent_id: str) -> Dict[str, Any]:
    cfg = load_config()
    agents = cfg.get("agents") or {}
    if agent_id not in agents:
        raise KeyError(f"unknown agent id: {agent_id}")
    return dict(agents[agent_id])


def resolve_binary(backend: str) -> str:
    env_key = BIN_ENV.get(backend)
    if env_key and os.environ.get(env_key):
        return os.environ[env_key]
    name = BACKEND_BINS.get(backend)
    if not name:
        raise ValueError(f"unknown backend: {backend}")
    found = shutil.which(name)
    return found or name


def backend_capabilities(backend: str) -> BackendCapabilities:
    if backend not in _BACKEND_CAPS:
        raise ValueError(f"unknown backend: {backend}")
    return _BACKEND_CAPS[backend]


def resolve_model_effort(backend: str, agent: Mapping[str, Any]) -> Tuple[str, str]:
    """Resolve model and effort with env overrides (same rules as backend_run.sh)."""
    model = str(agent.get("model") or "")
    env_model = MODEL_ENV.get(backend)
    if env_model and os.environ.get(env_model):
        model = os.environ[env_model]
    if backend == "codex-cli" and model == "gpt-5.6":
        model = "gpt-5.6-sol"

    effort = str(agent.get("effort") or "")
    env_effort = EFFORT_ENV.get(backend)
    if env_effort and os.environ.get(env_effort):
        effort = os.environ[env_effort]
    if backend in ("codex-cli", "claude-code", "grok-build"):
        effort = effort or "high"
    elif backend == "opencode" and effort == "none":
        effort = ""
    return model, effort


def resolve_agent(
    agent_id: str,
    *,
    mode: str = "review",
    require_delegate: bool = False,
) -> ResolvedBackend:
    agent = get_agent(agent_id)
    backend = str(agent.get("backend") or "")
    if backend not in _BACKEND_CAPS:
        raise ValueError(f"unknown backend {backend!r} for agent {agent_id}")
    caps = backend_capabilities(backend)
    model, effort = resolve_model_effort(backend, agent)
    binary = resolve_binary(backend)

    supports = agent.get("supports_delegate")
    if supports in (False, "false", 0, "0"):
        supports_delegate = False
    else:
        supports_delegate = caps.supports_delegate

    if require_delegate:
        if backend == "gemini-cli" or not supports_delegate:
            raise ValueError(
                f"agent '{agent_id}' cannot delegate (review-only / supports_delegate=false)"
            )

    mode_caps = get_mode_capabilities(mode)
    access = access_policy_for(mode)

    return ResolvedBackend(
        agent_id=agent_id,
        backend=backend,
        model=model,
        effort=effort,
        binary=binary,
        label=str(agent.get("label") or agent_id),
        role=str(agent.get("role") or "analyst"),
        supports_delegate=supports_delegate,
        review_instructions=str(agent.get("review_instructions") or ""),
        capabilities=caps,
        mode_capabilities=mode_caps,
        access_class=access,
    )


# --- Final-text assembly rules ------------------------------------------------

def final_text_from_normalized(
    backend: str,
    events: Sequence[Any],
    *,
    last_message: str = "",
) -> str:
    """Assemble final text using the backend's completeness rule."""
    rule = backend_capabilities(backend).final_text_rule
    if rule == "codex_last_message_or_deltas":
        if last_message:
            return last_message
        return assemble_final_text(events)
    if rule == "claude_result_over_deltas":
        return assemble_final_text(events)
    if rule == "grok_text_events_require_end":
        # Completeness is validated separately (end present, no error).
        return assemble_final_text(events)
    if rule in ("opencode_text_parts", "opencode_part_snapshots", "plain_stdout"):
        return assemble_final_text(events)
    return assemble_final_text(events)


def grok_stream_ok(events: Sequence[Any]) -> Tuple[bool, str]:
    """Grok one-shot success: end present, no error."""
    saw_end = False
    saw_error = False
    err = ""
    for item in events:
        if hasattr(item, "type"):
            typ = item.type
            data = item.data
        else:
            typ = item.get("type")
            data = item.get("data")
        if typ == "run_completed":
            saw_end = True
        elif typ == "run_failed":
            saw_error = True
            err = str(data or "")
        # Legacy stream names if present
        elif typ == "end":
            saw_end = True
        elif typ == "error":
            saw_error = True
            err = str(data or "")
    if saw_error:
        return False, f"grok stream error: {err}"
    if not saw_end:
        return False, "grok stream missing end event"
    return True, ""


def list_backend_capabilities() -> Dict[str, Dict[str, Any]]:
    return {k: v.to_dict() for k, v in _BACKEND_CAPS.items()}


def _main() -> int:
    import argparse
    import sys

    ap = argparse.ArgumentParser(description="Consilium shared backend contract")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_res = sub.add_parser("resolve", help="Resolve agent settings")
    p_res.add_argument("agent_id")
    p_res.add_argument("--mode", default="review")
    p_res.add_argument("--require-delegate", action="store_true")

    p_caps = sub.add_parser("capabilities", help="Backend capability matrix")
    p_caps.add_argument("backend", nargs="?")

    p_access = sub.add_parser("access-class", help="Mode access class")
    p_access.add_argument("mode")

    p_bin = sub.add_parser("binary", help="Resolve backend binary")
    p_bin.add_argument("backend")

    args = ap.parse_args()
    try:
        if args.cmd == "resolve":
            r = resolve_agent(
                args.agent_id,
                mode=args.mode,
                require_delegate=args.require_delegate,
            )
            print(json.dumps(r.to_dict(), indent=2))
            return 0
        if args.cmd == "capabilities":
            if args.backend:
                print(json.dumps(backend_capabilities(args.backend).to_dict(), indent=2))
            else:
                print(json.dumps(list_backend_capabilities(), indent=2))
            return 0
        if args.cmd == "access-class":
            print(access_policy_for(args.mode))
            return 0
        if args.cmd == "binary":
            print(resolve_binary(args.backend))
            return 0
    except (KeyError, ValueError, FileNotFoundError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 4
    return 2


if __name__ == "__main__":
    raise SystemExit(_main())
