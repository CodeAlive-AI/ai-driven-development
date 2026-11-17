# JVM tooling: Java and Kotlin

Read when the stack at hand is Java or Kotlin. The repository's existing tools win. These are
defaults for a role that nothing fills yet.

| Role | Common choice | Notes |
|---|---|---|
| Runner and case tables | JUnit with `@ParameterizedTest`; Kotest for Kotlin | AssertJ or the runner's own matchers |
| Doubles | Mockito, MockK | At external boundaries only |
| Real database and services | Testcontainers | The real engine, not H2, for dialect, constraints and transactions |
| HTTP stubbing | WireMock, MockWebServer | Fail on unmatched requests |
| Async | Awaitility | Instead of `Thread.sleep` |
| Time | An injected `java.time.Clock` | No reads of the system clock in domain code |
| Property-based | jqwik | Constrain generators |
| API contract | Pact JVM, Spring Cloud Contract | Needs provider verification to mean anything |
| Structural rules | ArchUnit | For structural requirements only |
| Browser | Playwright for Java, Selenium | See `ui-automation.md` |
| Sensitivity probe | PIT, scoped to the changed classes | Read survivors; do not chase a percentage |

## Traps

- **Transactional tests:** a test method that rolls back never reaches the real commit, deferred
  constraints or after-commit listeners. When the change touches those, commit for real and clean
  up.
- **Heavy contexts:** in Spring, every distinct context configuration, including each combination
  of mocked beans, starts a new application context. This is a common cause of slow suites.
  Prefer a slice test for a controller or repository risk, and reuse one full configuration for
  the rest.
- **Mocked persistence:** a mocked repository confirms nothing about queries, mappings, lazy
  loading or uniqueness. Test those against the real engine.
- **ORM cache:** read the result in a new transaction or session, or the assertion is served from
  the first-level cache.
- **Vacuous assertions:** `allMatch` on an empty stream is `true`, and `forEach` with assertions
  checks nothing on an empty collection.
- **Swallowed failures:** an exception inside another thread or an executor does not fail the
  test unless the future is joined and its result asserted.
- **Disabled tests:** `@Disabled` and conditional execution annotations leave a green build. Check
  the counts of run and skipped tests.
- **Static and shared state:** singletons, static caches and system properties leak between tests
  and show up only under a different order or parallel execution.
