# Capacitor 8.5 release-integrity gate

Load this reference whenever Capacitor is declared or detected from source, native state, or the submitted bundle. It defines the evidence required beyond the source-level heuristics in `scan_project.py`.

> Capacitor presence is an architecture fact, not evidence of a thin wrapper. Guideline 4.2 conclusions require product and runtime evidence.

## Qualification and activation

- Qualified range: `>=8.5.0 <9.0.0`.
- Below 8.5: report `CAP-VERSION-BELOW-8_5` as a framework-baseline failure, not an invented Apple rule.
- At or above 9.0: report `CAP-VERSION-UNVERIFIED-NEWER` and `FRAMEWORK BASELINE UNVERIFIED` until the new major is requalified.
- Auto-detect independently from `@capacitor/core` / `ios` / `cli`, `capacitor.config.*`, generated iOS resources, `CAPBridgeViewController`, Capacitor/Cordova frameworks, bridge resources, and bundled configuration.
- Archive-only detection activates the branch. An input that disables the branch while evidence proves Capacitor is present is `CAP-FRAMEWORK-CONFIG-CONFLICT`.
- Missing source, native, or submitted evidence may still produce a partial audit, but it prevents `READY FOR SUBMISSION`.

Keep framework configuration in an optional top-level `frameworks.capacitor` intake object, not in Apple app-type features. Use conservative defaults: `mode=auto`, `trusted_cli=false`, package manager and native-project policy `auto`, live updates disabled unless detected.

## Evidence precedence

When evidence conflicts, use this order:

1. Exact submitted `.app`, `.ipa`, or `.xcarchive`.
2. Generated native state used to build it.
3. Lockfile-resolved dependencies.
4. Source configuration and declarations.
5. Runtime observations, tied to the exact build.
6. Current official Capacitor documentation.
7. Community reports, only to generate scenarios.

Do not let a clean source config override a bundled `server.url`, or a package declaration prove that a plugin or privacy manifest reached the archive.

## Safe inspection contract

- Read `capacitor.config.json` exactly.
- Treat `.ts` and `.js` configs as executable. Use bounded static extraction of literal objects only; never import, `require`, transpile, or execute them by default.
- Do not run package lifecycle scripts, download packages with `npx`, or scan all of `node_modules`.
- A trusted mode may invoke only the project-local CLI, with argument arrays and no shell, inside a disposable copy. Prefer `node_modules/.bin/cap`; if `npx` is unavoidable, require `--no-install`.
- Never run `cap sync` in the user's working tree. Record executable, arguments, working directory, exit status, and output hashes.
- Bound plugin inspection to installed plugin metadata, native source, manifests, podspecs, `Package.swift`, and embedded artifacts.

## Three-state parity matrix

Build SHA-256 manifests and compare source, generated native, and submitted states:

| Contract | Source | Generated native | Submitted bundle |
|---|---|---|---|
| Config | `capacitor.config.*` | generated config | bundled config |
| Web assets | configured `webDir` | copied iOS `public` | final `.app/public` |
| Plugins | declared/resolved packages | SPM/Pods/generated integration | frameworks/resources |
| Privacy | app/plugin manifests | Xcode resources | final app/SDK manifests |
| Identity | `appId` / `appName` | Xcode settings/plists | final `Info.plist` |
| Origin | source environment | generated config | bundled config/runtime |

Record relative path, size, SHA-256, and type for every material file. Distinguish exact match, documented generated difference, and unexplained drift. Do not suppress all generated files with a broad ignore list.

Mandatory failures include missing `webDir`/`index.html`, missing referenced local assets, zero-byte critical assets, unresolved placeholders, staging/LAN/localhost origins, secret-shaped values, unexplained source maps, remote bootstrap code, and source/native or native/bundle drift. A weak CSP is a security finding, not automatically an Apple violation.

## Version and toolchain resolution

Resolve versions from the authoritative lockfile first, then installed package metadata, declarations, and final framework metadata. A range such as `^8.5.0` is not resolved evidence.

Require:

- aligned resolved Core, iOS, and CLI versions;
- compatible official plugin majors/peer ranges;
- one authoritative npm, pnpm, Yarn, or Bun lockfile unless a documented monorepo explains more;
- Node 22+, Xcode 26+, and iOS deployment target 15+ for the qualified Capacitor 8 line;
- policy freshness checked separately from framework freshness.

A newer Capacitor release alone does not make an older supported app noncompliant. Recheck official v8 docs, 8.0/8.5 upgrade guides, config, workflow, iOS/SPM, privacy, security, deep links, deployment, support policy, and release metadata when the framework baseline fingerprint changes.

## Configuration surface

Inspect source, generated, and bundled values for `appId`, `appName`, `webDir`, all `server.*` origin/start/error/navigation fields, scheme/hostname, logging, web debugging, included plugins, app-bound domains, notification handling, preferred content mode, `CapacitorHttp`, `CapacitorCookies`, Cordova origins, and experimental SPM settings.

- A final undocumented remote `server.url` is normally a blocker; source-only evidence is HIGH pending the archive.
- Cleartext, wildcard navigation, or an untrusted origin with privileged bridge access can be blockers.
- Reconcile `limitsNavigationsToAppBoundDomains` with final `WKAppBoundDomains`.
- Test browser/app handoff and prove unexpected origins cannot invoke privileged plugins.

