# Exploratory QA through browser, computer or phone use

Read when planning or doing a check of a running build through its real interface. At plan time,
write the charter; run it once the build exists.

## Contents

- [When a pass is needed](#when-a-pass-is-needed)
- [Charter](#charter)
- [Before acting](#before-acting)
- [While acting](#while-acting)
- [Scenario catalogue by trigger](#scenario-catalogue-by-trigger)
- [Surfaces and their limits](#surfaces-and-their-limits)
- [What each observation proves](#what-each-observation-proves)
- [From a finding to a permanent test](#from-a-finding-to-a-permanent-test)
- [Reporting a finding](#reporting-a-finding)
- [Checking the checker](#checking-the-checker)

## When a pass is needed

Run one when a user-facing path changed, when the risk lives in the UI, the OS or the device, or
when the wiring of the whole chain is in question. A cosmetic edit needs one look at the affected
spot, not a pass through the catalogue.

Browser use, computer use and phone use are ways to execute a scenario. They do not change what
counts as an oracle. A screenshot, a successful click and a finished tool call are not a completed
business operation.

## Charter

Give the pass a question to answer:

> Explore X under conditions Y to find out risk Z.

Example: "Explore draft saving after a lost connection and a restart, to find out whether typed
text can disappear or a duplicate can appear." The charter is narrow enough to know when the pass
is finished and free enough to change route when an anomaly appears, keeping the goal and
recording the finding.

```text
Explore:
Under conditions:
To find out the risk:
Revision and environment:
Initial state and role:
Expected result and forbidden effects, with their source:
Observations:
Problems found:
Boundaries not checked:
What to pin as a permanent test, at which level, and why:
```

## Before acting

1. Confirm that every live process runs the intended revision and that required migrations are
   applied.
2. Record the revision, environment, browser or device, account role, initial data and the source
   of the expected results.
3. Name the real and the substituted dependencies.
4. Use permitted test data with a clear cleanup. Real external effects stay within the authorised
   scope.
5. List the entry points: the feature route and every hub, list or search surface that shows it.

An independent pass receives the user goal, the accepted scenarios, known limitations, the build
address and revision, roles and prepared data. It does not need the author's account of why the
implementation is right. After the first pass, read the changes and probe the risks found there.

## While acting

- **Use user actions** for the material part of the route. API and database access serve setup and
  independent observation. They do not replace input through the UI when its availability to the
  user is what is being checked.
- **Observe before deciding.** After each material action look at the result. With coordinate
  control, act on a fresh screenshot.
- **Do not work around a problem** with a force-click, a hidden endpoint or a state change from
  the console and then report that the path works. A workaround is diagnosis and is described as
  diagnosis.
- **Uncertain result of a mutating action:** find out the state first. Pressing Create or Send
  again may produce a second effect. For an idempotency check the repeat is deliberate, with a
  stated expected number of objects.
- **Logs:** separate cumulative tool logs from the delta of one action before diagnosing duplicate
  requests.
- **Revise the sample.** A finding may show that another screen, role or state belongs in scope.

## Scenario catalogue by trigger

A catalogue of triggers. Run only the rows the change touches.

| Trigger | What to check through the interface |
|---|---|
| New user path | The normal entry point, reaching the goal, reopening the result |
| Saving data | A fresh read, the state on error, no false success |
| Form | Invalid data, a clear error, input preserved, correction |
| Asynchronous operation | Loading, success, error, and cancel or retry where supported |
| Authorization and roles | The allowed and the forbidden path, plus a direct request to the server |
| Navigation | Back and forward, refresh, deep link, expired session |
| Repeated action | Double press, repeat after a delay, the final state |
| Network | Loss and recovery of the connection when it threatens the user's work |
| Responsive layout | Layout breakpoints, long text, zoom, on-screen keyboard |
| Desktop application | Keyboard, focus, dialogs, files, several windows |
| Mobile application | Background and return, interruption, permission denied, restore |
| Accessibility | The material path by keyboard and with assistive technology |

A hidden button is not protection. When the access contract changed, check the forbidden
operation with a direct request as another user and another role.

## Surfaces and their limits

- **Browser:** an emulated device is a set of settings: viewport, user agent, touch, locale,
  permissions. Its name does not mean the physical device was checked, and it has no native
  lifecycle. In a second supported engine, repeat only the scenarios sensitive to the changed
  browser mechanism.
- **Desktop and computer use:** keyboard-only operation, focus order, system dialogs, file
  pickers, several windows and OS permissions, as the feature requires.
- **Phone:** recreation of a screen is not the death of the process, so check the restore that
  matters. A simulator or emulator does not reproduce real performance or every hardware feature.
  Camera, push, Bluetooth, background work and speed need an environment that implements them.
  Debug or release build and fresh install or upgrade can change behaviour.
- **Accessibility:** an automatic audit finds certain classes of problem and does not show that a
  workflow is accessible. Walk the material path with the keyboard and the relevant assistive
  technology.
- **Platform matrix:** choose by supported configurations, usage data, the changed mechanism and
  defect history. Check the risks that differ, not the product of sizes, browsers, locales and
  roles.

## What each observation proves

| Observation | Confirms | Does not confirm |
|---|---|---|
| Screenshot | The look of one state | Saving, permissions, calculations |
| Click and UI transition | The reaction of the interface | Completion of background work |
| API response | The response in this scenario | All side effects |
| Page refresh | That the display is restored | Server storage: a local cache is possible |
| A fresh authoritative read | The stored state as observed | Every concurrent and failure mode |
| Unit test | The rule on the chosen inputs | Wiring, the real database, the experience |

For data that matters, keep the object identifier and read it again from the authoritative source.

## From a finding to a permanent test

Automate when the risk will return, the oracle is stable, the setup is reproducible and the upkeep
is justified. Extract the smallest test that keeps the mechanism: a wrong price comparison becomes
a unit test, a routing error an integration test, a focus or on-screen keyboard problem a test in
that UI environment. Do not save the whole click history. A one-off layout look, a diagnostic
workaround and a review of design variants can end in a report with no new permanent test.

When the pass finds a defect, name the earliest inner check that should have caught it. Fix the
defect, strengthen that check, re-run it, and re-run the product pass last.

## Reporting a finding

A remark is a candidate defect. It becomes a defect with a basis for the expected behaviour and a
reproducible discrepancy: revision, actual steps, expected and actual result, and the relevant
trace, screenshot, object or log. Surprising behaviour may be a reason to clarify the requirement,
not always a bug. Keep only the artefacts needed to check the conclusion, with no secrets or
personal data.

## Checking the checker

Before turning a QA agent into a standing procedure, show it several known-good and known-broken
variants. Check that it notices a lost save, an unwired action and a false success, that it does
not invent defects in acceptable behaviour, and that it neither explores shallowly nor explains
away the problems it finds. Repeat when the model, the tools or the material instructions change.
