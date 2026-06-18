# Separation of Concerns Patterns

Reusable patterns for layering cross-cutting concerns onto domain code and for deciding what to log.

## Pattern: Decorator

### Intent

Add a cross-cutting concern (logging, caching, retries, auditing, metering) to an existing implementation without modifying it. The Decorator shares the interface of the wrapped object so it can be dropped in transparently.

### When to Use

- You need logging, caching, fault tolerance, or auditing on an existing service.
- The concern applies to many features behind the same interface.
- You want the core implementation to stay focused on the domain.
- You want to swap the concern on or off via DI registration.

### Structure

```csharp
public interface IService
{
    Task<Result> DoWork(Input input);
}

public sealed class RealService : IService
{
    public Task<Result> DoWork(Input input) { /* actual work */ }
}

public sealed class ConcernDecorator : IService
{
    private readonly IService inner;

    public ConcernDecorator(IService inner) { this.inner = inner; }

    public async Task<Result> DoWork(Input input)
    {
        // before: set up, measure, check cache, etc.
        var result = await inner.DoWork(input).ConfigureAwait(false);
        // after: log, cache, retry, etc.
        return result;
    }
}
```

### Example: Logging Decorator around a repository

Step 1 — the interface that all implementations share:

```csharp
public interface IReservationsRepository
{
    Task Create(int restaurantId, Reservation reservation);
    Task<IReadOnlyCollection<Reservation>> ReadReservations(
        int restaurantId, DateTime min, DateTime max);
    Task<Reservation?> ReadReservation(Guid id);
    Task Update(Reservation reservation);
    Task Delete(Guid id);
}
```

Step 2 — the real implementation (`SqlReservationsRepository`) talks to SQL Server and knows nothing about logging. It stays untouched.

Step 3 — the Decorator adds logging around every call:

```csharp
public sealed class LoggingReservationsRepository : IReservationsRepository
{
    public LoggingReservationsRepository(
        ILogger<LoggingReservationsRepository> logger,
        IReservationsRepository inner)
    {
        Logger = logger;
        Inner = inner;
    }

    public ILogger<LoggingReservationsRepository> Logger { get; }
    public IReservationsRepository Inner { get; }

    public async Task<Reservation?> ReadReservation(Guid id)
    {
        var output = await Inner.ReadReservation(id).ConfigureAwait(false);
        Logger.LogInformation(
            "{method}(id: {id}) => {output}",
            nameof(ReadReservation),
            id,
            JsonSerializer.Serialize(output?.ToDto()));
        return output;
    }

    // The other methods follow the same shape: call Inner, log, return.
}
```

Step 4 — compose at the DI registration, so the rest of the app sees only `IReservationsRepository`:

```csharp
var connStr = Configuration.GetConnectionString("Restaurant");
services.AddSingleton<IReservationsRepository>(sp =>
{
    var logger =
        sp.GetService<ILogger<LoggingReservationsRepository>>();
    return new LoggingReservationsRepository(
        logger,
        new SqlReservationsRepository(connStr));
});
```

A sample structured log entry (formatted for readability):

```
2020-11-12 16:48:29.441 +00:00 [Information] LoggingReservationsRepository:
ReadReservation(id: 55a1957b-f85e-41a0-9f1f-6b052f8dcafd) =>
{"Id":"55a1957b...","At":"2021-05-14T20:30:00","Email":"...","Quantity":5}
```

### Benefits

- Core class stays focused on its real job.
- Decorators stack: caching around logging around retry around the real service.
- Turning a concern on or off is a one-line DI change.
- Each Decorator is independently testable.

### Considerations

- One Decorator per concern; do not combine logging and caching in one class.
- Some DI containers support Decorators natively; the built-in ASP.NET container does not, so register with a lambda.
- Delegation must be total — every method must call `Inner` unless you deliberately short-circuit (e.g. cache hit).

---

## Pattern: Read-Through Cache Decorator

### Intent

Avoid hitting the real data source when a recent answer is already known. Same Decorator shape as logging — wrap, check, delegate, update.

```csharp
public sealed class CachingRepository : IReservationsRepository
{
    private readonly IMemoryCache cache;
    private readonly IReservationsRepository inner;

    public async Task<Reservation?> ReadReservation(Guid id)
    {
        if (cache.TryGetValue(id, out Reservation? hit))
            return hit;
        var result = await inner.ReadReservation(id).ConfigureAwait(false);
        cache.Set(id, result);
        return result;
    }
}
```

Caveats: also invalidate on writes; staleness window is a product decision.

---

## Pattern: What to Log

### Intent

Decide per call site whether to log, so the log contains just enough to reproduce execution.

### Rules of thumb

- **Log impure actions** (inputs and outputs): DB, HTTP, file I/O, clock, randomness, side effects.
- **Do not log pure calculations** — deterministic, trivially reproducible.
- **Always log failures**: exceptions, non-2xx responses, retries.
- **Redact secrets**: JWTs, passwords, card numbers.

### Example

```csharp
Log.Debug("Adding {x} and {y}.", x, y);   // external input -> log
int z = x + y;                             // pure -> no log
var r = await repo.ReadReservation(id);    // impure -> logged by Decorator
if (!r.IsValid) throw new InvalidReservationException();  // pure -> no log
```

If pure and impure are tangled, you must log everything until you refactor. Favour a functional core with an imperative shell to shrink what you need to log.

---

## Pattern Selection Guide

| Situation | Recommended Pattern |
|-----------|-------------------|
| Need to add logging without touching a service | Logging Decorator |
| Repeated reads of the same data | Read-Through Cache Decorator |
| Flaky downstream call | Circuit Breaker Decorator |
| Must know inputs/outputs of impure action | Log inputs and outputs at the Decorator |
| Pure function, deterministic | Do not log |
| Every feature needs auth | Framework middleware (not a custom Decorator) |
