# PR / Code Review Checklist

Use when you're asked to review a pull request, approve a change set, or decide whether a PR is ready to merge.

## Before You Start

- [ ] The PR has a clear title and description — you can tell at a glance what it does.
- [ ] You have time to do a proper review (a review that takes >1 hour is not effective; if the PR requires that, it's probably too big — decline and ask for a split).
- [ ] You know the author's intent (from the description or a linked ticket). If not, ask before reading code.

## Size and Focus

- [ ] The PR does **exactly one thing**. If it bundles unrelated concerns, ask to split.
- [ ] The change set is smaller than half a day's work. Rule of thumb: if you can't review it in under an hour, it's too big.
- [ ] No mixed-in reformatting. Pure-reformatting PRs are fine; mixed PRs are not.
- [ ] Not a "Death Star" commit that bundles refactors, features, and fixes together.

## Commit Hygiene

- [ ] Each commit message follows the **50/72 rule**: subject ≤50 chars, blank line, body wrapped at 72.
- [ ] Subject lines are in the **imperative mood** ("Add X", "Fix Y", "Return 404 for absent reservation" — not "Added" / "Fixed" / "Returns").
- [ ] Messages explain **why**, not just what (the diff already shows what).
- [ ] Commit history is a series of working snapshots — no commits that break the build or fail tests.
- [ ] Prose is well-written: correct spelling, punctuation, grammar.

## Build and Tests

- [ ] The code **builds** (CI green).
- [ ] **All tests pass**.
- [ ] **New behaviour has tests**. No new code path without a test exercising it.
- [ ] Tests are comprehensive and clear.
- [ ] If you're unsure, pull the branch and run it on your own machine.

## Readability — "Will I Be Okay Maintaining This?"

The fundamental review question. If the answer is no, reject.

- [ ] Does the code **fit in your head**? Methods short enough, complexity low enough.
- [ ] Is the **intent clear** without comments or author narration?
- [ ] Does the code work as intended (matches the stated goal in the PR description)?
- [ ] No needless duplication.
- [ ] Existing code in the codebase couldn't have solved this already (no reinvented wheel).
- [ ] Could this be simpler? If yes, suggest how.

## Invariants and Correctness

- [ ] Existing invariants are preserved (types, preconditions, postconditions, guard clauses).
- [ ] New invariants are enforced where they belong, not scattered.
- [ ] No silent weakening of checks (e.g. removed guard clauses, loosened types, disabled tests).
- [ ] Public API changes are deliberate and called out. Typos in public API names are worth fixing now (breaking change later would be worse).

## Review Process

- [ ] You're reading the code at **your own pace**, not being walked through it by the author.
- [ ] You're willing to **say no** if the bar isn't met — rejection is a real option, not sunk-cost appeasement.
- [ ] When you comment, you **offer a concrete alternative**, not just "I don't like this".
- [ ] You flag what you like as well as what you don't.
- [ ] Your tone is explicitly polite — tone is lost easily in async writing. Emojis help signal friendly intent.
- [ ] You avoid nitpicking formatting and variable names (fixable after merge) unless they're in a public API.

## Collective Ownership

- [ ] At least one reviewer other than the author has approved. (Pair/mob sessions count as approval.)
- [ ] More than one person on the team is now comfortable maintaining the changed code.
- [ ] No "single-owner" module is being created or reinforced.

## Integration

- [ ] The branch is being merged within ~4 hours of being ready for review (not days of stale).
- [ ] If the feature is incomplete, it is **hidden behind a feature flag** so mainline stays healthy.
- [ ] The merge won't force other open PRs into avoidable conflicts.

## Red Flags

Stop and address if you find:

- The PR is thousands of lines across dozens of files. **Decline it.** Ask for small, focused slices. Don't fall for sunk-cost reasoning ("they already spent a week on it").
- Commit messages like "WIP", "fix", "stuff", "Added", or "No empty saga". Ask for rewrites.
- Commits that don't build or don't pass tests in between working states.
- Tests removed, disabled, or weakened with no explanation.
- Public API names changed silently.
- Formatting churn mixed with logic changes — you can't tell real edits from noise.
- No new tests despite new behaviour.
- The author is narrating the code in review comments because it isn't self-explanatory.
- The review has been open for days with no activity — escalate or close.

## Quick Reference

| Aspect | Ideal | Acceptable | Red Flag |
|--------|-------|------------|----------|
| PR size | <½ day of work | A day's work | Days/weeks — decline |
| Review time | <30 min | Up to 1 hour | >1 hour — too big |
| Review latency | Hours | Same day | Days — fix the process |
| Commits | Many small, each green | Some larger, each green | Broken intermediate commits |
| Subject line | ≤50 chars, imperative | 50-72 chars, imperative | >72 chars or past tense |
| Scope | One thing | One thing + trivial fix | Multiple unrelated concerns |
| Tests | New behaviour fully tested | Most paths tested | No tests for new behaviour |
| Reviewers | 2+ approve (incl. non-author) | 1 non-author approves | Only author approves / self-merge |

## Decision Tree

1. **Is it too big?** → Decline. Ask for splits.
2. **Does it build and pass tests?** → No → Back to author.
3. **Does it fit in your head?** → No → Comment with concrete alternatives, send back.
4. **Are commits clean (50/72, imperative, explain why)?** → No → Ask for rewrite/squash.
5. **New behaviour tested?** → No → Ask for tests.
6. **Invariants preserved?** → No → Comment, send back.
7. **Would you be okay maintaining this?** → Yes → Approve. → No → Keep iterating.
