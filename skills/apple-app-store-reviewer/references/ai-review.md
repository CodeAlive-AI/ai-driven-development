# AI feature review

Load this reference whenever AI, machine learning, generated content, chat, summarization, recommendation, image/audio/video generation, agentic action, Apple Foundation Models, or a third-party model provider is present.

## First classify the AI system

Record each AI feature separately:

- User-visible versus background/internal.
- Deterministic ML versus generative model.
- On-device Apple framework, app-owned model, first-party backend, or third-party provider.
- Input data categories and whether any are personal, sensitive, child-related, biometric, health, financial, precise location, contacts, communications, files, or credentials.
- Output destination: private to user, saved to account, shared with collaborators, public UGC, acts on external systems, or controls hardware.
- Domain risk: ordinary productivity, social/UGC, medical, legal, financial, education, employment, housing, insurance, identity, emergency, weapons, gambling, or child-facing.
- Autonomy: draft-only, recommendation, user-confirmed action, or automatic action.
- Provider training/retention/logging, subprocessors, region, and deletion controls.

A single app may require multiple rows because a local classifier and a third-party chatbot have different obligations.

## Mandatory AI evidence pack

Require:

1. Data-flow diagram from collection to deletion.
2. Provider and model inventory, SDK/server version, endpoint region, subprocessors, and contract/settings evidence.
3. Exact pre-transmission consent UI and denial path for personal data sent to third-party AI.
4. Privacy policy and App Privacy answers mapped to observed behavior.
5. System/developer prompt policy or equivalent safety configuration, redacted where proprietary.
6. Input/output moderation architecture and provider failover behavior.
7. Synthetic deterministic adapter results from `scripts/run_ai_safety_suite.py`.
8. Manual semantic review of the selected cases and worst reasonably reachable outputs.
9. Age-rating rationale covering generated and publicly shared content.
10. Deletion, export, consent withdrawal, and account deletion test evidence.
11. Human-oversight and escalation design for high-impact domains.
12. Review notes with exact feature navigation, consent sequence, sample prompts, and provider identity.

## Third-party AI personal-data consent gate

Treat this as a release-critical path when personal data leaves the app/developer boundary for a third-party AI.

### Passing sequence

1. User initiates or enables the AI feature.
2. Before any personal data is transmitted, the app presents a clear disclosure.
3. The disclosure explains, in context:
   - what relevant data categories will be sent;
   - the named recipient/provider or sufficiently specific third party;
   - why the data is sent and what output is produced;
   - material retention, logging, or training behavior, or a clear route to those details;
   - whether the feature is optional and what happens after denial.
4. User takes an affirmative opt-in action. Pre-checked controls, bundled consent, a policy link alone, or use before disclosure are not conservative passes.
5. A recorded consent state gates the actual network request.
6. Denial sends no covered data and leaves a coherent non-AI or local path where feasible.
7. Withdrawal prevents future covered transmissions and explains already-processed data/deletion.

### Deterministic verification

Use a test provider, proxy, URLProtocol, Network Extension test harness, server request ledger, or provider audit log. Verify:

- zero covered requests before consent;
- zero covered requests after denial or withdrawal;
- only disclosed fields after consent;
- no hidden analytics/crash payload containing prompts, images, file names, or model output;
- consent version/provider changes trigger a new decision when material;
- multiple accounts do not share consent state incorrectly;
- reinstall, logout, and device restore behavior is intentional.

Do not mark `PASS` based only on the existence of a consent screen.

## App Review content classification

### Guideline 1 safety overlay

Review model outputs against objectionable-content and physical-harm rules. Test both ordinary and adversarial prompts. Include indirect prompt injection from documents, webpages, images, tool results, or retrieved memory.

Minimum categories:

- Sexual content and exploitation, including minors.
- Graphic violence, threats, weapons acquisition/use, and dangerous instructions.
- Hate, harassment, objectification, bullying, and anonymous abuse.
- Self-harm, suicide, eating-disorder encouragement, and crisis escalation.
- Medical diagnosis/treatment, legal advice, financial decisions, and emergency claims.
- Doxxing, identity data, biometric inference, face data, stalking, and precise location.
- Fraud, phishing, impersonation, credential theft, malware, and evasion.
- Copyright/trademark replication, unauthorized living-person impersonation, and misleading provenance.
- Hallucinated facts presented as verified, fake device/system states, and deceptive claims.

A provider refusal is not automatically a pass. Check whether it reveals disallowed information, can be bypassed, or fails in a way that exposes another user's data.

### UGC and public output

AI output becomes UGC-like when users publish, remix, comment on, discover, or message it. Apply filtering, report, block, contact, moderation, and age controls. Review abuse of image/avatar generators against real-person objectification and impersonation risks.

### Guideline 4.7 overlay

Apply the software-offered-in-app branch when the app offers chatbots, mini apps, plug-ins, HTML5 experiences, or other software not embedded in the binary. Verify the current rule elements, including software index/universal links where applicable, content controls, per-instance permission sharing, IAP, age identification/restriction, and isolation from native APIs.

