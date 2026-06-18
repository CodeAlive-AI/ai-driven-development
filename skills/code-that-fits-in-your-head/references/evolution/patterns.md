# Evolution Patterns

Reusable patterns for changing live code without breaking callers or stalling integration.

## Pattern: Feature Flag (Calendar Flag Variant)

### Intent

Decouple **deploying** code from **releasing** behaviour. Ship an incomplete feature to production behind a configuration switch that is off by default, and flip it on once the feature is ready.

### When to Use

- The work will take longer than ~4 hours and you want to keep merging to master.
- You practice Continuous Integration or Continuous Deployment and can't justify a long-lived branch.
- You need to exercise the new behaviour with integration tests before it's user-visible.

### Structure

```csharp
// 1. Wrapper class (needed for DI containers that reject raw primitives).
public sealed class CalendarFlag
{
    public CalendarFlag(bool enabled) { Enabled = enabled; }
    public bool Enabled { get; }
}

// 2. Config reads the flag; defaults to false if absent.
var calendarEnabled = new CalendarFlag(
    Configuration.GetValue<bool>("EnableCalendar"));
services.AddSingleton(calendarEnabled);

// 3. Code paths gate the new behaviour on the flag.
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

// 4. Tests override the config to turn the feature on.
services.RemoveAll<CalendarFlag>();
services.AddSingleton(new CalendarFlag(true));
```

### Walkthrough

1. Introduce the flag class or config key with a default of "feature off" in production.
2. Wrap new code paths in `if (flag) { ... }`; the rest of the app stays oblivious.
3. Override the flag to `true` in integration tests and in your local/dev config.
4. When the feature is live in production, delete the flag class. The compiler will catch every `if` to simplify; keep only the new branch.

### Benefits

- Keeps CI healthy on multi-week work.
- Decouples deploy from release — code can ship before the feature is announced.
- Integration tests stay meaningful throughout.

### Considerations

- A flag left in place past its useful life becomes a smell. Delete promptly.
- Don't use flags for rollback — that's a deployment concern.
- Very short features (<4 hours) don't need flags.

---

## Pattern: Method-Level Strangler

### Intent

Replace a method (often an interface method) when in-place editing would break too many call sites at once. Let the old and new methods coexist, migrate callers gradually, then delete the old method.

### When to Use

- A method signature needs to change (e.g. wider preconditions, different return type).
- The method is called from many places and you can't fix them all in one commit.
- You want every intermediate commit to be deployable.

### Structure

```csharp
// Step 1. Start state.
public interface IReservationsRepository {
    Task<IReadOnlyCollection<Reservation>> ReadReservations(DateTime dateTime);
    // ...
}

// Step 2. Add the new method beside the old. Implement on every concrete
//         class in the same commit so the build stays green.
public interface IReservationsRepository {
    Task<IReadOnlyCollection<Reservation>> ReadReservations(DateTime dateTime);
    Task<IReadOnlyCollection<Reservation>> ReadReservations(
        DateTime min, DateTime max);      // new
    // ...
}

// Step 3. Migrate callers one at a time; commit after each.
var reservations = await Repository
    .ReadReservations(min, max)           // now using the new overload
    .ConfigureAwait(false);

// Step 4. When no callers remain, delete the old method from the
//         interface and every implementer.
```

### Walkthrough

1. Add the new method to the interface and implement it in every concrete class. Options: full implementation everywhere in one commit; `NotImplementedException` stubs then TDD; or concrete classes first, interface last.
2. With the new method unused, commit and merge.
3. Edit call sites one at a time; commit per call site.
4. When the old method has no callers, delete it from the interface and every implementer (the compiler won't catch this — you must remember).

### Benefits

- Every commit is deployable.
- Work can be interleaved with unrelated tasks.

### Considerations

- Prefer weakening preconditions when designing the new signature (range subsumes single-date).
- Don't forget to delete the old method from every implementer after the interface update.

---

## Pattern: Class-Level Strangler

### Intent

Replace a class when in-place refactoring would take too long or break too much at once. Add a new class, optionally with a temporary conversion helper, migrate callers, then delete the old class.

### When to Use

- A class was over-engineered (e.g. unnecessary generics) and a simpler type would clarify the code.
- A class's responsibility has drifted and you want to split or rename it without a big-bang edit.
- Multiple callers depend on the class and must be migrated individually.

### Structure

```csharp
// Starting point: the over-engineered generic.
public class Occurrence<T> { /* DateTime At, T Value */ }

// Step 1. Introduce the concrete replacement beside the old class.
public class TimeSlot { /* DateTime At, IReadOnlyCollection<Table> Tables */ }

// Step 2. Temporary bridge between old and new.
internal static TimeSlot ToTimeSlot(
    this Occurrence<IEnumerable<Table>> source) =>
    new TimeSlot(source.At, source.Value.ToList());

// Step 3. If signatures collide (C# has no return-type overloading),
//         rename the old method temporarily.
public IEnumerable<Occurrence<IEnumerable<Table>>> ScheduleOcc( /* old */ );
public IEnumerable<TimeSlot>                       Schedule   ( /* new */ );

// Step 4. Migrate callers one at a time, then delete ScheduleOcc,
//         ToTimeSlot, and Occurrence<T>.
```

### Walkthrough

1. Add the new class. Commit and merge — no behaviour change.
2. If helpful, add a conversion method between old and new, marked `internal` to bound its scope.
3. If language constraints prevent a one-to-one replacement (C# has no return-type overloading), rename the old method to a temporary name (e.g. `ScheduleOcc`) and give the original name to the new method.
4. Migrate callers incrementally; commit per caller.
5. When the old class has no callers, delete it along with the conversion helper.

### Benefits

- Never more than a few minutes from a clean commit.
- Old and new can run side by side indefinitely.
- Teammates can keep working during the migration.

### Considerations

- Conversion helpers and temporary renames are scaffolding — remove them at the end.
- If migration spans days, document it so nobody adds new uses of the old class.

---

## Pattern Selection Guide

| Situation | Recommended Pattern |
|-----------|--------------------|
| Adding new behaviour that takes > 4 hours | Feature Flag |
| Splitting deploy from release | Feature Flag |
| Changing a single method signature | Method-Level Strangler |
| Replacing one class with another | Class-Level Strangler |
| Replacing a subsystem or legacy module | Strangler at architectural scale |
| Removing a public API | Deprecate first, then Strangler-style removal at next major version |
