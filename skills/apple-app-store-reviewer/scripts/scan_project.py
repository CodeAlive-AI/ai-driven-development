#!/usr/bin/env python3
"""Static, local-first scan of an Apple app source project.

This scanner deliberately separates exact evidence (for example, a committed
secret or a malformed privacy manifest) from contextual signals (for example,
web-wrapper risk). It never marks a runtime behavior as passed from source alone.
"""

from __future__ import annotations

import argparse
import json
import os
import plistlib
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping
from urllib.parse import urlparse

from catalogs import (
    AI_PROVIDER_PATTERNS,
    DYNAMIC_CODE_PATTERNS,
    FOUNDATION_MODELS_PATTERNS,
    IGNORED_DIRECTORY_NAMES,
    INFO_PLIST_NAMES,
    LISTED_THIRD_PARTY_SDKS,
    PAYMENT_PATTERNS,
    PERMISSION_SOURCE_PATTERNS,
    PERMISSION_USAGE_KEYS,
    PLACEHOLDER_PATTERNS,
    PRIVATE_OR_DEPRECATED_PATTERNS,
    PRIVACY_MANIFEST_NAME,
    REQUIRED_REASON_API_CATEGORIES,
    REQUIRED_REASON_SOURCE_PATTERNS,
    SECRET_PATTERNS,
    TEXT_EXTENSIONS,
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
)

MAX_DEFAULT_FILE_BYTES = 2 * 1024 * 1024
MAX_HITS_PER_SIGNAL = 12
LOCALE_STRINGS_RE = re.compile(r"(?:^|/)([A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*)\.lproj/")
URL_RE = re.compile(r"https?://[^\s\"'<>)}\]]+")
ACCOUNT_CREATION_PATTERNS = (
    "createAccount", "signUp", "signup", "registerAccount", "Create account", "Sign up",
)
ACCOUNT_DELETION_PATTERNS = (
    "deleteAccount", "delete account", "Delete Account", "requestAccountDeletion", "account deletion",
)
SOCIAL_LOGIN_PATTERNS = {
    "google": ("GIDSignIn", "GoogleSignIn", "Sign in with Google"),
    "facebook": ("FBSDKLogin", "LoginManager", "Sign in with Facebook"),
    "x": ("Sign in with X", "TwitterKit", "OAuthSwift"),
    "linkedin": ("Sign in with LinkedIn", "linkedin.com/oauth"),
    "amazon": ("LoginWithAmazon", "Sign in with Amazon"),
    "wechat": ("WXApi", "WeChat login"),
}
PRIVACY_PRESERVING_LOGIN_PATTERNS = (
    "ASAuthorizationAppleIDProvider", "ASAuthorizationAppleIDButton", "Sign in with Apple",
)
CONSENT_PATTERNS = (
    "explicitConsent", "aiConsent", "dataSharingConsent", "consentBefore", "Allow AI Processing",
    "Share with", "sent to", "third-party AI", "third party AI", "model provider",
)
UGC_PATTERNS = {
    "ugc": ("userGeneratedContent", "user-generated content", "postContent", "createPost", "publicFeed"),
    "filter": ("contentFilter", "moderation", "NSFW", "profanity", "objectionable"),
    "report": ("reportContent", "report user", "ReportContent", "flagContent"),
    "block": ("blockUser", "blockedUsers", "Block user"),
    "support": ("support@", "contact support", "SupportView"),
}
WEB_WRAPPER_PATTERNS = (
    "WKWebView", "SFSafariViewController", "loadHTMLString", "loadFileURL", "webview_flutter_wkwebview",
    "react-native-webview", "cordova", "capacitor", "window.location",
)
NATIVE_VALUE_PATTERNS = (
    "CoreLocation", "HealthKit", "ARKit", "RealityKit", "CoreML", "Vision", "WidgetKit", "AppIntents",
    "ActivityKit", "MapKit", "CoreBluetooth", "NearbyInteraction", "StoreKit", "UserNotifications",
    "Camera", "PhotosPicker", "ShareLink", "DocumentPicker", "CloudKit", "WatchConnectivity",
)
TRACKING_SDK_PATTERNS = (
    "FirebaseAnalytics", "AppsFlyer", "Adjust", "FacebookCore", "MetaAudienceNetwork", "GoogleMobileAds",
    "Mixpanel", "Amplitude", "Branch", "OneSignal", "AdSupport", "ASIdentifierManager",
)
RESTORE_PATTERNS = (
    "restorePurchases", "restore transactions", "AppStore.sync", "SKPaymentQueue.default().restoreCompletedTransactions",
)
EXTERNAL_PAYMENT_HOSTS = (
    "stripe.com", "paypal.com", "paddle.com", "lemonsqueezy.com", "checkout.com", "fastspring.com",
)
PERSONAL_DATA_SOURCE_PATTERNS = {
    "photos": ("PHPhotoLibrary", "PhotosPicker", "UIImagePickerController"),
    "contacts": ("CNContactStore",),
    "location": ("CLLocationManager",),
    "health": ("HKHealthStore",),
    "calendar": ("EKEventStore",),
    "microphone/audio": ("AVAudioRecorder", "AVAudioEngine", "SFSpeechRecognizer"),
    "camera/video": ("AVCaptureSession", "AVCaptureDevice"),
    "device identifiers": ("identifierForVendor", "ASIdentifierManager", "DeviceCheck", "AppAttest"),
    "user content": ("UITextView", "TextEditor", "fileImporter", "UIDocumentPicker"),
}
CAPACITOR_VERSION_PACKAGES = ("@capacitor/core", "@capacitor/ios", "@capacitor/cli")
CAPACITOR_PRIVACY_PLUGINS = {
    "@capacitor/preferences": "NSPrivacyAccessedAPICategoryUserDefaults",
    "@capacitor/filesystem": "NSPrivacyAccessedAPICategoryFileTimestamp",
}
CAPACITOR_LIVE_UPDATE_PATTERNS = (
    "@capacitor/live-updates", "@ionic-enterprise/live-updates", "@ionic-enterprise/deploy",
    "cordova-plugin-ionic", "Appflow", "LiveUpdates",
)
CAPACITOR_LEGACY_SCENE_CALLBACKS = (
    "applicationDidBecomeActive", "applicationWillResignActive", "applicationDidEnterBackground",
    "applicationWillEnterForeground", "application(_:open:options:)",
    "application(_:continue:restorationHandler:)", "open url: URL", "continue userActivity:",
)
CAPACITOR_REMOVED_85_PATTERNS = ("tmpWindow", "TmpViewController", "tmpViewControllerAppeared")


def _iter_files(root: Path, max_file_bytes: int) -> Iterable[Path]:
    for current, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRECTORY_NAMES and not d.endswith(".xcarchive"))
        for name in sorted(files):
            path = Path(current) / name
            if path.suffix.lower() not in TEXT_EXTENSIONS and name not in INFO_PLIST_NAMES and name != PRIVACY_MANIFEST_NAME:
                continue
            try:
                if path.is_symlink() or path.stat().st_size > max_file_bytes:
                    continue
            except OSError:
                continue
            yield path


def _read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="utf-8-sig")
        except (UnicodeDecodeError, OSError):
            return None
    except OSError:
        return None


