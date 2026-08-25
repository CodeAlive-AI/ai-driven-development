#!/usr/bin/env python3
"""Validate and normalize review-input.json."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any, Mapping

from common import (
    ReviewInputError,
    dump_json,
    load_json,
    make_check,
    make_evidence,
    make_finding,
    now_iso,
    resolve_config_paths,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "assets" / "review-input.schema.json"
LOCALE_RE = re.compile(r"^[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")


def _schema_errors(config: Any, schema_path: Path) -> tuple[list[str], str]:
    schema = load_json(schema_path)
    try:
        import jsonschema  # type: ignore
    except ImportError:
        errors: list[str] = []
        if not isinstance(config, dict):
            return ["root must be an object"], "manual"
        for key in ("app", "paths", "features"):
            if key not in config or not isinstance(config.get(key), dict):
                errors.append(f"/{key}: required object is missing")
        app = config.get("app", {}) if isinstance(config, dict) else {}
        for key in ("name", "bundle_id", "platforms", "device_families", "storefronts", "locales"):
            if not app.get(key):
                errors.append(f"/app/{key}: required value is missing")
        return errors, "manual"

    validator_cls = jsonschema.validators.validator_for(schema)
    validator_cls.check_schema(schema)
    validator = validator_cls(schema)
    errors = []
    for error in sorted(validator.iter_errors(config), key=lambda item: list(item.absolute_path)):
        path = "/" + "/".join(str(part) for part in error.absolute_path)
        errors.append(f"{path or '/'}: {error.message}")
    return errors, "jsonschema"


def _evidence(config_path: Path, detail: str, value: Any | None = None) -> dict[str, Any]:
    return make_evidence(kind="config", location=str(config_path), detail=detail, value=value)


def validate_config(config: Mapping[str, Any], config_path: str | Path, *, schema_path: str | Path = DEFAULT_SCHEMA) -> dict[str, Any]:
    config_path = Path(config_path).resolve()
    schema_path = Path(schema_path).resolve()
    raw = dict(config)
    resolved = resolve_config_paths(raw, config_path)
    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    facts: dict[str, Any] = {"resolved_paths": resolved.get("paths", {})}

    schema_errors, validator = _schema_errors(raw, schema_path)
    if schema_errors:
        for index, error in enumerate(schema_errors, start=1):
            findings.append(
                make_finding(
                    id=f"INPUT-SCHEMA-{index:03d}",
                    title="Review input does not match the schema",
                    severity="BLOCKER",
                    category="intake",
                    guideline="Submission evidence",
                    confidence="CERTAIN",
                    evidence=[_evidence(config_path, error)],
                    rationale="The audit cannot safely interpret an invalid control file; downstream checks may use the wrong scope or artifact.",
                    remediation="Correct review-input.json using assets/review-input.example.json and assets/review-input.schema.json.",
                    verification=[f"Run: python3 scripts/validate_input.py --config {config_path}"],
                    sources=["references/policy-baseline.md", "assets/review-input.schema.json"],
                )
            )
        checks.append(make_check("input.schema", "Review input schema", "ERROR", mandatory=True, tool=validator, detail=f"{len(schema_errors)} schema error(s)"))
    else:
        checks.append(make_check("input.schema", "Review input schema", "PASS", mandatory=True, tool=validator, detail="Input matches the pinned schema"))

    app = resolved.get("app", {})
    features = resolved.get("features", {})
    paths = resolved.get("paths", {})
    review = resolved.get("review", {})

    # Cross-field scope checks.
    locales = app.get("locales", []) or []
    primary_locale = app.get("primary_locale") or (locales[0] if locales else None)
    facts["primary_locale"] = primary_locale
    invalid_locales = [locale for locale in locales if not isinstance(locale, str) or not LOCALE_RE.match(locale)]
    if invalid_locales:
        findings.append(
            make_finding(
                id="INPUT-LOCALES-FORMAT",
                title="One or more locale identifiers are malformed",
                severity="MEDIUM",
                category="intake",
                guideline="2.3 Accurate Metadata",
                confidence="HIGH",
                evidence=[_evidence(config_path, "Malformed locale identifiers", invalid_locales)],
                rationale="Locale folders and metadata matching depend on stable BCP-47-like identifiers. A malformed identifier can hide missing localization evidence.",
                remediation="Use App Store Connect locale identifiers such as en-US, de-DE, ja, or zh-Hans.",
                verification=["Rerun input validation and confirm every declared locale is accepted."],
                sources=["references/screenshot-review.md"],
            )
        )
    if primary_locale and primary_locale not in locales:
        findings.append(
            make_finding(
                id="INPUT-PRIMARY-LOCALE",
                title="Primary locale is not present in the declared locale list",
                severity="HIGH",
                category="intake",
                guideline="2.3 Accurate Metadata",
                confidence="CERTAIN",
                evidence=[_evidence(config_path, f"primary_locale={primary_locale}; locales={locales}")],
                rationale="The audit cannot construct a reliable locale coverage matrix when the primary locale is outside scope.",
                remediation="Add the primary locale to app.locales or correct app.primary_locale.",
                verification=["Rerun input validation."],
                sources=["references/screenshot-review.md"],
            )
        )

    platforms = set(app.get("platforms", []) or [])
    families = set(app.get("device_families", []) or [])
    expected_family = {
        "ios": "iphone", "ipados": "ipad", "macos": "mac", "tvos": "apple-tv",
        "watchos": "apple-watch", "visionos": "vision-pro",
    }
    for platform, family in expected_family.items():
        if platform in platforms and family not in families:
            findings.append(
                make_finding(
                    id=f"INPUT-DEVICE-FAMILY-{platform.upper()}",
                    title=f"{platform} is enabled but {family} evidence is outside review scope",
                    severity="HIGH",
                    category="intake",
                    guideline="2.1 App Completeness; 2.3 Accurate Metadata",
                    confidence="HIGH",
                    evidence=[_evidence(config_path, f"platforms={sorted(platforms)}; device_families={sorted(families)}")],
                    rationale="A supported platform needs matching runtime and screenshot evidence. Omitting the device family can cause false readiness.",
                    remediation=f"Add {family} to app.device_families or remove {platform} if the release binary does not support it.",
                    verification=["Compare the final bundle's supported platforms/device families with review-input.json."],
                    sources=["references/policy-baseline.md", "references/screenshot-review.md"],
                )
            )

    # Artifact checks. Missing artifacts are represented as skipped mandatory checks,
    # not blockers, so a partial audit still produces value while remaining gated.
    artifact_specs = {
        "project": ("Source project", True),
        "archive": ("Release archive/app/IPA", True),
        "metadata": ("App Store metadata export", True),
        "screenshots": ("Final screenshots", True),
        "privacy_export": ("App Privacy export", False),
        "iap_export": ("In-App Purchase export", bool(features.get("commerce", {}).get("iap"))),
        "review_notes": ("App Review notes artifact", False),
        "runtime_results": ("Runtime test evidence", True),
        "ai_results": ("AI safety evidence", bool(features.get("ai", {}).get("enabled"))),
        "visual_results": ("Agent visual screenshot review", bool(paths.get("screenshots"))),
        "native_value_dossier": ("Native-value dossier", False),
    }
    artifact_manifest: dict[str, Any] = {}
    for key, (title, mandatory) in artifact_specs.items():
        value = paths.get(key)
        if not value:
            status = "SKIPPED"
            detail = "Path not supplied"
            artifact_manifest[key] = {"provided": False, "exists": False, "path": None}
        else:
            path = Path(value)
            exists = path.exists()
            status = "PASS" if exists else "ERROR"
            detail = "Artifact exists" if exists else "Configured path does not exist"
            artifact_manifest[key] = {"provided": True, "exists": exists, "path": str(path)}
            if not exists:
                findings.append(
                    make_finding(
                        id=f"INPUT-PATH-{key.upper().replace('_', '-')}",
                        title=f"Configured {title.lower()} path does not exist",
                        severity="HIGH" if mandatory else "MEDIUM",
                        category="intake",
                        guideline="2.1 App Completeness",
                        confidence="CERTAIN",
                        evidence=[_evidence(config_path, f"paths.{key} points to a missing path", str(path))],
                        rationale="The corresponding audit branch cannot run against the exact release evidence.",
                        remediation=f"Correct paths.{key} or generate the missing artifact.",
                        verification=[f"Confirm the path exists and rerun the review: {path}"],
                        sources=["references/policy-baseline.md"],
                    )
                )
        checks.append(make_check(f"input.artifact.{key}", title, status, mandatory=mandatory, tool="filesystem", detail=detail))
    facts["artifacts"] = artifact_manifest

    accounts = features.get("accounts", {})
    demo = review.get("demo_account", {})
    login_required = bool(accounts.get("login_required"))
    if login_required:
        username_env = demo.get("username_env")
        password_env = demo.get("password_env")
        missing_env_names = [key for key, value in (("username_env", username_env), ("password_env", password_env)) if not value]
        missing_env_values = [name for name in (username_env, password_env) if name and not os.environ.get(str(name))]
        if missing_env_names:
            findings.append(
                make_finding(
                    id="INPUT-DEMO-CREDENTIAL-NAMES",
                    title="Login-required review has no complete demo credential references",
                    severity="BLOCKER",
                    category="review-access",
                    guideline="2.1 App Completeness",
                    confidence="CERTAIN",
                    evidence=[_evidence(config_path, "Missing demo credential environment-variable names", missing_env_names)],
                    rationale="Apple must be able to access the full app during review unless an approved full-featured demo mode is provided.",
                    remediation="Set review.demo_account.username_env and password_env to environment-variable names; do not commit the secret values.",
                    verification=["Load both environment variables and perform a clean login using the review build."],
                    sources=["references/runtime-review.md"],
                )
            )
        if missing_env_values:
            findings.append(
                make_finding(
                    id="INPUT-DEMO-CREDENTIAL-VALUES",
                    title="Demo credential environment variables are not loaded",
                    severity="HIGH",
                    category="review-access",
                    guideline="2.1 App Completeness",
                    confidence="CERTAIN",
                    evidence=[_evidence(config_path, "Unset environment variables", missing_env_values)],
                    rationale="The deterministic audit cannot verify reviewer access. Do not place plaintext passwords in the configuration to work around this.",
                    remediation="Load the referenced environment variables in the release-review environment and test the account.",
                    verification=["Rerun input validation with the environment variables present."],
                    sources=["references/runtime-review.md"],
                )
            )
        if not demo.get("non_expiring"):
            findings.append(
                make_finding(
                    id="INPUT-DEMO-EXPIRY",
                    title="Demo account is not declared non-expiring",
                    severity="HIGH",
                    category="review-access",
                    guideline="2.1 App Completeness",
                    confidence="HIGH",
                    evidence=[_evidence(config_path, "review.demo_account.non_expiring is not true")],
                    rationale="Expired or one-time credentials are a frequent source of review failure and cannot be treated as reviewer-safe access.",
                    remediation="Provision and validate a non-expiring review account or a fully functional demo mode.",
                    verification=["Sign in from a fresh install twice and confirm no 2FA, email-link, or organization approval blocks review."],
                    sources=["references/runtime-review.md"],
                )
            )
        credential_status = "PASS" if not missing_env_names and not missing_env_values and demo.get("non_expiring") else "NEEDS_REVIEW"
        checks.append(make_check("input.demo_access", "Reviewer demo access", credential_status, mandatory=True, tool="environment", detail="Login-required app"))
    else:
        checks.append(make_check("input.demo_access", "Reviewer demo access", "PASS", mandatory=False, tool="config", detail="App is not declared login-required"))

    ai = features.get("ai", {})
    if ai.get("enabled"):
        if ai.get("third_party") and ai.get("personal_data_types"):
            if not ai.get("explicit_consent_before_transmission"):
                findings.append(
                    make_finding(
                        id="INPUT-AI-CONSENT-DECLARATION",
                        title="Third-party AI personal-data flow lacks pre-transmission explicit consent",
                        severity="BLOCKER",
                        category="ai-privacy",
                        guideline="5.1.2(i) Data Use and Sharing",
                        confidence="CERTAIN",
                        evidence=[_evidence(config_path, "AI feature declaration", ai)],
                        rationale="Apple requires clear disclosure and explicit permission before personal data is shared with a third party, including third-party AI.",
                        remediation="Implement an informed in-app consent event before the first transmission and update the declaration only after runtime verification.",
                        verification=["Fresh-install the app, deny consent, and prove no personal data reaches the provider; then allow and inspect the first request."],
                        sources=["references/ai-review.md", "references/privacy-security.md"],
                    )
                )
            if not ai.get("provider_named_in_consent"):
                findings.append(
                    make_finding(
                        id="INPUT-AI-PROVIDER-DISCLOSURE",
                        title="AI consent does not name the third-party recipient/provider",
                        severity="HIGH",
                        category="ai-privacy",
                        guideline="5.1.2(i) Data Use and Sharing",
                        confidence="HIGH",
                        evidence=[_evidence(config_path, "provider_named_in_consent is not true")],
                        rationale="Generic statements that data is sent to 'AI' may not clearly disclose where personal data is shared.",
                        remediation="Name the provider or recipient category precisely, list data categories and purpose, and describe material retention/training behavior.",
                        verification=["Capture the consent screen and compare it with the actual provider/data-flow map."],
                        sources=["references/ai-review.md"],
                    )
                )
        if ai.get("third_party") and not ai.get("providers"):
            findings.append(
                make_finding(
                    id="INPUT-AI-PROVIDER-MISSING",
                    title="Third-party AI is enabled but no provider is declared",
                    severity="HIGH",
                    category="ai-privacy",
                    guideline="5.1.2(i) Data Use and Sharing",
                    confidence="CERTAIN",
                    evidence=[_evidence(config_path, "features.ai.third_party=true and providers is empty")],
                    rationale="The review cannot reconcile consent, privacy policy, App Privacy answers, subprocessors, and runtime endpoints without the recipient identity.",
                    remediation="Declare every model/API provider and intermediary processor used by the release build.",
                    verification=["Compare source and network evidence with the completed provider list."],
                    sources=["references/ai-review.md"],
                )
            )

    commerce = features.get("commerce", {})
    if commerce.get("digital_goods") and not commerce.get("iap"):
        findings.append(
            make_finding(
                id="INPUT-DIGITAL-GOODS-NO-IAP",
                title="Digital goods are declared without In-App Purchase",
                severity="BLOCKER",
                category="payments",
                guideline="3.1.1 In-App Purchase",
                confidence="HIGH",
                evidence=[_evidence(config_path, "Commerce declaration", commerce)],
                rationale="Digital content, features, subscriptions, or credits consumed in the app normally must use Apple's In-App Purchase unless a precise guideline exception or entitlement applies.",
                remediation="Use In-App Purchase or document the exact reader, enterprise, person-to-person, multiplatform, regional, or other applicable exception and storefront scope.",
                verification=["Exercise every purchase/entitlement path in each target storefront."],
                sources=["references/business-payments.md"],
            )
        )

    ugc = features.get("ugc", {})
    if ugc.get("enabled"):
        missing = [name for name in ("filter", "report", "block", "support_contact") if not ugc.get(name)]
        if missing:
            findings.append(
                make_finding(
                    id="INPUT-UGC-CONTROLS",
                    title="Declared user-generated content lacks one or more baseline safety controls",
                    severity="BLOCKER",
                    category="safety",
                    guideline="1.2 User-Generated Content",
                    confidence="CERTAIN",
                    evidence=[_evidence(config_path, "Missing UGC controls", missing)],
                    rationale="Apps with user-generated content must provide filtering, reporting, blocking, and reachable contact mechanisms appropriate to the feature.",
                    remediation="Implement and test each missing control, including timely moderation response procedures.",
                    verification=["Create objectionable test content, report it, block its author, and verify support escalation from a fresh account."],
                    sources=["references/app-type-branches.md"],
                )
            )

    checks.append(make_check("input.cross_field", "Cross-field consistency", "PASS" if not findings else "NEEDS_REVIEW", mandatory=True, tool="validate_input.py", detail=f"{len(findings)} finding(s) emitted"))

    return {
        "module": "validate_input",
        "generated_at": now_iso(),
        "config_path": str(config_path),
        "schema_path": str(schema_path),
        "resolved_config": resolved,
        "facts": facts,
        "checks": checks,
        "findings": findings,
        "tool": {"name": "validate_input.py", "status": "OK", "detail": f"validator={validator}"},
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate and normalize an App Store review-input.json file.")
    parser.add_argument("--config", required=True, help="Path to review-input.json")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA), help="Input JSON Schema")
    parser.add_argument("--output", help="Write structured JSON result to this path")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero when any finding is emitted")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config = load_json(args.config)
        if not isinstance(config, dict):
            raise ReviewInputError("Review input root must be a JSON object")
        result = validate_config(config, args.config, schema_path=args.schema)
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"validate_input: {exc}\n")
        return 3
    text = dump_json(result, args.output) if args.output else dump_json(result)
    if not args.output:
        sys.stdout.write(text)
    return 2 if args.strict and result["findings"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
