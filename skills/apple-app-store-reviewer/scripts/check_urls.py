#!/usr/bin/env python3
"""Validate metadata URLs and optionally probe their public content."""

from __future__ import annotations

import argparse
import ipaddress
import re
import socket
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import urlparse

from common import ReviewInputError, dump_json, load_json, make_check, make_evidence, make_finding, now_iso

MAX_BODY_BYTES = 256 * 1024
PRIVACY_TERMS = ("privacy", "data", "collect", "retention", "delete", "consent")
SUPPORT_TERMS = ("support", "contact", "help", "email", "mailto:")
TERMS_TERMS = ("terms", "agreement", "eula", "subscription", "cancel")
HTML_TAG_RE = re.compile(r"<[^>]+>")


def _extract_urls(metadata: Mapping[str, Any], metadata_path: Path) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    locales = metadata.get("locales", {})
    if not isinstance(locales, dict):
        return output
    for locale, raw in sorted(locales.items()):
        if not isinstance(raw, dict):
            continue
        for field in ("privacy_policy_url", "support_url", "marketing_url", "terms_url"):
            value = raw.get(field)
            if isinstance(value, str) and value.strip():
                output.append({
                    "locale": str(locale),
                    "field": field,
                    "url": value.strip(),
                    "location": f"{metadata_path}#/locales/{locale}/{field}",
                })
    return output


def _validate_public_https(url: str) -> tuple[bool, str]:
    parsed = urlparse(url)
    if parsed.scheme.lower() != "https":
        return False, "URL must use HTTPS"
    if not parsed.hostname:
        return False, "URL has no hostname"
    if parsed.username or parsed.password:
        return False, "URL must not contain embedded credentials"
    if parsed.fragment:
        # A fragment is legal, but privacy/support root URLs should normally be stable.
        return True, "URL is syntactically valid; contains a fragment"
    return True, "URL is syntactically valid"


def _resolve_is_public(host: str) -> tuple[bool, str]:
    try:
        addresses = {item[4][0] for item in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)}
    except OSError as exc:
        return False, f"DNS resolution failed: {exc}"
    if not addresses:
        return False, "DNS returned no addresses"
    for address in addresses:
        try:
            ip = ipaddress.ip_address(address)
        except ValueError:
            continue
        if not ip.is_global:
            return False, f"Hostname resolves to non-public address {address}"
    return True, ", ".join(sorted(addresses))


def _fetch(url: str, timeout: float) -> dict[str, Any]:
    parsed = urlparse(url)
    public, dns_detail = _resolve_is_public(parsed.hostname or "")
    if not public:
        return {"ok": False, "error": dns_detail, "dns": dns_detail}
    headers = {
        "User-Agent": "Apple-App-Store-Reviewer-Skill/1.0 (+local preflight)",
        "Accept": "text/html,application/xhtml+xml,text/plain;q=0.9,*/*;q=0.1",
    }
    context = ssl.create_default_context()
    result: dict[str, Any] = {"dns": dns_detail}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
                result.update({
                    "ok": 200 <= response.status < 400,
                    "status": response.status,
                    "final_url": response.geturl(),
                    "content_type": response.headers.get("Content-Type", ""),
                    "method": method,
                })
                if method == "GET":
                    body = response.read(MAX_BODY_BYTES + 1)
                    result["truncated"] = len(body) > MAX_BODY_BYTES
                    body = body[:MAX_BODY_BYTES]
                    charset = response.headers.get_content_charset() or "utf-8"
                    try:
                        result["body"] = body.decode(charset, errors="replace")
                    except LookupError:
                        result["body"] = body.decode("utf-8", errors="replace")
                if method == "HEAD" and response.status not in {403, 405}:
                    # We still need body content for privacy/support verification.
                    continue
                if method == "GET":
                    return result
        except urllib.error.HTTPError as exc:
            result.update({"ok": False, "status": exc.code, "final_url": exc.geturl(), "error": str(exc), "method": method})
            if method == "HEAD" and exc.code in {403, 405}:
                continue
            if method == "GET":
                return result
        except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError) as exc:
            result.update({"ok": False, "error": str(exc), "method": method})
            if method == "GET":
                return result
    return result


