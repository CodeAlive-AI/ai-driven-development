# Evolution Patterns

Reusable patterns for replacing a method or a class while its callers keep working.

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

1. Add the new method to the interface and implement it in every concrete class. Options: full implementation everywhere in one commit; `NotImplementedException` stubs filled in one implementer at a time; or concrete classes first, interface last.
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
4. Migrate callers in coherent, verifiable batches. A systematic transformation may cover many callers at once when the mapping and oracle are trustworthy.
5. When the old class has no callers, delete it along with the conversion helper.

### Benefits

- Each meaningful checkpoint is verified and leaves a clear recovery path.
- Old and new can run side by side indefinitely.
- Teammates can keep working during the migration.

### Considerations

- Conversion helpers and temporary renames are scaffolding — remove them at the end.
- If migration remains incomplete across integrations, document it and prevent new uses of the old class.

---

## Pattern Selection Guide

| Situation | Recommended Pattern |
|-----------|--------------------|
| Changing a single method signature | Method-Level Strangler |
| Replacing one class with another | Class-Level Strangler |
| Removing a public API | Deprecate first, then Strangler-style removal at next major version |
| Replacing a subsystem or legacy module | Design the migration path first (`pragmatic-architecture`), then move each caller with the two patterns above |
| Changing a live schema, contract or stored format; staged exposure of a feature | Not this skill: `pragmatic-architecture` (change path) |
