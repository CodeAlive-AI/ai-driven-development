# Levels and test doubles: where to check and what must be real

Read when deciding between unit, integration, contract and e2e, when about to mock something, or
when testing a database, concurrency, a migration or an external service.

## Contents

- [Vocabulary](#vocabulary)
- [Selection algorithm](#selection-algorithm)
- [Checks that are not tests](#checks-that-are-not-tests)
- [Test doubles: purpose first](#test-doubles-purpose-first)
- [Defaults and the gap each double leaves](#defaults-and-the-gap-each-double-leaves)
- [Fidelity of a significant fake](#fidelity-of-a-significant-fake)
- [Database](#database)
- [Concurrency and idempotency](#concurrency-and-idempotency)
- [Migrations](#migrations)
- [External services and contracts](#external-services-and-contracts)
- [Worked example: autosave](#worked-example-autosave)

## Vocabulary

- **Unit:** a small coherent behaviour, usually in one process and without real external
  infrastructure. The unit may be a group of objects. Several classes do not make it an
  integration test.
- **Component:** a module or UI component as a whole behind a stated boundary.
- **Integration:** a chosen boundary between components, or the application with infrastructure:
  database, HTTP, file system, transport.
- **Contract:** compatibility of two interacting sides.
- **E2E:** a chosen working route through the whole system.

The names overlap. A browser test of one component is not e2e, and an e2e route may start at the
API. For a wide test, state where it starts, where it ends and which dependencies are substituted.
Use the repository's own vocabulary where it differs.

## Selection algorithm

1. State the contract violation: a wrong value, a lost record, wrong access, a repeated effect,
   input that does not work.
2. Identify the mechanism. Does it need SQL, browser layout, the OS, the network, several
   processes, real serialization?
3. Choose the smallest environment that keeps that mechanism. Removing the boundary the defect
   lives in makes the test cheaper and meaningless.
4. Check that the result is observable there. If not, move the observation point or go up a level.
5. Add a whole-chain check only for the remaining risk that the parts are wired wrongly. Do not
   repeat the combinations of a domain rule on it.

Going up a level is justified by a new observable mechanism: a real transaction, routing,
configuration, browser behaviour.

## Checks that are not tests

| Risk | Fitting evidence |
|---|---|
| Types, dependencies, build, packaging | Type check, the relevant lint, a real build and a launch of the package |
| Access and confidentiality | Analysis of trust boundaries and negative checks at the server boundary |
| Speed or resource use | Measurement on representative data and load against a stated budget |
| Usability and accessibility | Completing the user goal; input, errors and the relevant assistive technology |
| Recovery and operations | A failure scenario, state recovery, diagnostics that are actually useful |

A type check does not confirm a business rule. A clean build does not confirm a user goal. Do not
have a model re-interpret what a deterministic tool already checks reliably.

## Test doubles: purpose first

A **stub** supplies inputs or answers. A **spy** records interactions. A **mock** verifies
expected interactions. A **fake** is a simplified working implementation. The purpose of the
check matters more than the name of the library.

- **Assert a call only when the call is the promise.** "After confirmation, notify the recipient"
  can be checked at the delivery boundary. "Call the internal helper exactly once" pins the
  internals, unless there is a contract on cost, idempotency, performance or resources.
- **Requests are not effects.** Two network calls with one idempotency key may be a valid retry
  that produces one charge. Assert the business effect on the boundary where it is visible.
- **Managed or unmanaged.** What matters is whether the interaction is observable outside the
  system. A database only this application uses is managed: use the real one in integration
  tests. A database other applications read directly carries external contracts. Cloud or Docker
  hosting decides nothing.
- **No mock chains.** Test a thin orchestrator integrated, and move real computation into logic
  that can be tested directly when that improves the code itself. A temporary double in legacy
  code is a stated limitation, not proof of integration.
- **No design for the mock's sake.** Do not change a public API or add interfaces only to suit a
  mocking framework.

## Defaults and the gap each double leaves

| Dependency and purpose | Default | What stays unproven |
|---|---|---|
| Own pure logic | Real objects | Infrastructure outside the test |
| Time, UUIDs, randomness | A controlled source or a fixed input | Real timers and distributed time |
| Database when checking storage | A real compatible engine and schema | Nothing about SQL or transactions is proven by an in-memory fake |
| External API in CI | Stub, plus a separate adapter or contract check | Current compatibility and availability of the provider |
| Outgoing notification | Spy or mock at the external contract, or a test receiver | Delivery to the real recipient |
| Network and rate limits | Controlled injection of the failure | The other real network modes |
| UI in isolation | Network stub for the needed state | Frontend and backend working together |
| Message broker | Real broker for ack and redelivery; a double for the reaction | Real delivery when the callback runs in memory |
| Export to a file | A real temporary file system | The result opened by the external consumer |

Every double leaves a gap. Name it, and close it with a separate check when it matters for
acceptance.

## Fidelity of a significant fake

When a substitute carries real weight in the proof, answer five questions:

1. Which behaviour of the real dependency is modelled?
2. Where is that behaviour known from: a specification, provider verification, a real sandbox, a
   recorded and checked example?
3. Which states, errors and timing properties are not represented?
4. Which rules does the real platform enforce that the substitute does not: required
   user-visible effects, permissions, background limits, quotas, payload sizes, signing?
5. Which separate check closes the remaining material risk?

- A rule the substitute does not enforce is still a requirement on the code. A browser may
  require each push message to show a notification; a fake push service or a synthetic event in
  a unit test does not, so code that sometimes stays silent passes them. Take such rules from
  the platform's current documentation and check them where the platform runs.
- An API schema confirms the shape of a request. It does not confirm redelivery, idempotency or
  recovery after a lost response.
- A fake written from the author's own understanding of an API is not external confirmation of
  that understanding. Cross-check mock and production against a third source.
- At least one test starts from the raw payload in the provider's shape and passes through the
  production parser and validator.
- A stub that returns the final state on the first call hides a missing polling loop. Model the
  lifecycle the code has to wait through.
- A rich local emulator is verified against the real system on chosen interactions first, and its
  known differences are kept in a list.

## Database

1. Bring up an isolated environment and apply the real migrations.
2. Prepare minimal data with an explicit owner and a unique namespace.
3. Call the real write path through the chosen public boundary.
4. Read the result with a new session or connection, so it is not served from ORM memory.
5. Check the significant values, the number of records and the forbidden side effects.
6. Release data and resources without depending on the order of neighbouring tests.

- **Observation:** use the existing read API when it shows what is needed. A direct query is fine
  when the public API does not expose the state. When the risk is in the mapping or a migration,
  an independent read is better than reading through the same faulty mapping.
- **Isolation:** a container per test is one method, not the goal. A schema per worker, unique
  data and controlled cleanup can be cheaper.
- **Rollback wrappers:** a test wrapped in a rolled-back transaction never exercises the real
  commit, deferred constraints or after-commit processing.
- **Engine:** an in-memory substitute proves nothing about the production dialect, types,
  constraints, collation or transactions.

## Concurrency and idempotency

- A sequential double call and concurrent requests probe different risks.
- Arrange the overlap with a controlled barrier or another fitting synchronization. A random
  sleep rarely produces the intended schedule.
- Uniqueness and atomicity need the real database. A mock that always "saves successfully"
  confirms neither.
- Assert the state after the operations finish: number of objects, status, no doubled external
  effect.
- One schedule does not prove the absence of all races. Choose the schedule that matches the risk.

## Migrations

Creating an empty database does not cover updating existing data. Use representative old rows,
the real migration and a read by the new version. For a staged rollout, check the versions that
run side by side. Test a rollback only in the form that is really supported: a `down` file does
not make an irreversible migration reversible.

## External services and contracts

Separate the business reaction to a response from the technical compatibility of the adapter.

- **Regular suite:** reproduce the needed responses and failures.
- **Adapter:** check what the task changes: serialization, parameters, signature, timeouts,
  interpretation of the response.
- **Live sandbox smoke:** run it when the risk of a contract or environment change is real, and
  keep its instability out of local unit tests.
- **Lost response:** let the stub record the effect and then fail the reply with a timeout or a
  dropped connection. Assert that the retry reuses the provider-side idempotency key or looks the
  result up, and that the stub holds exactly one effect. A stub that fails before recording tests
  a different failure point.
- **Recordings:** an old recorded response does not prove the provider has not changed.
- **Contract tests:** a verified message contract does not prove that the order was written or
  the side effect delivered. Without provider verification it holds only the consumer's
  assumptions.

## Worked example: autosave

Agreed contract: an editor can save a change; a reader cannot; a failed save shows no false
success and keeps recovery possible; concurrent edits follow the chosen policy.

| Case | What must be established | Main check | Why there |
|---|---|---|---|
| A valid change is saved | A later read returns the new content | Integration with real storage | Actual persistence is the claim |
| A reader sends the change request directly | Rejected, data unchanged | Server-side integration | A hidden button says nothing about server authorization |
| The request never reaches the server | The UI reports it and keeps the draft | Component test with controlled transport | Needs a reproducible failure and UI state |
| The write succeeds and the response is lost | Recovery accounts for the stored state | Integration with controlled response loss | The failure point relative to the write matters |
| An old response arrives after a newer one | The stale response does not overwrite current state | Unit test of the state model if separable, otherwise component | A specific order of events |
| Two editors change the same version | The agreed conflict policy holds | Integration with the real concurrency mechanism | A mocked store hides the mechanism |
| The user edits and reopens the document | The whole path works and shows the stored result | One short e2e route | Wiring of the UI and the rest |
| The form is used with a phone keyboard | Field, actions and messages stay reachable | Targeted mobile UI check | Needs the real interaction |

This shows the distribution for that contract. It does not mean every autosave feature needs eight
new tests: part of the behaviour may already be covered, and part may be outside the change.
