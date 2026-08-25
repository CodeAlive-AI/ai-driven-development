# Runtime reviewer journey

The runtime review must reproduce how a skeptical Apple reviewer reaches and evaluates the release build. A passing unit-test suite alone is insufficient.

## Test environment

Record:

- Archive/app hash, bundle ID, version, and build.
- Source commit and dependency lockfile hashes.
- Device/simulator model, OS build, locale, region, time zone, appearance, text size, orientation, and network state.
- Clean install versus upgrade install.
- Backend/environment identifier and feature-flag snapshot.
- Demo account identifier without placing its password in artifacts.
- Test timestamp and operator/agent.

Use current shipping OS versions and representative supported hardware. Add oldest supported OS and hardware for compatibility risk.

## Controlled Xcode execution

Configure `runtime.reviewer_journey_tests` with explicit Xcode test identifiers. `run_xcode_tests.py` converts each to a controlled `-only-testing:` argument and uses no shell.

```json
{
  "runtime": {
    "workspace": "./App.xcworkspace",
    "project": null,
    "scheme": "App",
    "destination": "platform=iOS Simulator,name=iPhone 17 Pro Max,OS=latest",
    "configuration": "Release",
    "reviewer_journey_tests": [
      "AppUITests/AppReviewUITests/testReviewerJourney",
      "AppUITests/AppReviewUITests/testAIConsentDeniedSendsNoData"
    ]
  }
}
```

Run:

```bash
python3 scripts/run_xcode_tests.py \
  --config review-input.json \
  --output-dir review-output/runtime
```

`runtime.reviewer-journey` may pass only when the controlled identifiers are nonempty and xcodebuild passes. Adapt `assets/AppReviewUITests.swift` to stable accessibility identifiers; do not rely on localized labels for navigation.

## Core clean-install journey

1. Install the exact release app and reset app/server test state.
2. Launch without preloaded credentials or hidden developer defaults.
3. Observe launch time, crash/hang, placeholder/loading behavior, permission timing, and whether useful value is reachable.
4. Follow every primary metadata/screenshot claim.
5. Exercise account and purchase flows.
6. Exercise denial, error, empty, and recovery states.
7. Background/foreground, terminate/relaunch, and repeat core state.
8. Save screenshots, logs, request ledgers, and xcresult.

## Access and account branch

For login-required apps:

- Verify a non-expiring reviewer account twice from fresh installs.
- Eliminate 2FA, email magic-link, invitation, organization approval, captcha, geographic, device-trust, or rate-limit barriers, or document an approved bypass.
- Ensure the account contains all data needed to reach material features.
- Test password reset/recovery where offered.
- Test social login plus the applicable equivalent privacy-preserving login/exception.
- Test logout, token revocation, account switch, and stale session.
- Test in-app account deletion from exact navigation. Confirm deletion scope, reauthentication, timing, subscriptions, retained legal records, third-party/provider data, and re-registration behavior.

Do not put plaintext reviewer credentials in JSON, logs, screenshots, or source. Use environment-variable references and secure App Store Connect delivery.

## Network and backend matrix

Test:

- Normal production-like service.
- Airplane/no network at launch and during a write/payment/AI request.
- Slow network, timeout, malformed response, 401/403, 404, 409, 429, and 5xx as relevant.
- TLS/certificate failure in a controlled environment.
- Empty/new account and large/long-lived account.
- Backend maintenance/feature disabled/provider unavailable.
- Retry idempotency, duplicate taps, and transaction reconciliation.

The app must not display raw stack traces, secrets, internal endpoints, or an indefinite spinner. Error messages must support recovery without misrepresenting completed actions.

## Capacitor 8.5 runtime matrix

When the release uses Capacitor, preserve evidence for both the native container and bundled web application:

