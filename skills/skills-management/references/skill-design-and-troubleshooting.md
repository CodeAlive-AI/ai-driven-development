# Skill Design, Patterns & Troubleshooting

Cross-agent guide to designing, structuring, distributing, and debugging Agent Skills (`SKILL.md`).

## Contents

- [Core Principles & Token Budget](#core-principles--token-budget)
- [Directory Structure](#directory-structure)
- [Six Design Patterns](#six-design-patterns)
- [Distribution Channels](#distribution-channels)
- [Pre-Publish Checklist](#pre-publish-checklist)
- [Troubleshooting](#troubleshooting)
- [Resources & Examples](#resources--examples)

## Core Principles & Token Budget

Design skills for **Agent Experience (AX)** — autonomous execution under finite attention and non-interactive shells — using **four-tier progressive disclosure** (see `references/agent-experience-and-progressive-disclosure.md` for full AX & CLI ergonomics guidance):

1. **Frontmatter (`name` + `description`)**: Always loaded at startup (~50–100 tokens per skill). Available ≠ loaded; determines whether an agent auto-triggers the skill.
2. **`SKILL.md` body**: Loaded on demand when triggered or invoked via `/<name>`. Target **300–2000 tokens** (`review_skill.py` warns above 2000 and penalises above 4000). Act as an operating contract and conditional router — front-load critical invariants and move bulky schemas or examples into `references/`.
3. **Bundled `references/` & `assets/`**: Loaded conditionally on demand; keep references flat (depth 1 from `SKILL.md`) with `## Contents` TOCs on files >100 lines.
4. **Out-of-context execution (`scripts/` & subagents)**: Offload deterministic parsing, hashing, validation, and staged filesystem mutations to scripts so code runs outside the prompt and only compact verdicts return.

## Directory Structure

```text
my-skill/
├── SKILL.md            # Required (exact case): YAML frontmatter + procedural instructions
├── README.md           # Optional for publishable repos/skills.sh (short human overview only; never duplicate SKILL.md)
├── scripts/            # Optional: executable helpers (uv PEP 723, bash, etc.)
├── references/         # Optional: detailed manuals, schemas, checklists (one level deep from SKILL.md)
├── assets/             # Optional: templates, sample inputs, icons
└── examples/           # Optional: reference inputs/outputs
```

- **Folder name**: lowercase kebab-case matching frontmatter `name`.
- **Forbidden inside skill folders**: `CHANGELOG.md`, `INSTALLATION_GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md` (place those at the repository root instead; agents treat extra docs as noise).
- **Navigation**: add a `## Contents` TOC to any Markdown file longer than 100 lines and keep reference links one level deep from `SKILL.md`.

## Six Design Patterns

1. **Sequential workflow orchestration**: Explicit ordered phases with data passed between steps, validation gates at each transition, and rollback notes on failure.
2. **Multi-MCP coordination**: Separate phases per MCP provider (for example, design export → storage → issue tracker → chat notice), verifying auth and tool schemas independently.
3. **Iterative refinement**: Draft → deterministic validation script (`scripts/check_*.py`) → targeted fix loop → stop when quality gate passes.
4. **Context-aware tool selection**: Decision tree routing to different tools or backends by file size, type, or environment, explaining the chosen path.
5. **Domain-specific intelligence**: Embed compliance checks, governance rules, and audit trails ahead of mutating calls.
6. **Validated iterative refinement (SkillOpt)**: For underperforming skills with 20–100 measurable tasks, run bounded atomic edits (`L_t`), a strictly-greater held-out selection gate, a rejected-edit buffer, and epoch-boundary slow updates inside `<!-- SLOW_UPDATE_START -->` / `<!-- SLOW_UPDATE_END -->` (see `references/skill-optimization.md`).

## Distribution Channels

- **Cross-agent GitHub + Skills CLI (`npx skills`)**: Host `skills/<name>/SKILL.md` in a GitHub repo so users install via `npx skills add <owner/repo> --skill <name>` across 60+ agents and browse metrics on [skills.sh](https://skills.sh).
- **Repository-scoped sharing**: Commit `.agents/skills/<name>/SKILL.md` (or `.claude/skills/<name>/SKILL.md`) directly in a team repo for automatic discovery by Antigravity, Codex, OpenCode, Cursor, and Claude Code.
- **Antigravity Plugins & Marketplace**: Bundle skills with MCP configs, rules, hooks, and subagents under `plugins/<name>/` with `plugin.json`; validate with `agy plugin validate --strict` and publish or install via `/plugin` or `agy plugin install`.
- **Claude Code Plugin Marketplace**: Expose `.claude-plugin/marketplace.json` + `.claude-plugin/plugin.json` at the repo root for `/plugin marketplace add` and `/plugin install`.

## Pre-Publish Checklist

- [ ] Folder name is lowercase kebab-case and matches frontmatter `name`
- [ ] `SKILL.md` exists (exact casing) with valid `---` YAML frontmatter
- [ ] `description` states **what** the skill does, **when** to use it (trigger phrases), and negative triggers (`Not for...`) within 1024 characters; third-person; no `< >` XML brackets
- [ ] Body stays compact (300–2000 tokens target), procedural, cross-platform (forward slashes), and free of time-sensitive dates
- [ ] References are one level deep with `## Contents` TOCs on files >100 lines; `SKILL.md` uses conditional routing with no broken links, no orphaned references, and no eager "read all" directives; `README.md` (if present) never duplicates `SKILL.md`
- [ ] Bundled `scripts/` run non-interactively (no `stdin` hangs), offer `--format json` / `--dry-run` where appropriate, and return actionable recovery commands on error
- [ ] Passed `uv run scripts/review_skill.py --path <skill-dir>` with 0 errors and 0 warnings
- [ ] Tested triggering (`trigger_test.py`) on positive paraphrases and unrelated negative prompts
- [ ] Verified clean installation topology with `uv run scripts/audit_skill_duplicates.py`

## Troubleshooting

- **Skill does not appear in Antigravity / other agent**: Check that frontmatter includes both `name` (matching directory) and non-empty `description`; verify discovery root (`~/.gemini/config/skills`, `~/.agents/skills`, or workspace `.agents/skills`); run `/skills reload` in `agy` or restart session if a brand-new `skills/` parent directory was just created.
- **Skill never auto-triggers**: Description is too vague or lacks user phrasing. Add concrete trigger phrases and file extensions, then test with `trigger_test.py`.
- **Skill over-triggers on unrelated requests**: Narrow scope in `description` and add negative triggers (`Do not use for...`).
- **Instructions are ignored or drift**: Move critical rules to the top under `## Important`, cut prose bloat below 2000 tokens, replace vague checks ("validate properly") with deterministic `scripts/`, and verify `SKILL.md` doesn't contradict `AGENTS.md`/`GEMINI.md`/`CLAUDE.md`.
- **Duplicate or stale behavior across agents**: Run `audit_skill_duplicates.py` to find divergent copies, stale backups (`*.bak`), or enabled plugin overlaps; consolidate onto one canonical source with `install_skill.py --link`.
- **MCP calls fail inside a skill**: Test the MCP server independently first (`/mcp` or `/plugin`), verify OAuth sign-in / env vars, and check exact tool names.

## Resources & Examples

- Open standard specification: [agentskills.io](https://agentskills.io)
- Skills CLI & ecosystem directory: [vercel-labs/skills](https://github.com/vercel-labs/skills) · [skills.sh](https://skills.sh)
- Antigravity Skills & Plugins docs: [antigravity.google/docs/skills](https://antigravity.google/docs/skills) · [antigravity.google/docs/plugins](https://antigravity.google/docs/plugins)
- Claude Code Skills docs: [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)
- OpenCode Skills docs: [opencode.ai/docs/skills](https://opencode.ai/docs/skills/)
- Reference skill collections: [anthropics/skills](https://github.com/anthropics/skills) · [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
