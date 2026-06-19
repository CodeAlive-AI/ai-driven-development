# Codex CLI / Codex App Hooks Reference

Hook support in [OpenAI Codex](https://github.com/openai/codex). Codex CLI, Codex IDE extension, and Codex App share the same configuration layers under `~/.codex` and trusted project `.codex` directories.

## Contents

- [Current State](#current-state)
- [Enabling Hooks](#enabling-hooks)
- [Hook Events](#hook-events)
- [Configuration Format](#configuration-format)
- [Matchers](#matchers)
- [Blocking and Decision Control](#blocking-and-decision-control)
- [Hook Input Schema](#hook-input-schema)
- [Hook Output Schema](#hook-output-schema)
- [Common Patterns](#common-patterns)
- [Notify Setting](#notify-setting)
- [Rules vs Hooks](#rules-vs-hooks)
- [Comparison with Claude Code](#comparison-with-claude-code)
- [Migration from earlier Codex versions](#migration-from-earlier-codex-versions)
- [Trust Requirements](#trust-requirements)

## Current State

As of **2026-06**, lifecycle hooks are part of current Codex builds and are enabled by default. Codex supports ten lifecycle events and can intercept Bash, `apply_patch` file edits, and MCP tool calls.

What changed in 2026:
- **Feb 2026 (v0.117.0)**: PreToolUse + PostToolUse landed (originally only `SessionStart` and `Stop` existed).
- **Mar 2026 (PR #14626)**: `UserPromptSubmit` hook added.
- **Apr 2026 (v0.124.0)**: Hooks promoted to stable. Inline `[hooks.*]` tables in `config.toml` and `requirements.toml` are now supported in addition to `hooks.json`.
- **May/Jun 2026**: Canonical feature key became `[features].hooks`; `[features].codex_hooks` remains only as a deprecated alias. Non-managed command hooks require explicit review/trust through `/hooks`.

## Enabling Hooks

Hooks are enabled by default. To disable them:

```toml
[features]
hooks = false
```

Use `hooks` as the canonical feature key. `codex_hooks` still works as a deprecated alias in current builds but should not be written by new tooling.

Codex App / IDE and CLI share these config layers. The App settings UI opens the same `~/.codex/config.toml`.

## Hook Events

| Event | Scope | When it fires |
|-------|-------|---------------|
| `SessionStart` | session | Session initialization or resume |
| `SubagentStart` | subagent | Subagent starts |
| `PreToolUse` | turn | Before a tool runs (can block) |
| `PermissionRequest` | turn | When Codex is already about to ask for approval |
| `PostToolUse` | turn | After tool completes |
| `PreCompact` | turn | Before compaction |
| `PostCompact` | turn | After compaction |
| `UserPromptSubmit` | turn | User submits a prompt (can block) |
| `SubagentStop` | subagent | Subagent is about to stop; can request continuation |
| `Stop` | turn | When the agent's turn ends |

**`PreToolUse` interception scope:** Bash commands, file edits via `apply_patch`, and MCP tool calls. It is a guardrail — Codex may still accomplish equivalent work via another tool path, so do not treat hooks as a complete enforcement boundary.

## Configuration Format

Hooks live inline in `config.toml` or in a sibling `hooks.json`. Do **not** mix both representations in the same config layer — Codex loads both and warns.

### Inline TOML

```toml
# PreToolUse: gate Bash commands
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30                           # seconds; default 600
statusMessage = "Checking Bash command"

# PostToolUse: review Bash output
[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"
```

### hooks.json

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "^Bash$",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 ~/.codex/hooks/pre_tool_use_policy.py",
            "timeout": 30,
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ]
  }
}
```

### Enterprise-managed hooks

`requirements.toml` (admin-controlled) supports the same `[hooks.*]` blocks plus managed hook sources. Managed hooks are trusted by policy and cannot be disabled from the user hook browser.

```toml
[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
```

### Concurrency

When the same event matches in multiple config layers (user, project, requirements), **all matching hooks run** — higher-precedence layers do not replace lower ones. Multiple hooks for the same event run **concurrently**; one cannot prevent another from starting.

### Discovery and trust

Useful locations:
- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

Project-local hooks load only when the project `.codex/` layer is trusted. Non-managed command hooks must also be reviewed in `/hooks`; Codex records trust by hook definition hash, so changed hooks are skipped until reviewed again.

## Matchers

The `matcher` field is a regex matched against `tool_name` and tool aliases.

- `matcher = "^Bash$"` — only Bash
- `matcher = ""`, `matcher = "*"`, or omit `matcher` — every event
- `matcher = "apply_patch|Edit|Write"` — file edits via `apply_patch` (the alias also accepts `Edit` and `Write` for parity with Claude Code; `tool_name` in the input is still `apply_patch`)
- `matcher = "mcp__github__.*"` — all tools from a specific MCP server

## Blocking and Decision Control

Codex offers **two blocking mechanisms** for `PreToolUse`: exit code 2 (simple) and JSON `permissionDecision: "deny"` (rich).

### Exit code semantics

| Exit code | Meaning |
|-----------|---------|
| `0` with no output | Allow, continue silently |
| `2` | Block; `stderr` is shown to Codex as the reason |
| Other | Logged as error in verbose mode; non-blocking |

### JSON output (richer control)

PreToolUse and PermissionRequest accept a `hookSpecificOutput` JSON envelope. PostToolUse, UserPromptSubmit, and Stop accept a top-level decision object.

**PreToolUse — block with reason:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked."
  }
}
```

`PreToolUse` does **not** support `permissionDecision: "ask"` as of June 2026. If a hook returns `"ask"`, Codex marks that hook run as failed, reports the error, and continues the tool call. Use Codex approval policy/permissions for native prompts; otherwise choose between hard-blocking (`deny` / exit 2) and advisory context.

**PermissionRequest — deny with user-facing message:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}
```

**UserPromptSubmit — refuse a prompt:**
```json
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}
```

### Common output fields

All events accept these top-level keys:

| Key | Type | Effect |
|-----|------|--------|
| `continue` | boolean | Event-dependent; unsupported on PreToolUse / PermissionRequest |
| `stopReason` | string | Why we stopped (paired with `continue: false`) |
| `systemMessage` | string | Injected as a system note (PostToolUse only fully supports it) |
| `suppressOutput` | boolean | Hide hook stdout from the user (PostToolUse parses but does not currently honor) |

> **Capability gaps as of 2026-06:** `permissionDecision: "ask"`, `continue`, `stopReason`, and `suppressOutput` are **not** supported for PreToolUse. PermissionRequest can allow, deny, or decline to decide, but it only fires when Codex was already about to ask.

## Hook Input Schema

Every event receives JSON on stdin with these common fields:

| Field | Type | Description |
|-------|------|-------------|
| `session_id` | string | Conversation/session ID |
| `transcript_path` | string | Path to the running transcript |
| `cwd` | string | Working directory |
| `hook_event_name` | string | Event name (`PreToolUse`, etc.) |
| `model` | string | Model in use this turn |

### Per-event additions

| Event | Extra fields |
|-------|--------------|
| `SessionStart` | `source` in `startup`, `resume`, `clear`, `compact` |
| `SubagentStart` | `turn_id`, `agent_id`, `agent_type`, `permission_mode` |
| `UserPromptSubmit` | `turn_id`, `prompt` |
| `PreToolUse` | `turn_id`, `tool_name`, `tool_use_id`, `tool_input` |
| `PermissionRequest` | `turn_id`, `tool_name`, `tool_input` (incl. `description`) |
| `PostToolUse` | `turn_id`, `tool_name`, `tool_use_id`, `tool_input`, `tool_response` |
| `PreCompact` / `PostCompact` | `turn_id`, `trigger` (`manual` or `auto`) |
| `SubagentStop` | `turn_id`, `agent_id`, `agent_type`, `agent_transcript_path`, `stop_hook_active`, `last_assistant_message` |
| `Stop` | `turn_id`, `stop_hook_active`, `last_assistant_message` |

## Hook Output Schema

The complete output schema lives in [docs](https://developers.openai.com/codex/hooks). Quick reference:

```json
{
  "continue": true,
  "stopReason": "optional reason",
  "systemMessage": "optional banner",
  "suppressOutput": false,
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny",
    "permissionDecisionReason": "string"
  }
}
```

## Common Patterns

### Block destructive commands

```bash
#!/usr/bin/env python3
# .codex/hooks/pre_tool_use_policy.py
import json, sys

inp = json.load(sys.stdin)
cmd = " ".join(inp.get("tool_input", {}).get("command", []))

if "rm -rf" in cmd or "sudo " in cmd:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Destructive command blocked by hook."
        }
    }))
    sys.exit(0)

sys.exit(0)
```

### Scan for credentials in user prompts

```bash
#!/usr/bin/env python3
# .codex/hooks/scan_prompt.py
import json, sys, re

inp = json.load(sys.stdin)
prompt = inp.get("prompt", "")

if re.search(r"sk-[a-zA-Z0-9]{20,}|AKIA[0-9A-Z]{16}", prompt):
    print(json.dumps({
        "decision": "block",
        "reason": "API key or AWS access key detected in prompt."
    }))
    sys.exit(0)

sys.exit(0)
```

### Log every shell command (PostToolUse, fire-and-forget)

```toml
[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = 'jq -r ".tool_input.command | join(\" \")" >> ~/.codex/command-log.txt'
```

### Auto-format after `apply_patch`

```toml
[[hooks.PostToolUse]]
matcher = "apply_patch"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '~/.codex/hooks/format_changed.sh'
timeout = 60
```

## Notify Setting

Independent of `[hooks]`. Trigger an external program on lifecycle events (still useful for desktop notifications):

```toml
notify = ["notify-send", "Codex"]                         # Linux
notify = ["bash", "-lc", "afplay /System/Library/Sounds/Blow.aiff"]  # macOS

[tui]
notifications = ["agent-turn-complete", "approval-requested"]  # Filter
```

## Rules vs Hooks

Starlark rules in `.codex/rules/` and `~/.codex/rules/` are still useful — they fire **before** the model decides whether to invoke a tool, are cheap, and integrate with smart-approval learning:

```starlark
prefix_rule(
    pattern = ["rm", ["-rf", "-r"]],
    decision = "forbidden",
    justification = "Use git clean -fd instead.",
)
```

Rules cover **command policy** (allow / prompt / forbidden). Hooks cover **scripted automation**: logging, secret scanning, formatting, custom validators. Use both: rules for static policy, hooks for dynamic checks and side effects.

## Comparison with Claude Code

| Feature | Claude Code | Codex CLI / App (2026-06) |
|---------|------------|--------------------|
| **Total events** | 28+ | 10 |
| **PreToolUse blocking** | Full (exit 2 or JSON) | Supports `deny` / exit 2; hook-created `ask` unsupported |
| **PostToolUse** | Full | Full |
| **PreToolUse `updatedInput`** | Yes | Yes for supported tool inputs when paired with `permissionDecision: "allow"` |
| **`additionalContext` injection** | Yes | Yes for supported events |
| **PermissionRequest event** | Equivalent | Yes |
| **UserPromptSubmit** | Yes | Yes |
| **SessionStart / Stop** | Yes | Yes |
| **SubagentStart / SubagentStop** | Yes | Yes |
| **PreCompact / PostCompact** | Yes | Yes |
| **SessionEnd / Notification** | Yes | Not currently |
| **MCP tool interception** | Yes | Yes (in `PreToolUse`) |
| **File edit interception** | Yes (Edit/Write) | Yes (`apply_patch`) |
| **Concurrent hooks** | Yes | Yes |
| **Config format** | JSON (`settings.json`) | TOML (`[hooks.*]` in `config.toml`) or `hooks.json` |
| **Config locations** | `~/.claude/settings.json`, `.claude/settings.json` | `~/.codex/config.toml`, `~/.codex/hooks.json`, project `.codex/*`, managed config |
| **Trust gating** | None for user scope | Project `.codex` must be trusted; non-managed command hooks require `/hooks` review |

## Migration from earlier Codex versions

If you previously used `AfterAgent` / `AfterToolUse` (the original fire-and-forget events), migrate to the stable equivalents:

| Legacy event | Replace with |
|--------------|--------------|
| `AfterAgent` | `Stop` |
| `AfterToolUse` | `PostToolUse` |

Legacy fields:
- `hook_event` → `hook_event_name`
- `thread_id` → `session_id`
- `triggered_at` → not provided; compute in your hook if needed
- Argv-style payload → all events now read JSON from stdin

## Trust Requirements

- **User-level hooks** (`~/.codex/config.toml`, `~/.codex/hooks.json`): always loaded.
- **Project-level hooks** (`.codex/config.toml`, `.codex/hooks.json`): loaded **only** for trusted projects. Use `codex trust` (or accept the trust prompt) to enable.
- **Managed hooks** (`requirements.toml` + `managed_dir`): always loaded; not user-overridable.

## Sources

- [Codex hooks docs](https://developers.openai.com/codex/hooks)
- [Codex configuration reference](https://developers.openai.com/codex/config-reference)
- [Codex changelog](https://developers.openai.com/codex/changelog)
- [Codex Desktop hook regression report — openai/codex#21639](https://github.com/openai/codex/issues/21639)
