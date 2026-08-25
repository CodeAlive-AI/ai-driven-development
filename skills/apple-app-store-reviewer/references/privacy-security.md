# Privacy, security, permissions, and accounts

Load this reference for any data collection, protected resource, tracking, account, SDK, analytics, advertising, AI provider, health/financial/biometric data, or user-generated content.

## Data inventory

Create one row for every data element, including inferred and generated data:

| Field | Required content |
|---|---|
| Data category | Exact field, payload, file, image/audio/video, identifier, prompt/output, metadata |
| Subject/source | User, contact, child, device, third party, public source, inference |
| Collection point | Screen/API/SDK/server/import |
| Purpose | Core feature, personalization, analytics, ads, fraud, support, legal |
| Required/optional | Consequence of denial |
| Processing | On-device, developer server, third party, AI provider |
| Recipients | Named provider/subprocessor/entity |
| Linked/tracking | App Privacy classification and ATT relevance |
| Retention | Device/server/provider/log/backups and duration/criteria |
| Training | Whether used for model/product improvement and control |
| Security | Transport, at rest, access boundary, secrets |
| Deletion/export | User path, SLA, exceptions, downstream propagation |
| Disclosure/consent | Exact UI/policy/purpose string/version |

Include filenames, EXIF, clipboard, pasteboard, crash logs, analytics properties, support tickets, moderation logs, and derived embeddings. “We do not collect data” is false if a third-party SDK or backend receives it on the developer's behalf.

## Privacy-policy test

The policy must be public, app-specific, current, linked in App Store Connect and easily accessible in the app. It should clearly cover:

- What is collected and how.
- Each use/purpose.
- Third parties with access and equivalent protection expectations.
- Retention/deletion and consent withdrawal.
- Account deletion and contact route.
- AI provider prompt/upload/output handling, training, retention, and subprocessors when applicable.
- Children/minors, regional rights, and sensitive categories where applicable.

A generic company policy that omits the app's actual flows is not a pass.

## App Privacy consistency

Cross-check App Store Connect answers against:

- App code and SDKs.
- Backend request schemas and logs.
- Xcode privacy report and each `PrivacyInfo.xcprivacy`.
- Analytics/ad/crash/support providers.
- Account/profile/UGC/moderation data.
- AI prompts, uploads, outputs, identifiers, and provider use.
- Tracking domains, IDFA, fingerprinting, and data linkage.

Document ambiguities in the claim matrix. Do not infer “not collected” from data being encrypted or immediately transformed.

## Privacy manifests and required-reason APIs

Run source and final-bundle scans. Verify:

- The app manifest parses and declares used required-reason API categories.
- Each reason identifier is current and truthfully matches behavior.
- Embedded SDK manifests are present and included in the Xcode aggregate report.
- Listed SDKs match Apple's current manifest/signature list, including repackaged variants.
- Binary SDK signatures are from the expected developer/version; replacement/re-signing is reviewed.
- App Privacy answers incorporate third-party SDK collection.

Static source patterns are heuristics; the final archive is stronger evidence. A declared reason does not prove the use qualifies.

## Permissions and data minimization

For every permission:

- The feature is directly relevant.
- Purpose string is complete, specific, and user-understandable.
- Prompt occurs at the point of need.
- Denial has a coherent alternative when possible.
- The app requests the narrowest access: picker/share sheet, limited Photos, approximate location, selected contacts, etc.
- Paid/core functionality is not conditioned on unrelated data access.
- Revocation is respected immediately.

Flag unused purpose strings because they can indicate stale behavior or confuse App Review. Flag permission use without a matching purpose string as release-critical.

## Tracking, ads, and ATT

Inventory tracking independently of whether the app shows ads. Verify:

- SDK and server-to-server data combination across companies/apps/websites.
- IDFA access and ATT timing.
- No fingerprinting or alternate identifier used to bypass denial.
- Ads are age appropriate, clearly identifiable, and have functional close/report controls.
- Paid removal-of-ads behavior is consistent.
- Marketing push is opt-in and not required for core use.
- Kids Category restrictions receive the dedicated branch.

Consent for privacy collection and ATT authorization are not interchangeable.

## Account access and deletion

If significant account-based features are absent, review whether mandatory login is justified. When account creation exists:

- Offer account deletion inside the app.
- Make the path discoverable and functional; support-only email is normally insufficient unless a documented exception applies.
- Explain scope/timing, reauthentication, subscriptions, user-generated/public content, legal retention, backups, third-party data, and active exports/jobs.
- Test deletion completion, pending state, cancellation if offered, and re-registration.
- Revoke social credentials/data access where applicable.
- Delete or deidentify provider-side AI data as represented.

Do not confuse logout, deactivation, or profile deletion with account deletion.

## Login services

If a third-party/social service authenticates the user's primary account, verify an equivalent privacy-preserving option or a current documented exception. Test:

- Same material access and no punitive feature gap.
- Name/email-limited data, private email support, and no ad-interaction collection without consent.
- Account linking, duplicate accounts, hidden-email relay, credential revocation, and deletion.
- Enterprise/education, government identity, client-for-specific-service, own-account-system, and marketplace exceptions only when all facts fit.

Avoid hard-coding this as “Sign in with Apple required in every app”; the current rule is expressed as equivalent login properties and exceptions.

## Security review

### Secrets and transport

- No API/provider keys, private keys, credentials, bearer tokens, signing material, or admin URLs embedded in source, resources, screenshots, or reports.
- Client-side third-party AI keys are treated as exposed; use a bounded server broker or provider-supported ephemeral mechanism.
- ATS exceptions are minimal and justified; no arbitrary HTTP endpoints.
- TLS trust handling does not accept all certificates or disable validation in release.
- Logs and crash reports redact tokens, prompts, personal data, and purchase receipts.

### Authentication and authorization

- Server authorizes every object/action; do not rely on client-hidden UI.
- Test IDOR/cross-account access, account switch, stale tokens, deleted user, role downgrade, and share links.
- Use secure token storage and rotation; no passwords in UserDefaults/plain files.
- Sensitive actions use reauthentication/confirmation where appropriate.
- Rate limiting, abuse controls, and recovery do not leak account existence unnecessarily.

### Data handling

- Encrypt sensitive data at rest where appropriate and protect files with suitable Data Protection classes.
- Clipboard, screenshots, widgets, notifications, backups, Spotlight, Siri, logs, and caches do not leak sensitive content.
- Export/share operations require user intent and correct recipient.
- Deletion propagates to caches, indexes, AI/vector stores, moderation systems, and processors according to disclosed policy.

## Face, photo, biometric, and identity data

Require exact answers for:

- Whether faces are detected, recognized, compared, embedded, categorized, beautified, or used for identity/liveness.
- Raw image and derived-template storage, retention, encryption, sharing, training, deletion, and access.
- Whether results concern real-person attractiveness, protected traits, health, emotion, or identity.
- Child/minor data handling and rights/consent.
- Third-party AI/provider recipient and pre-transmission consent.
- Screenshot use and rights.

Do not claim that a face embedding is anonymous without technical/legal evidence; it may remain personal or biometric data.

## Evidence and severity

Direct observed disclosure/data-flow mismatch, exposed secrets, cross-user access, or pre-consent AI transmission can be `BLOCKER`. Source patterns, unused strings, or uncertain SDK behavior are normally `HIGH`/`MEDIUM` pending final-bundle/runtime verification.
