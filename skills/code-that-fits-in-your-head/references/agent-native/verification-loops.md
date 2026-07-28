# Verification Integrity (Agent-Native)

> ⚠️ **Not from the book.** This editorial amendment covers agent-specific verification risks. See `knowledge.md`.

Agents can implement large changes successfully. The controlling factors are architecture, acceptance criteria, and trustworthy evidence—not a universal limit on lines, files, or task duration.

## Verification Strategy

Define before implementation:

1. the target architecture and invariants that must remain true;
2. explicit acceptance and non-regression criteria;
3. the canonical repository verification command;
4. focused checks for each meaningful checkpoint;
5. an independent source of truth for material behavior.

Checkpoints should align with coherent architectural or behavioral stages. Do not force per-line commits or artificial micro-steps when a larger transformation is systematic and mechanically verifiable.

## Feedback Layers

Use the cheapest relevant layer during implementation and the complete required set before acceptance.

| Layer | Examples | Protects against |
|---|---|---|
| Parse/build | compiler, formatter | Invalid syntax and build graph |
| Types/static checks | typechecker, lint, architecture rules | Contract drift, invented symbols, forbidden dependencies |
| Focused tests | unit, property, contract | Local logic and invariants |
| Integration/system tests | real boundaries, E2E | Cross-component behavior |
| Operational evidence | migration rehearsal, telemetry, rollback test | Deployment and lifecycle risk |
| Independent acceptance | existing contract, product criteria, hidden cases, human decision | Shared blind spots in agent-written code and tests |

Latency is repository-specific. A slower high-value verifier is not "catastrophic"; run it at an appropriate checkpoint or gate rather than deleting it for throughput.

## Rules

1. **Verify coherent checkpoints, not only the final result.** Detect divergence before it contaminates later work.
2. **Use the repository's canonical commands.** Keep local and CI behavior aligned.
3. **Do not weaken verification to obtain green output.** Never delete assertions, skip tests, broaden suppressions, or relax types without an explicit requirement change and reviewable rationale.
4. **Require an independent oracle for material risk.** Tests written from the same mistaken interpretation as the implementation are not independent evidence.
5. **Record evidence.** State what ran, what it establishes, what was not run, and remaining uncertainty.
6. **Preserve recovery points.** Large migrations need recoverable commits, worktrees, backups, reversible stages, or another appropriate rollback mechanism.
7. **Stop on contradictory evidence.** Revise the plan or architecture instead of patching around repeated failures.

## Independent Oracles

Choose according to the risk:

- existing tests or recorded production behavior;
- product acceptance criteria or examples supplied independently;
- schema, protocol, or compatibility contracts;
- property and metamorphic tests;
- a reference implementation or differential comparison;
- security/static analysis maintained separately from the change;
- human acceptance for architecture, intent, and residual risk.

No single oracle proves correctness. Independence means it did not originate from the same unverified assumption as the implementation.

## Red Flags

- The agent edits tests until they match the implementation without explaining a requirement change.
- CI differs materially from the local verification path.
- A large change has no architectural map or acceptance criteria.
- Every check is authored by the same agent from the same prompt.
- A failing gate is suppressed rather than understood.
- The report says "all tests pass" without naming what was run or what remains unverified.

## Relation to the Book

This extends outside-in TDD, troubleshooting, and automated gates. The book's red-green discipline remains useful; agent authorship adds the need to protect the oracle itself.
