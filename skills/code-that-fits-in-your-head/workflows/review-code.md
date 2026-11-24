# Code Review Workflow

End-to-end process for reviewing a pull request or a diff, grounded in the book's heuristics.

## Table of Contents

- [When to Use](#when-to-use)
- [Prerequisites](#prerequisites)
- [Step 1: Understand the Change Set](#step-1-understand-the-change-set)
- [Step 2: Read the Tests for Intent](#step-2-read-the-tests-for-intent)
- [Step 3: Check Decomposition](#step-3-check-decomposition)
- [Step 4: Check Encapsulation](#step-4-check-encapsulation)
- [Step 5: Check API Design](#step-5-check-api-design-if-the-pr-changes-public-surface)
- [Step 6: Check Cross-Cutting & Security](#step-6-check-cross-cutting--security-if-applicable)
- [Step 7: Check Commit Hygiene](#step-7-check-commit-hygiene)
- [Step 8: Write the Feedback](#step-8-write-the-feedback)
- [Quick Checklist](#quick-checklist)
- [Common Mistakes](#common-mistakes)
- [Exit Criteria](#exit-criteria)

## When to Use

- A user asks to review a PR, a diff, or a set of changes
- A user asks "is this code good?" or "what's wrong with this code?"
- Before approving/merging a change set

## Prerequisites

- Access to the diff (or the full file if the change is small)
- Ability to run tests (ideally)
- Some sense of the code base's conventions

**Primary references**: `references/teamwork-git/checklist.md`, `references/decomposition/rules.md`, `references/api-design/rules.md`

---

## Workflow Steps

### Step 1: Understand the Change Set

**Goal**: Know what the change is trying to achieve before judging how it achieves it.

- [ ] Read the PR description / commit message. Is it clear *why*?
- [ ] Is the change architecturally coherent, even if it is large?
- [ ] Are unrelated cleanup and semantic changes separated?
- [ ] For systematic migrations, are the transformation, exceptions, and recovery path explicit?

**Ask**: "If I had to summarise this PR in one sentence, what is it doing?"

**Reference**: `references/teamwork-git/rules.md`, `references/agent-native/reviewability.md`

---

### Step 2: Read the Tests for Intent

**Goal**: Learn from the tests what the change is meant to do. Whether they are the right tests is not judged here.

- [ ] Read the tests of each new or changed behaviour before the production code: what do they say the code must do?
- [ ] A behaviour change with no check at all: block and ask why.
- [ ] Is some code hard to test because of a hidden dependency or a mixed effect? That is a design finding for Steps 3–4, not a testing problem.
- [ ] Did the change edit its own judges (tests, suppressions, analysers, CI)? Flag it.

Whether the tests are sufficient, sit at the right level and take their expected results from a source independent of the implementation is reviewed with `pragmatic-verification`.

**Reference**: `references/code-navigation/rules.md`

---

### Step 3: Check Decomposition

**Goal**: Verify each unit fits in a head.

Measure, don't estimate: complexity/cycle/duplication commands in `../references/tooling/commands.md`.

- [ ] Cyclomatic complexity > 15 anywhere, or lower complexity with opaque path interaction?
- [ ] Any method mixes unrelated responsibilities, effects, or abstraction levels?
- [ ] Too many unrelated values, mutable states, or dependencies interact at once?
- [ ] Any feature envy (method uses another class's data more than its own)?
- [ ] Cohesion OK (methods in a class share fields / serve one responsibility)?
- [ ] Any new cycles, layer violations, duplicated rules, broad coupling, or stale migration paths?

**Reference**: `references/decomposition/rules.md`, `references/decomposition/smells.md`

---

### Step 4: Check Encapsulation

**Goal**: Confirm invariants are protected at type level.

- [ ] Can any domain object be constructed in an invalid state?
- [ ] Is validation done once at parse time (parse-don't-validate) or scattered?
- [ ] Are DTOs and domain types distinct?
- [ ] Any `null!` or bypassed nullability? Ask why.
- [ ] 400 vs 500 distinction clear at API boundaries?

**Reference**: `references/encapsulation/rules.md`, `references/encapsulation/examples.md`

---

### Step 5: Check API Design (if the PR changes public surface)

**Goal**: The API should make wrong things hard to do.

- [ ] Does each method obey CQS (command OR query, never both)?
- [ ] Do names carry the design (X-Out test: blank names — does code still read)?
- [ ] Are affordances clear (what actions does this interface suggest)?
- [ ] Any comments that could be replaced by a better method/type name?

**Reference**: `references/api-design/rules.md`

---

### Step 6: Check Cross-Cutting & Security (if applicable)

**Goal**: Catch concerns that cut across layers.

- [ ] New logging/telemetry attached at an explicit seam appropriate to its scope?
- [ ] Any secrets, PII, or sensitive data risk of being logged?
- [ ] Queries and commands built from input are parameterised, never concatenated?
- [ ] Authorisation is checked on the server for each action, not inferred from what the client sends?
- [ ] New dependency → identity, provenance, locked version, and necessity verified?
- [ ] New entry point reachable by untrusted input, or a change in who may do what → was it threat-modelled when it was designed? If not, send it back to design (`pragmatic-architecture`).

These four lines are a reviewer's tripwire, not a security review. A security audit needs a dedicated security skill or reviewer.

**Reference**: `references/separation-of-concerns/rules.md`

---

### Step 7: Check Commit Hygiene

**Goal**: The history is the record — make it readable.

- [ ] Subjects are concise and imperative, following repository policy?
- [ ] Messages accurately explain non-obvious rationale?
- [ ] Commits preserve coherent known-good states useful for review or recovery?
- [ ] No drive-by refactors mixed with behaviour changes?

**Reference**: `references/teamwork-git/rules.md`

---

### Step 8: Write the Feedback

**Goal**: Give the author everything they need to respond.

- [ ] Separate blockers (must fix) from suggestions (nice to have)
- [ ] For each blocker: state the rule violated + point to the reference
- [ ] Offer a concrete alternative when possible
- [ ] Keep the total review under ~8 items; if more, pick the most important

**Ask**: "If I were the author, would I understand what to change?"

---

## Quick Checklist

```
[ ] Step 1: Understood the change's intent
[ ] Step 2: Tests read for intent; their quality handed to pragmatic-verification
[ ] Step 3: Complexity/debt delta understood (local + system structure)
[ ] Step 4: Encapsulation OK (invariants, validation)
[ ] Step 5: API design OK (CQS, naming)
[ ] Step 6: Cross-cutting & security OK
[ ] Step 7: History is accurate, coherent, and useful
[ ] Step 8: Feedback written (blockers vs suggestions)
```

---

## Common Mistakes

| Mistake | Why It's Bad | Do Instead |
|---------|--------------|------------|
| Reviewing line-by-line before understanding intent | Miss the forest for the trees | Read PR description + tests first |
| Flagging style nits as blockers | Drowns the real issues | Auto-format; reserve review for design |
| Approving without running the tests | Bugs slip through | Run locally or verify CI |
| Asking open-ended "why?" on everything | Review takes forever | Be specific: "rule X is violated here" |

---

## Exit Criteria

Review is done when:
- [ ] Every reviewer comment is either a blocker or marked as a suggestion
- [ ] Every blocker cites a rule / reference file
- [ ] Decision is explicit: approve / request changes / reject