def _line_for(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def _relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _hits(text: str, patterns: Iterable[str], path: Path, root: Path, *, case_sensitive: bool = False, limit: int = MAX_HITS_PER_SIGNAL) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    haystack = text if case_sensitive else text.casefold()
    for pattern in patterns:
        needle = pattern if case_sensitive else pattern.casefold()
        start = 0
        while len(out) < limit:
            index = haystack.find(needle, start)
            if index < 0:
                break
            line_start = text.rfind("\n", 0, index) + 1
            line_end = text.find("\n", index)
            if line_end < 0:
                line_end = len(text)
            snippet = text[line_start:line_end].strip()
            if len(snippet) > 240:
                snippet = snippet[:237] + "..."
            out.append(make_evidence(
                kind="source",
                location=_relative(path, root),
                line=_line_for(text, index),
                detail=f"Matched {pattern!r}: {snippet}",
            ))
            start = index + max(1, len(needle))
        if len(out) >= limit:
            break
    return out


def _version_line(value: Any) -> tuple[int, int] | None:
    match = re.search(r"(?:^|[^0-9])(\d+)\.(\d+)", str(value))
    return (int(match.group(1)), int(match.group(2))) if match else None


def _manifest_categories(manifests: Iterable[tuple[Path, dict[str, Any]]]) -> set[str]:
    categories: set[str] = set()
    for _, manifest in manifests:
        accessed_types = manifest.get("NSPrivacyAccessedAPITypes", [])
        if not isinstance(accessed_types, list):
            continue
        for item in accessed_types:
            if isinstance(item, dict) and isinstance(item.get("NSPrivacyAccessedAPIType"), str):
                categories.add(item["NSPrivacyAccessedAPIType"])
    return categories


def _config_value(config: Mapping[str, Any], *path: str) -> Any:
    value: Any = config
    for key in path:
        if not isinstance(value, Mapping):
            return None
        value = value.get(key)
    return value


def _scan_capacitor(
    root: Path,
    text_by_path: Mapping[Path, str],
    plists: Iterable[tuple[Path, dict[str, Any]]],
    manifests: Iterable[tuple[Path, dict[str, Any]]],
) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    package_data: dict[str, Any] = {}
    package_path: Path | None = None
    for path, text in sorted(text_by_path.items(), key=lambda item: (len(item[0].parts), str(item[0]))):
        if path.name != "package.json":
            continue
        try:
            candidate = json.loads(text)
        except json.JSONDecodeError:
            continue
        if not isinstance(candidate, dict):
            continue
        dependencies_value = candidate.get("dependencies", {})
        dev_dependencies_value = candidate.get("devDependencies", {})
        dependencies = {
            **(dependencies_value if isinstance(dependencies_value, dict) else {}),
            **(dev_dependencies_value if isinstance(dev_dependencies_value, dict) else {}),
        }
        if any(name in dependencies for name in CAPACITOR_VERSION_PACKAGES):
            package_data = dependencies
            package_path = path
            break

    capacitor_signal = package_path is not None or any(
        "@capacitor/ios" in text or "import Capacitor" in text
        for text in text_by_path.values()
    )
    if not capacitor_signal:
        return {}, [], []

    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    evidence_location = _relative(package_path, root) if package_path else str(root)
    versions = {name: str(package_data[name]) for name in CAPACITOR_VERSION_PACKAGES if name in package_data}
    version_lines = {name: _version_line(value) for name, value in versions.items()}
    comparable_lines = {line for line in version_lines.values() if line is not None}
    release_lines = [line for name in ("@capacitor/core", "@capacitor/ios") if (line := version_lines.get(name)) is not None]
    target_version_line = max(release_lines) if release_lines else None
    target_line = f"{target_version_line[0]}.{target_version_line[1]}" if target_version_line else "unknown"
    plugins = sorted(name for name in package_data if name.startswith("@capacitor/") and name not in CAPACITOR_VERSION_PACKAGES)
    lockfile_path = next((path for path in text_by_path if path.name in {"package-lock.json", "npm-shrinkwrap.json", "pnpm-lock.yaml", "yarn.lock"}), None)

    if len(comparable_lines) > 1:
        findings.append(_finding(
            id="SOURCE-CAPACITOR-VERSION-MISMATCH",
            title="Capacitor core, iOS, and CLI packages target different release lines",
            severity="HIGH",
            category="dependency-integrity",
            guideline="2.1 App Completeness; 2.5 Software Requirements",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="dependency", location=evidence_location, detail=f"Declared Capacitor versions: {versions}")],
            rationale="A mixed Capacitor release line can leave generated native code, bridge behavior, and plugins out of sync with the reviewed web bundle.",
            remediation="Align @capacitor/core, @capacitor/ios, and @capacitor/cli to the same supported release line, regenerate the lockfile, and run npx cap sync ios.",
            verification=["Resolve the lockfile, run npx cap doctor and npx cap sync ios, then rebuild the exact archive."],
            sources=["references/capacitor-ios.md"],
        ))
    if lockfile_path is None:
        findings.append(_finding(
            id="SOURCE-CAPACITOR-LOCKFILE-NOT-FOUND",
            title="Capacitor dependency versions lack resolved lockfile evidence",
            severity="MEDIUM",
            category="dependency-integrity",
            guideline="2.1 App Completeness; 2.5 Software Requirements",
            confidence="HIGH",
            status="NEEDS_REVIEW",
            automation="deterministic",
            evidence=[make_evidence(kind="dependency", location=evidence_location, detail="No npm, pnpm, or Yarn lockfile found in the scanned project")],
            rationale="Version ranges in package.json do not prove which Capacitor runtime and plugins were used to generate the reviewed native project.",
            remediation="Commit or supply the resolved release lockfile and rebuild the native project from it.",
            verification=["Install with the package manager's frozen-lockfile mode, run npx cap sync ios, and compare resolved versions with the archive."],
            sources=["references/capacitor-ios.md"],
        ))

    config_path: Path | None = None
    config: dict[str, Any] = {}
    config_text = ""
    for path, text in text_by_path.items():
        if path.name not in {"capacitor.config.json", "capacitor.config.ts", "capacitor.config.js"}:
            continue
        config_path, config_text = path, text
        if path.suffix == ".json":
            try:
                parsed = json.loads(text)
                config = parsed if isinstance(parsed, dict) else {}
            except json.JSONDecodeError:
                config = {}
        break

    config_location = _relative(config_path, root) if config_path else str(root)
    if config_path is None:
        findings.append(_finding(
            id="SOURCE-CAPACITOR-CONFIG-NOT-FOUND",
            title="Capacitor release configuration is missing from review evidence",
            severity="MEDIUM",
            category="release-configuration",
            guideline="2.1 App Completeness; 2.5 Software Requirements",
            confidence="HIGH",
            status="NEEDS_REVIEW",
            automation="deterministic",
            evidence=[make_evidence(kind="filesystem", location=str(root), detail="No capacitor.config.json, .ts, or .js file found")],
            rationale="Without the source configuration, the audit cannot verify the bundled asset directory, WebView origin, navigation boundary, or release diagnostics.",
            remediation="Supply the exact production Capacitor configuration and the configuration embedded in the archived app.",
            verification=["Rerun the scan with the release config and compare it with the final archive."],
            sources=["references/capacitor-ios.md"],
        ))
    server_url = _config_value(config, "server", "url")
    if not server_url and config_text:
        match = re.search(r"\burl\s*:\s*['\"](https?://[^'\"]+)", config_text)
        server_url = match.group(1) if match else None
    cleartext = _config_value(config, "server", "cleartext") is True or bool(re.search(r"\bcleartext\s*:\s*true", config_text))
    if server_url or cleartext:
        findings.append(_finding(
            id="SOURCE-CAPACITOR-DEVELOPMENT-SERVER",
            title="Capacitor release configuration loads an external development server",
            severity="HIGH",
            category="release-configuration",
            guideline="2.1 App Completeness; 2.5.2 Self-contained Apps",
            confidence="CERTAIN" if config else "HIGH",
            evidence=[make_evidence(kind="config", location=config_location, detail=f"server.url={server_url!r}; server.cleartext={cleartext}")],
            rationale="Capacitor documents server.url as a live-reload setting, not a production setting. It can ship a stale or unreachable release and move reviewed behavior outside the submitted bundle.",
            remediation="Remove server.url from the release configuration, rebuild the web assets, run npx cap sync ios, and archive again.",
            verification=["Inspect the archived Capacitor configuration and prove the app launches from bundled assets with the development host offline."],
            sources=["references/capacitor-ios.md"],
        ))

    allow_navigation = _config_value(config, "server", "allowNavigation")
    if allow_navigation is None and re.search(r"\ballowNavigation\s*:", config_text):
        allow_navigation = "declared"
    if allow_navigation:
        findings.append(_finding(
            id="SOURCE-CAPACITOR-UNSAFE-NAVIGATION",
            title="Capacitor WebView has additional in-app navigation origins",
            severity="HIGH" if allow_navigation == "declared" or "*" in str(allow_navigation) else "MEDIUM",
            category="webview-security",
            guideline="2.5 Software Requirements; 5.1 Privacy",
            confidence="CERTAIN" if config else "MEDIUM",
            status="NEEDS_REVIEW",
            automation="deterministic" if config else "heuristic",
            evidence=[make_evidence(kind="config", location=config_location, detail=f"server.allowNavigation: {allow_navigation}")],
            rationale="Capacitor documents allowNavigation as non-production configuration. Loading external origins inside the privileged app WebView expands the native bridge and content trust boundary.",
            remediation="Remove the setting where possible; otherwise use an exact allowlist, isolate untrusted content from native plugins, and document the necessity.",
            verification=["Proxy navigation attempts and prove untrusted origins open externally and cannot call the Capacitor bridge."],
            sources=["references/capacitor-ios.md"],
        ))

    release_diagnostics: list[str] = []
    if _config_value(config, "loggingBehavior") == "production" or re.search(r"\bloggingBehavior\s*:\s*['\"]production", config_text):
        release_diagnostics.append("loggingBehavior=production")
    if _config_value(config, "ios", "webContentsDebuggingEnabled") is True or re.search(r"\bwebContentsDebuggingEnabled\s*:\s*true", config_text):
        release_diagnostics.append("ios.webContentsDebuggingEnabled=true")
    if release_diagnostics:
        findings.append(_finding(
            id="SOURCE-CAPACITOR-RELEASE-DIAGNOSTICS",
            title="Capacitor release enables production logging or WebView inspection",
            severity="MEDIUM",
            category="release-configuration",
            guideline="2.5 Software Requirements; 5.1 Privacy",
            confidence="CERTAIN" if config else "HIGH",
            status="NEEDS_REVIEW",
            automation="deterministic" if config else "heuristic",
            evidence=[make_evidence(kind="config", location=config_location, detail=", ".join(release_diagnostics))],
            rationale="Release diagnostics can expose console output, user data, internal endpoints, or privileged WebView state on production devices.",
            remediation="Use debug-only logging and keep release WebView debugging disabled unless a documented, risk-reviewed requirement exists.",
            verification=["Inspect the release config and confirm Safari cannot attach to the production WebView and sensitive console output is absent."],
            sources=["references/capacitor-ios.md"],
        ))

    limits_app_bound = _config_value(config, "ios", "limitsNavigationsToAppBoundDomains") is True
    if limits_app_bound:
        app_bound_domains = next((plist.get("WKAppBoundDomains") for _, plist in plists if plist.get("WKAppBoundDomains")), None)
        hostname = _config_value(config, "server", "hostname") or "localhost"
        if not isinstance(app_bound_domains, list) or hostname not in app_bound_domains:
            findings.append(_finding(
                id="SOURCE-CAPACITOR-APP-BOUND-DOMAINS",
                title="Capacitor app-bound navigation is inconsistent with Info.plist",
                severity="HIGH",
                category="webview-configuration",
                guideline="2.1 App Completeness; 2.5 Software Requirements",
                confidence="HIGH",
                evidence=[make_evidence(kind="config", location=config_location, detail=f"limitsNavigationsToAppBoundDomains=true; expected host {hostname!r} in WKAppBoundDomains")],
                rationale="Capacitor warns that missing app-bound domains can block navigation or WebKit features, including the local app host.",
                remediation="Align WKAppBoundDomains with the exact trusted domains and the configured Capacitor hostname.",
                verification=["Exercise bundled app launch and every allowed/external navigation path on the release build."],
                sources=["references/capacitor-ios.md"],
            ))

    uses_capacitor_85_scene = bool(target_version_line and (target_version_line[0] > 8 or target_version_line >= (8, 5)))
    scene_manifest = any(
        isinstance(scene := plist.get("UIApplicationSceneManifest"), dict)
        and "UISceneDelegateClassName" in json.dumps(scene)
        for _, plist in plists
    )
    scene_delegate_texts = [(path, text) for path, text in text_by_path.items() if path.name == "SceneDelegate.swift"]
    has_scene_delegate = bool(scene_delegate_texts)
    has_scene_connect_proxy = any("SceneDelegateProxy.shared" in text and "willConnectTo" in text for _, text in scene_delegate_texts)
    has_scene_url_proxy = any("SceneDelegateProxy.shared" in text and "openURLContexts" in text for _, text in scene_delegate_texts)
    has_scene_universal_proxy = any("SceneDelegateProxy.shared" in text and "continue userActivity" in text for _, text in scene_delegate_texts)
    has_scene_proxy = has_scene_connect_proxy and has_scene_url_proxy and has_scene_universal_proxy
    has_scene_hook = any("configurationForConnecting" in text and "SceneDelegate.self" in text for text in text_by_path.values())
    project_files = [text for path, text in text_by_path.items() if path.suffix == ".pbxproj"]
    scene_target_membership = bool(project_files) and any("SceneDelegate.swift" in text for text in project_files)
    missing_scene_parts = [
        label for label, present in (
            ("UIApplicationSceneManifest", scene_manifest),
            ("SceneDelegate.swift", has_scene_delegate),
            ("SceneDelegateProxy connection forwarding", has_scene_connect_proxy),
            ("SceneDelegateProxy custom-URL forwarding", has_scene_url_proxy),
            ("SceneDelegateProxy universal-link forwarding", has_scene_universal_proxy),
            ("AppDelegate scene configuration hook", has_scene_hook),
            ("SceneDelegate target membership", scene_target_membership),
        ) if not present
    ]
    if uses_capacitor_85_scene and missing_scene_parts:
        partial_migration = scene_manifest or has_scene_delegate or has_scene_hook
        findings.append(_finding(
            id="SOURCE-CAPACITOR-UISCENE-MIGRATION-INCOMPLETE",
            title="Capacitor 8.5 UIScene migration is incomplete",
            severity="HIGH" if partial_migration else "MEDIUM",
            category="lifecycle-and-links",
            guideline="2.1 App Completeness; 2.5 Software Requirements",
            confidence="HIGH",
            status="NEEDS_REVIEW",
            automation="deterministic",
            evidence=[make_evidence(kind="source", location=str(root), detail=f"Missing: {', '.join(missing_scene_parts)}")],
            rationale="Capacitor 8.5 adopts UIScene. Xcode 27 requires the project migration, and an incomplete migration can break launch, lifecycle events, custom URLs, or universal links.",
            remediation="Apply the official Capacitor 8.5 UIScene migration, preserve custom CAPBridgeViewController behavior, register SceneDelegate in the app target, and run npx cap sync ios.",
            verification=["Test cold and warm custom URLs, universal links, App.getLaunchUrl(), appUrlOpen, pause/resume, and foreground/background on the release build."],
            sources=["references/capacitor-ios.md"],
        ))

    if scene_manifest:
        legacy_evidence: list[dict[str, Any]] = []
        for path, text in text_by_path.items():
            if path.name == "AppDelegate.swift":
                legacy_evidence.extend(_hits(text, CAPACITOR_LEGACY_SCENE_CALLBACKS, path, root, limit=8))
        if legacy_evidence:
            findings.append(_finding(
                id="SOURCE-CAPACITOR-UISCENE-LEGACY-CALLBACK",
                title="Custom AppDelegate behavior may no longer run under UIScene",
                severity="HIGH",
                category="lifecycle-and-links",
                guideline="2.1 App Completeness",
                confidence="MEDIUM",
                status="NEEDS_REVIEW",
                automation="heuristic",
                evidence=legacy_evidence,
                rationale="After the scene manifest is enabled, several AppDelegate URL and foreground/background callbacks stop receiving the corresponding events.",
                remediation="Move custom behavior to SceneDelegate callbacks or supported notifications while preserving Capacitor proxy forwarding.",
                verification=["Instrument and execute every affected lifecycle and deep-link path on a clean release build."],
                sources=["references/capacitor-ios.md"],
            ))

    removed_api_evidence: list[dict[str, Any]] = []
    for path, text in text_by_path.items():
        removed_api_evidence.extend(_hits(text, CAPACITOR_REMOVED_85_PATTERNS, path, root, limit=max(0, 8 - len(removed_api_evidence))))
    if uses_capacitor_85_scene and removed_api_evidence:
        findings.append(_finding(
            id="SOURCE-CAPACITOR-REMOVED-85-API",
            title="Project references APIs removed in Capacitor 8.5",
            severity="HIGH",
            category="dependency-compatibility",
            guideline="2.1 App Completeness; 2.5 Software Requirements",
            confidence="HIGH",
            evidence=removed_api_evidence,
            rationale="Capacitor 8.5 removed TmpViewController, CapacitorBridge.tmpWindow, and tmpViewControllerAppeared.",
            remediation="Remove the obsolete integration and use the bridge viewController as the presentation anchor.",
            verification=["Build and execute every native presentation path against the resolved Capacitor 8.5 dependency."],
            sources=["references/capacitor-ios.md"],
        ))

    declared_categories = _manifest_categories(manifests)
    missing_plugin_categories = {
        plugin: category for plugin, category in CAPACITOR_PRIVACY_PLUGINS.items()
        if plugin in package_data and category not in declared_categories
    }
    if missing_plugin_categories:
        findings.append(_finding(
            id="SOURCE-CAPACITOR-PLUGIN-PRIVACY-MANIFEST",
            title="Capacitor plugins require privacy-manifest reason review",
            severity="HIGH",
            category="privacy-manifest",
            guideline="Required-reason API declarations",
            confidence="HIGH",
            status="NEEDS_REVIEW",
            automation="deterministic",
            evidence=[make_evidence(kind="dependency", location=evidence_location, detail=f"Missing plugin/category evidence: {missing_plugin_categories}")],
            rationale="Capacitor documents that plugins such as Preferences and Filesystem may require approved-reason declarations; package presence alone cannot choose the app's truthful reason code.",
            remediation="Add the applicable categories and Apple-approved reasons to the app privacy manifest, then verify the aggregate archive manifest and App Privacy answers.",
            verification=["Inspect the final archive privacy report and resolve every App Store Connect required-reason warning."],
            sources=["references/capacitor-ios.md", "references/privacy-security.md"],
        ))

    live_update_evidence: list[dict[str, Any]] = []
    for path, text in text_by_path.items():
        live_update_evidence.extend(_hits(text, CAPACITOR_LIVE_UPDATE_PATTERNS, path, root, limit=max(0, 8 - len(live_update_evidence))))
    if live_update_evidence:
        findings.append(_finding(
            id="SOURCE-CAPACITOR-LIVE-UPDATES-REVIEW",
            title="Capacitor live-update mechanism requires executable-content review",
            severity="MEDIUM",
            category="software-requirements",
            guideline="2.5.2 Self-contained Apps; 4.7 software not embedded in binary",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=live_update_evidence,
            rationale="Remote web-bundle updates can be legitimate, but the reviewer must know what changes remotely, how bundles are signed, and whether updates materially alter reviewed functionality.",
            remediation="Document the update boundary, signing/integrity, rollout and rollback, bundled fallback, native-code prohibition, and App Review policy rationale.",
            verification=["Record the shipped and downloaded web-bundle hashes, reject a tampered update, exercise rollback, and prove native plugins cannot be added remotely."],
            sources=["references/capacitor-ios.md", "references/rule-matrix.md"],
        ))

    capacitor_facts = {
        "target_line": target_line,
        "versions": versions,
        "plugins": plugins,
        "lockfile": _relative(lockfile_path, root) if lockfile_path else None,
        "config": config_location if config_path else None,
        "uiscene": {
            "required_for_xcode_27": uses_capacitor_85_scene,
            "manifest": scene_manifest,
            "delegate": has_scene_delegate,
            "proxy_forwarding": has_scene_proxy,
            "app_delegate_hook": has_scene_hook,
            "target_membership": scene_target_membership,
        },
    }
    capacitor_ids = {finding["id"] for finding in findings}
    checks.extend([
        make_check("source.capacitor.inventory", "Capacitor dependency and plugin inventory", "PASS", mandatory=True, tool="scan_project.py", detail=f"Capacitor {target_line}; {len(plugins)} plugin(s)"),
        make_check("source.capacitor.release-config", "Capacitor production configuration", "NEEDS_REVIEW" if capacitor_ids & {"SOURCE-CAPACITOR-CONFIG-NOT-FOUND", "SOURCE-CAPACITOR-DEVELOPMENT-SERVER", "SOURCE-CAPACITOR-UNSAFE-NAVIGATION", "SOURCE-CAPACITOR-RELEASE-DIAGNOSTICS", "SOURCE-CAPACITOR-APP-BOUND-DOMAINS"} else "PASS", mandatory=True, tool="scan_project.py", detail=config_location),
        make_check("source.capacitor.uiscene", "Capacitor 8.5 UIScene integration", "NEEDS_REVIEW" if capacitor_ids & {"SOURCE-CAPACITOR-UISCENE-MIGRATION-INCOMPLETE", "SOURCE-CAPACITOR-UISCENE-LEGACY-CALLBACK", "SOURCE-CAPACITOR-REMOVED-85-API"} else "PASS", mandatory=uses_capacitor_85_scene, tool="scan_project.py", detail=f"Missing: {', '.join(missing_scene_parts) if missing_scene_parts else 'none'}"),
    ])
    return capacitor_facts, findings, checks


