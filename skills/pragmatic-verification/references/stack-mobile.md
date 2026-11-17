# iOS and Android tooling

Read when the change ships in a native or cross-platform mobile application. The repository's
existing tools win. These are defaults for a role that nothing fills yet.

| Role | iOS | Android |
|---|---|---|
| Logic tests | XCTest or Swift Testing | JUnit on the JVM; Robolectric when framework classes are involved |
| UI tests | XCUITest | Espresso or Compose UI testing |
| Stable locators | Accessibility identifiers | Test tags, content descriptions, resource ids |
| Lifecycle | Launch arguments, background and foreground through the test API | `ActivityScenario`: move through states and recreate |
| Waiting | Expectations and element existence with a timeout | Idling resources or wait-until conditions |
| Black-box flows | Maestro or Appium | Maestro or Appium |
| Accessibility | The built-in accessibility audit plus VoiceOver | Accessibility checks plus TalkBack |

## What each environment proves

| Environment | Good for | Does not prove |
|---|---|---|
| Emulated mobile viewport in a desktop browser | Responsive web layout | Anything about the native lifecycle or the real mobile browser |
| Simulator or emulator | Flows, layout, lifecycle transitions, most permissions | Real performance, thermal limits, camera, Bluetooth, some push and background behaviour |
| Physical device | Hardware features, real performance, release behaviour | Other devices, OS versions and screen classes |
| Debug build | Fast iteration | Release behaviour: optimization, code stripping, entitlements, and watchdog limits that a debugger relaxes |

## Scenarios that mobile adds

Pick the rows the change touches.

| Trigger | Scenario |
|---|---|
| State on a screen | Send the app to the background and return; recreate the screen; kill the process and restore |
| Input | The on-screen keyboard covers the field or the action; rotation; dynamic text size |
| Permissions | Denied, then granted in system settings; "ask every time" |
| Interruptions | An incoming call, a notification, the app switcher, low-power mode |
| Network | Loss in the middle of an operation, slow network, return of the connection |
| Entry points | Cold start and warm start from a deep link or a push notification |
| Upgrade | Install over the previous version with existing local data |

## Traps

- **Recreation is not process death.** Rotating or recreating a screen keeps the process. Restore
  after process death is a separate scenario and loses everything not persisted.
- **Fresh install only:** a migration of local data is exercised only by an upgrade from the
  previous version with real data in place.
- **Sleeps in UI tests:** wait for the element or the idle signal with a timeout.
- **Driving by coordinates:** act on a fresh screenshot, and keep device points and pixels apart.
  Prefer accessibility identifiers when the tool exposes them.
- **Shared device state:** permissions, keychain or keystore entries and local databases survive
  between runs. Reset them deliberately, or the second run tests a different state.
- **Automatic accessibility audit:** it finds certain classes of problem. Walk the material path
  with the screen reader as well.
