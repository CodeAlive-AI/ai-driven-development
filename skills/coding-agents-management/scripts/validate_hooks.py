#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Validate Claude Code or Antigravity hooks configuration."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _jsonc import load_jsonc

# Claude Code 28 lifecycle events (plus Setup alias seen in docs)
CLAUDE_VALID_EVENTS = {
    "SessionStart",
    "SessionEnd",
    "InstructionsLoaded",
    "UserPromptSubmit",
    "UserPromptExpansion",
    "PreToolUse",
    "PostToolUse",
    "PostToolUseFailure",
    "PostToolBatch",
    "PermissionRequest",
    "PermissionDenied",
    "Stop",
    "StopFailure",
    "SubagentStart",
    "SubagentStop",
    "TaskCreated",
    "TaskCompleted",
    "TeammateIdle",
    "ConfigChange",
    "FileChanged",
    "CwdChanged",
    "PreCompact",
    "PostCompact",
    "WorktreeCreate",
    "WorktreeRemove",
    "Elicitation",
    "ElicitationResult",
    "Notification",
}

CLAUDE_MATCHER_EVENTS = {
    "PreToolUse",
    "PostToolUse",
    "PostToolUseFailure",
    "PostToolBatch",
    "PermissionRequest",
    "PermissionDenied",
    "Notification",
    "PreCompact",
    "PostCompact",
    "SessionStart",
    "SessionEnd",
    "SubagentStart",
    "SubagentStop",
    "InstructionsLoaded",
    "ConfigChange",
    "FileChanged",
    "Elicitation",
    "ElicitationResult",
}

CLAUDE_VALID_HOOK_TYPES = {"command", "http", "mcp_tool", "prompt", "agent"}

CLAUDE_COMMAND_ONLY_EVENTS = {
    "PostCompact",
    "PermissionDenied",
    "Elicitation",
    "ElicitationResult",
    "FileChanged",
    "CwdChanged",
    "ConfigChange",
    "InstructionsLoaded",
    "WorktreeCreate",
    "WorktreeRemove",
    "SubagentStart",
    "StopFailure",
    "TeammateIdle",
    "SessionStart",
    "SessionEnd",
    "Notification",
}

AGY_FLAT_EVENTS = {"SessionStart", "PreInvocation", "PostInvocation", "Stop"}
AGY_MATCHER_EVENTS = {"PreToolUse", "PostToolUse"}
AGY_VALID_EVENTS = AGY_FLAT_EVENTS | AGY_MATCHER_EVENTS
AGY_NAMED_HOOK_META_KEYS = {"enabled", "description"}


def validate_regex(pattern: str) -> tuple[bool, str | None]:
    """Validate a matcher regex pattern."""
    if pattern in ("*", ""):
        return True, None
    try:
        re.compile(pattern)
        return True, None
    except re.error as exc:
        return False, str(exc)


def _validate_timeout_and_once(hook: dict[str, Any], path: str) -> list[str]:
    errors: list[str] = []
    if "timeout" in hook:
        timeout = hook["timeout"]
        if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or timeout <= 0:
            errors.append(f"{path}: 'timeout' must be a positive number")
    if "once" in hook and not isinstance(hook["once"], bool):
        errors.append(f"{path}: 'once' must be a boolean")
    return errors


def _validate_claude_handler(hook: dict[str, Any], event: str, path: str) -> list[str]:
    errors: list[str] = []
    hook_type = hook.get("type")
    if not hook_type:
        errors.append(f"{path}: missing required field 'type'")
        return errors

    if hook_type not in CLAUDE_VALID_HOOK_TYPES:
        errors.append(
            f"{path}: invalid type '{hook_type}', expected one of {sorted(CLAUDE_VALID_HOOK_TYPES)}"
        )
        return errors

    if event in CLAUDE_COMMAND_ONLY_EVENTS and hook_type != "command":
        errors.append(f"{path}: event '{event}' only supports 'command' hooks (got '{hook_type}')")

    if hook_type == "command":
        cmd = hook.get("command")
        if not isinstance(cmd, str) or not cmd.strip():
            errors.append(f"{path}: type 'command' requires non-empty string field 'command'")
    elif hook_type == "http":
        url = hook.get("url")
        if not isinstance(url, str) or not url.strip():
            errors.append(f"{path}: type 'http' requires non-empty string field 'url'")
    elif hook_type in ("prompt", "agent"):
        prompt = hook.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{path}: type '{hook_type}' requires non-empty string field 'prompt'")
    elif hook_type == "mcp_tool":
        tool_ref = hook.get("tool") or hook.get("tool_name") or hook.get("mcp_tool")
        if not isinstance(tool_ref, str) or not tool_ref.strip():
            errors.append(
                f"{path}: type 'mcp_tool' requires non-empty 'tool' (or 'tool_name'/'mcp_tool') field"
            )

    errors.extend(_validate_timeout_and_once(hook, path))
    return errors


