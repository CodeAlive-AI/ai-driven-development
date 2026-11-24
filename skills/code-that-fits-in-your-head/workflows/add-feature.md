# Add a Feature Workflow

Build a new feature as a thin vertical slice, from the boundary inward, so that every unit stays small enough to hold in mind.

## Table of Contents

- [When to Use](#when-to-use)
- [What This Workflow Does Not Decide](#what-this-workflow-does-not-decide)
- [Prerequisites](#prerequisites)
- [Step 1: Name the Boundary and Its Contract](#step-1-name-the-boundary-and-its-contract)
- [Step 2: Cut the Thinnest End-to-End Slice](#step-2-cut-the-thinnest-end-to-end-slice)
- [Step 3: Parse at the Boundary into Domain Types](#step-3-parse-at-the-boundary-into-domain-types)
- [Step 4: Put Each Rule Where Its Data Lives](#step-4-put-each-rule-where-its-data-lives)
- [Step 5: Shape the API for Its Caller](#step-5-shape-the-api-for-its-caller)
- [Step 6: Listen to How Hard the Code Is to Check](#step-6-listen-to-how-hard-the-code-is-to-check)
- [Step 7: Widen the Slice Case by Case](#step-7-widen-the-slice-case-by-case)
- [Step 8: Attach Cross-Cutting Concerns](#step-8-attach-cross-cutting-concerns-if-needed)
- [Step 9: Preserve Coherent, Recoverable History](#step-9-preserve-coherent-recoverable-history)
- [Quick Checklist](#quick-checklist)
- [Common Mistakes](#common-mistakes)
- [Exit Criteria](#exit-criteria)

## When to Use

- Adding a new endpoint, command, or user-visible capability
- Starting a new feature from scratch

## What This Workflow Does Not Decide

| Question | Where it is decided |
|----------|---------------------|
| Which construction to build when there is more than one; where state lives; what happens on a retry, a crash or a version change; how a schema or contract with live clients changes | `pragmatic-architecture`, before this workflow starts |
| What an untrusted caller can reach and do | A threat model at design time (`pragmatic-architecture`) |
| Which checks to write, at which level, in what order relative to the code, and when the feature counts as done | `pragmatic-verification` |

This workflow prescribes neither test-first nor test-after. It shapes the code. The checks that prove the code are chosen with the verification skill and may be written before, during or after any step.

## Prerequisites

- A concrete description of the feature: an example input and the expected outcome
- A code base that builds and deploys (if not: `references/codebase-setup/checklist.md`)
- Knowledge of the outermost layer the feature enters through

**Primary references**: `references/encapsulation/`, `references/decomposition/`, `references/api-design/`

---

## Workflow Steps

### Step 1: Name the Boundary and Its Contract

**Goal**: Know where the feature begins and what it promises there.

- [ ] Identify the entry point: HTTP route, CLI subcommand, queue handler
- [ ] Write down the external contract: input shape, output shape, errors (status codes, exit codes)
- [ ] Note which existing types and modules the feature will touch

**Ask**: "What does the caller send, and what do they get back?"

---

### Step 2: Cut the Thinnest End-to-End Slice

**Goal**: One path from the boundary to the lasting effect, running, before any breadth.

- [ ] Pick the simplest case that crosses every layer the feature needs. Prefer one that writes data, so later cases have something to read
- [ ] Wire it through the real entry point to the real effect, with the simplest code at each layer
- [ ] Leave out edge cases, options and anything speculative
- [ ] Start from the boundary, not from the database schema: the schema follows from what the slice needs

A slice that runs end to end shows where the design resists while changing it is still cheap.

---

### Step 3: Parse at the Boundary into Domain Types

**Goal**: Past the boundary, an invalid value cannot exist.

- [ ] List the invariants: what must always be true of a valid input?
- [ ] Parse the wire format into a domain type that guarantees them (parse, don't validate)
- [ ] Keep the DTO and the domain type separate
- [ ] Map invalid input to the caller's error (400, not 500)

**Reference**: `references/encapsulation/rules.md`, `references/encapsulation/examples.md`

---

### Step 4: Put Each Rule Where Its Data Lives

**Goal**: Decisions in pure code, effects at the shell.

- [ ] Move branching out of the handler into the types that own the data
- [ ] Keep decisions pure; perform I/O and read time and randomness at the edge
- [ ] Give each unit one reason to change
- [ ] Prefer sequential composition over nested

**Reference**: `references/decomposition/rules.md`, `references/decomposition/patterns.md`

---

### Step 5: Shape the API for Its Caller

**Goal**: The wrong call is hard to write.

- [ ] Each method is a command or a query, never both
- [ ] The signature says what the name says (X-out test)
- [ ] What is required is required by the type, not by a comment

**Reference**: `references/api-design/rules.md`

---

### Step 6: Listen to How Hard the Code Is to Check

**Goal**: Use testability as a design signal.

- [ ] A unit that can only be exercised with a network, a clock or a long setup has a hidden dependency, or an effect mixed into a decision. Fix the design (Step 4), not the test
- [ ] A check that has to reach into private state means the unit hides something its callers need. Fix the API (Step 5)

This step is about the shape of the code. What to check, and how, is `pragmatic-verification`'s subject.

**Reference**: `references/code-navigation/rules.md` (rule 4)

---

### Step 7: Widen the Slice Case by Case

**Goal**: Grow the feature without losing the structure.

- [ ] Add the next case. When it is awkward to add, restructure first, then add it
- [ ] Measure after widening: complexity above 15, new cycles, duplicated rules, cross-module coupling
- [ ] Remove the scaffolding of earlier steps: stubs, hard-coded values, temporary paths

**Reference**: `references/decomposition/smells.md`, `references/tooling/commands.md`

---

### Step 8: Attach Cross-Cutting Concerns (if needed)

**Goal**: Logging, metrics, caching — without mixing them into domain logic.

- [ ] Attach the concern at an explicit seam: Decorator, middleware, filter, pipeline, or domain behavior according to scope
- [ ] Log at the boundary of I/O (requests, failures), not on pure functions
- [ ] Keep wiring visible in the composition root or framework registration

**Reference**: `references/separation-of-concerns/patterns.md`, `references/separation-of-concerns/rules.md`

---

### Step 9: Preserve Coherent, Recoverable History

**Goal**: Each commit is a viable state.

- [ ] Preserve known-good checkpoints appropriate to the architecture and recovery plan
- [ ] Use concise imperative subjects that follow repository policy
- [ ] Keep behavior changes and mechanical refactoring distinguishable without forcing broken intermediate states

**Reference**: `references/teamwork-git/rules.md`

---

## Quick Checklist

```
[ ] Step 1: Boundary and contract named
[ ] Step 2: Thinnest slice runs end to end
[ ] Step 3: Domain types carry the invariants
[ ] Step 4: Decisions pure, effects at the shell
[ ] Step 5: API hard to misuse
[ ] Step 6: Hard-to-check code fixed by design, not by test tricks
[ ] Step 7: Slice widened; complexity and scaffolding checked
[ ] Step 8: Cross-cutting concern attached at an explicit seam
[ ] Step 9: History coherent and recoverable
```

---

## Common Mistakes

| Mistake | Why It's Bad | Do Instead |
|---------|--------------|------------|
| Starting with the database schema | Locks the design before the slice shows what it needs | Start at the boundary; infer the schema |
| Building every layer broadly before one path runs | No feedback until the end | One thin slice end to end, then widen |
| Validating in the handler and again in the domain | Invariants scattered and drifting | Parse once at the boundary |
| Making hard-to-check code checkable with more mocks | Hides the design problem | Separate the decision from the effect |
| Leaving stubs and temporary paths behind | The next reader must hold them in mind | Remove scaffolding before the feature is done |

---

## Exit Criteria

The code of the feature is in shape when:
- [ ] The slice runs end to end through the real boundary
- [ ] Invariants live in types, and no unit is above the complexity threshold without a stated reason
- [ ] No scaffolding is left behind
- [ ] Commit history is accurate, coherent, and useful for recovery

Whether the feature works, and whether the evidence is enough to call it done, is decided with `pragmatic-verification`.
