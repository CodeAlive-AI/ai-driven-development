#!/usr/bin/env python3
"""Minimal reality check for ranked OpenRouter endpoints.

Ranking is a hypothesis built from catalogue fields; several of those fields
are wrong often enough to change the answer (references/storefront-traps.md).
This sends a small number of real requests to each candidate and reports what
they actually do, then judges them against the constraints that were asked for.

It is deliberately small: a handful of requests per endpoint, no warm-up games,
no statistics beyond a median. It answers "is this endpoint disqualified", not
"what is its exact throughput".

Standard library only. The key is read from OPENROUTER_API_KEY and never
printed, logged or written to the output.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
import urllib.error
import urllib.request

ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"


# Rough characters-per-token for the filler below. Latin script runs near 4;
# Cyrillic, CJK and code all run lower, so a filler-sized prompt is only ever
# approximately the size asked for. That is fine for a rough cut and not fine
# for a decision — use --prompt-file, which needs no estimate at all.
FILLER_CHARS_PER_TOKEN = 4.0


def build_prompt(prompt_tokens: int) -> str:
    """Filler sized to roughly the caller's profile.

    Sized deliberately: TTFT measured on a short prompt is 4-6x optimistic
    against a real one, so the probe has to be about the size of the real
    thing. Wording does not matter here; size does. When it does matter — and
    it does for contract compliance, which is content-dependent — pass
    --prompt-file instead.
    """
    sentence = (
        "The clause states a requirement for the object and the conditions "
        "under which it applies. "
    )
    target = max(1, int(prompt_tokens * FILLER_CHARS_PER_TOKEN / len(sentence)))
    return sentence * target


def one_call(
    api_key: str,
    model: str,
    provider: str,
    prompt: str,
    max_tokens: int,
    reasoning_effort: str | None,
    timeout: float,
) -> dict:
    body: dict = {
        "model": model,
        "stream": True,
        "max_tokens": max_tokens,
        "usage": {"include": True},
        "messages": [{"role": "user", "content": prompt}],
        "provider": {"only": [provider], "allow_fallbacks": False},
    }
    if reasoning_effort:
        body["reasoning"] = {"effort": reasoning_effort}
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    started = time.monotonic()
    ttft: float | None = None
    usage: dict | None = None
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            for raw in response:
                line = raw.decode("utf-8", "replace").strip()
                if not line.startswith("data: "):
                    continue
                chunk = line[6:]
                if chunk == "[DONE]":
                    break
                try:
                    event = json.loads(chunk)
                except json.JSONDecodeError:
                    continue
                if event.get("usage"):
                    usage = event["usage"]
                delta = (event.get("choices") or [{}])[0].get("delta") or {}
                if ttft is None and delta.get("content"):
                    ttft = time.monotonic() - started
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace")[:200]
        return {"error": f"HTTP {error.code}", "detail": detail}
    except Exception as error:  # noqa: BLE001 - transport failures are data here
        return {"error": type(error).__name__, "detail": str(error)[:200]}
    return {"total": time.monotonic() - started, "ttft": ttft, "usage": usage}


def summarise(calls: list[dict], max_tokens: int) -> dict:
    ok = [c for c in calls if "error" not in c and c.get("usage")]
    errors = [c for c in calls if "error" in c]
    if not ok:
        classes = sorted({c["error"] for c in errors})
        return {
            "calls": len(calls),
            "error_classes": classes,
            "error_rate": 1.0,
            "verdict": "no successful call",
        }
    last = ok[-1]["usage"]
    completion = int(last.get("completion_tokens") or 0)
    prompt_tokens = int(last.get("prompt_tokens") or 0)
    cached = int((last.get("prompt_tokens_details") or {}).get("cached_tokens") or 0)
    ttfts = [c["ttft"] for c in ok if c["ttft"] is not None]
    gens = [c["total"] - (c["ttft"] or 0) for c in ok]
    generation = statistics.median(gens) if gens else 0.0
    return {
        "calls": len(calls),
        "cache_hit_rate": round(cached / prompt_tokens, 4) if prompt_tokens else 0.0,
        "cached_tokens": cached,
        "completion_tokens": completion,
        "cost_usd": round(statistics.median([c["usage"].get("cost", 0) for c in ok]), 6),
        "error_classes": sorted({c["error"] for c in errors}),
        "error_rate": round(len(errors) / len(calls), 4),
        "prompt_tokens": prompt_tokens,
        "respects_max_tokens": completion <= max_tokens,
        "total_s": round(statistics.median([c["total"] for c in ok]), 2),
        "tps": round(completion / generation, 1) if generation else 0.0,
        "ttft_s": round(statistics.median(ttfts), 2) if ttfts else None,
    }


def cache_verdict(hit_rate: float, synthetic_prompt: bool) -> tuple[str, bool]:
    """Whether a cache reading means anything.

    A hit proves caching. A miss does not disprove it: a prefix nobody has sent
    before does not become readable within a handful of consecutive requests.
    Measured — the same endpoint returned 99 % on two calls with a prompt used
    all day, and 0 % on four calls with a fresh one. So a zero is a conclusion
    only when the prompt is one the system actually reuses.
    """
    if hit_rate >= 0.5:
        return "hits", True
    if synthetic_prompt:
        return "no hit on a fresh prefix — inconclusive", False
    return "no hit on your own prompt", True


def judge(row: dict, limits: argparse.Namespace) -> list[str]:
    """Why this endpoint is disqualified, in the caller's own terms."""
    failures: list[str] = []
    if row.get("verdict") == "no successful call":
        return [f"no successful call ({', '.join(row['error_classes'])})"]
    if limits.max_error_rate is not None and row["error_rate"] > limits.max_error_rate:
        failures.append(
            f"error rate {row['error_rate']:.0%} > {limits.max_error_rate:.0%}"
            f" ({', '.join(row['error_classes'])})"
        )
    if limits.min_tps is not None and row["tps"] < limits.min_tps:
        failures.append(f"tps {row['tps']} < {limits.min_tps}")
    if limits.max_ttft is not None:
        # `None` means no content delta was seen — a reasoning-only stream, or a
        # shape this probe does not parse. Passing a latency constraint on an
        # unmeasured value is worse than having no constraint, so it fails.
        if row["ttft_s"] is None:
            failures.append("TTFT not observed (no content delta in the stream)")
        elif row["ttft_s"] > limits.max_ttft:
            failures.append(f"TTFT {row['ttft_s']}s > {limits.max_ttft}s")
    if limits.require_cache and row["cache_hit_rate"] < 0.5:
        # Only ever a failure on a prompt the system genuinely reuses. On a
        # fresh prefix a zero is inconclusive — see `cache_verdict` and
        # references/storefront-traps.md.
        if row["cache_conclusive"]:
            failures.append(
                f"cache hit {row['cache_hit_rate']:.0%} on a prompt that is reused"
            )
    if limits.require_max_tokens and not row["respects_max_tokens"]:
        failures.append(
            f"returned {row['completion_tokens']} completion tokens against"
            f" max_tokens={limits.max_tokens}"
        )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument(
        "--providers", required=True, help="comma-separated provider tags to probe"
    )
    parser.add_argument("--prompt-file", help="real prompt; preferred over --prompt-tokens")
    parser.add_argument("--prompt-tokens", type=int, default=8000)
    parser.add_argument("--max-tokens", type=int, default=600)
    parser.add_argument("--reasoning-effort", default=None)
    parser.add_argument(
        "--runs",
        type=int,
        default=3,
        help="identical calls per endpoint; >=2 is what exposes implicit caching",
    )
    parser.add_argument("--timeout", type=float, default=180.0)
    parser.add_argument("--min-tps", type=float, default=None)
    parser.add_argument("--max-ttft", type=float, default=None)
    parser.add_argument("--max-error-rate", type=float, default=None)
    parser.add_argument(
        "--require-cache",
        action="store_true",
        help=(
            "fail an endpoint that does not serve the prefix from cache. Only "
            "meaningful with --prompt-file: a fresh synthetic prefix does not "
            "become cacheable within a short probe, so a zero there is "
            "reported as inconclusive rather than as a failure."
        ),
    )
    parser.add_argument("--require-max-tokens", action="store_true")
    parser.add_argument("--output", help="write the rows as JSON here")
    args = parser.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("OPENROUTER_API_KEY is not set", file=sys.stderr)
        return 2

    prompt = (
        open(args.prompt_file, encoding="utf-8").read()
        if args.prompt_file
        else build_prompt(args.prompt_tokens)
    )
    providers = [p.strip() for p in args.providers.split(",") if p.strip()]
    if args.require_cache and args.prompt_file is None:
        print(
            "note: --require-cache with a synthetic prompt cannot fail an "
            "endpoint; a fresh prefix is not cacheable within a short probe. "
            "Pass --prompt-file with a prompt your system reuses.",
            file=sys.stderr,
        )

    rows: dict[str, dict] = {}
    for provider in providers:
        calls = [
            one_call(
                api_key,
                args.model,
                provider,
                prompt,
                args.max_tokens,
                args.reasoning_effort,
                args.timeout,
            )
            for _ in range(args.runs)
        ]
        row = summarise(calls, args.max_tokens)
        note, conclusive = cache_verdict(
            row.get("cache_hit_rate", 0.0), args.prompt_file is None
        )
        row["cache_note"] = note
        row["cache_conclusive"] = conclusive
        row["failures"] = judge(row, args)
        rows[provider] = row
        print(
            f"{provider:22s} "
            + (
                "  ".join(
                    [
                        f"ttft {row.get('ttft_s')}s"
                        if row.get("ttft_s") is not None
                        else "ttft n/a",
                        f"tps {row.get('tps')}",
                        f"${row.get('cost_usd')}",
                        f"cache {row.get('cache_hit_rate', 0):.0%}"
                        + ("" if row["cache_conclusive"] else "?"),
                        f"out {row.get('completion_tokens')}",
                        f"err {row.get('error_rate', 1):.0%}",
                    ]
                )
                if row.get("verdict") != "no successful call"
                else f"NO SUCCESSFUL CALL: {', '.join(row['error_classes'])}"
            )
            + ("  ✗ " + "; ".join(row["failures"]) if row["failures"] else "  ✓"),
            flush=True,
        )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            json.dump(rows, handle, ensure_ascii=False, indent=1)

    passing = [p for p, row in rows.items() if not row["failures"]]
    print(
        f"\npassed: {', '.join(passing) if passing else 'none'}",
        file=sys.stderr,
    )
    # 4 keeps the convention of rank_providers.py: constraints eliminated
    # everything, and the caller must decide what to relax rather than have it
    # relaxed for them.
    return 0 if passing else 4


if __name__ == "__main__":
    sys.exit(main())
