# Encapsulation Examples

Curated C# examples demonstrating always-valid objects, parse-don't-validate, and DTO-to-domain conversion.

## Bad Examples

### Anemic Domain Model — No Guards in the Constructor

```csharp
public Reservation(DateTime at, string email, string name, int quantity)
{
    At = at;
    Email = email;
    Name = name;
    Quantity = quantity;
}
```

**Problems**:
- A caller can construct `new Reservation(..., quantity: -3)`.
- Downstream code must defensively re-check `Quantity > 0`, `Email != null`, etc.
- The maintenance programmer has no guarantees just by looking at the type.

### Exclamation-Mark Suppression — Compile-Time Error Traded for Runtime Crash

```csharp
var r = new Reservation(
    DateTime.Parse(dto.At!, CultureInfo.InvariantCulture),
    dto.Email!,
    dto.Name!,
    dto.Quantity);
```

**Problems**:
- The `!` operator tells the compiler to stop warning, but it does not make the value non-null.
- If `dto.At` is null at runtime, `DateTime.Parse` throws — a `NullReferenceException` or `ArgumentNullException` becomes a 500 Internal Server Error.
- A compile-time error traded for a runtime exception is a poor trade-off.

### Boolean Validate — Throws Away Parsing Work

```csharp
internal bool IsValid()
{
    if (!DateTime.TryParse(At, out _)) return false;
    if (Email is null) return false;
    if (Quantity < 1) return false;
    return true;
}

// caller
if (!dto.IsValid()) return new BadRequestResult();
var r = new Reservation(
    DateTime.Parse(dto.At!, CultureInfo.InvariantCulture),  // parse AGAIN
    dto.Email!,                                             // suppress AGAIN
    dto.Name ?? "",
    dto.Quantity);
```

**Problems**:
- The parse happens twice — once in `IsValid`, once at construction.
- The compiler still forces `!` suppressions, because the Boolean return type does not carry the null-safety information forward.
- Nothing prevents another caller from skipping `IsValid` entirely.

## Good Examples

### Always-Valid Constructor with Guard Clause

```csharp
public Reservation(
    DateTime at,
    string email,
    string name,
    int quantity)
{
    if (quantity < 1)
        throw new ArgumentOutOfRangeException(
            nameof(quantity),
            "The value must be a positive (non-zero) number.");
    At = at;
    Email = email;
    Name = name;
    Quantity = quantity;
}
```

**Why it works**:
- Impossible to construct a `Reservation` with a non-positive quantity.
- Combined with non-nullable reference types, `At`, `Email`, and `Name` are guaranteed populated too.
- Every downstream method that receives a `Reservation` can dispense with defensive coding.

### Parse, Don't Validate — DTO Returns a Typed Domain Object

```csharp
// On ReservationDto
internal Reservation? Validate()
{
    if (!DateTime.TryParse(At, out var d))
        return null;
    if (Email is null)
        return null;
    if (Quantity < 1)
        return null;
    return new Reservation(d, Email, Name ?? "", Quantity);
}
```

**Why it works**:
- The method signature `Reservation? Validate()` is the abstraction: "does dto represent a valid reservation?".
- Parsing happens exactly once; the typed result carries the validity forward.
- Postel's Law: a null `Name` is liberally converted to `""`; a null `Email` or unparseable `At` is rejected.
- The compiler's nullable-reference-types analyser forces the caller to handle the null case.

### Controller Using the Parsed Domain Object

```csharp
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null)
        throw new ArgumentNullException(nameof(dto));

    Reservation? r = dto.Validate();
    if (r is null)
        return new BadRequestResult();

    var reservations = await Repository
        .ReadReservations(r.At)
        .ConfigureAwait(false);
    int reservedSeats = reservations.Sum(x => x.Quantity);
    if (10 < reservedSeats + r.Quantity)
        return new StatusCodeResult(
            StatusCodes.Status500InternalServerError);

    await Repository.Create(r).ConfigureAwait(false);
    return new NoContentResult();
}
```

**Why it works**:
- No `!` suppressions anywhere — `r.At`, `r.Email`, `r.Quantity` are all typed.
- Cyclomatic complexity is low (4); the method fits in your brain.
- A `null` from `Validate` becomes a 400 Bad Request; a valid `Reservation` flows to the repository.

### Parametrised Test Triangulating the `quantity` Invariant

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

**Why it works**:
- Two `[InlineData]` cases document that zero and negative are both invalid — consensus on "is zero a natural number?" varies, so the test pins the decision.
- Asserts only that *an* `ArgumentOutOfRangeException` is thrown; no brittle coupling to the exception message.
- Drives the constructor's guard clause via Red → Green → Refactor.

## Refactoring Walkthrough

### Before — Controller Carrying All Validation Inline

```csharp
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null)
        throw new ArgumentNullException(nameof(dto));
    if (!DateTime.TryParse(dto.At, out var d))
        return new BadRequestResult();
    if (dto.Email is null)
        return new BadRequestResult();
    if (dto.Quantity < 1)
        return new BadRequestResult();
    var r =
        new Reservation(d, dto.Email, dto.Name ?? "", dto.Quantity);
    await Repository.Create(r).ConfigureAwait(false);
    return new NoContentResult();
}
```

### After — Parse Extracted into DTO, Invariant Moved into Domain Constructor

```csharp
// ReservationDto.cs
internal Reservation? Validate()
{
    if (!DateTime.TryParse(At, out var d)) return null;
    if (Email is null) return null;
    if (Quantity < 1) return null;
    return new Reservation(d, Email, Name ?? "", Quantity);
}

// Reservation.cs
public Reservation(DateTime at, string email, string name, int quantity)
{
    if (quantity < 1)
        throw new ArgumentOutOfRangeException(
            nameof(quantity),
            "The value must be a positive (non-zero) number.");
    At = at; Email = email; Name = name; Quantity = quantity;
}

// ReservationsController.cs
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null)
        throw new ArgumentNullException(nameof(dto));
    Reservation? r = dto.Validate();
    if (r is null)
        return new BadRequestResult();
    await Repository.Create(r).ConfigureAwait(false);
    return new NoContentResult();
}
```

### Changes Made

1. Pulled parsing out of the controller into `ReservationDto.Validate()` — the controller no longer knows about date formats or null-email details.
2. Moved the `quantity < 1` invariant from the controller into the `Reservation` constructor — any future caller (not just this controller) is protected.
3. Changed `Validate` to return `Reservation?` instead of `bool` — parse-don't-validate. Parsing happens once; no `!` suppressions remain.
4. Controller cyclomatic complexity drops from 6 to 4; `Reservation` is now always-valid.
