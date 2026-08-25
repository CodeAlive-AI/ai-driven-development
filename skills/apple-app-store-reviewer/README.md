# Apple App Store Reviewer

Local-first Agent Skill for auditing Apple-platform apps before submission or after rejection. It combines deterministic checks with evidence-driven manual review and returns one gate: `NOT READY`, `CONDITIONALLY READY`, or `READY FOR SUBMISSION`.

It covers:

- source, archive/IPA, entitlements, privacy manifests, metadata, URLs, screenshots, IAP, subscriptions, login, and account deletion;
- AI consent, provider data flows, safety, age rating, advertising, and worst-case output;
- Capacitor 8.5 release configuration, UIScene migration, plugins/privacy, WebView boundaries, and live updates;
- simulator/XCUITest review journeys, reviewer notes, rejection recovery, and appeal evidence.

Apple makes the final decision. The skill never promises approval and never treats community reports as policy.

## Quick start

Requires Python 3.11+. Pillow and JSON Schema support are installed from `requirements.txt`; macOS with Xcode is required for complete archive, simulator, signing, and XCUITest checks.

```bash
python3 -m pip install -r requirements.txt
cp assets/review-input.example.json review-input.json
# Fill in release artifact, metadata, screenshot, and feature paths.
python3 scripts/review_app.py \
  --config review-input.json \
  --output-dir review-output
```

For the final release candidate on a controlled Mac:

```bash
python3 scripts/review_app.py \
  --config review-input.json \
  --output-dir review-output \
  --network \
  --strict
```

Paths in `review-input.json` are relative to that file. Reference reviewer credentials by environment-variable name; never store passwords in the config.

## Capacitor 8.5

Capacitor is auto-detected from package/config, native-project, bridge, or final-bundle evidence. The qualified range is `>=8.5.0 <9.0.0`; Capacitor 9 requires a separate baseline refresh.

The review compares three states: production `webDir` and source config, post-sync native config/assets/dependencies, and the exact submitted bundle. Missing config, asset, plugin, privacy, or identity parity prevents `READY FOR SUBMISSION`. Default inspection never executes JS/TS config or mutates the project; trusted CLI evidence must use the project-local CLI in a disposable copy. Framework presence alone is never a Guideline 4.2/4.3 finding.

## Evidence model

- `PASS` requires an observed artifact or runtime path.
- Missing evidence remains `SKIPPED` or `NEEDS_REVIEW`.
- Deterministic violations are separated from heuristics.
- Visual and AI semantic review remain mandatory even when automated checks pass.
- X, Reddit, forums, and vendor claims may trigger tests, but only current Apple authority and direct app evidence can support a blocker.

Start with [SKILL.md](SKILL.md) for the full workflow. Templates live in `assets/`; policy, Capacitor, AI, payment, screenshot, and community guidance live in `references/`.

## Validate the skill

```bash
python3 scripts/validate_skill.py .
python3 -m unittest discover -s tests -p 'test_*.py' -v
sha256sum -c CHECKSUMS.sha256
```

See [TEST-RESULTS.md](TEST-RESULTS.md) for verified coverage and environment limits, and [CHANGELOG.md](CHANGELOG.md) for release history.
