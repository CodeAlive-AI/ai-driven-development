# Capacitor iOS 8.5 review overlay

Apply this overlay whenever the release contains `@capacitor/ios`, `capacitor.config.*`, `CAPBridgeViewController`, or a Capacitor/Cordova bridge. Capacitor apps are native apps containing a privileged WKWebView and native plugin bridge. The architecture is not itself an App Review violation; review the exact release behavior and evidence.

This skill qualifies Capacitor `>=8.5.0 <9.0.0`. Versions below the requested baseline or at/above 9.0 cannot receive a framework-readiness pass; label a future major `FRAMEWORK BASELINE UNVERIFIED` until its final requirements and artifacts are requalified. Read `capacitor-release-integrity.md` for the mandatory evidence/gate contract and `capacitor-live-updates.md` when mutable remote assets are detected.

## Authoritative sources

- Capacitor v8 documentation: `https://capacitorjs.com/docs`
- Configuration schema: `https://capacitorjs.com/docs/config`
- iOS support and tooling: `https://capacitorjs.com/docs/ios`
- Capacitor 8.5 UIScene migration: `https://capacitorjs.com/docs/updating/8-5`
- iOS privacy manifests: `https://capacitorjs.com/docs/ios/privacy-manifest`
- Security guidance: `https://capacitorjs.com/docs/guides/security`
- Live reload: `https://capacitorjs.com/docs/guides/live-reload`
- Deploying updates: `https://capacitorjs.com/docs/guides/deploying-updates`

Use Capacitor documentation to interpret its runtime and configuration. Apple documentation and current App Review Guidelines remain authoritative for acceptance, privacy reasons, executable content, purchases, and metadata.

## Evidence inventory

Collect:

- `package.json` and the resolved npm/pnpm/yarn lockfile.
- Exact resolved versions of `@capacitor/core`, `@capacitor/ios`, `@capacitor/cli`, official plugins, community plugins, and Cordova plugins.
- `capacitor.config.ts`, `.js`, or `.json`, including environment-specific transforms.
- Generated `ios/` project after the final `npx cap sync ios`.
- Final archive, embedded frameworks/packages, `Info.plist`, entitlements, privacy manifests, and built web assets.
- Web-build commit/hash, `webDir`, CSP, source-map policy, and proof the archive contains the intended build.
- For remote updates: shipped and downloaded bundle hashes, signature/integrity scheme, channel, rollout, fallback, rollback, and server policy.
- Generated Capacitor config and copied native `public` tree, plus `Package.resolved` or `Podfile.lock` and the final embedded plugin/resource inventory.
- Exact Node, Xcode, deployment-target, device/OS, build, timestamps, runtime logs, screenshots, and expected/actual results.

Do not accept source declarations as proof of what was archived. Compare resolved dependencies and bundled assets with the final `.app`.

Never import, execute, or transpile `capacitor.config.ts` / `.js` during default inspection. Read JSON exactly and use bounded literal extraction only. A trusted CLI run may use only the project-local executable, without downloading packages or lifecycle scripts, inside a disposable copy; never run `cap sync` in the user's working tree.

## Release-line and sync checks

Require `@capacitor/core`, `@capacitor/ios`, and `@capacitor/cli` to resolve to a compatible supported release line. A declaration range alone is weaker than lockfile evidence.

After dependency, plugin, config, permission, or web-build changes:

1. Build the production web application.
2. Run `npx cap sync ios`.
3. Review the generated native diff; do not assume sync preserved custom native code.
4. Archive with the intended Release scheme and configuration.
5. Hash and compare the embedded web assets with the reviewed build.

Flag stale generated projects, missing plugins, unresolved Cordova dependencies, an absent `webDir`, or archive assets that do not match the production build.

## Capacitor 8.5 UIScene

Capacitor 8.5 introduces UIScene support required for Xcode 27. Check:

- `SceneDelegate.swift` exists and belongs to the app target.
- The delegate constructs the intended `CAPBridgeViewController` or custom subclass.
- `SceneDelegateProxy.shared` receives scene connection, custom URL, and universal-link callbacks.
- `UIApplicationSceneManifest` points at the intended delegate.
- AppDelegate provides `configurationForConnecting` and assigns `SceneDelegate.self`.
- Custom logic formerly in AppDelegate URL, universal-link, active/inactive, or foreground/background callbacks was moved to scene callbacks or supported notifications.
- Removed `tmpWindow`, `TmpViewController`, and related deprecated hooks are absent.

