# Debug a Defect Workflow

Methodical, scientific-method debugging — from bug report to regression-proofed fix.

## Table of Contents

- [When to Use](#when-to-use)
- [Prerequisites](#prerequisites)
- [Step 1: Understand the Report](#step-1-understand-the-report)
- [Step 2: Reproduce the Defect](#step-2-reproduce-the-defect)
- [Step 3: Simplify to the Smallest Failing Case](#step-3-simplify-to-the-smallest-failing-case)
- [Step 4: Hypothesise, Then Test](#step-4-hypothesise-then-test)
- [Step 5: If It's a Regression, Bisect](#step-5-if-its-a-regression-bisect)
- [Step 6: Fix with the Test as a Guard Rail](#step-6-fix-with-the-test-as-a-guard-rail)
- [Step 7: Understand Root Cause](#step-7-understand-root-cause)
- [Step 8: Commit and Document](#step-8-commit-and-document)
- [Quick Checklist](#quick-checklist)
- [Common Mistakes](#common-mistakes)
- [Exit Criteria](#exit-criteria)

## When to Use

- A bug report or failing test arrives
- A test is flaky and needs investigating
- You need to find when a regression was introduced

## Prerequisites

- Ability to run the code / test suite locally (or in CI)
- Access to git history
- A reproducible or semi-reproducible failure (if not, Step 2 is where you fight)

**Primary references**: `references/troubleshooting/`, `references/outside-in-tdd/rules.md`

---

## Workflow Steps

### Step 1: Understand the Report

**Goal**: Restate the defect in your own words.

- [ ] Read the full bug report (or the failing test output)
- [ ] Identify: What was the user doing? What did they expect? What did they get?
- [ ] Rubber-duck explanation — say it out loud (or write it down)
- [ ] Ask yourself: could this be user error / environment / config rather than a defect?

**Ask**: "What's the single sentence description of the wrong behaviour?"

**Reference**: `references/troubleshooting/knowledge.md` (rubber ducking)

---

### Step 2: Reproduce the Defect

**Goal**: Make the bug happen on demand, ideally in an automated test.

- [ ] Try to trigger the bug in your local environment with the reported inputs
- [ ] If it reproduces → convert it into a failing unit / integration test (reproduce-as-test)
- [ ] If it doesn't reproduce → simplify the reported scenario progressively
- [ ] If non-deterministic → isolate sources of non-determinism (clock, random, threads, external state)

**If you can't reproduce**: do not "fix" it. Escalate for more info (steps, environment, timestamps).

**Reference**: `references/troubleshooting/patterns.md` (Reproduce-as-Test, Isolate-Then-Fix)

---

### Step 3: Simplify to the Smallest Failing Case

**Goal**: Remove everything that's not the defect.

- [ ] Keep halving the input / setup until the bug disappears; then re-add only the last piece
- [ ] Remove unrelated code from the repro
- [ ] Aim for a test that takes milliseconds and isolates a single assertion

**Reference**: `references/troubleshooting/rules.md` (simplification)

---

### Step 4: Hypothesise, Then Test

**Goal**: Use the scientific method — don't guess-and-change.

- [ ] Write down your hypothesis: "I think X causes Y because Z"
- [ ] Design the smallest experiment that would disprove or confirm it
- [ ] Run the experiment; record the result
- [ ] If disproven → new hypothesis; do NOT tweak code randomly

**Ask**: "What would I expect to see if my hypothesis is right? If it's wrong?"

**Reference**: `references/troubleshooting/knowledge.md` (scientific method)

---

### Step 5: If It's a Regression, Bisect

**Goal**: Find the exact commit that introduced the defect.

- [ ] Identify a known-good commit (or tag)
- [ ] Identify a known-bad commit (usually `HEAD`)
- [ ] Run `git bisect start; git bisect bad; git bisect good <commit>`
- [ ] At each step, run your reproduction test → `git bisect good` or `git bisect bad`
- [ ] Git announces the first bad commit

**If the suite is too slow for bisection**: first make it fast (cf. `references/troubleshooting/rules.md` on slow tests).

**Reference**: `references/troubleshooting/patterns.md` (Git Bisection)

---

### Step 6: Fix with the Test as a Guard Rail

**Goal**: Fix makes the failing test pass; don't break any other test.

- [ ] Apply the minimum change that makes the reproduction test pass
- [ ] Run the full test suite — all green
- [ ] Review: does the fix handle related cases, or only the exact repro?
- [ ] Add a few more test cases (Devil's Advocate) to cover the generalisation

**Reference**: `references/outside-in-tdd/rules.md` (Devil's Advocate)

---

### Step 7: Understand Root Cause

**Goal**: Don't ship a fix without knowing why the defect existed.

- [ ] Explain in one paragraph: why did this bug exist? What invariant was violated?
- [ ] Could the bug have existed because of a missing type constraint? (Parse-don't-validate miss.)
- [ ] Could tests have caught it earlier? (What test was missing?)
- [ ] Are there similar defects lurking elsewhere?

**Reference**: `references/encapsulation/rules.md` (invariants, parse-don't-validate)

---

### Step 8: Commit and Document

**Goal**: Leave the history readable.

- [ ] Commit the failing test + the fix
- [ ] Commit subject: imperative, ≤ 50 chars ("Fix off-by-one in date parser")
- [ ] Body explains: what was the symptom, what was the root cause, how the fix works
- [ ] If warranted, add a comment at the fix site — but ONLY if the why is non-obvious

**Reference**: `references/teamwork-git/rules.md`

---

## Quick Checklist

```
[ ] Step 1: Report understood and restated
[ ] Step 2: Bug reproduced (as a test)
[ ] Step 3: Failing case simplified
[ ] Step 4: Hypothesis → experiment → result
[ ] Step 5: Bisected if regression
[ ] Step 6: Minimum fix + suite green
[ ] Step 7: Root cause explained
[ ] Step 8: Commit with clear message
```

---

## Common Mistakes

| Mistake | Why It's Bad | Do Instead |
|---------|--------------|------------|
| "Fixing" without reproducing | You don't know you fixed it | Reproduce first, always |
| Random changes + re-run test | Wastes time, adds noise | Write a hypothesis; test it |
| Patching the symptom (add `if` around crash) | Bug re-appears as a different symptom | Find the root cause |
| Fixing without a test | Regression next sprint | Every defect fix includes a regression test |
| Bisecting with a slow suite | Wall-clock pain | Fix the slow tests first |

---

## Exit Criteria

Defect investigation is done when:
- [ ] A test reliably reproduces the original failure
- [ ] The test now passes with the fix applied
- [ ] Root cause is understood and documented in the commit message
- [ ] No other tests regressed
- [ ] (Optional) Similar areas of code scanned for the same root-cause pattern
