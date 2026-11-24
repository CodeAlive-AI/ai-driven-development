# Pragmatic Architecture

> "For each desired change, make the change easy (warning: this may be hard), then make the easy
> change." — Kent Beck

An Agent Skill inspired by that line. It is a method for managing complexity in software
engineering: given the task and what the project really is, find the simplest design that is not
fragile, prepare the code so the change becomes easy, then make it.

## The idea

- **The best design for this project, not in general.** The answer follows from the inputs: the
  requirements, the existing code, its writers and consumers, the stakes, the deadline and the
  lifetime of the system. The same task gets a different design in a prototype and in a billing
  core.
- **Simple, but not fragile.** Simple means few things to hold in mind at once, not few lines. A
  design that breaks a required promise under a realistic sequence of events — a retry, a second
  writer, a partial failure, a migration — is out, however short it is.
- **Easy to change.** Among the designs that hold, prefer the one in which this change and the
  next plausible ones cost least, counting callers, migration, operation and recovery.
- **No technical debt by accident.** Shortcuts that the project's nature does not justify are not
  taken. Where debt is the right trade — a throwaway prototype, a hard deadline — it is taken
  knowingly and written down.

## What it does

- **Sizes the design** by what the change touches: an obvious change is made directly; money,
  deletion, access, concurrency, outside calls or migrations get the full route.
- **Finds the few facts that decide the choice** before choosing, instead of designing on
  assumptions.
- **Puts each guarantee where its violation is controlled**, with a property card and a
  counterexample for every promise at risk.
- **Compares against the simplest admissible alternative**, so extra machinery has to earn its
  place.
- **Plans the path of change:** the preparatory steps that make the change easy, in a safe order.

## Contents

```text
pragmatic-architecture/
├── SKILL.md                     core rule, sizing, the route, the property card
└── references/
    ├── context.md               reading the task and the system, criteria
    ├── models-and-boundaries.md state ownership, models, module boundaries, contracts
    ├── failure-and-recovery.md  retries, concurrency, partial failure, recovery
    ├── change-path.md           making the change easy, step order, migration
    ├── threat-model.md          what a hostile caller can force, as property cards
    ├── moves.md                 22 less obvious design moves
    └── sources.md               the authority behind the rules
```

The agent reads `SKILL.md` and opens a reference only when its trigger applies.

## Install

```bash
npx skills add CodeAlive-AI/ai-driven-development --skill pragmatic-architecture
```

Or copy this folder to `~/.claude/skills/` (Claude Code) or `~/.agents/skills/` (Codex).

For a large or risky change designed by several models at once, see
[architecture-consilium](https://github.com/CodeAlive-AI/pragmatic-orchestration/tree/main/skills/architecture-consilium).

## Not for

Code-level style and refactoring mechanics (`code-that-fits-in-your-head`), choosing tests
(`pragmatic-verification`), visual or UX design, or a clear local fix.
