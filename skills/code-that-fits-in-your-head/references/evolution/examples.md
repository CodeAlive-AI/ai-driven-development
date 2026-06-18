# Evolution Examples

Concrete C# examples from the restaurant reservation code base showing feature flags and the Strangler pattern in action.

## Example 1: Calendar Feature Flag

A calendar feature that took roughly two months of elapsed work. Merged to master continuously throughout, without exposing incomplete behaviour in production.

### Before (no calendar)

```csharp
public IActionResult Get()
{
    return Ok(new HomeDto { Links = new[]
    {
        CreateReservationsLink()
    } });
}
```

The `home` resource returns just the reservations link.

### With Feature Flag

```csharp
public IActionResult Get()
{
    var links = new List<LinkDto>();
    links.Add(CreateReservationsLink());
    if (enableCalendar)
    {
        links.Add(CreateYearLink());
        links.Add(CreateMonthLink());
        links.Add(CreateDayLink());
    }
    return Ok(new HomeDto { Links = links.ToArray() });
}
```

### Wiring the Flag

The flag is wrapped in a class because the built-in ASP.NET DI container won't inject primitive values. Configuration reads it with a default of `false`:

```csharp
public HomeController(CalendarFlag calendarFlag)
{
    if (calendarFlag is null)
        throw new ArgumentNullException(nameof(calendarFlag));
    enableCalendar = calendarFlag.Enabled;
}

// Startup:
var calendarEnabled = new CalendarFlag(
    Configuration.GetValue<bool>("EnableCalendar"));
services.AddSingleton(calendarEnabled);
```

### Flipping the Flag in Tests

```csharp
protected override void ConfigureWebHost(IWebHostBuilder builder)
{
    if (builder is null)
        throw new ArgumentNullException(nameof(builder));

    builder.ConfigureServices(services =>
    {
        services.RemoveAll<IReservationsRepository>();
        services.AddSingleton<IReservationsRepository>(
            new FakeDatabase());
        services.RemoveAll<CalendarFlag>();
        services.AddSingleton(new CalendarFlag(true));
    });
}
```

### After the Release

Once the feature was live, the author deleted the `CalendarFlag` class. Every reference failed to compile. He then "leaned on the compiler" to simplify every `if (enableCalendar)` into just the true branch. Final result: no flag, no conditional, all cleaned up.

**Why it works**:
- Production stayed unaffected because the config value was never set in production — defaults to `false`.
- Integration tests still drove the new behaviour.
- Every commit during the weeks of work was deployable.
- The cleanup at the end was mechanical (compiler-guided).

---

## Example 2: Method-Level Strangler — `ReadReservations`

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

## Example 3: Class-Level Strangler — `Occurrence<T>` to `TimeSlot`

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

Each caller was migrated in its own commit. When all callers used `Schedule` / `TimeSlot`:

1. `ScheduleOcc` was deleted.
2. The `ToTimeSlot` conversion helper was deleted.
3. The `Occurrence<T>` class was deleted.

Throughout the whole process the author was *"never more than five minutes from being able to do a commit, and all commits left the system in a consistent state that could be integrated and deployed."*

**Why it works**:
- The new class ships first, standalone, with no behaviour change.
- The temporary conversion helper contains the bridge to a single place that is trivial to delete later.
- The rename (`ScheduleOcc`) is explicit scaffolding, clearly short-lived.
- Every intermediate state is mergeable.