def _parse_plist(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        with path.open("rb") as handle:
            value = plistlib.load(handle)
        return (value if isinstance(value, dict) else None), None
    except (OSError, plistlib.InvalidFileException, ValueError, TypeError) as exc:
        # Some source plists contain unresolved Xcode variables or are JSON-like.
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            return (raw if isinstance(raw, dict) else None), None
        except Exception:
            return None, str(exc)


def _all_usage_descriptions(plists: list[tuple[Path, dict[str, Any]]]) -> dict[str, list[tuple[Path, Any]]]:
    values: dict[str, list[tuple[Path, Any]]] = defaultdict(list)
    for path, plist in plists:
        for key, value in plist.items():
            if key.endswith("UsageDescription"):
                values[key].append((path, value))
    return dict(values)


def _manifest_api_map(manifests: list[tuple[Path, dict[str, Any]]]) -> dict[str, set[str]]:
    result: dict[str, set[str]] = defaultdict(set)
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
                result[category].update(str(reason) for reason in reasons)
    return dict(result)


def _manifest_collected_types(manifests: list[tuple[Path, dict[str, Any]]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for path, manifest in manifests:
        entries = manifest.get("NSPrivacyCollectedDataTypes", [])
        if isinstance(entries, list):
            for entry in entries:
                if isinstance(entry, dict):
                    out.append({"path": str(path), **entry})
    return out


def _finding(**kwargs: Any) -> dict[str, Any]:
    return make_finding(**kwargs)


def scan_project(
    project: str | Path,
    *,
    config: Mapping[str, Any] | None = None,
    config_path: str | Path | None = None,
    max_file_bytes: int = MAX_DEFAULT_FILE_BYTES,
) -> dict[str, Any]:
    root = Path(project).resolve()
    if not root.exists() or not root.is_dir():
        raise ReviewInputError(f"Project directory not found: {root}")
    config = dict(config or {})
    if config_path:
        config = resolve_config_paths(config, config_path)
    features = config.get("features", {})
    app = config.get("app", {})

    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    files: list[Path] = []
    text_by_path: dict[Path, str] = {}
    plists: list[tuple[Path, dict[str, Any]]] = []
    manifests: list[tuple[Path, dict[str, Any]]] = []
    parse_errors: list[dict[str, Any]] = []

    # Bounded scan.
    for path in _iter_files(root, max_file_bytes):
        files.append(path)
        if path.name in INFO_PLIST_NAMES or path.suffix.lower() in {".plist", ".entitlements", ".xcprivacy"}:
            data, error = _parse_plist(path)
            if data is not None:
                if path.name == PRIVACY_MANIFEST_NAME or path.suffix.lower() == ".xcprivacy":
                    manifests.append((path, data))
                elif path.name in INFO_PLIST_NAMES or path.suffix.lower() == ".plist":
                    plists.append((path, data))
            elif error and path.name in INFO_PLIST_NAMES | {PRIVACY_MANIFEST_NAME}:
                parse_errors.append(make_evidence(kind="source", location=_relative(path, root), detail=f"Unable to parse property list: {error}"))
        text = _read_text(path)
        if text is not None:
            text_by_path[path] = text

    combined_casefold = "\n".join(text.casefold() for text in text_by_path.values())
    facts: dict[str, Any] = {
        "root": str(root),
        "file_count": len(files),
        "text_file_count": len(text_by_path),
        "info_plists": [_relative(path, root) for path, _ in plists],
        "privacy_manifests": [_relative(path, root) for path, _ in manifests],
        "parse_errors": parse_errors,
    }

    if not files:
        findings.append(_finding(
            id="SOURCE-NO-FILES",
            title="No scannable project files were found",
            severity="HIGH",
            category="source-evidence",
            guideline="2.1 App Completeness",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="filesystem", location=str(root), detail="No supported source/config files found")],
            rationale="The static audit cannot inspect the release project; the configured path may point to the wrong directory or only to generated output.",
            remediation="Point paths.project at the repository or exported source/config tree used for the release build.",
            verification=["Rerun scan_project.py and confirm file_count is nonzero."],
            sources=["references/policy-baseline.md"],
        ))
    checks.append(make_check("source.inventory", "Source inventory", "PASS" if files else "ERROR", mandatory=True, tool="scan_project.py", detail=f"{len(files)} files scanned"))

    if parse_errors:
        findings.append(_finding(
            id="SOURCE-PLIST-PARSE",
            title="One or more release property lists could not be parsed",
            severity="HIGH",
            category="bundle-configuration",
            guideline="2.1 App Completeness; 2.5 Software Requirements",
            confidence="HIGH",
            evidence=parse_errors[:MAX_HITS_PER_SIGNAL],
            rationale="Purpose strings, ATS settings, entitlements, or privacy manifests may be malformed or hidden from deterministic review.",
            remediation="Validate the final resolved plist files with plutil on macOS; ensure source placeholders resolve in the release archive.",
            verification=["Run plutil -lint on every Info.plist and PrivacyInfo.xcprivacy, then inspect the archive."],
            sources=["references/privacy-security.md"],
        ))

    capacitor_facts, capacitor_findings, capacitor_checks = _scan_capacitor(
        root, text_by_path, plists, manifests,
    )
    if capacitor_facts:
        facts["capacitor"] = capacitor_facts
        findings.extend(capacitor_findings)
        checks.extend(capacitor_checks)

    # Hardcoded secrets.
    secret_evidence: list[dict[str, Any]] = []
    secret_types: set[str] = set()
    compiled_secret_res = [(name, re.compile(pattern)) for name, pattern in SECRET_PATTERNS]
    for path, text in text_by_path.items():
        for secret_name, pattern in compiled_secret_res:
            for match in pattern.finditer(text):
                snippet = match.group(0)
                masked = snippet[:6] + "…" + snippet[-4:] if len(snippet) > 14 else "<redacted>"
                secret_evidence.append(make_evidence(kind="source", location=_relative(path, root), line=_line_for(text, match.start()), detail=f"Possible {secret_name}: {masked}"))
                secret_types.add(secret_name)
                if len(secret_evidence) >= MAX_HITS_PER_SIGNAL:
                    break
            if len(secret_evidence) >= MAX_HITS_PER_SIGNAL:
                break
        if len(secret_evidence) >= MAX_HITS_PER_SIGNAL:
            break
    if secret_evidence:
        findings.append(_finding(
            id="SOURCE-HARDCODED-SECRET",
            title="Potential production secret is committed in the project",
            severity="BLOCKER",
            category="security",
            guideline="5.1 Privacy; Developer Program security obligations",
            confidence="HIGH",
            evidence=secret_evidence,
            rationale="Client-side secrets can be extracted from source or the binary, expose user/provider data, and allow unauthorized API use. The report masks values but the key must be treated as compromised.",
            remediation="Revoke/rotate the secret, remove it from history and the client, and route privileged provider calls through an authenticated backend or platform-supported key protection.",
            verification=["Scan repository history and the final app binary; confirm the old credential is revoked and no replacement secret is embedded."],
            sources=["references/privacy-security.md"],
            tags=tuple(sorted(secret_types)),
        ))
    checks.append(make_check("source.secrets", "Hardcoded secret scan", "ERROR" if secret_evidence else "PASS", mandatory=True, tool="scan_project.py", detail=f"{len(secret_evidence)} candidate(s)"))

    # Info.plist purpose strings and declared permission scope.
    usage_values = _all_usage_descriptions(plists)
    permission_hits: dict[str, list[dict[str, Any]]] = {}
    for permission, patterns in PERMISSION_SOURCE_PATTERNS.items():
        evidence: list[dict[str, Any]] = []
        for path, text in text_by_path.items():
            evidence.extend(_hits(text, patterns, path, root, limit=max(0, MAX_HITS_PER_SIGNAL - len(evidence))))
            if len(evidence) >= MAX_HITS_PER_SIGNAL:
                break
        if evidence:
            permission_hits[permission] = evidence
            acceptable_keys = PERMISSION_USAGE_KEYS.get(permission, ())
            present_keys = [key for key in acceptable_keys if key in usage_values]
            if not present_keys:
                findings.append(_finding(
                    id=f"SOURCE-PURPOSE-{permission.upper().replace('-', '_')}-MISSING",
                    title=f"{permission.replace('-', ' ').title()} API signal has no matching usage-description evidence",
                    severity="HIGH",
                    category="permissions",
                    guideline="5.1.1(ii) Permission; 2.5 Software Requirements",
                    confidence="MEDIUM",
                    status="NEEDS_REVIEW",
                    automation="heuristic",
                    evidence=evidence[:4],
                    rationale="Protected-resource access normally requires a clear Info.plist purpose string. Source signals may include dead/test code, so confirm in the resolved release target before treating this as a direct violation.",
                    remediation=f"For every release target using this API, add a specific localized purpose string using one of: {', '.join(acceptable_keys) or 'the current platform key'}; otherwise remove the access.",
                    verification=["Inspect the final archive Info.plist and trigger the permission from a fresh install."],
                    sources=["references/privacy-security.md"],
                ))
    facts["permission_signals"] = {key: len(value) for key, value in permission_hits.items()}
    facts["usage_description_keys"] = sorted(usage_values)

    generic_terms = {"needed", "required", "permission required", "we need access", "used by app", "allow access", "access"}
    for key, values in sorted(usage_values.items()):
        for path, value in values:
            text = str(value or "").strip()
            if not text or text.casefold() in generic_terms or len(text) < 12:
                findings.append(_finding(
                    id=f"SOURCE-PURPOSE-{key.upper()}-GENERIC",
                    title="Permission purpose string is empty or insufficiently specific",
                    severity="HIGH",
                    category="permissions",
                    guideline="5.1.1(ii) Permission",
                    confidence="HIGH",
                    evidence=[make_evidence(kind="plist", location=_relative(path, root), detail=f"{key}={text!r}")],
                    rationale="Purpose strings must completely explain how the app uses the protected data; generic language can cause rejection and does not support informed consent.",
                    remediation="Describe the exact feature, data used, and user benefit in plain localized language. Do not claim a use that the build does not perform.",
                    verification=["Delete the app, reinstall, trigger the prompt, and visually review each locale."],
                    sources=["references/privacy-security.md"],
                ))

    declared_permissions = set(features.get("permissions", []) or [])
    detected_permissions = set(permission_hits)
    undeclared_permissions = sorted(detected_permissions - declared_permissions)
    if undeclared_permissions and config:
        findings.append(_finding(
            id="SOURCE-PERMISSIONS-SCOPE-MISMATCH",
            title="Source indicates permissions absent from review-input scope",
            severity="MEDIUM",
            category="evidence-consistency",
            guideline="2.3 Accurate Metadata; 5.1 Privacy",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=[make_evidence(kind="source-summary", location=str(root), detail="Detected but undeclared permission signals", value=undeclared_permissions)],
            rationale="The audit scope may be stale, or the project may contain dead code/third-party SDK access. Either case must be resolved before privacy labels and runtime checks can be trusted.",
            remediation="Confirm release-target reachability and update review-input/App Privacy/purpose strings or remove the access.",
            verification=["Inspect the archive and runtime permission prompts for the exact release build."],
            sources=["references/privacy-security.md"],
        ))

    # ATS and endpoints.
    ats_arbitrary: list[dict[str, Any]] = []
    for path, plist in plists:
        ats = plist.get("NSAppTransportSecurity")
        if isinstance(ats, dict) and (ats.get("NSAllowsArbitraryLoads") is True or ats.get("NSAllowsArbitraryLoadsInWebContent") is True):
            ats_arbitrary.append(make_evidence(kind="plist", location=_relative(path, root), detail="App Transport Security allows arbitrary loads", value=ats))
    if ats_arbitrary:
        findings.append(_finding(
            id="SOURCE-ATS-ARBITRARY-LOADS",
            title="App Transport Security permits broad insecure network loads",
            severity="HIGH",
            category="security",
            guideline="5.1 Privacy; 2.5 Software Requirements",
            confidence="CERTAIN",
            evidence=ats_arbitrary,
            rationale="Broad ATS exceptions increase interception risk and may be questioned when a narrower domain exception or HTTPS is feasible.",
            remediation="Remove arbitrary-load exceptions; use HTTPS and the narrowest current ATS exception only with documented necessity.",
            verification=["Inspect the resolved archive plist and proxy all release network traffic for cleartext requests."],
            sources=["references/privacy-security.md"],
        ))

    http_evidence: list[dict[str, Any]] = []
    external_payment_evidence: list[dict[str, Any]] = []
    urls_seen: set[str] = set()
    for path, text in text_by_path.items():
        for match in URL_RE.finditer(text):
            url = match.group(0).rstrip(".,;:")
            if url in urls_seen:
                continue
            urls_seen.add(url)
            parsed = urlparse(url)
            host = (parsed.hostname or "").lower()
            is_plist_doctype = host == "www.apple.com" and parsed.path == "/DTDs/PropertyList-1.0.dtd"
            if parsed.scheme == "http" and host not in {"localhost", "127.0.0.1", "0.0.0.0"} and not is_plist_doctype:
                http_evidence.append(make_evidence(kind="source", location=_relative(path, root), line=_line_for(text, match.start()), detail=f"Cleartext URL: {url}"))
            if any(host == domain or host.endswith("." + domain) for domain in EXTERNAL_PAYMENT_HOSTS):
                external_payment_evidence.append(make_evidence(kind="source", location=_relative(path, root), line=_line_for(text, match.start()), detail=f"External payment host: {host}"))
    if http_evidence:
        findings.append(_finding(
            id="SOURCE-CLEARTEXT-ENDPOINT",
            title="Project contains non-local cleartext HTTP endpoints",
            severity="HIGH",
            category="security",
            guideline="5.1 Privacy; 2.5 Software Requirements",
            confidence="HIGH",
            evidence=http_evidence[:MAX_HITS_PER_SIGNAL],
            rationale="Cleartext transport can expose credentials, personal data, or content and may require ATS exceptions.",
            remediation="Migrate production endpoints to HTTPS and remove release references to cleartext hosts.",
            verification=["Inspect release traffic and the archive for http:// strings."],
            sources=["references/privacy-security.md"],
        ))

    # Placeholder/staging signals.
    placeholder_evidence: list[dict[str, Any]] = []
    for path, text in text_by_path.items():
        # Ignore common docs/examples unless they are configuration/source files likely to ship.
        if path.suffix.lower() == ".md" and path.name.lower() in {"readme.md", "contributing.md"}:
            continue
        placeholder_evidence.extend(_hits(text, PLACEHOLDER_PATTERNS, path, root, limit=max(0, MAX_HITS_PER_SIGNAL - len(placeholder_evidence))))
        if len(placeholder_evidence) >= MAX_HITS_PER_SIGNAL:
            break
    if placeholder_evidence:
        findings.append(_finding(
            id="SOURCE-PLACEHOLDER-STAGING",
            title="Project contains placeholder, test, localhost, or staging signals",
            severity="MEDIUM",
            category="app-completeness",
            guideline="2.1 App Completeness",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=placeholder_evidence,
            rationale="These strings may be harmless test code, but a reachable development endpoint, unfinished label, or mock path is a common completeness failure.",
            remediation="Prove each hit is excluded from the release target or replace it with final production behavior/content.",
            verification=["Search the built app and execute the related feature in Release configuration."],
            sources=["references/runtime-review.md", "references/community-signals.md"],
        ))

    # Privacy manifests and required-reason APIs.
    manifest_api_map = _manifest_api_map(manifests)
    facts["privacy_manifest_api_reasons"] = {key: sorted(value) for key, value in manifest_api_map.items()}
    facts["privacy_manifest_collected_data"] = _manifest_collected_types(manifests)
    malformed_manifest_evidence: list[dict[str, Any]] = []
    for path, manifest in manifests:
        if "NSPrivacyTracking" in manifest and not isinstance(manifest.get("NSPrivacyTracking"), bool):
            malformed_manifest_evidence.append(make_evidence(kind="privacy-manifest", location=_relative(path, root), detail="NSPrivacyTracking must be Boolean"))
        if manifest.get("NSPrivacyTracking") is True and not isinstance(manifest.get("NSPrivacyTrackingDomains"), list):
            malformed_manifest_evidence.append(make_evidence(kind="privacy-manifest", location=_relative(path, root), detail="Tracking is true but NSPrivacyTrackingDomains is absent/not an array"))
        entries = manifest.get("NSPrivacyAccessedAPITypes", [])
        if entries is not None and not isinstance(entries, list):
            malformed_manifest_evidence.append(make_evidence(kind="privacy-manifest", location=_relative(path, root), detail="NSPrivacyAccessedAPITypes must be an array"))
    if malformed_manifest_evidence:
        findings.append(_finding(
            id="SOURCE-PRIVACY-MANIFEST-MALFORMED",
            title="Privacy manifest structure is malformed",
            severity="BLOCKER",
            category="privacy-manifest",
            guideline="5.1 Privacy; submission requirements",
            confidence="CERTAIN",
            evidence=malformed_manifest_evidence,
            rationale="A malformed PrivacyInfo.xcprivacy can fail upload validation or produce inaccurate privacy reporting.",
            remediation="Correct the property-list types and validate the final embedded manifest with plutil and archive inspection.",
            verification=["Run plutil -lint and inspect every embedded framework manifest in the archive."],
            sources=["references/privacy-security.md"],
        ))

    for category, reasons in manifest_api_map.items():
        known = REQUIRED_REASON_API_CATEGORIES.get(category)
        if known is None:
            findings.append(_finding(
                id=f"SOURCE-PRIVACY-REASON-UNKNOWN-{category}",
                title="Privacy manifest contains an unrecognized required-reason API category",
                severity="HIGH",
                category="privacy-manifest",
                guideline="Required-reason APIs",
                confidence="HIGH",
                status="NEEDS_REVIEW",
                automation="catalog-freshness",
                evidence=[make_evidence(kind="privacy-manifest", location=str(root), detail=f"Category: {category}; reasons: {sorted(reasons)}")],
                rationale="The pinned catalog may be stale or the category may be misspelled. A ready gate requires comparison with Apple's current list.",
                remediation="Check the current official required-reason API catalog and update the manifest/catalog as appropriate.",
                verification=["Run check_policy_freshness.py --network and inspect the final archive."],
                sources=["references/privacy-security.md", "references/source-index.md"],
            ))
        else:
            invalid = sorted(reason for reason in reasons if reason not in known)
            if invalid:
                findings.append(_finding(
                    id=f"SOURCE-PRIVACY-REASON-INVALID-{category}",
                    title="Privacy manifest uses an unrecognized reason identifier",
                    severity="BLOCKER",
                    category="privacy-manifest",
                    guideline="Required-reason APIs",
                    confidence="HIGH",
                    evidence=[make_evidence(kind="privacy-manifest", location=str(root), detail=f"Category: {category}; invalid reasons: {invalid}")],
                    rationale="App Store Connect validates approved reason identifiers for covered API categories.",
                    remediation="Select only current approved reasons that truthfully match the app/SDK behavior; do not copy a reason solely to satisfy validation.",
                    verification=["Compare every identifier and stated behavior with Apple's current catalog and the final archive privacy report."],
                    sources=["references/privacy-security.md"],
                ))

    required_reason_hits: dict[str, list[dict[str, Any]]] = {}
    for category, patterns in REQUIRED_REASON_SOURCE_PATTERNS.items():
        evidence: list[dict[str, Any]] = []
        for path, text in text_by_path.items():
            evidence.extend(_hits(text, patterns, path, root, limit=max(0, 6 - len(evidence))))
            if len(evidence) >= 6:
                break
        if evidence:
            required_reason_hits[category] = evidence
            if category not in manifest_api_map:
                findings.append(_finding(
                    id=f"SOURCE-PRIVACY-REASON-MISSING-{category}",
                    title="Required-reason API signal is not covered by supplied privacy manifests",
                    severity="HIGH",
                    category="privacy-manifest",
                    guideline="Required-reason APIs",
                    confidence="MEDIUM",
                    status="NEEDS_REVIEW",
                    automation="heuristic",
                    evidence=evidence,
                    rationale="Source use of a listed API category may require an approved reason in the app or responsible SDK manifest. Dead code and wrappers can produce false positives, so archive confirmation is mandatory.",
                    remediation="Determine the exact caller and purpose; add a truthful approved reason to the correct manifest or remove the API.",
                    verification=["Inspect the generated privacy report/final archive and run App Store Connect validation."],
                    sources=["references/privacy-security.md"],
                ))
    facts["required_reason_api_signals"] = {key: len(value) for key, value in required_reason_hits.items()}

    # Listed third-party SDK signals.
    listed_sdk_evidence: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path, text in text_by_path.items():
        normalized_path = _relative(path, root).casefold()
        lowered = text.casefold()
        for sdk in LISTED_THIRD_PARTY_SDKS:
            needle = sdk.casefold()
            if needle in normalized_path or needle in lowered:
                if len(listed_sdk_evidence[sdk]) < 3:
                    index = lowered.find(needle)
                    listed_sdk_evidence[sdk].append(make_evidence(
                        kind="dependency",
                        location=_relative(path, root),
                        line=_line_for(text, index) if index >= 0 else None,
                        detail=f"Listed SDK signal: {sdk}",
                    ))
    facts["listed_sdk_signals"] = sorted(listed_sdk_evidence)
    if listed_sdk_evidence and not manifests:
        evidence = []
        for sdk in sorted(listed_sdk_evidence)[:8]:
            evidence.extend(listed_sdk_evidence[sdk][:1])
        findings.append(_finding(
            id="SOURCE-LISTED-SDK-NO-MANIFEST",
            title="Listed third-party SDK signals exist but no privacy manifest was found in source evidence",
            severity="HIGH",
            category="third-party-sdk",
            guideline="Third-party SDK privacy manifest/signature requirements",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=evidence,
            rationale="Apple requires privacy manifests and signatures for SDKs on its current list. Dependency text does not prove what is embedded, so inspect the final archive before deciding compliance.",
            remediation="Upgrade each listed SDK to a compliant signed version and verify its embedded PrivacyInfo.xcprivacy; remove unused SDKs.",
            verification=["Enumerate frameworks in the final archive and compare each listed SDK with Apple's current requirement page."],
            sources=["references/privacy-security.md"],
        ))

    # Tracking and ATT consistency.
    tracking_evidence: list[dict[str, Any]] = []
    att_evidence: list[dict[str, Any]] = []
    for path, text in text_by_path.items():
        tracking_evidence.extend(_hits(text, TRACKING_SDK_PATTERNS, path, root, limit=max(0, 8 - len(tracking_evidence))))
        att_evidence.extend(_hits(text, ("ATTrackingManager", "requestTrackingAuthorization"), path, root, limit=max(0, 4 - len(att_evidence))))
        if len(tracking_evidence) >= 8 and len(att_evidence) >= 4:
            break
    tracking_config = bool(features.get("ads_tracking", {}).get("tracking"))
    if tracking_config and not att_evidence:
        findings.append(_finding(
            id="SOURCE-TRACKING-NO-ATT-FLOW",
            title="Tracking is declared but no ATT request implementation was detected",
            severity="HIGH",
            category="tracking",
            guideline="5.1.2(i) Data Use and Sharing",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=[make_evidence(kind="config", location=str(config_path or root), detail="features.ads_tracking.tracking=true")],
            rationale="Tracking requires explicit permission through App Tracking Transparency before tracking occurs. The flow may live in a dependency, so runtime/network verification is required.",
            remediation="Implement ATT with truthful purpose text and prevent SDK tracking until authorization; otherwise disable tracking and correct privacy declarations.",
            verification=["Fresh-install, deny ATT, and verify no tracking identifiers/cross-app data are transmitted."],
            sources=["references/privacy-security.md"],
        ))
    if tracking_evidence and not tracking_config and config:
        findings.append(_finding(
            id="SOURCE-TRACKING-SDK-SCOPE-MISMATCH",
            title="Analytics/advertising SDK signals conflict with tracking=false scope",
            severity="MEDIUM",
            category="tracking",
            guideline="5.1 Privacy",
            confidence="LOW",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=tracking_evidence,
            rationale="An SDK can be configured without tracking, but the release configuration and App Privacy answers must prove that distinction.",
            remediation="Document SDK data collection/linkage configuration and disable advertising/tracking features unless declared and consented.",
            verification=["Inspect outbound requests with ATT denied and compare the SDK's current privacy documentation."],
            sources=["references/privacy-security.md"],
        ))

    # AI detection, consent, personal data, and Foundation Models.
    ai_provider_evidence: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path, text in text_by_path.items():
        for provider, patterns in AI_PROVIDER_PATTERNS.items():
            hit = _hits(text, patterns, path, root, limit=2)
            if hit:
                ai_provider_evidence[provider].extend(hit[: max(0, 3 - len(ai_provider_evidence[provider]))])
    foundation_evidence: list[dict[str, Any]] = []
    consent_evidence: list[dict[str, Any]] = []
    personal_data_evidence: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path, text in text_by_path.items():
        foundation_evidence.extend(_hits(text, FOUNDATION_MODELS_PATTERNS, path, root, limit=max(0, 6 - len(foundation_evidence))))
        consent_evidence.extend(_hits(text, CONSENT_PATTERNS, path, root, limit=max(0, 8 - len(consent_evidence))))
        for data_type, patterns in PERSONAL_DATA_SOURCE_PATTERNS.items():
            if len(personal_data_evidence[data_type]) < 3:
                personal_data_evidence[data_type].extend(_hits(text, patterns, path, root, limit=max(0, 3 - len(personal_data_evidence[data_type]))))
    detected_providers = sorted(ai_provider_evidence)
    facts["ai"] = {
        "providers_detected": detected_providers,
        "foundation_models_signal": bool(foundation_evidence),
        "consent_signal_count": len(consent_evidence),
        "personal_data_signals": sorted(key for key, value in personal_data_evidence.items() if value),
    }
    ai_config = features.get("ai", {})
    if detected_providers and config and not ai_config.get("enabled"):
        evidence = [item for provider in detected_providers[:4] for item in ai_provider_evidence[provider][:1]]
        findings.append(_finding(
            id="SOURCE-AI-UNDECLARED",
            title="Third-party AI provider signals are absent from review scope",
            severity="HIGH",
            category="ai-consistency",
            guideline="2.3 Accurate Metadata; 5.1 Privacy",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=evidence,
            rationale="The project may contain an AI path or SDK that is not represented in privacy, age-rating, safety, and review-note evidence.",
            remediation="Confirm release reachability; declare every AI feature/provider or remove excluded/dead integration from the release target.",
            verification=["Exercise all feature entry points and inspect release network destinations."],
            sources=["references/ai-review.md"],
        ))
    declared_providers = {str(value).casefold() for value in ai_config.get("providers", []) or []}
    provider_mismatch = [provider for provider in detected_providers if provider.casefold() not in declared_providers]
    if ai_config.get("enabled") and provider_mismatch:
        findings.append(_finding(
            id="SOURCE-AI-PROVIDER-MISMATCH",
            title="Detected AI provider is not declared in review-input",
            severity="HIGH",
            category="ai-consistency",
            guideline="5.1.2(i) Data Use and Sharing",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=[item for provider in provider_mismatch[:4] for item in ai_provider_evidence[provider][:1]],
            rationale="Undeclared recipients can invalidate consent copy, privacy policy, App Privacy answers, subprocessors, and review notes.",
            remediation="Reconcile actual endpoints and intermediaries with the provider map; remove stale SDKs or update all disclosures.",
            verification=["Proxy the first AI request and compare every destination with the approved data-flow map."],
            sources=["references/ai-review.md"],
        ))
    if ai_config.get("enabled") and ai_config.get("third_party") and ai_config.get("personal_data_types") and not consent_evidence:
        findings.append(_finding(
            id="SOURCE-AI-CONSENT-NOT-FOUND",
            title="No source evidence of pre-transmission third-party AI consent was found",
            severity="HIGH",
            category="ai-privacy",
            guideline="5.1.2(i) Data Use and Sharing",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=[make_evidence(kind="config", location=str(config_path or root), detail="Third-party AI personal data types", value=ai_config.get("personal_data_types"))],
            rationale="Apple explicitly requires clear disclosure and permission before personal data is shared with third-party AI. Naming patterns can miss a valid implementation, so runtime denial/network evidence controls the final decision.",
            remediation="Implement an informed consent gate naming data categories, recipient/provider, purpose, and material retention/training behavior before any personal-data request.",
            verification=["Fresh-install, deny consent, and prove no request containing personal data reaches any provider or intermediary."],
            sources=["references/ai-review.md", "references/privacy-security.md", "references/community-signals.md"],
        ))
    if foundation_evidence and config and not ai_config.get("foundation_models"):
        findings.append(_finding(
            id="SOURCE-FOUNDATION-MODELS-SCOPE",
            title="Foundation Models framework signal is absent from review scope",
            severity="MEDIUM",
            category="ai-consistency",
            guideline="Apple Foundation Models acceptable-use requirements",
            confidence="HIGH",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=foundation_evidence,
            rationale="Foundation Models usage introduces platform acceptable-use and safeguard review that the current scope would skip.",
            remediation="Confirm the framework is in the release target, set foundation_models=true, and apply the AI/acceptable-use branch.",
            verification=["Inspect linked frameworks and execute the feature on a supported device/OS."],
            sources=["references/ai-review.md"],
        ))

    # Accounts and login.
    creation_evidence: list[dict[str, Any]] = []
    deletion_evidence: list[dict[str, Any]] = []
    social_evidence: dict[str, list[dict[str, Any]]] = defaultdict(list)
    privacy_login_evidence: list[dict[str, Any]] = []
    for path, text in text_by_path.items():
        creation_evidence.extend(_hits(text, ACCOUNT_CREATION_PATTERNS, path, root, limit=max(0, 6 - len(creation_evidence))))
        deletion_evidence.extend(_hits(text, ACCOUNT_DELETION_PATTERNS, path, root, limit=max(0, 6 - len(deletion_evidence))))
        privacy_login_evidence.extend(_hits(text, PRIVACY_PRESERVING_LOGIN_PATTERNS, path, root, limit=max(0, 6 - len(privacy_login_evidence))))
        for provider, patterns in SOCIAL_LOGIN_PATTERNS.items():
            social_evidence[provider].extend(_hits(text, patterns, path, root, limit=max(0, 3 - len(social_evidence[provider]))))
    detected_social = sorted(provider for provider, evidence in social_evidence.items() if evidence)
    facts["accounts"] = {
        "creation_signal": bool(creation_evidence),
        "deletion_signal": bool(deletion_evidence),
        "social_logins_detected": detected_social,
        "privacy_preserving_login_signal": bool(privacy_login_evidence),
    }
    accounts = features.get("accounts", {})
    if (accounts.get("creation") or creation_evidence) and not (accounts.get("deletion_in_app") or deletion_evidence):
        findings.append(_finding(
            id="SOURCE-ACCOUNT-DELETION-NOT-FOUND",
            title="Account creation is present but in-app account deletion was not evidenced",
            severity="HIGH",
            category="accounts",
            guideline="5.1.1(v) Account Sign-In",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=(creation_evidence[:4] or [make_evidence(kind="config", location=str(config_path or root), detail="features.accounts.creation=true")]),
            rationale="Apps supporting account creation must also offer account deletion within the app. Source naming can miss a valid implementation; runtime navigation is mandatory.",
            remediation="Provide a discoverable in-app deletion flow that deletes the account and associated data, with only legally required retention explained.",
            verification=["Create an account, delete it entirely in app, confirm backend deletion, and test re-login behavior."],
            sources=["references/privacy-security.md"],
        ))
    if detected_social and not (privacy_login_evidence or accounts.get("privacy_preserving_login") or accounts.get("login_exception")):
        findings.append(_finding(
            id="SOURCE-LOGIN-EQUIVALENT-NOT-FOUND",
            title="Social-login signals lack an equivalent privacy-preserving login option or documented exception",
            severity="HIGH",
            category="login",
            guideline="4.8 Login Services",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=[item for provider in detected_social[:3] for item in social_evidence[provider][:1]],
            rationale="Primary-account social login normally requires an equivalent option with Apple's privacy characteristics. Sign in with Apple is the common implementation, but the guideline allows defined exceptions.",
            remediation="Implement the equivalent option or document and verify the exact exception; ensure data requested and account deletion are equivalent.",
            verification=["Run all login methods from a clean install and compare collected/displayed data."],
            sources=["references/app-type-branches.md"],
        ))

    # Payments.
    payment_evidence: dict[str, list[dict[str, Any]]] = defaultdict(list)
    restore_evidence: list[dict[str, Any]] = []
    for path, text in text_by_path.items():
        for name, patterns in PAYMENT_PATTERNS.items():
            payment_evidence[name].extend(_hits(text, patterns, path, root, limit=max(0, 4 - len(payment_evidence[name]))))
        restore_evidence.extend(_hits(text, RESTORE_PATTERNS, path, root, limit=max(0, 6 - len(restore_evidence))))
    if external_payment_evidence:
        payment_evidence["external_host"].extend(external_payment_evidence[:4])
    facts["payments"] = {key: len(value) for key, value in payment_evidence.items() if value}
    commerce = features.get("commerce", {})
    has_storekit = bool(payment_evidence.get("storekit") or payment_evidence.get("revenuecat"))
    has_external = bool(payment_evidence.get("stripe") or payment_evidence.get("paddle") or payment_evidence.get("paypal") or payment_evidence.get("external_checkout") or payment_evidence.get("external_host"))
    if commerce.get("digital_goods") and has_external and not has_storekit:
        evidence = []
        for name in ("stripe", "paddle", "paypal", "external_checkout", "external_host"):
            evidence.extend(payment_evidence.get(name, [])[:2])
        findings.append(_finding(
            id="SOURCE-DIGITAL-GOODS-EXTERNAL-PAYMENT",
            title="Digital-goods scope has external-payment signals without StoreKit evidence",
            severity="BLOCKER",
            category="payments",
            guideline="3.1.1 In-App Purchase",
            confidence="HIGH",
            evidence=evidence[:MAX_HITS_PER_SIGNAL],
            rationale="Unlocking digital content/features in the app normally requires In-App Purchase unless a precise exception, entitlement, regional rule, or US storefront treatment applies. Static source cannot prove storefront gating.",
            remediation="Use StoreKit for in-app digital value or implement/document the exact allowed exception with storefront-specific behavior and entitlements.",
            verification=["Test every target storefront and account state; confirm external links/CTAs are absent where not permitted."],
            sources=["references/business-payments.md"],
        ))
    elif commerce.get("digital_goods") and not has_storekit:
        findings.append(_finding(
            id="SOURCE-DIGITAL-GOODS-NO-STOREKIT",
            title="Digital goods are declared but StoreKit/IAP integration was not detected",
            severity="HIGH",
            category="payments",
            guideline="3.1.1 In-App Purchase",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=[make_evidence(kind="config", location=str(config_path or root), detail="features.commerce.digital_goods=true")],
            rationale="The integration may be abstracted or server-driven, but the release path must use an allowed purchase mechanism.",
            remediation="Provide archive/runtime evidence for StoreKit or document the precise applicable exception.",
            verification=["Fetch and purchase every product in Sandbox using the exact release build."],
            sources=["references/business-payments.md"],
        ))
    if (commerce.get("iap") or has_storekit) and commerce.get("restore_purchases") and not restore_evidence:
        findings.append(_finding(
            id="SOURCE-RESTORE-NOT-FOUND",
            title="Restore purchases is declared but no implementation signal was detected",
            severity="MEDIUM",
            category="payments",
            guideline="3.1.1 In-App Purchase",
            confidence="LOW",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=[make_evidence(kind="config", location=str(config_path or root), detail="restore_purchases=true")],
            rationale="The restore implementation can be hidden behind an SDK, but the control and entitlement recovery must be tested before submission.",
            remediation="Expose a discoverable restore path and reconcile StoreKit entitlements with the backend.",
            verification=["Purchase, delete/reinstall, restore, and verify every durable entitlement."],
            sources=["references/business-payments.md"],
        ))

    # UGC controls.
    ugc_evidence: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path, text in text_by_path.items():
        for name, patterns in UGC_PATTERNS.items():
            ugc_evidence[name].extend(_hits(text, patterns, path, root, limit=max(0, 4 - len(ugc_evidence[name]))))
    ugc_config = features.get("ugc", {})
    ugc_present = bool(ugc_config.get("enabled") or ugc_evidence.get("ugc"))
    if ugc_present:
        missing_controls = []
        for key in ("filter", "report", "block", "support"):
            config_key = "support_contact" if key == "support" else key
            if not (ugc_config.get(config_key) or ugc_evidence.get(key)):
                missing_controls.append(key)
        if missing_controls:
            findings.append(_finding(
                id="SOURCE-UGC-CONTROLS-NOT-FOUND",
                title="UGC/chat signals lack complete filtering, reporting, blocking, or support evidence",
                severity="HIGH",
                category="safety",
                guideline="1.2 User-Generated Content; 4.7.1 when applicable",
                confidence="MEDIUM",
                status="NEEDS_REVIEW",
                automation="heuristic",
                evidence=(ugc_evidence.get("ugc", [])[:4] or [make_evidence(kind="config", location=str(config_path or root), detail="UGC enabled")]),
                rationale="Apps exposing user-generated content or hosted chatbots need effective controls and timely moderation. Source naming can miss valid controls, so runtime abuse testing is required.",
                remediation=f"Implement and document missing controls: {', '.join(missing_controls)}.",
                verification=["Publish objectionable test content, report it, block its author, and verify support/moderation response."],
                sources=["references/app-type-branches.md", "references/ai-review.md"],
        ))
    facts["ugc_signals"] = {key: len(value) for key, value in ugc_evidence.items() if value}

    # Private/deprecated API and dynamic-code signals.
    private_evidence: list[dict[str, Any]] = []
    dynamic_evidence: list[dict[str, Any]] = []
    for path, text in text_by_path.items():
        private_evidence.extend(_hits(text, PRIVATE_OR_DEPRECATED_PATTERNS, path, root, limit=max(0, 8 - len(private_evidence))))
        dynamic_evidence.extend(_hits(text, DYNAMIC_CODE_PATTERNS, path, root, limit=max(0, 8 - len(dynamic_evidence))))
    if private_evidence:
        findings.append(_finding(
            id="SOURCE-PRIVATE-DEPRECATED-API",
            title="Project contains private, deprecated, or review-sensitive API signals",
            severity="HIGH",
            category="software-requirements",
            guideline="2.5.1 Public APIs; 2.5.6 Browser engines; 2.5 Software Requirements",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=private_evidence,
            rationale="Some matches such as UIWebView are directly obsolete; others can be legitimate runtime lookup. The final binary and call context determine compliance.",
            remediation="Remove private/deprecated API use and justify any dynamic symbol lookup using public documented APIs only.",
            verification=["Run Xcode's archive validation and inspect linked symbols in the final binary."],
            sources=["references/rule-matrix.md"],
        ))
    if dynamic_evidence:
        findings.append(_finding(
            id="SOURCE-DYNAMIC-CODE-REVIEW",
            title="Dynamic code or script-execution signals require executable-code review",
            severity="MEDIUM",
            category="software-requirements",
            guideline="2.5.2 Self-contained apps; 4.7 software not embedded in binary",
            confidence="LOW",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=dynamic_evidence,
            rationale="JavaScript/web content is often allowed, but downloading or changing executable app behavior outside permitted 4.7 categories can violate self-contained-app requirements.",
            remediation="Document exactly what code/content is downloaded or interpreted, how it is reviewed, and which 4.7 controls apply; remove arbitrary executable updates.",
            verification=["Capture network responses and prove the app cannot download native executable code or bypass review."],
            sources=["references/app-type-branches.md", "references/rule-matrix.md"],
        ))

    # Web-wrapper/minimum-functionality risk.
    web_evidence: list[dict[str, Any]] = []
    native_evidence: list[dict[str, Any]] = []
    for path, text in text_by_path.items():
        web_evidence.extend(_hits(text, WEB_WRAPPER_PATTERNS, path, root, limit=max(0, 8 - len(web_evidence))))
        native_evidence.extend(_hits(text, NATIVE_VALUE_PATTERNS, path, root, limit=max(0, 12 - len(native_evidence))))
    web_score = len(web_evidence)
    native_score = len(native_evidence)
    facts["minimum_functionality"] = {"web_signals": web_score, "native_value_signals": native_score}
    if web_score and native_score == 0:
        findings.append(_finding(
            id="SOURCE-MINIMUM-FUNCTIONALITY-RISK",
            title="Project has web-wrapper signals without detected native-value evidence",
            severity="HIGH",
            category="design",
            guideline="4.2 Minimum Functionality; 4.3 Spam",
            confidence="LOW",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=web_evidence,
            rationale="A web view is not automatically noncompliant, but thin wrappers, template-generated apps, and indistinguishable AI front ends are recurring 4.2/4.3 rejection patterns.",
            remediation="Prepare a native value dossier and ensure the release offers durable, app-like utility beyond repackaged web content or one generic prompt screen.",
            verification=["Perform a black-box value review and compare the app with its website and materially similar App Store apps."],
            sources=["references/app-type-branches.md", "references/community-signals.md"],
        ))
    elif ai_config.get("enabled") and web_score and native_score < 2:
        findings.append(_finding(
            id="SOURCE-THIN-AI-WRAPPER-RISK",
            title="AI/web architecture may present minimum-functionality or spam risk",
            severity="MEDIUM",
            category="design",
            guideline="4.2 Minimum Functionality; 4.3 Spam",
            confidence="LOW",
            status="NEEDS_REVIEW",
            automation="heuristic",
            evidence=(web_evidence[:4] + [item for provider in detected_providers[:2] for item in ai_provider_evidence[provider][:1]]),
            rationale="Many legitimate AI apps use web/API components; the risk is weak differentiation, template duplication, or an experience equivalent to a simple website/chat prompt.",
            remediation="Document unique workflows, original content/data rights, native integrations, user control, export/history/offline value, and clear differentiation.",
            verification=["Have an independent reviewer evaluate useful functionality before login/payment and compare against the web version."],
            sources=["references/app-type-branches.md", "references/community-signals.md"],
        ))

    # Localizations found in source.
    source_locales: set[str] = set()
    for path in text_by_path:
        match = LOCALE_STRINGS_RE.search(_relative(path, root).replace("\\", "/"))
        if match:
            source_locales.add(match.group(1))
    facts["source_locales"] = sorted(source_locales)
    declared_locales = set(app.get("locales", []) or [])
    if declared_locales and source_locales and not declared_locales.issubset(source_locales | {app.get("primary_locale")}):
        missing = sorted(declared_locales - source_locales - {app.get("primary_locale")})
        if missing:
            findings.append(_finding(
                id="SOURCE-LOCALIZATION-COVERAGE",
                title="Declared App Store locales lack matching source localization evidence",
                severity="MEDIUM",
                category="localization",
                guideline="2.3 Accurate Metadata",
                confidence="LOW",
                status="NEEDS_REVIEW",
                automation="heuristic",
                evidence=[make_evidence(kind="source-summary", location=str(root), detail="No .lproj evidence for locales", value=missing)],
                rationale="The app may use a non-.lproj localization system, but missing in-app localization can create screenshots and metadata that do not match the product experience.",
                remediation="Provide runtime screenshots for each locale and confirm all reviewer-visible strings, paywalls, consent, permissions, and errors are localized.",
                verification=["Launch the release build under each declared language/region and traverse the full review journey."],
                sources=["references/screenshot-review.md"],
            ))

    checks.extend([
        make_check("source.plists", "Info.plist evidence", "PASS" if plists else "SKIPPED", mandatory=True, tool="plistlib", detail=f"{len(plists)} plist(s) parsed"),
        make_check("source.privacy_manifests", "Privacy manifest source evidence", "PASS" if manifests else "SKIPPED", mandatory=bool(manifests or required_reason_hits or listed_sdk_evidence), tool="plistlib", detail=f"{len(manifests)} manifest(s) parsed"),
        make_check("source.permissions", "Protected-resource purpose strings", "PASS" if not permission_hits or usage_values else "NEEDS_REVIEW", mandatory=bool(permission_hits), tool="scan_project.py", detail=f"{len(permission_hits)} permission category signal(s)"),
        make_check("source.ai", "AI source overlay", "PASS" if not ai_config.get("enabled") or bool(detected_providers or foundation_evidence) else "NEEDS_REVIEW", mandatory=bool(ai_config.get("enabled")), tool="scan_project.py", detail=f"providers={detected_providers}; foundation_models={bool(foundation_evidence)}"),
        make_check("source.payments", "Payment implementation signals", "PASS" if not commerce.get("iap") or has_storekit else "NEEDS_REVIEW", mandatory=bool(commerce.get("iap")), tool="scan_project.py", detail=f"storekit={has_storekit}; external={has_external}"),
        make_check("source.static_scan", "Static policy signal scan", "PASS", mandatory=True, tool="scan_project.py", detail=f"Completed bounded scan of {len(text_by_path)} text file(s)"),
    ])

    return {
        "module": "scan_project",
        "generated_at": now_iso(),
        "project": str(root),
        "facts": facts,
        "checks": checks,
        "findings": findings,
        "tool": {"name": "scan_project.py", "status": "OK", "detail": f"Local read-only scan; max_file_bytes={max_file_bytes}"},
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Statically scan an Apple app source tree for App Review risks.")
    parser.add_argument("--project", required=True, help="Project/repository directory")
    parser.add_argument("--config", help="Optional review-input.json")
    parser.add_argument("--max-file-bytes", type=int, default=MAX_DEFAULT_FILE_BYTES, help="Skip individual files larger than this")
    parser.add_argument("--output", help="Write structured JSON result")
    parser.add_argument("--strict", action="store_true", help="Exit 2 for open blocker/high findings")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config = load_json(args.config) if args.config else None
        if config is not None and not isinstance(config, dict):
            raise ReviewInputError("Config root must be a JSON object")
        result = scan_project(args.project, config=config, config_path=args.config, max_file_bytes=args.max_file_bytes)
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"scan_project: {exc}\n")
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
