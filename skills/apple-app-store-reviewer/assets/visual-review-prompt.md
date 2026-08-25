# Visual review prompt

Review the supplied App Store screenshot originals and contact sheets as a skeptical Apple App Review specialist. Do not infer a pass from dimensions or attractive design. Use `references/screenshot-review.md`.

For every original image:

1. Identify path/hash, locale, display group, orientation, and visible screen.
2. Decide PASS, FAIL, or NEEDS_REVIEW.
3. List exact observable facts; do not guess hidden behavior.
4. Check actual app use versus title card/mock/future feature.
5. Extract material visible claims conceptually: feature, price/trial, privacy/security, AI, accuracy, device/platform, social proof. Mark each for runtime/metadata verification.
6. Check clipping, overlap, small/unreadable text, mixed/untranslated language, wrong currency/date/number, stale branding, unsupported device/platform, distorted UI, fake system UI, and inconsistent sequence.
7. Check real personal/sensitive data, children's data/faces, tokens/QR codes, objectionable content, third-party brands/content, and required attribution.
8. Check paywall/subscription clarity and AI consent/provider disclosure where visible.
9. Compare all images in the locale/group for duplicates, missing core journey, login/splash domination, and contradictory states.
10. For a hybrid/Capacitor app, confirm the image came from the exact native WKWebView release build and review safe areas, bars, keyboard, permission ordering, iPad layout, error states, splash/blank frames, and parity with the final bundled route—not a desktop responsive preview.

Output JSON matching `assets/manual-evidence.schema.json`. Include exactly this mandatory check:

```json
{
  "id": "screenshots.visual",
  "title": "Agent visual review of every submitted screenshot",
  "status": "PASS|NEEDS_REVIEW|ERROR",
  "mandatory": true,
  "detail": "scope and result",
  "tool": "ai-agent-vision",
  "evidence": []
}
```

Set PASS only when every original was reviewed at full resolution, all declared locales/groups are covered, hashes match, and all visual findings are resolved. Do not use OCR as the default replacement for visual inspection.
