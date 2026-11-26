---
name: coding-agents-management
description: Manages MCP servers, lifecycle hooks, agent settings, permissions, rules, and plugins across Antigravity (App 2.0, IDE, CLI agy), Claude Code, Codex CLI/App, OpenCode, Devin, Cursor, and VS Code. Use when adding or debugging MCP servers, automating tool hooks, configuring TOML/JSON/JSONC settings and sandboxes, or scaffolding, validating, and publishing plugins. Do not use for authoring, auditing, optimizing, or deduplicating standalone SKILL.md skills — use skills-management instead.
---

# Coding Agents Management

> Unified configuration, automation, settings, and plugin operations across **Antigravity (`agy` / App 2.0 / IDE)**, **Claude Code**, **Codex CLI / App**, **OpenCode**, **Devin**, and peer coding agents.

## Contents

- [Surface & Scope Matrix](#surface--scope-matrix)
- [MCP Servers](#mcp-servers)
- [Lifecycle Hooks](#lifecycle-hooks)
- [Settings, Policies & Rules](#settings-policies--rules)
- [Plugins & Validation](#plugins--validation)
- [References](#references)

---

## Surface & Scope Matrix

| Agent | MCP Config | Hooks Config | Settings / Rules | Plugin Manifest |
|-------|------------|--------------|------------------|-----------------|
| **Antigravity** | `~/.gemini/config/mcp_config.json`, `.agents/mcp_config.json` | `~/.gemini/config/hooks.json`, `.agents/hooks.json` | `~/.gemini/antigravity-cli/settings.json`, `.antigravity/settings.json`, `AGENTS.md` | `<plugin>/plugin.json` (JSONC) |
| **Claude Code** | `~/.claude.json`, `.mcp.json` | `~/.claude/settings.json`, `.claude/settings.json` (`hooks`) | `~/.claude/settings.json`, `.claude/settings.json`, `CLAUDE.md` | `<plugin>/.claude-plugin/plugin.json` |
| **Codex CLI / App** | `~/.codex/config.toml`, `.codex/config.toml` | `~/.codex/hooks.json`, `.codex/hooks.json` | `~/.codex/config.toml`, `.codex/config.toml`, `AGENTS.md` | — |
| **OpenCode** | `~/.config/opencode/opencode.json`, `opencode.json` | Plugin SDK events in `.opencode/plugins/` | `~/.config/opencode/opencode.json`, `opencode.json` | npm package or `.opencode/plugins/` |
| **Devin CLI / Desktop** | `~/.config/devin/mcp_config.json`, `.devin/mcp_config.json` | Hooks inside Devin `config.json` | `~/.config/devin/config.json`, `.devin/config.json` | `.devin-plugin/plugin.json` |

---

## MCP Servers

1. **Multi-agent install (Streamable HTTP default):** run `npx add-mcp <source> [-n <name>] [-g]` for npm packages or HTTPS URLs.
2. **Claude Code:** `claude mcp add --transport http -s local|project|user <name> <url>` or `claude mcp add --transport stdio <name> -- <cmd> [args]`. Flags must precede `<name>`.
3. **Antigravity (`agy`):** `agy mcp add [-t http] [-e K=V] [-H "K: V"] <name> <cmdOrUrl> [args...]` (flags before `<name>`). Only Streamable HTTP (`serverUrl`/`url`) and `stdio` are supported natively — bridge legacy `/sse` endpoints with `npx -y mcp-remote <sse-url>`. Plugin `mcp_config.json` uses explicit `"variables"` instead of arbitrary host env vars.
4. **Codex CLI / App:** `codex mcp add <name> --url <url> --bearer-token-env-var ENV_VAR`. Restart Codex App after adding, removing, or logging into (`codex mcp login <name>`) a server so active threads reload its tools.

---

## Lifecycle Hooks

- **Antigravity:** Top-level named-hook map in `hooks.json` (`{"hook-name": {"enabled": true, "PreToolUse": [...]}}`), **never** inside `settings.json`, and at plugin root (`<plugin>/hooks.json`), **never** `hooks/hooks.json`. Supports 6 events (`SessionStart`, `PreInvocation`, `PostInvocation`, `Stop`, `PreToolUse`, `PostToolUse`) and synchronous `"command"` handlers using camelCase protojson I/O (`PLUGIN_ROOT`, `PLUGIN_DATA`).
- **Claude Code:** Supports 28 lifecycle events and 5 handler types (`command`, `http`, `mcp_tool`, `prompt`, `agent`; 16 events are command-only). For user confirmations on dangerous actions, emit JSON `PreToolUse` `permissionDecision: "ask"` (check `.claude/settings.local.json` `permissions.allow` if silently bypassed).
- **Codex / OpenCode / Devin:** Codex hooks run via `hooks.json` (enabled by default under canonical `[features].hooks`); OpenCode fires JS/TS plugin events (`tool.execute.*` skips MCP tools — use `permission` config); Devin configures hooks in `config.json`.
- **Validate before enabling:**

```bash
uv run scripts/validate_hooks.py --agent auto path/to/hooks-or-settings.json
```

---

## Settings, Policies & Rules

- **Antigravity:** Sparse JSON in `~/.gemini/antigravity-cli/settings.json` and `.antigravity/settings.json`. Never hand-edit `~/.gemini/config/config.json` (App/plugin state store). Terminal execution policies (`always-proceed`, `request-review`, `strict`, `proceed-in-sandbox`) are managed in App 2.0 Settings UI. Keep each `AGENTS.md` / `.agents/rules/*.md` file under 24 KB within the 20,000-token rules budget.
- **Claude Code:** Merge order goes from user -> project -> local (`settings.local.json`) -> CLI flags -> managed policy. Configure `permissions`, `sandbox`, `env`, and `autoMode` in JSON.
- **Codex:** TOML config in `~/.codex/config.toml` and trusted `.codex/config.toml`. Use `approval_policy = "on-request"` or `"never"`, `sandbox_mode`, and `[profiles.*]`.
- **OpenCode / Devin:** JSON/JSONC (`opencode.json`) with `{env:VAR}` / `{file:path}` substitutions; Devin reads `.claude/` and `AGENTS.md` when `read_config_from` is active.

---

## Plugins & Validation

1. **Scaffold:**
   ```bash
   uv run scripts/init_plugin.py <plugin-name> --agent claude-code|antigravity [--with-hooks] [--with-mcp]
   uv run scripts/init_marketplace.py <marketplace-name> [--with-plugin <plugin-name>]
   ```
2. **Validate locally before committing or tagging:**
   ```bash
   uv run scripts/validate_plugin.py --agent auto ./path/to/plugin
   agy plugin validate ./path/to/plugin --strict --json   # Antigravity native
   claude plugin validate .                               # Claude Code native
   ```
3. **Rule of placement:** Put components (`skills/`, `commands/`, `agents/`, `hooks/`, `hooks.json`, `mcp_config.json`, `.mcp.json`) at plugin **root**, never nested inside `.claude-plugin/`. Use `${CLAUDE_PLUGIN_ROOT}` / `${CLAUDE_PLUGIN_DATA}` (Claude) or `PLUGIN_ROOT` / `PLUGIN_DATA` (Antigravity).
4. **Submit / Import:** Run `uv run scripts/prepare_submission.py <plugin-path>` for Anthropic Directory fields, or `agy plugin import claude|gemini <path>` to convert existing plugins into Antigravity.

---

## References

Load only the reference matching your target surface and subsystem:

| Subsystem | Scope / Agent | Reference |
|-----------|---------------|-----------|
| **Antigravity (All)** | App 2.0, IDE, `agy` CLI schemas & policies | [antigravity-config.md](references/antigravity-config.md) |
| **MCP** | Multi-agent matrix, Codex App caveats, scopes, transports, troubleshooting | [mcp-guide.md](references/mcp-guide.md) |
| **MCP** | Searching servers and popular URLs/packages | [mcp-search.md](references/mcp-search.md) |
| **MCP** | OpenCode MCP schema, OAuth, and CLI | [mcp-opencode.md](references/mcp-opencode.md) |
| **Hooks** | Claude Code 28-event input/output JSON schemas | [hooks-claude-schemas.md](references/hooks-claude-schemas.md) |
| **Hooks** | Claude Code templates, `ask`/`deny`/`defer`, and allow-rule gotcha | [hooks-claude-templates.md](references/hooks-claude-templates.md) |
| **Hooks** | Codex CLI & App `hooks.json` setup and schemas | [hooks-codex.md](references/hooks-codex.md) |
| **Hooks** | OpenCode TypeScript/JS plugin hooks | [hooks-opencode.md](references/hooks-opencode.md) |
| **Hooks** | Devin CLI / Desktop hooks config | [hooks-devin.md](references/hooks-devin.md) |
| **Settings** | Claude Code `settings.json`, permissions, sandbox, env | [settings-claude.md](references/settings-claude.md) |
| **Settings** | Codex CLI TOML config, profiles, features, security | [settings-codex.md](references/settings-codex.md) |
| **Settings** | OpenCode JSON/JSONC settings and permissions | [settings-opencode.md](references/settings-opencode.md) |
| **Settings** | Devin CLI / Desktop settings and `.devin-plugin` | [settings-devin.md](references/settings-devin.md) |
| **Plugins** | Claude Code plugins, marketplaces, submission | [plugins-claude.md](references/plugins-claude.md) |
| **Plugins** | OpenCode npm & local plugin packaging | [plugins-opencode.md](references/plugins-opencode.md) |
| **Migrations** | Legacy SSE, Antigravity gotchas, Codex deprecated keys, `commands/*.md` | [legacy/migrations.md](references/legacy/migrations.md) |
