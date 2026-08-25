# Community and commercial-review signals — observed through 2026-08-26

These signals are deliberately separated from policy. They are anecdotal, selection-biased, and may omit facts from private App Review correspondence. They may add a test or evidence request; they cannot create a blocker unless an official rule and direct app evidence support it.

## Reliability labels

- **Medium:** Apple Developer Forums thread with detailed rejection text/evidence, but still developer-reported unless Apple staff confirms.
- **Low:** Reddit, X, blog, marketing page, or commercial-tool claim.
- **Operational only:** review queue timing/status reports; never score compliance from them.

## Recent recurring signals

### AI/photo/face data disclosure questions — medium

Developer forum reports describe reviewers asking for exact explanations of face/photo data collection, purpose, storage, retention, deletion, third-party sharing, and privacy-policy wording. Some reports also describe questions about whether screenshots match the current app and how the app makes money.

Use:

- Add a face/photo data-flow questionnaire.
- Capture consent before provider transmission.
- Add provider/retention/deletion detail to reviewer notes.
- Reconcile screenshot build and business model.

Authority remains Guidelines 2.3 and 5.1 plus current privacy/AI requirements.

### Third-party AI recipient and denial state — medium/low

Forum and X commentary reports rejection where a consent screen did not identify what was shared or the third-party AI recipient, or where AI remained active after denial.

Use:

- Test named recipient, data categories, purpose, timing, denial, withdrawal, and network ledger.
- Do not require wording copied from a post.

Authority remains current Guideline 5.1.2.

### Minimum functionality for links, feeds, and thin wrappers — low

Recent Reddit and X posts describe repeated 4.2/4.3 rejections for apps characterized as links, images, aggregated internet content, generic AI concepts, or one-screen prompt forwarders. Similar advice stresses useful workflows and differentiation beyond a website or chat box.

Use:

- Trigger the native-value dossier.
- Compare actual native workflows with a simple website.
- Test offline/device integration, original content/rights, durable utility, and differentiation.
- Compare sibling iOS/macOS apps and template-generated variants for duplicated concepts, metadata, and storefront presentation.

Do not state that all WebViews or AI wrappers are rejected, that every app is formally reviewed under 4.3 in the same way, or that adding screens/settings/offline behavior automatically “clears” review. Guidelines 4.2 and 4.3 remain fact-dependent; direct product evidence controls the finding.

### Release completeness and reviewer-path defects — low

X reports attribute rejections to defects visible in the submitted build: missing ATT prompts, incomplete subscription records, duplicate promotional images, misleading custom permission pre-prompts, premium state accidentally enabled for review, unclear HealthKit use, name mismatches, placeholder content, broken flows, and paywalls without restore/privacy/terms paths.

Use:

- Run the reviewer journey from a clean install with production flags and an ordinary reviewer account.
- Reconcile bundle/display/store names, paywall disclosures, IAP promotional images, permissions, HealthKit presentation, and App Store Connect product state.
- Test that custom pre-prompts do not impersonate the system decision or pre-commit the user to “Allow.”
- Fail the release on observed defects; never infer prevalence from social-media compilations.

Authority remains Guidelines 2.1, 2.3, 3.1, 5.1, current HIG/privacy guidance, and direct release evidence.

### Guideline 2.1 information-request package — low/operational

Several August 2026 X posts describe first submissions receiving requests for a physical-device screen recording, tested device/OS list, external-service inventory, IAP flow, feature purpose, and exact access instructions. The reports do not establish a universal new submission requirement.

Use:

- Prepare a concise real-device recording of the main reviewer journey when the app is new, hardware-dependent, AI-backed, or otherwise difficult to reproduce.
- Record tested devices/OS versions, external services, purchase paths, demo access, and feature navigation in review notes or attachments.
- Treat a 2.1 information request as a request for evidence unless Apple also identifies a substantive defect.

Do not fabricate a recording requirement or treat the absence of a video as an automatic violation. Current App Store Connect review-information requirements and the actual resolution-center message control.

### Generative content, advertising, and hidden behavior — low

X reports and amplified news coverage describe generative-image apps removed after reviewers or investigators observed nudification, explicit output, or advertising that promoted capabilities not candidly represented during review.

