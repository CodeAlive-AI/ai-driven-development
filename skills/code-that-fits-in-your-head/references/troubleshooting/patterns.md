# Troubleshooting Patterns

Reusable patterns for reproducing, localizing, and fixing defects.

## Pattern: Reproduce-as-Test

### Intent

Convert a bug report into a failing automated test, then fix the code to turn it green. The test simultaneously validates your hypothesis and becomes a permanent regression guard.

### When to Use

- A bug has been filed or observed (human report, log, exploratory testing).
- You have a hypothesis about where the defect lives.
- The behavior is reproducible, at least in principle.

### Structure

1. Observe the symptom.
2. Form a hypothesis about the cause.
3. Write a test asserting the *correct* behavior. Predict it will fail.
4. Run the test. Confirm it fails, and fails *for the reason you predicted*.
5. If it does not fail, or fails for a different reason, revise the hypothesis and go back to step 3.
6. Fix the production code.
7. Confirm the test now passes. Run the full suite.
8. Commit the test and the fix together.

### Example

```csharp
// Symptom: PUT /reservations/... returns name and email swapped.
// Hypothesis: ReadReservation passes columns to the Reservation
// constructor in the wrong order.
[Theory]
[InlineData("2032-01-01 01:12", "z@example.net", "z", "Zet", 4)]
public async Task PutAndReadRoundTrip(
    string date, string email, string name, string newName, int quantity)
{
    var r = new Reservation(
        Guid.NewGuid(),
        DateTime.Parse(date, CultureInfo.InvariantCulture),
        new Email(email), new Name(name), quantity);
    var sut = new SqlReservationsRepository(ConnectionStrings.Reservations);
    await sut.Create(r);
    var expected = r.WithName(new Name(newName));
    await sut.Update(expected);
    var actual = await sut.ReadReservation(expected.Id);
    Assert.Equal(expected, actual);
}

// Fix — swap the column order in the reader:
return new Reservation(id,
    (DateTime)rdr["At"],
    (string)rdr["Email"],   // was ["Name"]
    (string)rdr["Name"],    // was ["Email"]
    (int)rdr["Quantity"]);
```

### Benefits & Considerations

- Validates the hypothesis rigorously and leaves a regression guard.
- The test must fail *for the reason you predicted*; failing for a different reason means the hypothesis is wrong.
- If the repro needs a database or network, route it to the stage-two (slow) tier.

---

## Pattern: Git Bisection

### Intent

Binary-search the commit history to identify the exact commit that introduced a defect, when the offending commit is known to lie in a range too large to inspect manually.

### When to Use

- The feature worked at some earlier state and fails now.
- The offending commit sits inside a known range.
- You have a reliable classifier for "is the defect present at this checkout?" (automated test, manual check, HTTP call).

### Structure

```bash
# Start a session.
git bisect start

# Mark the current broken commit as bad (no SHA = HEAD).
git bisect bad

# Mark a known-good commit. Git checks out the midpoint.
git bisect good <good-sha>

# For each checkout git produces, classify and respond:
git bisect good     # defect NOT present
git bisect bad      # defect IS present

# After ~log2(N) steps, git prints the first bad commit.
git bisect reset    # return to original HEAD
```

### Example

A REST endpoint worked yesterday and now returns 401. About 130 commits separate the two states:

```bash
$ git bisect start
$ git bisect bad
$ git bisect good 58fc950
Bisecting: 75 revisions left to test after this (roughly 6 steps)
[3035c14...] Use InMemoryRestaurantDatabase in a test

$ git bisect good
Bisecting: 37 revisions left to test after this (roughly 5 steps)
[aa69259...] Delete Either API

# ... continue marking good/bad for ~8 iterations ...

$ git bisect good
2563131c2d06af8e48f1df2dccbf85e9fc8ddafc is the first bad commit
    Extract CreateTokenValidationParameters method

$ git bisect reset
```

### Benefits & Considerations

- Logarithmic in history size; 130 commits finish in about 8 iterations.
- Works even when no test caught the original regression.
- Can be automated via `git bisect run <command>` using exit codes.
- Requires small, buildable commits — broken intermediate commits make it painful.
- If the classifier is slow, 8 iterations become hours; keep tests fast.
- Always `git bisect reset` when done.

---

## Pattern: Isolate-Then-Fix (Non-determinism)

### Intent

For defects driven by uncontrolled inputs — threads, clock, random, locale, network — isolate the non-deterministic source first so behavior becomes testable, then fix.

### When to Use

- The defect reproduces "sometimes" rather than reliably.
- The symptom correlates with load, time of day, machine, locale, or external state.
- Standard Reproduce-as-Test fails because the test passes on re-runs.

### Structure

1. Identify the non-deterministic input (threading, clock, RNG, locale, external service).
2. Make it injectable — pass clock, RNG, or collaborator as a dependency.
3. Choose a reproduction strategy: **injection** (test pins the input — fixed clock, seed, culture), **stress loop** (run the scenario in a tight loop under a timeout), or **fixture** (spin up and tear down an isolated resource per case).
4. Write the reproduction test; accept that it may be slow or probabilistic and route it to the stage-two tier.
5. Fix the defect and re-run the reproduction until satisfied.

### Example (race condition)

Symptom: the system occasionally accepts overbooking when two HTTP requests arrive simultaneously — the `Post` method reads reservations, decides the new one fits, then writes, and a concurrent request slips in between.

Reproduction via stress loop, fix via transaction scope:

```csharp
[Fact]
public async Task NoOverbookingRace()
{
    var start = DateTimeOffset.UtcNow;
    var timeOut = TimeSpan.FromSeconds(30);
    var i = 0;
    while (DateTimeOffset.UtcNow - start < timeOut)
        await PostTwoConcurrentLiminalReservations(
            start.DateTime.AddDays(++i));
}

// Fix — serialize the read-and-write:
using var scope = new TransactionScope(
    TransactionScopeAsyncFlowOption.Enabled);
var reservations = await Repository.ReadReservations(r.At)
    .ConfigureAwait(false);
if (!MaitreD.WillAccept(DateTime.Now, reservations, r))
    return NoTables500InternalServerError();
await Repository.Create(r).ConfigureAwait(false);
await PostOffice.EmailReservationCreated(r).ConfigureAwait(false);
scope.Complete();
```

### Benefits & Considerations

- Turns "works on my machine" into a concrete failing case, and the injected seam usually improves the design.
- Stress-loop tests accept probabilistic coverage (and possible false negatives) in exchange for any coverage at all; run them in the stage-two tier.
- Architectural fixes (Unit of Work, durable queue with single-threaded writer) may be needed when transactions alone are insufficient.

---

## Pattern Selection Guide

| Situation | Recommended Pattern |
|-----------|-------------------|
| Bug filed, reproducible on demand | Reproduce-as-Test |
| "It worked yesterday" | Git Bisection |
| "It fails sometimes" | Isolate-Then-Fix |
| Large commit range, deterministic repro | Git Bisection, then Reproduce-as-Test on the first bad commit |
| Flaky test in CI | Isolate-Then-Fix (the test is the symptom of hidden non-determinism) |
