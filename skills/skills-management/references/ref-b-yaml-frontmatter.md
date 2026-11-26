# Reference B: YAML Frontmatter & Cross-Agent Matrix

YAML frontmatter schema for `SKILL.md` across the [Agent Skills standard](https://agentskills.io), Antigravity (App / IDE / CLI), Claude Code, Codex, and OpenCode.

## Contents

- [Cross-Agent Compatibility Matrix](#cross-agent-compatibility-matrix)
- [Minimal Portable Frontmatter](#minimal-portable-frontmatter)
- [Claude Code Extensions](#claude-code-extensions)
- [Framework Agent Extensions (Mastra & LangGraph / Deep Agents)](#framework-agent-extensions-mastra--langgraph--deep-agents)
- [String Substitutions & Dynamic Context](#string-substitutions--dynamic-context)
- [Skill Content Lifecycle & Permissions](#skill-content-lifecycle--permissions)
- [Security Restrictions](#security-restrictions)
- [Discovery Priority Overview](#discovery-priority-overview)

## Cross-Agent Compatibility Matrix

| Field / Rule | `agentskills.io` | Antigravity (App / IDE / CLI) | Claude Code | Codex | OpenCode |
|---|---|---|---|---|---|
| `name` | Required (`1–64` chars, `^[a-z0-9]+(-[a-z0-9]+)*$`, matches folder) | Required (falls back to folder in newer `agy`, dropped if missing in older/App) | Optional (defaults to folder name) | Required (matches skill id/folder) | Required (`1–64` chars, matches folder) |
| `description` | Required (`1–1024` chars, non-empty) | Required (non-empty; colons ok, `>-` / quotes safer) | Required (falls back to first paragraph; `description + when_to_use` truncated at `1,536` chars) | Required (used for routing) | Required (`1–1024` chars) |
| `license` | Optional | Ignored safely | Optional | Optional | Optional |
| `compatibility` | Optional (`1–500` chars) | Ignored safely | Optional | Optional | Optional |
| `metadata` | Optional (key-value string map) | Ignored safely | Optional | Optional | Optional (`string -> string`) |
| `allowed-tools` | Optional (experimental) | Ignored safely | Space-separated or YAML list | Ignored safely | Ignored safely |
| `disable-model-invocation` | Supported (`true` = explicit only) | Supported (`true` excludes from startup catalog; callable via `/name`) | Supported (`true` excludes from catalog, blocks subagent preload; `/name` works) | Ignored in `SKILL.md`; use `agents/openai.yaml` (`policy.allow_implicit_invocation: false`, `$name` works) | Ignored in `SKILL.md`; use `permission.skill.<name>: "ask"\|"deny"` in `opencode.json` |
| CC-only extensions (`when_to_use`, `argument-hint`, `arguments`, `user-invocable`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `shell`) | Ignored | `user-invocable` / `argument-hint` partially adopted in some runtimes; do not rely on CC-specific fields for cross-agent skills | Full support | Ignored | Ignored |

For maximum portability across Antigravity, Claude Code, Codex, Cursor, and OpenCode, keep required fields strictly to `name` (matching directory) and `description` (what + when + negative triggers).

## Minimal Portable Frontmatter

```yaml
---
name: skill-name-in-kebab-case
description: >-
  What the skill does and when to use it. Include specific trigger phrases.
  Do not use for unrelated tasks.
---
```

Constraints:
- `name`: lowercase letters, numbers, and hyphens only (`max 64` chars), no leading/trailing hyphen, no XML angle brackets, no `claude` or `anthropic` prefix.
- `description`: non-empty, `<= 1024` characters, third person, no XML angle brackets (`< >`). Front-load the core use case.

## Claude Code Extensions

| Field | Description |
|---|---|
| `when_to_use` | Additional invocation context (trigger phrases, examples). Appended to `description` (combined listing entry truncated at `1,536` chars). |
| `argument-hint` | Autocomplete hint, e.g. `[issue-number]` or `[filename] [format]`. |
| `arguments` | Named positional argument list (space-separated string or YAML list) for `$name` substitution. |
| `disable-model-invocation` | `true` = only the user can invoke (`/name`); Claude will not auto-load it and blocks subagent preload. Default: `false`. |
| `user-invocable` | `false` = hide from `/` menu (background knowledge skills). Default: `true`. |
| `allowed-tools` | Tools Claude can use without a permission prompt while the skill is active. Does NOT restrict tools — use permission settings to deny. |
| `model` | Model alias (`sonnet`, `opus`, `haiku`, `inherit`) or full model ID. Applies to current turn only. |
| `effort` | Reasoning effort: `low`, `medium`, `high`, `xhigh`, `max`. Inherits session level if absent. |
| `context` | `fork` to run in a forked subagent with isolated context. |
| `agent` | Subagent type when `context: fork` (`Explore`, `Plan`, `general-purpose`, or custom `.claude/agents/*`). |
| `hooks` | Hooks scoped to this skill's lifecycle. |
| `paths` | Glob patterns limiting auto-activation (comma-separated string or YAML list). |
| `shell` | `bash` (default) or `powershell` for `` !`command` `` and ` ```! ` blocks. |

## Framework Agent Extensions (Mastra & LangGraph / Deep Agents)

- **LangGraph / Deep Agents (`SkillsMiddleware`)**: supports `metadata.include_tools` (space-separated string or YAML list of tool names) to unlock bound tools only after `SKILL.md` is read. Sources are evaluated sequentially with **last-source-wins** precedence; `pinned_skills` or `/<name>` pre-loads `SKILL.md` as a `HumanMessage`.
- **Mastra (`@mastra/core`)**: filesystem `SKILL.md` in `Workspace` uses standard `name` + keyword-rich `description` (important for `SkillSearchProcessor` BM25/vector retrieval and `skill_read` on supporting files), or inline code-defined `createSkill({ name, description, instructions, references })`.
- See `references/framework-agent-skills.md` for storage backends (`FilesystemBackend`, `StateBackend`, `StoreBackend`), `SkillSearchProcessor`, and portability rules.

## String Substitutions & Dynamic Context

Claude Code string substitutions inside `SKILL.md`:

| Variable | Description |
|---|---|
| `$ARGUMENTS` | All arguments passed when invoking the skill (appended as `ARGUMENTS: <value>` if absent) |
| `$ARGUMENTS[N]` / `$N` | 0-based positional argument (`$0`, `$1`, ...) |
| `$name` | Named argument declared in `arguments` frontmatter |
| `${CLAUDE_SESSION_ID}` | Current Claude Code session ID |
| `${CLAUDE_SKILL_DIR}` | Directory containing the skill's `SKILL.md` |

Dynamic context injection (Claude Code): `` !`command` `` (or fenced ` ```! `) runs before skill content reaches the model; Claude sees only the output. Disable via `"disableSkillShellExecution": true` in settings.

## Skill Content Lifecycle & Permissions

- **Claude Code compaction**: Invoked `SKILL.md` enters the conversation as one message; auto-compaction re-attaches the most-recent invocation keeping up to **5,000 tokens** per skill within a **25,000-token** combined budget (most-recent first).
- **Claude Code permissions**: `Skill(name)` (exact), `Skill(name *)` (prefix with args), `Skill` in `deny` (block all).
- **OpenCode permissions**: `permission.skill` glob rules (`*`, `internal-*`, `destructive-*`) in `opencode.json`.
- **Antigravity**: Progressive disclosure at startup (`name` + `description`); `/skills reload` refreshes mid-session in `agy`.

## Security Restrictions

Forbidden in frontmatter:
- XML angle brackets (`< >`) in `name` or `description` (prompt-injection risk in system prompts)
- Code execution tags in YAML (loaders use safe YAML parsing)
- `claude` or `anthropic` prefixes in skill names (reserved)

## Discovery Priority Overview

- **Antigravity (App / IDE / CLI)**: Workspace `.agents/skills/` (walk-up to repo root, plus legacy `.agent/`, `_agents/`, `_agent/`) → workspace `skills.json`/`plugins.json` (confined to repo root) → `~/.gemini/config/skills/` → `~/.agents/skills/` (`agy` 1.5.16+) → enabled plugins (`~/.gemini/config/plugins/`). See `references/antigravity-skills.md`.
- **Claude Code**: Enterprise managed-settings → Personal `~/.claude/skills/` → Project `.claude/skills/` (plus `--add-dir` `.claude/skills/` and monorepo subdirs) → Enabled plugins (`plugin:skill`). Live change detection applies to existing `skills/` roots; creating a brand-new top-level `skills/` dir requires a restart.
- **Codex / OpenCode**: See `scripts/agents.py` (`detect_agents.py --all`) and `references/opencode-skills.md`.
