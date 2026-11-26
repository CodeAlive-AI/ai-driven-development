---
name: coding-agents-management
description: Manages MCP servers, lifecycle hooks, agent settings, permissions, rules, and plugins across Antigravity (App 2.0, IDE, CLI agy), Claude Code/Desktop, Codex CLI/App, OpenCode, Devin, Cursor, Grok Build, Gemini CLI, Qwen Code, Kimi Code, Hermes, Oh My Pi (omp), and VS Code. Use when adding or debugging MCP servers, automating tool hooks, configuring TOML/JSON/JSONC settings and sandboxes, or scaffolding, validating, and publishing plugins. Do not use for authoring, auditing, optimizing, or deduplicating standalone SKILL.md skills — use skills-management instead.
---

# Coding Agents Management

> Unified MCP, hooks, settings/rules, and plugin management across **Antigravity (`agy` / App 2.0 / IDE)**, **Claude Code**, **Codex**, **OpenCode**, **Devin**, **Cursor**, **Grok**, **Gemini CLI**, **Qwen**, **Kimi**, **Hermes**, and **Oh My Pi (`omp`)**.

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
| **Claude Code / Desktop Code** | `~/.claude.json`, `.mcp.json` | `~/.claude/settings.json`, `.claude/settings.json` (`hooks`) | `~/.claude/settings.json`, `.claude/settings.json`, `CLAUDE.md` | `<plugin>/.claude-plugin/plugin.json` |
| **Codex CLI / App** | `~/.codex/config.toml`, `.codex/config.toml` | `~/.codex/hooks.json`, `.codex/hooks.json` | `~/.codex/config.toml`, `.codex/config.toml`, `AGENTS.md` | — |
| **OpenCode** | `~/.config/opencode/opencode.json`, `opencode.json` | Plugin SDK events in `.opencode/plugins/` | `~/.config/opencode/opencode.json`, `opencode.json` | npm package or `.opencode/plugins/` |
| **Devin CLI / Desktop** | `~/.config/devin/mcp_config.json`, `.devin/mcp_config.json` | Devin `config.json` | `~/.config/devin/config.json`, `.devin/config.json` | `.devin-plugin/plugin.json` |
| **Peers (`grok`, `gemini-cli`, `cursor`, `qwen`, `kimi`, `hermes`, `omp`)** | `mcp.json` / `settings.json` / `config.yaml` (see [peer-harnesses.md](references/peer-harnesses.md)) | `.grok/hooks/`, `.cursor/hooks.json`, `[[hooks]]`, `HOOK.yaml` | `config.toml` / `settings.json` / `.cursor/rules/*.mdc` | Harness extension/plugin dirs |

---

## MCP Servers

1. **Cross-agent:** `npx add-mcp <source> [-n <name>] [-g]` (Streamable HTTP default).
2. **Claude Code:** `claude mcp add --transport http|stdio -s local|project|user <name> ...` (flags before `<name>`).
3. **Antigravity (`agy`):** `agy mcp add [-t http] [-e K=V] [-H "K: V"] <name> <cmdOrUrl> [args...]` (flags before `<name>`). Native transports: Streamable HTTP (`serverUrl`/`url`) and `stdio`; bridge `/sse` with `npx -y mcp-remote <url>`. Plugin `mcp_config.json` needs explicit `"variables"`.
4. **Codex:** `codex mcp add <name> --url <url> --bearer-token-env-var ENV_VAR`. Restart Codex App after add/remove/`codex mcp login`.

---

## Lifecycle Hooks

- **Antigravity:** Top-level named-hook map in `hooks.json` (`{"name": {"enabled": true, "PreToolUse": [...]}}`), **never** in `settings.json`, always at plugin root `<plugin>/hooks.json` (never `hooks/hooks.json`). Supports 6 events (`SessionStart`, `PreInvocation`, `PostInvocation`, `Stop`, `PreToolUse`, `PostToolUse`), synchronous `"command"` handlers, camelCase protojson I/O (`PLUGIN_ROOT`, `PLUGIN_DATA`).
- **Claude Code:** 28 events, 5 handler types (`command`, `http`, `mcp_tool`, `prompt`, `agent`; 16 command-only). Emit `PreToolUse` `permissionDecision: "ask"` for confirmations (check `.claude/settings.local.json` `permissions.allow` if bypassed).
- **Codex / OpenCode / Devin / Peers:** Codex uses `hooks.json` (`[features].hooks`); OpenCode uses JS/TS plugins (`tool.execute.*` skips MCP tools); Devin uses `config.json`.

