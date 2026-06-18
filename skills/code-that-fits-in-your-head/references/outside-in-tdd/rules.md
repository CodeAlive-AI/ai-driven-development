# Outside-In TDD Rules

Rules for driving code with tests: AAA structure, seeing tests fail, balancing static analysis, choosing between red-green-refactor and Devil's Advocate, and deciding when you have enough tests.

## Core Rules

### 1. Structure Tests as Arrange / Act / Assert

Separate the three phases with a single blank line. No other blank lines in the test body — they create ambiguity about which blank line separates which phase.

- Arrange: prepare everything the test needs (SUT, dependencies, inputs).
- Act: invoke the operation under test.
- Assert: verify the observed outcome against the expected outcome.

If the test is tiny (1-3 lines, one per phase) you can drop the blank lines. If the test is so large you need comments to mark phases, the test is too big.

**Example**:
```csharp
// Bad: Extra blank lines; phases are ambiguous
[Fact]
public async Task PostValidReservationWhenDatabaseIsEmpty()
{
    var db = new FakeDatabase();

    var sut = new ReservationsController(db);
    var dto = new ReservationDto { ... };

    await sut.Post(dto);
    var expected = new Reservation(...);

    Assert.Contains(expected, db);
}

// Good: Exactly two blank lines delineate three phases
[Fact]
public async Task PostValidReservationWhenDatabaseIsEmpty()
{
    var db = new FakeDatabase();
    var sut = new ReservationsController(db);

    var dto = new ReservationDto { ... };
    await sut.Post(dto);

    var expected = new Reservation(...);
    Assert.Contains(expected, db);
}
```

### 2. Start at the Boundary, Work Inward

First tests go against the outermost API (HTTP, CLI, queue). As combinatorial complexity appears, add unit tests for smaller units in isolation. Don't try to cover every edge case at the boundary.

### 3. See Every Test Fail Before You Trust It

A test you haven't seen fail may be tautological — it could pass even with broken production code.

- With TDD's red-green flow you see this for free on new tests.
- When you edit an existing test or write one after the production code, deliberately sabotage the SUT (return a hard-coded value, comment out logic) and confirm the test fails. Use `git stash` or staged changes to discard the sabotage cleanly.

### 4. Keep Boundary Assertions Light; Strengthen Over Time

At the outer boundary, early tests should only verify the most superficial stable property (e.g. `response.IsSuccessStatusCode`). Detailed assertions are brittle during exploration. You can always strengthen postconditions later by adding more assertions to an existing test.

### 5. Prefer Appending Over Modifying Test Code

The safe edits to test code are additive:
- Add a new test method.
- Add a test case to a parametrised `[Theory]`.
- Add another assertion to an existing act phase.

Anything that removes or changes existing asserts weakens postconditions and can hide regressions.

### 6. Refactor Test Code and Production Code in Separate Commits

If you must restructure test code, stop touching production code first. Stash partial production changes, refactor tests, run the suite, commit. Then re-apply production changes. This isolates the risk of silent test-weakening to a reviewable commit.

### 7. Moderate Static Analysis in Test Code

Treat static analysis as another driver of change, but not every rule applies to test code. Disable rules that only make sense in reusable production libraries (e.g. `CA2007 ConfigureAwait`) for test assemblies; suppress per-call with `[SuppressMessage]` when a rule fires on a literal you're going to type out anyway.

**Always document *why* you suppress**:
```csharp
[SuppressMessage(
    "Usage", "CA2234:Pass system uri objects instead of strings",
    Justification = "URL isn't passed as variable, but as literal.")]
```

### 8. Use Devil's Advocate to Decide When You Need Another Test

After a test passes, ask: can I write a deliberately stupid implementation that still passes? If yes, that's a signal to add a test case — often just another `[InlineData]` line — that would reject the stupid version. If no, your test set is strong enough for now.

### 9. Switch from Devil's Advocate to Red-Green-Refactor Once Structure Exists

Devil's Advocate forces you to add tests. Red-Green-Refactor says: once a test is green, look for a safe generalisation (replace a `SingleOrDefault` hack with `Sum`). Don't add a test when refactoring gets you the same correctness.

### 10. Separate DTO from Domain Model

The type that receives the wire format (JSON) has no invariants — all fields nullable, string-typed. The domain type enforces invariants and is what tests and production logic assert on. Don't let one type serve both roles.

## Guidelines

- Aim for balance between arrange / act / assert sections. A 2-2-2 or 1-1-1 shape reads better than 5-1-1.
- When an act section is a single line hidden behind a lot of setup, extract a SUT Encapsulation Method or Test Utility Method in the test project.
- Write down edge cases you think of while writing a test — don't derail to implement them mid-test.
- Commit after each passing test run; consider pushing through the deployment pipeline.
- Prefer Value Objects in the Domain Model — structural equality makes elegant `Assert.Contains(expected, actual)` possible.

## Exceptions

- **Characterisation tests**: No red phase by definition. Assert only the weakest stable property of the existing code.
- **Humble Objects** (SQL repositories, framework glue): May skip unit tests; push logic out and cover them with integration tests later.
- **Auto-generated code** (IDE-generated `Equals`, `GetHashCode`, constructors): Trust the generator; no need to triangulate.

## Deciding You Have Enough Tests

No quantitative rule exists. Ask:

1. How likely is a regression? (Assume benign intent from teammates.)
2. What's the impact of that regression?

If either is high, add the test. Any defect that reaches production has tautologically demonstrated it can happen — always add a regression test when you fix one.

## Quick Reference

| Rule | Summary |
|------|---------|
| AAA | Three phases, two blank lines, no more |
| Outside-In | Boundary first, unit tests inward |
| See Tests Fail | Never trust a test you haven't seen red |
| Light Assertions Early | Boundary tests assert weakest stable property |
| Append, Don't Modify | Adding test code is safe; editing isn't |
| Separate Refactor Commits | Tests and production code refactored apart |
| Moderate Static Analysis | Suppress with justification; disable where it doesn't fit |
| Devil's Advocate | Weak tests let stupid code pass; add test or refactor |
| When Enough Tests | Weigh probability × impact; no hard number |
