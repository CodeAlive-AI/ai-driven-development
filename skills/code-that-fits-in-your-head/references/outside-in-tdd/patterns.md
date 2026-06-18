# Outside-In TDD Patterns

Named patterns for test-driven development as practised in the book.

## Pattern: Walking Skeleton

### Intent

A deployable, testable, end-to-end slice of an application, established as early as possible — before any feature code exists.

### When to Use

- Starting a new codebase.
- Any time you need to prove a deployment pipeline works before weeks of feature work.

### Structure

1. Scaffold a new project (wizard / template).
2. Check it in; build script runs `dotnet test` (not just `dotnet build`).
3. Add a test project with one characterisation test at the outermost boundary.
4. Configure CI to run the script; deploy the result.

### Example

```csharp
[Fact]
public async Task HomeIsOk()
{
    using var factory = new WebApplicationFactory<Startup>();
    var client = factory.CreateClient();

    var response = await client.GetAsync("");

    Assert.True(
        response.IsSuccessStatusCode,
        $"Actual status code: {response.StatusCode}.");
}
```

### Benefits / Considerations

- Feedback on the full lifecycle from day one; later features are additive.
- Feels pointless ("just Hello World") but the value is in the infrastructure proof.

---

## Pattern: Characterisation Test

### Intent

Capture current behaviour of existing code to enable refactoring or feature additions without regression fear.

### When to Use

- Inherited codebase with no tests, scaffolded code to lock in, or before refactoring legacy code.

### Structure

Arrange minimal SUT, act as a real client would, assert ONLY the weakest stable property.

### Example

The Walking Skeleton test above is also a characterisation test — written after `dotnet new` scaffolded the project, asserts only `IsSuccessStatusCode`, and lets the team change the response body later without breaking the test.

### Considerations

- Not strict TDD (no red phase). Resist over-asserting — lock in only what must not regress.

---

## Pattern: Devil's Advocate

### Intent

Stress-test a test suite by trying to pass it with obviously wrong production code. The resulting stupid implementation tells you what test to write next.

### When to Use

- A test just went green and you aren't sure more tests are needed.
- Reviewing someone else's TDD work.
- Teaching TDD — exposes weak test sets.

### Structure

1. Write (or imagine) the simplest wrong code that passes all current tests — usually a hard-coded constant or a branch on a literal.
2. Ask: which new test case rejects it?
3. Add that case. Prefer another `[InlineData]` over a new method.
4. Re-run; continue until the stupid version no longer passes.

### Example

Given `OverbookAttempt` passes, the Devil writes:

```csharp
if (dto.Email == "shli@example.org")
    return new StatusCodeResult(
        StatusCodes.Status500InternalServerError);
```

Counter-case added to an *existing* test:

```csharp
[InlineData("2022-03-18 17:30", "shli@example.org", "Shanghai Li", 5)]
```

Same email, empty database, success expected — the stupid branch dies.

### Benefits

- Concrete heuristic for "do I need another test?"
- Drives the transformation from constant → scalar → variable logic.

### Considerations

- Pair with Red-Green-Refactor. Once the structure is right, refactoring is often better than yet another test.

---

## Pattern: Transformation Priority Premise (TPP)

### Intent

When passing a failing test, prefer the simpler code transformation on an ordered list (constant < scalar variable < conditional < loop < recursion). Keeps code generality in lockstep with test specificity.

### Example

`Reservation` starts hard-coded in `Post` (constant). Next transformation, constant → scalar: read values from the DTO. Later, `reservedSeats` uses `SingleOrDefault` (scalar on a one-element collection); next transformation, scalar → aggregate, is `Sum`.

### Considerations

- Full coverage lives in the encapsulation/ theme; referenced here as a decision aid for outside-in TDD.

---

## Pattern: Fake Object for I/O Isolation

### Intent

Replace an out-of-process dependency (DB, HTTP, queue) with an in-memory implementation of the same interface that has real observable behaviour.

### When to Use

- Unit tests needing persistence semantics without a real store.
- Boundary tests where DI must still work end-to-end.

### Structure

1. Define an interface for the dependency in production code.
2. In tests, inherit from an in-memory collection and implement the interface by delegating to self.
3. Swap real for fake via DI.

### Example

```csharp
public class FakeDatabase :
    Collection<Reservation>, IReservationsRepository
{
    public Task Create(Reservation reservation)
    {
        Add(reservation);
        return Task.CompletedTask;
    }
}
```

Boundary wiring:

```csharp
public class RestaurantApiFactory : WebApplicationFactory<Startup>
{
    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        builder.ConfigureServices(services =>
        {
            services.RemoveAll<IReservationsRepository>();
            services.AddSingleton<IReservationsRepository>(
                new FakeDatabase());
        });
    }
}
```

### Benefits / Considerations

- State-based assertions work trivially (`Assert.Contains(expected, db)`); fast and deterministic.
- Keep Fake behaviour realistic (date filtering, ordering) or tests pass while production breaks.
- Complement with a small number of real-infrastructure integration tests (Humble Object).

---

## Pattern Selection Guide

| Situation | Recommended Pattern |
|-----------|--------------------|
| Starting a brand-new codebase | Walking Skeleton + Characterisation Test |
| Adding first useful feature | Outside-In + Fake Object |
| Just made a test green, unsure what next | Devil's Advocate |
| Green test with obvious generalisation | Red-Green-Refactor (skip new test) |
| Two ways to pass a test | Transformation Priority Premise |
| Replacing DB / queue / HTTP in tests | Fake Object |
