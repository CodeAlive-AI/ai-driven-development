# Accountable Review (Agent-Native)

> ⚠️ **Not from the book.** This editorial amendment covers review when an agent authors much of the change. See `knowledge.md`.

Reviewability is the ability to judge intent, architecture, behavior, risk, and evidence without trusting the agent's narrative. It is not measured by approval time, line count, or number of files.

## Large Changes

Do not reject a change merely because it spans thousands of lines. Large systematic migrations can be easier to validate than small tangled patches when they provide:

- a coherent target architecture and dependency direction;
- a precise transformation or implementation plan;
- explicit acceptance and non-regression criteria;
- trustworthy automated verification;
- clear exceptions, uncertainties, and recovery strategy;
- a diff structure that separates generated/mechanical changes from semantic decisions.

Split or stage work when doing so improves architecture, recovery, or verification—not to satisfy an arbitrary size target.

## Review Contract

An agent-authored change should state:

- **Goal**: intended product or engineering outcome.
- **Architecture**: boundaries, ownership, and dependency changes.
- **Approach**: why this design was chosen and what alternatives were rejected.
- **Verification**: exact commands and evidence, including what each check establishes.
- **Independent oracle**: source of truth not created from the same assumption as the implementation.
- **Risk and recovery**: data, security, compatibility, deployment, rollback, and residual uncertainty.
- **Debt delta**: duplication, coupling, temporary paths, TODOs, dependencies, or cleanup introduced or removed.

The agent must not invent business rationale or hide uncertainty behind confident prose.

## Risk Lanes

Review effort should reflect risk, but the authoring agent must never assign its own lane.

A lane is selected by repository policy, a machine-checkable predicate, or a human. If none applies, default to human review.

| Lane | Typical examples | Required ownership |
|---|---|---|
| Mechanical | deterministic generated output, formatting-only change | automated verification under repository policy |
| Routine | localized behavior with stable contracts and strong tests | normal human review or explicit repository policy |
| Material | architecture, security boundary, data migration, public contract, irreversible effect | accountable human approval and independent evidence |

Automated agent review is useful screening. It does not create a second human maintainer, transfer product ownership, or accept residual risk.

## What to Review First

1. Does the change preserve or improve architectural boundaries?
2. Does it introduce unnecessary abstraction, duplication, coupling, or dependencies?
3. Are invariants and side effects explicit?
4. Are tests and gates trustworthy, or were they weakened to match the implementation?
5. Are migration and temporary paths removed or assigned an exit condition?
6. Does the evidence support the claimed behavior and risk?

## Red Flags

- Mixed unrelated concerns with no architectural reason.
- New dependency without provenance or design justification.
- Tests changed only to make the implementation pass.
- Broad suppressions, disabled checks, or reduced assertions.
- Parallel implementations, flags, adapters, or TODOs without cleanup ownership.
- Large prose explanation compensating for unclear names, types, or boundaries.
- A low-risk label supplied only by the authoring agent.
- Claims of correctness based solely on merge rate, generated volume, or self-review.

## Relation to the Book

This extends the book's Git and code-review discipline. The durable principle is accountable, independent judgment—not a fixed PR size, review duration, or approval SLA.
