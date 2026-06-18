# Encapsulation Knowledge

Core concepts for protecting objects from ever existing in an invalid state.

## Overview

Encapsulation is one of the most misunderstood concepts of object-oriented programming. Many programmers believe it is merely a prohibition against exposing class fields directly — that fields should be hidden behind getters and setters. That has little to do with encapsulation. The real idea is that an object guarantees it will never be in an invalid state, and the interaction between object and caller obeys a contract of pre- and postconditions.

## Key Concepts

### Encapsulation as Contract

**Definition**: Encapsulation is the idea that you can interact with an object without intimate knowledge of its implementation details, via a contract of pre- and postconditions.

Preconditions describe the caller's responsibilities. Postconditions describe the guarantees given by the object. Together they form invariants. This serves two purposes:

- It lets you change the implementation (refactor) without breaking callers.
- It lets you think about the object abstractly — replacing many implementation details with a simpler contract that fits in short-term memory.

### Protection of Invariants

**Definition**: Reduced to its essence, encapsulation guarantees that an object can never be in an invalid state.

There are two dimensions: validity and state. The state of an object is the combination of its constituent values; that combination must always be valid. If an object supports mutation, every state-changing operation must preserve validity. Immutable objects are attractive precisely because you only have to establish validity once — in the constructor.

### DTO vs Domain Model

**Definition**: A Data Transfer Object carries input across a boundary with nullable, unvalidated fields. A Domain Model object is always-valid and encodes business rules in its types.

A `ReservationDto` has nullable strings for `At`, `Email`, `Name` — anything the wire might carry. A `Reservation` domain object accepts a non-nullable `DateTime`, non-null strings, and a positive `int` for quantity. The DTO's purpose ends the moment it has been parsed into a Domain Model.

### Always-Valid Principle

**Definition**: A domain object should be impossible to construct in an invalid state.

If initialisation succeeds, the object is valid. Downstream code that receives such an object can dispense with defensive coding: `At`, `Email`, `Name`, and `Quantity` are guaranteed populated and within range. The knowledge of validity is preserved in the type rather than being rechecked at every call site.

### Natural Numbers as Type-Level Constraints

**Definition**: Use the type system (or constructor guards) to express that a value must be a natural number, a non-null string, a valid date — not just any int or string.

Built-in integer types are signed and allow zero. Unsigned integers still allow zero. For a reservation quantity, neither is correct: zero people and negative people are both invalid. A Guard Clause in the constructor rejects them with `ArgumentOutOfRangeException`. When evolving a Domain Model to describe the real world, natural numbers abound.

### Parse, Don't Validate

**Definition**: Instead of an `IsValid` Boolean method, a parser consumes less-structured input and produces more-structured output, returning the typed value (or `null`/`Maybe`) once.

> "A parser is just a function that consumes less-structured input and produces more-structured output. By its very nature, a parser is a partial function — some values in the domain do not correspond to any value in the range — so all parsers must have some notion of failure." — Alexis King

Validation alone discards information: the caller is told "yes it's valid" and then must re-parse. A parser projects the input into a stronger representation of the same data, and that representation carries the validity forward.

## Terminology

| Term | Definition |
|------|------------|
| Invariant | A condition that is always true for a valid object |
| Precondition | Obligation on the caller before invocation |
| Postcondition | Guarantee the object gives after invocation |
| Guard Clause | Early check at the top of a method that rejects invalid input |
| DTO | Data Transfer Object: nullable, unvalidated wire format |
| Domain Model | Object that encodes business rules and invariants in its type |
| Maybe / Option | Container type expressing presence or absence, used when null is disallowed |
| Postel's Law | Be conservative in what you send, liberal in what you accept |

## How It Relates To

- **Validation**: Validation is the red/green driver that discovers which invariants matter; encapsulation is where those invariants live once discovered.
- **Immutability**: Immutable objects make always-valid trivial — you only check in the constructor.
- **Static type system**: C#'s nullable reference types, non-nullable fields, and custom types carry invariants that the compiler enforces.
- **Decomposition (§7.2.5)**: Parse-don't-validate is the decomposition technique that turns a DTO into a domain object cleanly.

## Common Misconceptions

- **Myth**: Encapsulation means private fields with getters and setters.
  **Reality**: That is access control. Encapsulation is protection of invariants.

- **Myth**: The caller is responsible for making sure the data is valid before handing it to a domain object.
  **Reality**: The object knows best what "valid" means; it should reject invalid input itself.

- **Myth**: A `ReservationDto` and a `Reservation` can be the same class.
  **Reality**: The DTO is a wire format with nullable fields; the domain object is always-valid. Conflating them loses the validity guarantee.

- **Myth**: Throwing `NullReferenceException` is fine — it's still an exception.
  **Reality**: `ArgumentNullException` carries the name of the argument; `NullReferenceException` carries nothing useful. Guard explicitly.

## Quick Reference

| Concept | One-Line Summary |
|---------|-----------------|
| Encapsulation | An object can never be in an invalid state |
| Always-Valid | If the constructor succeeds, the object is valid |
| DTO → Domain | Parse the wire format into a typed, validated object once |
| Parse, don't validate | Return the typed result, not a Boolean |
| Postel's Law | Liberal inputs, conservative outputs |
| Natural Number | Use a Guard Clause or dedicated type; signed ints allow zero and negatives |
