# Python tooling

Read when the stack at hand is Python. The repository's existing tools win. These are defaults
for a role that nothing fills yet.

| Role | Common choice | Notes |
|---|---|---|
| Runner and case tables | pytest, `pytest.mark.parametrize` | Parametrize with lists, not sets: parallel workers need the same collection order |
| Property-based | Hypothesis | Prefer constrained strategies to `.filter` and `assume`; pin a found failure with `@example` |
| HTTP stubbing | `respx` for httpx, `responses` for requests, or a local stub server | Make unmatched requests fail |
| Real database and services | Testcontainers, or services the repository already provides | Apply the real migrations; a schema or database per worker |
| Time | An injected clock; `time-machine` or `freezegun` when injection is not possible | Pin a non-UTC zone when the zone matters |
| Async | `pytest-asyncio` or anyio | Wait on an `asyncio.Event`, not on `sleep`; do not define a custom event-loop fixture |
| Parallel and order | `pytest-xdist`, `pytest-randomly` | Session fixtures run once per worker; group contended resources |
| API contract | Schemathesis for OpenAPI, `pact-python` | Schema conformance is not behaviour |
| Browser | Playwright for Python | See `ui-automation.md` |
| Sensitivity probe | mutmut or cosmic-ray, scoped to the changed modules | Check how the tool reports survivors; see below |

## Traps

- **Vacuous assertions:** `assert all(check(x) for x in items)` and `for x in items: assert …`
  pass on an empty `items`. Assert `items` first.
- **Environment leaks:** `monkeypatch.setenv` is undone after the test. A direct write to
  `os.environ` in production code is not. Wrap it with `mock.patch.dict(os.environ)`.
- **Parallelism hides leaks.** Workers isolate modules from each other, so a leak may appear only
  in a serial run. Run suspects with `-p no:xdist` and in random order.
- **Hypothesis settings:** in CI, set `derandomize=True` and drop the deadline for slow machines.
  Do not suppress health checks wholesale. A slow-data warning usually means the strategy filters
  too much.
- **Property that restates the code:** ask whether a function returning `[]` or `None` would pass.
- **Validation path:** validate test payloads the way production does. Parsing JSON text directly
  into a model and validating an already parsed dict can differ in strictness.
- **Mutation tools:** an exit status of 0 may not mean "no survivors", and decorated functions may
  produce no mutants at all. Zero mutants is not a pass. Read the counts.
- **Skips:** a suite that reports only skips is green and verified nothing. An optional plugin or
  marker that silently disables a group of tests needs a check that the group ran.
- **Type checks:** mypy or pyright confirm types, not business rules.
