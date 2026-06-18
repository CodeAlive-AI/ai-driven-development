# Troubleshooting Rules

Actionable rules for debugging defects: prioritize understanding, reproduce before fixing, and localize before modifying.

## Core Rules

### 1. Understand Before You Fix

Your first reaction to a problem must be to understand why it is happening, not to make the symptom disappear. Do not try random incantations (restart, reboot, elevate, tweak) until the problem stops manifesting. That is programming by coincidence and leaves the defect in place.

- If you have no idea at all, ask for help.
- If you have some idea, form an explicit hypothesis.
- The goal of the first round of work is knowledge, not a green build.

### 2. Write the Hypothesis Down Before the Experiment

Apply the scientific method: predict, then experiment, then compare. A good hypothesis is falsifiable and concrete — "if I call this function with these arguments, it will return 42," not "something is wrong with the cache."

- Write the prediction before running anything.
- After the experiment, compare outcome to prediction out loud or in notes.
- If they disagree, revise the hypothesis. Do not adjust the hypothesis silently to match the result.

### 3. Reproduce the Defect as an Automated Test

Before fixing the code, write a test that fails because of the defect. This is both the experiment that validates your hypothesis and a permanent regression guard.

- A hypothesis of "the database repository swaps name and email" becomes a round-trip integration test that saves and re-reads a record.
- If the test passes unexpectedly, your hypothesis is wrong — revise it.
- Only fix the code after the failing test exists. Confirm the test now passes and re-run the full suite.

**Example** (C#):
```csharp
[Theory]
[InlineData("2032-01-01 01:12", "z@example.net", "z", "Zet", 4)]
public async Task PutAndReadRoundTrip(
    string date, string email, string name, string newName, int quantity)
{
    var r = new Reservation(
        Guid.NewGuid(),
        DateTime.Parse(date, CultureInfo.InvariantCulture),
        new Email(email),
        new Name(name),
        quantity);
    var sut = new SqlReservationsRepository(ConnectionStrings.Reservations);
    await sut.Create(r);
    var expected = r.WithName(new Name(newName));
    await sut.Update(expected);
    var actual = await sut.ReadReservation(expected.Id);
    Assert.Equal(expected, actual);
}
```

### 4. Rubber-Duck Before Pinging a Human

Before interrupting a colleague, explain the problem to a passive listener — a rubber duck, a draft Stack Overflow question, or an empty chat window. You will often find the answer mid-explanation.

- Time-box stuck periods (e.g. 25 minutes), then take a real break away from the screen.
- Write the question as if you intended to publish it. Include a minimal working example.
- If the answer comes to you, delete the draft. Do not fall for the sunk-cost fallacy.

### 5. Try Deleting Code Before Adding More

When a problem appears, consider whether removing code makes it go away. The default response of adding a special case for the new symptom usually compounds the underlying error.

- Ask: "What code could I delete to fix this?"
- Look for elaborate frameworks (DI containers, mock libraries, ORMs) where simpler code would serve.
- Simpler solutions are harder to find but have fewer defects to begin with.

### 6. Keep the Inner Test Suite Under Ten Seconds

The test suite you run during refactoring and the Red-Green-Refactor cycle must complete in seconds, not minutes. Beyond ten seconds, focus drifts, runs become rare, and the safety net evaporates.

- Put database, filesystem, and network tests in a separate project/solution (the "slow" or "integration" tier).
- Have a second build script (e.g. `build.sh`) that runs everything, used locally on demand and on the CI server.
- For `git bisect` to be practical, the suite used to classify each checkout must also be fast.

**Example** (`build.sh`):
```bash
#!/usr/bin/env bash
dotnet test Build.sln --configuration Release
```

### 7. Isolate Non-Determinism Before Fixing It

For defects driven by threading, clock, random, locale, or external state: pin the non-deterministic source (inject it, mock it, or stress it) before attempting the fix.

- For threading: write a loop test that hammers the scenario under a timeout (e.g. 30 seconds).
- For clock: inject an `IClock` / `DateTime` provider so tests can pin "now".
- For random: inject the RNG so the seed is controlled.
- For locale: assert or pin `CurrentCulture` in the test.
- For external state: stand up a disposable fixture (create + tear down per test).

**Example** (non-deterministic loop test):
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
```

### 8. Use `git bisect` When You Know It Broke Recently

If a feature worked at some past commit and fails now, do not stare at the diff. Bisect.

- You need a known-good commit, a known-bad commit, and a way to classify a checkout (a test, a command, an HTTP request).
- An N-commit range finishes in roughly log2(N) steps. 130 commits = ~8 iterations.
- Commit small and often so the first bad commit, when found, is small enough to diagnose at a glance.

**Example**:
```bash
$ git bisect start
$ git bisect bad               # current commit is broken
$ git bisect good 58fc950      # known-good commit
# git checks out the midpoint; verify and respond:
$ git bisect good              # or `git bisect bad`
# repeat until git prints "<sha> is the first bad commit"
$ git bisect reset
```

## Guidelines

Less strict recommendations:

- Prefer nondeterministic tests over no test coverage for defects that resist deterministic reproduction.
- False negatives (missed bugs) are tolerable; false positives (flaky failures) are corrosive — fix or quarantine them.
- Avoid stringly typed code (e.g. two consecutive `string` parameters with no type distinction). It makes silent argument swaps possible and is hard to catch via Humble Object testing alone.
- Do not lean on the debugger as your primary tool. It is unavailable in production and does not leave regression coverage behind.
- When you find the cause via bisection, write the regression test before closing the issue.

## Exceptions

When these rules may be relaxed:

- **Humble Object with cyclomatic complexity 1**: a unit test with the same complexity may not pay for itself. Even so, integration coverage is warranted if the code bridges two worlds (e.g. database mapping).
- **One-off exploration**: if you are investigating an unknown system with no test harness at all, ad-hoc scripts and REPL interaction are fine — but once the defect is reproduced, convert the repro into a test before fixing.
- **Genuinely rare races**: if a scenario reproduces on the order of once a month, a 30-second loop test may not be enough. Document the hypothesis and consider architectural changes (serialization via transactions, durable queues, single-writer components).

## Quick Reference

| Rule | Summary |
|------|---------|
| Understand first | Do not apply random fixes; ask why. |
| Write the hypothesis | Predict before experimenting. |
| Reproduce-as-test | Failing test before fix; it becomes the regression guard. |
| Rubber duck | Explain to something passive before pinging a human. |
| Delete first | Try removing code before adding more. |
| Ten-second budget | Inner-loop tests must be fast; slow tests go stage two. |
| Isolate non-determinism | Inject clock/random/etc. before fixing flakes. |
| `git bisect` | Binary-search history when you know it broke recently. |
