# Pragmatic Verification

**Gives a coding agent the right way of thinking about tests.**

In agent-driven development tests are a necessity and a trap at the same time. The agent needs
them to know its work is done. But badly chosen tests do more than miss what matters: they
become technical debt, slow every later change, make the project harder for the next agent to
work on and, in the end, make results worse. Typical LLM output is a pile of redundant cases,
tests that confirm the code with itself, mocks that only test mocks, brittle UI tests and
flaky waits.

This skill is about deliberate testing and verification: the right checks, at the right level,
in the right amount. Language-agnostic; stack tooling lives in separate references.

## What it gives the agent

1. **A decision map for choosing tests.** For each risk, the agent picks the cheapest check
   that still contains the mechanism of the possible defect: unit, integration, contract,
   component, browser, e2e or device. It decides what to mock and what must be real, which
   cases deserve a test at all, and which QA scenarios to walk through browser, computer or
   phone use.
2. **A catalogue of testing techniques** the agent can bring into a project when they fit:
   boundary and state models, property-based and metamorphic tests, contract tests, real-engine
   database tests, controlled clocks and failure injection, exploratory passes. The goal is a
   balance of test kinds that suits the project, not more tests.
3. **An audit of a project's whole verification system:** tests, gates, CI, flaky and slow
   suites. Parallel workers on a cheaper model scan, the auditor verifies their claims and ranks
   concrete improvements. On an existing project this is a good place to start.

## When to use it

- Planning or building a new feature.
- Fixing a bug: a regression test that is shown to fail on the old defect.
- Repairing failing, flaky or slow tests, or pruning a bloated suite.
- Reviewing tests someone (or some agent) wrote.
- Deciding whether the evidence is enough to call a task done.

## Deliberate, not ritual, TDD

Test-first done on autopilot does more harm than good: a test written first can still encode an
invented expectation, and an agent then writes code to satisfy its own guess. The skill keeps
TDD where it works, for a clear rule or a reproducible bug, and asks for what actually makes a
test worth having: an expected result from a source independent of the code, a test shown to
fail for the right reason, and a run of the real product when users touch the change.

## Contents

```text
pragmatic-verification/
├── SKILL.md                     the route, the decision map, prohibitions, what to read when
└── references/
    ├── case-design.md           requirement → cases: boundaries, states, time, combinations
    ├── levels-and-doubles.md    level choice, mocks vs real, databases, concurrency, migrations
    ├── test-quality.md          oracles, self-confirming and weak tests, TDD in its place
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
