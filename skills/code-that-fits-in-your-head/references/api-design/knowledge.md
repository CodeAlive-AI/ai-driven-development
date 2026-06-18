# API Design Knowledge

Core concepts and foundational understanding for designing public APIs that fit in readers' heads.

## Overview

An API is an affordance: the set of methods, values, functions, and objects a client has at its disposal to interact with other code. Good API design advertises what is possible, makes what should be impossible hard to even type, and communicates intent primarily through types and names rather than comments or documentation.

## Key Concepts

### Affordance

**Definition**: The relationship between the properties of an object and the capabilities of the agent, which determines how the object could possibly be used.

Borrowed from Donald A. Norman. A chair affords sitting; a door handle affords opening. In code, an API affords its capabilities only to client code that satisfies its preconditions. In statically typed languages, the type system advertises affordances through IDE features like IntelliSense ("dot-driven development").

**Key points**:
- What you cannot express in code is as important as what you can
- Well-encapsulated APIs expose only operations that preserve invariants
- Discoverability comes from types, not documentation

### Poka-Yoke (Mistake-Proofing)

**Definition**: A lean-manufacturing term meaning "mistake-proofing" — designing artifacts so that misuse is difficult or impossible.

Active poka-yoke inspects as artifacts are created (e.g., TDD). Passive poka-yoke builds the constraint into the shape of the thing itself (like USB connectors that only insert one way). In API design, make illegal states unrepresentable so that invalid uses do not even compile. A compiler error gives faster feedback than a runtime exception.

**Key points**:
- Favor compile-time prevention over runtime validation
- Specialised APIs beat Swiss Army knives (God Classes)
- What you *exclude* from the API tells the reader what they should not do

### Command Query Separation (CQS)

**Definition**: Every method is either a Command (has side effects, returns no data — `void`) or a Query (returns data, has no observable side effects) — never both.

Coined by Bertrand Meyer. Not enforced by most compilers; the developer's discipline. Local state changes inside a method that are not observable from outside do not count as side effects. Queries are easier to reason about, so prefer Queries over Commands where possible.

**Key points**:
- A `void` return type means "this exists to have a side effect"
- A non-`void` return type promises "no observable side effect"
- CQS is distinct from CQRS (an architectural style that merely borrows the terminology)

### X-Out Names Exercise

**Definition**: A design exercise where you mentally replace every name in an API with `Xxx` and ask whether the types alone still communicate what each method does.

If three methods on an interface all compile to distinct, unambiguous shapes after blanking out names, your types are pulling their weight. If every method returns `string` or `int`, the types disambiguate nothing and names must do all the work. Favor specialized types over "stringly typed" APIs so that the X-Out exercise still produces a readable API.

### Hierarchy of Communication

**Definition**: An ordering of communication mechanisms by how durable and trustworthy they are, with types at the top and external documentation at the bottom.

Priority order (most to least important):
1. Give APIs distinct **types**
2. Give methods helpful **names**
3. Write good **comments**
4. Provide illustrative examples as automated **tests**
5. Write helpful **commit messages** in Git
6. Write good **documentation**

Only types are checked by the compiler. Everything below types can grow stale. Code is the only artifact guaranteed to be current.

### Write for Readers

**Definition**: Code is read more than it is written; author every line for the human who will read it later (possibly yourself).

The sender-receiver relationship you learned in essay writing still applies. Encapsulation lets the reader ignore implementation details until they need them.

## Terminology

| Term | Definition |
|------|------------|
| Affordance | The capabilities an object offers to an agent given the agent's ability |
| Poka-yoke | Japanese for "mistake-proofing"; design that prevents misuse |
| Command | Method that mutates state and returns nothing (`void`) |
| Query | Method that returns data without observable side effects |
| CQS | Command Query Separation — every method is one or the other |
| Dot-driven development | Using IDE autocompletion on a `.` to discover an API |
| God Class | Antipattern: class with dozens of members and thousands of lines |
| Stringly typed | Antipattern: passing everything as `string` instead of specific types |
| Ubiquitous language | Domain-driven term for shared vocabulary with domain experts |

## How It Relates To

- **Encapsulation**: APIs are the observable surface of encapsulated objects; good encapsulation ensures invariants hold for every afforded operation.
- **Domain-Driven Design**: A ubiquitous language (e.g., `MaitreD` for the head waiter) guides naming of domain objects.
- **Type-Driven Design**: Distinct types for distinct concepts (e.g., `TimeOfDay`, `Reservation`) make the X-Out exercise succeed.
- **Testing**: Automated tests serve as executable illustrative examples in the communication hierarchy.

## Common Misconceptions

- **Myth**: A good API exposes every capability users might want.
  **Reality**: A Swiss Army knife becomes a God Class. Specialized APIs with few, well-typed methods are easier to reason about.

- **Myth**: Comments explain what names cannot.
  **Reality**: Most comments can be replaced by a well-named method. Comments are for *why*, not *what*.

- **Myth**: Returning a value from a method that also mutates state is a convenience.
  **Reality**: It violates CQS and makes the method harder to reason about from the signature alone.

- **Myth**: CQS and CQRS are the same thing.
  **Reality**: CQRS is an architectural style that borrows terminology from CQS but applies it at a different scale.

## Quick Reference

| Concept | One-Line Summary |
|---------|-----------------|
| Affordance | The API shows you what you can do through its types |
| Poka-yoke | Make invalid states fail to compile, not just fail at runtime |
| CQS | Commands return void; Queries have no side effects |
| X-Out Names | If blanking names leaves the API readable, names are underused |
| Hierarchy | Types > names > comments > tests > commits > docs |
