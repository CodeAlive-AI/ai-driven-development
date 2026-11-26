# Legacy Paths, Formats & Migrations

Historical formats, deprecated discovery locations, and step-by-step migration paths for Antigravity, Claude Code, Codex, and ecosystem tooling.

## Contents

- [Antigravity Pre-2.0 Skill Directories](#antigravity-pre-20-skill-directories)
- [Antigravity Deprecated Workflows to Skills](#antigravity-deprecated-workflows-to-skills)
- [Migrating Other Agents into Antigravity](#migrating-other-agents-into-antigravity)
- [Claude Code Legacy `.claude/commands/`](#claude-code-legacy-claudecommands)
- [Historical Claude.ai Manual `.zip` Upload](#historical-claudeai-manual-zip-upload)
- [Renamed CLIs & Legacy Agent Roots](#renamed-clis--legacy-agent-roots)

## Antigravity Pre-2.0 Skill Directories

- **`~/.gemini/antigravity/skills/`**: Pre-2.0 Antigravity IDE/App global skills path. On current installations it is typically a symlink to `~/.gemini/config/skills/`. Never write new global skills here; if a real directory still exists alongside `~/.gemini/config/skills/`, consolidate into `~/.gemini/config/skills/` and replace or remove the old copy (keeping the symlink if older tools expect it).
- **`~/.gemini/antigravity-cli/skills/` & `~/.gemini/skills/`**: Legacy CLI global directories. Current `agy` reads `~/.gemini/config/skills/` (primary) and `~/.agents/skills/` (cross-tool fallback, `agy 1.5.16+`). `audit_skill_duplicates.py` and `delete_skill.py --all-agents` scan these legacy paths via `extra_global_dirs`.
- **Workspace legacy roots**: `.agent/skills/`, `_agents/skills/`, and `_agent/skills/` remain discovered for backward compatibility, but **`.agents/skills/`** is the standard workspace directory for new skills.

## Antigravity Deprecated Workflows to Skills

Single-file Markdown workflows (`workflows/*.md` and `workflows.json`) are deprecated in favor of skills (`skills/<name>/SKILL.md`), which add `/<name>` slash commands, semantic auto-invocation, and `scripts/` / `references/`.

Deprecated paths scanned during migration:

| Scope | Legacy Workflow Path | Target Skill Path |
|---|---|---|
| Global | `~/.gemini/config/global_workflows/*.md` | `~/.gemini/config/skills/<name>/SKILL.md` |
| Global | `~/.gemini/config/workflows/*.md` | `~/.gemini/config/skills/<name>/SKILL.md` |
| Workspace | `<workspace>/{.agents,_agents,.agent,_agent}/workflows/*.md` | `<workspace>/{.agents,_agents,.agent,_agent}/skills/<name>/SKILL.md` |
| Manifests | `~/.gemini/config/workflows.json`, `<workspace>/{.agents,...}/workflows.json` | Entries removed after migration |

**Migration procedure** (automated by Antigravity's built-in `/migrate-workflows` skill):

1. Check if `<target_dir>/<name>/SKILL.md` already exists — never overwrite an existing skill (during transition, skills take precedence over same-named workflows).
2. Wrap the workflow body with YAML frontmatter (`name` matching folder + concise one-sentence `description`).
3. Write `<target_dir>/<name>/SKILL.md`.
4. Rename the legacy `.md` file to `<name>.md.bak` (safe archive) and prune migrated entries from `workflows.json`. Move `.md.bak` files out of discovery roots if they trigger stale-backup warnings.

## Migrating Other Agents into Antigravity

- **Plugins & extensions via CLI**:
  - `agy plugin import claude` — imports enabled user-level Claude Code marketplace plugins (`~/.claude/plugins/`), converting `commands/*.md` to skills, converting `PreToolUse`/`PostToolUse`/`Stop`/`SessionStart` hooks (mapping `Bash` → `run_command`), and expanding `${CLAUDE_PLUGIN_ROOT}`. Single-project Claude plugins and disabled plugins are skipped.
  - `agy plugin import gemini` — imports Gemini CLI extensions from `~/.gemini/extensions/`.
- **Loose user settings via built-in `/migrate-agent-settings`**:
  - Consolidates Claude Code (`~/.claude.json`, `.mcp.json`, `~/.claude/skills/`, `~/.claude/commands/`, `~/.claude/agents/`, `CLAUDE.md`), Codex (`~/.codex/config.toml`, `~/.codex/skills/`, `~/.codex/prompts/`, `AGENTS.md`), Cursor (`~/.cursor/mcp.json`, `.cursor/rules/*.mdc`), and Gemini CLI (`~/.gemini/settings.json`, `~/.gemini/commands/**/*.toml`, `GEMINI.md`) into a single reversible Antigravity plugin under `~/.gemini/config/plugins/<name>/`.
  - Ensures every migrated `SKILL.md` has `name` (folder name) and non-empty `description` (required by Antigravity), converts `$ARGUMENTS` / `$1` / `{{args}}` placeholders in imported commands, and flags legacy SSE MCP servers (`type: sse`) for `mcp-remote` bridging.

## Claude Code Legacy `.claude/commands/`

`.claude/commands/<name>.md` files are superseded by `.claude/skills/<name>/SKILL.md` (both create `/<name>`, while skills add supporting files, frontmatter, and auto-invocation). When migrating:

1. Move `.claude/commands/foo.md` → `.claude/skills/foo/SKILL.md` (and `~/.claude/commands/foo.md` → `~/.claude/skills/foo/SKILL.md`).
2. Add `name: foo` and `description` frontmatter if absent; keep `$ARGUMENTS` substitutions intact.
3. Re-run `audit_skill_duplicates.py` to confirm no duplicate copy remains.

## Historical Claude.ai Manual `.zip` Upload

Early 2025/early-2026 Claude.ai web workflows distributed skills by compressing `<skill-name>/` into a `.zip` archive and uploading it via `Claude.ai > Settings > Capabilities > Skills`. For coding agents (Claude Code, Antigravity, Codex, Cursor, OpenCode), prefer GitHub + `npx skills add` or native plugins (`agy plugin install`, `/plugin`).

## Renamed CLIs & Legacy Agent Roots

| Legacy Name / Path | Current Canonical Equivalent | Notes |
|---|---|---|
| `vercel-labs/add-skill`, `npx add-skill` | `vercel-labs/skills`, `npx skills` | Package and CLI renamed |
| OpenClaw `~/.clawdbot/skills`, `~/.moltbot/skills` | `~/.openclaw/skills` | Pre-rename OpenClaw homes |
| Kilo `~/.kilocode/skills` | `~/.agents/skills` (or `~/.kilo/skills`) | Legacy Kilo config dir |
| Goose `~/.config/goose/skills` (v1.16–1.24) | `~/.agents/skills` | Goose 1.25+ uses `.agents/skills` |
| Kimi CLI `~/.config/agents/skills` | `~/.agents/skills` | `kimi-cli` renamed to `kimi-code-cli` |
| Windsurf `.windsurf/skills` | Devin Desktop / `.agents/skills` | Windsurf docs redirect to Devin Desktop |