```bash
uv run scripts/validate_hooks.py --agent auto path/to/hooks-or-settings.json
```

---

## Settings, Policies & Rules

- **Antigravity:** Sparse JSON in `~/.gemini/antigravity-cli/settings.json` and `.antigravity/settings.json`. Never hand-edit `~/.gemini/config/config.json`. Terminal policies live in App 2.0 UI. Keep `AGENTS.md`/`.agents/rules/*.md` `<24 KB` within the 20,000-token budget.
- **Claude / Codex / OpenCode / Devin / Peers:** Claude merges user -> project -> local -> CLI -> managed (`permissions`, `sandbox`, `env`, `autoMode`). Codex uses trusted `config.toml` (`approval_policy`, `sandbox_mode`, `[profiles.*]`). OpenCode uses JSON/JSONC (`{env:VAR}`, `{file:path}`). Devin reads `.claude/` & `AGENTS.md` via `read_config_from`. See [peer-harnesses.md](references/peer-harnesses.md) for Grok/Gemini/Cursor/Qwen/Kimi/Hermes/OMP.

---

## Plugins & Validation

1. **Scaffold:** `uv run scripts/init_plugin.py <name> --agent claude-code|antigravity [--with-hooks] [--with-mcp]` · `init_marketplace.py <name>`
2. **Validate:** `uv run scripts/validate_plugin.py --agent auto ./path/to/plugin` · `agy plugin validate ... --strict --json` · `claude plugin validate .`
3. **Placement:** Put `skills/`, `commands/`, `agents/`, `hooks/`, `hooks.json`, `mcp_config.json`, `.mcp.json` at plugin **root**, never inside `.claude-plugin/`. Use `${CLAUDE_PLUGIN_ROOT}`/`${CLAUDE_PLUGIN_DATA}` or `PLUGIN_ROOT`/`PLUGIN_DATA`.
4. **Submit / Import:** `uv run scripts/prepare_submission.py <plugin-path>` or `agy plugin import claude|gemini <path>`.

---

## References

Load **only** the reference matching the target agent and subsystem:

| Subsystem | Scope / Agent | Reference |
|-----------|---------------|-----------|
| **Antigravity (All)** | App 2.0, IDE, `agy` CLI schemas & policies | [antigravity-config.md](references/antigravity-config.md) |
| **Peer Harnesses** | Grok, Gemini CLI, Cursor, Qwen, Kimi, Hermes, OMP, Claude Desktop | [peer-harnesses.md](references/peer-harnesses.md) |
| **MCP** | Multi-agent matrix, Codex App caveats, scopes, transports, search, OpenCode | [mcp-guide.md](references/mcp-guide.md) · [mcp-search.md](references/mcp-search.md) · [mcp-opencode.md](references/mcp-opencode.md) |
| **Hooks** | Claude Code schemas/templates; Codex, OpenCode, Devin hooks | [hooks-claude-schemas.md](references/hooks-claude-schemas.md) · [hooks-claude-templates.md](references/hooks-claude-templates.md) · [hooks-codex.md](references/hooks-codex.md) · [hooks-opencode.md](references/hooks-opencode.md) · [hooks-devin.md](references/hooks-devin.md) |
| **Settings** | Claude Code, Codex, OpenCode, Devin settings & permissions | [settings-claude.md](references/settings-claude.md) · [settings-codex.md](references/settings-codex.md) · [settings-opencode.md](references/settings-opencode.md) · [settings-devin.md](references/settings-devin.md) |
| **Plugins** | Claude Code & OpenCode packaging and submission | [plugins-claude.md](references/plugins-claude.md) · [plugins-opencode.md](references/plugins-opencode.md) |
| **Migrations** | Legacy SSE, Antigravity gotchas, Codex deprecated keys, `commands/*.md` | [legacy/migrations.md](references/legacy/migrations.md) |
