#!/usr/bin/env python3
"""Deterministically inspect App Store screenshots and create visual queues."""

from __future__ import annotations

import argparse
import hashlib
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping

from catalogs import (
    APPLE_SCREENSHOT_SPEC_URL,
    DEVICE_FAMILY_GROUPS,
    REQUIRED_SCREENSHOT_COVERAGE,
    SCREENSHOT_DIMENSIONS,
    groups_for_dimensions,
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

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}
LOCALE_RE = re.compile(r"^[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")
GROUP_ALIASES = {
    "iphone69": "iphone-6.9", "iphone-69": "iphone-6.9", "6.9": "iphone-6.9", "6_9": "iphone-6.9",
    "iphone65": "iphone-6.5", "iphone-65": "iphone-6.5", "6.5": "iphone-6.5", "6_5": "iphone-6.5",
    "iphone63": "iphone-6.3", "iphone-63": "iphone-6.3", "6.3": "iphone-6.3", "6_3": "iphone-6.3",
    "iphone61": "iphone-6.1", "iphone-61": "iphone-6.1", "6.1": "iphone-6.1", "6_1": "iphone-6.1",
    "ipad13": "ipad-13", "ipad-13-inch": "ipad-13", "13-inch-ipad": "ipad-13",
    "ipad11": "ipad-11", "ipad-11-inch": "ipad-11",
    "appletv": "apple-tv", "tv": "apple-tv",
    "vision": "vision-pro", "visionpro": "vision-pro",
    "watch": "apple-watch", "applewatch": "apple-watch",
}
GROUP_PRIORITY = [
    "iphone-6.9", "iphone-6.5", "iphone-6.3", "iphone-6.1", "iphone-5.5", "iphone-4.7", "iphone-4", "iphone-3.5",
    "ipad-13", "ipad-12.9", "ipad-11", "ipad-10.5", "ipad-9.7", "mac", "apple-tv", "vision-pro", "apple-watch",
]
VISUAL_CHECKS = [
    "Shows actual app use rather than only a title, splash, login, or marketing card.",
    "UI and feature state match the exact submitted build and current OS behavior.",
    "Locale, currency, price, trial, subscription duration, and legal links are correct.",
    "No clipped, overlapped, truncated, untranslated, placeholder, or debug text is visible.",
    "No real personal data, access token, email, phone, precise location, or private content is exposed.",
    "No misleading performance, health, financial, AI accuracy, ranking, or 'free' claim appears.",
    "No unsupported device/platform frame, fake system UI, Apple endorsement, or third-party trademark misuse appears.",
    "Permission, AI consent, paywall, account deletion, and safety controls shown here are reproducible.",
    "Objectionable/generated/UGC content is consistent with the declared age rating and moderation controls.",
    "The screenshot is legible, visually coherent, and does not hide material terms behind decoration.",
]


def _pillow() -> tuple[Any, Any, Any, Any, Any]:
    try:
        from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat  # type: ignore
    except ImportError as exc:
        raise ReviewInputError("Pillow is required. Install requirements.txt before screenshot inspection.") from exc
    return Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat


def _normalize_group(part: str) -> str | None:
    value = part.casefold().replace(" ", "-")
    if value in SCREENSHOT_DIMENSIONS:
        return value
    compact = value.replace("_", "-")
    if compact in SCREENSHOT_DIMENSIONS:
        return compact
    return GROUP_ALIASES.get(value) or GROUP_ALIASES.get(compact)


def _infer_locale_and_group(path: Path, root: Path, primary_locale: str) -> tuple[str, str | None, list[str]]:
    relative = path.relative_to(root)
    locale = primary_locale
    folder_group: str | None = None
    diagnostics: list[str] = []
    for part in relative.parts[:-1]:
        if LOCALE_RE.match(part):
            locale = part
        group = _normalize_group(part)
        if group:
            if folder_group and group != folder_group:
                diagnostics.append(f"multiple group hints: {folder_group}, {group}")
            folder_group = group
    return locale, folder_group, diagnostics


