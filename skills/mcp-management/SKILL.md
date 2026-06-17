---
name: mcp-management
description: Search, install, configure, update, and remove MCP servers across coding agents (Claude Code, Cursor, VS Code, Claude Desktop, Gemini CLI, Codex, Goose, Zed, and more). Supports multi-agent installation via npx add-mcp, the official MCP registry, and direct config editing.
---

# MCP Server Management

**IMPORTANT**: After adding, removing, or updating MCP servers, inform the user to **restart the affected agent** for changes to take effect.

**CRITICAL**: Before removing any server, use `AskUserQuestion` to confirm with the user.

## Quick Reference (Claude Code)

```bash
# Install
claude mcp add --transport http <name> <url>
claude mcp add --transport stdio <name> -- <command> [args...]
claude mcp add-json <name> '<json>'              # Full JSON config in one shot

# List/inspect
claude mcp list
claude mcp get <name>

# Remove (confirm with user first!)
claude mcp remove <name>

# OAuth login/logout (for OAuth-protected HTTP servers)
claude mcp login <name>
claude mcp logout <name>
```

Options must come BEFORE the server name. As of 2026-04, `--transport http` (Streamable HTTP) is recommended; `sse` is end-of-life.

Plugin MCP servers connect automatically at session start. Use `/reload-plugins` to re-init after enabling/disabling a plugin mid-session.

## Multi-Agent Installation (npx add-mcp)

