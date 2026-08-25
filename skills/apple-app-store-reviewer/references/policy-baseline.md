# Policy baseline — 2026-08-25

This file is the mandatory policy entry point for every review. It identifies the pinned Apple requirements, the authority hierarchy, the freshness gate, and the limits of the skill.

## Baseline status

- Review date: **August 25, 2026**.
- App Review Guidelines page: **Last Updated June 8, 2026**.
- Upload toolchain minimum in force since **April 28, 2026**: Xcode 26 or later and the applicable version 26 platform SDK for iOS, iPadOS, tvOS, visionOS, and watchOS submissions.
- Updated age-rating system is in force for current platforms: 4+, 9+, 13+, 16+, 18+, plus regional variants and Unrated for distribution methods where permitted. Updated questions have been required for submissions since January 31, 2026.
- App Store Connect added social-media capability questions on July 9, 2026. Answers can be supplied now and become required for new apps, updates, and alternative-distribution notarization beginning in **September 2026**.
- Guideline 5.1.2 requires clear disclosure and explicit permission before personal data is shared with third parties, including third-party AI.

The policy freshness script is authoritative for the skill's own readiness:

```bash
python3 scripts/check_policy_freshness.py \
  --catalog references/source-catalog.json \
  --network \
  --output review-output/policy.json
```

A newer observed guideline date, an altered required-page fingerprint, or an unreviewed submission requirement blocks a `READY FOR SUBMISSION` gate. A failed fetch is not proof of a policy change; it is an unverified gate.

## Authority hierarchy

Use sources in this order:

1. Applicable law, court order, regulator requirement, Apple Developer Program License Agreement, paid-app agreement, entitlement terms, and regional addenda.
2. App Review Guidelines and App Store Connect submission/help requirements.
3. Apple platform documentation, Human Interface Guidelines, privacy-manifest and SDK-signature requirements, Foundation Models acceptable-use requirements, StoreKit documentation, and entitlement-specific terms.
4. Direct App Review correspondence for the exact app/build. It may clarify the observed problem but does not silently supersede published rules.
5. Apple Developer Forums posts from Apple staff, when clearly identified.
6. Developer reports on forums, Reddit, X, blogs, and commercial reviewer tools. These are testing signals only.

Never convert a community anecdote into an Apple rule. Use it to create a scenario, collect evidence, or improve reviewer notes.

## Review boundary

This skill is an evidence-driven preflight, not Apple, a law firm, a regulator, or a security certification. It cannot guarantee approval because:

- Some judgments are discretionary, especially minimum functionality, copycat/spam, user value, content suitability, and misleading presentation.
- App Review can exercise paths or backend states not reproduced locally.
- Storefront rules, entitlements, agreements, and laws can differ.
- The submitted binary and App Store Connect records can change after the audit.
- Apple may update policy after the pinned date.

The gate therefore states only whether the supplied evidence satisfies this skill's current tests.

## Mandatory 2026 release facts

### Build and upload

Verify the final archive, not only build settings:

- Xcode and platform SDK meet the current upload minimum.
- Bundle identifier, marketing version, build number, supported platforms, device families, minimum OS, and entitlements match App Store Connect.
- Release configuration has no staging endpoints, debug menus, test credentials, development-only entitlements, private frameworks, unsupported architectures, embedded quarantine attributes, or unsigned/re-signed listed binary SDKs.
- Required-reason APIs are declared with current approved reason identifiers for the app and embedded dependencies.
- Listed third-party SDKs include required privacy manifests; binary dependencies meet signature requirements.

### Completeness and access

Treat these as release blockers until demonstrated:

- No crashes, dead buttons, placeholder content, broken links, missing backend data, unavailable IAP, or nonfunctional login on a clean install.
- App Review can access all material features through a non-expiring account, approved demo mode, hardware instructions, or other documented path.
- Review notes identify non-obvious navigation, special configuration, regional behavior, hardware, and purchases.
- New features and products are visible and reviewable in the exact submitted build.

### Accurate metadata

The product page must describe the actual build and current service:

- Screenshots show the app in use and are not only title cards, ads, mockups, or unavailable future functionality.
- Claims, prices, trials, subscriptions, AI capabilities, supported devices, and external services are reproducible.
- No unrelated keywords, protected names, imitation of Apple UI/branding, unverifiable superlatives, or third-party content without rights.
- Support and privacy URLs are public, stable, app-specific, and usable without credentials.

### Safety, content, and age rating

Review intended and reasonably reachable content:

- UGC/social features have filtering, reporting, blocking, support contact, timely moderation, and age controls where required.
- AI output is rated by the worst reasonably reachable result, not only curated prompts.
- Medical, financial, legal, safety, emergency, weapons, gambling, and other high-risk claims receive the applicable specialist branch.
- Kids Category and minor-data restrictions are applied independently of the ordinary age rating.
- Social-media capability questions are answered consistently before their September 2026 enforcement date.

### Privacy and AI

Build a complete data-flow inventory:

- Collection, local processing, backend, third parties, AI providers, subprocessors, analytics, logs, training, retention, deletion, export, and public sharing.
- Purpose strings, just-in-time disclosures, permissions, App Privacy answers, privacy policy, consent records, provider settings, and actual network behavior agree.
- Personal data is not sent to a third-party AI before a clear disclosure and explicit permission event.
- The disclosure identifies the relevant data, recipient/provider, purpose, and material retention/training behavior. Denial must not trigger the transmission.
- Account deletion is offered in the app when account creation is supported; deletion scope and timing are explained.

### Business model

Classify value before deciding payment rules:

- Digital goods/features consumed in the app normally use In-App Purchase unless a current, documented exception or storefront entitlement applies.
- Physical goods/services, qualifying person-to-person services, enterprise-only services, reader/multiplatform exceptions, and external-purchase-link treatment are tested separately.
- Every IAP/subscription is submitted, available in Sandbox, visible to review, correctly localized, and consistent with the paywall and metadata.
- Restore, entitlement, billing retry, grace period, cancellation, upgrade/downgrade, refund, family sharing, and account transitions are tested as applicable.

## Policy refresh protocol

When a source fingerprint changes:

1. Save the old and new page snapshots or a textual diff where permitted.
2. Identify the effective date, affected storefronts/platforms, transition period, and whether it applies to new apps, updates, or existing apps.
3. Update `references/source-catalog.json`, this baseline, `references/rule-matrix.md`, the relevant focused reference, catalogs, schemas, scripts, fixtures, and evals.
4. Add at least one failing fixture for the new rule and one compliant fixture.
5. Run the full test suite and a real-app dry run.
6. Change `POLICY_BASELINE` and `GUIDELINES_LAST_UPDATED` only after reconciliation.
7. Record assumptions and unresolved ambiguity. Never silently repin a date.

## Primary official sources

- App Review Guidelines: `https://developer.apple.com/app-store/review/guidelines/`
- Upcoming Requirements: `https://developer.apple.com/news/upcoming-requirements/`
- App Store Connect Help: `https://developer.apple.com/help/app-store-connect/`
- Screenshot specifications: `https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications`
- Age rating values: `https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions/`
- Third-party SDK requirements: `https://developer.apple.com/support/third-party-SDK-requirements/`
- Required-reason APIs: `https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api`
- Account deletion: `https://developer.apple.com/support/offering-account-deletion-in-your-app/`
- Generative AI HIG: `https://developer.apple.com/design/human-interface-guidelines/generative-ai`
- Foundation Models acceptable use: `https://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework/`

Use `references/source-index.md` for the complete maintained source map.
