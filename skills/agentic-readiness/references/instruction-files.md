# Instruction Files Across Agents

Verified against official documentation on 2026-07-19.

## Contents

1. Recommended topology
2. Discovery differences
3. Lessons learned
4. What belongs in instruction files
5. Verification
6. Sources

## Recommended topology

Use one shared source of truth:

```text
repository/
├── AGENTS.md          # canonical cross-agent instructions
├── CLAUDE.md          # regular file containing: @AGENTS.md
└── packages/
    └── billing/
        └── AGENTS.md  # only billing-specific additions or overrides
```

Why this works:

- Codex and Codex App natively read `AGENTS.md`.
- OpenCode prefers `AGENTS.md` and uses `CLAUDE.md` only as a fallback.
- Claude Code does not natively read `AGENTS.md`, but officially supports importing it from `CLAUDE.md`.
- A regular import shim is portable to Windows and can carry a small Claude-specific section. A symlink also works, but is harder to create on Windows and cannot contain extra Claude-only guidance.

Keep `AGENTS.md` canonical unless the repository intentionally supports Claude Code only. Do not maintain full copies in both files.

## Discovery differences

| Surface | Project discovery | Nested behavior | Important limits |
|---|---|---|---|
| Codex CLI / Codex App | Builds a chain from Git/project root to the session working directory. At each level: `AGENTS.override.md`, then `AGENTS.md`, then configured fallback names; at most one file per directory. | The chain is built once per run/session. Later shell `cd` or work in another subtree/repository does not rebuild it. | Combined project instructions stop at `project_doc_max_bytes`, 32 KiB by default. `AGENTS.override.md` masks `AGENTS.md` at the same level. |
| Claude Code | Loads `CLAUDE.md` and `CLAUDE.local.md` while walking from filesystem root to the launch directory. | Discovers files below the launch directory lazily when it reads files in those subdirectories. `.claude/rules/` can be path-scoped. | `@imports` resolve relative to the importing file and recurse up to five hops. Imports improve organization but still consume startup context. Target under 200 lines per `CLAUDE.md`. |
| OpenCode | Walks upward from the current directory and prefers `AGENTS.md`; `CLAUDE.md` is a compatibility fallback. It also supports global `~/.config/opencode/AGENTS.md`. | Do not assume Codex-style chaining or Claude-style lazy loading. Use `opencode.json` `instructions` globs when multiple nested files must be loaded. | OpenCode does not automatically expand `@file` references in `AGENTS.md`; declare extra instruction files in `opencode.json` or explicitly tell the agent to read them. |

The same filesystem can therefore produce three different effective prompts. Audit what each agent actually loads, not just whether files exist.

## Lessons learned

### 1. Changing directories is not instruction discovery

In a meta-repository, an agent may start at the parent workspace and later run a command with `cwd=child-repo`. For Codex, that does not load the child repository's `AGENTS.md`: the instruction chain was already built when the session started.

Add this invariant to the meta-repository root:

```markdown
Before the first operation in a child Git repository, read that repository's
root `AGENTS.md` and the applicable instruction chain down to the target path.
Changing a command's working directory does not reload Codex instructions.
```

This is not a substitute for native discovery. It is an explicit bridge for long-lived sessions that cross Git roots.

### 2. Add a routing map, not copied rules

For a workspace with several child repositories, put a compact routing table in the parent `AGENTS.md`:

```markdown
| Repository | Local instructions | Scope |
|---|---|---|
| `backend` | [`backend/AGENTS.md`](backend/AGENTS.md) | API, jobs, tests, infrastructure |
| `landing` | [`landing/AGENTS.md`](landing/AGENTS.md) | Website, blog, localization, publishing |
```

The map should contain links and trigger descriptions only. Copying child rules into the parent wastes context, creates conflicting sources of truth, and can exhaust Codex's combined instruction budget before the more specific file is reached.

### 3. Index nested files selectively

Every repository-level file should state:

```markdown
Before editing or inspecting a target path, read every applicable `AGENTS.md`
from the repository root through the target directory. Do not load instructions
from unrelated subtrees.
```