An entirely legacy project on Capacitor 8.5 is a migration warning, not automatically an App Store blocker while the selected Xcode still supports it. A partial scene migration that breaks launch, deep links, or lifecycle behavior can be HIGH. Verify both cold and warm links, process death, `App.getLaunchUrl()`, `appUrlOpen`, and JavaScript `pause`/`resume`.

## Production configuration

Inspect both source config and the config embedded into the archived app.

- `server.url`: development/live-reload only; remove from release.
- `server.cleartext`: do not use to support a production live-reload host.
- `server.allowNavigation`: Capacitor documents it as non-production. Remove it or require an exact, justified allowlist and a bridge-isolation test.
- `ios.webContentsDebuggingEnabled`: normally false for release.
- `loggingBehavior`: do not expose sensitive production console output.
- `ios.limitsNavigationsToAppBoundDomains`: when true, align `WKAppBoundDomains` with exact trusted domains and the Capacitor hostname, normally `localhost`.
- `server.hostname` and `iosScheme`: test secure-context APIs, routing, OAuth callbacks, universal links, and any migration-specific scheme behavior.

Treat a release that depends on a LAN/staging host as incomplete. Test launch while every development host is unavailable.

## Plugin, permission, and privacy matrix

Build one row per plugin:

`package + resolved version → native target/framework → protected resource → Info.plist usage text → capability/entitlement → required-reason API category/reason → collected data → App Privacy answer → runtime path`

Capacitor documents that plugins including Preferences and Filesystem may require app-level privacy-manifest reasons. The scanner can detect a missing category, but it must not invent the Apple-approved reason: select the truthful reason from current Apple documentation.

For community and Cordova plugins, inspect native source, embedded SDKs, manifests, signatures, network destinations, background modes, and maintenance status. A JavaScript import does not prove target membership; an npm dependency does not prove it is reachable in the release.

## WebView and bridge security

Review the WebView as a privileged boundary:

- Use a restrictive CSP appropriate to the shipped application.
- Do not place API secrets, signing keys, admin endpoints, or privileged credentials in JavaScript, environment substitutions, source maps, or bundled assets.
- Use PKCE for OAuth and prefer verified universal links over tokens in custom URL schemes.
- Keep session or encryption material in Keychain-backed storage rather than ordinary web storage or unprotected Preferences.
- Do not grant untrusted remote origins access to native plugins.
- Test cookies, `CapacitorHttp`, redirects, downloads, window opening, certificate failure, and navigation outside the allowlist.
- Reconcile plugin/server traffic with privacy disclosures, consent, deletion, and account isolation.

## Minimum functionality

Do not classify every Capacitor app as a thin wrapper. Evaluate observable value:

- durable workflows and useful functionality before payment/login where appropriate;
- native integrations that materially support the product;
- offline and failure behavior;
- original content/data rights and differentiation;
- accessibility, platform conventions, safe areas, keyboard behavior, iPad/window behavior, and performance;
- whether the same experience is merely a repackaged website or template.

Record plugin inventory as evidence, not as an automatic native-value pass. A camera or notification dependency that is unreachable does not establish meaningful functionality.

## Live updates and executable content

Capacitor/Appflow and third-party systems can update web assets remotely. Do not infer policy compliance from marketing language such as “app-store friendly.” Record:

- exact remotely mutable files and whether they can add features or materially change reviewed behavior;
- signature/integrity verification and transport security;
- channel selection, staged rollout, audit log, kill switch, bundled fallback, and rollback;
- prohibition on adding native executable code or undeclared native plugins remotely;
- version/build/web-bundle identifiers exposed in evidence and support diagnostics;
- App Review rationale under current Guidelines 2.5.2 and, when applicable, 4.7.

Reject a tampered update in testing. Disable the update service and prove the reviewed bundled release remains usable. A remotely delivered web bundle cannot compensate for an incomplete or misleading submitted binary.

## Gate effect

- Version mismatch, partial UIScene migration that breaks required behavior, development server dependency, broad privileged navigation, or missing applicable privacy declarations can be HIGH or BLOCKER depending on direct archive/runtime evidence.
- An unperformed 8.5 migration while using a still-compatible Xcode, a documented live-update mechanism awaiting runtime proof, or incomplete bridge-security evidence is normally `NEEDS_REVIEW` and prevents a ready gate.
- A ready verdict requires the exact archive, synchronized web assets, plugin/privacy reconciliation, complete reviewer journey, and current Apple policy evidence.
- Source-only checks named `source.capacitor.*` describe source risk only. They cannot establish generated-native or submitted-bundle parity and must never be promoted to a full Capacitor readiness pass.
