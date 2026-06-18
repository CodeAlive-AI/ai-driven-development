# Code Navigation Rules

Actionable rules for onboarding to an unfamiliar code base and using tests, architecture cues, and behavioural data to find your way.

## Core Rules

### 1. Start at the entry point, then zoom in

When you open a new code base, do not start with the file tree. Start at the framework's entry point (`Main`, `Startup`, `program.ts`, etc.) and read the top-level configuration as a table of contents.

- `ConfigureServices`-style methods list every major subsystem by name
- Each call is a pointer you can Go To Definition on
- Do not read implementations until you know which one you need

**Example**:
```csharp
// Big picture first — this is the "table of contents"
public void ConfigureServices(IServiceCollection services)
{
    // ...
    ConfigureAuthorization(services);
    ConfigureRepository(services);
    ConfigureRestaurants(services);
    ConfigureClock(services);
    ConfigurePostOffice(services);
}
```

### 2. Navigate with the IDE, not the file tree

Hide the file/solution explorer as an exercise. Use Go To Definition (F12 in Visual Studio), Go To Implementation, Find All References, symbol search, and tab switching. The file you worked on three minutes ago is one keyboard shortcut away.

- Don't scroll a tree to find a class by name
- Learn the keybindings for your IDE's navigation commands
- Open files by symbol, not by path

### 3. Read tests first — they encode intent

When a code base has a test suite, the tests are the shortest path to understanding usage. A good test has a high abstraction level: it shows *what* the system does without drowning you in *how*.

- Look for tests named after the behaviour you want to understand
- Follow Test Utility Methods to discover the public shape of the API
- If you find utilities that are not test-specific, consider promoting them to production

**Example**:
```csharp
[Fact]
public async Task ReserveTableAtNono()
{
    using var api = new SelfHostedApi();
    var client = api.CreateClient();
    var dto = Some.Reservation.ToDto();
    dto.Quantity = 6;
    var response = await client.PostReservation("Nono", dto);
    // The test itself documents the happy path
}
```

### 4. Treat hard-to-write tests as a design smell

If writing a test requires elaborate setup, deep mocking, or global state manipulation, the problem is in the production code, not the test. "Listen to your tests."

- Test pain = design pain
- Refactor the System Under Test, not the test, when tests get ugly
- Remember: test code is code; maintain and refactor it like production

### 5. Check for dependency cycles early

Cycles between classes or packages block understanding because they collapse abstraction levels. If A depends on B which depends on A, no zoom level is self-contained.

- A typical cycle: a Domain Model repository interface that uses ORM row types in its signatures
- Splitting the code into packages makes cycles a compile error — free poka-yoke
- If cycles exist, understanding order-of-reading becomes arbitrary

**Example** — cycle to avoid:
```csharp
// Domain Model package
public interface IRepository
{
    void Create(Row row); // Row is defined in the data-access package
}

// Data access package
public class OrmRepository : IRepository { /* must reference Domain Model */ }
// => Domain Model depends on Data Access, and vice versa. Cycle.
```

### 6. A monolith is not automatically wrong

Single-package deployment is the simplest shape. The anti-pattern is *internal* spaghetti, not the monolith itself. Judge a monolith by whether its insides follow ports-and-adapters or functional-core-imperative-shell, not by package count.

- Don't recommend a split until you see concrete coupling problems
- Splitting into packages is a tool for enforcing acyclic dependencies, not a goal
- F# and Haskell programmers can often keep a monolith clean by habit

### 7. Use property-based testing for invariants

When you can describe a property more easily than enumerate cases, reach for a property-based testing library (FsCheck, QuickCheck, Hypothesis, fast-check). The framework generates ~100 inputs per run, biased toward boundary values.

- Good for: "must be positive", "must round-trip", "must be idempotent", "must be sorted"
- Complement, don't replace, example-based tests — use both
- Start with built-in wrappers (`NonNegativeInt`, `PositiveInt`) before writing custom generators

**Example**:
```csharp
[Property]
public void QuantityMustBePositive(
    Guid id, DateTime at, Email email, Name name, NonNegativeInt i)
{
    var invalidQuantity = -i?.Item ?? 0;
    Assert.Throws<ArgumentOutOfRangeException>(
        () => new Reservation(id, at, email, name, invalidQuantity));
}
```

### 8. Use behavioural code analysis on legacy bases

For any code base with real history, mine Git to find hotspots (high complexity × high change frequency) and change coupling (files that commit together).

- Hotspot enclosure diagram: circle size = complexity, colour intensity = change frequency
- Change coupling catches copy-paste dependencies that static analysis misses
- Watch trends, not absolute numbers — a bad trend is actionable even on a legacy code base
- Optionally wire it into your Continuous Delivery pipeline

## Guidelines

Less strict recommendations:

- Prefer flat directories until a group of files is clearly and narrowly scoped (e.g. ASP.NET options DTOs)
- When a Test Utility Method has no test-specific logic, consider moving it to a production client SDK
- Use numerical thresholds from behavioural code analysis to direct attention, not as law
- On a larger team, use knowledge maps to find single-author files (bus-factor risk)

## Exceptions

When these rules may be relaxed:

- **Framework conventions**: If a framework expects a specific folder layout (e.g. Next.js `app/`, Rails MVC), follow it — fighting conventions costs more than it saves
- **Regulatory splits**: Some compliance regimes require package-level isolation regardless of coupling
- **Experienced F#/Haskell teams**: Can keep a monolith decoupled without compile-time package barriers

## Quick Reference

| Rule | Summary |
|------|---------|
| Start at entry point | Read `Main`/`Startup` as table of contents before drilling in |
| Navigate with IDE | Go To Definition beats folder scrolling |
| Read tests first | They document intent in runnable form |
| Listen to tests | Painful tests reveal bad design |
| Check for cycles | Red flag; packages make them impossible |
| Monolith is fine | Only the *internal* structure matters |
| Property-based for invariants | Framework-generated inputs over hand-picked ones |
| Behavioural analysis for legacy | Git history reveals hotspots and coupling |