def check_urls(metadata: Mapping[str, Any], metadata_path: str | Path, *, network: bool = False, timeout: float = 8.0) -> dict[str, Any]:
    metadata_path = Path(metadata_path).resolve()
    urls = _extract_urls(metadata, metadata_path)
    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    facts: dict[str, Any] = {"network_enabled": bool(network), "urls": []}

    required_fields = {"privacy_policy_url", "support_url"}
    for index, item in enumerate(urls, start=1):
        valid, detail = _validate_public_https(item["url"])
        record: dict[str, Any] = {**item, "syntax_ok": valid, "syntax_detail": detail}
        facts["urls"].append(record)
        if not valid:
            findings.append(make_finding(
                id=f"URL-SYNTAX-{index:03d}",
                title=f"{item['field'].replace('_', ' ').title()} is not a valid public HTTPS URL",
                severity="BLOCKER" if item["field"] in required_fields else "HIGH",
                category="metadata-urls",
                guideline="2.1 App Completeness; 5.1.1 Privacy Policies",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="metadata-url", location=item["location"], detail=detail, value=item["url"])],
                rationale="Reviewers and customers must be able to access stable production privacy/support information.",
                remediation="Use an absolute public HTTPS URL without embedded credentials.",
                verification=["Rerun check_urls.py --network and open the URL from a clean browser session."],
                sources=["references/privacy-security.md"],
            ))
            continue
        if not network:
            continue
        probe = _fetch(item["url"], timeout)
        record["probe"] = {key: value for key, value in probe.items() if key != "body"}
        if not probe.get("ok"):
            findings.append(make_finding(
                id=f"URL-UNREACHABLE-{index:03d}",
                title=f"{item['field'].replace('_', ' ').title()} is not publicly reachable",
                severity="BLOCKER" if item["field"] in required_fields else "HIGH",
                category="metadata-urls",
                guideline="2.1 App Completeness; 5.1.1 Privacy Policies",
                confidence="HIGH",
                evidence=[make_evidence(kind="network", location=item["url"], detail=str(probe.get("error") or probe.get("status") or "request failed"))],
                rationale="A broken, private, blocked, or authentication-gated URL prevents review and customer access.",
                remediation="Publish the page without login, geo/IP restriction, bot challenge, or broken redirect and keep it live during review.",
                verification=["Open the URL from an unauthenticated external connection and rerun the network check."],
                sources=["references/privacy-security.md", "references/community-signals.md"],
            ))
            continue
        final_url = str(probe.get("final_url") or item["url"])
        final_valid, final_detail = _validate_public_https(final_url)
        if not final_valid:
            findings.append(make_finding(
                id=f"URL-INSECURE-REDIRECT-{index:03d}",
                title="Metadata URL redirects to an invalid or non-HTTPS destination",
                severity="BLOCKER" if item["field"] in required_fields else "HIGH",
                category="metadata-urls",
                guideline="5.1 Privacy",
                confidence="CERTAIN",
                evidence=[make_evidence(kind="network", location=item["url"], detail=f"Final URL {final_url}: {final_detail}")],
                rationale="The visible HTTPS URL does not protect or reliably expose the final page.",
                remediation="Keep the entire redirect chain on public HTTPS endpoints.",
                verification=["Inspect the redirect chain from an external client."],
                sources=["references/privacy-security.md"],
            ))
        content_type = str(probe.get("content_type") or "").casefold()
        body = str(probe.get("body") or "")
        plain = HTML_TAG_RE.sub(" ", body).casefold()
        expected_terms: tuple[str, ...]
        if item["field"] == "privacy_policy_url":
            expected_terms = PRIVACY_TERMS
        elif item["field"] == "support_url":
            expected_terms = SUPPORT_TERMS
        elif item["field"] == "terms_url":
            expected_terms = TERMS_TERMS
        else:
            expected_terms = ()
        hits = [term for term in expected_terms if term in plain or term in body.casefold()]
        record["content_term_hits"] = hits
        if expected_terms and len(hits) < 2:
            findings.append(make_finding(
                id=f"URL-CONTENT-{index:03d}",
                title=f"{item['field'].replace('_', ' ').title()} content could not be verified",
                severity="HIGH" if item["field"] == "privacy_policy_url" else "MEDIUM",
                category="metadata-urls",
                guideline="2.1 App Completeness; 5.1.1 Privacy Policies",
                confidence="MEDIUM",
                status="NEEDS_REVIEW",
                automation="content-heuristic",
                evidence=[make_evidence(kind="network", location=final_url, detail=f"content-type={content_type}; expected term hits={hits}; body_truncated={probe.get('truncated', False)}")],
                rationale="The endpoint responded, but it may be a generic homepage, JavaScript shell, error/interstitial, or page lacking the promised privacy/support/terms content.",
                remediation="Manually open and review the rendered page; ensure the required information is visible without authentication or client-specific scripts.",
                verification=["Review the page in a browser and compare it with the app's actual data/payment/support behavior."],
                sources=["references/privacy-security.md", "references/reviewer-notes-and-appeals.md"],
            ))

    # Required URLs may be missing from metadata entirely.
    for locale, raw in sorted((metadata.get("locales") or {}).items() if isinstance(metadata.get("locales"), dict) else []):
        if not isinstance(raw, dict):
            continue
        for field in required_fields:
            if not str(raw.get(field) or "").strip():
                findings.append(make_finding(
                    id=f"URL-MISSING-{str(locale).upper()}-{field.upper().replace('_', '-')}",
                    title=f"Required {field.replace('_', ' ')} is missing",
                    severity="BLOCKER",
                    category="metadata-urls",
                    guideline="2.1 App Completeness; 5.1.1 Privacy Policies",
                    confidence="CERTAIN",
                    evidence=[make_evidence(kind="metadata-url", location=f"{metadata_path}#/locales/{locale}/{field}", detail="Missing or empty")],
                    rationale="The product page lacks a required/reviewer-critical destination.",
                    remediation=f"Provide a public production {field.replace('_', ' ')} HTTPS URL.",
                    verification=["Run this checker with network access and open the page externally."],
                    sources=["references/privacy-security.md"],
                ))

    syntax_failed = any(f["id"].startswith("URL-SYNTAX") or f["id"].startswith("URL-MISSING") for f in findings)
    network_failed = any(f["id"].startswith(("URL-UNREACHABLE", "URL-INSECURE")) for f in findings)
    checks.append(make_check("urls.syntax", "Metadata URL syntax", "ERROR" if syntax_failed else "PASS", mandatory=True, tool="urllib.parse", detail=f"{len(urls)} URL(s)"))
    checks.append(make_check(
        "urls.network",
        "Public URL reachability/content",
        ("ERROR" if network_failed else "PASS") if network else "SKIPPED",
        mandatory=True,
        tool="urllib.request",
        detail="Network explicitly enabled" if network else "Network disabled; pass --network to verify public availability",
    ))

    return {
        "module": "check_urls",
        "generated_at": now_iso(),
        "metadata_path": str(metadata_path),
        "facts": facts,
        "checks": checks,
        "findings": findings,
        "tool": {"name": "check_urls.py", "status": "OK", "detail": f"network={network}; max_body_bytes={MAX_BODY_BYTES}; timeout={timeout}"},
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate and optionally probe public App Store metadata URLs.")
    parser.add_argument("--metadata", required=True, help="Metadata JSON")
    parser.add_argument("--network", action="store_true", help="Explicitly enable public DNS/HTTPS requests")
    parser.add_argument("--timeout", type=float, default=8.0, help="Per-request timeout seconds")
    parser.add_argument("--output", help="Write structured JSON result")
    parser.add_argument("--strict", action="store_true", help="Exit 2 for blocker/high findings or skipped network verification")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        metadata = load_json(args.metadata)
        if not isinstance(metadata, dict):
            raise ReviewInputError("Metadata root must be an object")
        result = check_urls(metadata, args.metadata, network=args.network, timeout=args.timeout)
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"check_urls: {exc}\n")
        return 3
    if args.output:
        dump_json(result, args.output)
    else:
        sys.stdout.write(dump_json(result))
    if args.strict:
        severe = any(f.get("severity") in {"BLOCKER", "HIGH"} and f.get("status") in {"OPEN", "NEEDS_REVIEW", "ERROR"} for f in result["findings"])
        skipped = any(c.get("mandatory") and c.get("status") == "SKIPPED" for c in result["checks"])
        if severe or skipped:
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
