# MCP Multi-Agent Configuration, Scopes, Transports & Troubleshooting

> Unified MCP configuration guide across Claude Code, Antigravity (App 2.0 / IDE / `agy`), Codex CLI/App, OpenCode, Devin, Cursor, VS Code, Gemini CLI, Goose, Copilot CLI, and Zed.

## Contents

- [Multi-Agent Installation (`npx add-mcp`)](#multi-agent-installation-npx-add-mcp)
- [Agent Configuration Reference](#agent-configuration-reference)
- [Codex App / Desktop Caveats](#codex-app--desktop-caveats)
- [Claude Code Scopes & Enterprise Policy](#claude-code-scopes--enterprise-policy)
- [Transports (Streamable HTTP & Stdio)](#transports-streamable-http--stdio)
- [Troubleshooting & Security](#troubleshooting--security)

---

## Multi-Agent Installation (`npx add-mcp`)

[add-mcp](https://github.com/neondatabase/add-mcp) installs MCP servers into multiple coding agents with one command, handling agent detection, config format differences, and field transformations:

```bash
npx add-mcp <source> [options]
```

- **Auto-detected sources:** URLs (`https://...`) -> Streamable HTTP; scoped/simple npm packages -> `stdio` via `npx -y`; quoted commands with spaces -> custom `stdio`.
- **Name inference:** `https://mcp.neon.tech/mcp` -> `neon`, `@modelcontextprotocol/server-postgres` -> `postgres`, `mcp-server-github` -> `github`. Override with `-n <name>`.
- **Common options:** `--agent <name>`, `--global`, `--header "Key: Value"`, `--list-agents`, `--transport http`.

```bash
# Streamable HTTP (default for URLs)
npx add-mcp https://mcp.stripe.com
npx add-mcp --header "Authorization: Bearer TOKEN" https://api.example.com/mcp

# Stdio npm or local commands
npx add-mcp @modelcontextprotocol/server-postgres
npx add-mcp "python -m mcp_server --host localhost" -n my-py-mcp
```

---

## Agent Configuration Reference

| Agent | Global Config | Project Config | Top Key / Format | Notes |
|-------|---------------|----------------|------------------|-------|
| **Claude Code** | `~/.claude.json` | `.mcp.json` | `mcpServers` / JSON | Local, project, user scopes; OAuth 2.1 + CIMD |
| **Claude Desktop** | macOS `~/Library/Application Support/Claude/claude_desktop_config.json`, Win `%APPDATA%/Claude/...`, Linux `~/.config/Claude/...` | None | `mcpServers` / JSON | Global only |
| **Antigravity** | `~/.gemini/config/mcp_config.json` | `.agents/mcp_config.json` | `mcpServers` / JSON | Uses `serverUrl`/`url`; see `references/antigravity-config.md` & `agy mcp` |
| **Codex CLI / App** | `~/.codex/config.toml` | `.codex/config.toml` (trusted) | `mcp_servers` / TOML | Streamable HTTP & stdio; `bearer_token_env_var`, `oauth_scopes` |
| **OpenCode** | `~/.config/opencode/opencode.json` | `opencode.json` or `.opencode/opencode.json` | `mcp` / JSON(C) | `type: "local"|"remote"`, `command: [...]`, `environment`, `oauth` |
| **Devin CLI / Desktop** | `~/.config/devin/mcp_config.json` (Win `%APPDATA%/devin/mcp_config.json`) | `.devin/mcp_config.json`, `.devin/mcp_config.local.json` | `mcpServers` / JSON | Imports `.claude/`, `.cursor/rules`, etc. when `read_config_from` is enabled |
| **Cursor** | `~/.cursor/mcp.json` | `.cursor/mcp.json` | `mcpServers` / JSON | Remote entries use `url` + optional `headers` (no `type`) |
| **VS Code** | macOS `~/Library/Application Support/Code/User/mcp.json`, Win `%APPDATA%/Code/User/mcp.json`, Linux `~/.config/Code/User/mcp.json` | `.vscode/mcp.json` | `servers` / JSON | Shared project file with Copilot CLI |
| **GitHub Copilot CLI** | `~/.copilot/mcp-config.json` | `.vscode/mcp.json` | `mcpServers` (global) / `servers` (proj) / JSON | Global config adds `tools: ["*"]` |
| **Gemini CLI** | `~/.gemini/settings.json` | `.gemini/settings.json` | `mcpServers` / JSON | Nested under `settings.json` |
| **Goose** | `~/.config/goose/config.yaml` (Win `%APPDATA%/Block/goose/config/config.yaml`) | None | `extensions` / YAML | Uses `uri`, `type: streamable_http`, `cmd`, `envs`, `enabled`, `timeout` |
| **Zed** | `~/Library/Application Support/Zed/settings.json` (Linux `~/.config/zed/settings.json`) | `.zed/settings.json` | `context_servers` / JSON | Adds `source: "custom"` |

### Codex Advanced TOML Options

```toml
[mcp_servers.my-server]
enabled = true
required = true                             # Fail startup if server cannot init
command = "npx"                             # Stdio executable
args = ["-y", "@org/mcp-server"]
cwd = "/path/to/server"
url = "https://example.com/mcp"             # Streamable HTTP endpoint
bearer_token_env_var = "MY_TOKEN"
startup_timeout_sec = 10.0
tool_timeout_sec = 60.0
enabled_tools = ["search", "summarize"]
disabled_tools = ["slow-tool"]
supports_parallel_tool_calls = false
default_tools_approval_mode = "on-request"
oauth_scopes = ["read", "write"]

[mcp_servers.my-server.approval_mode]
search = "never"
delete = "untrusted"

[mcp_servers.my-server.env]
API_KEY = "value"

[mcp_servers.my-server.http_headers]
X-Custom = "value"

[mcp_servers.my-server.env_http_headers]
Authorization = "AUTH_TOKEN_ENV"
```

Useful Codex CLI commands: `codex mcp add`, `codex mcp list [--json]`, `codex mcp get <name>`, `codex mcp remove <name>`, `codex mcp login <server>`, `codex mcp logout <server>`, plus `/mcp verbose` in the TUI.

### Goose YAML Example

```yaml
extensions:
  neon:
    name: neon
    type: streamable_http
    uri: https://mcp.neon.tech/mcp
    headers: {}
    enabled: true
    timeout: 300
  postgres:
    name: postgres
    cmd: npx
    args: ["-y", "@modelcontextprotocol/server-postgres"]
    type: stdio
    envs: {}
    enabled: true
    timeout: 300
```

---

## Codex App / Desktop Caveats

Codex has two distinct runtime surfaces:

- **Codex CLI** (`codex mcp list`, `codex mcp get`, `codex mcp login`) inspects and validates config directly.
- **Codex App / Desktop threads** receive MCP tools only when the app starts/reloads a thread with those servers loaded and authenticated. A server visible in `codex mcp list` can still be missing from an existing thread until reload.

Checklist for Codex App setup:

1. **Trust project repos** when using `.codex/config.toml`: ensure `~/.codex/config.toml` has `[projects."/absolute/path"] trust_level = "trusted"`.
2. **OAuth HTTP servers:** run `codex mcp login <server-name>` and confirm `codex mcp list` reports `Auth: OAuth`.
3. **Bearer-token HTTP servers:** prefer `--bearer-token-env-var EXAMPLE_API_KEY` (`bearer_token_env_var = "EXAMPLE_API_KEY"` inside `[mcp_servers.<name>]`) over raw `Authorization` header strings.
4. **Restart Codex App** after adding, editing, removing, or logging into an MCP server; create a fresh thread only as fallback if `tool_search` still finds no tools from that server.
5. **Diagnostic fallback:** if project `.codex/config.toml` is ignored by the App, temporarily test the same block in `~/.codex/config.toml`, restart, then clean up the duplicate if repo-only setup was requested.

---

## Claude Code Scopes & Enterprise Policy

| Scope | Command Flag | Location | Section | Precedence |
|-------|--------------|----------|---------|------------|
| **Local** (default) | `--scope local` | `~/.claude.json` | `projects.<project-path>.mcpServers` | 1 (highest) |
| **Project** (shared) | `--scope project` | `.mcp.json` | `mcpServers` | 2 |
| **User** (global) | `--scope user` | `~/.claude.json` | `mcpServers` | 3 (lowest) |

Environment variable expansion syntax in `.mcp.json` / `~/.claude.json`: `${VAR}` or `${VAR:-default}`.

### Enterprise / Managed MCP

Paths: macOS `/Library/Application Support/ClaudeCode/managed-mcp.json`, Linux/WSL `/etc/claude-code/managed-mcp.json`, Windows `C:\Program Files\ClaudeCode\managed-mcp.json`.

- **Exclusive control:** populate `"mcpServers"` in `managed-mcp.json` so users cannot add or alter servers.
- **Allowlist / denylist:** configure `"allowedMcpServers"` and `"deniedMcpServers"` entries matching `{"serverName": "..."}` or `{"serverUrl": "https://.../*"}`.

---

## Transports (Streamable HTTP & Stdio)

### Streamable HTTP (Standard Remote Transport)

Streamable HTTP (`"type": "http"` in Claude/Devin, `"type": "remote"` in OpenCode, `"serverUrl"` in Antigravity, `url = "..."` in Codex) is the standard remote MCP transport across modern clients.

```bash
# Claude Code
claude mcp add --transport http <name> <url> --header "Authorization: Bearer TOKEN"

# Antigravity (flags MUST precede <name>)
agy mcp add -t http -H "Authorization: Bearer TOKEN" <name> <url>
```

- **Claude Code OAuth & large outputs:** supports OAuth 2.1, RFC 9728 PRM discovery, CIMD (SEP-991), `oauth.authServerMetadataUrl` override, and `_meta["anthropic/maxResultSizeChars"]` up to `500000`. Header helper scripts receive `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL`.
- **Legacy SSE endpoints (`/sse`):** deprecated by the MCP spec; Antigravity does not connect to raw SSE directly and several newer clients require Streamable HTTP. Migrate configs to Streamable HTTP URLs, or bridge legacy SSE-only servers locally with `npx -y mcp-remote <sse-url>` (see `references/legacy/migrations.md`).

### Stdio Transport

Runs local servers (npm packages, Python modules, binaries) over stdin/stdout:

```bash
claude mcp add --transport stdio <name> -- npx -y @package/name --flag
agy mcp add -e API_KEY=val <name> npx -y @package/name --flag
```

### Popular Reference Servers

| Server | Transport / Endpoint or Command |
|--------|--------------------------------|
| **Filesystem** | `npx -y @modelcontextprotocol/server-filesystem /path` |
| **PostgreSQL (`dbhub`)** | `npx -y @bytebase/dbhub --dsn "postgresql://..."` |
| **SQLite** | `npx -y @modelcontextprotocol/server-sqlite path/to/db.sqlite` |
| **GitHub** | `https://api.githubcopilot.com/mcp/` |
| **Sentry** | `https://mcp.sentry.dev/mcp` |
| **Notion** | `https://mcp.notion.com/mcp` |

---

## Troubleshooting & Security

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `"Options must come before server name"` | Flags placed after positional `<name>` | Put `-s`/`--scope`/`-t`/`--transport`/`-e`/`-H` before `<name>` (applies to `claude mcp` and `agy mcp`) |
| Stdio fails immediately | Missing binary or Windows cmd quoting | Test `which npx` and `npx -y <pkg> --help`; on Windows wrap with `cmd /c npx ...` |
| `--env` mangles special characters | Shell/CLI argument parsing edge case | Add server without `--env`, then edit the config file directly |
| Env vars not expanding in Antigravity plugin | Plugin `mcp_config.json` isolates host env | Declare user secrets in server `"variables"` or use plugin auth |
| Output truncated at 25K tokens | Default `MAX_MCP_OUTPUT_TOKENS` ceiling | Export `MAX_MCP_OUTPUT_TOKENS=50000` (Claude) or use server `_meta["anthropic/maxResultSizeChars"]` |
| Startup timeout | Slow cold `npx` download or auth check | Raise `MCP_TIMEOUT=30000` (ms, Claude) or `startup_timeout_sec` (Codex) |
| OAuth loop or expired token | Stale cached token | Run `/mcp` (`claude`), `codex mcp login <name>`, or `opencode mcp auth <name>` |

### Security Practices

- Keep personal secrets in local/user configs or env-var references (`${VAR}`), never committed plaintext in `.mcp.json` or `.agents/mcp_config.json`.
- Audit third-party stdio packages and remote URLs before trusting them (prompt injection / arbitrary command execution risk).
- Review repo-scoped `.mcp.json`, `.codex/config.toml`, and `.agents/mcp_config.json` changes in pull requests before approving.