def validate_claude_hooks_config(config: dict[str, Any]) -> tuple[list[str], list[str]]:
    """Validate Claude Code hooks configuration dict. Returns (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    if "hooks" not in config:
        return errors, warnings

    hooks = config["hooks"]
    if not isinstance(hooks, dict):
        return ["hooks: must be an object"], warnings

    for event, entries in hooks.items():
        if event not in CLAUDE_VALID_EVENTS:
            errors.append(f"hooks.{event}: invalid Claude Code event name")
            continue

        if not isinstance(entries, list):
            errors.append(f"hooks.{event}: must be an array")
            continue

        for idx, entry in enumerate(entries):
            path = f"hooks.{event}[{idx}]"
            if not isinstance(entry, dict):
                errors.append(f"{path}: must be an object")
                continue

            if "matcher" in entry:
                matcher = entry["matcher"]
                if not isinstance(matcher, str):
                    errors.append(f"{path}.matcher: must be a string")
                else:
                    if event not in CLAUDE_MATCHER_EVENTS:
                        warnings.append(f"{path}.matcher: event '{event}' ignores matchers")
                    valid, regex_err = validate_regex(matcher)
                    if not valid:
                        errors.append(f"{path}.matcher: invalid regex '{matcher}': {regex_err}")

            handler_list = entry.get("hooks")
            if not isinstance(handler_list, list) or not handler_list:
                errors.append(f"{path}: requires non-empty 'hooks' array")
                continue

            for h_idx, handler in enumerate(handler_list):
                if not isinstance(handler, dict):
                    errors.append(f"{path}.hooks[{h_idx}]: must be an object")
                    continue
                errors.extend(_validate_claude_handler(handler, event, f"{path}.hooks[{h_idx}]"))

    return errors, warnings


def _validate_agy_handler(handler: Any, path: str) -> list[str]:
    if not isinstance(handler, dict):
        return [f"{path}: must be an object"]
    errors: list[str] = []
    hook_type = handler.get("type", "command")
    if hook_type != "command":
        errors.append(f"{path}: Antigravity only supports 'command' hooks (got '{hook_type}')")
    cmd = handler.get("command")
    if not isinstance(cmd, str) or not cmd.strip():
        errors.append(f"{path}: missing non-empty string 'command'")
    errors.extend(_validate_timeout_and_once(handler, path))
    return errors


def validate_antigravity_hooks_config(
    config: dict[str, Any], filepath: Path | None = None
) -> tuple[list[str], list[str]]:
    """Validate Antigravity hooks.json named-hook map. Returns (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    if filepath is not None:
        if filepath.name == "settings.json" and "hooks" in config:
            errors.append(
                "Antigravity settings.json ignores 'hooks' keys; move hooks to ~/.gemini/config/hooks.json or .agents/hooks.json"
            )
            return errors, warnings
        if filepath.name == "hooks.json" and filepath.parent.name == "hooks":
            warnings.append(
                "Native Antigravity plugins load hooks from <plugin>/hooks.json at root, not hooks/hooks.json"
            )

    if "hooks" in config and isinstance(config["hooks"], dict):
        errors.append(
            "Top-level 'hooks' wrapper detected; Antigravity hooks.json uses a named-hook map directly at root"
        )
        return errors, warnings

    for hook_name, body in config.items():
        if hook_name == "$schema":
            continue
        if not isinstance(body, dict):
            errors.append(f"{hook_name}: named hook entry must be an object")
            continue

        if "enabled" in body and not isinstance(body["enabled"], bool):
            errors.append(f"{hook_name}.enabled: must be a boolean")

        has_event = False
        for key, value in body.items():
            if key in AGY_NAMED_HOOK_META_KEYS:
                continue
            if key not in AGY_VALID_EVENTS:
                errors.append(
                    f"{hook_name}.{key}: unknown Antigravity event (expected one of {sorted(AGY_VALID_EVENTS)})"
                )
                continue
            has_event = True
            if not isinstance(value, list):
                errors.append(f"{hook_name}.{key}: must be an array")
                continue

            if key in AGY_FLAT_EVENTS:
                for idx, handler in enumerate(value):
                    errors.extend(_validate_agy_handler(handler, f"{hook_name}.{key}[{idx}]"))
            else:
                for idx, entry in enumerate(value):
                    entry_path = f"{hook_name}.{key}[{idx}]"
                    if not isinstance(entry, dict):
                        errors.append(f"{entry_path}: must be a matcher object")
                        continue
                    if "matcher" in entry:
                        if not isinstance(entry["matcher"], str):
                            errors.append(f"{entry_path}.matcher: must be a string")
                        else:
                            valid, regex_err = validate_regex(entry["matcher"])
                            if not valid:
                                errors.append(
                                    f"{entry_path}.matcher: invalid regex '{entry['matcher']}': {regex_err}"
                                )
                    inner_hooks = entry.get("hooks")
                    if not isinstance(inner_hooks, list) or not inner_hooks:
                        errors.append(f"{entry_path}: requires non-empty 'hooks' array")
                        continue
                    for h_idx, handler in enumerate(inner_hooks):
                        errors.extend(_validate_agy_handler(handler, f"{entry_path}.hooks[{h_idx}]"))

        if not has_event:
            warnings.append(f"{hook_name}: hook definition has no event triggers configured")

    return errors, warnings


def detect_agent(config: dict[str, Any], filepath: Path) -> str:
    """Infer target agent schema ('claude-code' or 'antigravity')."""
    if filepath.name == "settings.json":
        if ".gemini" in filepath.parts or ".antigravity" in filepath.parts:
            return "antigravity"
        return "claude-code"
    if "hooks" in config and isinstance(config["hooks"], dict):
        return "claude-code"
    if any(
        isinstance(v, dict) and ("enabled" in v or any(ev in v for ev in AGY_VALID_EVENTS))
        for k, v in config.items()
        if k != "$schema"
    ):
        return "antigravity"
    if ".agents" in filepath.parts or (filepath.name == "hooks.json" and (filepath.parent / "plugin.json").exists()):
        return "antigravity"
    return "claude-code"


def validate_file(filepath: str, agent: str = "auto") -> dict[str, Any]:
    """Validate a hooks or settings file. Returns structured result dictionary."""
    path = Path(filepath)
    if not path.exists():
        return {"valid": False, "agent": agent, "file": str(path), "errors": [f"File not found: {filepath}"], "warnings": []}

    try:
        config = load_jsonc(path)
    except Exception as exc:
        return {"valid": False, "agent": agent, "file": str(path), "errors": [f"Invalid JSON/JSONC: {exc}"], "warnings": []}

    if not isinstance(config, dict):
        return {
            "valid": False,
            "agent": agent,
            "file": str(path),
            "errors": ["Configuration root must be a JSON object"],
            "warnings": [],
        }

    resolved_agent = detect_agent(config, path) if agent == "auto" else agent
    if resolved_agent == "antigravity":
        errors, warnings = validate_antigravity_hooks_config(config, path)
    else:
        errors, warnings = validate_claude_hooks_config(config)

    return {
        "valid": len(errors) == 0,
        "agent": resolved_agent,
        "file": str(path),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate hooks configuration for Claude Code or Antigravity")
    parser.add_argument("config_file", help="Path to settings.json or hooks.json")
    parser.add_argument(
        "--agent",
        choices=("auto", "claude-code", "antigravity"),
        default="auto",
        help="Schema to validate against (default: auto)",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format (default: text)",
    )
    args = parser.parse_args()

    result = validate_file(args.config_file, agent=args.agent)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        status = "VALID" if result["valid"] else "INVALID"
        print(f"[{status}] ({result['agent']}) {result['file']}")
        for warn in result["warnings"]:
            print(f"  WARN: {warn}")
        for err in result["errors"]:
            print(f"  ERROR: {err}", file=sys.stderr)

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
