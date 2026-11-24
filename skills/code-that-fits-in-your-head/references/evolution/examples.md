# Evolution Examples

Concrete C# examples from the restaurant reservation code base showing the Strangler pattern at method and class level.

## Example 1: Method-Level Strangler — `ReadReservations`

The existing repository interface only supported reading a single date. A new calendar feature needed a date range.

### Before

```csharp
public interface IReservationsRepository
{
    Task Create(Reservation reservation);
    Task<IReadOnlyCollection<Reservation>> ReadReservations(
        DateTime dateTime);
    Task<Reservation?> ReadReservation(Guid id);
    Task Update(Reservation reservation);
    Task Delete(Guid id);
}
```

### Step 1: Add the New Overload

```csharp
public interface IReservationsRepository
{
    Task Create(Reservation reservation);
    Task<IReadOnlyCollection<Reservation>> ReadReservations(
        DateTime dateTime);
    Task<IReadOnlyCollection<Reservation>> ReadReservations(
        DateTime min, DateTime max);        // new
    Task<Reservation?> ReadReservation(Guid id);
    Task Update(Reservation reservation);
    Task Delete(Guid id);
}
```

Both implementers (`SqlReservationsRepository` and `FakeDatabase`) got the new method in the same commit so the build stayed green. About 5-10 minutes of work.

### Step 2: Migrate Callers One at a Time

```csharp
var min = res.At.Date;
var max = min.AddDays(1).AddTicks(-1);
var reservations = await Repository
    .ReadReservations(min, max)
    .ConfigureAwait(false);
```

Each call site was edited in its own commit. At every point, the tree was mergeable.

### Step 3: Delete the Old Method

```csharp
public interface IReservationsRepository
{
    Task Create(Reservation reservation);
    Task<IReadOnlyCollection<Reservation>> ReadReservations(
        DateTime min, DateTime max);
    Task<Reservation?> ReadReservation(Guid id);
    Task Update(Reservation reservation);
    Task Delete(Guid id);
}
```

The single-date `ReadReservations` was removed from the interface and from every implementer.

**Why it works**:
- The new signature *weakened* preconditions (a single date is just a range of length 1), so the new method could subsume the old.
- The compiler caught every unmigrated call site.
- Each commit was deployable; the work could be paused and resumed.

---

## Example 2: Class-Level Strangler — `Occurrence<T>` to `TimeSlot`

A generic `Occurrence<T>` class had been over-engineered. All real uses associated a `DateTime` with a collection of tables, so a concrete `TimeSlot` class would be clearer.

### Before: the over-abstract generic

```csharp
public class Occurrence<T>
{
    public Occurrence(DateTime at, T value)
    {
        At = at;
        Value = value;
    }
    public DateTime At { get; }
    public T Value { get; }
}

// A method signature full of nested generics:
public IEnumerable<Occurrence<IEnumerable<Table>>> Schedule(
    IEnumerable<Reservation> reservations)
```

### Step 1: Introduce `TimeSlot` Beside `Occurrence<T>`

```csharp
public class TimeSlot
{
    public TimeSlot(DateTime at, IReadOnlyCollection<Table> tables)
    {
        At = at;
        Tables = tables;
    }
    public DateTime At { get; }
    public IReadOnlyCollection<Table> Tables { get; }
}
```

Commit and merge — no behaviour change.

### Step 2: Add a Temporary Bridge

```csharp
internal static TimeSlot ToTimeSlot(
    this Occurrence<IEnumerable<Table>> source)
{
    return new TimeSlot(source.At, source.Value.ToList());
}
```

### Step 3: Work Around Return-Type Overloading

C# doesn't allow two methods that differ only by return type. The author renamed the old `Schedule` to `ScheduleOcc`, then created a new `Schedule` with the better return type:

```csharp
// Temporary rename of the old method:
public IEnumerable<Occurrence<IEnumerable<Table>>> ScheduleOcc(
    IEnumerable<Reservation> reservations) { /* ... */ }

// New method with the original name and a concrete return type:
public IEnumerable<TimeSlot> Schedule(
    IEnumerable<Reservation> reservations) { /* ... */ }
```

Helper-method signatures were migrated too:

```csharp
// Before
private TimeDto MakeEntry(Occurrence<IEnumerable<Table>> occurrence)

// After
private static TimeDto MakeEntry(TimeSlot timeSlot)
```

### Step 4: Migrate Callers, Then Delete the Old Class

Callers were migrated through coherent, verified checkpoints. When all callers used `Schedule` / `TimeSlot`:

1. `ScheduleOcc` was deleted.
2. The `ToTimeSlot` conversion helper was deleted.
3. The `Occurrence<T>` class was deleted.

Throughout the process, every meaningful checkpoint left the system in a consistent state that could be verified, integrated, and deployed.

**Why it works**:
- The new class ships first, standalone, with no behaviour change.
- The temporary conversion helper contains the bridge to a single place that is trivial to delete later.
- The rename (`ScheduleOcc`) is explicit scaffolding, clearly short-lived.
- Every intermediate state is mergeable.
