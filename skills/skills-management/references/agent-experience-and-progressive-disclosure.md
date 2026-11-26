# Agent Experience (AX) & Progressive Disclosure Guide

Design principles for building Agent Skills and bundled CLIs that autonomous LLM executors can discover, navigate, execute, and recover from with minimal context waste.

## Contents

- [What Agent Experience Means for Skills](#what-agent-experience-means-for-skills)
- [Choosing the Right Primitive](#choosing-the-right-primitive)
- [Four-Tier Progressive Disclosure](#four-tier-progressive-disclosure)
- [Progressive Disclosure Anti-Patterns](#progressive-disclosure-anti-patterns)
- [AX for Bundled Scripts and CLIs (AXI)](#ax-for-bundled-scripts-and-clis-axi)
- [AX & Progressive Disclosure Review Checklist](#ax--progressive-disclosure-review-checklist)

## What Agent Experience Means for Skills

**Agent Experience (AX)** applies the rigor of UX and DX to AI coding agents. A skill is not documentation for a human reader — it is an **operating contract** executed under finite context attention, strict tool schemas, and non-interactive shells.

Good AX optimizes for five measurable outcomes:

- **First-try completion**: Clear preconditions, stop gates, and exact commands remove back-and-forth clarifications.
- **Minimal context footprint**: Only task-relevant rules enter the context window at any turn.
- **Deterministic execution**: Fragile parsing, hashing, validation, and staged filesystem swaps live in scripts rather than prose.
- **Zero interactive hangs**: Bundled CLIs never block waiting on `stdin` prompts or open-ended menus.
- **Self-healing recovery**: Errors state what failed, why, and the exact next command to fix or override safely.

## Choosing the Right Primitive

Selecting the wrong extension layer degrades AX — either by bloating every startup prompt or by hiding critical invariants behind probabilistic discovery:

| Primitive | Load / Trigger Model | Best For | Avoid For |
|---|---|---|---|
| **Always-on rules** (`AGENTS.md`, `GEMINI.md`, `CLAUDE.md`) | Unconditionally loaded every turn | Universal repo invariants, build/test commands, architecture boundaries (compact!) | Multi-step runbooks, domain checklists, or rare workflows |
| **Skill** (`SKILL.md`) | Progressive: frontmatter always loaded; body + files on demand | Repeatable workflows, domain protocols, decision trees, bundled helpers | Standing facts needed on every turn, or hard security gates |
| **Hook** (`hooks.json`, `PreToolUse`) | Deterministic lifecycle event | Enforcing non-negotiable safety guards, formatting, policy checks | Teaching complex reasoning or multi-step workflows |
| **MCP server** | Tool schemas injected into model context | Live external APIs, DBs, auth-gated remote services | Local file operations already handled by shell/scripts |
| **Bundled `scripts/`** | Executed out-of-context; only stdout/stderr enters context | Parsing, hashing, diffing, bulk checks, atomic file mutations | Open-ended synthesis or judgment calls |
| **Subagent** | Isolated context window | Broad codebase research, noisy log analysis, parallel fan-out | Single quick lookups or trivial edits |
| **Retrieval / RAG** | Query-time search | Large changing corpora (thousands of docs, tickets, code search) | Small procedural playbooks (<2,000 tokens) |

## Four-Tier Progressive Disclosure

Treat **available ≠ loaded** as the core invariant of context engineering. Structure every skill across four tiers:

### Tier 1 — Discovery Metadata (`name` + `description`)

- Loaded into every session's startup catalog (~50–100 tokens per skill).
- Subject to hard platform budgets: Claude Code truncates `description + when_to_use` at `1,536` characters and budgets ~2% of context (`~16,000` chars fallback); Codex budgets **2% of the model context window** in tokens (`~5,440` tokens on 272k; `8,000`-char fallback only when unknown), configurable via `[skills].max_context_tokens` up to `10,000` tokens, caps individual descriptions at `1,024` chars, prefers `short_description` when set, and lets you hide implicit injection via `agents/openai.yaml` (`policy.allow_implicit_invocation: false`) or disable skills for Codex via `[[skills.config]]` (`enabled = false`).
- **Front-load** what the skill does, **imperative trigger conditions** (`Use when...`, user phrasing, file extensions), and **negative triggers** (`Do not use for...` / `Not for...`).
- Write in third person with no XML angle brackets (`< >`), and keep descriptions distinct from sibling skills to prevent ambiguous routing.

### Tier 2 — `SKILL.md` Body (Router + Operating Contract)

- Loaded on demand when triggered or invoked via `/<name>`.
- Target **300–2000 tokens** (`review_skill.py` warns above 2000 and penalises above 4000).
- Act as an **execution router and invariant contract**: core workflow steps, safety rules, verification criteria, and a conditional routing table pointing to `references/`.
- **Front-load non-negotiables** at the top of `SKILL.md`: attention decays in the middle of long prompts, and Claude Code compaction re-attaches only the first `5,000` tokens per skill within a `25,000`-token combined budget.

### Tier 3 — On-Demand `references/` and `assets/`

- Split references by **decision branch or task phase** (e.g., `deduplication.md`, `antigravity-skills.md`, `optimization.md`), never as arbitrary textbook chapters (`chapter-1.md` … `chapter-7.md`).
- Keep the reference graph **flat (depth 1 from `SKILL.md`)** so agents reach any needed file in one read without hopping `SKILL.md` → `a.md` → `b.md`. Mention sibling files in backticks rather than chained Markdown links.
- Use **explicit conditional load cues** in `SKILL.md` (e.g., *"Read `references/skill-deduplication.md` before resolving conflicts or installing"*), never *"Read all references first"*.
- Include a `## Contents` TOC with anchor links in every Markdown file over 100 lines so agents can jump straight to relevant sections with line-range reads.

### Tier 4 — Out-of-Context Execution (`scripts/` and Subagents)

- Offload deterministic computation (YAML/JSONC parsing, SHA-256 hashing, token counting, staged swaps) into `scripts/` so source code and intermediate data never consume prompt tokens.
- For noisy or multi-file tasks (scanning large repos, parallel audits, browser/UI QA), isolate intermediate output inside a subagent and return only a structured verdict.

## Progressive Disclosure Anti-Patterns

- **Monolithic `SKILL.md`**: >2000–4000 tokens or >500 lines dumping full schemas, examples, and FAQs into the entry prompt.
- **Eager-loading directives**: Telling the agent to *"read all files in `references/`"* or *"load every reference before starting"*, which defeats progressive disclosure.
- **Nested reference chains**: `SKILL.md` linking to `a.md` which links to `b.md` — agents either miss `b.md` or waste extra turns traversing.
- **Orphaned reference files**: Leaving `.md` files under `references/` that `SKILL.md` never links or names; agents will not discover them reliably.
- **Content duplication**: Copying `SKILL.md` instructions into `README.md` or `AGENTS.md` (doubles context cost when both are read and causes instruction drift).
- **Human repo noise inside skill folders**: Putting `CHANGELOG.md`, `CONTRIBUTING.md`, `INSTALLATION_GUIDE.md`, or `LICENSE.md` inside a skill directory instead of the repository root.

## AX for Bundled Scripts and CLIs (AXI)

When a skill ships scripts, design their interface as an **Agent eXperience Interface (AXI)**:

1. **Non-interactive by default**: Detect terminals with `sys.stdin.isatty()`. In non-TTY agent shells, never block on `input()`; refuse destructive actions cleanly and print the exact flag (`--force`) to pass once the user confirms.
2. **Self-healing error messages**: Every failure should tell the agent *what* failed and the *exact command* to recover:
   - Wrong Python version → print `uv run <script> ...`
   - Accidental project-scope install from inside a skill folder → print the rewritten `--scope global` command
   - Unknown `--agent` ID → print the sorted list of valid IDs
   - Deleting a directory with active symlinks → print `delete_skill.py <name> --all-agents --force`
3. **Structured, bounded output**: Provide `--format json` alongside compact human-readable text; suppress ANSI progress bars/spinners when stdout is not a TTY; filter or summarize large payloads (never dump raw `SKILL.md` bodies like unfiltered `GetAllPlugins` RPC responses).
4. **Compound idempotent commands & portable paths**: Bundle fragile multi-step shell sequences into one script with staged atomic writes (`stage_and_swap`), PEP 723 dependency headers (`uv run`), and asset paths resolved relative to `Path(__file__).parent` rather than `Path.cwd()`.
5. **Safe mutations & supply-chain hygiene**: Support `--dry-run` and read-only preflight modes (`audit_skill_duplicates.py --candidate ... --fail-on-conflict`), use distinct exit codes (`0` success, `1` runtime/validation error, `2` policy/conflict gate), never echo credentials, and audit third-party `scripts/` like code dependencies.

## AX & Progressive Disclosure Review Checklist

Combine automated checks (`uv run scripts/review_skill.py --path <dir>`) with a quick manual AX pass:

- [ ] **Tier 1**: `description` (<1024 chars, third-person) includes clear trigger phrases, negative triggers, and zero XML `< >` tags
- [ ] **Tier 2**: `SKILL.md` body is 300–2000 tokens, front-loads critical invariants, and uses a conditional routing table for `references/`
- [ ] **Tier 3**: Every file in `references/` is linked from `SKILL.md` (depth 1, no orphans, no broken local links), files >100 lines have a `## Contents` TOC, and `SKILL.md` contains no eager "read all references" directives
- [ ] **Tier 4 / AXI**: Bundled scripts work non-interactively, offer `--format json` / `--dry-run` where relevant, emit actionable recovery hints on error, and avoid dumping unbounded context to stdout
