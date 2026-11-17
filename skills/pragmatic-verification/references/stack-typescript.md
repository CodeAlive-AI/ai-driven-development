# TypeScript and JavaScript tooling

Read when the stack at hand is TypeScript or JavaScript, in the browser or on Node. The
repository's existing tools win. These are defaults for a role that nothing fills yet.

| Role | Common choice | Notes |
|---|---|---|
| Runner and case tables | Vitest or Jest, `test.each` | Use the one already configured |
| Component tests | Testing Library | `getByRole` first; `userEvent`, not `fireEvent`, for typing |
| Network stubbing | MSW | Set `onUnhandledRequest: 'error'`; model multi-stage lifecycles |
| Property-based | fast-check | Constrain arbitraries rather than filter |
| Browser and e2e | Playwright | Role locators and auto-retrying assertions; see `ui-automation.md` |
| Real database and services | Testcontainers for Node, or services the repository provides | Real migrations, isolated data |
| Time | Fake timers of the runner, an injected clock | Set `TZ` before the process starts: Node caches the zone |
| API contract | Pact JS, OpenAPI validation | Message compatibility is not behaviour |
| Sensitivity probe | StrykerJS scoped with `--mutate` to changed files | Run only related tests per mutant, or it runs the whole suite each time |
| Static | `tsc --noEmit`, ESLint | A type check is not a behaviour test |

## Traps

- **Vacuous assertions:** `[].every(…)` is `true`, and `items.forEach(i => expect(…))` asserts
  nothing on an empty array. Assert the length first.
- **Floating promises:** an unawaited `expect(promise).resolves…` passes before it runs. Await it,
  enable the `no-floating-promises` lint rule, or use `expect.assertions(n)`.
- **Swallowed errors:** a rejected promise or a throwing handler can be hidden by polling. Await a
  settled state and assert that no unhandled error was captured.
- **Simulated DOM limits:** jsdom and similar environments have no layout, no real focus movement
  and no computed colours. Move a check to a real browser when the risk is layout, focus,
  scrolling or contrast.
- **Typing:** in Playwright use `pressSequentially` when input handling is the risk, and `fill`
  for paste, autofill and native pickers.
- **Waiting:** no `waitForTimeout` and no `networkidle` as a business signal. Wait for the element
  or the state that shows the outcome.
- **Label matching:** when one label is a prefix of another, match exactly.
- **Stub fidelity:** a handler that returns the final status on the first request hides a missing
  polling loop. Give it the pending states.
- **Retries:** a test that passes on retry is flaky. Keep a trace of the first failure.
- **Mocked modules:** mocking the module under test, or its immediate collaborators inside the
  same feature, leaves a test in which only mocks run.
- **Snapshots:** large component snapshots pin markup nobody promised. Keep them small, or assert
  the roles and the text.
