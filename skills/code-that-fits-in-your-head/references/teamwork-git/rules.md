# Teamwork and Git Rules

> **Source note:** This book-derived theme includes 2026 editorial reframing for agent-authored changes. Agent-specific additions are not from Seemann.

Rules for trustworthy history, integration, collective ownership, and review. Project conventions may define formatting and timing; this chapter preserves the engineering purpose rather than universal numbers.

## Core Rules

### 1. Write Accurate, Searchable Commit Messages

- Use a concise imperative subject.
- Explain why the change exists and any non-obvious constraints.
- Follow the repository's commit format when one is configured.
- Do not fabricate product or business rationale; obtain it from the issue, specification, or human owner.

Exact subject width and body wrapping are project conventions, not maintainability laws.

### 2. Preserve Useful Working History

Commit coherent known-good states that help diagnose, review, revert, or resume the work.

- A commit should have one explainable purpose and pass its required checks.
- Large systematic migrations may use larger commits when the transformation and verification are clearer that way.
- Avoid history made of arbitrary per-line or per-file checkpoints that obscures the design.

### 3. Integrate Frequently Enough to Control Divergence

Continuous integration means keeping work compatible with the shared mainline. Choose a cadence appropriate to concurrency, risk, and verification cost.

- Long-running work may stay isolated when required, but continuously rebase/merge and verify against current mainline.
- Use feature flags, branch-by-abstraction, or staged migration when incomplete behavior must integrate safely.
- Do not treat a fixed number of hours as the definition of CI.

### 4. Keep Each Review Architecturally Coherent

One review should have one explainable outcome. It may touch many files when the change is systematic and shares one architecture and acceptance contract.

- Separate unrelated cleanup and opportunistic refactors.
- Distinguish mechanical/generated changes from semantic decisions.
- Provide exact verification evidence and remaining uncertainty.
- Reject changes whose complexity, coupling, or debt cannot be evaluated—not changes merely because they are large.

### 5. Review Independently

Read the change, tests, architecture, and evidence at your own pace. Do not rely on an author's walkthrough or confident narrative to substitute for understandable code.

### 6. Preserve Human Ownership Where It Matters

Automated and agent review can screen for defects, but they do not create a second human maintainer or accept product, architectural, security, or operational risk.

- Apply repository-defined risk policy.
- Material changes require accountable human approval.
- Mechanical or routine changes may use lighter review only when policy or a machine-checkable predicate assigns that lane; the authoring agent cannot self-classify.
- Pairing or mobbing counts as human review when the participants actually understand the change.

See `../agent-native/reviewability.md` for the canonical risk-lane policy.

### 7. Make Rejection Actionable

- State the violated invariant, risk, or design concern.
- Offer a concrete alternative or required evidence.
- Distinguish blockers from optional improvements.
- Ignore sunk generation cost: cheap output does not justify permanent maintenance burden.

### 8. Protect the Integrity of Tests and Gates

Review changes to tests, suppressions, dependencies, permissions, and CI as carefully as production logic. A green result is not trustworthy if the change weakened the oracle.

## Guidelines

- Keep published history coherent and useful for bisection and recovery.
- Automate formatting and other objective style policy rather than spending human review on it.
- Rotate human ownership across important areas to reduce knowledge silos.
- Run the change locally or in an isolated environment when risk warrants it.
- Prefer asynchronous written rationale for durable decisions; use synchronous collaboration when ambiguity is cheaper to resolve together.

## Exceptions

- **Ephemeral code** may not need durable history or formal review.
- **Solo work** cannot create a second human owner; compensate with stronger automated evidence and deliberate later review for material risk.
- **Emergency response** may merge through an expedited lane with explicit follow-up and post-change review.

## Quick Reference

| Rule | Summary |
|---|---|
| Accurate messages | Record intent and rationale; follow project formatting |
| Useful commits | Preserve coherent known-good states |
| Control divergence | Integrate according to concurrency and risk, not a clock constant |
| Coherent reviews | Judge architecture and verification, not file count |
| Independent reading | Do not trust the author's narrative alone |
| Human ownership | Material risk requires accountable human approval |
| Actionable rejection | Explain the concern and required alternative |
| Protect gates | Test and CI changes can invalidate green evidence |
