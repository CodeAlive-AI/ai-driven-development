"""Load consilium config.json via shared backend_contract (one-shot + steerable)."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, Tuple

# scripts/lib is the shared module root for events/backend_contract/mode_policy.
_LIB = Path(__file__).resolve().parents[1]
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from backend_contract import (  # noqa: E402
    BACKEND_BINS,
    BIN_ENV,
    config_path,
    get_agent,
    load_config,
    resolve_agent,
    resolve_binary,
    skill_root,
)

__all__ = [
    "BACKEND_BINS",
    "BIN_ENV",
    "skill_root",
    "config_path",
    "load_config",
    "get_agent",
    "resolve_binary",
    "agent_settings",
]


def agent_settings(agent_id: str) -> Tuple[Dict[str, Any], str, str, str]:
    """Return (agent_dict, backend, model, binary) — same shape as before.

    Uses the shared backend_contract so model/effort/binary resolution matches
    ordinary backend_run.sh paths (including env overrides).
    """
    r = resolve_agent(agent_id, mode="delegate-steerable", require_delegate=True)
    agent = get_agent(agent_id)
    agent = dict(agent)
    agent["model"] = r.model
    agent["effort"] = r.effort
    return agent, r.backend, r.model, r.binary