## Plugin and dependency-manager contract

Build four plugin inventories: declared, lockfile-resolved, natively integrated, and finally embedded. For every official, community, Cordova, or custom plugin, record version, JS calls, native source inspected, permissions/purpose strings, capabilities/entitlements, required-reason APIs, App Privacy candidates, network/AI data flow, SPM support, final manifests/resources, and required runtime tests.

A catalog is only a starting hypothesis. Unknown plugins require manual review, not automatic failure. Never copy sample required-reason codes without matching actual use.

For SPM, inspect generated `CapApp-SPM/Package.swift`, `Package.resolved`, plugin dependencies, sync warnings, manual edits to generated state, and final products. For CocoaPods, inspect `Podfile`, `Podfile.lock`, workspace/project references, plugin compatibility, final products, and manifests. Flag mixed/stale SPM/Pods state and declared/resolved/integrated/embedded drift.

Inspect the entire final app tree for nested frameworks/bundles and duplicate `CFBundleIdentifier` values. These are generic upload invariants, not a rule against Capacitor 8.5.

## UIScene 8.5 state machine

Score four static signals: SceneDelegate exists; target membership; scene manifest registration; AppDelegate configuration hook/equivalent.

- `0/4` intentional legacy on Xcode 26: INFO/future readiness, not an Apple blocker by itself.
- `1–3/4` partial: HIGH; callbacks may be split or stranded.
- `4/4` complete: inspect custom code and require runtime proof.

Audit proxy forwarding, custom AppDelegate URL/universal-link and foreground/background code, custom bridge view controllers, removed temporary-window APIs, notification handling, cold/warm custom URLs, universal links, `getLaunchUrl`, `appUrlOpen`, pause/resume, and process death.

## Runtime, visual, and AI evidence

Tie every observation to exact build/hash, OS, device/simulator, timestamp, logs, screenshot, and expected/actual result. Exercise online/offline fresh launch, bridge/plugin smoke, background/resume, cold/warm links, universal links, denial and later revocation, external navigation, keyboard/safe areas, iPad resize/orientation, upgrade storage migration, backend failure, purchase/restore, and account deletion.

Capture screenshots from the exact native WKWebView release candidate, not a desktop responsive emulator. Check bars/safe areas, keyboard, permission ordering, StoreKit/plugin UI, iPad layout, errors, stale splash/white flash/blank frames, and feature parity with final web-asset hashes.

For AI, trace browser `fetch`/XHR, backend, `CapacitorHttp`, and native-plugin paths. Join camera/photo/file/location/contact/clipboard/microphone access to privacy labels, named-provider consent, retention/deletion, and network evidence. Consent denial/withdrawal must yield zero covered provider transmissions across every enabled network stack. Never embed provider secrets in the web bundle or expose the bridge to an untrusted remote origin.

## Mandatory check inventory

When detected, require evidence for:

```text
capacitor.detection
capacitor.version-resolution
capacitor.version-alignment
capacitor.tested-range
capacitor.toolchain
capacitor.config-source-native-parity
capacitor.config-native-bundle-parity
capacitor.web-assets-source-native-parity
capacitor.web-assets-native-bundle-parity
capacitor.local-runtime-origin
capacitor.plugin-inventory
capacitor.plugin-native-resolution
capacitor.plugin-permission-contracts
capacitor.plugin-privacy-contracts
capacitor.package-manager-state
capacitor.uiscene-state
capacitor.runtime-bridge
capacitor.runtime-lifecycle
capacitor.runtime-deep-links
capacitor.runtime-offline-startup
```

Conditionally require plugin permissions, notifications, purchases, AI network consent, and live-update policy/integrity/rollback. A ready gate requires every applicable mandatory check. A parity `PASS` must name paths and hashes; plugin-privacy `PASS` must name resolved plugins and final manifests. Source-only evidence cannot pass final parity.

## CI and review notes

Use a frozen JS install and production build with Node 22. Run project-local `cap doctor` / `cap ls ios` without downloads. Copy the repository to a disposable workspace, sync only there, fail on unexplained committed-native diff, resolve SPM/Pods deterministically, archive with Xcode 26+, then inspect the exact exported app and run generic plus Capacitor runtime tests. Never mutate the original checkout during review.

Reviewer notes should explain the hybrid architecture, bundled origin, build/sync identity, external services, plugin purposes, deep-link access, live-update boundary if any, and attach tested device/OS plus physical-device recording for difficult-to-reproduce paths when useful. Do not imply that a video is universally required.

## Apple mapping and severity

- Missing/stale assets, bridge or link failures: 2.1.
- Screenshot/build mismatch: 2.3.
- Custom native plugin/public API evidence: 2.5.1.
- Remote boot/runtime or downloaded functionality: 2.5.2; assess 4.7 only when the model actually applies.
- Digital web checkout/unlock: 3.1.
- Repackaged website established by product/runtime evidence: 4.2.
- Login equivalence: 4.8.
- Listed SDK/plugin privacy and AI data: third-party SDK requirements, 5.1.1, 5.1.2.

Severity follows evidence stage. Source hints are not equivalent to final bundled proof; final evidence is not downgraded because source appears clean. Community and vendor claims can add tests only.
