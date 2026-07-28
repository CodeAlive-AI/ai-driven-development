# Executable Guardrails (Agent-Native)

> ⚠️ **Not from the book.** This editorial amendment reframes types, schemas, tests, and specifications for agent-authored code. See `knowledge.md`.

Agents benefit from constraints that reject invalid output mechanically. No language ranking is universal, and types alone do not prove behavior or intent.

## Complementary Guardrails

| Guardrail | Best at catching | Does not prove |
|---|---|---|
| Types and static checks | Invalid symbols, signatures, nullability, forbidden dependencies | Business correctness or runtime data shape |
| Runtime schemas/parsers | Invalid external data and configuration | Correct downstream decisions |
| Tests and properties | Behavior, invariants, regressions | Completeness when derived from the same mistaken assumption |
| Explicit contracts | Compatibility and caller/callee expectations | That implementation satisfies the contract without verification |
| Architecture checks | Cycles, layer violations, restricted dependencies | Good domain boundaries or product fit |

## Rules

1. **Use the strongest practical constraints for the repository.** New code should enable strict modes where they provide signal. Brownfield systems should ratchet toward stricter checks without flooding the change with unrelated noise.
2. **Type public and cross-module contracts.** Make optionality, failures, and variants explicit.
3. **Parse external data into stronger internal types.** Validate HTTP, files, environment, queues, and API responses at trust boundaries.
4. **Prefer domain types over primitive conventions.** Make invalid states difficult to express.
5. **Keep examples executable when they define behavior.** Use tests, doctests, schemas, or runnable samples instead of comments that silently drift.
6. **Fail closed at trust and security boundaries.** Accept compatibility only when it is deliberate and tested.
7. **Do not suppress a guardrail merely to unblock generation.** Narrow exceptions require a reason and an owner.
8. **Pair self-authored tests with independent evidence for material changes.** See `verification-loops.md`.

## Choosing a Stack

Evaluate properties rather than ranking languages:

- quality and completeness of types or stubs;
- runtime schema support;
- deterministic build and test tooling;
- dependency metadata, lockfiles, and provenance;
- static analysis and architecture-test support;
- ecosystem maturity and team competence.

A well-governed dynamic-language project can be safer than a poorly structured statically typed one.

## Antipatterns

| Pattern | Why it is dangerous |
|---|---|
| Broad `any`, ignore, or suppression to get green | Removes the constraint exactly where uncertainty exists |
| Types without runtime boundary validation | External data can still violate compile-time assumptions |
| Tests that duplicate implementation logic | Both can agree on the same error |
| Enabling every analyser in brownfield at once | Creates noise and encourages blanket suppression |
| Selecting a language solely for agent convenience | Ignores domain, ecosystem, operations, and team ownership |

## Relation to the Book

This strengthens always-valid objects and parse-don't-validate while preserving the book's gradual-ratchet advice for existing systems.
