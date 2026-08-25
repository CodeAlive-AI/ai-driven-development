#!/usr/bin/env python3
"""Check whether the skill's pinned Apple policy baseline is still current.

Network access is opt-in. Without ``--network``, the script records that policy
freshness was not checked and intentionally prevents a READY gate.
"""

from __future__ import annotations

import argparse
import html
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from common import (
    GUIDELINES_LAST_UPDATED,
    POLICY_BASELINE,
    ReviewInputError,
    dump_json,
    load_json,
    make_check,
    make_evidence,
    make_finding,
    now_iso,
    print_json,
)

DEFAULT_CATALOG = Path(__file__).resolve().parents[1] / "references" / "source-catalog.json"
MAX_BODY = 2 * 1024 * 1024
ALLOWED_HOSTS = {"developer.apple.com", "agentskills.io"}


def _strip_html(raw: str) -> str:
    raw = re.sub(r"(?is)<script\b[^>]*>.*?</script>", " ", raw)
    raw = re.sub(r"(?is)<style\b[^>]*>.*?</style>", " ", raw)
    raw = re.sub(r"(?is)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()


def _safe_url(url: str) -> tuple[bool, str]:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https":
        return False, "Only HTTPS sources are permitted"
    if parsed.username or parsed.password:
        return False, "Credentials in source URLs are forbidden"
    host = (parsed.hostname or "").lower().rstrip(".")
    if host not in ALLOWED_HOSTS:
        return False, f"Host not allow-listed: {host or '<missing>'}"
    if parsed.port not in (None, 443):
        return False, "Non-standard ports are forbidden"
    return True, "ok"


def _fetch(url: str, timeout: float) -> tuple[str | None, dict[str, Any]]:
    allowed, reason = _safe_url(url)
    if not allowed:
        return None, {"status": "ERROR", "detail": reason}
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "apple-app-store-reviewer/1.0 policy-freshness",
            "Accept": "text/html,application/xhtml+xml,text/plain;q=0.8",
        },
        method="GET",
    )
    context = ssl.create_default_context()
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
            final_url = response.geturl()
            allowed_final, final_reason = _safe_url(final_url)
            if not allowed_final:
                return None, {"status": "ERROR", "detail": f"Unsafe redirect: {final_reason}"}
            length = response.headers.get("Content-Length")
            if length and int(length) > MAX_BODY:
                return None, {"status": "ERROR", "detail": f"Response exceeds {MAX_BODY} bytes"}
            body = response.read(MAX_BODY + 1)
            if len(body) > MAX_BODY:
                return None, {"status": "ERROR", "detail": f"Response exceeds {MAX_BODY} bytes"}
            charset = response.headers.get_content_charset() or "utf-8"
            return _strip_html(body.decode(charset, errors="replace")), {
                "status": "PASS",
                "detail": f"HTTP {getattr(response, 'status', 200)}",
                "final_url": final_url,
                "bytes": len(body),
            }
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, ValueError) as exc:
        return None, {"status": "ERROR", "detail": f"Fetch failed: {type(exc).__name__}: {exc}"}


def _parse_date(value: str) -> datetime | None:
    for fmt in ("%Y-%m-%d", "%B %d, %Y", "%b %d, %Y"):
        try:
            return datetime.strptime(value.strip(), fmt)
        except ValueError:
            pass
    return None


