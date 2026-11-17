# .NET tooling

Read when the stack at hand is C# or another .NET language. The repository's existing tools win.
These are defaults for a role that nothing fills yet.

| Role | Common choice | Notes |
|---|---|---|
| Runner and case tables | xUnit `[Theory]` with `[InlineData]`, or NUnit | Use the one already configured |
| Doubles | NSubstitute, Moq | At unmanaged boundaries only |
| In-process host | `WebApplicationFactory` | Real routing, model binding, filters and serialization |
| Real database and services | Testcontainers for .NET | The real provider, not the EF Core in-memory provider, for relational behaviour |
| Data reset | Respawn, or unique data per test | Cheaper than a container per test |
| HTTP stubbing | WireMock.Net, or a stub `HttpMessageHandler` | Fail on unmatched requests |
| Time | `TimeProvider` with a fake provider | No `DateTime.Now` in domain code |
| Property-based | FsCheck, CsCheck | Constrain generators |
| Snapshots | Verify | Small and reviewed |
| UI | Playwright for .NET; bUnit for Blazor components | See `ui-automation.md` |
| API contract | PactNet | Needs provider verification to mean anything |
| Sensitivity probe | Stryker.NET with diff scoping | Read survivors; do not chase a percentage |

## Traps

- **In-memory database:** the in-memory provider and SQLite do not reproduce the constraints,
  transactions, collation or SQL translation of the production engine.
- **Change tracker:** read the result through a new context instance, or the assertion is served
  from tracked entities.
- **`async void`:** an exception in an `async void` test or handler is not observed by the
  runner. Return `Task`.
- **Waiting:** no `Task.Delay` as synchronization. Await the completion signal, or poll a
  condition with a timeout.
- **Vacuous assertions:** `All(…)` on an empty sequence is `true`, and a `foreach` with assertions
  checks nothing on an empty collection.
- **Shared fixtures:** class and collection fixtures share state across tests. Data created there
  needs unique keys, and tests must not rely on order.
- **Over-mocked handlers:** a handler test in which every collaborator is a substitute proves only
  that the substitutes were called. Run the handler through the in-process host with a real
  database.
- **Skipped tests:** `Skip = "…"` leaves a green run. Check the counts of run and skipped tests.

When the `unit-testing-principles` skill is installed, it carries detailed C# examples for unit
and integration tests.