Use:

- Test the worst reasonably reachable output, jailbreaks, shared/public output, and age-rating impact.
- Reconcile ads, landing pages, social promotion, screenshots, review notes, feature flags, and production behavior with the submitted binary.
- Require filtering, reporting, blocking, escalation, and abuse-response evidence appropriate to the product.
- Never hide a remotely enabled or policy-sensitive feature from review.

Authority remains current safety, metadata, UGC, age-rating, and developer-conduct requirements. Community reports cannot prove why a particular app or account was removed.

### IAP submission and subscription clarity — medium/low

Apple forum and X reports mention products not attached/submitted with the app version, missing EULA/terms links, and unclear subscription benefits.

Use:

- Require App Store Connect product status/version attachment evidence.
- Run Sandbox load/purchase/restore/manage tests.
- Cross-check duration, price, trial, renewal/commitment, benefit, privacy, and EULA.

Authority remains Guidelines 2.1 and 3.1 plus App Store Connect product requirements.

### Privacy-manifest and screenshot mismatch — low

Community reports continue to mention privacy manifests, required-reason API declarations, and screenshots that do not reflect the reviewed binary.

Use:

- Inspect the final archive and aggregate privacy report.
- Hash the final screenshot set and compare against runtime.
- Treat static package-name detection as a lead, not proof.

### Review delays — operational only

Multiple forum posts reported prolonged `Waiting for Review` periods in August 2026. This does not indicate compliance, rejection risk, or a reliable expected duration.

Use only for release planning. Do not promise review times or recommend duplicate/manipulative submissions.

### Storefront-specific AI metadata — low

An X post promoting an open-source preflight tool mentions China-specific AI terminology checks alongside privacy manifests, unused entitlements, and subscription pricing. The post does not supply an authoritative banned-term list.

Use only to trigger a current storefront/legal review of metadata, licensing, model availability, data residency, and local declarations. Do not ship or maintain a blacklist derived from a social post; require current official terms or qualified legal evidence.

### Capacitor submission and packaging reports — low

Ionic Forum reports describe privacy-manifest failures becoming visible during full submission even when TestFlight appeared usable, especially in older Capacitor/Cordova/Firebase plugin chains. Maintainer discussion discourages loading an external website as the production app, and a 2026 Capacitor 9 alpha issue reports nested-framework and duplicate-bundle-ID upload failures while describing 8.5.0 as unaffected.

Use these only to trigger final-archive manifest inspection, final bundled-origin checks, and framework-neutral nested-bundle/duplicate-identifier validation. They do not establish a Capacitor-specific Apple rule. No reliable current X report in the supplied assessment was strong enough to encode; preserve that evidence scarcity instead of inventing consensus.

## Commercial tools reviewed as product-pattern references

Public descriptions of Rork Reviewer, App Store Preflight, AcceptMyApp, NoReject AI, and similar tools emphasize combinations of code scan, metadata review, screenshots, API/privacy checks, live App Store Connect data, guided fixes, or CI integration. Reported rejection percentages, benchmark accuracy, or approval-rate improvements are vendor/developer claims unless an independently reproducible dataset and protocol are supplied. Their public marketing does not expose Apple's internal review process and should not be treated as validation.

This skill deliberately adds:

- Fail-closed evidence gates rather than an unexplained approval score.
- Final-bundle and runtime branches, not only source/metadata.
- Explicit screenshot capture plus deterministic and semantic review.
- Third-party AI consent/data-flow and safety test suite.
- Claim consistency across binary, runtime, metadata, privacy, age, and payments.
- Policy freshness fingerprints and source confidence labels.
- Reproducible report schema, hashes, remediation, and re-verification.

## Signal-handling rule

For every community-derived concern, record:

1. Source, observation date, and reliability.
2. The official rule potentially implicated.
3. A falsifiable app-specific test.
4. Direct evidence and result.
5. Whether the signal was confirmed, disproved, or remains uncertain.

Never cite “developers say” as the rationale for a blocker.

The maintained URLs and observations are in `references/source-catalog.json` and `references/source-index.md`.
