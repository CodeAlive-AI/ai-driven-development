#!/usr/bin/env python3
"""
render-cleanup-plan.py — generate an interactive HTML cleanup-plan UI,
serve it on 127.0.0.1, open it in the default browser, and wait for the
user's selection. Designed to be invoked by the maintaining-macos-health
skill after a scan.

Usage:
    render-cleanup-plan.py <data.json>

<data.json> schema:
    {
      "baseline": {
        "container_free_gb": 117.2,
        "container_total_gb": 460,
        "container_used_gb": 329,
        "uptime": "...",
        "memory_free_pct": 40
      },
      "categories": [
        {
          "id": "tier-1-3",
          "title": "Tier 1-3 — Безрисковые кэши",
          "subtitle": "Регенерируются на следующем билде",
          "tier": 1,
          "default_open": true,
          "items": [
            {
              "id": "uniq-stable-id",
              "label": "User app cache (mo clean)",
              "path": "(via mo clean)",
              "size_bytes": 8723000000,
              "age_days": null,
              "kind": "cache",
              "command": "mo clean --confirm",
              "protected": false,
              "warning": null,
              "default_selected": true
            }, ...
          ]
        }, ...
      ]
    }

Selection JSON written to <tempdir>/cleanup-selection-<ts>.json on submit
(tempdir = %TEMP% on Windows, /tmp on macOS/Linux — tempfile.gettempdir()):
    {
      "timestamp": "2026-05-22T18:40:00",
      "selected_ids": ["...", "..."],
      "selected_items": [<full item objects>],
      "totals": {"count": 12, "size_bytes": 25000000000},
      "protected_overrides": ["id1", ...]  # protected items the user explicitly opted in
    }

Stdout: path to selection JSON when submit succeeds (or "CANCELLED\\n").
Exit code: 0 on submit, 1 on cancel/timeout/error.
"""
from __future__ import annotations

import html
import http.server
import json
import os
import socketserver
import sys
import tempfile
import threading
import time
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Any

PORT = 18347
HOST = "127.0.0.1"
SUBMIT_TIMEOUT_SEC = 60 * 60  # 1 hour — user may take their time


def human_size(num_bytes: int) -> str:
    if num_bytes is None:
        return "—"
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(num_bytes) < 1024.0:
            return f"{num_bytes:3.1f} {unit}" if unit != "B" else f"{int(num_bytes)} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} PB"


def size_class(num_bytes: int) -> str:
    if num_bytes is None:
        return "size-unknown"
    gb = num_bytes / (1024**3)
    if gb >= 5:
        return "size-xl"
    if gb >= 1:
        return "size-lg"
    if gb >= 0.1:
        return "size-md"
    return "size-sm"


