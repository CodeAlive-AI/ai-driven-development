---
name: apple-app-store-reviewer
description: Audit Apple-platform apps before App Store submission or resubmission. Use for iOS, iPadOS, macOS, tvOS, watchOS, and visionOS release reviews involving source code, archives or IPAs, App Store Connect metadata, screenshots, subscriptions, login, privacy manifests, AI features, UGC, age ratings, review notes, or an Apple rejection. Produces evidence-backed findings, deterministic preflight results, screenshot review queues, runtime test plans, remediation steps, and a submission-readiness gate.
license: MIT
compatibility: Python 3.11+ for deterministic checks; Pillow recommended for screenshot analysis; macOS with Xcode is required for simulator capture, XCUITest, codesign, otool, and complete archive inspection. Network access is optional and must be explicitly enabled.
metadata:
  version: "1.2.0"
  policy-baseline: "2026-08-25"
  apple-guidelines-last-updated: "2026-06-08"
---

# Apple App Store Reviewer

Simulate a skeptical App Review team using reproducible evidence. Review the exact release candidate, not a development branch or mock build. The objective is to remove every observable rejection trigger before submission; Apple makes the final decision, so never promise approval.

## Non-negotiable rules

1. Treat current Apple documentation as authoritative. Use community reports only as weak signals for reviewer behavior, never as policy.
2. Run `scripts/check_policy_freshness.py --network` when current network access is permitted. If the official guideline update date is newer than this skill's baseline, stop the readiness decision, refresh the policy references, and label the review `POLICY STALE`.
3. Never mark a check `PASS` unless the relevant artifact or runtime path was actually observed. Missing evidence is `SKIPPED` or `NEEDS_REVIEW`, not a pass.
4. Do not upload source, archives, screenshots, prompts, credentials, or user data to third parties without explicit permission. The bundled scripts are local-first and read-only.
5. Use release configuration, production-like backend settings, a fresh install, and reviewer-safe demo credentials. Scrub secrets from reports.
6. Distinguish direct violations from heuristics. A deterministic mismatch can be a `BLOCKER`; a source-code signal that needs context is normally `HIGH` or `MEDIUM` with `NEEDS_REVIEW`.
7. Do not infer legal compliance. Require licenses, regulatory approvals, terms, or counsel confirmation as evidence when a regulated branch applies.

## Evidence to request or locate

Create an evidence manifest before reviewing. Prefer all of the following:

- Release source tree and lockfiles.
- For Capacitor apps: `package.json`, the authoritative resolved lockfile, `capacitor.config.*`, post-sync iOS project, generated and bundled Capacitor config, source/native/final web-asset trees, `Package.resolved` or `Podfile.lock`, final plugin/privacy inventory, and trusted `cap doctor` / `cap ls ios` output when available.
- `.xcarchive`, exported `.app`, or `.ipa` built for submission.
- `review-input.json` based on `assets/review-input.example.json`.
- App Store Connect metadata export or `metadata.json` per locale.
- Final screenshots grouped by locale and device family.
- App Privacy answers, `PrivacyInfo.xcprivacy`, entitlements, and Info.plist files.
- In-App Purchase and subscription records, including review screenshots and submission status.
- A non-expiring demo account or approved full-featured demo mode.
- Review notes, privacy policy, terms/EULA, support page, and any regulatory evidence.
- For AI: provider/data-flow map, consent copy, retention/training settings, safety policy, age-rating rationale, and test adapter if available.

Record absent artifacts explicitly. Do not delay a useful partial audit, but the final gate cannot be `READY FOR SUBMISSION` while mandatory evidence is absent.

## Core procedure

### 1. Establish scope and policy freshness

Read `references/policy-baseline.md`. Determine:

- Platforms and device families actually enabled by the binary.
- New app versus update, storefronts, locales, category, age target, and release date.
- Business model and whether value is digital, physical, person-to-person, enterprise, reader, or multiplatform.
- Feature branches: account creation, social login, AI, UGC/chat, creator content, subscriptions, ads/tracking, sensitive permissions, health, finance, kids, gambling, crypto, VPN/MDM, browsers, remote desktop, extensions, mini apps, or regulated services.

