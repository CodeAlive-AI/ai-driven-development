# App Review notes, rejection response, and appeal procedure

Good notes reduce ambiguity; they do not excuse a broken build or hide noncompliance. Use `assets/review-notes-template.md` and replace every placeholder.

## Submission notes content

Include only information that helps review the exact build:

- App name, version/build, relevant storefronts and feature flags.
- Non-expiring demo account delivery method and role. Never paste credentials into reusable artifacts.
- Exact tap-by-tap path to every non-obvious material feature.
- AI provider, on-device/server split, consent decline/accept/withdraw path, sample prompts, and public-output controls.
- IAP/subscription product IDs and exact paywall/restore/manage path.
- Account deletion path and expected completion behavior.
- Hardware, region, entitlement, VPN/MDM, regulated, or backend setup.
- Explanation for features that are intentionally unavailable to the demo account or a storefront.
- Attachments: short screen recording, license, authorization, methodology, or data-flow diagram where useful.
- Contact who can respond promptly and understands the implementation.

Avoid marketing copy, legal conclusions without evidence, hostility, irrelevant history, and instructions that require the reviewer to contact support before using the app.

## AI note example structure

```text
AI feature: Project > Add source > Generate summary.
Provider/data: User-entered text and the selected document are sent to [provider] only after the disclosure shown on first use. No request is sent after Decline; this can be observed in the attached request-ledger recording.
Consent test: Decline on first launch, retry Generate, then Settings > Privacy > AI Processing > Allow.
Retention/training: [precise behavior and control].
Sample prompt: [safe reproducible prompt].
Deletion: Settings > Account > Delete Account; provider-side deletion behavior: [precise behavior].
```

Do not claim “anonymous” or “not retained” unless it is technically and contractually supported.

## Responding to a rejection

### 1. Preserve evidence

Save:

- Rejection message, guideline section, screenshots/attachments, timestamp, version/build, review device/OS if shown.
- Submitted binary/archive hash, metadata, screenshots, App Privacy, IAP records, review notes, backend/feature flags, and demo account state.
- Relevant logs without personal data/secrets.

Do not modify the backend or metadata before preserving the reviewed state unless safety requires immediate action; otherwise the root cause becomes harder to prove.

### 2. Reproduce the reviewer path

Translate the message into exact hypotheses. Reproduce on a clean install using the stated device/OS and reviewer account. Test adjacent states because the visible symptom may be downstream of login, network, product status, or feature flag.

### 3. Decide fix, clarify, or appeal

**Fix** when direct evidence shows noncompliance, broken behavior, unclear UI, missing product, misleading metadata, or inadequate notes.

**Clarify** when the build is compliant but the reviewer could not reach/understand it. Supply concise navigation and objective evidence, not a debate.

**Appeal** when:

- the cited rule appears factually inapplicable;
- the review relies on an incorrect app fact;
- inconsistent decisions persist after clear evidence/fix;
- a novel/discretionary issue needs App Review Board interpretation.

A fix and an appeal can coexist when the fix improves clarity without conceding an incorrect rule interpretation. State what changed and what principle remains disputed.

### 4. Draft the response

Use this structure:

1. Acknowledge the cited section and observed concern.
2. State the exact build and reproduced result.
3. State the fix or factual clarification.
4. Give exact navigation and attach concise evidence.
5. Ask one precise question only if ambiguity remains.

Example:

```text
We reviewed build 104 under Guideline 5.1.2. In the previous build, the AI disclosure appeared after the user selected a document. Build 105 now presents the disclosure before any document bytes or metadata are sent, identifies [provider], lists the data categories and purpose, and leaves the feature disabled after Decline. Navigation: Projects > New > Add document > Generate. The attached recording includes a request ledger showing zero provider requests before opt-in. Please review build 105.
```

Do not accuse the reviewer, cite Reddit as authority, threaten publicity, or flood the thread with multiple speculative explanations.

## Recurring rejection control

Repeated rejection for the same section requires a root-cause dossier:

- Timeline of builds and changes.
- Exact App Review messages.
- Rule elements and app facts.
- Reproduction results for each hypothesis.
- Before/after screenshots and logs.
- Remaining ambiguity.

Escalate to appeal only with a coherent record. Repeatedly resubmitting unchanged builds can increase scrutiny and delay.

## After approval

Archive the evidence package and monitor:

- Backend/config/provider changes.
- New SDKs/data flows.
- StoreKit product/price changes.
- User reports/refunds/moderation.
- Policy and regional changes.
- Screenshot/metadata drift.

Approval of one build does not certify future versions or server behavior.
