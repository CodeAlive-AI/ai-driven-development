"""Load consilium config.json (same resolution concepts as config.sh)."""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


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


def skill_root() -> Path:
    # scripts/lib/steer/config_loader.py -> skill root is ../../..
    return Path(__file__).resolve().parents[3]


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
    # Prefer PATH
    found = shutil.which(name)
    if found:
        return found
    return name


def agent_settings(agent_id: str) -> Tuple[Dict[str, Any], str, str, str]:
    """Return (agent_dict, backend, model, binary)."""
    agent = get_agent(agent_id)
    backend = agent.get("backend") or ""
    if backend == "gemini-cli" or agent.get("supports_delegate") in (False, "false", 0, "0"):
        raise ValueError(f"agent '{agent_id}' cannot steerable-delegate (review-only)")
    model = agent.get("model") or ""
    if backend == "codex-cli" and model == "gpt-5.6":
        model = "gpt-5.6-sol"
    # Env model overrides (same spirit as existing backends)
    env_model = {
        "codex-cli": "CODEX_MODEL",
        "claude-code": "CLAUDE_MODEL",
        "opencode": "OPENCODE_MODEL",
        "grok-build": "GROK_MODEL",
    }.get(backend)
    if env_model and os.environ.get(env_model):
        model = os.environ[env_model]
    effort = agent.get("effort") or ""
    env_effort = {
        "codex-cli": "CODEX_EFFORT",
        "claude-code": "CLAUDE_EFFORT",
        "opencode": "OPENCODE_EFFORT",
        "grok-build": "GROK_EFFORT",
    }.get(backend)
    if env_effort and os.environ.get(env_effort):
        effort = os.environ[env_effort]
    agent = dict(agent)
    agent["model"] = model
    agent["effort"] = effort
    binary = resolve_binary(backend)
    return agent, backend, model, binary
