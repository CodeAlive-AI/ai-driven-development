#!/usr/bin/env python3
"""Deterministically validate App Store Connect metadata exports."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import urlparse

from catalogs import METADATA_LIMITS
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

PLACEHOLDER_RE = re.compile(
    r"(?i)\b(?:lorem ipsum|todo|tbd|fixme|coming soon|under construction|sample text|"
    r"test app|beta version|dummy|placeholder|example\.com|localhost)\b"
)
PRICE_RE = re.compile(r"(?i)(?:[$€£¥]\s?\d|\b\d+(?:[.,]\d{1,2})?\s?(?:usd|eur|gbp|cad|aud|jpy)\b)")
SUPERLATIVE_RE = re.compile(r"(?i)\b(?:best|#\s?1|number one|most accurate|guaranteed|100%|perfect|never fails)\b")
COMPETITOR_HINT_RE = re.compile(r"(?i)\b(?:better than|alternative to|replacement for|like)\b")
HTML_RE = re.compile(r"<[^>]+>")
VALID_RATINGS = {"4+", "9+", "13+", "16+", "18+", "unrated"}


def _loc(metadata_path: Path, pointer: str, detail: str, value: Any | None = None) -> dict[str, Any]:
    return make_evidence(kind="metadata", location=f"{metadata_path}#{pointer}", detail=detail, value=value)


def _is_https_url(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlparse(value.strip())
    return parsed.scheme.lower() == "https" and bool(parsed.netloc)


def _utf8_len(value: Any) -> int:
    return len(str(value or "").encode("utf-8"))


def _find(
    *,
    id: str,
    title: str,
    severity: str,
    category: str,
    guideline: str,
    evidence: list[dict[str, Any]],
    rationale: str,
    remediation: str,
    verification: list[str],
    sources: list[str],
    confidence: str = "CERTAIN",
    status: str = "OPEN",
    automation: str = "deterministic",
    tags: tuple[str, ...] = (),
) -> dict[str, Any]:
    return make_finding(
        id=id,
        title=title,
        severity=severity,
        category=category,
        guideline=guideline,
        evidence=evidence,
        rationale=rationale,
        remediation=remediation,
        verification=verification,
        sources=sources,
        confidence=confidence,
        status=status,
        automation=automation,
        tags=tags,
    )


def _length_finding(metadata_path: Path, locale: str, field: str, value: str, minimum: int | None, maximum: int | None) -> dict[str, Any] | None:
    length = len(value)
    if minimum is not None and length < minimum:
        condition = f"{length} characters; minimum is {minimum}"
    elif maximum is not None and length > maximum:
        condition = f"{length} characters; maximum is {maximum}"
    else:
        return None
    return _find(
        id=f"META-{locale.upper()}-{field.upper().replace('_', '-')}-LENGTH",
        title=f"{field.replace('_', ' ').title()} length is outside App Store limits",
        severity="BLOCKER",
        category="metadata",
        guideline="2.3 Accurate Metadata",
        evidence=[_loc(metadata_path, f"/locales/{locale}/{field}", condition, value)],
        rationale="App Store Connect enforces metadata field limits and may prevent submission or truncate/reject the product page.",
        remediation=f"Rewrite {field.replace('_', ' ')} within the accepted limit without changing material claims.",
        verification=["Count Unicode characters and re-run validate_metadata.py."],
        sources=["references/policy-baseline.md", "references/rule-matrix.md"],
    )


def validate_metadata(
    metadata: Mapping[str, Any],
    metadata_path: str | Path,
    *,
    config: Mapping[str, Any] | None = None,
    config_path: str | Path | None = None,
) -> dict[str, Any]:
    metadata_path = Path(metadata_path).resolve()
    config = dict(config or {})
    if config_path:
        config = resolve_config_paths(config, config_path)
    app = config.get("app", {})
    features = config.get("features", {})
    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    facts: dict[str, Any] = {}

    locales = metadata.get("locales")
    if not isinstance(locales, dict) or not locales:
        findings.append(_find(
            id="META-LOCALES-MISSING",
            title="No localized App Store metadata was supplied",
            severity="BLOCKER",
            category="metadata",
            guideline="2.1 App Completeness; 2.3 Accurate Metadata",
            evidence=[_loc(metadata_path, "/locales", "Expected a non-empty object of locale metadata")],
            rationale="The review cannot verify the product page, required URLs, or localization consistency without the exact metadata submitted to App Store Connect.",
            remediation="Export or construct metadata.json with one object per App Store locale.",
            verification=["Rerun the metadata validator and compare the values with App Store Connect."],
            sources=["references/policy-baseline.md"],
        ))
        locales = {}
    checks.append(make_check(
        "metadata.locales",
        "Localized metadata present",
        "PASS" if locales else "ERROR",
        mandatory=True,
        tool="validate_metadata.py",
        detail=f"{len(locales)} locale(s)",
    ))

    declared_locales = set(app.get("locales", []) or [])
    actual_locales = set(locales.keys())
    missing_locales = sorted(declared_locales - actual_locales)
    extra_locales = sorted(actual_locales - declared_locales) if declared_locales else []
    if missing_locales:
        findings.append(_find(
            id="META-DECLARED-LOCALES-MISSING",
            title="Declared storefront locales have no metadata evidence",
            severity="HIGH",
            category="localization",
            guideline="2.3 Accurate Metadata",
            evidence=[_loc(metadata_path, "/locales", "Missing locales declared in review input", missing_locales)],
            rationale="Missing locale evidence can conceal placeholder text, incorrect URLs, untranslated screenshots, or materially inconsistent claims.",
            remediation="Export every declared localization or narrow the review scope to the actual App Store Connect locales.",
            verification=["Compare the locale list with App Store Connect and re-run the audit."],
            sources=["references/screenshot-review.md"],
        ))
    facts["locales"] = sorted(actual_locales)
    facts["extra_locales"] = extra_locales

    app_name = str(app.get("name") or "")
    company_name = str(app.get("company_name") or "")
    competitors = [str(value) for value in app.get("competitor_names", []) or [] if str(value).strip()]
    all_text_by_locale: dict[str, str] = {}
    url_fields: list[dict[str, str]] = []

    for locale, raw in sorted(locales.items()):
        if not isinstance(raw, dict):
            findings.append(_find(
                id=f"META-{locale.upper()}-OBJECT",
                title="Locale metadata is not an object",
                severity="BLOCKER",
                category="metadata",
                guideline="2.3 Accurate Metadata",
                evidence=[_loc(metadata_path, f"/locales/{locale}", "Expected an object", raw)],
                rationale="The locale cannot be validated or submitted in this structure.",
                remediation="Replace the value with a metadata object.",
                verification=["Rerun validate_metadata.py."],
                sources=["assets/metadata.example.json"],
            ))
            continue

        values = {key: str(raw.get(key) or "").strip() for key in (
            "name", "subtitle", "promotional_text", "description", "keywords", "whats_new",
            "support_url", "marketing_url", "privacy_policy_url", "terms_url",
        )}
        all_text = "\n".join(values.values())
        all_text_by_locale[locale] = all_text

        # Exact field limits.
        limit_specs = {
            "name": (METADATA_LIMITS["name_min_chars"], METADATA_LIMITS["name_max_chars"]),
            "subtitle": (None, METADATA_LIMITS["subtitle_max_chars"]),
            "promotional_text": (None, METADATA_LIMITS["promotional_text_max_chars"]),
            "description": (None, METADATA_LIMITS["description_max_chars"]),
            "whats_new": (None, METADATA_LIMITS["whats_new_max_chars"]),
        }
        for field, (minimum, maximum) in limit_specs.items():
            finding = _length_finding(metadata_path, locale, field, values[field], minimum, maximum)
            if finding:
                findings.append(finding)

        for required_field in ("name", "description", "support_url", "privacy_policy_url"):
            if not values[required_field]:
                findings.append(_find(
                    id=f"META-{locale.upper()}-{required_field.upper().replace('_', '-')}-MISSING",
                    title=f"Required {required_field.replace('_', ' ')} is empty",
                    severity="BLOCKER",
                    category="metadata",
                    guideline="2.1 App Completeness; 2.3 Accurate Metadata; 5.1.1 Privacy Policies",
                    evidence=[_loc(metadata_path, f"/locales/{locale}/{required_field}", "Empty or missing")],
                    rationale="A required or reviewer-critical metadata field is missing from the release product page.",
                    remediation=f"Provide a production-ready localized {required_field.replace('_', ' ')}.",
                    verification=["Compare the value with App Store Connect and rerun the validator."],
                    sources=["references/policy-baseline.md", "references/privacy-security.md"],
                ))

        for field in ("support_url", "marketing_url", "privacy_policy_url", "terms_url"):
            value = values[field]
            if not value:
                continue
            url_fields.append({"locale": locale, "field": field, "url": value})
            if not _is_https_url(value):
                findings.append(_find(
                    id=f"META-{locale.upper()}-{field.upper().replace('_', '-')}-URL",
                    title=f"{field.replace('_', ' ').title()} is not a valid HTTPS URL",
                    severity="BLOCKER" if field in {"support_url", "privacy_policy_url"} else "HIGH",
                    category="metadata",
                    guideline="2.1 App Completeness; 5.1.1 Privacy Policies",
                    evidence=[_loc(metadata_path, f"/locales/{locale}/{field}", "Invalid or non-HTTPS URL", value)],
                    rationale="Reviewers and customers must be able to reach production support/privacy information through a stable URL.",
                    remediation="Use an absolute HTTPS URL with a public hostname; validate its content and redirects.",
                    verification=["Run scripts/check_urls.py --network against the metadata file."],
                    sources=["references/privacy-security.md"],
                ))

        keywords = values["keywords"]
        keyword_bytes = _utf8_len(keywords)
        if keyword_bytes > METADATA_LIMITS["keywords_max_utf8_bytes"]:
            findings.append(_find(
                id=f"META-{locale.upper()}-KEYWORDS-LENGTH",
                title="Keywords exceed the App Store byte limit",
                severity="BLOCKER",
                category="metadata",
                guideline="2.3 Accurate Metadata",
                evidence=[_loc(metadata_path, f"/locales/{locale}/keywords", f"{keyword_bytes} UTF-8 bytes; maximum is {METADATA_LIMITS['keywords_max_utf8_bytes']}", keywords)],
                rationale="App Store Connect measures the keyword field against a fixed limit; multi-byte localized text can exceed it even when the character count appears acceptable.",
                remediation="Reduce the comma-separated keyword string to at most 100 UTF-8 bytes.",
                verification=["Measure len(keywords.encode('utf-8')) and rerun the validator."],
                sources=["references/rule-matrix.md"],
            ))
        if keywords:
            items = [item.strip() for item in keywords.split(",")]
            empties = [index + 1 for index, item in enumerate(items) if not item]
            duplicates = sorted({item.casefold() for item in items if item and sum(1 for x in items if x.casefold() == item.casefold()) > 1})
            too_short = [item for item in items if len(item) <= 2]
            if empties or duplicates or too_short:
                findings.append(_find(
                    id=f"META-{locale.upper()}-KEYWORDS-QUALITY",
                    title="Keyword list contains low-quality or duplicate entries",
                    severity="LOW",
                    category="metadata",
                    guideline="2.3.7 Metadata and search relevance",
                    confidence="HIGH",
                    evidence=[_loc(metadata_path, f"/locales/{locale}/keywords", "Keyword diagnostics", {"empty_positions": empties, "duplicates": duplicates, "two_or_fewer_chars": too_short})],
                    rationale="Redundant, empty, or overly short terms waste the limited keyword field and can make metadata appear manipulative.",
                    remediation="Use distinct, relevant comma-separated terms without app/company names or competitor trademarks.",
                    verification=["Re-run the keyword diagnostics."],
                    sources=["references/rule-matrix.md"],
                ))
            forbidden_keyword_hits = []
            for term in [app_name, company_name, *competitors]:
                if term and term.casefold() in keywords.casefold():
                    forbidden_keyword_hits.append(term)
            if forbidden_keyword_hits:
                findings.append(_find(
                    id=f"META-{locale.upper()}-KEYWORDS-NAMES",
                    title="Keywords repeat app/company names or competitor terms",
                    severity="MEDIUM" if competitors and any(x in competitors for x in forbidden_keyword_hits) else "LOW",
                    category="metadata-ip",
                    guideline="2.3.7 Accurate Metadata; 5.2 Intellectual Property",
                    confidence="HIGH",
                    evidence=[_loc(metadata_path, f"/locales/{locale}/keywords", "Detected terms", forbidden_keyword_hits)],
                    rationale="App/company names are indexed elsewhere, while competitor trademarks can create relevance and intellectual-property issues.",
                    remediation="Remove repeated names and all unlicensed competitor/trademark terms.",
                    verification=["Search every localized metadata field for third-party marks."],
                    sources=["references/rule-matrix.md"],
                ))

        placeholder_matches = sorted({match.group(0) for match in PLACEHOLDER_RE.finditer(all_text)})
        if placeholder_matches:
            findings.append(_find(
                id=f"META-{locale.upper()}-PLACEHOLDER",
                title="Metadata contains placeholder, beta, or development text",
                severity="BLOCKER",
                category="app-completeness",
                guideline="2.1 App Completeness; 2.3 Accurate Metadata",
                evidence=[_loc(metadata_path, f"/locales/{locale}", "Detected placeholder-like text", placeholder_matches)],
                rationale="Submission metadata must describe a final build and use production destinations.",
                remediation="Replace every placeholder/development phrase and URL with final localized content.",
                verification=["Search the App Store Connect record and binary for the same terms."],
                sources=["references/policy-baseline.md"],
            ))

        if HTML_RE.search(values["description"]):
            findings.append(_find(
                id=f"META-{locale.upper()}-DESCRIPTION-HTML",
                title="Description contains HTML-like markup",
                severity="MEDIUM",
                category="metadata",
                guideline="2.3 Accurate Metadata",
                confidence="HIGH",
                evidence=[_loc(metadata_path, f"/locales/{locale}/description", "HTML tag-like content detected")],
                rationale="App Store descriptions are plain text; markup can render incorrectly or present misleading formatting.",
                remediation="Replace markup with readable plain text.",
                verification=["Preview the final product page in App Store Connect."],
                sources=["references/rule-matrix.md"],
            ))

        # Claims are a manual consistency queue, not automatic violations.
        claims: dict[str, list[str]] = {}
        if SUPERLATIVE_RE.search(all_text):
            claims["unsubstantiated_superlative"] = sorted({m.group(0) for m in SUPERLATIVE_RE.finditer(all_text)})
        if PRICE_RE.search(all_text):
            claims["hardcoded_price"] = sorted({m.group(0) for m in PRICE_RE.finditer(all_text)})
        if COMPETITOR_HINT_RE.search(all_text):
            claims["comparison"] = sorted({m.group(0) for m in COMPETITOR_HINT_RE.finditer(all_text)})
        if claims:
            findings.append(_find(
                id=f"META-{locale.upper()}-CLAIMS-REVIEW",
                title="Metadata contains claims requiring build/storefront verification",
                severity="MEDIUM",
                category="metadata-claims",
                guideline="2.3 Accurate Metadata; 5.6 Developer Code of Conduct",
                confidence="MEDIUM",
                status="NEEDS_REVIEW",
                automation="heuristic",
                evidence=[_loc(metadata_path, f"/locales/{locale}", "Claim signals", claims)],
                rationale="Superlatives, guarantees, comparisons, and hardcoded prices are not necessarily prohibited, but they are high-friction when evidence, localization, or the build disagrees.",
                remediation="Substantiate or remove each claim; use localized StoreKit pricing instead of static currency text where the product is sold in-app.",
                verification=["Add every claim to the claim-consistency matrix and reproduce it in the release build/storefront."],
                sources=["references/rule-matrix.md", "assets/claim-consistency-template.csv"],
            ))

        if app_name and values["name"] and app_name.casefold() != values["name"].casefold() and locale == (metadata.get("primary_locale") or app.get("primary_locale")):
            findings.append(_find(
                id="META-PRIMARY-NAME-MISMATCH",
                title="Primary metadata name differs from review-input app name",
                severity="MEDIUM",
                category="consistency",
                guideline="2.3 Accurate Metadata",
                confidence="CERTAIN",
                evidence=[_loc(metadata_path, f"/locales/{locale}/name", f"metadata={values['name']!r}; config={app_name!r}")],
                rationale="Identity mismatches can indicate the audit is using stale metadata or the wrong build.",
                remediation="Reconcile the release config, bundle display name, and App Store Connect product name.",
                verification=["Confirm the exact app record and build number in App Store Connect."],
                sources=["references/policy-baseline.md"],
            ))

    facts["urls"] = url_fields
    facts["localized_text"] = all_text_by_locale

    # Review access and notes.
    review = metadata.get("review", {}) if isinstance(metadata.get("review"), dict) else {}
    notes = str(review.get("notes") or config.get("review", {}).get("notes") or "").strip()
    if _utf8_len(notes) > METADATA_LIMITS["review_notes_max_utf8_bytes"]:
        findings.append(_find(
            id="META-REVIEW-NOTES-LENGTH",
            title="App Review notes exceed the field limit",
            severity="BLOCKER",
            category="review-access",
            guideline="2.1 App Completeness",
            evidence=[_loc(metadata_path, "/review/notes", f"{_utf8_len(notes)} UTF-8 bytes; maximum {METADATA_LIMITS['review_notes_max_utf8_bytes']}")],
            rationale="Review notes that cannot be saved or are truncated may omit credentials and navigation required to review the app.",
            remediation="Condense notes while retaining exact navigation, demo access, IAP, AI disclosure, hardware, and special configuration details.",
            verification=["Paste the final text into App Store Connect and confirm it saves intact."],
            sources=["references/reviewer-notes-and-appeals.md"],
        ))
    if not notes:
        findings.append(_find(
            id="META-REVIEW-NOTES-MISSING",
            title="App Review notes are empty",
            severity="HIGH",
            category="review-access",
            guideline="2.1 App Completeness",
            evidence=[_loc(metadata_path, "/review/notes", "No review notes supplied")],
            rationale="Complex login, AI, subscription, hardware, regional, or non-obvious features require precise reviewer guidance. Empty notes create avoidable review friction.",
            remediation="Draft concise notes using assets/review-notes-template.md.",
            verification=["Have a person unfamiliar with the app follow only the notes on a fresh install."],
            sources=["references/reviewer-notes-and-appeals.md"],
        ))
    elif len(notes) < 40 or re.fullmatch(r"(?i)(?:n/?a|none|no notes|test the app|thanks)[.! ]*", notes):
        findings.append(_find(
            id="META-REVIEW-NOTES-GENERIC",
            title="App Review notes appear too generic for a reproducible review",
            severity="MEDIUM",
            category="review-access",
            guideline="2.1 App Completeness",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=[_loc(metadata_path, "/review/notes", "Notes are very short or generic", notes)],
            rationale="Reviewers need exact navigation and explanations for non-obvious behavior; a generic note does not prove accessibility.",
            remediation="State exact steps, credentials delivery, backend state, AI consent path, purchases, hardware, and special conditions.",
            verification=["Execute the notes as a black-box reviewer."],
            sources=["references/reviewer-notes-and-appeals.md"],
        ))

    accounts = features.get("accounts", {})
    login_required = bool(accounts.get("login_required"))
    demo = review.get("demo_account", {}) if isinstance(review.get("demo_account"), dict) else {}
    if login_required:
        for key in ("username_env", "password_env"):
            env_name = demo.get(key) or config.get("review", {}).get("demo_account", {}).get(key)
            if not env_name:
                findings.append(_find(
                    id=f"META-DEMO-{key.upper().replace('_', '-')}",
                    title="Login-required app lacks complete demo-account references",
                    severity="BLOCKER",
                    category="review-access",
                    guideline="2.1 App Completeness",
                    evidence=[_loc(metadata_path, f"/review/demo_account/{key}", "Missing environment-variable reference")],
                    rationale="Reviewers must receive working full-access credentials or an approved demo mode.",
                    remediation="Reference a non-expiring review credential through a secure process and include navigation in review notes.",
                    verification=["Test login from a clean install without one-time email, 2FA, or organization approval."],
                    sources=["references/runtime-review.md"],
                ))
        if demo and not demo.get("non_expiring"):
            findings.append(_find(
                id="META-DEMO-EXPIRING",
                title="Review metadata does not confirm a non-expiring demo account",
                severity="HIGH",
                category="review-access",
                guideline="2.1 App Completeness",
                evidence=[_loc(metadata_path, "/review/demo_account/non_expiring", "Value is not true")],
                rationale="Temporary credentials can fail before or during review.",
                remediation="Use a stable account and document any 2FA bypass or preloaded state.",
                verification=["Login twice on separate fresh installs."],
                sources=["references/runtime-review.md"],
            ))

    # Privacy disclosure consistency.
    app_privacy = metadata.get("app_privacy", {}) if isinstance(metadata.get("app_privacy"), dict) else {}
    if not app_privacy.get("completed"):
        findings.append(_find(
            id="META-APP-PRIVACY-INCOMPLETE",
            title="App Privacy answers are not marked complete",
            severity="BLOCKER",
            category="privacy",
            guideline="5.1 Privacy",
            evidence=[_loc(metadata_path, "/app_privacy/completed", "Value is not true")],
            rationale="App Privacy information must accurately represent the release app and its third-party SDKs/data flows.",
            remediation="Complete the App Privacy questionnaire from an evidence-based data inventory.",
            verification=["Compare every declared data type/purpose/recipient with source, archive, backend, and provider configuration."],
            sources=["references/privacy-security.md"],
        ))
    tracking_declared = bool(app_privacy.get("tracking"))
    tracking_feature = bool(features.get("ads_tracking", {}).get("tracking"))
    if tracking_declared != tracking_feature:
        findings.append(_find(
            id="META-TRACKING-CONTRADICTION",
            title="Tracking declaration conflicts with review-input feature scope",
            severity="HIGH",
            category="privacy-consistency",
            guideline="5.1.2 Data Use and Sharing",
            evidence=[_loc(metadata_path, "/app_privacy/tracking", f"metadata={tracking_declared}; feature scope={tracking_feature}")],
            rationale="A tracking mismatch can lead to inaccurate privacy labels or missing App Tracking Transparency behavior.",
            remediation="Determine actual tracking behavior, SDK configuration, and data-linkage purpose; update both declarations and the build.",
            verification=["Inspect the final archive, ATT runtime path, and App Privacy answers together."],
            sources=["references/privacy-security.md"],
        ))

    ai = features.get("ai", {})
    if ai.get("enabled") and ai.get("third_party"):
        declared_third_parties = set()
        for entry in app_privacy.get("data_types", []) if isinstance(app_privacy.get("data_types"), list) else []:
            if isinstance(entry, dict):
                declared_third_parties.update(str(x).casefold() for x in entry.get("third_parties", []) or [])
        missing_providers = [provider for provider in ai.get("providers", []) or [] if str(provider).casefold() not in declared_third_parties]
        if ai.get("personal_data_types") and missing_providers:
            findings.append(_find(
                id="META-AI-PRIVACY-PROVIDER-MISMATCH",
                title="Third-party AI provider is absent from the supplied App Privacy evidence",
                severity="HIGH",
                category="ai-privacy",
                guideline="5.1.1; 5.1.2(i)",
                confidence="HIGH",
                evidence=[_loc(metadata_path, "/app_privacy/data_types", "AI providers not found in third-party evidence", missing_providers)],
                rationale="The privacy policy, privacy labels, consent UI, and actual recipients must consistently disclose personal-data sharing.",
                remediation="Reconcile the provider/subprocessor map with App Privacy answers and consent copy; do not add recipients mechanically if the export format does not expose them.",
                verification=["Trace each declared personal data type through the release network flow and privacy disclosures."],
                sources=["references/ai-review.md", "references/privacy-security.md"],
            ))

    # Age rating.
    age = metadata.get("age_rating", {}) if isinstance(metadata.get("age_rating"), dict) else {}
    if not age.get("completed"):
        findings.append(_find(
            id="META-AGE-RATING-INCOMPLETE",
            title="Age rating questionnaire is not marked complete",
            severity="BLOCKER",
            category="age-rating",
            guideline="2.3.6 Accurate Age Rating",
            evidence=[_loc(metadata_path, "/age_rating/completed", "Value is not true")],
            rationale="Age rating is a required app-level property and must reflect all reasonably accessible content and capabilities.",
            remediation="Complete the current App Store Connect age-rating questionnaire for the worst reasonably reachable content.",
            verification=["Reconcile the resulting rating with AI/UGC/chat, browser access, violence, sexual content, gambling, and regional ratings."],
            sources=["references/app-type-branches.md", "references/ai-review.md"],
        ))
    rating = str(age.get("declared_rating") or "").lower()
    if rating and rating not in VALID_RATINGS:
        findings.append(_find(
            id="META-AGE-RATING-VALUE",
            title="Declared age rating is not in the current Apple rating scale",
            severity="HIGH",
            category="age-rating",
            guideline="2.3.6 Accurate Age Rating",
            evidence=[_loc(metadata_path, "/age_rating/declared_rating", "Unexpected value", rating)],
            rationale="Apple's current global scale uses 4+, 9+, 13+, 16+, and 18+, with regional variants generated from the questionnaire.",
            remediation="Use the exact current App Store Connect result rather than a legacy 12+/17+ value.",
            verification=["Open App Information in App Store Connect and record the current assigned rating."],
            sources=["references/policy-baseline.md"],
        ))
    ai_or_chat = bool(ai.get("enabled") or ai.get("chatbot") or features.get("ugc", {}).get("chat_or_messaging"))
    if ai_or_chat and not age.get("ai_or_chatbot_considered"):
        findings.append(_find(
            id="META-AGE-RATING-AI-OMITTED",
            title="AI/chat capability is not documented in the age-rating rationale",
            severity="HIGH",
            category="age-rating",
            guideline="2.3.6 Accurate Age Rating; 4.7.5",
            confidence="HIGH",
            evidence=[_loc(metadata_path, "/age_rating/ai_or_chatbot_considered", "Value is not true")],
            rationale="Generative or user-directed outputs can expose content beyond intended examples; rating only curated prompts understates reachable content.",
            remediation="Evaluate worst reasonably reachable outputs and answer the current capability/content questions accordingly.",
            verification=["Run the AI safety suite and compare semantic outcomes with the questionnaire."],
            sources=["references/ai-review.md"],
        ))
    if age.get("social_media_capability") and metadata.get("policy_date", "") < "2026-09-01":
        findings.append(_find(
            id="META-SOCIAL-AGE-RATING-SEPTEMBER",
            title="Prepare for September 2026 social-media age-rating questions",
            severity="LOW",
            category="age-rating",
            guideline="Upcoming App Store Connect requirement",
            confidence="HIGH",
            status="NEEDS_REVIEW",
            automation="policy-timeline",
            evidence=[_loc(metadata_path, "/age_rating/social_media_capability", "Social-media capability declared")],
            rationale="Apple announced additional social-media capability questions for the age-rating workflow beginning in September 2026.",
            remediation="Document feed, messaging, user interaction, moderation, and age controls now so the questionnaire can be answered consistently when effective.",
            verification=["Re-run policy freshness after September 1, 2026 and update the metadata export."],
            sources=["references/policy-baseline.md"],
        ))

    # Purchases and subscriptions.
    commerce = features.get("commerce", {})
    iap = metadata.get("iap", []) if isinstance(metadata.get("iap"), list) else []
    if commerce.get("iap") and not iap:
        findings.append(_find(
            id="META-IAP-MISSING",
            title="In-App Purchase is enabled but no IAP review records were supplied",
            severity="BLOCKER",
            category="payments",
            guideline="2.1 App Completeness; 3.1.1 In-App Purchase",
            evidence=[_loc(metadata_path, "/iap", "Empty or missing IAP list")],
            rationale="New or changed purchase products must be available to App Review with complete metadata and review evidence.",
            remediation="Export each product/subscription, include its review screenshot and submission status, and attach it to the app submission.",
            verification=["Use Sandbox to fetch, buy, restore, and reopen every product in the exact release build."],
            sources=["references/business-payments.md"],
        ))
    product_ids: set[str] = set()
    for index, product in enumerate(iap):
        pointer = f"/iap/{index}"
        if not isinstance(product, dict):
            findings.append(_find(
                id=f"META-IAP-{index}-OBJECT",
                title="IAP record is not an object",
                severity="BLOCKER",
                category="payments",
                guideline="2.1 App Completeness",
                evidence=[_loc(metadata_path, pointer, "Expected an object", product)],
                rationale="The product cannot be validated from this export.",
                remediation="Export a complete structured IAP record.",
                verification=["Rerun validate_metadata.py."],
                sources=["references/business-payments.md"],
            ))
            continue
        product_id = str(product.get("product_id") or "")
        if not product_id:
            findings.append(_find(
                id=f"META-IAP-{index}-PRODUCT-ID",
                title="IAP record has no product identifier",
                severity="BLOCKER",
                category="payments",
                guideline="2.1 App Completeness",
                evidence=[_loc(metadata_path, f"{pointer}/product_id", "Missing")],
                rationale="The binary, StoreKit configuration, and App Store Connect product cannot be reconciled without a stable identifier.",
                remediation="Provide the exact App Store Connect product ID.",
                verification=["Compare the product ID with the StoreKit request observed at runtime."],
                sources=["references/business-payments.md"],
            ))
        elif product_id in product_ids:
            findings.append(_find(
                id=f"META-IAP-{index}-DUPLICATE",
                title="Duplicate IAP product identifier in metadata evidence",
                severity="HIGH",
                category="payments",
                guideline="2.1 App Completeness",
                evidence=[_loc(metadata_path, f"{pointer}/product_id", "Duplicate product ID", product_id)],
                rationale="Duplicate records can hide mismatched product types, durations, or review status.",
                remediation="Deduplicate the export and verify the product catalog.",
                verification=["Fetch the product from Sandbox and compare all localized values."],
                sources=["references/business-payments.md"],
            ))
        product_ids.add(product_id)
        if not product.get("submitted_for_review"):
            findings.append(_find(
                id=f"META-IAP-{index}-NOT-SUBMITTED",
                title="IAP product is not marked submitted for review",
                severity="BLOCKER",
                category="payments",
                guideline="2.1 App Completeness; 3.1.1 In-App Purchase",
                evidence=[_loc(metadata_path, f"{pointer}/submitted_for_review", "Value is not true", product_id)],
                rationale="A reviewer cannot approve a purchase path when the referenced product is unavailable to the submission.",
                remediation="Complete and submit the product with the app version.",
                verification=["Confirm the product is attached to the submission and fetches in Sandbox."],
                sources=["references/business-payments.md"],
            ))
        review_screenshot = product.get("review_screenshot")
        if not review_screenshot:
            findings.append(_find(
                id=f"META-IAP-{index}-REVIEW-SCREENSHOT",
                title="IAP record has no review screenshot",
                severity="BLOCKER",
                category="payments",
                guideline="2.1 App Completeness",
                evidence=[_loc(metadata_path, f"{pointer}/review_screenshot", "Missing", product_id)],
                rationale="App Store Connect requires review information showing where the purchase appears in the app.",
                remediation="Attach a clear screenshot of the purchase UI for this product.",
                verification=["Open the product in App Store Connect and confirm the screenshot is saved."],
                sources=["references/business-payments.md"],
            ))
        elif config_path:
            screenshot_path = Path(str(review_screenshot))
            if not screenshot_path.is_absolute():
                screenshot_path = metadata_path.parent / screenshot_path
            if not screenshot_path.exists():
                findings.append(_find(
                    id=f"META-IAP-{index}-REVIEW-SCREENSHOT-PATH",
                    title="Referenced IAP review screenshot is absent from evidence",
                    severity="HIGH",
                    category="payments",
                    guideline="2.1 App Completeness",
                    evidence=[_loc(metadata_path, f"{pointer}/review_screenshot", "File not found", str(screenshot_path))],
                    rationale="The audit cannot confirm that the purchase location shown to Apple matches the final build.",
                    remediation="Export the exact screenshot or correct the evidence path.",
                    verification=["Open the image and reproduce the same screen in the release build."],
                    sources=["references/business-payments.md"],
                ))

    subscription_ui = metadata.get("subscription_ui", {}) if isinstance(metadata.get("subscription_ui"), dict) else {}
    if commerce.get("subscriptions"):
        required_disclosures = {
            "product_name_visible": "subscription product/service name",
            "duration_visible": "renewal duration",
            "localized_price_visible": "localized price",
            "auto_renewal_visible": "auto-renewal/cancellation disclosure",
            "restore_visible": "restore purchases control",
            "privacy_link_visible": "privacy policy link",
            "terms_link_visible": "Terms/EULA link",
        }
        missing = [description for key, description in required_disclosures.items() if not subscription_ui.get(key)]
        if missing:
            findings.append(_find(
                id="META-SUBSCRIPTION-DISCLOSURES",
                title="Subscription UI evidence lacks required material disclosures",
                severity="BLOCKER",
                category="subscriptions",
                guideline="3.1.2 Subscriptions",
                evidence=[_loc(metadata_path, "/subscription_ui", "Missing disclosure evidence", missing)],
                rationale="Users must understand what they receive, renewal term, actual charges, and how to manage/cancel before purchase; policy and terms links must be accessible.",
                remediation="Update the paywall and export evidence for every disclosure using localized StoreKit product data.",
                verification=["Inspect the paywall at all Dynamic Type sizes and complete a Sandbox purchase/restore/cancel journey."],
                sources=["references/business-payments.md"],
            ))
        if any(isinstance(product, dict) and product.get("trial") for product in iap) and not subscription_ui.get("trial_and_post_trial_price_visible"):
            findings.append(_find(
                id="META-SUBSCRIPTION-TRIAL-PRICE",
                title="Free-trial evidence does not show post-trial price and duration",
                severity="BLOCKER",
                category="subscriptions",
                guideline="3.1.2 Subscriptions; 5.6 Developer Code of Conduct",
                evidence=[_loc(metadata_path, "/subscription_ui/trial_and_post_trial_price_visible", "Value is not true")],
                rationale="Trial conversion must be presented clearly before purchase and must not rely on hidden or ambiguous pricing.",
                remediation="Display trial length, recurring duration, localized post-trial price, auto-renewal, and cancellation path together.",
                verification=["Capture the paywall in each target locale/storefront and reconcile it with StoreKit."],
                sources=["references/business-payments.md"],
            ))

    if commerce.get("credits") and not commerce.get("restore_purchases"):
        findings.append(_find(
            id="META-CREDITS-RESTORE",
            title="Digital credits are declared without restore/entitlement recovery evidence",
            severity="HIGH",
            category="payments",
            guideline="3.1.1 In-App Purchase",
            confidence="HIGH",
            evidence=[_loc(metadata_path, "/subscription_ui/restore_visible", "Credits enabled; restore not declared")],
            rationale="Purchased credits may not expire and durable entitlements need a recovery path appropriate to the product type.",
            remediation="Document credit persistence and implement restore/reconciliation behavior for non-consumable entitlements and server-backed balances.",
            verification=["Reinstall, sign in, and confirm balances/entitlements recover correctly."],
            sources=["references/business-payments.md"],
        ))

    terms_present = any(item.get("field") == "terms_url" for item in url_fields) or metadata.get("eula") in {"standard", "custom"}
    if commerce.get("subscriptions") and not terms_present:
        findings.append(_find(
            id="META-TERMS-MISSING",
            title="Subscription metadata has no Terms of Use/EULA evidence",
            severity="BLOCKER",
            category="subscriptions",
            guideline="3.1.2 Subscriptions",
            evidence=[_loc(metadata_path, "/eula", "No terms URL or standard/custom EULA declaration")],
            rationale="Subscription purchase information must provide access to terms and privacy information.",
            remediation="Use Apple's standard EULA or a valid custom EULA and expose it from the paywall/product page as applicable.",
            verification=["Open both links from the release paywall and App Store metadata."],
            sources=["references/business-payments.md"],
        ))

    # Login service branch.
    social = features.get("accounts", {}).get("social_logins", []) or []
    if social and not features.get("accounts", {}).get("privacy_preserving_login") and not features.get("accounts", {}).get("login_exception"):
        findings.append(_find(
            id="META-SOCIAL-LOGIN-EQUIVALENT",
            title="Third-party primary-account login lacks an equivalent privacy-preserving option or documented exception",
            severity="BLOCKER",
            category="login",
            guideline="4.8 Login Services",
            confidence="HIGH",
            evidence=[_loc(metadata_path, "/review/notes", "Social login providers", social)],
            rationale="Apps using third-party/social login for the primary account must also offer an equivalent option with Apple's specified privacy characteristics unless an exception applies.",
            remediation="Implement the equivalent login option (commonly Sign in with Apple) or document the precise guideline exception in review notes.",
            verification=["Create and delete accounts through every login method and compare data requested/displayed."],
            sources=["references/app-type-branches.md"],
        ))

    checks.extend([
        make_check("metadata.lengths", "Metadata field limits", "PASS" if not any(f["id"].endswith("-LENGTH") for f in findings) else "ERROR", mandatory=True, tool="validate_metadata.py", detail="Character and UTF-8 byte limits checked"),
        make_check("metadata.urls.syntax", "Metadata URL syntax", "PASS" if not any(f["id"].endswith("-URL") for f in findings) else "ERROR", mandatory=True, tool="validate_metadata.py", detail=f"{len(url_fields)} URL(s) inventoried; network not checked here"),
        make_check("metadata.privacy", "Privacy metadata", "PASS" if app_privacy.get("completed") else "ERROR", mandatory=True, tool="validate_metadata.py", detail="App Privacy completion declaration"),
        make_check("metadata.age_rating", "Age rating", "PASS" if age.get("completed") else "ERROR", mandatory=True, tool="validate_metadata.py", detail=str(age.get("declared_rating") or "not supplied")),
        make_check("metadata.review_notes", "App Review notes", "PASS" if notes else "NEEDS_REVIEW", mandatory=True, tool="validate_metadata.py", detail=f"{_utf8_len(notes)} UTF-8 bytes"),
        make_check("metadata.iap", "IAP metadata", "PASS" if not commerce.get("iap") or (iap and all(isinstance(p, dict) and p.get("submitted_for_review") and p.get("review_screenshot") for p in iap)) else "ERROR", mandatory=bool(commerce.get("iap")), tool="validate_metadata.py", detail=f"{len(iap)} product(s)"),
    ])

    return {
        "module": "validate_metadata",
        "generated_at": now_iso(),
        "metadata_path": str(metadata_path),
        "facts": facts,
        "checks": checks,
        "findings": findings,
        "tool": {"name": "validate_metadata.py", "status": "OK", "detail": "Local deterministic metadata validation"},
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate App Store Connect metadata, privacy, age-rating, IAP, and subscription evidence.")
    parser.add_argument("--metadata", required=True, help="Path to metadata JSON")
    parser.add_argument("--config", help="Optional review-input.json for cross-field checks")
    parser.add_argument("--output", help="Write structured JSON result")
    parser.add_argument("--strict", action="store_true", help="Exit 2 when any blocker/high finding is open")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        metadata = load_json(args.metadata)
        if not isinstance(metadata, dict):
            raise ReviewInputError("Metadata root must be a JSON object")
        config = load_json(args.config) if args.config else None
        if config is not None and not isinstance(config, dict):
            raise ReviewInputError("Config root must be a JSON object")
        result = validate_metadata(metadata, args.metadata, config=config, config_path=args.config)
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"validate_metadata: {exc}\n")
        return 3
    if args.output:
        dump_json(result, args.output)
    else:
        sys.stdout.write(dump_json(result))
    if args.strict and any(f.get("status") in {"OPEN", "NEEDS_REVIEW", "ERROR"} and f.get("severity") in {"BLOCKER", "HIGH"} for f in result["findings"]):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
