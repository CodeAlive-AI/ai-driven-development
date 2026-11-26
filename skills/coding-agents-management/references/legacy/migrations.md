# Coding Agents Configuration Migration Guide

> Historical deprecations, broken patterns, and step-by-step upgrades for MCP, Hooks, Settings, and Plugins across coding agents.

## Contents

- [MCP: Legacy SSE to Streamable HTTP / `mcp-remote`](#mcp-legacy-sse-to-streamable-http--mcp-remote)
- [Antigravity: Inert Keys & Plugin Hook/MCP Layout Fixes](#antigravity-inert-keys--plugin-hookmcp-layout-fixes)
- [Codex CLI: Deprecated Feature Keys & Hook/Approval Names](#codex-cli-deprecated-feature-keys--hookapproval-names)
- [Claude Code: Commands to Skills & Plugin Portability](#claude-code-commands-to-skills--plugin-portability)
- [Devin CLI / Desktop: Moving `mcpServers` Out of `config.json`](#devin-cli--desktop-moving-mcpservers-out-of-configjson)

---

## MCP: Legacy SSE to Streamable HTTP / `mcp-remote`

- **Change:** MCP deprecated raw SSE remote transport in favor of **Streamable HTTP**. Antigravity does not accept SSE directly, and Codex only supports Streamable HTTP cleanly.
- **How to migrate:**
  1. Switch endpoint URLs from `/sse` to `/mcp` (when supported by the provider) and update transport type:
     - Claude Code: `"type": "sse"` -> `"type": "http"` (`claude mcp add --transport http ...`)
     - Antigravity: `agy mcp add -t http <name> https://host/mcp`
     - Codex TOML: use `url = "https://host/mcp"`
  2. If a third-party server strictly serves SSE with no `/mcp` endpoint, wrap it locally with `mcp-remote`:
     ```json
     {
       "mcpServers": {
         "legacy-sse": {
           "command": "npx",
           "args": ["-y", "mcp-remote", "https://example.com/sse"]
         }
       }
     }
     ```

---

## Antigravity: Inert Keys & Plugin Hook/MCP Layout Fixes

| Legacy / Claude Habit | Why It Fails in Antigravity | Native Fix |
|-----------------------|-----------------------------|------------|
| Placing `"hooks": {...}` inside `settings.json` | Antigravity ignores `"hooks"` in `settings.json` | Move hooks into `~/.gemini/config/hooks.json` or `.agents/hooks.json` |
| Placing plugin hooks at `hooks/hooks.json` | Native Antigravity plugins read `hooks.json` at plugin **root** | Move `hooks/hooks.json` -> `hooks.json` (or import via `agy plugin import claude`) |
| Wrapping Antigravity `hooks.json` in `{"hooks": {"PreToolUse": ...}}` | Antigravity uses a named-hook map at root, not a `"hooks"` wrapper | Use `{"my-hook": {"enabled": true, "PreToolUse": [...]}}` |
| Using `ephemeralMessage` in Antigravity hook output | Unsupported field name | Use camelCase protojson fields (`decision`, `reason`, `overwrite`, `injectSteps`, `continuationActive`) |
| Hand-editing `~/.gemini/config/config.json` | Corrupts internal state and plugin/extension registry | Use `agy plugin enable|disable|install|uninstall` or Plugins Manager UI |
| Relying on `$HOST_ENV_VAR` in plugin `mcp_config.json` | Plugin MCP configs do not auto-expand arbitrary OS env vars | Declare secrets in server `"variables"` or plugin auth providers |
| Keeping custom arbitrary keys in `plugin.json` | Unknown top-level fields are silently discarded | Stick to documented schema (`name`, `displayName`, `version`, `description`, `logo`, `suggestedPrompts`, `skills`, `extensions`, etc.) |

---

## Codex CLI: Deprecated Feature Keys & Hook/Approval Names

- **`[features].codex_hooks = true` -> `[features].hooks` (enabled by default):** `codex_hooks` was replaced by canonical `[features].hooks`, and lifecycle hooks are enabled by default in modern builds. Remove `codex_hooks = true` from new configs unless targeting pinned legacy versions.
- **`approval_policy = "on-failure"` -> `"on-request"` or `"never"`:** `"on-failure"` is deprecated and scheduled for removal in TOML config.
- **Hook event & JSON field renames from early builds:**
  - Early snake-case or Claude names like `AfterAgent` / `AfterToolUse` map to **`Stop`** and **`PostToolUse`** in `hooks.json`.
  - Use `hooks.json` (project `.codex/hooks.json` or user `~/.codex/hooks.json`) matching Codex's official schemas (`SessionStart`, `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `PermissionRequest`).

---

## Claude Code: Commands to Skills & Plugin Portability

- **`commands/*.md` -> `skills/<name>/SKILL.md`:** Custom slash commands under `commands/*.md` still work, but new plugins should author **skills** (`skills/<name>/SKILL.md`), which support progressive disclosure, scripts, references, and cross-agent discovery via `.agents/skills/`.
- **Legacy relative paths in hooks/MCP (`./scripts/...`) -> `${CLAUDE_PLUGIN_ROOT}` / `${CLAUDE_PLUGIN_DATA}`:** Claude Code caches installed plugins cleanly by version; bare relative paths fail after plugin installation. Always prefix plugin hook/MCP paths with `${CLAUDE_PLUGIN_ROOT}` (or `PLUGIN_ROOT` in Antigravity).
- **HTTP remote MCP in `.mcp.json`:** Modern plugins frequently ship HTTP remote MCP servers (`{"type": "http", "url": "..."}`) without any `"command"` field — validators must accept both `stdio` and `http`.

---

## Devin CLI / Desktop: Moving `mcpServers` Out of `config.json`

- Older Devin builds stored `mcpServers` inside `config.json`.
- Current Devin CLI / Desktop (`v3000.3` / Local `3.6`+) reads MCP servers from dedicated **`~/.config/devin/mcp_config.json`** and workspace **`.devin/mcp_config.json`** / `.devin/mcp_config.local.json`.
- If upgrading an older setup, move `"mcpServers"` out of `config.json` into `mcp_config.json` cleanly so edits in one place do not conflict with migrated entries.
