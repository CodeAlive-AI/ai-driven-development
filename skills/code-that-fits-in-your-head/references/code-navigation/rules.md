# Code Navigation Rules

Actionable rules for onboarding to an unfamiliar code base using search, tests, architecture cues, and behavioural data.

## Core Rules

### 1. Start at the entry point, then zoom in

When you open a new code base, do not start by reading the whole file tree. Start at the framework's entry point (`Main`, `Startup`, `program.ts`, composition root) and read the top-level configuration as a table of contents.

- Service-registration and route-wiring methods list every major subsystem by name
- Each call is a pointer you can follow with search or LSP when needed
- Do not read implementations until you know which one the task requires

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

### 2. Navigate with search, imports, tests, and history

Use the most direct signal for the question at hand:

| Question | Prefer |
|----------|--------|
| Where is this symbol defined? | `rg 'SymbolName'` or LSP go-to-definition |
| Who calls this? | `rg -w 'SymbolName'` |
| How is this wired? | Follow imports from the composition root / entry point |
| What should this do? | Read the test named after the behaviour **before** the implementation |
| Why is this here? | `git log --follow -- <file>` and blame |

File layout is complementary, not a design rule. Do not reorganise directories for navigation convenience.

### 3. Read tests first — they encode intent

When a code base has a test suite, the tests are the shortest path to understanding usage. A good test has a high abstraction level: it shows *what* the system does without drowning you in *how*.

- Look for tests named after the behaviour you want to understand
- Follow test helpers to discover the public shape of the API
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
- Remember: test code is code; maintain it carefully (tests have no safety net)

### 5. Check for dependency cycles early

Cycles between classes or packages block understanding because they collapse abstraction levels. If A depends on B which depends on A, no zoom level is self-contained.

- A typical cycle: a Domain Model repository interface that uses ORM row types in its signatures
- Splitting the code into packages/projects makes cycles a compile error — free poka-yoke
- Detection commands: `../tooling/commands.md` (cycle and layer tools)

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

### 7. Use property-based testing for invariants

When you can describe a property more easily than enumerate cases, reach for a property-based testing library (FsCheck, QuickCheck, Hypothesis, fast-check). The framework generates many inputs per run, biased toward boundary values.

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

- Commands for churn, hotspots, and coupling: `../tooling/commands.md`
- Change coupling catches copy-paste dependencies that static analysis misses
- Watch trends, not absolute numbers — a bad trend is actionable even on a legacy code base

## Context Budget

In a large repository, read progressively — do not ingest the tree:

1. Entry point / composition root (table of contents).
2. The one module the task touches.
3. Its tests (behaviour named after the task).
4. **Stop.** Do not read whole directories speculatively.

Further discipline:

- Prefer summarising a file's public surface (exports, public methods, type signatures) over ingesting method bodies.
- When the map is bigger than the remaining context budget, write findings to a scratch note and continue from the note — do not re-read the same files.
- Follow one import chain at a time; breadth-first directory listing is almost always waste.

## Guidelines

- Follow the repository's existing file-organisation convention; flat vs deep is a project choice
- When a test helper has no test-specific logic, consider moving it to a production client SDK
- Use numerical thresholds from behavioural analysis to direct attention, not as law
- On a larger team, use knowledge maps (main author per file) to find bus-factor risk

## Exceptions

When these rules may be relaxed:

- **Framework conventions**: If a framework expects a specific folder layout (e.g. Next.js `app/`, Rails MVC), follow it — fighting conventions costs more than it saves
- **Regulatory splits**: Some compliance regimes require package-level isolation regardless of coupling
- **Tiny repositories**: Progressive disclosure still helps, but a full read may fit the budget

## Quick Reference

| Rule | Summary |
|------|---------|
| Start at entry point | Read `Main`/`Startup`/composition root as table of contents |
| Navigate with search | `rg` / LSP / imports / tests / `git log --follow` |
| Read tests first | They document intent in runnable form |
| Listen to tests | Painful tests reveal bad design |
| Check for cycles | Red flag; packages make them a compile error |
| Monolith is fine | Only the *internal* structure matters |
| Property-based for invariants | Framework-generated inputs over hand-picked ones |
| Behavioural analysis | Git history reveals hotspots and coupling (`../tooling/commands.md`) |
| Context budget | Entry → one module → its tests → stop; scratch notes beat re-reads |