Run:

```bash
python3 scripts/check_policy_freshness.py --output review-output/policy.json
# Add --network only when network access is permitted.
```

The August 25, 2026 baseline expects App Review Guidelines last updated June 8, 2026 and the Xcode 26 / platform SDK 26 upload minimum effective April 28, 2026. September 2026 social-media age-rating questions are a near-term warning until their effective date.

### 2. Validate intake and run deterministic preflight

Copy and complete `assets/review-input.example.json`. Keep reviewer passwords in environment variables, not committed JSON.

```bash
python3 scripts/review_app.py \
  --config review-input.json \
  --output-dir review-output
```

For a release gate, rerun on macOS with the final archive and use `--network` only for URL and policy checks:

```bash
python3 scripts/review_app.py \
  --config review-input.json \
  --output-dir review-output \
  --network \
  --strict
```

Inspect every script diagnostic. `TOOL_UNAVAILABLE` means the associated check is unverified; it is not a failure by itself, but may prevent a ready gate.

### 3. Review deterministic findings

The orchestrator checks, when artifacts are available:

- Metadata lengths, required URLs, placeholders, keywords, demo access, IAP records, and subscription disclosures.
- Source/config signals for permissions, privacy, accounts, login, purchases, AI providers, UGC controls, web-wrapper risk, staging code, secrets, tracking, private APIs, and dynamic code.
- Capacitor release-line alignment, production configuration, plugin privacy requirements, live-update signals, and the Capacitor 8.5 UIScene migration.
- Bundle identity, versions, SDK/Xcode metadata, device families, usage descriptions, ATS settings, privacy manifests, listed third-party SDK manifests, architectures, signatures, entitlements, and linked frameworks.
- Screenshot file count, exact accepted dimensions, transparency, duplicates, blank/title-card signals, locale/device coverage, and contact-sheet creation.
- URL reachability and basic content only when `--network` is explicitly enabled.

Reproduce each `BLOCKER` before reporting it. Downgrade false-positive heuristics and explain why.

### 4. Take and visually evaluate screenshots

When macOS/Xcode and a simulator build are available, create a capture plan from `assets/capture-plan.example.json`, then run:

```bash
python3 scripts/capture_simulator.py \
  --app path/to/App.app \
  --bundle-id com.example.app \
  --plan capture-plan.json \
  --output-dir review-output/captured-screenshots \
  --normalize-status-bar
```

Capture the core journey, purchase screens, permissions, AI consent, account deletion, error/empty states, and any path mentioned in metadata. For paths not reachable by deep link, use an XCUITest based on `assets/AppReviewUITests.swift` and then inspect the generated images.

Run deterministic image checks:

```bash
python3 scripts/inspect_screenshots.py \
  --screenshots review-output/captured-screenshots \
  --config review-input.json \
  --output review-output/screenshots.json \
  --contact-sheets review-output/contact-sheets
```

Then use vision to inspect each original image and each contact sheet. Read `references/screenshot-review.md`. Evaluate actual app use, current UI, device/locale consistency, clipped or untranslated text, real personal data, misleading claims, prices and trials, other-platform branding, objectionable content, fake system UI, login/splash-only sets, and feature claims not reproducible in the build. Do not use OCR as the default substitute for visual inspection.

### 5. Execute the reviewer journey

Read `references/runtime-review.md`. Test on a clean install and, where relevant, an upgrade install:

1. Cold launch on the newest shipping OS and supported hardware classes; repeat with no network, slow network, denied permissions, revoked permissions, and backend errors.
2. Reach useful functionality without unnecessary registration. Exercise account creation, login/logout, credential recovery, social login, and in-app account deletion.
3. Buy, cancel, upgrade/downgrade, restore, and re-open every IAP/subscription path in Sandbox. Confirm products are separately submitted and visible to review.
4. Verify deep links, universal links, notifications, background behavior, extensions, widgets, camera/microphone/location flows, external hardware, and orientation/multitasking where declared.
5. Compare every reviewer-visible fact with metadata, privacy answers, screenshots, age rating, review notes, and the production backend.
6. Save reproducible evidence: exact steps, device/OS, build number, timestamps, screenshots, logs, crash reports, and expected versus actual behavior.

