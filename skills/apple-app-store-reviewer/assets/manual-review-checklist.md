# Manual release-review checklist

Use this after deterministic scripts. Every checked item needs evidence; unchecked applicable items prevent a ready gate.

## Scope and freshness

- [ ] Policy freshness is CURRENT for the review date.
- [ ] Final archive/build and submission metadata are hash/version matched.
- [ ] Platforms, device families, locales, storefronts, category, age target, business model, and special branches are complete.
- [ ] New app versus update and migration scope are recorded.

## Completeness and reviewer access

- [ ] Clean install reaches useful functionality.
- [ ] Production-like backend and feature flags are live.
- [ ] Non-expiring demo account works twice without 2FA/invite/captcha blockers.
- [ ] Every advertised/reviewed feature is reachable.
- [ ] No crash, hang, placeholder, broken link, dead control, raw error, or indefinite loading state.
- [ ] Offline, timeout, denied permission, revoked permission, and backend failure recover coherently.
- [ ] Production review state does not auto-enable premium, hidden, debug, test, or reviewer-only behavior.

## Metadata and visuals

- [ ] Description, subtitle, promotional text, keywords, category, URLs, and review notes match the build.
- [ ] Every screenshot original and contact sheet received semantic review.
- [ ] Screenshot dimensions/formats/count/alpha/locale/device coverage pass.
- [ ] No real personal data, stale UI, mock-only feature, misleading price, unsupported device, or unlicensed content.
- [ ] Claims are reconciled in claim-consistency.csv.
- [ ] App Store name, bundle display name, in-app identity, sibling-platform naming, and IAP promotional images are consistent and non-duplicative.

## Privacy and security

- [ ] Full data inventory includes SDKs, backend, AI, logs, support, moderation, and derived data.
- [ ] App Privacy, policy, manifests, purpose strings, consent UI, and network behavior agree.
- [ ] Required-reason API declarations and listed SDK manifests/signatures are current.
- [ ] No secret/client AI key/private key/token/admin endpoint is shipped.
- [ ] Account deletion, social credential revocation, export, and provider deletion are tested.
- [ ] Authorization and cross-account isolation are tested.
- [ ] Custom permission pre-prompts are accurate and do not impersonate or pre-commit the system Allow/Don’t Allow choice.

## AI

- [ ] Provider/data/purpose/retention/training map is complete.
- [ ] Personal data is not sent to third-party AI before informed explicit permission.
- [ ] Decline and withdrawal produce zero covered transmission.
- [ ] Deterministic adapter contracts ran against the release environment.
- [ ] Manual semantic queue and worst-case age-rating review are complete.
- [ ] Prompt injection, cross-user leakage, provider failure, public output, and deletion are tested.
- [ ] High-impact outputs have bounded claims and qualified human oversight.
- [ ] Guideline 4.7 and 4.2/4.3 branches were applied where relevant.

## Commerce

- [ ] Transaction type and storefront exception/entitlement are documented.
- [ ] Every IAP/subscription is submitted/attached, localized, visible, and Sandbox-tested.
- [ ] Price, duration, trial, renewal/commitment, benefits, privacy, and EULA are clear.
- [ ] Purchase, cancel, pending, restore, manage, renewal, expiration, billing retry, refund/revocation, and account deletion states are tested as applicable.
- [ ] No impermissible external purchase call-to-action or hidden digital unlock.

## Safety and specialized branches

- [ ] UGC has filter/report/block/contact/moderation and age controls.
- [ ] Kids/minor, medical, finance, gambling, crypto, VPN/MDM, browser, remote desktop, extension, and regional branches are complete where matched.
- [ ] Rights/licenses/authorizations/regulatory evidence are attached where required.
- [ ] Native-value dossier addresses minimum-functionality/template/spam risk.
- [ ] Ads, landing pages, social promotion, remote flags, and production behavior disclose the same generative/AI capabilities reviewed in the binary.
- [ ] Storefront-specific AI wording, licensing, availability, data handling, and declarations rely on current official or qualified legal evidence, not community blacklists.

## Submission package

- [ ] Review notes contain exact navigation, AI consent/provider, IAP IDs, deletion, hardware, and attachments.
- [ ] For new or hard-to-reproduce apps, a current physical-device recording, tested device/OS list, external-service inventory, and primary feature/IAP journey are ready for a 2.1 information request.
- [ ] No plaintext credentials or personal data appear in artifacts.
- [ ] No open BLOCKER/HIGH finding remains.
- [ ] Every mandatory check is PASS.
- [ ] `validate_report.py --strict` passes.
- [ ] The complete audit was rerun after fixes.

## Capacitor 8.5, when applicable

- [ ] Detected version is inside `>=8.5.0 <9.0.0`; a future major is explicitly framework-unverified.
- [ ] `@capacitor/core`, `@capacitor/ios`, and `@capacitor/cli` resolve to the same supported release line, followed by `npx cap sync ios`.
- [ ] Source config/webDir, post-sync native config/public, and final bundle paths plus SHA-256 manifests agree or have documented generated differences.
- [ ] Declared, lockfile-resolved, SPM/Pods-integrated, and finally embedded plugin inventories agree.
- [ ] Default inspection did not execute TS/JS config, download packages, or mutate the working tree; any trusted CLI/sync ran from the local executable in a disposable copy.
- [ ] Release config has no `server.url`, cleartext live-reload, broad `allowNavigation`, production logging, or WebView debugging.
- [ ] UIScene manifest, SceneDelegate proxy forwarding, AppDelegate scene hook, and target membership are complete.
- [ ] Cold/warm custom URLs, universal links, `App.getLaunchUrl()`, `appUrlOpen`, `pause`/`resume`, and background/foreground paths pass.
- [ ] Plugin inventory is reconciled with purpose strings, capabilities, privacy manifests, App Privacy answers, and runtime permission prompts.
- [ ] Bundled web assets match the reviewed build and launch with every development host unavailable.
- [ ] CSP, OAuth PKCE, token storage, native bridge exposure, and external WebView navigation were reviewed.
- [ ] Any live-update system has signed/integrity-checked bundles, a bundled fallback, rollback evidence, and a documented policy boundary.
