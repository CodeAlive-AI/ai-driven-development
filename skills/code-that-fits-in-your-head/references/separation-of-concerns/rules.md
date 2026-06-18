# Separation of Concerns Rules

Actionable rules for adding cross-cutting concerns cleanly and for deciding when performance is actually worth your time.

## Core Rules

### 1. Use a Decorator for cross-cutting concerns

Do not edit the real implementation to add logging, caching, auditing, or retries. Wrap it with a Decorator that implements the same interface.

- Decorator implements the interface fully.
- Decorator holds an `Inner` reference to the wrapped instance.
- Each method delegates to `Inner` and adds its own behaviour around the call.

**Example**:
```csharp
// Bad: logging mixed into the SQL repository itself
public sealed class SqlReservationsRepository : IReservationsRepository
{
    public async Task<Reservation?> ReadReservation(Guid id)
    {
        logger.LogInformation("Reading {id}", id);
        // ... SQL code ...
        logger.LogInformation("Got {output}", output);
        return output;
    }
}

// Good: a separate Decorator carries the logging concern
public sealed class LoggingReservationsRepository : IReservationsRepository
{
    public LoggingReservationsRepository(
        ILogger<LoggingReservationsRepository> logger,
        IReservationsRepository inner) { /* ... */ }

    public async Task<Reservation?> ReadReservation(Guid id)
    {
        var output = await Inner.ReadReservation(id).ConfigureAwait(false);
        Logger.LogInformation(
            "{method}(id: {id}) => {output}",
            nameof(ReadReservation), id,
            JsonSerializer.Serialize(output?.ToDto()));
        return output;
    }
}
```

### 2. Log what you cannot reproduce

Log every impure action: wall clock reads, random numbers, file or database I/O, web-service calls, anything with side effects, and any failure. Do not log pure calculations — given the inputs, you can recompute the output.

- Impure action -> log inputs and outputs.
- Pure function -> do not log; it is reproducible.
- If the code does not separate pure from impure, you must log everything.

**Example**:
```csharp
// Bad: logging the result of a pure addition
Log.Debug($"Adding {x} and {y}.");
int z = x + y;
Log.Debug($"Result of addition: {z}");  // redundant; deterministic

// Good: log only the impure call
var reservation = await repo.ReadReservation(id);  // impure -> log it
var total = reservation.Quantity + extraSeats;     // pure -> do not log
```

### 3. Do not double-log application-level events

If your framework already logs HTTP requests and responses, do not log the same command again from inside the handler. Logs should cover the data exactly once at the most useful level.

- Web server log captures the inbound request -> do not re-log the payload.
- Repository Decorator logs the DB call -> do not also log it from the domain service.

### 4. Log unhandled exceptions; treat each as a defect

The ideal number of unhandled exceptions in the log is zero. ASP.NET (and most web frameworks) log these automatically, so you rarely need custom code for this. When one appears, fix the root cause rather than silencing the log.

### 5. Use structured logging

Pass named fields to the logger instead of interpolating them into a message string. Structured backends can filter and aggregate on those fields.

**Example**:
```csharp
// Bad: unstructured, only grep can find things
Log.Information($"ReadReservation({id}) => {JsonSerializer.Serialize(output)}");

// Good: named placeholders, queryable
Logger.LogInformation(
    "{method}(id: {id}) => {output}",
    nameof(ReadReservation), id,
    JsonSerializer.Serialize(output?.ToDto()));
```

### 6. Prefer legibility over micro-optimisation

Readable code is the default. Do not sacrifice clarity for a few nanoseconds. If you think code is too slow, measure first; you cannot reason about performance.

- Modern compilers inline, reorder, and vectorise — your mental model is likely wrong.
- Performance depends on hardware, OS, and concurrent load.
- A 100-nanosecond saving is irrelevant next to a millisecond-scale database call.

### 7. Only optimise proven bottlenecks

Correctness first, then (if required by stakeholders) performance. Even then, only optimise where measurement points — typically a hot loop or a latency-critical endpoint.

- Make it work.
- Ask stakeholders whether performance or security matters more.
- If performance wins, profile and optimise the bottleneck, not the method next to it.

## Guidelines

- Redact sensitive fields before logging (JWTs, passwords, card numbers).
- One Decorator, one concern. Do not stack logging + caching + retries into one class.
- Put Decorator wiring in composition root (DI registration), not in the domain.
- When the framework offers a built-in cross-cutting feature (e.g. authentication middleware), prefer it over a home-grown Decorator.

## Exceptions

- **Legacy code with intertwined pure/impure logic**: You may have to log everything until the code is refactored.
- **Tight inner loops with measured bottlenecks**: Profile-backed micro-optimisation is legitimate here, but comment the "why" and keep the unoptimised version nearby.
- **Framework-level cross-cutting concerns (security, CORS)**: Built-in middleware is usually better than a custom Decorator.

## Quick Reference

| Rule | Summary |
|------|---------|
| Decorator, not edits | Add concerns by wrapping, never by rewriting the core |
| Log impure actions | Skip pure functions; log I/O, clock, randomness, failures |
| No double-logging | Record each event at one layer only |
| Always log unhandled exceptions | And treat each as a defect to fix |
| Structured logging | Named placeholders, not interpolated strings |
| Legibility over speed | Micro-optimisation is waste without measurement |
| Optimise bottlenecks only | Profile first, fix the slow link, leave the rest alone |
