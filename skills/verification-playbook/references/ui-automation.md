# UI automation: permanent component, browser and e2e tests

Read when writing a permanent test that drives a user interface. For a one-off pass through a
running build, read `exploratory-qa.md` instead.

## Contents

- [Choose the smallest UI environment](#choose-the-smallest-ui-environment)
- [Act like the user](#act-like-the-user)
- [Wait for outcomes](#wait-for-outcomes)
- [End in a meaningful observation](#end-in-a-meaningful-observation)
- [Name what is substituted](#name-what-is-substituted)
- [Isolation and diagnosis](#isolation-and-diagnosis)
- [Visual comparison](#visual-comparison)

## Choose the smallest UI environment

| Risk | Environment |
|---|---|
| Form logic, validation messages, handler wiring | Component test with the real UI tree and controlled network responses |
| Layout, focus, browser APIs, cookies, downloads, navigation | A real browser |
| Assembly of the whole chain | A few selected e2e routes |

UI and e2e are not synonyms. A browser test of a component with a stubbed API is a component
test. Keep the e2e set to the routes where wiring is the risk, and never push the combinations of
a domain rule through it.

## Act like the user

- Drive the interface through input, selection, clicks and navigation, and observe the result.
  Calling a handler directly does not show that it is connected to the button.
- **Locators:** role and accessible name first, a stable test id second. A long CSS path or a node
  index needs a specific justification. Do not put runtime identifiers into test ids: keep the id
  static and expose the entity in a separate attribute.
- **Typing:** when input handling is the risk, type key by key through real user events, and
  assert both the value and that focus is retained. Setting the value directly skips the handlers.
  Direct setting is fine for paste, autofill and native pickers.
- **Ambiguity:** two visible controls with the same accessible name are a defect in the UI or in
  the test. Resolve it. Do not pick the first match.

## Wait for outcomes

- Automatic waiting before an action confirms that the action is possible. It does not confirm
  that the business operation finished. Assert the result separately after the action.
- Wait for an observable state or event, with a timeout chosen for that operation. A fixed pause
  confirms only that time passed. "Network idle" is not a business outcome.
- A negative assertion ("no request was sent", "nothing changed") is meaningful only after the
  moment at which the effect would have appeared. Wait for the next observable state first.

## End in a meaningful observation

| Scenario | Not enough | Observe instead, by risk |
|---|---|---|
| Saving a form | The modal closed | The value after a fresh read or reopening |
| Download | The button exists | The content of the file |
| Placing an order | A success toast | The identifier and status of the order, and no duplicate |
| Deleting | The row disappeared | The object is gone after a reload, and related data is intact |

## Name what is substituted

- A stubbed backend makes the result "frontend with a stubbed API". Say so in the test name or
  its description.
- A replaced payment service means the scenario covers the application chain up to that boundary
  and not the real charge.
- Network stubs fail on unhandled requests, so a missing stub is visible. Assert UI outcomes, not
  "a request was made", unless the request is the contract.
- A stub that answers with the final state at once hides polling and loading defects. Give it the
  lifecycle the UI must wait through.

## Isolation and diagnosis

- Each test creates its own data under unique names and does not depend on test order or on a
  database reset.
- Use isolated browser state per test, and prepared authentication state instead of logging in
  through the UI every time, unless login is the subject.
- Diagnose from traces, network logs and server logs. Do not guess from the picture.
- A pass after a retry is reported as flaky, not as passed. See `flaky-and-brittle.md`.

## Visual comparison

Screenshots and visual regression serve layout and visual changes. They do not replace functional
assertions. Apply them to selected stable states, and control fonts, viewport size, data,
animations and time. Updating a baseline requires looking at the diff and a reason why the new
look matches the task.
