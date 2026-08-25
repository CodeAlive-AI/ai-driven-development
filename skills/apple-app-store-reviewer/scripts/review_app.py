#!/usr/bin/env python3
"""Orchestrate the complete App Store preflight review.

The orchestrator is deliberately fail-closed: unavailable release evidence is
recorded as a mandatory unverified check, never inferred as a pass.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any, Callable, Mapping

from check_policy_freshness import DEFAULT_CATALOG, check_policy_freshness
from check_urls import check_urls
from common import (
    ReviewInputError,
    base_report,
    dump_json,
    finalize_report,
    load_json,
    make_check,
    make_evidence,
    make_finding,
    markdown_report,
    now_iso,
    redact,
    report_exit_code,
    resolve_config_paths,
    sha256_file,
)
from inspect_bundle import inspect_bundle
from inspect_screenshots import inspect_screenshots
from run_xcode_tests import run_xcode_tests
from scan_project import scan_project
from validate_input import DEFAULT_SCHEMA as INPUT_SCHEMA, validate_config
from validate_metadata import validate_metadata
from validate_report import DEFAULT_SCHEMA as REPORT_SCHEMA, validate_report
from validate_evidence import validate_evidence_data

ROOT = Path(__file__).resolve().parents[1]
MANUAL_SCHEMA = ROOT / "assets" / "manual-evidence.schema.json"
MAX_MANIFEST_FILES = 5000
MAX_MANIFEST_HASH_BYTES = 512 * 1024 * 1024


def _module_filename(name: str) -> str:
    return "".join(ch if ch.isalnum() or ch in "._-" else "-" for ch in name).strip("-") + ".json"


def _record_module(report: dict[str, Any], result: Mapping[str, Any], *, namespace: str, modules_dir: Path) -> None:
    safe = redact(dict(result))
    dump_json(safe, modules_dir / _module_filename(namespace))
    report["checks"].extend(safe.get("checks", []) if isinstance(safe.get("checks"), list) else [])
    report["findings"].extend(safe.get("findings", []) if isinstance(safe.get("findings"), list) else [])
    if isinstance(safe.get("facts"), Mapping):
        report["facts"][namespace] = safe["facts"]
    if isinstance(safe.get("tool"), Mapping):
        report["tools"].append(dict(safe["tool"]))
    if isinstance(safe.get("tools"), list):
        report["tools"].extend(item for item in safe["tools"] if isinstance(item, Mapping))


def _run_module(
    report: dict[str, Any],
    *,
    namespace: str,
    modules_dir: Path,
    title: str,
    mandatory: bool,
    function: Callable[[], Mapping[str, Any]],
) -> Mapping[str, Any] | None:
    try:
        result = function()
        _record_module(report, result, namespace=namespace, modules_dir=modules_dir)
        return result
    except Exception as exc:  # Preserve a partial report even when one checker fails.
        detail = f"{type(exc).__name__}: {exc}"
        report["tools"].append({"name": namespace, "status": "ERROR", "detail": redact(detail)})
        report["checks"].append(make_check(
            f"tool.{namespace}", title, "ERROR", mandatory=mandatory, tool=namespace,
            detail=redact(detail),
        ))
        report["findings"].append(make_finding(
            id=f"TOOL-{namespace.upper().replace('.', '-').replace('_', '-')}-ERROR",
            title=f"Review branch failed: {title}",
            severity="HIGH" if mandatory else "MEDIUM",
            category="review-tooling",
            guideline="Evidence integrity",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="tool-error", location=namespace, detail=detail)],
            rationale="The release gate cannot treat an unexecuted or crashed audit branch as passed.",
            remediation="Correct the artifact or checker error, rerun this branch, then rerun the complete preflight.",
            verification=[f"The {namespace} module completes and emits structured evidence."],
            sources=["references/policy-baseline.md"],
            automation="deterministic-orchestration",
        ))
        return None


def _validate_manual_evidence(
    data: Mapping[str, Any],
    path: Path,
    *,
    screenshots_root: Path | None = None,
) -> list[str]:
    result = validate_evidence_data(
        data,
        evidence_path=path,
        schema_path=MANUAL_SCHEMA,
        screenshots_root=screenshots_root,
        required_checks=["screenshots.visual"],
    )
    errors: list[str] = []
    if not result.get("valid"):
        for finding in result.get("findings", [])[:20]:
            if isinstance(finding, Mapping):
                errors.append(f"{finding.get('id')}: {finding.get('title')}")
    return errors


def _ingest_evidence(
    report: dict[str, Any], path: Path, *, namespace: str, modules_dir: Path, mandatory: bool,
    screenshots_root: Path | None = None,
) -> Mapping[str, Any] | None:
    try:
        data = load_json(path)
        if not isinstance(data, Mapping):
            raise ReviewInputError("Evidence root must be an object")
        # Manual/vision evidence has a dedicated schema. Runtime/AI module output
        # is accepted through the report module contract and then report-validated.
        if namespace == "visual-evidence":
            errors = _validate_manual_evidence(data, path, screenshots_root=screenshots_root)
            if errors:
                raise ReviewInputError("; ".join(errors[:20]))
        _record_module(report, data, namespace=namespace, modules_dir=modules_dir)
        report["tools"].append({"name": f"ingest:{namespace}", "status": "PASS", "detail": str(path)})
        return data
    except Exception as exc:
        detail = f"{type(exc).__name__}: {exc}"
        report["checks"].append(make_check(f"evidence.{namespace}", f"Ingest {namespace}", "ERROR", mandatory=mandatory, tool="review_app.py", detail=detail))
        report["findings"].append(make_finding(
            id=f"EVIDENCE-{namespace.upper().replace('_', '-').replace('.', '-')}-INVALID",
            title=f"Provided {namespace} is invalid",
            severity="HIGH" if mandatory else "MEDIUM",
            category="evidence-integrity",
            guideline="Submission evidence",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="file", location=str(path), detail=detail)],
            rationale="Unvalidated evidence cannot satisfy a release gate.",
            remediation="Regenerate the evidence using the bundled schema/tool and rerun the review.",
            verification=["The evidence parses, validates, and its referenced artifacts still match by hash."],
            sources=["assets/manual-evidence.schema.json" if namespace == "visual-evidence" else "assets/review-report.schema.json"],
            automation="deterministic-ingestion",
        ))
        return None


def _path_manifest(path: Path) -> dict[str, Any]:
    record: dict[str, Any] = {"path": str(path), "exists": path.exists()}
    if not path.exists():
        return record
    if path.is_file():
        record.update({"kind": "file", "bytes": path.stat().st_size, "sha256": sha256_file(path)})
        return record
    if not path.is_dir():
        record["kind"] = "other"
        return record
    digest = hashlib.sha256()
    count = 0
    total = 0
    partial = False
    for child in sorted(item for item in path.rglob("*") if item.is_file()):
        try:
            relative = child.relative_to(path).as_posix()
            size = child.stat().st_size
        except OSError:
            partial = True
            continue
        count += 1
        total += size
        if count > MAX_MANIFEST_FILES or total > MAX_MANIFEST_HASH_BYTES:
            partial = True
            break
        digest.update(relative.encode("utf-8", errors="surrogateescape"))
        digest.update(b"\0")
        digest.update(str(size).encode("ascii"))
        digest.update(b"\0")
        try:
            digest.update(bytes.fromhex(sha256_file(child)))
        except OSError:
            partial = True
    record.update({
        "kind": "directory",
        "files_hashed": min(count, MAX_MANIFEST_FILES),
        "bytes_hashed": min(total, MAX_MANIFEST_HASH_BYTES),
        "tree_sha256": digest.hexdigest(),
        "partial": partial,
    })
    return record


def _build_manifest(config_path: Path, config: Mapping[str, Any]) -> dict[str, Any]:
    paths = config.get("paths", {}) if isinstance(config.get("paths"), Mapping) else {}
    manifest = {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "config": _path_manifest(config_path),
        "artifacts": {},
        "limits": {"max_files": MAX_MANIFEST_FILES, "max_hash_bytes": MAX_MANIFEST_HASH_BYTES},
    }
    for key, value in sorted(paths.items()):
        if value:
            manifest["artifacts"][key] = _path_manifest(Path(str(value)))
        else:
            manifest["artifacts"][key] = {"path": None, "exists": False}
    return manifest


def _dedupe_checks(checks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    # The most conservative status wins and evidence is merged. Required
    # placeholders are only added after ingestion when an exact check ID is absent.
    rank = {"ERROR": 7, "OPEN": 6, "NEEDS_REVIEW": 5, "SKIPPED": 4, "PASS": 3, "FIXED": 2, "ACCEPTED_RISK": 1}
    chosen: dict[str, dict[str, Any]] = {}
    for raw in checks:
        if not isinstance(raw, Mapping):
            continue
        item = dict(raw)
        key = str(item.get("id", "")).strip()
        if not key:
            continue
        current = chosen.get(key)
        if current is None or rank.get(str(item.get("status")), 0) > rank.get(str(current.get("status")), 0):
            chosen[key] = item
        elif current is not None and item.get("status") == current.get("status"):
            evidence = current.setdefault("evidence", [])
            for entry in item.get("evidence", []) or []:
                if entry not in evidence:
                    evidence.append(entry)
            if item.get("detail") and item.get("detail") not in str(current.get("detail", "")):
                current["detail"] = (str(current.get("detail", "")) + "; " + str(item["detail"])).strip("; ")
            current["mandatory"] = bool(current.get("mandatory") or item.get("mandatory"))
    return sorted(chosen.values(), key=lambda item: str(item.get("id")))


def _has_check(checks: list[dict[str, Any]], check_id: str) -> bool:
    return any(isinstance(item, Mapping) and str(item.get("id")) == check_id for item in checks)


def _ensure_required_check(
    checks: list[dict[str, Any]],
    *,
    check_id: str,
    title: str,
    tool: str,
    detail: str,
) -> None:
    if not _has_check(checks, check_id):
        checks.append(make_check(check_id, title, "NEEDS_REVIEW", mandatory=True, tool=tool, detail=detail))


def _dedupe_tools(tools: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    output: list[dict[str, Any]] = []
    for item in tools:
        if not isinstance(item, Mapping):
            continue
        encoded = json.dumps(redact(dict(item)), sort_keys=True, ensure_ascii=False)
        if encoded not in seen:
            output.append(redact(dict(item)))
            seen.add(encoded)
    return output


def _claim_rows(config: Mapping[str, Any], metadata: Mapping[str, Any] | None) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    features = config.get("features", {}) if isinstance(config.get("features"), Mapping) else {}
    app = config.get("app", {}) if isinstance(config.get("app"), Mapping) else {}

    def add(claim: str, source: str, expected: str) -> None:
        rows.append({
            "claim": claim,
            "declared_source": source,
            "expected_release_behavior": expected,
            "binary_or_source": "UNVERIFIED",
            "runtime": "UNVERIFIED",
            "metadata": "UNVERIFIED",
            "screenshots": "UNVERIFIED",
            "privacy": "UNVERIFIED",
            "age_rating": "UNVERIFIED",
            "iap_paywall": "UNVERIFIED",
            "review_notes": "UNVERIFIED",
            "verdict": "NEEDS_REVIEW",
            "evidence": "",
        })

    add(f"App identity: {app.get('name', '')} / {app.get('bundle_id', '')}", "review-input.app", "Matches the final bundle and every locale")
    ai = features.get("ai", {}) if isinstance(features.get("ai"), Mapping) else {}
    if ai.get("enabled"):
        add(f"AI feature; providers={', '.join(ai.get('providers', []) or [])}", "review-input.features.ai", "Actual endpoints, consent, privacy answers, age rating, and screenshots agree")
        if ai.get("third_party"):
            add("Third-party AI informed consent before personal-data transmission", "review-input.features.ai", "First transmission is impossible before explicit permission; denial is coherent")
    accounts = features.get("accounts", {}) if isinstance(features.get("accounts"), Mapping) else {}
    if accounts.get("creation"):
        add("Account creation and in-app deletion", "review-input.features.accounts", "All account/login methods can reach complete deletion")
    commerce = features.get("commerce", {}) if isinstance(features.get("commerce"), Mapping) else {}
    if commerce.get("iap"):
        add("Digital purchase/subscription via IAP", "review-input.features.commerce", "Product records, paywall, localized price, restore/manage, and Sandbox all agree")
    ugc = features.get("ugc", {}) if isinstance(features.get("ugc"), Mapping) else {}
    if ugc.get("enabled"):
        add("User-generated/public content controls", "review-input.features.ugc", "Filtering, reporting, blocking, support, moderation, and age rating are observable")
    for permission in features.get("permissions", []) or []:
        add(f"Permission: {permission}", "review-input.features.permissions", "Usage is necessary, purpose string is specific, denial/revocation state works")
    if metadata and isinstance(metadata.get("locales"), Mapping):
        for locale, localized in metadata["locales"].items():
            if isinstance(localized, Mapping):
                for field in ("name", "subtitle", "promotional_text"):
                    value = str(localized.get(field) or "").strip()
                    if value:
                        add(f"{locale} {field}: {value}", f"metadata.locales.{locale}.{field}", "Claim is demonstrably true in the release build")
    return rows


def _write_claim_matrix(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys()) if rows else [
        "claim", "declared_source", "expected_release_behavior", "binary_or_source", "runtime", "metadata",
        "screenshots", "privacy", "age_rating", "iap_paywall", "review_notes", "verdict", "evidence",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_remediation(report: Mapping[str, Any], path: Path) -> None:
    lines = ["# Prioritized remediation plan", "", f"Generated: {report.get('generated_at', '')}", ""]
    unresolved = [finding for finding in report.get("findings", []) if finding.get("status") in {"OPEN", "NEEDS_REVIEW", "ERROR"}]
    if not unresolved:
        lines.append("No unresolved findings.")
    for index, finding in enumerate(unresolved, start=1):
        lines.extend([
            f"## {index}. [{finding.get('severity')}] {finding.get('id')}: {finding.get('title')}",
            "", finding.get("remediation", ""), "", "Verification:",
        ])
        for step in finding.get("verification", []):
            lines.append(f"- {step}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def _review_notes_draft(config: Mapping[str, Any], metadata: Mapping[str, Any] | None) -> str:
    app = config.get("app", {})
    features = config.get("features", {})
    review = config.get("review", {})
    ai = features.get("ai", {}) if isinstance(features, Mapping) else {}
    commerce = features.get("commerce", {}) if isinstance(features, Mapping) else {}
    accounts = features.get("accounts", {}) if isinstance(features, Mapping) else {}
    notes = [
        f"# App Review notes draft — {app.get('name', '')}", "",
        f"Bundle ID: `{app.get('bundle_id', '')}`  ",
        f"Version/build: `{app.get('version', '')}` / `{app.get('build', '')}`", "",
        "## Review access", "",
    ]
    if accounts.get("login_required"):
        demo = review.get("demo_account", {})
        notes.append(f"Use the non-expiring review credentials supplied securely through `{demo.get('username_env', 'USERNAME_ENV')}` and `{demo.get('password_env', 'PASSWORD_ENV')}`. Do not paste credentials into this file.")
        if demo.get("two_factor_bypass"):
            notes.append(f"2FA/review access: {demo.get('two_factor_bypass')}")
    else:
        notes.append("No login is required to reach the core feature.")
    notes.extend(["", "## Exact reviewer journey", "", "1. Launch from a clean install.", "2. Follow the core feature path and verify the result/error/empty states."])
    if ai.get("enabled"):
        notes.extend([
            "3. Open the AI feature. Before the first applicable third-party transmission, review the disclosure and explicit permission control.",
            f"4. Declared AI provider(s): {', '.join(ai.get('providers', []) or ['REPLACE'])}. Declared personal-data categories: {', '.join(ai.get('personal_data_types', []) or ['none'])}.",
            "5. Decline first and verify that no data is sent; then grant permission and run the synthetic review case.",
        ])
    if commerce.get("iap"):
        notes.append("6. Open the paywall, purchase the submitted Sandbox product, restore purchases, and open Manage Subscription.")
    if accounts.get("creation"):
        notes.append("7. Account deletion path: REPLACE WITH EXACT TAP-BY-TAP NAVIGATION and confirm scope/timing.")
    notes.extend([
        "", "## Production dependencies and special setup", "",
        f"Backend declared live: {bool(review.get('backend_live'))}.",
        f"Required hardware: {', '.join(review.get('hardware', []) or ['none'])}.",
        "Regional/storefront exceptions or entitlements: REPLACE OR STATE NONE.",
        "", "## Attachments", "",
    ])
    for attachment in review.get("attachments", []) or []:
        notes.append(f"- {attachment}")
    if not review.get("attachments"):
        notes.append("- Add a short screen recording or evidence attachment for any non-obvious flow.")
    notes.extend(["", "## Existing developer notes", "", str(review.get("notes") or (metadata or {}).get("review", {}).get("notes") or "None supplied.")])
    return "\n".join(notes) + "\n"


def review_app(
    config_path: str | Path,
    *,
    output_dir: str | Path,
    network: bool = False,
    strict: bool = False,
    run_runtime: bool = False,
    policy_catalog: str | Path = DEFAULT_CATALOG,
) -> dict[str, Any]:
    config_path = Path(config_path).resolve()
    output_path = Path(output_dir).resolve()
    modules_dir = output_path / "modules"
    contact_sheets = output_path / "contact-sheets"
    output_path.mkdir(parents=True, exist_ok=True)
    modules_dir.mkdir(parents=True, exist_ok=True)

    raw = load_json(config_path)
    if not isinstance(raw, Mapping):
        raise ReviewInputError("Config root must be a JSON object")
    report = base_report(raw, strict=strict)

    input_result = _run_module(
        report, namespace="input", modules_dir=modules_dir, title="Review input validation", mandatory=True,
        function=lambda: validate_config(raw, config_path, schema_path=INPUT_SCHEMA),
    )
    config = (input_result or {}).get("resolved_config") if isinstance(input_result, Mapping) else None
    if not isinstance(config, Mapping):
        config = resolve_config_paths(raw, config_path)
    report["app"] = redact(config.get("app", {}))
    report["scope"] = redact(config.get("scope", {}))
    paths = config.get("paths", {}) if isinstance(config.get("paths"), Mapping) else {}
    features = config.get("features", {}) if isinstance(config.get("features"), Mapping) else {}

    catalog = load_json(policy_catalog)
    if not isinstance(catalog, Mapping):
        raise ReviewInputError("Policy catalog root must be an object")
    policy_result = _run_module(
        report, namespace="policy", modules_dir=modules_dir, title="Current Apple policy fingerprint", mandatory=True,
        function=lambda: check_policy_freshness(catalog, catalog_path=policy_catalog, network=network),
    )
    if isinstance(policy_result, Mapping) and isinstance(policy_result.get("policy"), Mapping):
        report["policy"].update(redact(policy_result["policy"]))

    metadata: Mapping[str, Any] | None = None
    metadata_path = Path(str(paths.get("metadata"))) if paths.get("metadata") else None
    if metadata_path and metadata_path.exists():
        loaded = load_json(metadata_path)
        if isinstance(loaded, Mapping):
            metadata = loaded
            _run_module(
                report, namespace="metadata", modules_dir=modules_dir, title="App Store metadata validation", mandatory=True,
                function=lambda: validate_metadata(metadata, metadata_path, config=config, config_path=config_path),
            )
            _run_module(
                report, namespace="urls", modules_dir=modules_dir, title="Public metadata URL validation", mandatory=True,
                function=lambda: check_urls(metadata, metadata_path, network=network),
            )
        else:
            report["findings"].append(make_finding(
                id="METADATA-ROOT-INVALID", title="Metadata export root is not an object", severity="BLOCKER",
                category="metadata", guideline="2.1 App Completeness; 2.3 Accurate Metadata", confidence="CERTAIN",
                evidence=[make_evidence(kind="file", location=str(metadata_path), detail="Expected a JSON object")],
                rationale="The release product page cannot be validated from this artifact.", remediation="Regenerate metadata.json using the bundled example.",
                verification=["validate_metadata.py parses the export"], sources=["assets/metadata.example.json"],
            ))

    project_path = Path(str(paths.get("project"))) if paths.get("project") else None
    source_result = None
    if project_path and project_path.exists():
        source_result = _run_module(
            report, namespace="source", modules_dir=modules_dir, title="Static source/configuration scan", mandatory=True,
            function=lambda: scan_project(project_path, config=config, config_path=config_path),
        )

    archive_path = Path(str(paths.get("archive"))) if paths.get("archive") else None
    if archive_path and archive_path.exists():
        _run_module(
            report, namespace="bundle", modules_dir=modules_dir, title="Final release bundle inspection", mandatory=True,
            function=lambda: inspect_bundle(archive_path, config=config, config_path=config_path),
        )

    screenshots_path = Path(str(paths.get("screenshots"))) if paths.get("screenshots") else None
    screenshot_result = None
    if screenshots_path and screenshots_path.exists():
        screenshot_result = _run_module(
            report, namespace="screenshots", modules_dir=modules_dir, title="Deterministic screenshot inspection", mandatory=True,
            function=lambda: inspect_screenshots(screenshots_path, config=config, config_path=config_path, contact_sheets=contact_sheets),
        )

    visual_path = Path(str(paths.get("visual_results"))) if paths.get("visual_results") else None
    visual_result = None
    if visual_path and visual_path.exists():
        visual_result = _ingest_evidence(report, visual_path, namespace="visual-evidence", modules_dir=modules_dir, mandatory=True, screenshots_root=screenshots_path)
    _ensure_required_check(
        report["checks"], check_id="screenshots.visual",
        title="Agent visual review of every submitted screenshot", tool="ai-agent-vision",
        detail=(
            "No explicit screenshots.visual check was supplied. Review every original and contact sheet, then provide paths.visual_results."
            if screenshots_path
            else "Final App Store screenshots were not supplied, so full-resolution visual review could not be performed."
        ),
    )

    runtime_path = Path(str(paths.get("runtime_results"))) if paths.get("runtime_results") else None
    runtime_result = None
    if run_runtime:
        runtime_result = _run_module(
            report, namespace="runtime", modules_dir=modules_dir, title="Configured Xcode release tests", mandatory=True,
            function=lambda: run_xcode_tests(config, config_path=config_path, output_dir=output_path / "runtime"),
        )
    elif runtime_path and runtime_path.exists():
        runtime_result = _ingest_evidence(report, runtime_path, namespace="runtime", modules_dir=modules_dir, mandatory=True)
    _ensure_required_check(
        report["checks"], check_id="runtime.reviewer-journey",
        title="Clean-install reviewer journey and failure-state verification", tool="human/XCUITest",
        detail="No explicit runtime.reviewer-journey check was supplied or executed.",
    )

    ai = features.get("ai", {}) if isinstance(features.get("ai"), Mapping) else {}
    ai_path = Path(str(paths.get("ai_results"))) if paths.get("ai_results") else None
    ai_result = None
    if ai.get("enabled") and ai_path and ai_path.exists():
        ai_result = _ingest_evidence(report, ai_path, namespace="ai", modules_dir=modules_dir, mandatory=True)
    if ai.get("enabled"):
        _ensure_required_check(
            report["checks"], check_id="ai.adapter-contracts",
            title="AI deterministic safety/privacy adapter contracts", tool="run_ai_safety_suite.py",
            detail="No explicit ai.adapter-contracts check was supplied.",
        )
        _ensure_required_check(
            report["checks"], check_id="ai.semantic-review",
            title="Manual semantic AI output and worst-case age-rating review", tool="vision/language review",
            detail="No explicit ai.semantic-review check was supplied; inspect worst reasonably reachable outputs.",
        )

    commerce = features.get("commerce", {}) if isinstance(features.get("commerce"), Mapping) else {}
    if commerce.get("iap"):
        if not any(str(check.get("id", "")).startswith("payments.sandbox") and check.get("status") == "PASS" for check in report["checks"]):
            report["checks"].append(make_check(
                "payments.sandbox-runtime", "Sandbox purchase/restore/manage/cancel journey", "NEEDS_REVIEW", mandatory=True,
                tool="StoreKit/XCUITest/manual", detail="No passing Sandbox purchase evidence was identified.",
            ))

    specialized = features.get("specialized", []) or []
    for branch in specialized:
        report["checks"].append(make_check(
            f"specialized.{branch}", f"Specialized category review: {branch}", "NEEDS_REVIEW", mandatory=True,
            tool="manual specialist review", detail=f"Apply references/app-type-branches.md and current licensing/regional requirements for {branch}.",
        ))

    # Guideline 4.2/4.3 risk is partly discretionary. Require a dossier whenever
    # static/deterministic findings signal thin-wrapper, web aggregation, copycat,
    # or template risk; do not claim the dossier itself proves approval.
    value_risk = any(
        ("4.2" in str(finding.get("guideline")) or "4.3" in str(finding.get("guideline")) or "thin" in str(finding.get("title", "")).casefold() or "wrapper" in str(finding.get("title", "")).casefold())
        and finding.get("status") in {"OPEN", "NEEDS_REVIEW", "ERROR"}
        for finding in report["findings"]
    )
    dossier_path = Path(str(paths.get("native_value_dossier"))) if paths.get("native_value_dossier") else None
    if value_risk:
        report["checks"].append(make_check(
            "design.native-value-dossier", "Guideline 4.2/4.3 native-value dossier", "PASS" if dossier_path and dossier_path.exists() else "NEEDS_REVIEW",
            mandatory=True, tool="manual product review", detail=str(dossier_path) if dossier_path and dossier_path.exists() else "Required because thin/template/wrapper risk was detected.",
        ))

    rows = _claim_rows(config, metadata)
    claim_path = output_path / "claim-consistency.csv"
    _write_claim_matrix(rows, claim_path)
    report["checks"].append(make_check(
        "consistency.claim-matrix", "Cross-artifact claim consistency matrix", "NEEDS_REVIEW", mandatory=True,
        tool="review_app.py + agent", detail=f"Generated {len(rows)} rows at {claim_path}; fill evidence and verdicts before submission.",
        evidence=[make_evidence(kind="file", location=str(claim_path), detail="Generated claim matrix")],
    ))

    manifest = _build_manifest(config_path, config)
    dump_json(manifest, output_path / "evidence-manifest.json")
    report["inputs"] = manifest

    report["checks"] = _dedupe_checks(report["checks"])
    report["tools"] = _dedupe_tools(report["tools"])
    report = finalize_report(report, strict=strict)

    # Report validation itself is a mandatory release check. Add a structured
    # blocker only when the first validation pass detects an invalid report.
    validation = validate_report(report, schema_path=REPORT_SCHEMA, strict=strict)
    if validation["valid"]:
        report["checks"].append(make_check("report.schema", "Final report schema and gate invariants", "PASS", mandatory=True, tool="validate_report.py", detail="Report validates"))
    else:
        report["checks"].append(make_check("report.schema", "Final report schema and gate invariants", "ERROR", mandatory=True, tool="validate_report.py", detail=f"{len(validation['errors'])} validation error(s)"))
        report["findings"].append(make_finding(
            id="REPORT-VALIDATION-FAILED", title="Generated review report failed validation", severity="BLOCKER",
            category="evidence-integrity", guideline="Release gate", confidence="CERTAIN",
            evidence=[make_evidence(kind="validation", location=str(output_path / "report-validation.json"), detail="Report validation errors", value=validation["errors"][:20])],
            rationale="An internally inconsistent report cannot support a release decision.", remediation="Correct the producing checker or evidence, regenerate the report, and rerun validate_report.py --strict.",
            verification=["validate_report.py exits 0"], sources=["assets/review-report.schema.json"], automation="deterministic-validation",
        ))
    report["checks"] = _dedupe_checks(report["checks"])
    report = finalize_report(report, strict=strict)
    validation = validate_report(report, schema_path=REPORT_SCHEMA, strict=strict)

    dump_json(report, output_path / "report.json")
    (output_path / "report.md").write_text(markdown_report(report), encoding="utf-8")
    dump_json(validation, output_path / "report-validation.json")
    _write_remediation(report, output_path / "remediation-plan.md")
    (output_path / "app-review-notes-draft.md").write_text(_review_notes_draft(config, metadata), encoding="utf-8")
    dump_json({
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "visual_queue": (screenshot_result or {}).get("facts", {}).get("visual_queue_path") if isinstance(screenshot_result, Mapping) else None,
        "next_actions": [
            "Resolve all blocker/high findings.",
            "Complete every mandatory NEEDS_REVIEW/SKIPPED/ERROR check.",
            "Fill claim-consistency.csv with evidence and rerun the complete release audit.",
        ],
    }, output_path / "next-actions.json")
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the complete Apple App Store preflight skill against review-input.json.")
    parser.add_argument("--config", required=True, help="Path to review-input.json")
    parser.add_argument("--output-dir", required=True, help="Directory for the report and evidence package")
    parser.add_argument("--network", action="store_true", help="Explicitly enable controlled official-policy and public-URL HTTPS checks")
    parser.add_argument("--strict", action="store_true", help="Treat open medium findings as conditionally ready")
    parser.add_argument("--run-runtime", action="store_true", help="Execute configured xcodebuild tests rather than only ingesting runtime_results")
    parser.add_argument("--policy-catalog", default=str(DEFAULT_CATALOG), help="Pinned policy source catalog")
    parser.add_argument("--always-zero", action="store_true", help="Return 0 after writing the report regardless of gate")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        report = review_app(
            args.config,
            output_dir=args.output_dir,
            network=args.network,
            strict=args.strict,
            run_runtime=args.run_runtime,
            policy_catalog=args.policy_catalog,
        )
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"review_app: {exc}\n")
        return 3
    sys.stdout.write(dump_json({
        "report": str((Path(args.output_dir).resolve() / "report.json")),
        "gate": report.get("gate"),
    }))
    return 0 if args.always_zero else report_exit_code(report)


if __name__ == "__main__":
    raise SystemExit(main())