def _choose_group(matches: list[str], folder_group: str | None) -> str | None:
    if folder_group and folder_group in matches:
        return folder_group
    for group in GROUP_PRIORITY:
        if group in matches:
            return group
    return matches[0] if matches else folder_group


def _dhash(image: Any, image_module: Any) -> str:
    resampling = getattr(image_module, "Resampling", image_module)
    grayscale = image.convert("L").resize((9, 8), resampling.LANCZOS)
    pixels = list(grayscale.getdata())
    bits = []
    for row in range(8):
        offset = row * 9
        for col in range(8):
            bits.append(1 if pixels[offset + col] > pixels[offset + col + 1] else 0)
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return f"{value:016x}"


def _hamming_hex(left: str, right: str) -> int:
    return (int(left, 16) ^ int(right, 16)).bit_count()


def _image_metrics(image: Any, image_module: Any, image_filter: Any, image_stat: Any) -> dict[str, float]:
    resampling = getattr(image_module, "Resampling", image_module)
    thumb = image.convert("RGB")
    thumb.thumbnail((256, 256), resampling.LANCZOS)
    gray = thumb.convert("L")
    stat = image_stat.Stat(gray)
    stddev = float(stat.stddev[0]) if stat.stddev else 0.0
    entropy = float(gray.entropy())
    quantized = thumb.quantize(colors=32)
    colors = quantized.getcolors(maxcolors=32 * 256) or []
    pixels = max(1, thumb.width * thumb.height)
    dominant_ratio = max((count for count, _ in colors), default=0) / pixels
    edges = gray.filter(image_filter.FIND_EDGES)
    edge_stat = image_stat.Stat(edges)
    edge_mean = float(edge_stat.mean[0]) if edge_stat.mean else 0.0
    return {
        "stddev": round(stddev, 4),
        "entropy": round(entropy, 4),
        "dominant_color_ratio": round(dominant_ratio, 4),
        "edge_mean": round(edge_mean, 4),
    }


def _has_alpha(image: Any) -> bool:
    bands = image.getbands()
    return "A" in bands or "transparency" in image.info


def _contact_sheet(entries: list[dict[str, Any]], root: Path, output: Path, title: str) -> None:
    Image, ImageDraw, _, ImageFont, ImageOps, _ = _pillow()
    if not entries:
        return
    thumb_width = 300
    thumb_height = 430
    label_height = 62
    columns = min(4, max(1, len(entries)))
    rows = math.ceil(len(entries) / columns)
    margin = 20
    header = 52
    sheet = Image.new("RGB", (margin * 2 + columns * thumb_width, margin * 2 + header + rows * (thumb_height + label_height)), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    draw.text((margin, margin), title[:150], fill="black", font=font)
    for index, entry in enumerate(entries):
        row, col = divmod(index, columns)
        x = margin + col * thumb_width
        y = margin + header + row * (thumb_height + label_height)
        source = root / entry["relative_path"]
        try:
            with Image.open(source) as image:
                image = ImageOps.exif_transpose(image).convert("RGB")
                image.thumbnail((thumb_width - 16, thumb_height - 16), Image.Resampling.LANCZOS)
                cell = Image.new("RGB", (thumb_width - 8, thumb_height - 8), "white")
                px = (cell.width - image.width) // 2
                py = (cell.height - image.height) // 2
                cell.paste(image, (px, py))
                sheet.paste(cell, (x + 4, y + 4))
        except Exception as exc:
            draw.rectangle((x + 4, y + 4, x + thumb_width - 4, y + thumb_height - 4), outline="black")
            draw.text((x + 12, y + 12), f"ERROR: {exc}"[:100], fill="black", font=font)
        label = f"{index + 1:02d} {Path(entry['relative_path']).name}\n{entry.get('width')}x{entry.get('height')} · {entry.get('group') or 'unknown'}"
        draw.multiline_text((x + 6, y + thumb_height + 4), label[:180], fill="black", font=font, spacing=2)
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, format="PNG")


