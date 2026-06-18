# Reviewability as a Design Constraint (Agent-Native)

> ⚠️ **Not from the book.** This is an editorial amendment. Seemann covers code review and PR etiquette in Ch 9, but does NOT distinguish "readable" from "reviewable" or address the agent-as-author case. See `references/agent-native/README.md`.

"Readable code" and "reviewable code" look similar but optimise for different things. For agent-produced PRs, review-ability is the harder target.

## The Distinction

Seemann's readability (Ch 3.2.3) optimises for a human *reading to understand* — minutes of attention, goal is mental model. Reviewability optimises for a human *reading to approve* — seconds of attention, goal is a confident yes/no decision.

| Aspect | Readable (book) | Reviewable (agent-era) |
|--------|-----------------|------------------------|
| Reader's goal | Understand the code | Decide to approve |
| Time budget | Minutes | Seconds-to-a-minute |
| Unknowns tolerated | Some (reader fills in) | Near-zero |
| Verbosity preference | Condensed | Explicit |
| Confidence signal | "I get it" | "I believe the author verified it" |

They overlap: clear names, small functions, explicit contracts serve both. They diverge: clever condensation helps readability and hurts reviewability. A terse one-liner is beautiful to read and terrifying to approve — did the author consider the edge case it hides?

## Why It Matters More for Agent-Written Code

Human review is the rate-limiting step of the agent → production pipeline. If the agent generates a 400-line PR that takes 40 minutes to review, the agent's throughput advantage evaporates. Worse, reviewers under time pressure approve-with-skim, and silent defects slip through.

The agent's job isn't just "generate correct code." It's "generate code a human will confidently approve in under three minutes."

## Rules

1. **Small diffs.** Aim for < 200 net lines per PR. Split larger changes into a sequence of PRs that each stand alone.

2. **One concept per PR, one concept per commit.** A reviewer who bisects the PR mentally ("accept the new feature, reject the style change") has already lost. Keep refactors separate from behaviour changes.

3. **Explicit over clever.** `const userIds = users.map(u => u.id)` beats `const userIds = users.map(u => u?.id).filter(Boolean)` when the latter hides an edge-case decision. If you're inlining a filter, spell out *why*.

4. **Names answer what AND why.** `calculateTax` is what; `calculateTaxForEuCustomer` is what + when. Reviewers don't have to jump to the call site to understand.

5. **Surface intent in the commit title AND the PR description.** The title is the TL;DR; the description is the review context. Both matter.

6. **PR description — agent edition** should include:
   - **Goal**: one sentence. What user-visible outcome?
   - **Approach**: one paragraph. Why this design?
   - **Alternatives considered and rejected**: two or three with reasons.
   - **What's uncertain**: areas you're unsure about, and what would change if the assumption is wrong.
   - **How to verify**: exact steps to sanity-check this locally.

7. **Mark assumptions and TODOs explicitly.** `// ASSUMPTION: callers always pass non-null X` is reviewable. Silent assumption is not. TODO comments with the thing-to-do + who-to-ask + when are reviewable; "TODO: figure out" is a request to the reviewer.

8. **Don't hide drive-by changes.** A `renamed this function while I was at it` in a feature PR is a trust-breaker. Separate PR, always.

9. **Keep the PR self-contained for local verification.** The reviewer shouldn't need to `git checkout + set up env + run e2e`. Ideally: `checkout; npm test -- <path>` and you're convinced.

10. **When in doubt, ask in the PR description, don't guess in the code.** The review is a collaborative decision, not a code puzzle.

## Red Flags in an Agent-Generated PR

| Flag | What it usually means |
|------|-----------------------|
| Silent refactor mixed with the feature | Agent couldn't resist; now review is 3× the work |
| New dependency added without justification | Possibly hallucinated; possibly bloat |
| Test-only file added that always passes | Fake test to satisfy "add tests" request |
| Comment says "TODO: handle this edge case" | Agent should have asked or handled; this is buck-passing |
| Large prose comment explaining what the code does | Names and types are underused; rewrite |
| "Fixed" several things with no root-cause explanation | Multiple suspected issues patched without understanding |
| Removed a test that was failing | Suppressed a signal rather than solving |

## Review Etiquette When the Author Is an Agent

Assume, while reviewing:

- Syntax is probably correct
- Types mostly check (if they don't, rebuild the stack)
- **Architecture may be questionable** — look here first
- **Edge cases may be missed** — look here second
- "Looks complete" ≠ "is complete" — ask the agent to enumerate what it *didn't* cover

## Agent → Reviewer Contract

A good agent PR gives the reviewer:

- A minimal, focused diff
- A commit history that tells the story
- A PR description that makes alternatives and uncertainties visible
- Verifiable claims ("runs locally with `npm test`")
- Explicit handling of known edge cases; explicit acknowledgment of unknown ones

The reviewer's contract in return:

- Approve fast when the above is met
- Request changes with specificity (line + rule + alternative), not vibes
- Reject early when the description shows the agent didn't understand the problem

## Relation to the Book

Seemann's Ch 9 (Teamwork — code review, PRs, rejecting change sets) sets the ground rules. His 50/72 commit-message rule and "small commits" principle (§9.1.3) directly serve reviewability. This file extends those norms to the case where the author is an agent and the reviewer is under specific time pressure to process many agent PRs per day.