def render_html(data: dict[str, Any]) -> str:
    baseline = data.get("baseline", {})
    container_free_gb = baseline.get("container_free_gb")
    container_total_gb = baseline.get("container_total_gb")
    container_used_gb = baseline.get("container_used_gb")

    pct_free = (container_free_gb / container_total_gb * 100) if container_total_gb else 0

    categories_html_parts: list[str] = []
    total_candidates_bytes = 0
    total_items_count = 0

    for cat in data.get("categories", []):
        cat_id = html.escape(cat["id"])
        cat_title = html.escape(cat["title"])
        cat_subtitle = html.escape(cat.get("subtitle", ""))
        default_open = "open" if cat.get("default_open", False) else ""
        tier = cat.get("tier", "")

        items_html: list[str] = []
        cat_bytes = 0
        cat_count = 0
        # Sort items inside each category by size descending — largest first.
        sorted_items = sorted(
            cat.get("items", []),
            key=lambda it: -(it.get("size_bytes") or 0),
        )
        for item in sorted_items:
            item_id = html.escape(item["id"])
            label = html.escape(item["label"])
            path = html.escape(item.get("path", ""))
            size_bytes = item.get("size_bytes", 0) or 0
            age_days = item.get("age_days")
            kind = html.escape(item.get("kind", ""))
            command = item.get("command")
            protected = bool(item.get("protected", False))
            warning = item.get("warning")
            default_selected = bool(item.get("default_selected", not protected))

            cat_bytes += size_bytes
            cat_count += 1
            total_candidates_bytes += size_bytes
            total_items_count += 1

            sz_label = human_size(size_bytes)
            sz_cls = size_class(size_bytes)
            age_label = f"{age_days}d" if age_days is not None else ""
            row_classes = ["item-row"]
            if protected:
                row_classes.append("protected")
            checked = "checked" if default_selected else ""
            data_attrs = (
                f'data-id="{item_id}" '
                f'data-size="{size_bytes}" '
                f'data-protected="{int(protected)}" '
            )
            warning_attr = (
                f' data-warning="{html.escape(warning, quote=True)}"'
                if warning
                else ""
            )

            # Build a structured tooltip payload (JSON-encoded into a data attribute)
            tooltip_payload = {
                "label": item["label"],
                "description": item.get("description", ""),
                "path": item.get("path", ""),
                "size": sz_label,
                "kind": kind,
                "age": (f"{age_days} days" if age_days is not None else None),
                "command": command,
                "warning": warning,
                "protected": protected,
            }
            tooltip_attr = html.escape(json.dumps(tooltip_payload, ensure_ascii=False), quote=True)

            badge_html = (
                '<span class="badge badge-protected" aria-label="protected">🔒</span>'
                if protected
                else ""
            )

            items_html.append(
                f'''
                <label class="{' '.join(row_classes)}" data-tooltip="{tooltip_attr}"{warning_attr}>
                  <input type="checkbox" class="item-cb" {checked} {data_attrs}>
                  <span class="size {sz_cls}">{sz_label}</span>
                  <span class="age">{age_label}</span>
                  <span class="kind">{kind}</span>
                  <div class="item-main">
                    <div class="label">{label}{badge_html}</div>
                    <div class="path">{path}</div>
                  </div>
                </label>
                '''
            )

        category_total = human_size(cat_bytes)
        tier_str = str(tier)
        if tier_str in ("1-3",):
            tier_cls = "cat-tier-safe"
        elif tier_str in ("7", "5", "8"):
            tier_cls = "cat-tier-medium"
        elif tier_str == "10":
            tier_cls = "cat-tier-careful"
        elif tier_str == "P":
            tier_cls = "cat-tier-protected"
        else:
            tier_cls = ""
        categories_html_parts.append(
            f'''
            <details class="category" {default_open} data-cat="{cat_id}" data-cat-total-bytes="{cat_bytes}" data-cat-total-count="{cat_count}">
              <summary>
                <span class="cat-toggle">▸</span>
                <span class="cat-tier {tier_cls}">T{tier}</span>
                <span class="cat-title">{cat_title}</span>
                <span class="cat-subtitle">{cat_subtitle}</span>
                <span class="cat-stats">
                  <span class="cat-sel-size">0 B</span><span class="sep">/</span><span class="cat-total-size">{category_total}</span>
                  <span class="dot">·</span>
                  <span class="cat-sel-count">0</span><span class="sep">/</span><span class="cat-total-count">{cat_count}</span> items
                </span>
                <label class="select-all-wrap" onclick="event.stopPropagation()">
                  <input type="checkbox" class="select-all" data-cat="{cat_id}">
                  <span class="select-all-label">all</span>
                </label>
              </summary>
              <div class="category-body">
                {''.join(items_html)}
              </div>
            </details>
            '''
        )

    categories_html = "\n".join(categories_html_parts)
    total_candidates_label = human_size(total_candidates_bytes)
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    container_free_bytes = int((container_free_gb or 0) * (1024 ** 3))
    container_total_bytes = int((container_total_gb or 0) * (1024 ** 3))
    return HTML_TEMPLATE.format(
        container_free_gb=f"{container_free_gb:.1f}" if container_free_gb else "—",
        container_total_gb=f"{container_total_gb:.0f}" if container_total_gb else "—",
        container_used_gb=f"{container_used_gb:.0f}" if container_used_gb else "—",
        container_free_bytes=container_free_bytes,
        container_total_bytes=container_total_bytes,
        pct_free=f"{pct_free:.0f}",
        total_candidates_label=total_candidates_label,
        total_items_count=total_items_count,
        categories_html=categories_html,
        generated_at=generated_at,
    )


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en" data-theme="auto">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>macOS cleanup plan</title>
  <style>
    :root {{
      --bg: #fafaf9;
      --fg: #1c1917;
      --muted: #78716c;
      --card: #ffffff;
      --border: #e7e5e4;
      --border-strong: #d6d3d1;
      --accent: #2563eb;
      --accent-fg: #ffffff;
      --warn: #c2410c;
      --warn-bg: #fff7ed;
      --danger: #b91c1c;
      --ok: #15803d;
      --shadow: 0 1px 2px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.04);
      --size-sm: #16a34a;
      --size-md: #ca8a04;
      --size-lg: #ea580c;
      --size-xl: #dc2626;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #18181b;
        --fg: #f4f4f5;
        --muted: #a1a1aa;
        --card: #27272a;
        --border: #3f3f46;
        --border-strong: #52525b;
        --accent: #60a5fa;
        --accent-fg: #0c0a09;
        --warn: #fb923c;
        --warn-bg: #431407;
        --danger: #f87171;
        --ok: #4ade80;
        --shadow: 0 1px 2px rgba(0,0,0,0.4), 0 4px 12px rgba(0,0,0,0.3);
      }}
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; padding: 0; background: var(--bg); color: var(--fg); }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif;
      font-size: 14px;
      line-height: 1.5;
      padding-bottom: 120px;
    }}
    header {{
      position: sticky;
      top: 0;
      z-index: 10;
      background: var(--bg);
      border-bottom: 1px solid var(--border);
      padding: 16px 24px;
      backdrop-filter: blur(8px);
    }}
    header h1 {{
      font-size: 18px;
      margin: 0 0 6px 0;
      font-weight: 600;
      letter-spacing: -0.01em;
    }}
    header .meta {{
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 12px;
      color: var(--muted);
    }}
    header .meta strong {{ color: var(--fg); font-weight: 600; }}
    .container {{ max-width: 1100px; margin: 0 auto; padding: 24px; }}
    .category {{
      background: var(--card);
      border: 1px solid var(--border);
      border-left: 3px solid var(--border);
      border-radius: 10px;
      margin-bottom: 14px;
      box-shadow: var(--shadow);
      overflow: hidden;
      transition: border-left-color 0.15s;
    }}
    .category.has-selection {{ border-left-color: var(--accent); }}
    .category summary {{
      display: grid;
      grid-template-columns: 18px 56px minmax(180px, max-content) 1fr auto auto;
      grid-template-rows: auto auto;
      column-gap: 14px;
      row-gap: 4px;
      align-items: center;
      padding: 14px 18px;
      cursor: pointer;
      list-style: none;
      user-select: none;
    }}
    .category summary .cat-toggle,
    .category summary .cat-tier,
    .category summary .cat-title,
    .category summary .cat-stats,
    .category summary .select-all-wrap {{ grid-row: 1; }}
    .category summary .cat-subtitle {{
      grid-column: 3 / -1;
      grid-row: 2;
      margin-top: -2px;
    }}
    .category summary::-webkit-details-marker {{ display: none; }}
    .cat-toggle {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.15s;
      color: var(--fg);
      font-size: 14px;
      width: 18px;
      line-height: 1;
    }}
    .category[open] .cat-toggle {{ transform: rotate(90deg); }}
    .cat-tier {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 52px;
      height: 22px;
      padding: 0 10px;
      border-radius: 6px;
      background: var(--border);
      color: var(--muted);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.02em;
      white-space: nowrap;
    }}
    .cat-tier-safe {{ background: rgba(34,197,94,0.18); color: var(--ok); }}
    .cat-tier-medium {{ background: rgba(37,99,235,0.18); color: var(--accent); }}
    .cat-tier-careful {{ background: rgba(194,65,12,0.22); color: var(--warn); }}
    .cat-tier-protected {{ background: rgba(185,28,28,0.22); color: var(--danger); }}
    .cat-title {{
      font-weight: 600;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .cat-subtitle {{
      color: var(--muted);
      font-size: 12px;
      font-weight: 400;
      white-space: normal;
      line-height: 1.4;
    }}
    .cat-stats {{
      color: var(--muted);
      font-size: 12px;
      font-variant-numeric: tabular-nums;
      white-space: nowrap;
      display: inline-flex;
      align-items: baseline;
      gap: 4px;
    }}
    .cat-stats .cat-sel-size {{
      color: var(--accent);
      font-weight: 700;
      font-size: 13px;
    }}
    .cat-stats .cat-total-size,
    .cat-stats .cat-sel-count,
    .cat-stats .cat-total-count {{ color: var(--fg); font-weight: 500; }}
    .cat-stats .sep, .cat-stats .dot {{ color: var(--muted); margin: 0 2px; }}
    .category.empty-selection .cat-sel-size {{ color: var(--muted); font-weight: 500; }}
    .select-all-wrap {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 6px;
      background: var(--bg);
      font-size: 11px;
      color: var(--muted);
      cursor: pointer;
      white-space: nowrap;
    }}
    .select-all-wrap input {{ margin: 0; cursor: pointer; }}
    .actions .select-all-wrap {{
      padding: 10px 14px;
      border: 1px solid var(--border-strong);
      color: var(--fg);
      font-weight: 500;
    }}
    .category-body {{
      border-top: 1px solid var(--border);
      padding: 4px 0;
    }}
    .item-row {{
      display: grid;
      grid-template-columns: 22px 78px 44px 110px 1fr;
      column-gap: 12px;
      align-items: center;
      padding: 8px 18px;
      cursor: pointer;
      border-radius: 6px;
      margin: 2px 8px;
      transition: background 0.1s;
      min-height: 44px;
    }}
    .item-row:hover {{ background: var(--bg); }}
    .item-row.protected {{ opacity: 0.6; }}
    .item-row.protected:hover {{ opacity: 0.95; }}
    .item-row input[type="checkbox"] {{ margin: 0; cursor: pointer; transform: scale(1.1); }}
    .item-row .size {{
      font-variant-numeric: tabular-nums;
      font-weight: 600;
      text-align: right;
      font-size: 12px;
    }}
    .size-sm {{ color: var(--size-sm); }}
    .size-md {{ color: var(--size-md); }}
    .size-lg {{ color: var(--size-lg); }}
    .size-xl {{ color: var(--size-xl); }}
    .size-unknown {{ color: var(--muted); }}
    .item-row .age {{
      font-size: 11px;
      color: var(--muted);
      font-variant-numeric: tabular-nums;
      text-align: right;
    }}
    .item-row .kind {{
      font-size: 11px;
      color: var(--muted);
      padding: 2px 6px;
      background: var(--bg);
      border-radius: 4px;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .item-main {{
      min-width: 0;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}
    .item-main .label {{
      font-weight: 500;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .item-main .path {{
      font-family: "SF Mono", "Menlo", "Consolas", monospace;
      font-size: 11px;
      color: var(--muted);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      direction: ltr;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      font-size: 10px;
      padding: 1px 5px;
      border-radius: 4px;
      font-weight: 600;
      letter-spacing: 0.02em;
      line-height: 1;
    }}
    .badge-protected {{
      background: var(--warn-bg);
      color: var(--warn);
      border: 1px solid var(--warn);
    }}
    footer {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: var(--card);
      border-top: 1px solid var(--border-strong);
      padding: 14px 24px;
      box-shadow: 0 -4px 12px rgba(0,0,0,0.06);
      z-index: 100;
    }}
    footer .inner {{
      max-width: 1100px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}
    .summary-stats {{
      display: flex;
      gap: 28px;
      align-items: baseline;
    }}
    .summary-stats .big {{
      font-size: 22px;
      font-weight: 700;
      font-variant-numeric: tabular-nums;
      letter-spacing: -0.02em;
    }}
    .summary-stats .big.accent {{ color: var(--accent); }}
    .summary-stats .label-sub {{
      color: var(--muted);
      font-size: 12px;
      margin-left: 4px;
    }}
    .summary-stats .muted-dot {{ margin: 0 4px; }}
    .summary-stats .after-preview {{
      display: flex;
      align-items: baseline;
      gap: 4px;
      padding: 6px 14px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
    }}
    .summary-stats .after-preview .big {{
      color: var(--ok);
      font-size: 20px;
    }}
    .summary-stats .protected-count {{ color: var(--warn); }}
    .actions button {{
      font: inherit;
      padding: 10px 18px;
      border: 1px solid var(--border-strong);
      border-radius: 8px;
      background: var(--card);
      color: var(--fg);
      cursor: pointer;
      font-weight: 500;
      transition: all 0.1s;
    }}
    .actions button:hover {{ background: var(--bg); }}
    .actions button.primary {{
      background: var(--accent);
      color: var(--accent-fg);
      border-color: var(--accent);
      font-weight: 600;
      margin-left: 8px;
    }}
    .actions button.primary:hover {{ filter: brightness(1.1); }}
    .actions button:disabled {{ opacity: 0.5; cursor: not-allowed; }}
    #done-screen {{
      display: none;
      position: fixed;
      inset: 0;
      background: var(--bg);
      align-items: center;
      justify-content: center;
      flex-direction: column;
      gap: 16px;
      text-align: center;
      padding: 24px;
      z-index: 1000;
    }}
    #done-screen.shown {{ display: flex; }}
    #done-screen .check {{
      font-size: 48px;
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background: var(--ok);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
    }}
    #done-screen h2 {{ margin: 0; font-size: 22px; }}
    #done-screen p {{ color: var(--muted); margin: 0; max-width: 480px; }}
    #done-screen .done-stats {{
      display: flex;
      gap: 28px;
      align-items: baseline;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 22px;
      box-shadow: var(--shadow);
    }}
    #done-screen .done-stats .stat-block {{
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 2px;
    }}
    #done-screen .done-stats .stat-num {{
      font-size: 22px;
      font-weight: 700;
      letter-spacing: -0.02em;
      font-variant-numeric: tabular-nums;
    }}
    #done-screen .done-stats .stat-num.accent {{ color: var(--accent); }}
    #done-screen .done-stats .stat-num.ok {{ color: var(--ok); }}
    #done-screen .done-stats .stat-label {{
      color: var(--muted);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    #done-screen code {{
      background: var(--card);
      padding: 4px 8px;
      border-radius: 4px;
      font-family: "SF Mono", monospace;
      font-size: 12px;
    }}
    .toast {{
      position: fixed;
      top: 24px;
      right: 24px;
      background: var(--danger);
      color: white;
      padding: 12px 16px;
      border-radius: 8px;
      box-shadow: var(--shadow);
      z-index: 200;
      opacity: 0;
      transform: translateY(-10px);
      transition: all 0.2s;
      pointer-events: none;
    }}
    .toast.shown {{ opacity: 1; transform: translateY(0); }}
    #tt {{
      position: fixed;
      z-index: 200;
      max-width: 520px;
      min-width: 280px;
      background: var(--card);
      color: var(--fg);
      border: 1px solid var(--border-strong);
      border-radius: 8px;
      padding: 12px 14px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.18), 0 2px 6px rgba(0,0,0,0.12);
      font-size: 12px;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.08s ease-out;
      display: none;
    }}
    #tt.shown {{ opacity: 1; display: block; }}
    #tt .tt-title {{
      font-weight: 600;
      font-size: 13px;
      margin: 0 0 6px 0;
      letter-spacing: -0.01em;
    }}
    #tt .tt-desc {{
      color: var(--fg);
      font-size: 12px;
      line-height: 1.5;
      margin: 0 0 10px 0;
      padding: 8px 10px;
      background: var(--bg);
      border-radius: 6px;
      border-left: 3px solid var(--accent);
    }}
    #tt .tt-row {{
      display: grid;
      grid-template-columns: 78px 1fr;
      gap: 8px;
      align-items: baseline;
      padding: 2px 0;
    }}
    #tt .tt-label {{
      color: var(--muted);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    #tt .tt-value {{
      font-family: "SF Mono", "Menlo", "Consolas", monospace;
      font-size: 11.5px;
      word-break: break-all;
      white-space: pre-wrap;
    }}
    #tt .tt-value.tt-mono-strong {{
      color: var(--fg);
      font-weight: 500;
    }}
    #tt .tt-warning {{
      margin-top: 8px;
      padding: 8px 10px;
      border-radius: 6px;
      background: var(--warn-bg);
      color: var(--warn);
      border: 1px solid var(--warn);
      font-size: 11.5px;
      line-height: 1.45;
    }}
    #tt .tt-protected {{
      margin-top: 8px;
      padding: 6px 10px;
      border-radius: 6px;
      background: var(--warn-bg);
      color: var(--warn);
      font-weight: 600;
      font-size: 11px;
      letter-spacing: 0.02em;
    }}
    @media (max-width: 720px) {{
      .item-row {{ grid-template-columns: 22px 60px 1fr; }}
      .item-row .age, .item-row .kind {{ display: none; }}
      .item-main .path {{ display: none; }}
      .category summary {{ grid-template-columns: 18px 52px 1fr auto; }}
      .cat-subtitle, .cat-stats {{ display: none; }}
    }}
    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{
        transition-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
      }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>🧹 Windows cleanup plan</h1>
    <div class="meta">
      <span><strong>{container_free_gb} GB</strong> free <span class="label-sub">/ {container_total_gb} GB · {pct_free}%</span></span>
      <span><strong>{container_used_gb} GB</strong> used</span>
      <span><strong>{total_items_count}</strong> candidate items · <strong>{total_candidates_label}</strong> total</span>
      <span class="label-sub">Generated {generated_at}</span>
    </div>
  </header>

  <main class="container">
    {categories_html}
  </main>

  <footer>
    <div class="inner">
      <div class="summary-stats">
        <div>
          <span class="big accent" id="sel-size">0 B</span>
          <span class="label-sub">selected</span>
          <span class="label-sub muted-dot">·</span>
          <span class="label-sub"><span id="sel-count">0</span> items</span>
        </div>
        <div class="after-preview" id="after-preview">
          <span class="label-sub">after cleanup →</span>
          <span class="big" id="after-free">{container_free_gb} GB</span>
          <span class="label-sub">free (<span id="after-pct">{pct_free}</span>%)</span>
        </div>
        <div id="protected-warning" style="display:none">
          <span class="big protected-count" id="sel-protected">0</span>
          <span class="label-sub">protected ⚠</span>
        </div>
      </div>
      <div class="actions">
        <label class="select-all-wrap">
          <input type="checkbox" id="select-all-global">
          <span class="select-all-label">all files</span>
        </label>
        <button id="cancel-btn" type="button">Cancel</button>
        <button id="submit-btn" class="primary" type="button" disabled>Submit plan →</button>
      </div>
    </div>
  </footer>

  <div id="done-screen">
    <div class="check">✓</div>
    <h2>Plan submitted</h2>
    <p id="done-summary">You can close this window. Return to the terminal — the agent will show your selection and ask for confirmation before applying any changes.</p>
    <div id="done-stats" class="done-stats"></div>
    <code id="done-path"></code>
  </div>

  <div class="toast" id="toast"></div>

  <div id="tt" role="tooltip"></div>

  <script>
    const allItems = document.querySelectorAll('.item-cb');
    const selSize = document.getElementById('sel-size');
    const selCount = document.getElementById('sel-count');
    const selProtected = document.getElementById('sel-protected');
    const protectedWarning = document.getElementById('protected-warning');
    const selectAllGlobal = document.getElementById('select-all-global');
    const submitBtn = document.getElementById('submit-btn');
    const cancelBtn = document.getElementById('cancel-btn');
    const doneScreen = document.getElementById('done-screen');
    const donePath = document.getElementById('done-path');
    const toast = document.getElementById('toast');

    function humanSize(bytes) {{
      const units = ['B', 'KB', 'MB', 'GB', 'TB'];
      let n = bytes, i = 0;
      while (n >= 1024 && i < units.length - 1) {{ n /= 1024; i++; }}
      return (i === 0 ? n.toFixed(0) : n.toFixed(1)) + ' ' + units[i];
    }}

    function showToast(msg, ms) {{
      toast.textContent = msg;
      toast.classList.add('shown');
      setTimeout(() => toast.classList.remove('shown'), ms || 3000);
    }}

    const BASELINE_FREE_BYTES = {container_free_bytes};
    const BASELINE_TOTAL_BYTES = {container_total_bytes};
    const afterFree = document.getElementById('after-free');
    const afterPct = document.getElementById('after-pct');
    function updateTotals() {{
      let totalBytes = 0, count = 0, protectedCount = 0;
      allItems.forEach(cb => {{
        if (cb.checked) {{
          count++;
          totalBytes += parseInt(cb.dataset.size, 10) || 0;
          if (cb.dataset.protected === '1') protectedCount++;
        }}
      }});
      selSize.textContent = humanSize(totalBytes);
      selCount.textContent = count;
      submitBtn.disabled = count === 0;

      // After-cleanup preview: free + selected, capped at total
      const afterBytes = Math.min(BASELINE_FREE_BYTES + totalBytes, BASELINE_TOTAL_BYTES);
      const afterGb = afterBytes / (1024 ** 3);
      const afterPctVal = (afterBytes / BASELINE_TOTAL_BYTES) * 100;
      if (afterFree) afterFree.textContent = afterGb.toFixed(1) + ' GB';
      if (afterPct) afterPct.textContent = afterPctVal.toFixed(0);

      if (protectedCount > 0) {{
        protectedWarning.style.display = '';
        selProtected.textContent = protectedCount;
      }} else {{
        protectedWarning.style.display = 'none';
      }}
      // category counters + per-category live size
      document.querySelectorAll('.category').forEach(cat => {{
        const items = cat.querySelectorAll('.item-cb');
        const checked = cat.querySelectorAll('.item-cb:checked');
        let catBytes = 0;
        checked.forEach(cb => {{ catBytes += parseInt(cb.dataset.size, 10) || 0; }});
        const selSizeEl = cat.querySelector('.cat-sel-size');
        const selCountEl = cat.querySelector('.cat-sel-count');
        if (selSizeEl) selSizeEl.textContent = humanSize(catBytes);
        if (selCountEl) selCountEl.textContent = checked.length;
        cat.classList.toggle('empty-selection', checked.length === 0);
        cat.classList.toggle('has-selection', checked.length > 0);
        const selectAll = cat.querySelector('.select-all');
        if (selectAll) {{
          selectAll.checked = items.length > 0 && items.length === checked.length;
          selectAll.indeterminate = checked.length > 0 && checked.length < items.length;
        }}
      }});
      if (selectAllGlobal) {{
        selectAllGlobal.checked = allItems.length > 0 && count === allItems.length;
        selectAllGlobal.indeterminate = count > 0 && count < allItems.length;
      }}
    }}

    // Esc → cancel (peak-end / keyboard-friendly)
    document.addEventListener('keydown', (ev) => {{
      if (ev.key === 'Escape' && !doneScreen.classList.contains('shown')) {{
        ev.preventDefault();
        cancelBtn.click();
      }}
    }});

    allItems.forEach(cb => {{
      cb.addEventListener('change', (ev) => {{
        const row = cb.closest('.item-row');
        if (cb.checked && cb.dataset.protected === '1') {{
          const warning = row.dataset.warning || 'This item is protected. Deleting it can lose user data or break apps.';
          if (!confirm('⚠️ PROTECTED ITEM\\n\\n' + warning + '\\n\\nAre you sure you want to include this?')) {{
            cb.checked = false;
          }}
        }}
        updateTotals();
      }});
    }});

    function confirmProtectedBulk(scopeLabel, protectedCount) {{
      if (protectedCount === 0) return true;
      return confirm(
        '⚠️ PROTECTED ITEMS\\n\\n' +
        scopeLabel + ' includes ' + protectedCount + ' protected item(s). ' +
        'These may include user data, synced files, dumps, models, VM disks, or irreversible system actions.\\n\\n' +
        'Select them anyway?'
      );
    }}

    function setItemsChecked(items, checked, scopeLabel) {{
      const itemList = Array.from(items);
      const protectedCount = itemList.filter(cb => cb.dataset.protected === '1').length;
      if (checked && !confirmProtectedBulk(scopeLabel, protectedCount)) {{
        return false;
      }}
      itemList.forEach(cb => {{ cb.checked = checked; }});
      updateTotals();
      if (checked && protectedCount > 0) {{
        showToast('Selected ' + protectedCount + ' protected item(s). Review before Submit.', 5000);
      }}
      return true;
    }}

    document.querySelectorAll('.select-all').forEach(sa => {{
      sa.addEventListener('change', (ev) => {{
        ev.stopPropagation();
        const catId = sa.dataset.cat;
        const cat = document.querySelector('.category[data-cat="' + catId + '"]');
        const items = cat.querySelectorAll('.item-cb');
        if (!setItemsChecked(items, sa.checked, 'This category')) {{
          updateTotals();
        }}
      }});
    }});

    selectAllGlobal.addEventListener('change', () => {{
      if (!setItemsChecked(allItems, selectAllGlobal.checked, 'The full cleanup plan')) {{
        updateTotals();
      }}
    }});

    cancelBtn.addEventListener('click', async () => {{
      if (!confirm('Cancel and close? No cleanup will be performed.')) return;
      try {{
        await fetch('/cancel', {{ method: 'POST' }});
      }} catch (e) {{}}
      doneScreen.querySelector('.check').textContent = '×';
      doneScreen.querySelector('.check').style.background = 'var(--muted)';
      doneScreen.querySelector('h2').textContent = 'Cancelled';
      doneScreen.querySelector('p').textContent = 'No changes were made. You can close this window.';
      donePath.style.display = 'none';
      doneScreen.classList.add('shown');
    }});

    submitBtn.addEventListener('click', async () => {{
      const selected = [];
      const protectedOverrides = [];
      let totalBytes = 0;
      allItems.forEach(cb => {{
        if (cb.checked) {{
          selected.push(cb.dataset.id);
          totalBytes += parseInt(cb.dataset.size, 10) || 0;
          if (cb.dataset.protected === '1') protectedOverrides.push(cb.dataset.id);
        }}
      }});
      if (selected.length === 0) {{ showToast('Nothing selected.'); return; }}
      const payload = {{
        selected_ids: selected,
        protected_overrides: protectedOverrides,
        totals: {{ count: selected.length, size_bytes: totalBytes }}
      }};
      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending…';
      try {{
        const resp = await fetch('/submit', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify(payload)
        }});
        if (!resp.ok) throw new Error('HTTP ' + resp.status);
        const result = await resp.json();
        donePath.textContent = result.path || '';
        const afterBytes = Math.min(BASELINE_FREE_BYTES + totalBytes, BASELINE_TOTAL_BYTES);
        const afterGb = (afterBytes / (1024 ** 3)).toFixed(1);
        const afterPctVal = ((afterBytes / BASELINE_TOTAL_BYTES) * 100).toFixed(0);
        document.getElementById('done-stats').innerHTML =
          '<div class="stat-block"><span class="stat-num accent">' + humanSize(totalBytes) + '</span><span class="stat-label">to be freed</span></div>' +
          '<div class="stat-block"><span class="stat-num">' + selected.length + '</span><span class="stat-label">items</span></div>' +
          '<div class="stat-block"><span class="stat-num ok">' + afterGb + ' GB</span><span class="stat-label">free after (' + afterPctVal + '%)</span></div>' +
          (protectedOverrides.length > 0
            ? '<div class="stat-block"><span class="stat-num" style="color:var(--warn)">' + protectedOverrides.length + ' ⚠</span><span class="stat-label">protected overrides</span></div>'
            : '');
        doneScreen.classList.add('shown');
      }} catch (e) {{
        showToast('Submit failed: ' + e.message, 6000);
        submitBtn.disabled = false;
        submitBtn.textContent = 'Submit plan →';
      }}
    }});

    updateTotals();

    // -----------------------------------------------------------------------
    // Custom tooltip — multi-line, structured, instant
    // -----------------------------------------------------------------------
    const tt = document.getElementById('tt');
    function escapeHtml(s) {{
      return String(s == null ? '' : s)
        .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    }}
    function renderTooltip(payload) {{
      const descHtml = payload.description
        ? '<div class="tt-desc">' + escapeHtml(payload.description) + '</div>'
        : '';
      const rows = [];
      if (payload.path)    rows.push(['Path',    payload.path,    'tt-mono-strong']);
      if (payload.kind)    rows.push(['Kind',    payload.kind]);
      if (payload.size)    rows.push(['Size',    payload.size]);
      if (payload.age)     rows.push(['Modified', payload.age + ' ago']);
      if (payload.command) rows.push(['Command', payload.command, 'tt-mono-strong']);
      const rowsHtml = rows.map(([l, v, cls]) =>
        '<div class="tt-row"><div class="tt-label">' + escapeHtml(l) +
        '</div><div class="tt-value ' + (cls || '') + '">' + escapeHtml(v) + '</div></div>'
      ).join('');
      const warnHtml = payload.warning
        ? '<div class="tt-warning">⚠ ' + escapeHtml(payload.warning) + '</div>'
        : '';
      const protHtml = payload.protected
        ? '<div class="tt-protected">🔒 PROTECTED — checking requires explicit confirm</div>'
        : '';
      return '<div class="tt-title">' + escapeHtml(payload.label || '') + '</div>' +
             descHtml + rowsHtml + warnHtml + protHtml;
    }}
    function positionTooltip(clientX, clientY) {{
      const margin = 14;
      const rect = tt.getBoundingClientRect();
      const vw = window.innerWidth, vh = window.innerHeight;
      let x = clientX + 18;
      let y = clientY + 18;
      if (x + rect.width + margin > vw) x = Math.max(margin, clientX - rect.width - 18);
      if (y + rect.height + margin > vh) y = Math.max(margin, clientY - rect.height - 18);
      tt.style.left = x + 'px';
      tt.style.top = y + 'px';
    }}
    function showTooltipFromEvent(target, ev) {{
      const raw = target.getAttribute('data-tooltip');
      if (!raw) return;
      let payload;
      try {{ payload = JSON.parse(raw); }} catch (e) {{ return; }}
      tt.innerHTML = renderTooltip(payload);
      tt.classList.add('shown');
      positionTooltip(ev.clientX, ev.clientY);
    }}
    function hideTooltip() {{ tt.classList.remove('shown'); }}
    document.addEventListener('mouseover', (ev) => {{
      const target = ev.target.closest('[data-tooltip]');
      if (target) showTooltipFromEvent(target, ev);
    }});
    document.addEventListener('mousemove', (ev) => {{
      if (!tt.classList.contains('shown')) return;
      const target = ev.target.closest('[data-tooltip]');
      if (!target) {{ hideTooltip(); return; }}
      positionTooltip(ev.clientX, ev.clientY);
    }});
    document.addEventListener('mouseout', (ev) => {{
      if (!ev.relatedTarget || !ev.relatedTarget.closest('[data-tooltip]')) hideTooltip();
    }});
    document.addEventListener('scroll', hideTooltip, true);
  </script>
