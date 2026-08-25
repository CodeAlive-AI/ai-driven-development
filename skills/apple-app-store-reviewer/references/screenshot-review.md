# Screenshot and visual review

This reference covers App Store screenshots, app previews, simulator evidence, and AI/human visual evaluation. Deterministic image checks and semantic visual review are separate gates.

## Artifact layout

Preferred structure:

```text
screenshots/
  en-US/
    iphone-6.9/
      01-home.png
      02-core-workflow.png
    ipad-13/
      01-dashboard.png
  de-DE/
    iphone-6.9/
      ...
```

Folder names must map to the declared locales and accepted display groups in `scripts/catalogs.py`. Keep originals immutable after review; use SHA-256 in visual evidence.

## Deterministic checks

Run:

```bash
python3 scripts/inspect_screenshots.py \
  --screenshots screenshots \
  --config review-input.json \
  --output review-output/screenshots.json \
  --contact-sheets review-output/contact-sheets
```

The checker validates:

- JPEG/JPG/PNG format and decodability.
- Exact accepted pixel dimensions, including portrait/landscape reversal.
- No alpha channel/transparency.
- 1–10 images per locale/display group.
- Declared locale/device coverage.
- Duplicate and near-duplicate image signals.
- Blank, low-information, or title-card signals.
- Contact sheets and a visual-review queue.

A correct dimension is not a semantic pass.

## Visual-review procedure

For Capacitor/hybrid apps, require captures from the exact native WKWebView release build, not a desktop browser or responsive emulator. Check safe areas, system bars, home indicator, keyboard, modal and permission ordering, iPad resize/orientation, external handoff, local/network errors, stale splash/white flash/blank frames, and that every claimed feature exists in the final hashed web bundle. Browser chrome, desktop navigation, hover-only affordances, or a website cookie banner are wrapper-risk observations, not automatic 4.2 findings.

Review every original at full resolution, then each contact sheet for sequence consistency. Produce `paths.visual_results` using `assets/manual-evidence.schema.json` and include an exact `screenshots.visual` check.

For each image record:

- Path and SHA-256.
- PASS/FAIL/NEEDS_REVIEW.
- Visible feature/claim.
- Locale/device/build context.
- Sensitive data or third-party content.
- Exact observations and finding IDs.

Use `assets/visual-review-prompt.md` as the agent rubric.

## Semantic rubric

### Actual app use

Pass only when the set primarily shows real, reachable app experiences. Flag:

- Splash/login/title cards dominating the set.
- Marketing artwork with no recognizable app UI.
- UI mockups, concept designs, prototype states, or future features.
- Screens from a different build, platform, device family, or old brand.
- A website or third-party service represented as native app functionality.

Text and graphic overlays are not automatically prohibited, but must not obscure the actual UI or mislead.

### Claim accuracy

For every visible claim, find runtime evidence:

- “Free,” price, discount, trial length, renewal, lifetime, or “no ads.”
- “Private,” “on device,” “encrypted,” “anonymous,” “not used for training.”
- AI provider/model, accuracy, professional advice, or guaranteed result.
- Offline, sync, collaboration, device support, language, or accessibility.
- Awards, rankings, user counts, ratings, testimonials, and comparative claims.

An unverified material claim is at least `HIGH` until reconciled.

### Privacy and safety

Flag:

- Real names, emails, phone numbers, faces, addresses, location, messages, health/financial data, tokens, QR codes, or internal identifiers.
- Children's data or faces without documented rights/consent.
- Objectionable or age-inconsistent generated/UGC content.
- Fake security/system alerts, fake permissions, or UI that impersonates Apple.
- Third-party content, brands, celebrities, copyrighted media, or maps without rights/required attribution.

Use synthetic accounts/data. Blurring is inferior to capturing clean synthetic evidence because residual information can remain.

### Localization

Inspect each locale independently:

- No untranslated text, placeholder keys, mixed languages, clipped strings, broken line wrapping, mojibake, or wrong number/date/currency format.
- Marketing overlay and app UI agree on locale.
- Price/trial text matches storefront and submitted product.
- Right-to-left layout is intentional where applicable.
- The screenshot order tells a coherent story for that locale.

Do not assume English screenshots are acceptable merely because the app supports English.

### Device and platform integrity

Verify:

- iPhone screenshots show iPhone UI; iPad shows usable iPad layout; no stretched phone image.
- Correct safe areas, status bar, keyboard, orientation, split view, and pointer behavior where relevant.
- No Android/Windows/browser chrome or unsupported-device imagery.
- Apple hardware/device frames and platform assets are used consistently with current marketing requirements.
- macOS, tvOS, watchOS, and visionOS sets show their actual interaction model.

### Commerce

Inspect paywall/store images for:

- Product name, duration, price, trial, billing cadence, renewal/commitment, and included benefits.
- Restore and manage-subscription paths where relevant.
- No false countdowns, hidden close controls, deceptive emphasis, or preselected high-cost options.
- No external purchase call-to-action where not permitted for that storefront/entitlement.
- Screenshot claims agree with App Store Connect products and runtime.

### AI-specific visuals

Verify:

- AI is identified appropriately; generated results are not represented as verified fact.
- Consent appears before personal-data transmission, not after upload has begun.
- Provider/data-purpose disclosure is readable and specific.
- Refusal, no-result, unsafe-output, and correction/report states are coherent.
- High-impact outputs include appropriate uncertainty and confirmation in context.
- Worst-case reachable output does not make the declared age rating misleading.

## Simulator evidence capture

Use `scripts/capture_simulator.py` for deterministic deep-link/state capture. The plan is allow-listed and does not execute arbitrary shell commands.

Capture at least:

- First launch and useful home state.
- Core advertised workflow.
- Permission pre-prompt/system prompt/denial/recovery.
- AI consent decline and accept states.
- Paywall, purchase success, restore, manage subscription.
- Account creation/login/logout/deletion.
- Empty, loading, offline, timeout, server error, and revoked-permission states.
- UGC report/block/moderation.
- Platform-specific layout and all supported orientations where material.

Status-bar normalization is evidence hygiene, not a substitute for actual screenshot compliance.

## Preview/video review

When app previews exist, additionally verify:

- Footage is screen-captured from the app, current, and platform-accurate.
- No unlicensed audio, misleading cuts, inaccessible feature, or simulated interaction presented as actual.
- Text is readable within App Store playback and locale appropriate.
- Any price, offer, or time-sensitive content is current.
- The first frames communicate real app use rather than only brand animation.

The bundled image checker does not parse preview video; this remains a manual branch.

## Visual pass invariant

`screenshots.visual = PASS` requires:

- every submitted original reviewed;
- every declared locale/display group reviewed;
- hashes match the final submission files;
- all FAIL findings resolved or explicitly removed/replaced;
- the final set cross-checked against runtime, metadata, privacy, age rating, and IAP records.

A contact-sheet-only review cannot pass because small text and sensitive details may be missed.
