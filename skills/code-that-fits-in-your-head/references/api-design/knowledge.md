# API Design Knowledge

Core concepts for designing public APIs that fit in readers' heads.

## Overview

An API is an affordance: the set of methods, values, functions, and objects a client has at its disposal. Good design advertises what is possible, makes illegal states hard to express, and communicates intent primarily through types and names rather than comments or documentation.

## Key Concepts

### Affordance

The API advertises capabilities through its types. What you cannot express is as important as what you can; well-encapsulated APIs expose only operations that preserve invariants. Discoverability comes from types, not documentation.

### Poka-Yoke (Mistake-Proofing)

Design so misuse is difficult or impossible. Active poka-yoke inspects as artifacts are created (e.g. TDD); passive poka-yoke builds the constraint into the shape of the thing (compile-time prevention). Prefer specialised APIs over Swiss Army knives (God Classes). A compiler error is faster feedback than a runtime exception.

### Command Query Separation (CQS)

Every method is either a Command (side effects, returns `void`) or a Query (returns data, no observable side effects) — never both. Local unobservable state changes do not count as side effects. Prefer Queries where possible. **CQS ≠ CQRS**: CQRS is an architectural style that borrows the terminology at a different scale.

### X-Out Names Exercise

Mentally replace every name with `Xxx` and ask whether the types alone still communicate what each method does. If every method returns `string` or `int`, types disambiguate nothing. Favour specialised types over "stringly typed" APIs.

### Hierarchy of Communication

Most durable to least:

1. Distinct **types**
2. Helpful **names**
3. Good **comments** (for *why*, not *what*)
4. Automated **tests** as illustrative examples
5. Helpful **commit messages**
6. External **documentation**

Only types are compiler-checked. Code is the only artifact guaranteed to be current.

## Common Misconceptions

- **Myth**: A good API exposes every capability users might want.
  **Reality**: A Swiss Army knife becomes a God Class. Specialised APIs with few, well-typed methods are easier to reason about.

- **Myth**: Comments explain what names cannot.
  **Reality**: Most comments can be replaced by a well-named method. Comments are for *why*, not *what*.

- **Myth**: Returning a value from a method that also mutates state is a convenience.
  **Reality**: It violates CQS and makes the method harder to reason about from the signature alone.

- **Myth**: CQS and CQRS are the same thing.
  **Reality**: CQRS is an architectural style that borrows terminology from CQS but applies it at a different scale.