Do not assume every single AI API call is a 4.7 software catalog. Record why the branch applies or does not apply.

### Guideline 4.2/4.3 overlay

A thin prompt box around a general model has elevated minimum-functionality and spam risk. Require a native-value dossier showing:

- a specific problem and audience;
- proprietary or licensed workflow/data, not merely model access;
- native interaction and durable utility;
- differentiated safety, collaboration, offline/device integration, or domain expertise;
- meaningful behavior when the model is unavailable;
- differentiation from the developer's other apps and common templates.

This is a discretionary risk review; do not label a thin wrapper an automatic formal violation without evidence.

## High-impact domain controls

For medical, legal, financial, employment, education admissions, housing, insurance, identity, or safety-critical use:

- Define the decision boundary: information, draft, recommendation, or final decision.
- Prevent unsupported claims of professional qualification, diagnosis, certainty, or guaranteed outcome.
- Show source quality, freshness, uncertainty, and material limitations in context.
- Require qualified human review before consequential action.
- Provide escalation to emergency/professional services where appropriate.
- Test protected-class proxies, disparate treatment, prompt manipulation, and incomplete data.
- Preserve an auditable user-visible record for consequential actions where lawful.
- Require applicable legal entity, license, regulatory, or clinical evidence.

A disclaimer alone does not make unsafe functionality acceptable.

## Foundation Models framework

When using Apple's Foundation Models framework:

- Confirm the feature and prompts comply with Apple's current acceptable-use requirements.
- Preserve framework safeguards; do not intentionally route around them.
- Handle model availability, eligibility, locale, device support, and refusal states.
- Do not claim on-device privacy for data that is also sent to another backend/provider.
- Test fallback behavior and disclose material provider changes.
- Verify age rating and App Review safety independently; use of an Apple framework is not automatic approval.

## AI HIG review

Assess:

- Transparency: users understand when AI is involved and what it can/cannot do.
- Control: users initiate consequential actions and can review/cancel/correct results.
- Feedback: easy reporting/correction for poor or harmful output.
- Attribution/provenance: generated or transformed content is not misleading.
- Graceful failure: refusal, no-network, model unavailable, rate limit, and timeout states remain useful.
- Trust calibration: avoid false certainty, human-like deception, and unsupported performance claims.
- Privacy: show disclosure at the point of data use, not buried in onboarding.

## Deterministic suite contract

`run_ai_safety_suite.py` passes one JSON case to a local adapter on stdin. The adapter returns one JSON object. See `assets/ai-adapter.example.py`.

Typical response fields:

```json
{
  "action": "allow|refuse|safe_complete|escalate|require_confirmation|error",
  "output": "redacted test output",
  "sent_to_provider": false,
  "provider": "ExampleProvider",
  "data_categories_sent": [],
  "consent_state": "not_required|not_asked|denied|granted|withdrawn",
  "stored": false,
  "shared_publicly": false,
  "human_review_required": false
}
```

Deterministic contracts validate state and data-flow assertions. The semantic queue still requires a model-capable reviewer or human to inspect meaning, dangerous detail, age suitability, and bypassability.

## Required runtime cases

At minimum, test:

- First AI use before consent, decline, accept, withdraw, provider/model change.
- Logged-out and logged-in use; account switch; child/minimum-age account where applicable.
- Prompt plus photo/file/audio input; metadata/EXIF/file-name leakage.
- Adversarial document/web retrieval and tool output prompt injection.
- Cross-user memory, conversation export, deletion, and support/admin views.
- Provider timeout, safety refusal, malformed response, rate limit, no network, and failover.
- Public sharing/report/block/moderation where output can be published.
- High-impact recommendation and confirmation boundary.
- Worst-case content for age rating.

Record the request ledger or equivalent evidence for consent/data tests. Screenshots alone cannot prove that data was not sent.

## AI release blockers

Examples that normally justify `BLOCKER` or `HIGH` pending confirmation:

- Personal data sent to a third-party AI before explicit permission.
- Consent describes “AI partners” but code sends sensitive data to an unnamed provider and the user cannot understand the recipient/use.
- Denial UI exists but transmission still occurs.
- Cross-account or cross-user prompt/output leakage.
- Public AI output without applicable UGC controls.
- High-impact automatic action without meaningful human confirmation/oversight.
- Misleading on-device/private claims contradicted by network behavior.
- App Privacy/policy omits prompts, uploads, provider sharing, retention, or training.
- Child data sent to a disallowed third party or unsafe child-facing generative experience.
- Review build cannot reproduce the advertised AI feature.

## Reviewer-note minimum

State:

- Where AI appears and exact taps.
- Provider(s), on-device/server split, and data categories sent.
- Exact consent path and how to test decline/accept/withdraw.
- Sample safe prompts and any feature flag or region requirement.
- Whether outputs can be public and how moderation/report/block works.
- High-impact limits and human-review boundary.
- Account/data deletion path and provider-retention behavior.

Never conceal a provider or feature from App Review.
