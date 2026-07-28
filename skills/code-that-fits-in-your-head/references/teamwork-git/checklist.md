# PR / Code Review Checklist

> **Source note:** This book-derived checklist includes 2026 editorial checks for agent authorship, verification integrity, and risk ownership.

Use for human or agent-authored changes. Judge architecture, evidence, and future change cost—not line count or approval speed.

## Intent and Architecture

- [ ] Goal and non-goals are explicit.
- [ ] The change is architecturally coherent, even if it spans many files.
- [ ] Dependency direction and ownership boundaries remain clear.
- [ ] Mechanical/generated edits are distinguishable from semantic decisions.
- [ ] Unrelated cleanup is excluded or justified separately.

## Complexity and Debt Delta

- [ ] No unnecessary abstraction, dependency, duplication, or indirection.
- [ ] Cyclomatic complexity above 15 is understood and justified or refactored.
- [ ] No new dependency cycles, layer violations, or cross-module sprawl.
- [ ] Temporary flags, adapters, parallel implementations, and TODOs have owners and exit conditions.
- [ ] The change makes future modifications no harder than necessary.

## Verification Integrity

- [ ] Canonical build and required checks pass.
- [ ] New behavior has appropriate tests or executable acceptance checks.
- [ ] Existing assertions, types, analysers, permissions, and CI were not weakened merely to get green.
- [ ] Material behavior has evidence independent of the implementation where practical.
- [ ] The report names what ran, what it proves, and what remains unverified.

## Invariants, Effects, and Security

- [ ] Domain invariants are enforced at the correct boundary.
- [ ] Side effects and failure behavior are explicit.
- [ ] Public contracts and migration/compatibility effects are called out.
- [ ] New dependencies have verified identity, provenance, locked version, and justification.
- [ ] Security, data, deployment, and rollback risks receive appropriate review.

## History and Rationale

- [ ] Commit messages are accurate, concise, imperative, and follow repository policy.
- [ ] Non-obvious decisions explain why; the agent has not invented business rationale.
- [ ] Commits preserve useful known-good or recoverable states.
- [ ] History supports review and diagnosis rather than arbitrary micro-checkpoints.

## Ownership and Review

- [ ] The reviewer reads independently rather than trusting an author walkthrough.
- [ ] Material residual risk is accepted by an accountable human.
- [ ] The authoring agent did not assign its own low-risk lane.
- [ ] Automated review is treated as screening, not a replacement for human ownership or bus factor.
- [ ] Blockers are separated from optional suggestions and include a concrete alternative or required evidence.

## Large Changes

Do not decline a change merely because it contains thousands of lines. Require:

- coherent target architecture;
- explicit transformation or implementation plan;
- trustworthy verification and acceptance criteria;
- documented exceptions and uncertainties;
- recovery, rollback, or safe continuation strategy.

Split or stage only when it improves architecture, verification, review, or recovery.

## Red Flags

- The change touches unrelated areas with no architectural explanation.
- Tests or gates were changed to accommodate the implementation without a requirement change.
- A new abstraction duplicates an existing capability.
- Generated prose is confident but evidence is missing.
- Migration scaffolding has no deletion path.
- Review depends on merge rate, file count, or "the agent already spent time on it."

## Decision

1. Is the intended outcome and architecture clear?
2. Does the change preserve maintainability and avoid unnecessary debt?
3. Is the verification trustworthy and proportional to risk?
4. Is ownership of residual risk explicit?
5. Would the team be comfortable changing this code later?

Approve, request changes, or reject with concrete reasons.