Install MCP servers to multiple coding agents at once using [add-mcp](https://github.com/neondatabase/add-mcp):

```bash
# Remote server (HTTP)
npx add-mcp https://mcp.example.com/mcp

# npm package (stdio)
npx add-mcp @modelcontextprotocol/server-postgres

# Local command
npx add-mcp "npx -y @org/mcp-server --flag value"

# SSE transport
npx add-mcp https://mcp.example.com/sse --transport sse
```

### Options

| Flag | Description |
|------|-------------|
| `-g, --global` | Install globally instead of project-level |
| `-a, --agent <agent>` | Target specific agent(s), repeatable |
| `-n, --name <name>` | Custom server name |
| `-t, --transport <type>` | HTTP (default) or SSE |
| `--header <header>` | Custom HTTP headers, repeatable |
| `-y, --yes` | Skip confirmation prompts |
| `--all` | Install to all detected agents |

### Supported Agents

| Agent | CLI Argument | Supports Project-Level |
|-------|-------------|----------------------|
| Claude Code | `claude-code` | Yes (`.mcp.json`) |
| Claude Desktop | `claude-desktop` | No (global only) |
| Cursor | `cursor` | Yes (`.cursor/mcp.json`) |
| VS Code | `vscode` | Yes (`.vscode/mcp.json`) |
| Gemini CLI | `gemini-cli` | Yes (`.gemini/settings.json`) |
| Codex | `codex` | Yes (`.codex/config.toml`, trusted projects only) |
| Goose | `goose` | No (global only) |
| GitHub Copilot CLI | `github-copilot-cli` | Yes (`.vscode/mcp.json`) |
| OpenCode | `opencode` | Yes (`opencode.json`) |
| Zed | `zed` | Yes (`.zed/settings.json`) |

### Codex App / Desktop caveats

Codex has two relevant surfaces:

- **Codex CLI** (`codex mcp list`, `codex mcp get`, `codex mcp login`) can see and validate
  MCP configuration from the CLI process.
- **Codex App / Desktop threads** receive MCP tools only when the app starts a thread with
  those servers loaded and authenticated. A server can appear in `codex mcp list` but still
  be absent from the current model turn's tool list if the thread was created before the
  server was added, authenticated, or reloaded.

When configuring MCP for Codex App:

1. Prefer project-level `.codex/config.toml` when the user explicitly asks for repo-level
   setup. The project must be trusted in `~/.codex/config.toml` under
   `[projects."/absolute/path"] trust_level = "trusted"`.
2. For HTTP servers that use OAuth, run:
   ```bash
   codex mcp login <server-name>
   ```
   Then verify `codex mcp list` shows `Auth: OAuth`.
3. For HTTP servers that use bearer tokens, prefer Codex's native bearer-token env form
   over hardcoding a header:
   ```bash
   codex mcp add <name> --url https://example.com/mcp --bearer-token-env-var EXAMPLE_API_KEY
   ```
   If writing `.codex/config.toml` directly, this is the expected shape:
   ```toml
   [mcp_servers.example]
   type = "http"
   url = "https://example.com/mcp"
   bearer_token_env_var = "EXAMPLE_API_KEY"
   ```
   Some third-party installers write `http_headers.Authorization = "Bearer ${EXAMPLE_API_KEY}"`;
   Codex CLI may display this as a bearer-token server, but the native field is clearer.
4. After adding, removing, editing, or logging in to a Codex App MCP server, tell the user to
   fully restart Codex App. Existing threads can receive newly available tools after the app
   restart; create a new thread only as a fallback if `tool_search` still cannot find the
   server tools in the existing thread.
5. Verification has two levels:
   ```bash
   codex mcp list
   codex mcp get <server-name>
   ```
   confirms Codex CLI/config/auth. Inside a Codex App thread, also use `tool_search` for a
   server-specific tool name (for example `supabase execute_sql` or `render list_services`).
   If `tool_search` returns no tools while `codex mcp list` is correct, the issue is usually
   App/thread reload or the server being configured only in a scope the App did not load.
6. If project-level `.codex/config.toml` is not being picked up by Codex App, as a temporary
   diagnostic duplicate the server in user-level `~/.codex/config.toml`, restart the App, and
   confirm tools appear. Remove the user-level duplicate afterward if the user wanted repo-only
   setup.

### Examples

```bash
# Install to Claude Code and Cursor only
npx add-mcp -a claude-code -a cursor https://mcp.stripe.com

# Install npm package to all agents, globally
npx add-mcp -g --all @modelcontextprotocol/server-postgres

# Install with custom name and headers
npx add-mcp -n my-api --header "Authorization: Bearer TOKEN" https://api.example.com/mcp

# List available agents
npx add-mcp list-agents
```

See [references/multi-agent.md](references/multi-agent.md) for agent-specific config paths, formats, and transformations.

## Searching for MCP Servers

When users ask to find or install an MCP server, see [references/search.md](references/search.md) for:
- Official vendor server lookup (always try first)
- MCP Registry API queries (fallback)
- Known official servers table
- User choice template format

**Trust hierarchy**: Official vendor > MCP reference servers > Verified partners > Community

## Adding Servers (Claude Code)

### With Environment Variables

The `--env` CLI flag is unreliable with special characters. Instead:

1. Add server without env vars:
   ```bash
   claude mcp add --transport stdio <name> -- npx -y @package/mcp-server
   ```

2. Edit config file to add env vars. See [references/scopes.md](references/scopes.md) for file locations.

### Collect Configuration First

Before installing, check if the server needs API keys or tokens. Use `AskUserQuestion` to collect required values before running install commands.

## Updating Servers

No direct update command exists. Options:

1. **Edit config directly** (preferred for credential changes)
2. **Remove and re-add** (confirm removal with user first)
3. **Use environment variables** for credentials that change often

For OAuth servers (GitHub, Sentry): Run `/mcp` in Claude Code to re-authenticate.

## Removing Servers

Always confirm with user via `AskUserQuestion` before removing.

```bash
claude mcp remove <server-name>
```

For project-scoped servers in `.mcp.json`, delete the entry from the file after user confirmation.

## OpenCode-specific notes

For OpenCode (anomalyco/opencode v1.14.x):
- Top-level key is `mcp` (not `mcpServers`); each server **must** declare `type: "local"` or `type: "remote"`
- For local servers, `command` is a single array `["bin", "arg1", "arg2"]` — there's no separate `args` field
- Env vars go under `environment` (not `env`)
- Per-server `enabled: false` disables without removing
- Use `opencode mcp auth <name>` / `opencode mcp logout <name>` for OAuth servers (e.g., GitHub)
- Plugin `tool.execute.*` hooks **do not** fire for MCP tool calls in v1.14.x — use `permission` rules instead

See [references/opencode-mcp.md](references/opencode-mcp.md) for the full OpenCode MCP reference.

## Reference

- **Search and known servers**: [references/search.md](references/search.md)
- **Multi-agent installation**: [references/multi-agent.md](references/multi-agent.md)
- **OpenCode MCP**: [references/opencode-mcp.md](references/opencode-mcp.md)
- **Transport types**: [references/transports.md](references/transports.md)
- **Scopes and config files**: [references/scopes.md](references/scopes.md)
- **Troubleshooting**: [references/troubleshooting.md](references/troubleshooting.md)

## Scopes Summary (Claude Code)

| Scope | Flag | Config Location | Use Case |
|-------|------|-----------------|----------|
| Local | `--scope local` (default) | `~/.claude.json` | Personal dev servers |
| Project | `--scope project` | `.mcp.json` | Team-shared servers |
| User | `--scope user` | `~/.claude.json` | Cross-project tools |

## Environment Variable Syntax

In config files: `${VAR}` or `${VAR:-default}`

## Windows Note

Use `cmd /c` wrapper for npx:
```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```
