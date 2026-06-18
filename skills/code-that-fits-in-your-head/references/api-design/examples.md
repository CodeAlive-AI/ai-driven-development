# API Design Examples

Code examples demonstrating API design principles: affordance, poka-yoke, CQS, naming, and the X-Out exercise.

## Bad Examples

### Comment Explaining What the Code Does

```csharp
// Reject reservation if it's outside of opening hours
if (candidate.At.TimeOfDay < OpensAt ||
    LastSeating < candidate.At.TimeOfDay)
    return false;
```

**Problems**:
- The comment and the code can drift out of sync as the code evolves
- The reader must still parse the conditional to verify the comment
- The intent is not extractable — callers cannot reuse the check

### Stringly Typed / X-Out Failure

```csharp
public interface IThings
{
    string DoSomething(string a, string b);
    string GetSomething(string c);
    string MakeSomething(string d, string e);
}
```

**Problems**:
- If you X-out names, every signature looks identical
- `string` carries no domain meaning — any value can be passed
- Nothing prevents callers from swapping arguments by mistake

### CQS Violation

```csharp
// Both mutates state AND returns data
public int AddReservationAndGetCount(Reservation r)
{
    _store.Add(r);
    return _store.Count;
}
```

**Problems**:
- Cannot tell from the signature whether it is "safe" to call
- Mixes a persistence effect with a count query
- Forces callers who want only the count to also persist

### Swiss Army Knife Constructor

```csharp
public ReservationsController(
    IReservationsRepository repository,
    TimeOfDay opensAt,
    TimeOfDay lastSeating,
    TimeSpan seatingDuration,
    IEnumerable<Table> tables)
{
    Repository = repository;
    MaitreD = new MaitreD(opensAt, lastSeating, seatingDuration, tables);
}
```

**Problems**:
- Controller now knows MaitreD's constructor shape; any change ripples
- Configuration concerns leak into a class that should handle HTTP
- No single type represents "restaurant policy"

## Good Examples

### MaitreD as Affordance

```csharp
public MaitreD(
    TimeOfDay opensAt,
    TimeOfDay lastSeating,
    TimeSpan seatingDuration,
    IEnumerable<Table> tables)

public bool WillAccept(
    DateTime now,
    IEnumerable<Reservation> existingReservations,
    Reservation candidate)
```

**Why it works**:
- Custom `TimeOfDay`, `Reservation`, and `Table` types carry domain meaning (ubiquitous language — "maitre d'" is what a domain expert would say)
- Constructor demands everything needed up front; none can be `null`
- `WillAccept` returns `bool`, so by CQS it has no side effects — safe to call
- X-Out Names: even with names replaced, the types clearly describe a policy constructor and a decision query

### Well-Named Method Replacing a Comment

```csharp
// Before (comment doing the communication)
// Reject reservation if it's outside of opening hours
if (candidate.At.TimeOfDay < OpensAt ||
    LastSeating < candidate.At.TimeOfDay)
    return false;

// After (method name doing the communication)
if (IsOutsideOfOpeningHours(candidate))
    return false;
```

**Why it works**:
- The name is checked by the compiler whenever the method is renamed
- Intent is reusable — other branches can call `IsOutsideOfOpeningHours`
- Reader does not need to parse the conditional to confirm the intent

### Query With No Observable Side Effects (CQS)

```csharp
private IEnumerable<Table> Allocate(
    IEnumerable<Reservation> reservations)
{
    List<Table> availableTables = Tables.ToList();
    foreach (var r in reservations)
    {
        var table = availableTables.Find(t => t.Fits(r.Quantity));
        if (table is { })
        {
            availableTables.Remove(table);
            if (table.IsCommunal)
                availableTables.Add(table.Reserve(r.Quantity));
        }
    }
    return availableTables;
}
```

**Why it works**:
- Mutates only a local `List<Table>` — not observable to the caller
- Returns `IEnumerable<Table>`, signalling "this is a Query"
- Caller can rely on the signature alone; no need to read the body

### Nullability Expressed in the Type (Poka-Yoke + Hierarchy)

```csharp
public interface IReservationsRepository
{
    Task Create(Reservation reservation);
    Task<IReadOnlyCollection<Reservation>> ReadReservations(DateTime dateTime);
    Task<Reservation?> ReadReservation(Guid id);
}
```

**Why it works**:
- The `?` on `Reservation?` tells callers they must handle `null`
- No need for a `GetReservationOrNull` suffix that could rot
- Applying X-Out Names still leaves each method distinguishable — `Task` vs `Task<IReadOnlyCollection<Reservation>>` vs `Task<Reservation?>` signal Command, list-Query, and lookup-Query respectively

### Dependency as a Whole Object (Poka-Yoke at the Seam)

```csharp
public ReservationsController(
    IReservationsRepository repository,
    MaitreD maitreD)
{
    Repository = repository;
    MaitreD = maitreD;
}

public IReservationsRepository Repository { get; }
public MaitreD MaitreD { get; }
```

**Why it works**:
- Controller depends on `MaitreD`, not on its parts
- Changes to `MaitreD`'s constructor do not ripple into the controller
- `MaitreD` is immutable, so it is safe to register as a Singleton
- The composition root (Startup) is the only place that knows the raw configuration values

## Refactoring Walkthrough

### Before

Business logic hard-coded in the controller:

```csharp
int reservedSeats = reservations.Sum(r => r.Quantity);
if (10 < reservedSeats + r.Quantity)
    // reject...
```

### After

The decision is delegated to a domain object with a well-designed API:

```csharp
if (!MaitreD.WillAccept(DateTime.Now, reservations, r))
    // reject...
```

### Changes Made

1. **Extracted a domain class** (`MaitreD`) named in the ubiquitous language so that domain experts and code agree on vocabulary.
2. **Replaced a magic number (10) with a typed collection** (`IEnumerable<Table>`) passed to the constructor — this makes per-restaurant configuration expressible and invalid capacities unrepresentable.
3. **Named the decision method `WillAccept`** so that the call site reads like business intent. Returning `bool` makes it a Query; by CQS the caller knows no state is mutated.
4. **Moved side-effect-free allocation to a private Query** (`Allocate`) that returns an `IEnumerable<Table>`, keeping the public API small and the X-Out exercise viable.
5. **Injected `MaitreD` via the constructor** rather than reconstructing it from exploded config on every request — reducing coupling between the controller and MaitreD's shape.
