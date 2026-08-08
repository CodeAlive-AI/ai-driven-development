#!/usr/bin/env python3
"""Redact common credentials from diagnostic text before it is displayed."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPLACEMENT = "<redacted>"


def redact(text: str) -> str:
    text = re.sub(
        r"(?i)\b(https?://)[^\s/@:]+:[^\s/@]+@",
        rf"\1{REPLACEMENT}@",
        text,
    )
    text = re.sub(
        r"(?i)([?&][^\s=&]*(?:api[_-]?key|token|secret|password|passwd|authorization|auth)[^\s=&]*=)[^\s&#\"']+",
        rf"\1{REPLACEMENT}",
        text,
    )
    text = re.sub(
        r"(?i)(\bAuthorization\s*[:=]\s*)(?:Bearer|Basic)\s+[^\s,;\"']+",
        rf"\1{REPLACEMENT}",
        text,
    )
    credential = r"(?:api[_-]?key|access[_-]?token|refresh[_-]?token|auth[_-]?token|client[_-]?secret|password|passwd)"
    text = re.sub(
        rf"(?i)([\"']?{credential}[\"']?\s*[:=]\s*[\"']?)[^\s,;\"']+",
        rf"\1{REPLACEMENT}",
        text,
    )
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input")
    parser.add_argument("--output")
    args = parser.parse_args()
    source = (
        Path(args.input).read_text(encoding="utf-8", errors="replace")
        if args.input
        else sys.stdin.read()
    )
    result = redact(source)
    if args.output:
        Path(args.output).write_text(result, encoding="utf-8")
    else:
        sys.stdout.write(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