- Launch with the configured development/live-reload host offline; the release must load its reviewed bundled assets.
- Exercise cold and warm custom URLs and universal links. Verify `App.getLaunchUrl()` and the `appUrlOpen` listener receive the intended route without exposing tokens.
- Background and foreground the exact scene repeatedly; verify JavaScript `pause` and `resume`, state persistence, media, timers, and protected-data behavior.
- Deny and revoke every native-plugin permission, then return through the WebView and confirm recovery UI and bridge errors remain coherent.
- Navigate to every external origin and prove untrusted content opens outside the privileged WebView or otherwise cannot call native plugins.
- Verify CSP, OAuth PKCE, cookie/session behavior, Keychain-backed token storage, and redaction of production JavaScript console output.
- Record the bundled web-asset hash. For live updates, also record the downloaded bundle hash, signature/integrity verdict, rollout, rejection of tampering, bundled fallback, and rollback.

For Capacitor 8.5 UIScene projects, explicitly test the release after process death and while already running. Missing proxy forwarding or custom AppDelegate behavior that was not moved to SceneDelegate can affect launch URLs, universal links, and lifecycle events differently.

## Permission matrix

For each declared protected resource:

- First use before authorization.
- Contextual pre-prompt and system prompt.
- Allow, limited access, one-time/approximate access where supported.
- Deny, revoke in Settings, and return to app.
- Not determined after reinstall.
- Device lacks resource or simulator returns no data.
- Data minimization path using picker/share sheet when possible.

Purpose strings must match the exact feature. The app must not force unrelated permission to obtain paid/core value.

## Commerce runtime matrix

For every submitted product:

- Product loads in Sandbox and is visible to reviewer.
- Price, duration, offer eligibility, trial, renewal, commitment, and benefits match App Store Connect.
- Buy, pending/Ask to Buy, cancel sheet, success, duplicate tap, interrupted purchase, and failed verification.
- Restore on clean install and a second device/account where applicable.
- Subscription upgrade, downgrade, crossgrade, expiration, grace period, billing retry, refund/revocation, and resubscribe.
- Manage subscription and customer support paths.
- App account deletion while an Apple subscription remains active.
- Server notification and entitlement reconciliation where used.

A successful local StoreKit configuration test does not prove the products were submitted and attached for App Review.

## AI runtime matrix

Follow `references/ai-review.md`. Runtime evidence must prove the consent-to-network contract, not only UI presence. Include provider request logs or a test interceptor.

Test:

- Consent not asked, denied, granted, withdrawn, and version/provider change.
- Prompt/upload with synthetic personal data.
- Hidden telemetry and crash logs.
- Provider timeout/refusal/malformed output/failover.
- Cross-user/account history and deletion.
- Public sharing/report/block if applicable.
- High-impact confirmation and human escalation.

## UGC/social runtime matrix

- Create/edit/delete content.
- Filter prohibited content before and after publication.
- Report content/user and observe acknowledgement.
- Block/unblock; verify visibility and messaging behavior.
- Moderator response/takedown in test environment.
- Ban evasion, anonymous/random chat, NSFW default, child account, age restriction.
- Social-media capability and age-question answers match behavior.

## Device/platform branches

- iPad multitasking, keyboard, pointer, rotation, and scalable layout.
- macOS sandbox, file access, menu/keyboard, window lifecycle, quarantine, helper/login items.
- tvOS remote-only core use unless controller requirement is disclosed.
- watchOS independence/paired behavior, complications, background limits.
- visionOS spatial layout, comfort, permissions, and controller/input behavior.
- Extensions/widgets: host app value, data sharing, revoked access, stale timeline, extension crash.
- External hardware: unavailable/disconnected/permission/firmware states and reviewer instructions.

## Upgrade review

For updates, test upgrade from the current App Store version with representative data:

- Schema/data migration and rollback/error handling.
- Authentication/session continuity.
- Subscription/entitlement continuity.
- Permission and consent changes, especially new AI provider/data use.
- Deleted/deprecated feature migration.
- Notification/deep-link compatibility.

A clean install pass does not cover migration risk.

## Evidence format

Runtime evidence should include checks and findings in the report-module contract. The mandatory exact ID is:

```json
{
  "id": "runtime.reviewer-journey",
  "title": "Clean-install reviewer journey and failure-state verification",
  "status": "PASS",
  "mandatory": true,
  "detail": "Exact build and controlled journey tests passed",
  "tool": "XCUITest + request ledger",
  "evidence": []
}
```

Populate evidence with real log/xcresult/screenshot locations and hashes. Do not submit a fabricated PASS object.
