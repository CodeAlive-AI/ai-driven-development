# Antigravity Configuration Reference

> Unified configuration spec for **Antigravity App (2.0)**, **Antigravity IDE**, and **Antigravity CLI (`agy`)**.

## Contents

- [Architecture & Config Precedence](#architecture--config-precedence)
- [MCP Servers (`mcp_config.json` & `agy mcp`)](#mcp-servers-mcp_configjson--agy-mcp)
- [Hooks (`hooks.json`)](#hooks-hooksjson)
- [Settings, Policies & Rules (`AGENTS.md`)](#settings-policies--rules-agentsmd)
- [Plugins (`plugin.json` & `agy plugin`)](#plugins-pluginjson--agy-plugin)
- [UI Navigation & Discovery in Agent Replies](#ui-navigation--discovery-in-agent-replies)

---

## Architecture & Config Precedence

Antigravity shares core customization primitives across **App (2.0)**, **IDE**, and **CLI (`agy`)** while keeping surface-specific UI/settings files:

| Artifact | Global / User Path | Workspace / Project Path | Plugin Path |
|----------|--------------------|--------------------------|-------------|
| **MCP Servers** | `~/.gemini/config/mcp_config.json` | `<workspace>/.agents/mcp_config.json` | `<plugin>/mcp_config.json` |
| **Hooks** | `~/.gemini/config/hooks.json` | `<workspace>/.agents/hooks.json` | `<plugin>/hooks.json` *(root only)* |
| **Skills** | `~/.gemini/config/skills/` *(plus shared `~/.agents/skills/`)* | `<workspace>/.agents/skills/` | `<plugin>/skills/` *(or `plugin.json` `skills`)* |
| **Rules / Memory** | `~/.gemini/GEMINI.md` | `<workspace>/.agents/rules/*.md`, `<workspace>/AGENTS.md` | `<plugin>/rules/` |
| **Workflows** | `~/.gemini/config/global_workflows/` | `<workspace>/.agents/workflows/` | — |
| **Plugin Manifest** | — | — | `<plugin>/plugin.json` |
| **Plugin Registry / Toggles** | `~/.gemini/config/config.json` *(managed by AGY — never hand-edit)* | — | — |
| **CLI Settings** | `~/.gemini/antigravity-cli/settings.json` | `<workspace>/.antigravity/settings.json` | — |

### Precedence Order

1. **Workspace customizations** (`.agents/` inside the workspace) override user customizations for the same resource.
2. **User customizations** (`~/.gemini/config/`, `~/.gemini/GEMINI.md`).
3. **Installed plugins** (`<plugin>/` enabled in `config.json`). For MCP server name collisions, project overrides user/plugin; across plugins, enable/disable cleanly instead of duplicating names.

> **Never hand-edit `~/.gemini/config/config.json`.** It holds internal plugin state and `extensions` arrays; use `agy plugin enable/disable/install/uninstall` or the Antigravity UI instead.

---

## MCP Servers (`mcp_config.json` & `agy mcp`)

### File Schema

`mcp_config.json` uses `"mcpServers"` as its top-level key across user, workspace, and plugin scopes:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"],
      "env": {
        "LOG_LEVEL": "info"
      }
    },
    "remote-docs": {
      "serverUrl": "https://docs.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${API_TOKEN}"
      },
      "disabled": false
    }
  }
}
```

### Transport & Auth Rules

- **Local (`stdio`):** Requires `"command"` (string) and optional `"args"` (string array), `"env"` (string map), `"cwd"`, `"disabled"` (bool).
- **Remote (`Streamable HTTP`):** Uses `"serverUrl"` (or `"url"`) + optional `"headers"`. **Legacy SSE (`/sse`) is unsupported directly** — bridge legacy SSE endpoints with `npx -y mcp-remote <sse-url>` as a `stdio` server.
- **Plugin `mcp_config.json` variables:** Plugin MCP configs do **not** inherit arbitrary host OS environment variables. Declare user-supplied secrets in a `"variables"` map on the server entry (or use the plugin account/auth provider flow) rather than assuming `$ENV_VAR` expansion will resolve host shell vars.
- **OAuth / Sign-In:** Authenticated HTTP MCP servers connect through Antigravity's built-in OAuth/plugin auth flow when configured.

### CLI Management (`agy mcp`)

Place flags **before** `<name>` (CLI flag parser stops parsing flags after positional arguments):

```bash
# Add stdio server (flags before name)
agy mcp add -e API_KEY=xxx my-server npx -y @org/my-mcp

# Add remote Streamable HTTP server (HTTP URLs are auto-detected; -t http is explicit)
agy mcp add -t http -H "Authorization: Bearer token" my-api https://api.example.com/mcp

# Inspect & toggle
agy mcp list
agy mcp enable my-server
agy mcp disable my-server
agy mcp remove my-server
```

---

## Hooks (`hooks.json`)

> **Important:** Antigravity `settings.json` ignores any `"hooks"` key. Hooks load exclusively from `~/.gemini/config/hooks.json`, `<workspace>/.agents/hooks.json`, and `<plugin>/hooks.json` (at the **plugin root** — never `hooks/hooks.json` in native plugins).

### Named-Hook Map Structure

The top-level JSON object maps unique **hook names** to hook definitions (NOT `{"hooks": {...}}` like Claude Code):

```json
{
  "guard-destructive-shell": {
    "enabled": true,
    "PreToolUse": [
      {
        "matcher": "run_command",
        "hooks": [
          {
            "type": "command",
            "command": "./scripts/guard-shell.sh",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "session-audit": {
    "enabled": true,
    "SessionStart": [
      {
        "type": "command",
        "command": "node ./scripts/log-start.mjs"
      }
    ]
  }
}
```

### Supported Events & Handler Shapes

| Event | Shape | When It Fires |
|-------|-------|---------------|
| `SessionStart` | Flat array of handler objects `[{"command": ...}]` | Session initialization |
| `PreInvocation` | Flat array of handler objects | Before model invocation turn |
| `PostInvocation` | Flat array of handler objects | After model invocation finishes |
| `Stop` | Flat array of handler objects | Agent is about to stop responding |
| `PreToolUse` | Array of matcher blocks `[{"matcher": "...", "hooks": [...]}]` | Before a tool executes |
| `PostToolUse` | Array of matcher blocks `[{"matcher": "...", "hooks": [...]}]` | After a tool completes |

### Execution & Wire Protocol

- **Handler types:** Only `"type": "command"` (optional; defaults to `"command"`). Runs synchronously.
- **Working directory:** Parent directory of the `hooks.json` file (so `./scripts/...` resolves relative to the plugin or `.agents/` folder).
- **Environment variables:** Plugin hooks receive `PLUGIN_ROOT` (install directory of the plugin) and `PLUGIN_DATA` (persistent plugin data directory).
- **Payload keys (camelCase protojson):** Stdin and stdout use camelCase fields (unlike Claude Code snake_case in some keys):
  - Input includes `sessionId`, `toolName`, `toolInput`, `toolResponse`, etc.
  - `PreToolUse` stdout decisions: `{"decision": "allow" | "deny" | "ask" | "force_ask", "reason": "..."}` plus optional `"overwrite"` (modified tool args), `"permissionOverrides"`, `"injectSteps"`.
  - `Stop` continuation: `{"decision": "continue", "reason": "..."}` (note `continuationActive` on follow-up invocations so hooks avoid infinite loops).
  - Non-empty stdout must be valid JSON on decision hooks; exit `0` + plain stderr for diagnostics, non-zero exit fails/blocks depending on hook strictness.

---

## Settings, Policies & Rules (`AGENTS.md`)

### CLI & Project Settings (`settings.json`)

- **User CLI settings:** `~/.gemini/antigravity-cli/settings.json` (sparse JSON — store only non-default overrides)
- **Workspace settings:** `<workspace>/.antigravity/settings.json`

### Antigravity App (2.0) Settings & Terminal Execution Policies

App 2.0 separates UI/terminal autonomy settings (managed in App Settings UI) from CLI `settings.json`. Key execution/review policy modes:

| Policy Mode | Behavior |
|-------------|----------|
| `always-proceed` | Execute terminal commands automatically unless allow/deny rules block |
| `request-review` | Prompt the user before running commands |
| `strict` | Deny unless explicitly allowlisted |
| `proceed-in-sandbox` | Run sandboxed commands automatically; prompt only on sandbox bypass |

> Never edit `~/.gemini/config/config.json` manually for App or IDE customization state. Use `agy` subcommands or the Antigravity Settings / Plugins Manager UI.

### Rules Files (`AGENTS.md` / `GEMINI.md` / `.agents/rules/`)

- Global instructions live in `~/.gemini/GEMINI.md`.
- Workspace instructions live in `<workspace>/AGENTS.md` (preferred cross-agent standard) and `<workspace>/.agents/rules/*.md`.
- **Size & Token Budgets:**
  - Single rule file cap: **24 KB** (larger files risk truncation).
  - Combined rules token budget: **20,000 tokens** (`defaultRulesBudget`).
  - Keep root `AGENTS.md` lean and route task-specific guidance into `.agents/skills/` or scoped `.agents/rules/*.md`.

---

## Plugins (`plugin.json` & `agy plugin`)

### Manifest (`plugin.json`)

Antigravity native plugins use JSONC (`plugin.json` at the plugin root) supporting line (`//`) and block (`/* ... */`) comments plus trailing commas:

```jsonc
{
  "$schema": "https://antigravity.dev/schemas/plugin.json",
  "name": "my-team-tools",          // required: kebab-case ID
  "displayName": "My Team Tools",
  "version": "1.2.0",
  "description": "Short summary shown in Plugins Manager",
  "logo": "assets/logo.png",        // relative path or URL
  "author": { "name": "Team" },
  "homepage": "https://example.com",
  "repository": "https://github.com/org/repo",
  "category": "Developer Tools",
  "suggestedPrompts": [             // max 3 prompts shown in UI
    "Audit this repository"
  ],
  "skills": "skills/",              // optional string or string[] of skill dirs
  "disabled": false
}
```

- **Unknown top-level fields are silently discarded** during loading — do not rely on custom manifest keys outside the official schema (`$schema`, `name`, `displayName`, `version`, `description`, `logo`, `suggestedPrompts`, `author`, `homepage`, `repository`, `category`, `disabled`, `skills`, `extensions`).
- **Component placement in native Antigravity plugins:**
  - Skills: `<plugin>/skills/<skill-name>/SKILL.md` (or path(s) in `skills` field)
  - Hooks: `<plugin>/hooks.json` (root — **not** `hooks/hooks.json`)
  - MCP: `<plugin>/mcp_config.json` (root — **not** `.mcp.json`)
  - Rules: `<plugin>/rules/*.md`

### CLI Workflows (`agy plugin`)

```bash
# List installed plugins (human or JSON)
agy plugin list --json

# Install from local directory, git URL, or registry
agy plugin install ./my-plugin

# Import a Claude Code or Gemini CLI plugin into Antigravity format
agy plugin import claude ./path/to/claude-plugin
agy plugin import gemini ./path/to/gemini-extension

# Toggle or remove
agy plugin enable my-plugin
agy plugin disable my-plugin
agy plugin uninstall my-plugin

# Validate structure before publishing
agy plugin validate ./my-plugin --strict --json
```

---

## UI Navigation & Discovery in Agent Replies

When working inside Antigravity, agents can surface live plugin surfaces cleanly in responses:

- **Open an installed plugin panel in side pane:** `[Plugin Name](customization://<dir>)` where `<dir>` is the plugin's actual install directory name under the config plugins folder (discoverable via `agy plugin list --json` / `GetAllPlugins`).
- **Suggest a Marketplace plugin:** Use `<plugin-card catalog-id="<id>"></plugin-card>` on its own line rather than inventing CLI install workarounds.
- **Avoid claiming manual `config.json` edits:** Always direct users to `agy plugin` CLI or the Plugins Manager UI.
