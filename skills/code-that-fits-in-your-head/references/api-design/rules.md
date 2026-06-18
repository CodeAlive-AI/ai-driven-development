# API Design Rules

Actionable rules for designing public APIs that advertise their contracts through types and names.

## Core Rules

### 1. Every Method Is a Command OR a Query — Never Both

Commands have side effects and return `void` (or `Task`). Queries return data and have no observable side effects. A method that does both violates CQS and is harder to reason about.

- A `void` return advertises "this method exists for its side effect"
- A non-`void` return promises "calling this does not change observable state"
- Local state mutation inside the method body is fine if it is not observable to callers

**Example**:
```csharp
// Bad — mutates AND returns (neither Command nor Query)
public int AddItemAndReturnTotal(Item item) { ... }

// Good — split into a Command and a Query
public void AddItem(Item item) { ... }
public int Total { get; }
```

### 2. Prefer Queries Over Commands

Queries are easier to reason about because both their input and output types hint at their intent. Commands communicate only through their input types and name.

### 3. Make Illegal States Unrepresentable (Poka-Yoke)

Design APIs so that invalid inputs or states cannot be expressed in code. Use custom types, non-nullable references, and required constructor parameters instead of runtime validation.

- Use specialized types (`TimeOfDay`, `Reservation`) instead of primitives
- Make all constructor parameters required; reject `null`
- Prefer compile-time errors to runtime exceptions

**Example**:
```csharp
// Bad — caller can pass any int, including invalid hours
public Reservation(int hour, int minute, string email) { ... }

// Good — TimeOfDay and Email types constrain valid values
public Reservation(TimeOfDay at, Email email) { ... }
```

### 4. Advertise Contracts With Types, Not Just Names

If the return type is `Task<Reservation?>`, the `?` tells the reader nullability is possible without needing a `GetReservationOrNull` name. Use the type system to carry semantic information so renaming the method later does not lie.

### 5. Favor Well-Named Methods Over Comments

If a comment explains *what* code does, extract the code into a method whose name says it. Reserve comments for *why* — reasons a future reader could not infer from the code.

**Example**:
```csharp
// Bad
// Reject reservation if it's outside of opening hours
if (candidate.At.TimeOfDay < OpensAt ||
    LastSeating < candidate.At.TimeOfDay)
    return false;

// Good
if (IsOutsideOfOpeningHours(candidate))
    return false;
```

### 6. Apply the X-Out Names Exercise

Mentally replace every method name with `Xxx`. If the types alone still make it obvious what each method does, your types are doing their job. If not, either introduce distinct types or accept that you lean heavily on names.

- Works best when the class exposes only a few methods, each with distinct types
- Fails for "stringly typed" APIs where every signature looks the same
- A reason to keep classes focused rather than growing into God Classes

### 7. Respect the Hierarchy of Communication

Distill intent in this order, using the next mechanism only when the prior one cannot express the idea:

1. **Types** — checked by the compiler; never stale
2. **Method names** — read on every use
3. **Comments** — for reasons and caveats
4. **Automated tests** — executable illustrative examples
5. **Commit messages** — context for a particular change
6. **External docs** — high-level setup and mission

### 8. Design for the Reader, Not the Writer

Code is read more than it is written. The reader may be you in six months with none of the context. Optimize every name, type, and signature for understanding at reading time, not typing speed.

### 9. Avoid Swiss Army Knives

An API with dozens of methods in a single class (a God Class) makes reasoning impossible. Split capabilities into focused, specialized types so that each afforded operation has a distinct signature.

## Guidelines

- Prefer non-nullable reference types; use `?` only when `null` is genuinely a valid value
- Use an IDE's method-signature tooltip to evaluate whether a constructor is self-explanatory
- When in doubt, write a test that tries to misuse the API — if it is too easy, tighten the types
- If a class owns configuration, pass the whole class as a dependency rather than exploding its fields

## Exceptions

- **Legacy databases or transports**: You may have to return generated IDs from an insert. This is solvable within CQS but sometimes framework constraints force pragmatic violations.
- **Cross-boundary DTOs**: Configuration objects populated from JSON or environment files often have anemic encapsulation by necessity.
- **Performance-critical paths**: Occasionally a combined Command+Query is justified; document the why and isolate it.

## Quick Reference

| Rule | Summary |
|------|---------|
| CQS | Command (void) or Query (returns data), never both |
| Poka-yoke | Make invalid states fail to compile |
| Hierarchy | Types > names > comments > tests > commits > docs |
| X-Out | Blank every name — if still readable, names underused |
| No Swiss Army | Favor specialized APIs over God Classes |
| Write for readers | Optimize for reading, not writing |
