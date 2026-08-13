# Encapsulation Knowledge

Core concepts for protecting objects from ever existing in an invalid state.

## Overview

Encapsulation is not merely private fields behind getters and setters. The real idea is that an object guarantees it will never be in an invalid state, and the interaction between object and caller obeys a contract of pre- and postconditions.

## Key Concepts

### Encapsulation as Contract

Interact with an object without intimate knowledge of its implementation, via preconditions (caller's responsibilities) and postconditions (object's guarantees). Together they form invariants. This lets you refactor without breaking callers and replace many implementation details with a simpler contract that fits in short-term memory.

### Always-Valid and Protection of Invariants

Reduced to its essence: an object can never be in an invalid state. If initialisation succeeds, the object is valid — downstream code dispenses with defensive re-checks. Immutable objects are attractive because validity is established once, in the constructor. Every mutating operation must preserve validity.

### DTO vs Domain Model

A Data Transfer Object carries input across a boundary with nullable, unvalidated fields. A Domain Model object is always-valid and encodes business rules in its types. The DTO's purpose ends the moment it has been parsed into a Domain Model.

### Parse, Don't Validate

Instead of an `IsValid` Boolean, a parser consumes less-structured input and produces more-structured output (or failure). Validation alone discards information: the caller is told "yes" and must re-parse. A parser projects into a stronger representation that carries validity forward.

### Explicit Boundary Compatibility (Postel's Law reframed)

Compatibility is a deliberate, tested contract decision — not an unconditional virtue of "liberal acceptance". Parse untrusted input into an explicit supported form; accept only the shapes the public contract defines; reject the rest. Do not silently coerce malformed or invented shapes merely to be "liberal".

### Natural Numbers as Type-Level Constraints

Use the type system or constructor guards to express natural numbers, non-null strings, valid dates — not just any `int` or `string`. Signed ints allow zero and negatives; for a reservation quantity, neither is correct.

## Terminology

| Term | Definition |
|------|------------|
| Invariant | Condition that is always true for a valid object |
| Precondition / Postcondition | Caller obligation / object guarantee |
| Guard Clause | Early check that rejects invalid input |
| DTO | Nullable, unvalidated wire format |
| Domain Model | Object that encodes business rules in its type |
| Postel's Law (reframed) | Accept only deliberate, tested compatibility; reject malformed input |

## Common Misconceptions

- **Myth**: Encapsulation means private fields with getters and setters.
  **Reality**: That is access control. Encapsulation is protection of invariants.

- **Myth**: The caller is responsible for making sure the data is valid before handing it to a domain object.
  **Reality**: The object knows best what "valid" means; it should reject invalid input itself.

- **Myth**: A `ReservationDto` and a `Reservation` can be the same class.
  **Reality**: The DTO is a wire format with nullable fields; the domain object is always-valid.

- **Myth**: Throwing `NullReferenceException` is fine — it's still an exception.
  **Reality**: `ArgumentNullException` names the argument; `NullReferenceException` carries nothing useful.
