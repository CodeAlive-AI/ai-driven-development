# Outside-In TDD Rules

Rules for driving code with tests: AAA structure, seeing tests fail, balancing static analysis, choosing between red-green-refactor and Devil's Advocate, and deciding when you have enough tests.

## Core Rules

### 1. Make Arrange / Act / Assert Visually Clear

Separate setup, execution, and observation so a reader can identify each phase immediately. Blank lines, helper methods, or framework conventions may express the structure; exact whitespace is a project style choice.

- Arrange: prepare everything the test needs (SUT, dependencies, inputs).
- Act: invoke the operation under test.
- Assert: verify the observed outcome against the expected outcome.

If comments are required to find the act or assertion, simplify the test or extract setup that obscures behavior.

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

### 4. Start With Stable Boundary Assertions; Strengthen Before Acceptance

During the first walking-skeleton slice, assert the smallest stable observable contract. Before the feature is accepted, cover the user-visible outcome and material side effects. A superficial success status is not sufficient final evidence when behavior matters.

### 5. Preserve Test Intent When Modifying Tests

Additive edits are easier to review:
- Add a new test method.
- Add a test case to a parametrised `[Theory]`.
- Add another assertion to an existing act phase.

Changing or removing assertions may be correct when requirements change or tests are refactored, but the reason and changed oracle must be explicit. Never weaken tests merely to make production code pass.

### 6. Make Oracle Changes Auditable

Reviewers must be able to distinguish changed behavior, changed test oracle, and mechanical test refactoring. Separate commits are one good technique, but do not force broken intermediate states or contort an atomic change.

### 7. Apply Useful Static Analysis to Test Code

Use the strictest practical checks that produce useful signal. Disable rules that genuinely do not apply to test code, and suppress narrowly with a reason rather than weakening the entire test project.

**Always document *why* you suppress**:
```csharp
[SuppressMessage(
    "Usage", "CA2234:Pass system uri objects instead of strings",
    Justification = "URL isn't passed as variable, but as literal.")]
```

### 8. Use Devil's Advocate to Decide When You Need Another Test

After a test passes, ask: can I write a deliberately stupid implementation that still passes? If yes, that's a signal to add a test case — often just another `[InlineData]` line — that would reject the stupid version. If no, your test set is strong enough for now. To automate this heuristic on a touched module, run mutation testing (Stryker, mutmut, PIT, cargo-mutants — see `../tooling/commands.md`); surviving mutants are the missing test cases.

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
| AAA | Make setup, execution, and observation obvious |
| Outside-In | Boundary first, unit tests inward |
| See Tests Fail | Never trust a test you haven't seen red |
| Light Assertions Early | Boundary tests assert weakest stable property |
| Preserve test intent | Oracle changes require explicit rationale |
| Auditable refactoring | Distinguish behavior, oracle, and mechanical edits |
| Moderate Static Analysis | Suppress with justification; disable where it doesn't fit |
| Devil's Advocate | Weak tests let stupid code pass; add test or refactor |
| When Enough Tests | Weigh probability × impact; no hard number |

## Editorial Amendment (2026) — Not from the Book

Pairing self-authored tests with an independent oracle and never weakening verification are covered canonically in `../agent-native/verification-loops.md`.
