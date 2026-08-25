#!/usr/bin/env python3
"""Inspect a final .xcarchive, .app, or .ipa without modifying it."""

from __future__ import annotations

import argparse
import json
import os
import plistlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any, Iterable, Mapping

from catalogs import (
    INFO_PLIST_NAMES,
    LISTED_THIRD_PARTY_SDKS,
    PERMISSION_USAGE_KEYS,
    PRIVATE_OR_DEPRECATED_PATTERNS,
    PRIVACY_MANIFEST_NAME,
    REQUIRED_REASON_API_CATEGORIES,
)
from common import (
    ReviewInputError,
    dump_json,
    load_json,
    make_check,
    make_evidence,
    make_finding,
    now_iso,
    resolve_config_paths,
    sha256_file,
)

MAX_BINARY_SCAN_BYTES = 256 * 1024 * 1024
PURPOSE_GENERIC = {"needed", "required", "permission required", "allow access", "access", "used by app", "we need access"}
DEVICE_FAMILY_CODES = {
    1: "iphone",
    2: "ipad",
    3: "apple-tv",
    4: "apple-watch",
    6: "mac",
    7: "vision-pro",
}
SDK_PLATFORM_PREFIXES = {
    "iphoneos": "ios",
    "iphonesimulator": "ios-simulator",
    "appletvos": "tvos",
    "appletvsimulator": "tvos-simulator",
    "watchos": "watchos",
    "watchsimulator": "watchos-simulator",
    "xros": "visionos",
    "xrsimulator": "visionos-simulator",
    "macosx": "macos",
}
DISALLOWED_ARCHS_FOR_DEVICE = {"i386", "x86_64"}
PRIVATE_FRAMEWORK_NAMES = {
    "MobileInstallation", "SpringBoardServices", "BackBoardServices", "GraphicsServices",
    "AppSupport", "AppleAccount", "FrontBoard", "MobileGestalt", "RunningBoardServices",
}


def _run(command: list[str], *, timeout: int = 30) -> tuple[int, str, str]:
    try:
        completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
        return completed.returncode, completed.stdout, completed.stderr
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 127, "", str(exc)


def _safe_extract(zf: zipfile.ZipFile, destination: Path) -> None:
    destination = destination.resolve()
    for member in zf.infolist():
        member_path = (destination / member.filename).resolve()
        if destination != member_path and destination not in member_path.parents:
            raise ReviewInputError(f"Unsafe archive member path: {member.filename}")
    zf.extractall(destination)


def _locate_app(input_path: Path, temp_root: Path) -> tuple[Path, str]:
    if input_path.is_dir() and input_path.suffix == ".app":
        return input_path, "app"
    if input_path.is_dir() and input_path.suffix == ".xcarchive":
        applications = input_path / "Products" / "Applications"
        apps = sorted(applications.glob("*.app")) if applications.exists() else []
        if not apps:
            apps = sorted(input_path.rglob("*.app"))
        if not apps:
            raise ReviewInputError(f"No .app bundle found in archive: {input_path}")
        return apps[0], "xcarchive"
    if input_path.is_file() and input_path.suffix.lower() == ".ipa":
        try:
            with zipfile.ZipFile(input_path) as zf:
                _safe_extract(zf, temp_root)
        except (zipfile.BadZipFile, OSError) as exc:
            raise ReviewInputError(f"Unable to extract IPA: {exc}") from exc
        apps = sorted((temp_root / "Payload").glob("*.app"))
        if not apps:
            apps = sorted(temp_root.rglob("*.app"))
        if not apps:
            raise ReviewInputError("IPA contains no Payload/*.app")
        return apps[0], "ipa"
    raise ReviewInputError("--bundle must point to a .xcarchive directory, .app directory, or .ipa file")