def check_policy_freshness(
    catalog: Mapping[str, Any],
    *,
    catalog_path: str | Path,
    network: bool = False,
    timeout: float = 10.0,
) -> dict[str, Any]:
    catalog_path = Path(catalog_path).resolve()
    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    sources: list[dict[str, Any]] = []
    observed_guideline_date: str | None = None

    if str(catalog.get("baseline_date")) != POLICY_BASELINE:
        findings.append(
            make_finding(
                id="POLICY-CATALOG-BASELINE-MISMATCH",
                title="Source catalog baseline does not match the skill",
                severity="BLOCKER",
                category="policy-freshness",
                guideline="Policy baseline",
                evidence=[make_evidence(kind="file", location=str(catalog_path), detail="baseline_date differs", value=catalog.get("baseline_date"))],
                rationale="The executable checks and policy reference set are not pinned to the same review date.",
                remediation=f"Set the catalog baseline to {POLICY_BASELINE} only after reconciling all policy changes.",
                verification=["Rerun check_policy_freshness.py."],
                sources=[],
                confidence="CERTAIN",
            )
        )

    if not network:
        checks.append(
            make_check(
                "policy.freshness",
                "Current official Apple policy fingerprint",
                "SKIPPED",
                mandatory=True,
                tool="check_policy_freshness.py",
                detail="Network access was not enabled; pinned policy may have changed.",
            )
        )
        return {
            "schema_version": "1.0",
            "generated_at": now_iso(),
            "policy": {
                "baseline_date": POLICY_BASELINE,
                "guidelines_last_updated": GUIDELINES_LAST_UPDATED,
                "freshness": "NOT_CHECKED",
                "observed_guidelines_last_updated": None,
            },
            "sources": sources,
            "checks": checks,
            "findings": findings,
            "facts": {"network_enabled": False, "catalog": str(catalog_path)},
        }

    required_failures = 0
    policy_newer = False
    for source in catalog.get("official_sources", []):
        if not isinstance(source, Mapping):
            continue
        source_id = str(source.get("id", "unknown"))
        url = str(source.get("url", ""))
        text, fetch = _fetch(url, timeout)
        record: dict[str, Any] = {
            "id": source_id,
            "url": url,
            "required": bool(source.get("required")),
            **fetch,
            "markers": {},
        }
        if text is None:
            sources.append(record)
            if source.get("required"):
                required_failures += 1
                findings.append(
                    make_finding(
                        id=f"POLICY-FETCH-{re.sub(r'[^A-Z0-9]+', '-', source_id.upper()).strip('-')}",
                        title=f"Could not verify required policy source: {source.get('title', source_id)}",
                        severity="HIGH",
                        category="policy-freshness",
                        guideline="Policy baseline",
                        evidence=[make_evidence(kind="network", location=url, detail=fetch.get("detail", "Fetch failed"))],
                        rationale="A required current Apple source could not be fingerprinted, so the pinned baseline cannot be trusted for release gating.",
                        remediation="Restore controlled network access or manually inspect the current official page and update the source catalog.",
                        verification=[f"Fetch {url} successfully and rerun the freshness check."],
                        sources=[url],
                        confidence="CERTAIN",
                        automation="deterministic-network",
                    )
                )
            continue

        folded = text.casefold()
        missing_all = [marker for marker in source.get("markers_all", []) if str(marker).casefold() not in folded]
        any_markers = [str(marker) for marker in source.get("markers_any", [])]
        any_ok = not any_markers or any(marker.casefold() in folded for marker in any_markers)
        record["markers"] = {
            "missing_all": missing_all,
            "any_ok": any_ok,
            "expected_any": any_markers,
        }
        if missing_all or not any_ok:
            severity = "HIGH" if source.get("required") else "MEDIUM"
            if source.get("required"):
                required_failures += 1
            findings.append(
                make_finding(
                    id=f"POLICY-FINGERPRINT-{re.sub(r'[^A-Z0-9]+', '-', source_id.upper()).strip('-')}",
                    title=f"Policy page fingerprint changed: {source.get('title', source_id)}",
                    severity=severity,
                    category="policy-freshness",
                    guideline="Policy baseline",
                    evidence=[make_evidence(kind="network", location=url, detail="Expected page markers were absent", value=record["markers"])],
                    rationale="The official page content no longer matches the pinned catalog. This may be a policy change, content redesign, localization, or fetch anomaly.",
                    remediation="Open the official page, compare it with the pinned rules, update catalogs/tests/references, and record the change date.",
                    verification=["All expected markers are present or the catalog is deliberately repinned after policy review."],
                    sources=[url],
                    confidence="HIGH",
                    automation="deterministic-network",
                )
            )

        date_regex = source.get("date_regex")
        if date_regex:
            match = re.search(str(date_regex), text, flags=re.IGNORECASE)
            if match:
                observed_guideline_date = match.group(1)
                record["observed_date"] = observed_guideline_date
                expected = _parse_date(str(source.get("expected_date", GUIDELINES_LAST_UPDATED)))
                observed = _parse_date(observed_guideline_date)
                if expected and observed and observed > expected:
                    policy_newer = True
                    findings.append(
                        make_finding(
                            id="POLICY-GUIDELINES-NEWER-THAN-PIN",
                            title="Apple App Review Guidelines are newer than this skill's baseline",
                            severity="BLOCKER",
                            category="policy-freshness",
                            guideline="Policy baseline",
                            evidence=[make_evidence(kind="network", location=url, detail="Observed a newer Last Updated date", value=observed_guideline_date)],
                            rationale="A review based on an older guideline version can miss new requirements or apply superseded ones.",
                            remediation="Diff the current guidelines against the pinned baseline, update the skill, catalogs, tests, and references, then repin the date.",
                            verification=["The pinned date equals the current official Last Updated date and all policy changes are covered."],
                            sources=[url],
                            confidence="CERTAIN",
                            automation="deterministic-network",
                        )
                    )
            else:
                record["observed_date"] = None
                findings.append(
                    make_finding(
                        id="POLICY-GUIDELINES-DATE-NOT-PARSED",
                        title="Could not parse the App Review Guidelines update date",
                        severity="HIGH",
                        category="policy-freshness",
                        guideline="Policy baseline",
                        evidence=[make_evidence(kind="network", location=url, detail="The configured date expression did not match")],
                        rationale="The skill cannot prove that its policy baseline is current.",
                        remediation="Inspect the current page and update the date parser or source catalog.",
                        verification=["The checker extracts the current Last Updated date."],
                        sources=[url],
                        confidence="HIGH",
                        automation="deterministic-network",
                    )
                )
                required_failures += 1
        sources.append(record)

    if policy_newer:
        freshness = "STALE"
        status = "ERROR"
        detail = "A newer App Review Guidelines date was observed."
    elif required_failures:
        freshness = "UNVERIFIED"
        status = "NEEDS_REVIEW"
        detail = f"{required_failures} required policy source(s) could not be verified."
    else:
        freshness = "CURRENT"
        status = "PASS"
        detail = "All required official page fingerprints matched the pinned baseline."

    checks.append(
        make_check(
            "policy.freshness",
            "Current official Apple policy fingerprint",
            status,
            mandatory=True,
            tool="check_policy_freshness.py",
            detail=detail,
            evidence=[make_evidence(kind="file", location=str(catalog_path), detail="Pinned source catalog")],
        )
    )
    return {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "policy": {
            "baseline_date": POLICY_BASELINE,
            "guidelines_last_updated": GUIDELINES_LAST_UPDATED,
            "freshness": freshness,
            "observed_guidelines_last_updated": observed_guideline_date,
        },
        "sources": sources,
        "checks": checks,
        "findings": findings,
        "facts": {
            "network_enabled": True,
            "catalog": str(catalog_path),
            "required_failures": required_failures,
        },
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fingerprint current official Apple policy pages against the pinned skill baseline.")
    parser.add_argument("--catalog", default=str(DEFAULT_CATALOG), help="Path to references/source-catalog.json.")
    parser.add_argument("--network", action="store_true", help="Explicitly allow HTTPS fetches to allow-listed official hosts.")
    parser.add_argument("--timeout", type=float, default=10.0, help="Per-source timeout in seconds (default: 10).")
    parser.add_argument("--output", help="Write structured JSON to this file instead of stdout.")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero unless freshness is CURRENT.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        catalog = load_json(args.catalog)
        if not isinstance(catalog, Mapping):
            raise ReviewInputError("Source catalog root must be a JSON object")
        result = check_policy_freshness(catalog, catalog_path=args.catalog, network=args.network, timeout=args.timeout)
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"check_policy_freshness: {exc}\n")
        return 3
    if args.output:
        dump_json(result, args.output)
    else:
        print_json(result)
    freshness = result.get("policy", {}).get("freshness")
    if freshness == "STALE":
        return 2
    if args.strict and freshness != "CURRENT":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
