# Pragmatic Verification

An Agent Skill that teaches a coding agent to verify its work with tests and checks that earn
their keep. It targets the usual failures of LLM-written tests: redundant cases, tests that
confirm the code with itself, mocks that test only mocks, brittle UI tests, flaky waits, and
"done" claimed without evidence.

Language-agnostic. Stack tooling lives in separate references.

## What it does

- **Sizes the effort.** A cosmetic change gets one look; access, money, deletion and migrations
  get negative cases, real storage and an independent review.
- **Follows one route:** contract → oracle → existing checks → cases from failure mechanisms →
  level and doubles → a test shown to fail → a pass through the running product → closeout on
  evidence.
- **Puts each check at the smallest boundary** that still contains the defect: unit,
  integration, contract, component, browser, e2e or device.
- **Plans QA passes** through browser, computer or phone use, and keeps a one-off pass from
  becoming a permanent test without a reason.
- **Audits an existing suite:** parallel workers on a cheaper model scan; the auditor verifies
  their claims and ranks concrete fixes.
- **Reports honestly:** each claim is verified, partially verified, not verified or blocked,
  with what ran and on which revision.

## Contents

```text
pragmatic-verification/
├── SKILL.md                     the route, the level table, prohibitions, what to read when
└── references/
    ├── case-design.md           requirement → cases: boundaries, states, time, combinations
    ├── levels-and-doubles.md    level choice, mocks vs real, databases, concurrency, migrations
    ├── test-quality.md          oracles, self-confirming and weak tests, showing a test can fail
    ├── ui-automation.md         permanent component, browser and e2e tests
    ├── exploratory-qa.md        passes through the running product
    ├── flaky-and-brittle.md     intermittent tests, quarantine, slow suites
    ├── evidence-and-closeout.md when to stop, review findings, the final report
    ├── suite-audit.md           auditing a project's tests and gates
    ├── suite-audit-worker.md    the brief for audit workers
    ├── llm-features.md          products that call an LLM at runtime
    ├── sources.md               the authority behind the rules
    └── stack-*.md               Python, TypeScript, JVM, .NET, Go, mobile tooling
```

The agent reads `SKILL.md` and opens a reference only when its trigger applies.

## Install

```bash
npx skills add CodeAlive-AI/ai-driven-development --skill pragmatic-verification
```

Or copy this folder to `~/.claude/skills/` (Claude Code) or `~/.agents/skills/` (Codex).

## Not for

Tool syntax tutorials, load testing, security audits, or evals of LLM output quality.