def _load_plist(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        with path.open("rb") as handle:
            value = plistlib.load(handle)
        return (value if isinstance(value, dict) else None), None
    except (OSError, plistlib.InvalidFileException, ValueError, TypeError) as exc:
        return None, str(exc)


def _find_executable(app_path: Path, info: Mapping[str, Any]) -> Path | None:
    name = info.get("CFBundleExecutable")
    if isinstance(name, str) and name:
        candidate = app_path / name
        if candidate.exists():
            return candidate
    # macOS layout.
    if isinstance(name, str) and name:
        candidate = app_path / "Contents" / "MacOS" / name
        if candidate.exists():
            return candidate
    return None


def _info_plist_path(app_path: Path) -> Path:
    direct = app_path / "Info.plist"
    mac = app_path / "Contents" / "Info.plist"
    if direct.exists():
        return direct
    if mac.exists():
        return mac
    raise ReviewInputError(f"No Info.plist in app bundle: {app_path}")


def _relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _evidence(app_path: Path, path: Path, detail: str, value: Any | None = None) -> dict[str, Any]:
    return make_evidence(kind="bundle", location=_relative(path, app_path), detail=detail, value=value)


def _sdk_major(sdk_name: Any) -> tuple[str | None, int | None]:
    value = str(sdk_name or "").lower()
    for prefix, platform in SDK_PLATFORM_PREFIXES.items():
        if value.startswith(prefix):
            match = re.search(r"(\d+)", value[len(prefix):])
            return platform, int(match.group(1)) if match else None
    return None, None


def _xcode_build_number(value: Any) -> int | None:
    text = str(value or "")
    digits = re.sub(r"\D", "", text)
    try:
        return int(digits) if digits else None
    except ValueError:
        return None


def _parse_privacy_manifests(app_path: Path) -> tuple[list[tuple[Path, dict[str, Any]]], list[dict[str, Any]]]:
    manifests: list[tuple[Path, dict[str, Any]]] = []
    errors: list[dict[str, Any]] = []
    for path in sorted(app_path.rglob(PRIVACY_MANIFEST_NAME)):
        data, error = _load_plist(path)
        if data is None:
            errors.append(_evidence(app_path, path, f"Unable to parse privacy manifest: {error}"))
        else:
            manifests.append((path, data))
    return manifests, errors


def _framework_roots(app_path: Path) -> list[Path]:
    candidates = [app_path / "Frameworks", app_path / "Contents" / "Frameworks"]
    roots = [path for path in candidates if path.exists()]
    for plug_in in (app_path / "PlugIns", app_path / "Watch"):
        if plug_in.exists():
            roots.append(plug_in)
    return roots


def _embedded_frameworks(app_path: Path) -> list[Path]:
    values: list[Path] = []
    for root in _framework_roots(app_path):
        values.extend(root.rglob("*.framework"))
        values.extend(root.rglob("*.xcframework"))
    return sorted(set(values))


def _privacy_manifest_reasons(manifests: Iterable[tuple[Path, dict[str, Any]]]) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for _, manifest in manifests:
        entries = manifest.get("NSPrivacyAccessedAPITypes", [])
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            category = entry.get("NSPrivacyAccessedAPIType")
            reasons = entry.get("NSPrivacyAccessedAPITypeReasons", [])
            if isinstance(category, str) and isinstance(reasons, list):
                result.setdefault(category, set()).update(str(reason) for reason in reasons)
    return result


def _framework_name(path: Path) -> str:
    name = path.name
    for suffix in (".framework", ".xcframework"):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return path.stem


def _strings_scan(executable: Path, patterns: Iterable[str]) -> list[str]:
    if not executable.exists():
        return []
    try:
        if executable.stat().st_size > MAX_BINARY_SCAN_BYTES:
            return []
    except OSError:
        return []
    strings_tool = shutil.which("strings")
    if not strings_tool:
        return []
    code, stdout, _ = _run([strings_tool, "-a", str(executable)], timeout=45)
    if code != 0:
        return []
    lowered = stdout.casefold()
    return sorted({pattern for pattern in patterns if pattern.casefold() in lowered})


def inspect_bundle(
    bundle: str | Path,
    *,
    config: Mapping[str, Any] | None = None,
    config_path: str | Path | None = None,
) -> dict[str, Any]:
    input_path = Path(bundle).resolve()
    if not input_path.exists():
        raise ReviewInputError(f"Bundle path not found: {input_path}")
    config = dict(config or {})
    if config_path:
        config = resolve_config_paths(config, config_path)
    app_config = config.get("app", {})
    features = config.get("features", {})

    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    tools: list[dict[str, Any]] = []

    with tempfile.TemporaryDirectory(prefix="appstore-review-bundle-") as temp:
        app_path, container_type = _locate_app(input_path, Path(temp))
        info_path = _info_plist_path(app_path)
        info, error = _load_plist(info_path)
        if info is None:
            raise ReviewInputError(f"Unable to parse {info_path}: {error}")
        executable = _find_executable(app_path, info)
        manifests, manifest_errors = _parse_privacy_manifests(app_path)
        frameworks = _embedded_frameworks(app_path)

        facts: dict[str, Any] = {
            "input": str(input_path),
            "container_type": container_type,
            "app_path": str(app_path),
            "input_sha256": sha256_file(input_path) if input_path.is_file() else None,
            "bundle_id": info.get("CFBundleIdentifier"),
            "display_name": info.get("CFBundleDisplayName") or info.get("CFBundleName"),
            "version": info.get("CFBundleShortVersionString"),
            "build": info.get("CFBundleVersion"),
            "xcode": info.get("DTXcode"),
            "xcode_build": info.get("DTXcodeBuild"),
            "sdk_name": info.get("DTSDKName"),
            "sdk_build": info.get("DTSDKBuild"),
            "platform_name": info.get("DTPlatformName"),
            "minimum_os": info.get("MinimumOSVersion") or info.get("LSMinimumSystemVersion"),
            "device_family_codes": info.get("UIDeviceFamily", []),
            "executable": str(executable) if executable else None,
            "privacy_manifests": [_relative(path, app_path) for path, _ in manifests],
            "frameworks": [_relative(path, app_path) for path in frameworks],
        }

        checks.append(make_check("bundle.info_plist", "Resolved bundle Info.plist", "PASS", mandatory=True, tool="plistlib", detail=_relative(info_path, app_path)))
        if not executable:
            findings.append(make_finding(
                id="BUNDLE-EXECUTABLE-MISSING",
                title="Bundle executable is missing",
                severity="BLOCKER",
                category="binary",
                guideline="2.1 App Completeness",
                confidence="CERTAIN",
                evidence=[_evidence(app_path, info_path, "CFBundleExecutable does not resolve to a file", info.get("CFBundleExecutable"))],
                rationale="The release bundle is incomplete or the audit is pointed at an invalid app package.",
                remediation="Rebuild/archive the correct release target and inspect the exported artifact.",
                verification=["Open the archive in Xcode Organizer and run Validate App."],
                sources=["references/policy-baseline.md"],
            ))
            checks.append(make_check("bundle.executable", "Bundle executable", "ERROR", mandatory=True, tool="filesystem", detail="Executable not found"))
        else:
            checks.append(make_check("bundle.executable", "Bundle executable", "PASS", mandatory=True, tool="filesystem", detail=_relative(executable, app_path)))

        # Identity consistency.
        identity_fields = {
            "bundle_id": ("CFBundleIdentifier", info.get("CFBundleIdentifier")),
            "version": ("CFBundleShortVersionString", info.get("CFBundleShortVersionString")),
            "build": ("CFBundleVersion", info.get("CFBundleVersion")),
        }
        for config_key, (plist_key, actual) in identity_fields.items():
            expected = app_config.get(config_key)
            if expected not in (None, "") and str(expected) != str(actual or ""):
                findings.append(make_finding(
                    id=f"BUNDLE-IDENTITY-{config_key.upper()}",
                    title=f"Final bundle {config_key.replace('_', ' ')} does not match review input",
                    severity="BLOCKER",
                    category="artifact-consistency",
                    guideline="2.1 App Completeness; 2.3 Accurate Metadata",
                    confidence="CERTAIN",
                    evidence=[_evidence(app_path, info_path, f"{plist_key}={actual!r}; expected={expected!r}")],
                    rationale="The audit may be reviewing the wrong app record/build, so all metadata and runtime conclusions are unsafe.",
                    remediation="Use the exact archive selected in App Store Connect or correct review-input.json.",
                    verification=["Compare bundle ID, version, and build in Xcode Organizer and App Store Connect."],
                    sources=["references/policy-baseline.md"],
                ))

        # Current Xcode/SDK minimum.
        xcode_number = _xcode_build_number(info.get("DTXcode"))
        sdk_platform, sdk_major = _sdk_major(info.get("DTSDKName"))
        facts["sdk_platform"] = sdk_platform
        facts["sdk_major"] = sdk_major
        if xcode_number is None:
            findings.append(make_finding(
                id="BUNDLE-XCODE-UNVERIFIED",
                title="Xcode build metadata is absent from the final bundle",
                severity="HIGH",
                category="submission-requirements",
                guideline="App Store submission SDK requirements",
                confidence="HIGH",
                status="NEEDS_REVIEW",
                automation="deterministic",
                evidence=[_evidence(app_path, info_path, "DTXcode is missing", info.get("DTXcode"))],
                rationale="The pinned April 28, 2026 upload minimum cannot be verified from this artifact.",
                remediation="Inspect a distribution archive generated by Xcode 26 or later and preserve its build metadata.",
                verification=["Run xcodebuild -version and Xcode Organizer Validate App on the exact archive."],
                sources=["references/policy-baseline.md"],
            ))
        elif xcode_number < 2600:
            findings.append(make_finding(
                id="BUNDLE-XCODE-TOO-OLD",
                title="Bundle was built with an Xcode version below the current upload minimum",
                severity="BLOCKER",
                category="submission-requirements",
                guideline="App Store submission SDK requirements",
                confidence="CERTAIN",
                evidence=[_evidence(app_path, info_path, f"DTXcode={info.get('DTXcode')}; minimum baseline is Xcode 26")],
                rationale="Since April 28, 2026, App Store Connect uploads require Xcode 26 or later.",
                remediation="Rebuild and archive with a supported Xcode 26+ release using the required platform SDK.",
                verification=["Inspect DTXcode/DTSDKName in the new archive and run Validate App."],
                sources=["references/policy-baseline.md"],
            ))
        if sdk_platform and sdk_platform.endswith("-simulator"):
            findings.append(make_finding(
                id="BUNDLE-SIMULATOR-SDK",
                title="Submission bundle was built against a simulator SDK",
                severity="BLOCKER",
                category="submission-requirements",
                guideline="2.1 App Completeness; upload validation",
                confidence="CERTAIN",
                evidence=[_evidence(app_path, info_path, f"DTSDKName={info.get('DTSDKName')}")],
                rationale="Simulator builds cannot be submitted to the App Store.",
                remediation="Archive the device/distribution target in Release configuration.",
                verification=["Validate the archive in Xcode Organizer."],
                sources=["references/policy-baseline.md"],
            ))
        elif sdk_platform in {"ios", "tvos", "watchos", "visionos", "macos"} and sdk_major is not None and sdk_major < 26:
            findings.append(make_finding(
                id="BUNDLE-SDK-TOO-OLD",
                title="Bundle uses a platform SDK below the current upload baseline",
                severity="BLOCKER",
                category="submission-requirements",
                guideline="App Store submission SDK requirements",
                confidence="CERTAIN",
                evidence=[_evidence(app_path, info_path, f"DTSDKName={info.get('DTSDKName')}; expected major 26+")],
                rationale="The April 28, 2026 submission baseline requires current platform SDK 26 for supported Apple platforms.",
                remediation="Rebuild using the platform 26 SDK or later in Xcode 26+.",
                verification=["Inspect the new archive's DTSDKName and run App Store Connect validation."],
                sources=["references/policy-baseline.md"],
            ))
        checks.append(make_check(
            "bundle.sdk_minimum",
            "Xcode/SDK upload minimum",
            "PASS" if xcode_number is not None and xcode_number >= 2600 and sdk_platform and not sdk_platform.endswith("-simulator") and (sdk_major is None or sdk_major >= 26) else "ERROR",
            mandatory=True,
            tool="Info.plist",
            detail=f"DTXcode={info.get('DTXcode')}; DTSDKName={info.get('DTSDKName')}",
        ))

        # Device family consistency.
        raw_families = info.get("UIDeviceFamily", [])
        if isinstance(raw_families, int):
            raw_families = [raw_families]
        actual_families = {DEVICE_FAMILY_CODES.get(int(code), f"unknown-{code}") for code in raw_families if str(code).isdigit()}
        facts["device_families"] = sorted(actual_families)
        expected_families = set(app_config.get("device_families", []) or [])
        if expected_families and actual_families:
            material_expected = {f for f in expected_families if f in {"iphone", "ipad", "apple-tv", "vision-pro", "mac", "apple-watch"}}
            missing = sorted(material_expected - actual_families)
            extra = sorted(actual_families - material_expected)
            if missing or extra:
                findings.append(make_finding(
                    id="BUNDLE-DEVICE-FAMILY-MISMATCH",
                    title="Bundle device families conflict with review scope",
                    severity="HIGH",
                    category="artifact-consistency",
                    guideline="2.1 App Completeness; 2.3 Accurate Metadata",
                    confidence="HIGH",
                    evidence=[_evidence(app_path, info_path, "Device family mismatch", {"bundle": sorted(actual_families), "scope": sorted(material_expected), "missing": missing, "extra": extra})],
                    rationale="Screenshot, runtime, and metadata coverage may omit a platform the binary actually supports or review a platform not present in the artifact.",
                    remediation="Reconcile target settings, availability, App Store platforms, and review-input device families.",
                    verification=["Inspect General > Deployment Info and the uploaded build metadata in App Store Connect."],
                    sources=["references/screenshot-review.md"],
                ))

        # Purpose strings in the resolved binary.
        all_usage_keys = {key for keys in PERMISSION_USAGE_KEYS.values() for key in keys}
        purpose_facts: dict[str, Any] = {}
        for key in sorted(all_usage_keys):
            if key in info:
                value = str(info.get(key) or "").strip()
                purpose_facts[key] = value
                if not value or value.casefold() in PURPOSE_GENERIC or len(value) < 12:
                    findings.append(make_finding(
                        id=f"BUNDLE-PURPOSE-{key.upper()}-GENERIC",
                        title="Resolved permission purpose string is empty or insufficiently specific",
                        severity="BLOCKER",
                        category="permissions",
                        guideline="5.1.1(ii) Permission",
                        confidence="CERTAIN",
                        evidence=[_evidence(app_path, info_path, f"{key}={value!r}")],
                        rationale="The final prompt text must clearly and completely explain the app's use of protected data.",
                        remediation="Replace the value with specific localized language tied to the actual feature and data use.",
                        verification=["Fresh-install and visually inspect the system prompt in every target locale."],
                        sources=["references/privacy-security.md"],
                    ))
        facts["purpose_strings"] = purpose_facts

        # ATS.
        ats = info.get("NSAppTransportSecurity")
        if isinstance(ats, dict) and (ats.get("NSAllowsArbitraryLoads") is True or ats.get("NSAllowsArbitraryLoadsInWebContent") is True):
            findings.append(make_finding(
                id="BUNDLE-ATS-ARBITRARY-LOADS",
                title="Resolved bundle permits broad App Transport Security exceptions",
                severity="HIGH",
                category="security",
                guideline="5.1 Privacy; 2.5 Software Requirements",
                confidence="CERTAIN",
                evidence=[_evidence(app_path, info_path, "NSAppTransportSecurity", ats)],
                rationale="Broad exceptions expose traffic to cleartext/interception risk and should be narrowed to documented necessities.",
                remediation="Use HTTPS and remove arbitrary-load exceptions or constrain exceptions to the narrowest required domain/use.",
                verification=["Proxy release traffic and inspect the resolved Info.plist."],
                sources=["references/privacy-security.md"],
            ))

        # Privacy manifests.
        if manifest_errors:
            findings.append(make_finding(
                id="BUNDLE-PRIVACY-MANIFEST-PARSE",
                title="Embedded privacy manifest cannot be parsed",
                severity="BLOCKER",
                category="privacy-manifest",
                guideline="Required-reason APIs; third-party SDK requirements",
                confidence="CERTAIN",
                evidence=manifest_errors,
                rationale="Malformed embedded manifests can fail upload or hide required disclosures.",
                remediation="Fix the manifest in the responsible app/framework and rebuild the archive.",
                verification=["Run plutil -lint on every embedded PrivacyInfo.xcprivacy and Validate App."],
                sources=["references/privacy-security.md"],
            ))
        manifest_reasons = _privacy_manifest_reasons(manifests)
        facts["privacy_manifest_reasons"] = {key: sorted(value) for key, value in manifest_reasons.items()}
        for category, reasons in manifest_reasons.items():
            known = REQUIRED_REASON_API_CATEGORIES.get(category)
            if known is None:
                findings.append(make_finding(
                    id=f"BUNDLE-PRIVACY-UNKNOWN-{category}",
                    title="Embedded privacy manifest uses an unrecognized API category",
                    severity="HIGH",
                    category="privacy-manifest",
                    guideline="Required-reason APIs",
                    confidence="HIGH",
                    status="NEEDS_REVIEW",
                    automation="catalog-freshness",
                    evidence=[make_evidence(kind="privacy-manifest", location=str(app_path), detail=f"{category}: {sorted(reasons)}")],
                    rationale="The identifier may be misspelled or newer than the pinned catalog; readiness requires checking the current official catalog.",
                    remediation="Compare the category with Apple's current required-reason API documentation and refresh the skill catalog if needed.",
                    verification=["Run check_policy_freshness.py --network and Validate App."],
                    sources=["references/privacy-security.md"],
                ))
            else:
                invalid = sorted(reason for reason in reasons if reason not in known)
                if invalid:
                    findings.append(make_finding(
                        id=f"BUNDLE-PRIVACY-INVALID-{category}",
                        title="Embedded privacy manifest contains an unrecognized reason ID",
                        severity="BLOCKER",
                        category="privacy-manifest",
                        guideline="Required-reason APIs",
                        confidence="HIGH",
                        evidence=[make_evidence(kind="privacy-manifest", location=str(app_path), detail=f"{category}: invalid {invalid}")],
                        rationale="App Store Connect validates approved reason IDs, and the reason must truthfully match behavior.",
                        remediation="Use only a current approved reason that describes the actual app/SDK behavior or remove the API.",
                        verification=["Inspect the archive privacy report and run Validate App."],
                        sources=["references/privacy-security.md"],
                    ))

        # Listed SDK manifest coverage.
        listed_embedded: list[dict[str, Any]] = []
        for framework in frameworks:
            name = _framework_name(framework)
            matched = next((sdk for sdk in LISTED_THIRD_PARTY_SDKS if sdk.casefold() == name.casefold() or sdk.casefold() in name.casefold()), None)
            if not matched:
                continue
            manifest_candidates = [framework / PRIVACY_MANIFEST_NAME]
            if framework.suffix == ".framework":
                manifest_candidates.append(framework / "Resources" / PRIVACY_MANIFEST_NAME)
            has_manifest = any(path.exists() for path in manifest_candidates) or any(framework in manifest_path.parents for manifest_path, _ in manifests)
            listed_embedded.append({"sdk": matched, "framework": _relative(framework, app_path), "privacy_manifest": has_manifest})
            if not has_manifest:
                findings.append(make_finding(
                    id=f"BUNDLE-SDK-MANIFEST-{re.sub(r'[^A-Z0-9]+', '-', matched.upper()).strip('-')}",
                    title=f"Listed SDK {matched} has no embedded privacy manifest",
                    severity="BLOCKER",
                    category="third-party-sdk",
                    guideline="Third-party SDK privacy manifest/signature requirements",
                    confidence="HIGH",
                    evidence=[_evidence(app_path, framework, "Listed SDK framework lacks PrivacyInfo.xcprivacy")],
                    rationale="Apple requires privacy manifests and signatures for SDKs on its current list; an embedded noncompliant SDK can block upload.",
                    remediation="Upgrade to a current compliant signed SDK build or remove the SDK, then rebuild from a clean archive.",
                    verification=["Inspect the embedded framework and run Xcode Organizer Validate App/App Store Connect upload validation."],
                    sources=["references/privacy-security.md"],
                ))
        facts["listed_embedded_sdks"] = listed_embedded
        checks.append(make_check(
            "bundle.privacy_manifests",
            "Embedded privacy manifests",
            "PASS" if manifests and not manifest_errors else ("SKIPPED" if not manifests else "ERROR"),
            mandatory=bool(listed_embedded or manifests),
            tool="plistlib",
            detail=f"{len(manifests)} manifest(s); {len(listed_embedded)} listed SDK(s)",
        ))

        # Platform tools: code signature and entitlements.
        codesign = shutil.which("codesign")
        entitlements: dict[str, Any] | None = None
        if codesign:
            code, _, stderr = _run([codesign, "--verify", "--deep", "--strict", "--verbose=2", str(app_path)], timeout=60)
            status = "PASS" if code == 0 else "ERROR"
            checks.append(make_check("bundle.codesign", "Code signature verification", status, mandatory=True, tool="codesign", detail=(stderr.strip()[-500:] or f"exit={code}")))
            tools.append({"name": "codesign", "status": "OK" if code != 127 else "TOOL_UNAVAILABLE", "detail": shutil.which("codesign") or "not found"})
            if code != 0:
                findings.append(make_finding(
                    id="BUNDLE-CODESIGN-INVALID",
                    title="Bundle code signature verification failed",
                    severity="BLOCKER",
                    category="code-signing",
                    guideline="2.1 App Completeness; upload validation",
                    confidence="CERTAIN",
                    evidence=[make_evidence(kind="tool", location=str(app_path), detail=f"codesign exit {code}: {stderr.strip()[-1000:]}")],
                    rationale="An invalid or incomplete signature cannot be accepted for App Store distribution.",
                    remediation="Re-archive with the correct distribution signing identity, provisioning profile, entitlements, and unmodified embedded frameworks.",
                    verification=["Run codesign verification and Xcode Organizer Validate App on a clean archive."],
                    sources=["references/policy-baseline.md"],
                ))
            ent_code, ent_stdout, ent_stderr = _run([codesign, "-d", "--entitlements", ":-", str(app_path)], timeout=30)
            if ent_code == 0 and ent_stdout.strip():
                try:
                    entitlements = plistlib.loads(ent_stdout.encode("utf-8"))
                except Exception:
                    # Some codesign versions write entitlements to stderr.
                    try:
                        start = ent_stderr.find("<?xml")
                        entitlements = plistlib.loads(ent_stderr[start:].encode("utf-8")) if start >= 0 else None
                    except Exception:
                        entitlements = None
            facts["entitlements"] = entitlements
            if isinstance(entitlements, dict) and entitlements.get("get-task-allow") is True:
                findings.append(make_finding(
                    id="BUNDLE-DEBUG-ENTITLEMENT",
                    title="Distribution bundle has get-task-allow enabled",
                    severity="BLOCKER",
                    category="code-signing",
                    guideline="2.5 Software Requirements; upload validation",
                    confidence="CERTAIN",
                    evidence=[make_evidence(kind="entitlement", location=str(app_path), detail="get-task-allow=true")],
                    rationale="The debug entitlement is inappropriate for an App Store distribution build and commonly indicates incorrect signing/provisioning.",
                    remediation="Archive with the Release distribution profile and disable debug entitlements.",
                    verification=["Dump entitlements from the new archive and run Validate App."],
                    sources=["references/privacy-security.md"],
                ))
        else:
            checks.append(make_check("bundle.codesign", "Code signature verification", "SKIPPED", mandatory=True, tool="codesign", detail="codesign is available only on macOS/Xcode environments"))
            tools.append({"name": "codesign", "status": "TOOL_UNAVAILABLE", "detail": "not found"})

        # Architectures.
        architectures: list[str] = []
        if executable:
            lipo = shutil.which("lipo")
            file_tool = shutil.which("file")
            if lipo:
                code, stdout, stderr = _run([lipo, "-archs", str(executable)])
                if code == 0:
                    architectures = stdout.strip().split()
                tools.append({"name": "lipo", "status": "OK" if code == 0 else "ERROR", "detail": stderr.strip()[-300:] or stdout.strip()})
            elif file_tool:
                code, stdout, stderr = _run([file_tool, str(executable)])
                for arch in ("arm64", "arm64e", "x86_64", "i386"):
                    if arch in stdout:
                        architectures.append(arch)
                tools.append({"name": "file", "status": "OK" if code == 0 else "ERROR", "detail": stdout.strip() or stderr.strip()})
            facts["architectures"] = sorted(set(architectures))
            if sdk_platform in {"ios", "tvos", "watchos", "visionos"} and DISALLOWED_ARCHS_FOR_DEVICE.intersection(architectures):
                findings.append(make_finding(
                    id="BUNDLE-SIMULATOR-ARCHITECTURE",
                    title="Device submission binary contains simulator-only architecture",
                    severity="BLOCKER",
                    category="binary",
                    guideline="Upload validation",
                    confidence="HIGH",
                    evidence=[make_evidence(kind="binary", location=_relative(executable, app_path), detail=f"Architectures: {architectures}")],
                    rationale="Simulator architectures cannot be present in an iOS/tvOS/watchOS/visionOS device submission executable.",
                    remediation="Archive the device target and remove incorrectly embedded simulator frameworks/slices.",
                    verification=["Run lipo -archs on the app and every embedded framework, then Validate App."],
                    sources=["references/policy-baseline.md"],
                ))
            checks.append(make_check("bundle.architectures", "Executable architectures", "PASS" if architectures else "SKIPPED", mandatory=True, tool="lipo/file", detail=", ".join(architectures) or "Unable to inspect"))

        # Linked frameworks/private frameworks.
        if executable and shutil.which("otool"):
            code, stdout, stderr = _run(["otool", "-L", str(executable)])
            linked = []
            if code == 0:
                for line in stdout.splitlines()[1:]:
                    token = line.strip().split(" ", 1)[0]
                    if token:
                        linked.append(token)
                private = sorted({name for name in PRIVATE_FRAMEWORK_NAMES if any(f"/{name}.framework/" in value for value in linked)})
                if private:
                    findings.append(make_finding(
                        id="BUNDLE-PRIVATE-FRAMEWORK",
                        title="Executable links against private Apple frameworks",
                        severity="BLOCKER",
                        category="software-requirements",
                        guideline="2.5.1 Public APIs",
                        confidence="HIGH",
                        evidence=[make_evidence(kind="binary", location=_relative(executable, app_path), detail="Private framework names", value=private)],
                        rationale="Apps must use public APIs and frameworks appropriate for App Store distribution.",
                        remediation="Remove private framework linkage and replace it with documented public APIs.",
                        verification=["Run otool -L and Xcode Organizer Validate App on the rebuilt binary."],
                        sources=["references/rule-matrix.md"],
                    ))
                facts["linked_libraries"] = linked
            tools.append({"name": "otool", "status": "OK" if code == 0 else "ERROR", "detail": stderr.strip()[-300:] or f"{len(linked)} linked libraries"})
        else:
            tools.append({"name": "otool", "status": "TOOL_UNAVAILABLE", "detail": "not found or executable missing"})

        # Binary string signals (bounded, not direct proof).
        if executable:
            private_hits = _strings_scan(executable, PRIVATE_OR_DEPRECATED_PATTERNS)
            facts["binary_sensitive_string_hits"] = private_hits
            if private_hits:
                findings.append(make_finding(
                    id="BUNDLE-SENSITIVE-SYMBOL-STRINGS",
                    title="Binary contains deprecated/private/dynamic symbol strings requiring review",
                    severity="MEDIUM",
                    category="software-requirements",
                    guideline="2.5.1 Public APIs; 2.5.2 Self-contained apps",
                    confidence="LOW",
                    status="NEEDS_REVIEW",
                    automation="heuristic",
                    evidence=[make_evidence(kind="binary", location=_relative(executable, app_path), detail="String matches", value=private_hits)],
                    rationale="Strings can originate from harmless libraries or dead code; symbol/linkage and runtime context determine compliance.",
                    remediation="Trace each hit to a public documented API or remove it from the release binary.",
                    verification=["Inspect symbols/linkage and execute the related code path."],
                    sources=["references/rule-matrix.md"],
                ))

        # macOS quarantine extended attribute requirement.
        if sdk_platform == "macos":
            xattr = shutil.which("xattr")
            if xattr:
                code, stdout, stderr = _run([xattr, "-r", str(app_path)], timeout=60)
                quarantine_paths = [line for line in stdout.splitlines() if "com.apple.quarantine" in line]
                if quarantine_paths:
                    findings.append(make_finding(
                        id="BUNDLE-MAC-QUARANTINE-XATTR",
                        title="macOS app contains com.apple.quarantine extended attributes",
                        severity="BLOCKER",
                        category="submission-requirements",
                        guideline="App Store upload requirements",
                        confidence="HIGH",
                        evidence=[make_evidence(kind="tool", location=str(app_path), detail="Quarantine attribute output", value=quarantine_paths[:20])],
                        rationale="Apple's current macOS upload requirements prohibit quarantine attributes in App Store Connect submissions.",
                        remediation="Remove the quarantine extended attribute from all bundle files before signing/archive export, then rebuild cleanly.",
                        verification=["Run xattr -r on the final app and Validate App."],
                        sources=["references/policy-baseline.md"],
                    ))
                checks.append(make_check("bundle.macos_quarantine", "macOS quarantine attributes", "ERROR" if quarantine_paths else "PASS", mandatory=True, tool="xattr", detail=f"{len(quarantine_paths)} hit(s)"))
            else:
                checks.append(make_check("bundle.macos_quarantine", "macOS quarantine attributes", "SKIPPED", mandatory=True, tool="xattr", detail="xattr unavailable"))

        # Archive-specific metadata and validation hints.
        if container_type == "xcarchive":
            archive_info_path = input_path / "Info.plist"
            archive_info, archive_error = _load_plist(archive_info_path) if archive_info_path.exists() else (None, "missing")
            facts["archive_info"] = archive_info
            if archive_info is None:
                findings.append(make_finding(
                    id="BUNDLE-XCARCHIVE-INFO",
                    title="xcarchive metadata is missing or malformed",
                    severity="HIGH",
                    category="artifact-consistency",
                    guideline="2.1 App Completeness",
                    confidence="CERTAIN",
                    evidence=[make_evidence(kind="archive", location=str(archive_info_path), detail=f"Unable to parse archive Info.plist: {archive_error}")],
                    rationale="A valid distribution archive should preserve application and signing metadata used by Xcode Organizer.",
                    remediation="Create a clean Release archive using xcodebuild archive or Xcode Organizer.",
                    verification=["Open the archive in Xcode Organizer and run Validate App."],
                    sources=["references/runtime-review.md"],
                ))

        checks.append(make_check(
            "bundle.inspection",
            "Final bundle deterministic inspection",
            "PASS",
            mandatory=True,
            tool="inspect_bundle.py",
            detail=f"Inspected {container_type}: {app_path.name}",
        ))

        result = {
            "module": "inspect_bundle",
            "generated_at": now_iso(),
            "bundle": str(input_path),
            "facts": facts,
            "checks": checks,
            "findings": findings,
            "tool": {"name": "inspect_bundle.py", "status": "OK", "detail": "Read-only archive/app/IPA inspection"},
            "tools": tools,
        }
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect a final .xcarchive, .app, or .ipa for App Store submission risks.")
    parser.add_argument("--bundle", required=True, help="Path to .xcarchive, .app, or .ipa")
    parser.add_argument("--config", help="Optional review-input.json")
    parser.add_argument("--output", help="Write structured JSON result")
    parser.add_argument("--strict", action="store_true", help="Exit 2 for open blocker/high findings")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config = load_json(args.config) if args.config else None
        if config is not None and not isinstance(config, dict):
            raise ReviewInputError("Config root must be an object")
        result = inspect_bundle(args.bundle, config=config, config_path=args.config)
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"inspect_bundle: {exc}\n")
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