List nested files explicitly when the repository has a meaningful instruction topology: many independent applications, localized legal trees, or several operational workspaces. Do not index generated output, dependencies, caches, virtual environments, secondary worktrees, or incidental test fixtures.

For small repositories, the invariant is enough. An exhaustive table that adds no routing value becomes another stale index.

### 4. Prefer a Claude import shim over duplication or symlinks

Use:

```markdown
@AGENTS.md
```

as the complete default `CLAUDE.md`. Add a Claude-specific section only when behavior truly differs.

Avoid two independently edited instruction files. A symlink is acceptable on Unix-heavy teams, but the import shim is easier to review, works without elevated Windows symlink support, and follows Claude Code's documented migration pattern.

### 5. `AGENTS.override.md` is an override, not an extension

Codex selects only one instruction file per directory. If `AGENTS.override.md` exists, the normal `AGENTS.md` at that level is skipped. Use overrides for deliberate temporary or environment-specific replacement, usually outside version control. Do not add one merely because a repository has nested scopes.

### 6. Context limits change architecture

Codex stops adding project instruction files after the configured combined byte limit. Claude Code warns that long files reduce adherence, and imported content still occupies context. Therefore:

- Keep the root file a navigation and policy layer, not a wiki.
- Put narrow rules close to the code they govern.
- Link to detailed runbooks and load them only when their trigger matches.
- Keep security invariants and required verification commands above optional background.
- Audit the worst root-to-subtree chain, not only each file independently.

### 7. Instruction files are not enforcement

An agent may miss, misread, or lose attention to a rule. If a condition must always hold, enforce it mechanically:

- routing-table drift check in CI;
- lint rule for canonical names;
- pre-commit or pre-push verification;
- hook for a lifecycle-critical action;
- repository policy for protected branches or signed commits.

Use `AGENTS.md` to explain intent and the correct workflow; use automation to guarantee invariants.

### 8. Test discovery from representative starting points

Test at least:

- repository root;
- a deeply nested application directory;
- the parent of a child Git repository in a meta-workspace;
- a secondary worktree if the team uses them.

For Codex, start a fresh run with `codex --cd <dir>` and ask it to list active instruction sources. For Claude Code, use `/memory` or the `InstructionsLoaded` hook. For OpenCode, start in the representative directory and verify the effective rules, including any `opencode.json` `instructions` globs.

### 9. Add a drift checker when routing is non-trivial

A useful CI check should fail when:

- a new repository-level or important nested `AGENTS.md` is not represented in the declared routing map;
- `CLAUDE.md` stops importing the canonical `AGENTS.md`;
- both files contain independent copies;
- a committed `AGENTS.override.md` unexpectedly masks normal rules;
- a generated or secondary-worktree instruction file leaks into the index.

Keep the checker repository-specific. Generic heuristics can identify candidates but cannot know which nested areas deserve an explicit route.

## What belongs in instruction files

Prefer facts and constraints that change agent decisions:

- repository purpose and boundaries;
- exact build, test, lint, format, and focused-test commands;
- architecture entry points that filenames do not reveal;
- naming and domain-language rules;
- branch, commit, release, and publishing requirements;
- destructive-action boundaries and secret-handling rules;
- definition of done and required verification;
- routing to task-specific skills and runbooks.

Move these elsewhere:

- long API or architecture documentation: normal docs, referenced on demand;
- repeated multi-step procedure: skill;
- non-negotiable lifecycle action: hook or CI;
- personal preference: global/user instructions;
- one-off task constraint: current prompt;
- secrets or credentials: never instruction files.

## Verification

After changing instruction topology:

1. Check `git diff` for accidental copies and unrelated files.
2. Run `python scripts/audit_repo.py --root .`.
3. Run repository-specific routing and link checks.
4. Start fresh sessions from representative directories.
5. Ask each agent which instruction sources are active and compare with the intended chain.
6. Verify that required commands are executable, not merely documented.

## Sources

- [OpenAI: Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [OpenAI: Codex customization](https://learn.chatgpt.com/docs/customization/overview)
- [Anthropic: How Claude remembers your project](https://code.claude.com/docs/en/memory)
- [OpenCode: Rules](https://opencode.ai/docs/rules/)
