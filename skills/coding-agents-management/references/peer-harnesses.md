# Peer Coding-Agent Harnesses (Porch Parity)

Configuration paths for schemas outside the 5 primary agents in `SKILL.md`.

## Contents

- [Summary Matrix](#summary-matrix)
- [Grok Build (`grok` / `grok-build`)](#grok-build-grok--grok-build)
- [Gemini CLI (`gemini-cli` / `gemini`)](#gemini-cli-gemini-cli--gemini)
- [Cursor IDE & CLI (`cursor` / `cursor-cli`)](#cursor-ide--cli-cursor--cursor-cli)
- [Qwen Code (`qwen-code`)](#qwen-code-qwen-code)
- [Kimi Code CLI (`kimi-code`)](#kimi-code-cli-kimi-code)
- [Hermes Agent (`hermes` / `hermes-agent`)](#hermes-agent-hermes--hermes-agent)
- [Oh My Pi (`omp`)](#oh-my-pi-omp)
- [Claude Desktop (`claude-desktop`)](#claude-desktop-claude-desktop)

---

## Summary Matrix

| Agent / Harness | Env Override | MCP Config | Hooks | Settings / Rules |
|---|---|---|---|---|
| **Grok Build** | `$GROK_HOME` (`~/.grok`) | `.mcp.json` bridged, `grok mcp` | `.grok/hooks/` (`SessionStart`, `PreToolUse`, `PostToolUse`) | `~/.grok/config.toml`, `.grok/config.toml`, `AGENTS.md` |
| **Gemini CLI** | — | `~/.gemini/settings.json`, `.gemini/settings.json` (`mcpServers`) | Extension `hooks/hooks.json` (`BeforeTool`, `AfterTool`, `BeforeAgent`, `SessionStart`) | `~/.gemini/settings.json`, `GEMINI.md` |
| **Cursor** | `$CURSOR_CONFIG_DIR` / `$XDG_CONFIG_HOME/cursor` | `~/.cursor/mcp.json`, `.cursor/mcp.json` | `.cursor/hooks.json` (`afterFileEdit`, `beforeMCPExecution`) | `.cursor/rules/*.mdc` (`alwaysApply`, `globs`) |
| **Qwen Code** | — | `~/.qwen/settings.json` (`mcpServers`) | `~/.qwen/settings.json` (`hooks`, `disableAllHooks`) | `~/.qwen/settings.json` |
| **Kimi Code CLI** | `$KIMI_CODE_HOME` (`~/.kimi-code`) | `~/.kimi-code/mcp.json`, `/mcp-config` | `[[hooks]]` array in `~/.kimi-code/config.toml` | `~/.kimi-code/config.toml`, `tui.toml` |
| **Hermes Agent** | `$HERMES_HOME` (`~/.hermes`) | `~/.hermes/config.yaml` (`mcp_servers`) | `~/.hermes/hooks/<name>/{HOOK.yaml,handler.py}` | `config.yaml` + `.env` |
| **Oh My Pi (`omp`)** | — | `~/.omp/agent/mcp.json`, `.omp/mcp.json` | `~/.omp/agent/settings.json`, `.omp/settings.json` (`disableAllHooks`) | `.omp/RULES.md`, `.omp/commands/*.md` |

---

## Grok Build (`grok` / `grok-build`)

- **Settings**: `~/.grok/config.toml` and repo-local `.grok/config.toml` (`[models]`, `[tools] respect_gitignore = true`). Session state lives under `~/.grok/sessions/`.
- **MCP**: Bridges `.mcp.json`, Claude configs, and `.cursor/mcp.json`. Manage via `grok mcp add <name>`, `grok mcp enable|disable`, `grok mcp list`, `grok mcp doctor`.
- **Hooks**: Global or `.grok/hooks/` scripts for `SessionStart`, `PreToolUse`, `PostToolUse`.
- **Inspect & capture**: `grok inspect [--json]` prints active skills, rules, plugins, hooks, and MCP servers; `/skillify` saves session playbooks.

## Gemini CLI (`gemini-cli` / `gemini`)

- **Settings & MCP**: JSON in `~/.gemini/settings.json` and `<project>/.gemini/settings.json` under `"mcpServers"` (stdio + HTTP; extension MCPs overridden by local settings). Supports `fastmcp install gemini-cli server.py`.
- **Extensions**: `gemini extensions install|config`, `/extensions list`. Extension secrets go to OS keychain, never plaintext JSON.
- **Hooks**: `SessionStart`, `SessionEnd`, `BeforeAgent`, `AfterAgent`, `BeforeModel`, `AfterModel`, `BeforeToolSelection`, `BeforeTool`, `AfterTool`; extension-bundled in `hooks/hooks.json` using `${extensionPath}/scripts/...`.

## Cursor IDE & CLI (`cursor` / `cursor-cli`)

- **Home resolution**: `$CURSOR_CONFIG_DIR` -> `$XDG_CONFIG_HOME/cursor` -> `~/.cursor` (important when running isolated `CURSOR_CONFIG_DIR` instances).
- **MCP & Hooks**: `.cursor/mcp.json` (`mcpServers`, shared between IDE & `agent` CLI), `.cursor/hooks.json` (`hooks.afterFileEdit`, `beforeMCPExecution` JSON over stdio).
- **Rules**: `.cursor/rules/*.mdc` with YAML frontmatter (`description`, `globs`, `alwaysApply`).
- **CLI**: `agent -p [--force] [--output-format json] "..."`.

## Qwen Code (`qwen-code`)

- **Settings, MCP & Hooks**: All inside `~/.qwen/settings.json` (and project overrides): `"mcpServers"` (stdio, SSE, Streamable HTTP; manage with `qwen mcp add`), `"hooks"` (`PreToolUse`, `PostToolUse`, session lifecycle with `matcher` + `command`), and `"disableAllHooks": true` safety kill-switch. Inspect read-only inside TUI via `/hooks`.

## Kimi Code CLI (`kimi-code`)

- **Settings**: `$KIMI_CODE_HOME/config.toml` (default `~/.kimi-code/config.toml`) with `default_model`, `default_permission_mode`. Successor to legacy Python `kimi-cli` (`~/.kimi/`).
- **MCP**: `~/.kimi-code/mcp.json` (stdio or remote); interactive management via `/mcp-config`.
- **Hooks**: TOML array of tables `[[hooks]]` in `config.toml` (`event`, regex `matcher`, `command`, `timeout`). Exit `0` = allow, exit `2` = block, other non-zero fail-open.

## Hermes Agent (`hermes` / `hermes-agent`)

- **Config separation**: Non-secret settings and `mcp_servers` live in `~/.hermes/config.yaml`; secrets/API keys live strictly in `~/.hermes/.env`. `hermes import-agent claude-code` migrates MCPs.
- **Gateway Hooks**: Placed in `~/.hermes/hooks/<hook_name>/` containing `HOOK.yaml` (non-empty `events` list) and in-process `handler.py`.
- **Skills nuance**: Hermes discovers `~/.agents/skills` **only** when listed under `skills.external_dirs` in `config.yaml`, and trusts project `.hermes/skills` only after `hermes skills trust`.

## Oh My Pi (`omp`)

- **MCP**: `~/.omp/agent/mcp.json`, project `.omp/mcp.json` (fallback `.omp/.mcp.json`) with `"mcpServers"`; also auto-discovers `.claude`/`.cursor` configs. Inspect effective config via `omp config list --json`.
- **Hooks & Rules**: Hooks configured in `~/.omp/agent/settings.json` and `.omp/settings.json` (`"disableAllHooks": true` kill-switch; ecosystem packages support Claude-style lifecycle events). Project instructions in `.omp/RULES.md` and slash commands in `.omp/commands/*.md`.

## Claude Desktop (`claude-desktop`)

- **Code tab (`code-sessions`)**: Reads `~/.claude.json`, `~/.claude/settings.json`, `~/.claude/skills/`, and project `.mcp.json`/`.claude/` identically to Claude Code.
- **Cowork (`local-agent-mode-sessions`)**: Skills uploaded in Desktop UI (`Customize -> Skills`) are cloud-synced to the user account rather than editable under `~/.claude/skills/`.
