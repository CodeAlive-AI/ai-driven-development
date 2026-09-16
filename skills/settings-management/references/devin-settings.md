# Devin CLI / Desktop settings

Devin CLI (and Devin Desktop, which embeds it) uses JSON config. The same
`config.json` schema applies on every surface.

## File locations

| Scope | Path | Shared? |
|-------|------|---------|
| User | `~/.config/devin/config.json` (`%APPDATA%\devin\config.json` on Windows) | No |
| Project | `.devin/config.json` | Yes (committed) |
| Project local | `.devin/config.local.json` | No (gitignored) |
| MCP (user) | `~/.config/devin/mcp_config.json` (`%APPDATA%\devin\mcp_config.json`) | No |
| MCP (project) | `.devin/mcp_config.json`, `.devin/mcp_config.local.json` | mixed |

**Precedence** (lowest → highest): user → project → project-local → env/CLI
flags. `permissions`, `read_config_from`, and `hooks` are the only keys allowed
in project configs; everything else is user-only.

## Key options (user config)

| Key | Type | Notes |
|-----|------|-------|
| `agent.model` | string | Default model (e.g. `"swe-2-high"`) |
| `agent.show_history_on_continue` | bool | Replay transcript on resume |
| `theme_mode` | string | `null`/`light`/`dark`/`terminal-dark`/`terminal-light`/`nocolor` |
| `permissions` | object | `allow`/`deny`/`ask` lists, e.g. `"Exec(git)"`, `"Write(**/.env*)"` |
| `hooks` | object | Lifecycle hooks (prefer `.devin/hooks.v1.json` for projects) |
| `read_config_from` | object | Import rules/hooks/subagents from `cursor`, `windsurf`, `claude` (all default `true`) |
| `notify` | object | Desktop/terminal notifications |
| `proxy` | object | Outbound HTTP/HTTPS proxy for CLI traffic |
| `sandbox` | object | `allowed_domains`, `denied_domains`, `network_mode` (`full`/`limited`) |
| `subagents_enabled` | bool | Toggle subagent support |
| `auto_update`, `keymap`, `show_path`, `show_hints`, `unicode_mode`, `include_gitignored_files`, `respect_gitignore`, `attribution` | misc UI/workspace toggles |

## Related locations

- Skills: `.agents/skills/` and `.devin/skills/` and `.windsurf/skills/` (project); `~/.agents/skills/`, `~/.config/devin/skills/` (`%APPDATA%\devin\skills\`), `~/.codeium/<channel>/skills/` (global)
- Subagents: `.devin/agents/<name>.md` or `.devin/agents/<name>/AGENT.md`, `.agents/agents/`, `~/.config/devin/agents/`
- Rules: `AGENTS.md` at project root; user-level `~/.config/devin/AGENTS.md`
- Hooks: `.devin/hooks.v1.json` (recommended) or `"hooks"` in config files
- Plugins: `.devin-plugin/plugin.json` manifest inside a plugin source; `devin plugins` CLI

Restart the CLI/Desktop session after config changes — settings load at startup.