def inspect_screenshots(
    screenshots: str | Path,
    *,
    config: Mapping[str, Any] | None = None,
    config_path: str | Path | None = None,
    contact_sheets: str | Path | None = None,
) -> dict[str, Any]:
    Image, _, ImageFilter, _, ImageOps, ImageStat = _pillow()
    root = Path(screenshots).resolve()
    if not root.exists() or not root.is_dir():
        raise ReviewInputError(f"Screenshot directory not found: {root}")
    config = dict(config or {})
    if config_path:
        config = resolve_config_paths(config, config_path)
    app = config.get("app", {})
    primary_locale = str(app.get("primary_locale") or (app.get("locales", []) or ["en-US"])[0])
    declared_locales = list(app.get("locales", []) or [primary_locale])
    device_families = list(app.get("device_families", []) or [])

    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    entries: list[dict[str, Any]] = []
    unsupported_files: list[str] = []

    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        if contact_sheets and Path(contact_sheets).resolve() in path.resolve().parents:
            continue
        if path.suffix.lower() not in IMAGE_SUFFIXES:
            if path.suffix.lower() in {".gif", ".webp", ".heic", ".heif", ".tiff", ".bmp"}:
                unsupported_files.append(str(path.relative_to(root)))
            continue
        locale, folder_group, folder_diagnostics = _infer_locale_and_group(path, root, primary_locale)
        entry: dict[str, Any] = {
            "relative_path": str(path.relative_to(root)),
            "locale": locale,
            "folder_group": folder_group,
            "folder_diagnostics": folder_diagnostics,
            "sha256": sha256_file(path),
        }
        try:
            with Image.open(path) as image:
                image.load()
                width, height = image.size
                matches = groups_for_dimensions(width, height)
                group = _choose_group(matches, folder_group)
                exif_orientation = None
                try:
                    exif_orientation = image.getexif().get(274)
                except Exception:
                    exif_orientation = None
                entry.update({
                    "format": str(image.format or "").upper(),
                    "mode": image.mode,
                    "width": width,
                    "height": height,
                    "orientation": "portrait" if height > width else ("landscape" if width > height else "square"),
                    "dimension_matches": matches,
                    "group": group,
                    "has_alpha": _has_alpha(image),
                    "exif_orientation": exif_orientation,
                    "dhash": _dhash(ImageOps.exif_transpose(image), Image),
                    "metrics": _image_metrics(ImageOps.exif_transpose(image), Image, ImageFilter, ImageStat),
                })
        except Exception as exc:
            entry["error"] = str(exc)
        entries.append(entry)

    if unsupported_files:
        findings.append(make_finding(
            id="SCREENSHOT-UNSUPPORTED-FORMAT",
            title="Screenshot directory contains unsupported image formats",
            severity="BLOCKER",
            category="screenshots",
            guideline="2.3 Accurate Metadata; screenshot specifications",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="screenshot", location=str(root), detail="Unsupported files", value=unsupported_files[:30])],
            rationale="App Store Connect accepts screenshot uploads only in JPEG/JPG/PNG formats.",
            remediation="Export final screenshots as .jpg/.jpeg or .png without alpha channels.",
            verification=["Rerun inspect_screenshots.py and upload the exact files to App Store Connect."],
            sources=[APPLE_SCREENSHOT_SPEC_URL, "references/screenshot-review.md"],
        ))

    if not entries:
        findings.append(make_finding(
            id="SCREENSHOT-NONE",
            title="No App Store screenshots were found",
            severity="BLOCKER",
            category="screenshots",
            guideline="2.3 Accurate Metadata; screenshot specifications",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="filesystem", location=str(root), detail="No .png/.jpg/.jpeg files found")],
            rationale="Required device families need at least one valid screenshot for the product page.",
            remediation="Capture final screenshots from the exact release build and organize them by locale/device family.",
            verification=["Rerun the screenshot inspector and compare the files with App Store Connect."],
            sources=[APPLE_SCREENSHOT_SPEC_URL, "references/screenshot-review.md"],
        ))
    checks.append(make_check("screenshots.inventory", "Screenshot inventory", "PASS" if entries else "ERROR", mandatory=True, tool="Pillow", detail=f"{len(entries)} supported image file(s)"))

    # Per-file deterministic checks.
    for index, entry in enumerate(entries, start=1):
        location = str(root / entry["relative_path"])
        if entry.get("error"):
            findings.append(make_finding(
                id=f"SCREENSHOT-READ-{index:03d}",
                title="Screenshot cannot be decoded",
                severity="BLOCKER",
                category="screenshots",
                guideline="Screenshot specifications",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="screenshot", location=location, detail=str(entry["error"]))],
                rationale="A corrupt or unsupported file cannot be reviewed or uploaded reliably.",
                remediation="Re-export the screenshot from a trusted image pipeline.",
                verification=["Open the file and rerun the inspector."],
                sources=[APPLE_SCREENSHOT_SPEC_URL],
            ))
            continue
        if entry.get("format") not in {"PNG", "JPEG", "JPG"}:
            findings.append(make_finding(
                id=f"SCREENSHOT-FORMAT-{index:03d}",
                title="Screenshot encoding is not an accepted format",
                severity="BLOCKER",
                category="screenshots",
                guideline="Screenshot specifications",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="screenshot", location=location, detail=f"Pillow format={entry.get('format')}")],
                rationale="The filename extension is not sufficient; the encoded file must be JPEG or PNG.",
                remediation="Re-encode as JPEG or PNG.",
                verification=["Rerun the inspector."],
                sources=[APPLE_SCREENSHOT_SPEC_URL],
            ))
        if entry.get("has_alpha"):
            findings.append(make_finding(
                id=f"SCREENSHOT-ALPHA-{index:03d}",
                title="Screenshot contains an alpha channel or transparency metadata",
                severity="BLOCKER",
                category="screenshots",
                guideline="Screenshot specifications",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="screenshot", location=location, detail=f"mode={entry.get('mode')}; alpha/transparency detected")],
                rationale="Apple's screenshot specification does not permit alpha channels or transparency, even when all pixels appear opaque.",
                remediation="Flatten the image onto an opaque RGB background and export without alpha.",
                verification=["Confirm image bands do not include alpha and rerun the inspector."],
                sources=[APPLE_SCREENSHOT_SPEC_URL],
            ))
        matches = entry.get("dimension_matches", [])
        if not matches:
            findings.append(make_finding(
                id=f"SCREENSHOT-DIMENSIONS-{index:03d}",
                title="Screenshot dimensions do not match an accepted Apple size",
                severity="BLOCKER",
                category="screenshots",
                guideline="Screenshot specifications",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="screenshot", location=location, detail=f"{entry.get('width')} x {entry.get('height')} pixels")],
                rationale="App Store Connect validates screenshots against exact pixel dimensions for each device family.",
                remediation="Capture/export at one of the current exact dimensions in references/screenshot-review.md.",
                verification=["Rerun the inspector and upload the exact file."],
                sources=[APPLE_SCREENSHOT_SPEC_URL, "references/screenshot-review.md"],
            ))
        if entry.get("folder_group") and matches and entry["folder_group"] not in matches:
            findings.append(make_finding(
                id=f"SCREENSHOT-GROUP-MISMATCH-{index:03d}",
                title="Screenshot folder/device label conflicts with its pixel dimensions",
                severity="HIGH",
                category="screenshots",
                guideline="2.3 Accurate Metadata; screenshot specifications",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="screenshot", location=location, detail=f"folder={entry['folder_group']}; dimensions match {matches}")],
                rationale="A mislabeled screenshot can be uploaded to the wrong device slot or make the coverage report unreliable.",
                remediation="Move the file to the correct group or recapture it on the intended device class.",
                verification=["Confirm the App Store Connect screenshot slot and image dimensions agree."],
                sources=[APPLE_SCREENSHOT_SPEC_URL],
            ))
        if entry.get("exif_orientation") not in (None, 1):
            findings.append(make_finding(
                id=f"SCREENSHOT-EXIF-ORIENTATION-{index:03d}",
                title="Screenshot relies on EXIF orientation metadata",
                severity="MEDIUM",
                category="screenshots",
                guideline="2.3 Accurate Metadata",
                confidence="HIGH",
                status="NEEDS_REVIEW",
                automation="deterministic",
                evidence=[make_evidence(kind="screenshot", location=location, detail=f"EXIF orientation={entry.get('exif_orientation')}")],
                rationale="Some upload/rendering pipelines ignore orientation metadata, producing rotated screenshots or dimension mismatches.",
                remediation="Bake the orientation into pixels and remove the EXIF orientation tag.",
                verification=["Open the exported file in multiple viewers and rerun the inspector."],
                sources=["references/screenshot-review.md"],
            ))
        if entry.get("mode") not in {"RGB", "L"} and not entry.get("has_alpha"):
            findings.append(make_finding(
                id=f"SCREENSHOT-COLOR-MODE-{index:03d}",
                title="Screenshot uses an unusual color mode",
                severity="LOW",
                category="screenshots",
                guideline="Screenshot quality",
                confidence="HIGH",
                status="NEEDS_REVIEW",
                automation="deterministic",
                evidence=[make_evidence(kind="screenshot", location=location, detail=f"mode={entry.get('mode')}")],
                rationale="CMYK, palette, or other non-RGB encodings can render differently after App Store processing.",
                remediation="Export as standard RGB JPEG or opaque RGB PNG.",
                verification=["Review the processed App Store Connect preview."],
                sources=["references/screenshot-review.md"],
            ))
        metrics = entry.get("metrics", {})
        if metrics.get("stddev", 99) < 2.0 and metrics.get("entropy", 99) < 1.0:
            findings.append(make_finding(
                id=f"SCREENSHOT-BLANK-{index:03d}",
                title="Screenshot appears blank or nearly uniform",
                severity="HIGH",
                category="screenshots",
                guideline="2.3.3 Accurate Screenshots; 2.1 App Completeness",
                confidence="HIGH",
                status="NEEDS_REVIEW",
                automation="visual-heuristic",
                evidence=[make_evidence(kind="screenshot", location=location, detail="Low-information image metrics", value=metrics)],
                rationale="A blank/loading/failed capture does not demonstrate app use and may reflect a broken runtime path.",
                remediation="Recapture after content is fully loaded and confirm the feature works on the release backend.",
                verification=["Visually review the original and reproduce the screen from a fresh install."],
                sources=["references/screenshot-review.md"],
            ))
        elif metrics.get("dominant_color_ratio", 0) > 0.82 and metrics.get("edge_mean", 99) < 10:
            findings.append(make_finding(
                id=f"SCREENSHOT-TITLE-CARD-RISK-{index:03d}",
                title="Screenshot may be a low-information title/marketing card",
                severity="LOW",
                category="screenshots",
                guideline="2.3.3 Accurate Screenshots",
                confidence="LOW",
                status="NEEDS_REVIEW",
                automation="visual-heuristic",
                evidence=[make_evidence(kind="screenshot", location=location, detail="High uniformity/low edge metrics", value=metrics)],
                rationale="Apple expects screenshots to show the app in use; a dominant flat card can be acceptable only when meaningful app UI remains visible and accurate.",
                remediation="Use the visual queue to verify that actual app functionality—not only branding or claims—is prominent.",
                verification=["Visually inspect the original at full resolution."],
                sources=["references/screenshot-review.md"],
            ))

    # Counts and coverage.
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    by_locale: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        if entry.get("error"):
            continue
        by_locale[entry["locale"]].append(entry)
        if entry.get("group"):
            grouped[(entry["locale"], entry["group"])].append(entry)

    for (locale, group), group_entries in sorted(grouped.items()):
        count = len(group_entries)
        if count > 10:
            findings.append(make_finding(
                id=f"SCREENSHOT-COUNT-{locale.upper()}-{group.upper().replace('.', '_')}",
                title="Screenshot group exceeds Apple's one-to-ten file limit",
                severity="BLOCKER",
                category="screenshots",
                guideline="Screenshot specifications",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="screenshot-group", location=f"{root}/{locale}/{group}", detail=f"{count} screenshots")],
                rationale="App Store Connect accepts at most 10 screenshots per device-size localization set.",
                remediation="Select the strongest 10 distinct, accurate screenshots.",
                verification=["Rerun the inspector and compare the set with App Store Connect."],
                sources=[APPLE_SCREENSHOT_SPEC_URL],
            ))
        orientations = sorted({item.get("orientation") for item in group_entries})
        if len(orientations) > 1:
            findings.append(make_finding(
                id=f"SCREENSHOT-MIXED-ORIENTATION-{locale.upper()}-{group.upper().replace('.', '_')}",
                title="Screenshot set mixes portrait and landscape orientation",
                severity="LOW",
                category="screenshots",
                guideline="Screenshot presentation quality",
                confidence="CERTAIN",
                status="NEEDS_REVIEW",
                automation="deterministic",
                evidence=[make_evidence(kind="screenshot-group", location=f"{locale}/{group}", detail="Orientations", value=orientations)],
                rationale="Mixed orientation may be valid, but the product-page sequence should remain intentional and visually coherent.",
                remediation="Review the App Store Connect preview and use a deliberate orientation sequence.",
                verification=["Inspect the processed product page on device."],
                sources=["references/screenshot-review.md"],
            ))

    primary_groups = {entry.get("group") for entry in by_locale.get(primary_locale, []) if entry.get("group")}
    for family in device_families:
        alternatives = REQUIRED_SCREENSHOT_COVERAGE.get(family)
        if not alternatives:
            continue
        satisfied = False
        if family == "iphone":
            # First alternative is preferred; second is official fallback.
            satisfied = any(alt.issubset(primary_groups) for alt in alternatives)
        else:
            satisfied = any(alt.issubset(primary_groups) for alt in alternatives)
        if not satisfied:
            findings.append(make_finding(
                id=f"SCREENSHOT-COVERAGE-{family.upper()}",
                title=f"Primary locale lacks required {family} screenshot coverage",
                severity="BLOCKER",
                category="screenshots",
                guideline="Screenshot specifications",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="screenshot-coverage", location=str(root), detail=f"primary_locale={primary_locale}; groups={sorted(x for x in primary_groups if x)}")],
                rationale="The product page needs a valid screenshot set for every supported required device family.",
                remediation=f"Provide one to 10 current screenshots in the accepted required {family} size group.",
                verification=["Rerun the inspector and upload the exact files to the matching App Store Connect slots."],
                sources=[APPLE_SCREENSHOT_SPEC_URL, "references/screenshot-review.md"],
            ))
        checks.append(make_check(
            f"screenshots.coverage.{family}",
            f"{family} screenshot coverage",
            "PASS" if satisfied else "ERROR",
            mandatory=True,
            tool="inspect_screenshots.py",
            detail=f"primary locale {primary_locale}; groups={sorted(x for x in primary_groups if x)}",
        ))

    for locale in declared_locales:
        if locale == primary_locale:
            continue
        if not by_locale.get(locale):
            findings.append(make_finding(
                id=f"SCREENSHOT-LOCALIZATION-{locale.upper()}",
                title="No localized screenshots were supplied for a declared locale",
                severity="LOW",
                category="localization",
                guideline="2.3 Accurate Metadata",
                confidence="CERTAIN",
                status="NEEDS_REVIEW",
                automation="deterministic",
                evidence=[make_evidence(kind="screenshot-coverage", location=str(root), detail=f"No screenshot folder/files inferred for {locale}")],
                rationale="App Store Connect can fall back to the primary screenshots, but the fallback must still be linguistically and commercially accurate for the locale.",
                remediation="Either add localized screenshots or explicitly review the primary fallback for language, currency, claims, and legal terms.",
                verification=["Preview the product page under the locale/storefront and execute the app in that language."],
                sources=["references/screenshot-review.md"],
            ))

    # Apple Watch requires one consistent size across all localizations.
    watch_sizes: dict[str, set[tuple[int, int]]] = defaultdict(set)
    for entry in entries:
        if entry.get("group") == "apple-watch" and not entry.get("error"):
            watch_sizes[entry["locale"]].add((entry["width"], entry["height"]))
    watch_union = {size for sizes in watch_sizes.values() for size in sizes}
    if len(watch_union) > 1:
        findings.append(make_finding(
            id="SCREENSHOT-WATCH-SIZE-CONSISTENCY",
            title="Apple Watch screenshot size is inconsistent across localizations",
            severity="BLOCKER",
            category="screenshots",
            guideline="Screenshot specifications",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="screenshot-coverage", location=str(root), detail="Watch sizes by locale", value={key: sorted(value) for key, value in watch_sizes.items()})],
            rationale="Apple requires the same Apple Watch screenshot size to be used consistently across all localizations for an app.",
            remediation="Select one accepted watch size and recapture/export every localization at that size.",
            verification=["Rerun the inspector and compare all watch slots in App Store Connect."],
            sources=[APPLE_SCREENSHOT_SPEC_URL],
        ))

    # Duplicates: exact and perceptual within a locale/group.
    exact_groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        if entry.get("sha256") and entry.get("group"):
            exact_groups[(entry["locale"], entry["group"], entry["sha256"])].append(entry)
    duplicate_sets = [values for values in exact_groups.values() if len(values) > 1]
    for dup_index, values in enumerate(duplicate_sets, start=1):
        findings.append(make_finding(
            id=f"SCREENSHOT-EXACT-DUPLICATE-{dup_index:03d}",
            title="Screenshot set contains exact duplicate files",
            severity="MEDIUM",
            category="screenshots",
            guideline="2.3.3 Accurate Screenshots",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="screenshot", location=str(root / item["relative_path"]), detail="Same SHA-256 as another screenshot") for item in values[:10]],
            rationale="Duplicate slots waste product-page coverage and can make the set appear incomplete or low-value.",
            remediation="Remove duplicates and use each slot to show a distinct accurate workflow/state.",
            verification=["Rerun duplicate detection and review the product-page sequence."],
            sources=["references/screenshot-review.md", "references/community-signals.md"],
        ))

    perceptual_pairs: list[dict[str, Any]] = []
    for key, group_entries in grouped.items():
        for left_index in range(len(group_entries)):
            left = group_entries[left_index]
            if not left.get("dhash"):
                continue
            for right in group_entries[left_index + 1:]:
                if left.get("sha256") == right.get("sha256") or not right.get("dhash"):
                    continue
                distance = _hamming_hex(left["dhash"], right["dhash"])
                if distance <= 3:
                    perceptual_pairs.append({
                        "locale": key[0], "group": key[1], "left": left["relative_path"], "right": right["relative_path"], "distance": distance,
                    })
                    if len(perceptual_pairs) >= 20:
                        break
            if len(perceptual_pairs) >= 20:
                break
        if len(perceptual_pairs) >= 20:
            break
    if perceptual_pairs:
        findings.append(make_finding(
            id="SCREENSHOT-NEAR-DUPLICATES",
            title="Screenshot set contains visually near-duplicate images",
            severity="LOW",
            category="screenshots",
            guideline="2.3.3 Accurate Screenshots",
            confidence="MEDIUM",
            status="NEEDS_REVIEW",
            automation="visual-heuristic",
            evidence=[make_evidence(kind="screenshot-pair", location=f"{pair['left']} ↔ {pair['right']}", detail=f"dHash distance={pair['distance']}") for pair in perceptual_pairs],
            rationale="Minor animation/cursor/text changes may be legitimate, but near-duplicates often indicate weak feature coverage.",
            remediation="Visually compare each pair and retain both only when each communicates materially different functionality.",
            verification=["Review the contact sheet and final product-page order."],
            sources=["references/screenshot-review.md"],
        ))

    # Generate contact sheets and visual queue.
    sheet_paths: list[str] = []
    if contact_sheets:
        sheet_root = Path(contact_sheets).resolve()
        sheet_root.mkdir(parents=True, exist_ok=True)
        for (locale, group), group_entries in sorted(grouped.items()):
            safe_group = group.replace(".", "_")
            output = sheet_root / f"{locale}--{safe_group}.png"
            _contact_sheet(group_entries, root, output, f"{locale} · {group} · {len(group_entries)} screenshots")
            sheet_paths.append(str(output))
        if entries:
            overview = sheet_root / "overview.png"
            _contact_sheet(entries, root, overview, f"All screenshots · {len(entries)} files")
            sheet_paths.append(str(overview))

    visual_queue = {
        "generated_at": now_iso(),
        "root": str(root),
        "instructions": "Inspect each original at full resolution. Contact sheets are navigation aids, not a substitute for original-image review. Do not mark PASS from deterministic metrics alone.",
        "checks": VISUAL_CHECKS,
        "items": [
            {
                "relative_path": entry["relative_path"],
                "locale": entry.get("locale"),
                "group": entry.get("group"),
                "dimensions": [entry.get("width"), entry.get("height")],
                "deterministic_flags": [
                    finding["id"] for finding in findings
                    if any(str(root / entry["relative_path"]) == evidence.get("location") for evidence in finding.get("evidence", []))
                ],
                "manual_status": "NOT_REVIEWED",
                "manual_notes": "",
            }
            for entry in entries if not entry.get("error")
        ],
        "contact_sheets": sheet_paths,
    }
    queue_path = None
    if contact_sheets:
        queue_path = str(Path(contact_sheets).resolve() / "visual-review-queue.json")
        dump_json(visual_queue, queue_path)

    checks.append(make_check(
        "screenshots.visual_review",
        "Full-resolution visual screenshot review",
        "NEEDS_REVIEW" if entries else "SKIPPED",
        mandatory=True,
        tool="agent vision/manual",
        detail=f"{len(entries)} screenshot(s); queue={queue_path or 'embedded only'}",
    ))
    checks.append(make_check(
        "screenshots.deterministic",
        "Deterministic screenshot validation",
        "PASS" if entries else "ERROR",
        mandatory=True,
        tool="Pillow",
        detail="Format, dimensions, alpha, counts, coverage, duplicates, and image metrics checked",
    ))

    facts = {
        "root": str(root),
        "primary_locale": primary_locale,
        "declared_locales": declared_locales,
        "device_families": device_families,
        "entries": entries,
        "group_counts": {f"{locale}/{group}": len(values) for (locale, group), values in sorted(grouped.items())},
        "contact_sheets": sheet_paths,
        "visual_queue_path": queue_path,
        "unsupported_files": unsupported_files,
    }
    return {
        "module": "inspect_screenshots",
        "generated_at": now_iso(),
        "screenshots": str(root),
        "facts": facts,
        "checks": checks,
        "findings": findings,
        "visual_review_queue": visual_queue,
        "tool": {"name": "inspect_screenshots.py", "status": "OK", "detail": "Local Pillow inspection; no OCR or upload"},
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate App Store screenshots and create contact sheets/visual review queues.")
    parser.add_argument("--screenshots", required=True, help="Screenshot root directory")
    parser.add_argument("--config", help="Optional review-input.json")
    parser.add_argument("--output", help="Write structured JSON result")
    parser.add_argument("--contact-sheets", help="Generate contact sheets and visual-review-queue.json in this directory")
    parser.add_argument("--strict", action="store_true", help="Exit 2 for open blocker/high findings")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config = load_json(args.config) if args.config else None
        if config is not None and not isinstance(config, dict):
            raise ReviewInputError("Config root must be an object")
        result = inspect_screenshots(
            args.screenshots,
            config=config,
            config_path=args.config,
            contact_sheets=args.contact_sheets,
        )
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"inspect_screenshots: {exc}\n")
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
