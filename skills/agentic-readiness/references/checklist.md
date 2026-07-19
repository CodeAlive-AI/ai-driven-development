# Agentic Readiness Audit Checklist

## Scope

- [ ] Identify the real Git root and current worktree.
- [ ] Determine whether this is a single repo, monorepo, or parent directory containing child Git repositories.
- [ ] Read the applicable instruction chain before other inspection.
- [ ] Preserve unrelated local and staged changes.

## Instruction topology

- [ ] Root `AGENTS.md` exists when Codex or OpenCode is supported.
- [ ] Root `CLAUDE.md` exists when Claude Code is supported.
- [ ] `CLAUDE.md` imports `@AGENTS.md` or intentionally contains Claude-only guidance.
- [ ] Independent `AGENTS.md` and `CLAUDE.md` copies are not drifting.
- [ ] `AGENTS.override.md` is intentional and does not unexpectedly mask `AGENTS.md`.
- [ ] Nested files contain only local deltas.
- [ ] Meta-repositories route to each child Git repository's instructions.
- [ ] Important nested instruction files are indexed selectively.
- [ ] Generated directories, dependencies, caches, and secondary worktrees are excluded.
- [ ] Codex's worst root-to-target chain fits the configured byte budget.
- [ ] Claude imports resolve and do not exceed five hops.
- [ ] OpenCode `instructions` globs cover nested files that must load automatically.

## Instruction quality

- [ ] Purpose and repository boundaries are explicit.
- [ ] Build, test, lint, format, and focused verification commands are accurate.
- [ ] Architecture entry points and non-obvious module boundaries are named.
- [ ] Naming, domain-language, and testing conventions are concrete.
- [ ] Destructive-action and secret-handling boundaries are clear.
- [ ] Git, release, and publishing rules match actual repository policy.
- [ ] Definition of done is verifiable.
- [ ] Detailed runbooks are routed on demand instead of copied.
- [ ] Contradictions and stale references are absent.

## Agent-specific surfaces

- [ ] Codex project/user config is syntactically valid and scoped appropriately.
- [ ] Claude Code project/local/managed settings are syntactically valid and non-conflicting.
- [ ] OpenCode project/global config is syntactically valid and scoped appropriately.
- [ ] MCP configurations expose only needed servers and contain no committed secrets.
- [ ] Skills have valid frontmatter, narrow triggers, and tested scripts.
- [ ] Subagents have clear roles and appropriate tool access.
- [ ] Hooks or CI enforce rules that cannot rely on model adherence.

## Scale and routing

- [ ] Count tracked files and identify directory hotspots.
- [ ] For more than 3,000 files, assess retrieval/context-engine support.
- [ ] Check the active chain from the repository root and representative deep directories.
- [ ] Check a parent-to-child-repository transition in meta-workspaces.
- [ ] Check secondary worktrees if used by the team.

## Verification

- [ ] Run `python scripts/audit_repo.py --root .`.
- [ ] Validate documented commands against package/build files.
- [ ] Run repository routing/link checks.
- [ ] Start fresh Codex, Claude Code, and OpenCode sessions where supported.
- [ ] Confirm active sources with Codex instruction listing/logs and Claude `/memory` or `InstructionsLoaded`.
- [ ] Review the final diff and report intentional gaps.

## Priority guide

- **P0:** The agent cannot get required project guidance, or guidance creates an immediate safety/correctness failure.
- **P1:** Cross-agent discovery is broken, canonical files drift, commands are wrong, or a context/routing issue frequently causes incorrect work.
- **P2:** Maintainability, portability, or efficiency issue with a practical workaround.
- **P3:** Optional improvement with limited current impact.
