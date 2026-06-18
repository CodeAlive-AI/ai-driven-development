# Verification Loops (Agent-Native)

> ⚠️ **Not from the book.** This is an editorial amendment added to cover an agent-specific concern Seemann does not address. See `references/agent-native/README.md`.

Why an agent's edit-verify cycle differs from human TDD — and how to structure it.

## The Core Difference

Seemann's TDD assumes human pace: minutes between red and green, a "cycle" of a few minutes. An agent runs `tsc --noEmit` in 0.5 seconds and a focused test in under one. The cycle shrinks by 10-100×.

**Consequence**: verification should happen *after every change*, not in batches. An agent that batches edits and verifies at the end inherits the worst properties of waterfall.

| Aspect | Human cycle (book) | Agent cycle |
|--------|-------------------|-------------|
| Red → green | 5-15 min | 0.5-10 s |
| Feedback source | Run test suite locally | Typecheck / focused test / grep |
| Failure cost | Cheap to revert | Near-zero — edit → verify → revert is a single loop |
| Optimal granularity | Per-feature slice | Per-line or per-hunk |

## Tiered Feedback Pyramid

Pick the *fastest* tool that can detect your class of error. Escalate only when the lower tier is green.

| Tier | Tool | Latency | Catches |
|------|------|---------|---------|
| 0. Syntax | Parse / compile | ms | Typos, unbalanced braces |
| 1. Types | `tsc --noEmit`, `mypy`, `pyright`, `cargo check`, `go vet` | seconds | Wrong signatures, invented methods, null-handling gaps |
| 2. Lint | `eslint`, `ruff`, `clippy` | seconds | Unused vars, dead code, anti-patterns |
| 3. Unit test | Focused test of the touched SUT | seconds | Wrong logic in the edited unit |
| 4. Integration | Multi-unit test, real DB | tens of seconds | Contract mismatches |
| 5. E2E | Full app, HTTP calls | minutes | System-level regressions |

**Rule**: the higher the tier, the fewer times per edit you should run it.

## Rules

1. **Verify after each edit, not "I'll test at the end".** An undetected error compounds through later edits.
2. **Run tier 1 (types) after every file change.** This catches the most common agent failure mode — invented symbols — before wasting a test run.
3. **Never skip a failing tier because "it's just a warning".** Warnings today are blockers tomorrow.
4. **Kill slow verification steps immediately.** A 60-second test step is catastrophic for agent throughput; rewrite it, split it, or run it only at gate time (pre-commit, not per-edit).
5. **Commit after each green cycle.** Each commit is a known-good revert point. Squash before PR if needed.
6. **Before editing: read the target file.** Don't edit from recall.
7. **After editing: run at least tier 1 before declaring done.** "It should work" is not a verification tier.

## Antipatterns

| Pattern | Why it's bad |
|---------|--------------|
| "Write 200 lines across 5 files, then run all tests" | A single failure buries root cause in noise |
| "Skip typecheck; the tests will catch it" | Tests are 10× slower; you're wasting your loop |
| "Comment out the failing test to get a green run" | Destroys the feedback; agent proceeds on false signal |
| "`any`/`// @ts-ignore` to unblock typecheck" | Removes the guardrail that was protecting the agent from itself |
| "Assume `git status` is clean" — never verify | Ships accidental junk files |

## Tool Setup for an Agent-Friendly Repo

- Watch mode on types: `tsc --watch --noEmit`, `pytest --watch`, `cargo watch`
- Pre-commit hook running tier 1-3 (fast tiers only)
- Fast focused-test runner (`pytest path/to/test_x.py::test_y`, `vitest run path/to/x.test.ts`)
- `--fail-fast` on the test runner
- A linter with auto-fix so style fixes don't consume agent loops
- A revert script / worktree setup so "let me try this approach" is cheap

## Relation to the Book

This builds on Ch 11 (Editing Unit Tests) and Ch 12 (Troubleshooting / slow tests). Seemann's "keep tests fast so you bisect quickly" applies here too, but with tighter tolerances. His "see tests fail first" rule holds — an agent that skips this step may pass tests that assert nothing.