For detected or declared Capacitor apps, read `references/capacitor-ios.md` and `references/capacitor-release-integrity.md`. The qualified line is `>=8.5.0 <9.0.0`; a future major is `FRAMEWORK BASELINE UNVERIFIED` until requalified. Also test cold and warm custom URLs, universal links, `App.getLaunchUrl()`, `appUrlOpen`, JavaScript `pause`/`resume`, bundled-asset launch with the development host unavailable, native plugin denial/revocation, bridge isolation, upgrade storage, and applicable live-update rollback. Missing source/generated/submitted parity evidence prevents a ready gate.

Run configured XCUITests with:

```bash
python3 scripts/run_xcode_tests.py --config review-input.json --output-dir review-output/runtime
```

### 6. Apply the AI overlay

If the app uses AI, read `references/ai-review.md` and `references/privacy-security.md`.

Required review:

- Map every user/device datum from collection to app, backend, model provider, subprocessors, logs, training, retention, deletion, and output destination.
- If personal data is sent to a third-party AI, verify an informed explicit-permission event occurs before the first transmission. The disclosure must identify the data categories, recipient/provider, purpose, and relevant retention or training behavior; privacy-policy text alone is not a conservative substitute.
- Confirm denial leaves the app in a coherent state and that consent can be withdrawn where applicable.
- Verify App Privacy answers and the privacy policy match actual provider SDK/server behavior.
- Review whether the app is a chatbot or offers software not embedded in the binary under Guideline 4.7, including filtering, reporting, blocking, per-instance permission sharing, indexing, universal links, IAP, and age restrictions where applicable.
- Assess the worst reasonably reachable AI output for age rating and content safety. Do not rate only intended prompts.
- For medical, legal, financial, employment, education, insurance, or other high-impact outputs, require bounded claims, qualified human oversight, escalation, and applicable licenses. A disclaimer does not cure unsafe functionality.
- If using Apple's Foundation Models framework, apply the current acceptable-use requirements and preserve platform safeguards.
- Check AI transparency, user control, feedback/correction, provenance, hallucination handling, prompt injection, data exfiltration, cross-user leakage, output sharing, abuse reporting, and rate/age controls.

Generate or execute the bundled deterministic safety suite:

```bash
python3 scripts/run_ai_safety_suite.py \
  --suite assets/ai-safety-test-cases.json \
  --emit review-output/ai-prompts.jsonl

# Optional local adapter: receives one JSON object on stdin and returns JSON.
python3 scripts/run_ai_safety_suite.py \
  --suite assets/ai-safety-test-cases.json \
  --command ./assets/ai-adapter.example.py \
  --output review-output/ai-results.json
```

The runner checks response contracts when possible; semantic safety remains a manual/agent review. Never send production personal data in red-team prompts.

### 7. Apply app-type and storefront branches

Read `references/app-type-branches.md` for every matched feature. Read `references/business-payments.md` for any monetization or external purchase path. Do not assume the United States external-link treatment applies to other storefronts. For regional entitlements, licenses, age assurance, or local-law declarations, verify the exact storefront and current official terms.

For low-value, template-generated, web-wrapper, aggregator, or saturated-category risk, require a concrete “native value dossier”:

- Unique user problem and target audience.
- Native capabilities and workflows unavailable from a simple website.
- Original content/data rights and meaningful differentiation from existing apps.
- Retention/utility evidence, offline or device integration where relevant.
- A reviewer note that points to these features without marketing exaggeration.

This is mandatory when Guideline 4.2 or 4.3 risk is plausible, including many thin AI wrappers.

For a Capacitor project, apply `references/capacitor-ios.md` in addition to the ordinary WebView/minimum-functionality branch. Treat Capacitor as a native runtime architecture, not an automatic 4.2 violation. Require evidence of useful app behavior, correct bridge boundaries, synchronized bundled assets, and release-safe native configuration.

### 8. Cross-consistency review

Build a claim matrix with rows for each material feature/data/payment claim and columns for:

- Binary/source behavior.
- Runtime observation.
- App Store description and promotional text.
- Screenshots/previews.
- App Privacy answers and privacy policy.
- Age rating.
- IAP/subscription records and paywall.
- Review notes and demo account.