</body>
</html>
"""


class CleanupServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    """ThreadingMixIn so requests don't block each other; daemon_threads so the process
    can exit cleanly even if a request thread is mid-flight."""
    allow_reuse_address = True
    daemon_threads = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.submission: dict | None = None
        self.cancelled = False
        self.shutdown_event = threading.Event()


def make_handler(html_content: str, data_categories: list[dict]):
    # index items by id for resolving selection back to full objects
    id_to_item: dict[str, dict] = {}
    id_to_category: dict[str, str] = {}
    for cat in data_categories:
        for item in cat.get("items", []):
            id_to_item[item["id"]] = item
            id_to_category[item["id"]] = cat["id"]

    class Handler(http.server.BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            pass  # silence stderr

        def do_GET(self):
            if self.path in ("/", "/index.html"):
                body = html_content.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            elif self.path == "/health":
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"ok")
            else:
                self.send_error(404)

        def do_POST(self):
            try:
                length = int(self.headers.get("Content-Length", "0"))
                raw = self.rfile.read(length) if length else b""
            except Exception as exc:
                self.send_error(400, f"bad request: {exc}")
                return

            if self.path == "/cancel":
                self.server.cancelled = True
                try:
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Connection", "close")
                    self.end_headers()
                    self.wfile.write(b'{"ok":true}')
                    self.wfile.flush()
                except Exception:
                    pass
                # Signal main thread to exit. ThreadingMixIn + daemon_threads means
                # serve_forever() is still running on another thread; setting the event
                # lets main wake up, call server.shutdown(), and the loop ends cleanly.
                self.server.shutdown_event.set()
                return

            if self.path == "/submit":
                print(f"[render-cleanup-plan] received /submit ({len(raw)} bytes)", file=sys.stderr)
                try:
                    payload = json.loads(raw.decode("utf-8")) if raw else {}
                except Exception as exc:
                    self.send_error(400, f"bad json: {exc}")
                    return
                try:
                    selected_ids = payload.get("selected_ids", []) or []
                    protected_overrides = payload.get("protected_overrides", []) or []
                    selected_items = [
                        {**id_to_item[i], "category_id": id_to_category.get(i, "")}
                        for i in selected_ids
                        if i in id_to_item
                    ]
                    total_bytes = sum(it.get("size_bytes", 0) or 0 for it in selected_items)
                    selection = {
                        "timestamp": datetime.now().isoformat(),
                        "selected_ids": selected_ids,
                        "selected_items": selected_items,
                        "protected_overrides": protected_overrides,
                        "totals": {"count": len(selected_items), "size_bytes": total_bytes},
                    }
                    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
                    # Cross-platform temp dir: /tmp on macOS/Linux, %TEMP% on Windows.
                    out_path = Path(tempfile.gettempdir()) / f"cleanup-selection-{ts}.json"
                    out_path.write_text(json.dumps(selection, indent=2, ensure_ascii=False), encoding="utf-8")
                    self.server.submission = {"selection": selection, "path": str(out_path)}
                    body = json.dumps({"ok": True, "path": str(out_path)}).encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Connection", "close")
                    self.end_headers()
                    self.wfile.write(body)
                    self.wfile.flush()
                except Exception as exc:
                    print(f"[render-cleanup-plan] /submit handler error: {exc}", file=sys.stderr)
                    try:
                        self.send_error(500, f"server error: {exc}")
                    except Exception:
                        pass
                    return
                # Now signal main to exit. No sleep needed — ThreadingMixIn means the
                # response has been written and flushed before this point.
                self.server.shutdown_event.set()
                return

            self.send_error(404)

    return Handler


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: render-cleanup-plan.py <data.json>", file=sys.stderr)
        return 2
    data_path = Path(argv[1])
    if not data_path.is_file():
        print(f"data file not found: {data_path}", file=sys.stderr)
        return 2
    data = json.loads(data_path.read_text(encoding="utf-8"))
    html_content = render_html(data)

    handler = make_handler(html_content, data.get("categories", []))
    try:
        server = CleanupServer((HOST, PORT), handler)
    except OSError as exc:
        print(f"failed to bind {HOST}:{PORT}: {exc}", file=sys.stderr)
        return 1

    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    url = f"http://{HOST}:{PORT}/"
    # eprint, not stdout — stdout is reserved for the final selection path
    print(f"[render-cleanup-plan] serving at {url}", file=sys.stderr)
    print(f"[render-cleanup-plan] waiting for user selection (timeout {SUBMIT_TIMEOUT_SEC}s)…", file=sys.stderr)

    # macOS: `open` works for arbitrary URLs and respects the user's default browser
    try:
        if sys.platform == "darwin":
            os.system(f"open '{url}'")
        else:
            webbrowser.open(url)
    except Exception:
        pass

    finished = server.shutdown_event.wait(timeout=SUBMIT_TIMEOUT_SEC)
    print("[render-cleanup-plan] shutdown_event received, stopping server", file=sys.stderr)
    try:
        server.shutdown()
    except Exception as exc:
        print(f"[render-cleanup-plan] server.shutdown() error: {exc}", file=sys.stderr)
    try:
        server.server_close()
    except Exception:
        pass
    server_thread.join(timeout=2)

    if not finished:
        print("TIMEOUT", file=sys.stderr)
        return 1
    if server.cancelled:
        print("CANCELLED")
        return 1
    if server.submission:
        print(server.submission["path"])
        return 0
    print("NO_SUBMISSION", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
