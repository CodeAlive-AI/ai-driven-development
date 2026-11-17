# Go tooling

Read when the stack at hand is Go. The repository's existing tools win. These are defaults for a
role that nothing fills yet.

| Role | Common choice | Notes |
|---|---|---|
| Runner and case tables | `testing` with table-driven subtests via `t.Run` | An assertion library is optional |
| Doubles | Small interfaces defined by the consumer, hand-written fakes | At external boundaries only |
| HTTP | `net/http/httptest` | Real handlers, a real client, no network |
| Real database and services | testcontainers-go, or services the repository provides | Real migrations, isolated data |
| Files and environment | `t.TempDir()`, `t.Setenv` | `t.Setenv` cannot be combined with `t.Parallel` |
| Concurrency | The race detector, `testing/synctest`, channel or `sync.WaitGroup` barriers | Instead of `time.Sleep` |
| Fuzzing and properties | Native fuzzing with `go test -fuzz`, `rapid` | Keep the found inputs in the corpus |
| Golden files | A small file with an `-update` flag | Review every update of the file |
| Sensitivity probe | A mutation tool scoped to the changed packages, or a manual break | Read survivors |

## Useful flags

| Flag | Use |
|---|---|
| `-race` | Data races in the code the tests exercise |
| `-shuffle=on` | Dependence on test order |
| `-count=1` | A fresh run that bypasses the test cache |
| `-run` with `-count=N` | Repeating a suspect to study a flake |

## Traps

- **Cached results:** `go test` reports cached passes. A cached pass is not a run on the current
  environment. Use `-count=1` when the environment or an external dependency matters.
- **Build tags:** tests behind a build tag that the pipeline never selects verify nothing and stay
  green. Confirm that the tagged suite ran.
- **Parallel subtests:** `t.Parallel` with shared state or a captured loop variable in older
  language versions gives order-dependent results.
- **Goroutine failures:** `t.Fatal` from another goroutine does not stop the test correctly.
  Report through a channel and assert in the test goroutine.
- **Ignored errors:** a test helper that drops an `err` hides the failure. Fail on it.
- **Vacuous loops:** a `for` over an empty slice with assertions inside checks nothing. Assert the
  length first.
- **Interface for mocking only:** an interface added to the producer package only to mock it
  changes the design for the test's sake. Define it where it is consumed, and only at a real
  boundary.
- **Race detector scope:** `-race` finds races on the paths that ran. It does not prove their
  absence elsewhere.
