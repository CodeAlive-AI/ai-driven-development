# Devin CLI hooks

Devin CLI/Desktop hooks are JSON-configured and fire on lifecycle events.
The format is close to Claude Code's but not identical — read the event table
before porting a hook.

## Where hooks live

Project level (discovered in the working directory and ancestors up to the
repository root):

| File | Format |
|------|--------|
| `.devin/hooks.v1.json` | Standalone hooks file — the whole file is the hooks object (recommended) |
| `.devin/config.json` | `"hooks"` key |
| `.devin/config.local.json` | `"hooks"` key (gitignored) |
| `.claude/settings.json` / `.claude/settings.local.json` | `"hooks"` key — Claude Code format is picked up automatically |

User level:

| File | Format |
|------|--------|
| `~/.config/devin/config.json` (`%APPDATA%\devin\config.json` on Windows) | `"hooks"` key |
| `~/.claude.json`, `~/.claude/settings.json`, `~/.claude/settings.local.json` | `"hooks"` key (imported) |

## Events

| Event | Fires |
|-------|-------|
| `PreToolUse` | Before a tool executes (can rewrite input via `updatedInput`) |
| `PostToolUse` | After a tool finishes |
| `PermissionRequest` | When a permission decision is needed |
| `UserPromptSubmit` | On user message submit (`additionalContext` injects context) |
| `Stop` | When the agent wants to stop (can block to force follow-up) |
| `PostCompaction` | After context compaction completes |
| `SessionStart` | Session begin (no `prompt_id` yet) |
| `SessionEnd` | Session end |

## Hook entry format

```json
{
  "PreToolUse": [
    {
      "matcher": "Exec",
      "hooks": [
        { "type": "command", "command": "./scripts/check-command.sh" }
      ]
    }
  ]
}
```

- `matcher` — regex against the event's `tool_name`; empty/omitted matches all.
- `type` — `command` (runs a shell command) or `prompt`.
- Command hooks get event JSON on **stdin**; every payload carries `session_id`
  (stable) and `prompt_id` (rotated per user prompt, absent before the first
  prompt).
- Exit code `0` = ok, non-zero = block the action.

## Stdout control contract

Print a JSON object to stdout to influence the run:

| Field | Effect |
|-------|--------|
| `hookSpecificOutput.hookEventName` | Event the output applies to |
| `hookSpecificOutput.additionalContext` | Injected into context (`UserPromptSubmit`, `SessionStart`, `PostToolUse`) |
| `hookSpecificOutput.updatedInput` | Merged into tool args before execution (`PreToolUse` only) |

## Notes

- `Stop` hooks that block can loop the agent — ensure the condition converges.
- `.local.` in any config filename marks a gitignored personal override.
- Changes require a session restart to take effect.
