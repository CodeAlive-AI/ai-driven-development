# Add a Feature Outside-In Workflow

Build a new feature from the outside (HTTP / CLI boundary) inward to the domain, test-first.

## Table of Contents

- [When to Use](#when-to-use)
- [Prerequisites](#prerequisites)
- [Step 1: Clarify the Boundary](#step-1-clarify-the-boundary)
- [Step 2: Write the Boundary Test First](#step-2-write-the-boundary-test-first)
- [Step 3: Make the Boundary Test Pass with the Thinnest Possible Slice](#step-3-make-the-boundary-test-pass-with-the-thinnest-possible-slice)
- [Step 4: Triangulate with Additional Boundary Cases](#step-4-triangulate-with-additional-boundary-cases)
- [Step 5: Drive Inward — Extract the Domain Model](#step-5-drive-inward--extract-the-domain-model)
- [Step 6: Unit-Test the Domain](#step-6-unit-test-the-domain)
- [Step 7: Decompose If Needed](#step-7-decompose-if-needed)
- [Step 8: Add Cross-Cutting Concerns](#step-8-add-cross-cutting-concerns-if-needed)
- [Step 9: Threat-Model If Publicly Exposed](#step-9-threat-model-if-publicly-exposed)
- [Step 10: Commit in Small, Reversible Steps](#step-10-commit-in-small-reversible-steps)
- [Quick Checklist](#quick-checklist)
- [Common Mistakes](#common-mistakes)
- [Exit Criteria](#exit-criteria)

## When to Use

- Adding a new endpoint, command, or user-visible capability
- Starting a new feature from scratch
- You want the fastest credible path to a deployable slice

## Prerequisites

- A code base with a basic walking skeleton (CI, tests runnable, a deployable build)
- A concrete description of the feature (user story, example input/output)
- Understanding of the existing boundaries (what's the outermost layer?)

**Primary references**: `references/outside-in-tdd/`, `references/encapsulation/`, `references/api-design/`

---

## Workflow Steps

### Step 1: Clarify the Boundary

**Goal**: Name the outermost entry point — where the feature begins.

- [ ] Identify the boundary: HTTP route, CLI subcommand, queue handler, etc.
- [ ] Sketch the external contract: input shape, output shape, errors
- [ ] Decide status codes / error shapes if HTTP; exit codes if CLI

**Ask**: "What does the user type / send, and what do they get back?"

**Reference**: `references/outside-in-tdd/knowledge.md` (walking skeleton, vertical slice)

---

### Step 2: Write the Boundary Test First

**Goal**: A test at the outermost layer that fails.

- [ ] Write one test at the boundary (e.g. `HttpClient.PostAsync`) covering the happy path
- [ ] Use AAA structure
- [ ] Keep assertions light at this level (status code, key response field)
- [ ] Run the test — verify it FAILS (and fails for the right reason)

**If the test passes without any production code**: your test isn't testing what you think. Fix it.

**Reference**: `references/outside-in-tdd/rules.md` (AAA, see tests fail)

---

### Step 3: Make the Boundary Test Pass with the Thinnest Possible Slice

**Goal**: Hard-coded response that makes the test green.

- [ ] Return a hard-coded response or always-success
- [ ] Add only the wiring needed to reach the handler
- [ ] No database, no domain logic yet — just plumb the call
- [ ] Run: all tests green

**Reference**: `references/outside-in-tdd/patterns.md` (Walking Skeleton), `references/outside-in-tdd/examples.md`

---

### Step 4: Triangulate with Additional Boundary Cases

**Goal**: Force the implementation to generalise.

- [ ] Add a second test case that fails with the hard-coded version
- [ ] Use parametrised tests when the cases share structure
- [ ] Apply the Devil's Advocate: "what input would break my current code?"
- [ ] Add tests until the implementation is the simplest generalisation

**Reference**: `references/outside-in-tdd/rules.md` (Devil's Advocate, red-green-refactor, when enough tests)

---

### Step 5: Drive Inward — Extract the Domain Model

**Goal**: Move logic from the controller into typed domain objects.

- [ ] Identify the invariants (what must always be true for a valid input?)
- [ ] Parse input at the boundary into a domain type with those invariants guaranteed
- [ ] Follow parse-don't-validate: return `null` / `Result` from the parse function
- [ ] Move branching logic out of the controller; let types do the work

**Reference**: `references/encapsulation/rules.md`, `references/encapsulation/examples.md`

---

### Step 6: Unit-Test the Domain

**Goal**: Inner units have their own fast unit tests.

- [ ] Write unit tests for each domain method (AAA, one assertion concept)
- [ ] Use parametrised tests for invariants ("any negative quantity rejected")
- [ ] Use a Fake (not a mock) for I/O dependencies
- [ ] Keep domain tests fast (milliseconds) — they're the feedback loop

**Reference**: `references/outside-in-tdd/patterns.md` (Fake Object), `references/outside-in-tdd/examples.md`

---

### Step 7: Decompose If Needed

**Goal**: Keep units small.

- [ ] Any method now exceeds 80×24 or complexity > 7? Decompose.
- [ ] Prefer sequential composition over nested
- [ ] Extract pure helpers; keep side effects at the shell
- [ ] Re-run tests after each extraction

**Reference**: `references/decomposition/rules.md`, `references/decomposition/patterns.md`

---

### Step 8: Add Cross-Cutting Concerns (if needed)

**Goal**: Logging, metrics, caching — without littering the code.

- [ ] Use a Decorator pattern, not inline calls
- [ ] Log at the boundary of I/O (requests, failures), not on pure functions
- [ ] Register the decorator at composition root

**Reference**: `references/separation-of-concerns/patterns.md`, `references/separation-of-concerns/rules.md`

---

### Step 9: Threat-Model If Publicly Exposed

**Goal**: New endpoint → STRIDE check.

- [ ] Run through `workflows/threat-model.md` if the feature is reachable by untrusted input
- [ ] Add authn / authz / input limits / audit logging as needed

**Reference**: `workflows/threat-model.md`

---

### Step 10: Commit in Small, Reversible Steps

**Goal**: Each commit is a viable state.

- [ ] Commit after each green test + refactor
- [ ] Subject ≤ 50 chars, imperative mood
- [ ] Keep test-only and production-only refactors in separate commits

**Reference**: `references/teamwork-git/rules.md`

---

## Quick Checklist

```
[ ] Step 1: Boundary identified
[ ] Step 2: Boundary test fails
[ ] Step 3: Thinnest slice makes it pass
[ ] Step 4: Triangulated with Devil's Advocate
[ ] Step 5: Domain types with invariants
[ ] Step 6: Domain unit-tested
[ ] Step 7: Decomposition OK
[ ] Step 8: Cross-cutting via Decorator
[ ] Step 9: Threat-modelled if exposed
[ ] Step 10: Small, clean commits
```

---

## Common Mistakes

| Mistake | Why It's Bad | Do Instead |
|---------|--------------|------------|
| Starting with the database schema | House-building thinking; locks design | Start at the boundary; infer schema later |
| Writing all tests first, then all code | Big-bang; no feedback loop | One test → one slice → refactor → repeat |
| Mocking everything | Tests decouple from reality | Use Fakes for I/O, real objects for domain |
| Skipping the "see it fail" step | Green-from-start tests assert nothing | Always watch the test fail first |
| Inflating the first slice | Never reach green | Hard-code until the next test forces generalisation |

---

## Exit Criteria

Feature is done when:
- [ ] All boundary tests pass
- [ ] Domain unit tests pass
- [ ] Decomposition rules satisfied
- [ ] Threat model considered if applicable
- [ ] Commits follow 50/72 and small-focused principles
- [ ] Deployable end-to-end slice works
