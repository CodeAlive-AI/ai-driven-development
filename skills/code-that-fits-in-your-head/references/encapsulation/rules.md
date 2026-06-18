# Encapsulation Rules

Actionable rules for protecting invariants, validating input, and converting DTOs into domain objects.

## Core Rules

### 1. A Domain Object Must Never Exist in an Invalid State

Reduced to its essence, encapsulation guarantees the object can never be in an invalid state. The object — not the caller — is responsible for enforcing this.

- Every constructor must reject inputs that violate invariants.
- Every mutating operation (if any) must preserve invariants.
- Prefer immutability: validity only needs to be established once.

**Example**:
```csharp
// Bad — caller is trusted to pass valid data
public Reservation(DateTime at, string email, string name, int quantity)
{
    At = at; Email = email; Name = name; Quantity = quantity;
}

// Good — constructor enforces the invariant
public Reservation(DateTime at, string email, string name, int quantity)
{
    if (quantity < 1)
        throw new ArgumentOutOfRangeException(
            nameof(quantity),
            "The value must be a positive (non-zero) number.");
    At = at; Email = email; Name = name; Quantity = quantity;
}
```

### 2. Validate at Construction, Not at Each Call Site

If an object has already been validated at construction, downstream code can dispense with defensive coding. Re-checking invariants at every call site is wasted work and an invitation for drift.

- Do not write `if (reservation.Quantity > 0)` in callers — the type already guarantees it.
- The maintenance programmer should not have to do detective work to answer "is `Quantity` a natural number?".

### 3. Parse, Don't Validate

Do not return a Boolean `IsValid`. Return the parsed, typed value — or a null/Maybe indicating failure. A parser consumes less-structured input and produces more-structured output.

- A `Validate()` method on a DTO should return `Reservation?`, not `bool`.
- Only construct the Domain Model once all preconditions are met.
- Callers branch on the return value; they never re-parse.

**Example**:
```csharp
// Bad — Boolean throws away information
internal bool IsValid() { /* ... */ }
// caller must re-parse At, re-check Email, etc.

// Good — parse once, return the typed result
internal Reservation? Validate()
{
    if (!DateTime.TryParse(At, out var d)) return null;
    if (Email is null) return null;
    if (Quantity < 1) return null;
    return new Reservation(d, Email, Name ?? "", Quantity);
}
```

### 4. Apply Postel's Law: Liberal Inputs, Conservative Outputs

Be conservative in what you send, be liberal in what you accept. Accept any input you can meaningfully work with — but no further. As soon as input is unworkable, fail fast.

- Convert a missing `Name` to `""` — you can still fulfil the reservation without it.
- Reject a missing `Email` — you cannot contact the guest without it.
- Reject a non-parseable `At` — there is no meaningful reservation without a date.

### 5. Throw `ArgumentNullException`, Not `NullReferenceException`

A `NullReferenceException` carries no useful information. An `ArgumentNullException` carries the name of the argument that was null. Write explicit null guards.

**Example**:
```csharp
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null)
        throw new ArgumentNullException(nameof(dto));
    // ...
}
```

### 6. Return 400 Bad Request for Invalid HTTP Input

At an HTTP boundary, invalid input is a client error, not a server error. Don't let an unhandled exception leak out as 500.

- Guard Clauses at the controller return `new BadRequestResult()`.
- Constructor exceptions (e.g. `ArgumentOutOfRangeException`) from the domain object are programming errors — by that point the controller should already have rejected the input.

### 7. Separate DTO from Domain Model

A DTO is the wire format: nullable fields, string dates, untrusted values. A Domain Model is always-valid. Do not reuse the same class for both.

- `ReservationDto` has `string? At`, `string? Email`, `string? Name`, `int Quantity`.
- `Reservation` has `DateTime At`, non-null `Email`, non-null `Name`, positive `Quantity`.
- The only bridge between them is a parse/validate method.

### 8. Drive Invariants with Parametrised Tests

When you need to triangulate a type — "is zero valid? is -1 valid?" — use a parametrised test with several `[InlineData]` cases rather than one test per input. This both documents the invariant and drives the implementation.

**Example**:
```csharp
[Theory]
[InlineData( 0)]
[InlineData(-1)]
public void QuantityMustBePositive(int invalidQantity)
{
    Assert.Throws<ArgumentOutOfRangeException>(
        () => new Reservation(
            new DateTime(2024, 8, 19, 11, 30, 0),
            "mail@example.com",
            "Marie Ilsøe",
            invalidQantity));
}
```

### 9. Move in Small Transformations (TPP)

Don't leap from a hard-coded constant to a fully implemented method. Use the Transformation Priority Premise: move one step at a time — constant→scalar, scalar→array, expression→function. Each step should keep the tests green.

- After each transformation, run the full test suite.
- If a transformation leaves the code broken for more than a few seconds, back out.

## Guidelines

- Prefer a dedicated type (e.g. `NaturalNumber`) over a raw `int` when an invariant applies across many methods.
- If your language lacks nullable reference types, use a `Maybe<T>` / `Option<T>` container instead of `null`.
- Don't assert on exception messages — the message is not part of behaviour; coupling tests to it causes needless churn.
- Follow Red → Green → Refactor: after every green, ask "can I simplify this?".

## Exceptions

When these rules may be relaxed:

- **Legacy boundaries**: When wrapping a legacy API that already returns half-validated data, a transitional adapter with looser invariants may be justified.
- **Internal-only types**: If a type is only ever constructed from already-validated data within a single module, its guards can be lighter — but document this.
- **Performance-critical hot paths**: Where measured profiling shows guard clauses dominate, consider moving validation to the boundary only. This is rare.

## Quick Reference

| Rule | Summary |
|------|---------|
| Always Valid | Invalid construction must throw |
| Validate at construction | Callers need not defend |
| Parse, don't validate | Return the typed value, not a Boolean |
| Postel's Law | Accept what you can use; reject the rest |
| ArgumentNullException | Name the null argument |
| 400 on invalid input | Don't leak exceptions as 500 |
| DTO ≠ Domain | Separate wire format from domain model |
| Parametrised tests | Triangulate invariants with `[InlineData]` |
| TPP | Move in small transformations |
