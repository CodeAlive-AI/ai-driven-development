# Code Review Workflow

End-to-end process for reviewing a pull request or a diff, grounded in the book's heuristics.

## Table of Contents

- [When to Use](#when-to-use)
- [Prerequisites](#prerequisites)
- [Step 1: Understand the Change Set](#step-1-understand-the-change-set)
- [Step 2: Read the Tests First](#step-2-read-the-tests-first)
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
- [ ] Size check: is the change focused (ideally one commit ~= one concept)?
- [ ] Count distinct concerns in the diff — if > 1, flag for splitting

**Ask**: "If I had to summarise this PR in one sentence, what is it doing?"

**Reference**: `references/teamwork-git/rules.md` (50/72 rule, one-PR-one-thing)

---

### Step 2: Read the Tests First

**Goal**: Tests encode intent — read them before the production code.

- [ ] For each new/changed behaviour, is there a test?
- [ ] Do the tests follow AAA structure (Arrange / Act / Assert)?
- [ ] Would you believe the tests cover the stated behaviour?
- [ ] Any flaky patterns (time, random, network without isolation)?

**If no tests for a behaviour change**: block and ask why (reference `references/outside-in-tdd/rules.md`).

**Reference**: `references/outside-in-tdd/rules.md`, `references/code-navigation/rules.md`

---

### Step 3: Check Decomposition

**Goal**: Verify each unit fits in a head.

- [ ] Any method exceeds 80 cols × 24 rows?
- [ ] Cyclomatic complexity > 7 anywhere?
- [ ] Count of distinct variables in a method > 7?
- [ ] Any feature envy (method uses another class's data more than its own)?
- [ ] Cohesion OK (methods in a class share fields / serve one responsibility)?

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

- [ ] New logging in the right place (via Decorator, not littering code)?
- [ ] Any secrets, PII, or sensitive data risk of being logged?
- [ ] New endpoint → did we STRIDE it? (Optional deeper dive: `workflows/threat-model.md`)

**Reference**: `references/separation-of-concerns/rules.md`, `references/security/checklist.md`

---

### Step 7: Check Commit Hygiene

**Goal**: The history is the record — make it readable.

- [ ] Subject ≤ 50 chars, imperative mood?
- [ ] Body wrapped at 72 cols?
- [ ] Commits are small and focused (each one could compile + pass tests)?
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
[ ] Step 2: Read the tests first
[ ] Step 3: Decomposition OK (complexity, size, cohesion)
[ ] Step 4: Encapsulation OK (invariants, validation)
[ ] Step 5: API design OK (CQS, naming)
[ ] Step 6: Cross-cutting & security OK
[ ] Step 7: Commits OK (50/72, small, focused)
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