Any material contradiction is at least `HIGH`; a directly misleading price, hidden feature, broken URL, or undisclosed data flow can be a `BLOCKER`.

### 9. Report, fix, and re-verify

Use the report schema in `assets/review-report.schema.json`. Every finding must contain:

- Stable ID, status, severity, confidence, category, and guideline.
- Exact evidence with file/path/screen/steps.
- Why Apple may reject it.
- Minimal safe fix plus any product-level alternative.
- Deterministic or manual verification steps.
- Official source; community source only when labeled as anecdotal.

Gate rules:

- `NOT READY`: one or more open `BLOCKER` findings.
- `CONDITIONALLY READY`: no blockers, but open `HIGH` findings, mandatory `NEEDS_REVIEW` items, stale policy, or missing release evidence.
- `READY FOR SUBMISSION`: no open blocker/high findings, all mandatory paths observed, policy current, and report validation passes.

After fixes, rerun only affected checks first, then rerun the complete release audit. Validate the report:

```bash
python3 scripts/validate_report.py review-output/report.json --strict
```

Draft App Review notes from `assets/review-notes-template.md`. Include exact navigation, demo credentials via secure delivery, unusual business-model explanation, AI provider/consent path, IAP locations, hardware requirements, and attachments. Never hide a feature from review.

Before distributing or materially changing the skill itself, run:

```bash
python3 scripts/validate_skill.py .
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Use `evals/evals.json` for isolated with-skill versus baseline agent evaluations after policy or workflow changes.

## Severity calibration

- `BLOCKER`: current, directly applicable requirement is observably unmet; upload/review is expected to fail or the app presents material safety/legal risk.
- `HIGH`: strong rejection likelihood but context or runtime confirmation is still needed.
- `MEDIUM`: reviewer friction, quality issue, or plausible policy concern.
- `LOW`: quality hardening or weak community signal.
- `INFO`: verified fact or non-actionable context.

Confidence is separate from severity. Use `CERTAIN` only for direct evidence, `HIGH` for strong deterministic inference, `MEDIUM` for contextual inference, and `LOW` for anecdotal or weak heuristics.

## Progressive references

- Read `references/policy-baseline.md` on every review.
- Read `references/rule-matrix.md` to map evidence to Apple guideline sections.
- Read `references/screenshot-review.md` whenever screenshots or previews exist.
- Read `references/runtime-review.md` before manual or simulator testing.
- Read `references/ai-review.md` for any AI/ML, generated content, chatbot, or Foundation Models feature.
- Read `references/privacy-security.md` for any data collection, permissions, tracking, third-party SDK, or account feature.
- Read `references/business-payments.md` for purchases, subscriptions, credits, external links, physical goods, services, or reader apps.
- Read `references/app-type-branches.md` for specialized categories and regional/storefront branches.
- Read `references/community-signals.md` only after official-policy review; use it to add tests, not rules.
- Read `references/reviewer-notes-and-appeals.md` when drafting notes, responding to rejection, or deciding fix versus appeal.
- Read `references/capacitor-ios.md` whenever `@capacitor/ios`, `capacitor.config.*`, `CAPBridgeViewController`, or a Capacitor/Cordova bridge is present.
- Read `references/capacitor-release-integrity.md` for every detected or declared Capacitor app; it defines safe inspection, source/generated/submitted parity, dependency/plugin contracts, required checks, and gate semantics.
- Read `references/capacitor-live-updates.md` only when an OTA/live-update package, remote web bundle, asset-path switcher, or custom update bootstrap is detected.
- Use `references/source-index.md` and `references/source-catalog.json` to refresh the baseline.

## Output package

Return or save:

1. `report.json` and `report.md`.
2. Evidence manifest and tool/skipped-check inventory.
3. Screenshot findings, visual-review queue, and contact sheets.
4. AI safety prompts/results and manual semantic verdicts when applicable.
5. Claim-consistency matrix.
6. Prioritized remediation plan with verification commands.
7. Reviewer journey log and final App Review notes draft.
8. Final gate with explicit limitations; never state that approval is guaranteed.
