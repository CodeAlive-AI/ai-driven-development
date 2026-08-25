# Validation record

Release: `apple-app-store-reviewer` 1.2.0
Policy baseline: 2026-08-25
Validation environment: macOS, Python 3.14, no release Xcode execution

## Executed checks

| Check | Command | Result |
|---|---|---|
| Skill package contract | `python3 scripts/validate_skill.py .` | PASS; no errors or warnings |
| Python syntax | `python3 -m compileall -q scripts tests assets/ai-adapter.example.py` | PASS |
| CLI startup | Every Python entry point under `scripts/` invoked with `--help` | PASS |
| Regression suite | `python3 -m unittest discover -s tests -p 'test_*.py' -v` | PASS; 11/11 tests |
| AI adapter contracts | `python3 scripts/run_ai_safety_suite.py --command ./assets/ai-adapter.example.py --output <temp>/ai-full.json` | PASS; 27 deterministic passes, 0 failures, 0 execution errors |
| AI semantic queue | Same AI run | 10 cases correctly remained `NEEDS_REVIEW`; no deterministic pass was fabricated |
| Orchestrator gate | Covered by `test_orchestrator_is_fail_closed_and_report_validates` | PASS; missing release evidence produces `NOT READY`, and the report validates |
| Screenshot evidence integrity | Covered by screenshot/evidence regression tests | PASS; exact image dimensions and hashes accepted, stale or incomplete visual evidence rejected |
| Source heuristics | Covered by the deliberately bad Swift/plist/privacy-manifest fixture | PASS; direct and heuristic findings emitted separately |
| Capacitor 8.5 overlay | Covered by safe and unsafe Capacitor fixtures | PASS; version, config, UIScene, plugin privacy, and live-update findings distinguish valid release evidence from unsafe configuration |
| Capacitor release-integrity contract | Covered by reference/schema regression checks | PASS; qualified range, safe config handling, source/native/archive parity, four-stage plugin inventory, and fail-closed live-update evidence are mandatory |
| Community-signal contract | Covered by source-catalog and community-reference regression checks | PASS; X posts and vendor claims remain low reliability and cannot create policy or universal requirements |
| Policy freshness logic | `python3 scripts/check_policy_freshness.py --network ...` | Correctly `UNVERIFIED`: this container could not resolve external hosts, so the checker failed closed |

## What was not executed here

A Linux container cannot perform the Apple-toolchain checks. The following must be run on the exact release candidate from a macOS host with the intended Xcode version:

- simulator boot/install/launch and screenshot capture;
- XCUITest reviewer journeys;
- archive export and installation tests;
- `codesign`, entitlements, provisioning, architecture, `otool`, embedded-framework, and notarization checks;
- real-device paths such as camera, microphone, Bluetooth, location, notifications, StoreKit, Sign in with Apple, background execution, and limited/offline conditions.

The live policy checker also requires controlled outbound network access. Independent research used to construct the pinned baseline was completed on 2026-08-25, but the package intentionally does not convert that build-time research into a future release-time `PASS`.

## Gate semantics verified

- A mandatory check cannot pass without explicit evidence.
- A passed visual check requires a complete scope declaration and SHA-256 matches for the reviewed originals.
- A passed AI adapter check does not imply semantic output safety or age-rating correctness.
- Community reports cannot create an Apple policy violation; they can only trigger a targeted investigation.
- A newer official guideline date or an unreachable required policy source prevents `READY FOR SUBMISSION` in strict mode.
- Report validation detects contradictory gates, duplicate check identifiers, secret-shaped material, and unsupported pass states.
