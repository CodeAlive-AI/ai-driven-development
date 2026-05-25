---
name: skills-management
description: Search, find, discover, install, remove, update, review, list, move, optimise, and iterate on skills for AI coding agents. Use when user asks "find a skill for X", "search for a skill", "is there a skill for X", "install skill", "remove skill", "update skills", "list skills", "review skill quality", "move skill", "check for updates", "optimise skill", "train skill on tasks", "iterate skill", "audit skill edits", "log skill edit", "diff skill versions", "trigger test skill", "transfer skill across agents", or "how do I do X" where X might have an existing skill. THE tool for skill discovery, ecosystem search, and SkillOpt-style training loops. Do not use for creating skills from scratch (use /skill-creator instead).
---

# Skills Manager

## Quick Reference

| Task | Command |
|------|---------|
| List all | `python3 scripts/list_skills.py` |
| List by scope | `python3 scripts/list_skills.py -s user` or `-s project` |
| Show details | `python3 scripts/show_skill.py <name>` |
| Review skill | `python3 scripts/review_skill.py <name>` |
| Delete | `python3 scripts/delete_skill.py <name>` |
| Delete from agents | `python3 scripts/delete_skill.py <name> --all-agents --force` |
| Move to user | `python3 scripts/move_skill.py <name> user` |
| Move to project | `python3 scripts/move_skill.py <name> project` |
| Create new | Use `/skill-creator` |
| **Optimize & Iterate (SkillOpt-style)** | |
| Plan optimisation | `python3 scripts/optimize_skill.py <name> --tasks tasks.jsonl --dry-run` |
| Run optimisation | `python3 scripts/optimize_skill.py <name> --tasks tasks.jsonl --output-dir runs/r1` |
| Log a manual edit | `python3 scripts/log_skill_edit.py <name> --reason "..." --snapshot` |
| List recent edits | `python3 scripts/log_skill_edit.py <name> --list --since 7d` |
| Diff vs last snapshot | `python3 scripts/diff_skill_versions.py <name> --log --format stats` |
| Diff between commits | `python3 scripts/diff_skill_versions.py <name> --git HEAD~3 HEAD` |
| Trigger test | `python3 scripts/trigger_test.py <name> --cases cases.yaml` |
| Generate trigger cases | `python3 scripts/trigger_test.py <name> --generate > cases.yaml` |
| Transfer test | `python3 scripts/transfer_test.py <name> --all` |
| Aggregate runs | `python3 scripts/aggregate_runs.py runs/*` |
| Compare runs | `python3 scripts/aggregate_runs.py runs/r1 runs/r2 --compare` |
| **Discovery & Install** | |
| Find skills | `npx skills find [query]` |
| Review remote skills | Fetch skills.sh pages, assess using [assessment framework](references/remote-skill-assessment.md) |
| List ecosystem skills | `npx skills list` or `npx skills ls` |
| Install from GitHub | `npx skills add <owner/repo@skill> -g -y` |
| Remove ecosystem skill | `npx skills remove <name> -g -y` or `npx skills rm` |
| Check for updates | `npx skills check` |
| Update all | `npx skills update` |
| Browse online | [skills.sh](https://skills.sh) |
| **Multi-Agent** | |
| Detect agents | `python3 scripts/detect_agents.py` |
| List agent skills | `python3 scripts/list_agent_skills.py --agent cursor` |
| Install to agent | `python3 scripts/install_skill.py /path --agent cursor` |
| Copy between agents | `python3 scripts/copy_skill.py <name> --from claude-code --to cursor` |
| Move between agents | `python3 scripts/move_skill_agent.py <name> --from claude-code --to cursor` |

## Scopes

| Scope | Path | Visibility |
|-------|------|------------|
| User | `~/.claude/skills/` | All projects for this user |
| Project | `.claude/skills/` | This repository only |

User scope takes precedence over project scope for skills with the same name.

## Operations

### List Skills

```bash
python3 scripts/list_skills.py              # All skills
python3 scripts/list_skills.py -s user      # User scope only
python3 scripts/list_skills.py -f json      # JSON output
```

### Show Skill Details

```bash
python3 scripts/show_skill.py <name>           # Basic info
python3 scripts/show_skill.py <name> --files   # Include file listing
python3 scripts/show_skill.py <name> -f json   # JSON output
```

### Review Skill

Audits a skill against best practices and suggests improvements:

```bash
python3 scripts/review_skill.py <name>         # Review with text output
python3 scripts/review_skill.py <name> -f json # JSON output for programmatic use
```

**Checks performed:**
- Name format (lowercase, hyphens, max 64 chars, gerund form)
- Name matches directory name
- Description quality (triggers, negative triggers, third person, specificity)
- XML angle brackets in frontmatter (security)
- Forbidden docs files (README.md, CHANGELOG.md)
- Body length (warns if >500 lines)
- **Token footprint** (300-2000 tokens target per SkillOpt; warns at 2000, penalises at 4000)
- **Procedurality** (instance-specific markers — filenames, literal numbers, task references — should be rare)
- **Patch-friendliness** (anchor density: `##`/`###` headings + `**Label:**` markers needed for reliable `insert_after` edits)
- **Slow-update section integrity** (`<!-- SLOW_UPDATE_START -->` / `<!-- SLOW_UPDATE_END -->` markers must be balanced and unnested)
- Time-sensitive content
- Path format (no Windows backslashes)
- Reference depth (should be one level)
- Table of contents for long files

**After reviewing:** Read the skill's SKILL.md and apply the suggested fixes directly.

### Delete Skill

**CRITICAL**: Always use `AskUserQuestion` to confirm before deleting: "Are you sure you want to delete the skill '[name]'? This cannot be undone."

```bash
python3 scripts/delete_skill.py <name>              # Claude Code only, with confirmation
python3 scripts/delete_skill.py <name> --force      # Skip confirmation prompt
python3 scripts/delete_skill.py <name> -s project   # Target specific scope
python3 scripts/delete_skill.py <name> -a cursor    # Delete from specific agent
python3 scripts/delete_skill.py <name> --all-agents --force  # Delete from all agents
```

**Multi-agent deletion:** Skills installed via `npx skills add` may exist in multiple agent directories. The default mode (no flags) deletes from Claude Code only and warns if copies remain in other agents. Use `--all-agents` to delete from every detected agent at once.

For ecosystem-installed skills, prefer `npx skills remove <name> -g -y` first. Use `delete_skill.py --all-agents` as fallback for manual cleanup.

### Move Skill

```bash
python3 scripts/move_skill.py <name> user      # Project → User (personal)
python3 scripts/move_skill.py <name> project   # User → Project (share with team)
python3 scripts/move_skill.py <name> user -f   # Overwrite if exists
```

### Modify Skill

1. Run `python3 scripts/show_skill.py <name>` to locate it
2. Edit SKILL.md directly at the returned path

### Create New Skill

Use the `/skill-creator` skill for guided creation with proper structure.

## Optimize a Skill (SkillOpt-style)

Treat a skill as a **trainable text artefact**: bounded edits + held-out validation gate + rejected-edit buffer + epoch-wise slow update. See [references/skill-optimization.md](references/skill-optimization.md) for the full method (Microsoft, arXiv 2605.23904, May 2026).

**When to use this loop:**
- Skill already exists and underperforms on a measurable task set
- You have (or can write) a verifier — exact-match, scored output, or LLM judge
- You can produce 20-100 representative tasks with reference answers

**When NOT to use:**
- Task has no measurable success signal — bounded text optimisation needs a gate
- Creating a skill from scratch — write a v0 with `/skill-creator` first
- Only 1-5 tasks available — the loop needs evidence batches

### Run the loop

```bash
# 1. Dry-run to see the plan (splits, schedule, prompt previews)
python3 scripts/optimize_skill.py <name> \
    --tasks tasks.jsonl --epochs 4 --edit-budget 4 \
    --output-dir runs/r1 --dry-run

# 2. Real run
python3 scripts/optimize_skill.py <name> \
    --tasks tasks.jsonl --output-dir runs/r1 \
    --optimizer-cmd "claude -p --model claude-opus-4-7" \
    --target-cmd  "claude -p --model claude-haiku-4-5-20251001"

# 3. Inspect
cat runs/r1/optimization_report.md
python3 scripts/diff_skill_versions.py <name> --files \
    runs/r1/initial_skill.md runs/r1/best_skill.md --format stats
```

The loop produces `best_skill.md`, `optimization_report.md`, `edit_apply_report.json`, `rejected_buffer.json`, and `meta_skill.json` (optimiser-side only — not shipped).

### Manual-edit audit trail

For edits made outside the loop (hand-tweaks, bug-fix follow-ups), keep a lightweight log:

```bash
# After saving an edit
python3 scripts/log_skill_edit.py <name> \
    --reason "tightened insert_after target" \
    --source from-bug --ref "issue #42" --snapshot

python3 scripts/log_skill_edit.py <name> --list --since 30d
python3 scripts/diff_skill_versions.py <name> --log
```

`--snapshot` saves a copy under `<skill>/.skill_snapshots/SKILL.<sha8>.md` so the diff helper can show actual content, not just hashes.

### Protected slow-update section

A skill that gets optimised iteratively should include a markup-fenced region for longitudinal guidance:

```markdown
<!-- SLOW_UPDATE_START -->
<!-- This block is managed by the epoch-boundary slow-update process.
     Step-level edits never modify it. -->
<!-- SLOW_UPDATE_END -->
```

`scripts/review_skill.py` flags unbalanced or nested markers. `scripts/optimize_skill.py` refuses to apply step-level edits that target content inside this region.

### Trigger and transfer tests

```bash
# Auto-generate candidate trigger cases from the skill's description
python3 scripts/trigger_test.py <name> --generate > cases.yaml
# Curate, then run
python3 scripts/trigger_test.py <name> --cases cases.yaml --threshold 0.8

# Verify skill lands and parses in other agents
python3 scripts/transfer_test.py <name> --all --scope global
```

## Discover & Install Skills

Search and install skills from the open agent skills ecosystem via the [Skills CLI](https://github.com/vercel-labs/add-skill) (`npx skills`). Browse at [skills.sh](https://skills.sh).

### Find Skills

```bash
npx skills find [query]              # Interactive search
npx skills find react performance    # Keyword search
npx skills find pr review            # Search by task
```

### Install from Ecosystem

```bash
npx skills add <owner/repo@skill> -g -y    # Install globally, skip prompts
npx skills add vercel-labs/agent-skills@vercel-react-best-practices -g -y
```

### List Ecosystem Skills

```bash
npx skills list                      # List all installed ecosystem skills
npx skills ls                        # Alias
npx skills list -g                   # Global skills only
npx skills list -a cursor            # Skills for a specific agent
```

### Remove Ecosystem Skills

Uninstalls skills installed via `npx skills add`. For locally-created skills, use `python3 scripts/delete_skill.py` instead.

**CRITICAL**: Always confirm with the user before removing.

```bash
npx skills remove <name> -g -y       # Remove a global skill, skip prompt
npx skills rm <name>                 # Alias, with confirmation prompt
npx skills remove <name> -a cursor   # Remove from specific agent
npx skills remove --all -g -y        # Remove all global ecosystem skills
```

### Check & Update

```bash
npx skills check                     # Check for available updates
npx skills update                    # Update all installed skills
```

When the user asks to "update skills", "update all skills", "are my skills up to date?", or "check for updates":

1. Run `npx skills check` first to show what has updates available
2. If updates exist, confirm with user before running `npx skills update`
3. After updating, remind user to restart the agent for changes to take effect

### When to Search

Use `npx skills find` when the user:
- Asks "how do I do X" where X is a common task
- Says "find a skill for X" or "is there a skill for X"
- Wants specialized capabilities (design, testing, deployment, etc.)

### Common Search Categories

| Category | Example queries |
|----------|----------------|
| Web Dev | react, nextjs, typescript, tailwind |
| Testing | testing, jest, playwright, e2e |
| DevOps | deploy, docker, kubernetes, ci-cd |
| Docs | docs, readme, changelog, api-docs |
| Quality | review, lint, refactor, best-practices |
| Design | ui, ux, design-system, accessibility |
| Productivity | workflow, automation, git |

### Review & Compare Results

**Always suggest reviewing found skills after a search.** After presenting search results, ask the user if they'd like you to review and compare the top candidates before installing.

When there are 2+ results, proactively offer to fetch and assess the top candidates. This is agent-driven — use WebFetch on `https://skills.sh/<owner>/<repo>/<skill>` pages and apply judgment.

**Always offer review when:**
- Any search returns results (ask: "Want me to review these skills before you install?")
- 3+ results returned — review is especially valuable
- Multiple results with similar names or overlapping descriptions
- User asks to compare, review, evaluate, or pick the best
- A result has suspicious metrics (niche topic with very high installs)

**Process:**
1. Present the search results summary first
2. Ask the user if they want you to review/compare the top candidates
3. If yes: fetch skills.sh pages for top 3-6 candidates
4. Evaluate quality signals: install count, agent distribution, age, description, relevance, overlap with installed skills
5. Assign verdict: Recommended / Consider / Skip
6. Present ranked summary with 1-2 sentence assessments

See [references/remote-skill-assessment.md](references/remote-skill-assessment.md) for the full assessment framework including red flags and scoring signals.

### No Results

If no skills found: offer to help directly, then suggest `npx skills init <name>` to create a custom skill.

## Multi-Agent Operations

Manage skills across 42 supported AI coding agents. Full registry at [skills.sh](https://skills.sh).

### Supported Agents

| Agent ID | Display Name | Project Skills Dir | Global Skills Dir |
|----------|--------------|-------------------|-------------------|
| `adal` | AdaL | `.adal/skills` | `~/.adal/skills` |
| `amp` | Amp | `.agents/skills` | `~/.config/agents/skills` |
| `antigravity` | Antigravity | `.agent/skills` | `~/.gemini/antigravity/skills` |
| `augment` | Augment | `.augment/skills` | `~/.augment/skills` |
| `claude-code` | Claude Code | `.claude/skills` | `~/.claude/skills` |
| `cline` | Cline | `.cline/skills` | `~/.cline/skills` |
| `codebuddy` | CodeBuddy | `.codebuddy/skills` | `~/.codebuddy/skills` |
| `codex` | Codex | `.agents/skills` | `~/.codex/skills` |
| `command-code` | Command Code | `.commandcode/skills` | `~/.commandcode/skills` |
| `continue` | Continue | `.continue/skills` | `~/.continue/skills` |
| `crush` | Crush | `.crush/skills` | `~/.config/crush/skills` |
| `cursor` | Cursor | `.cursor/skills` | `~/.cursor/skills` |
| `droid` | Droid | `.factory/skills` | `~/.factory/skills` |
| `gemini-cli` | Gemini CLI | `.agents/skills` | `~/.gemini/skills` |
| `github-copilot` | GitHub Copilot | `.agents/skills` | `~/.copilot/skills` |
| `goose` | Goose | `.goose/skills` | `~/.config/goose/skills` |
| `iflow-cli` | iFlow CLI | `.iflow/skills` | `~/.iflow/skills` |
| `junie` | Junie | `.junie/skills` | `~/.junie/skills` |
| `kilo` | Kilo Code | `.kilocode/skills` | `~/.kilocode/skills` |
| `kimi-cli` | Kimi Code CLI | `.agents/skills` | `~/.config/agents/skills` |
| `kiro-cli` | Kiro CLI | `.kiro/skills` | `~/.kiro/skills` |
| `kode` | Kode | `.kode/skills` | `~/.kode/skills` |
| `mcpjam` | MCPJam | `.mcpjam/skills` | `~/.mcpjam/skills` |
| `mistral-vibe` | Mistral Vibe | `.vibe/skills` | `~/.vibe/skills` |
| `mux` | Mux | `.mux/skills` | `~/.mux/skills` |
| `neovate` | Neovate | `.neovate/skills` | `~/.neovate/skills` |
| `openclaw` | OpenClaw | `skills` | `~/.openclaw/skills` |
| `opencode` | OpenCode | `.agents/skills` | `~/.config/opencode/skills` |
| `openhands` | OpenHands | `.openhands/skills` | `~/.openhands/skills` |
| `pi` | Pi | `.pi/skills` | `~/.pi/agent/skills` |
| `pochi` | Pochi | `.pochi/skills` | `~/.pochi/skills` |
| `qoder` | Qoder | `.qoder/skills` | `~/.qoder/skills` |
| `qwen-code` | Qwen Code | `.qwen/skills` | `~/.qwen/skills` |
| `replit` | Replit | `.agents/skills` | `~/.config/agents/skills` |
| `roo` | Roo Code | `.roo/skills` | `~/.roo/skills` |
| `trae` | Trae | `.trae/skills` | `~/.trae/skills` |
| `trae-cn` | Trae CN | `.trae/skills` | `~/.trae-cn/skills` |
| `windsurf` | Windsurf | `.windsurf/skills` | `~/.codeium/windsurf/skills` |
| `zencoder` | Zencoder | `.zencoder/skills` | `~/.zencoder/skills` |

### Detect Installed Agents

```bash
python3 scripts/detect_agents.py              # List detected agents
python3 scripts/detect_agents.py --all        # Show all supported agents
python3 scripts/detect_agents.py -f json      # JSON output
```

### List Skills for Any Agent

```bash
python3 scripts/list_agent_skills.py --agent cursor           # Single agent
python3 scripts/list_agent_skills.py --agent goose -s global  # Specific scope
python3 scripts/list_agent_skills.py --all                    # All detected agents
python3 scripts/list_agent_skills.py --agent amp -f json      # JSON output
```

### Install Skill to Agents

```bash
python3 scripts/install_skill.py /path/to/skill --agent cursor              # Single agent
python3 scripts/install_skill.py /path/to/skill --agent cursor --agent amp  # Multiple agents
python3 scripts/install_skill.py /path/to/skill --all                       # All detected
python3 scripts/install_skill.py /path/to/skill --agent goose -s global     # Global scope
python3 scripts/install_skill.py /path/to/skill --agent cursor --force      # Overwrite
```

### Copy Skill Between Agents

```bash
python3 scripts/copy_skill.py my-skill --from claude-code --to cursor
python3 scripts/copy_skill.py my-skill --from claude-code --to cursor --to-scope global
python3 scripts/copy_skill.py my-skill --from claude-code --from-scope project --to amp
python3 scripts/copy_skill.py my-skill --from claude-code --to cursor --force
```

### Move Skill Between Agents

```bash
python3 scripts/move_skill_agent.py my-skill --from claude-code --to cursor
python3 scripts/move_skill_agent.py my-skill --from claude-code --to goose --force
```

## Important Notes

- **Restart required for new top-level dirs**: Creating a top-level `skills/` directory that did not exist when the session started requires restarting Claude Code so the directory can be watched
- **Live change detection (Claude Code, 2026)**: Adding, editing, or removing a skill under `~/.claude/skills/`, project `.claude/skills/`, or `.claude/skills/` inside an `--add-dir` directory takes effect within the current Claude Code session — no restart needed
- **Edits are immediate**: Changes to existing skill content work without restart
- **Agent detection**: Uses config directory presence to detect installed agents
- **Always update all agents**: When updating a locally-developed skill, use `install_skill.py --all -s global --force` to push changes to every detected agent — not just Claude Code. A skill updated only in `~/.claude/skills/` will be stale in all other agents
- **Custom commands have merged into skills (Claude Code, 2026)**: A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy`. Existing `.claude/commands/` files keep working; skills add a directory for supporting files, frontmatter, and auto-invocation.
- **Plugin skills are namespaced** as `plugin-name:skill-name` and cannot conflict with user/project skills

## OpenCode-specific notes

OpenCode (anomalyco/opencode v1.14.x) reads skills from **multiple compatible locations** in addition to its native paths:

- Project: `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` — all loaded
- Global: `~/.config/opencode/skills/`, `~/.claude/skills/`, `~/.agents/skills/` — all loaded
- Walks up from CWD to the git worktree root, collecting skills along the way

This means a single Anthropic-format `SKILL.md` skill works across Claude Code, Codex, and OpenCode unchanged. Optional polish for OpenCode users:
- Add `compatibility: opencode,claude-code,codex` to the frontmatter
- Use lowercase tool names if your skill body invokes tools (`bash`, `edit`, `read` — not `Bash`/`Edit`/`Read`)

Skill access can be gated per-name with the `permission.skill` block in `opencode.json`:

```json
{ "permission": { "skill": { "*": "allow", "internal-*": "deny" } } }
```

See [references/opencode-skills.md](references/opencode-skills.md) for the full OpenCode skills reference.

## References — The Complete Guide to Building Skills for Claude

Consult these when reviewing skills or advising on skill structure and best practices.

| File | Description |
|------|-------------|
| `references/01-introduction.md` | What skills are, who this guide is for, two learning paths |
| `references/02-fundamentals.md` | Skill structure, progressive disclosure, composability, MCP integration |
| `references/03-planning-and-design.md` | Use cases, categories, success criteria, YAML frontmatter, writing instructions |
| `references/04-testing-and-iteration.md` | Trigger tests, functional tests, performance comparison, skill-creator usage |
| `references/05-distribution-and-sharing.md` | Distribution model, API usage, GitHub hosting, positioning |
| `references/06-patterns-and-troubleshooting.md` | 7 workflow patterns (incl. SkillOpt-style validated iterative refinement), common errors and fixes |
| `references/07-resources-and-references.md` | Official docs, example skills, tools, support channels |
| `references/ref-a-quick-checklist.md` | Pre-build, development, upload, and post-upload checklists |
| `references/ref-b-yaml-frontmatter.md` | Required/optional fields, security restrictions |
| `references/ref-c-complete-skill-examples.md` | Links to production-ready skill examples |
| `references/remote-skill-assessment.md` | Framework for evaluating ecosystem skills before installation |
| `references/skill-optimization.md` | SkillOpt-style training loop: bounded edits, validation gate, rejected buffer, slow/meta update (Microsoft, arXiv 2605.23904) |
| `references/optimization-artifacts-schemas.md` | JSON schemas for every artefact written by `optimize_skill.py` and `log_skill_edit.py` (splits, state, rollouts, proposals, decisions, edit_apply_report, rejected_buffer, meta_skill, etc.) |
| `references/optimization-grading-checklist.md` | Audit checklist for a finished optimization run — what to inspect in `best_skill.md`, `edit_apply_report.json`, `rejected_buffer.json` before shipping |
| `prompts/analyst_error.md`, `analyst_success.md` | Failure / success analysis prompt contracts for the optimiser |
| `prompts/merge_failure.md`, `merge_success.md`, `merge_final.md` | Hierarchical edit-merge contracts |
| `prompts/ranking.md` | Edit ranking and selection contract |
| `prompts/slow_update.md`, `meta_skill.md` | Epoch-boundary slow-update and optimiser-side meta-skill contracts |

## Acknowledgments

Multi-agent support is based on the [Skills CLI](https://github.com/vercel-labs/add-skill) (`npx skills`) by Vercel Labs. Browse the open agent skills ecosystem at [skills.sh](https://skills.sh).
