"""Loopback-only selection + confirmation. Submit never authorizes deletion."""
from __future__ import annotations

import importlib.util
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys
import threading
import time
from urllib.parse import urlsplit

from disk_safety import ASSETS, digest, read_json, write_json
from disk_responses import review_selection, set_status


def _renderer():
    path = ASSETS / "render-cleanup-plan.py"
    spec = importlib.util.spec_from_file_location("mac_health_cleanup_plan", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def page(plan, token):
    """Render the automatic incident through the skill's canonical plan UI."""
    free, total = plan.get("free_bytes", 0), plan.get("total_bytes", 1)
    grouped = {}
    for item in plan["items"]:
        root = item.get("root", "Other")
        grouped.setdefault(root, []).append(item)
    categories = []
    for root, items in grouped.items():
        downloads = root == "Downloads"
        audit = root == "Storage audit"
        categories.append({
            "id": "storage-audit" if audit else ("downloads" if downloads else "safe-package-caches"),
            "title": "Storage map (read-only)" if audit else ("Protected downloads" if downloads else "Regenerable package caches"),
            "subtitle": ("Largest folders found by the skill; open them for a deeper manual plan."
                         if audit else ("Shown for context only; automatic deletion is disabled for possible unique data."
                         if downloads else "Controller-verified files removed one at a time through Mole.")),
            "tier": "P" if downloads or audit else "1-3",
            "default_open": True,
            "items": [{**item, "kind": "archive" if downloads else "cache",
                       "protected": downloads or audit,
                       "selectable": item.get("operation") == "mole-remove-file" and not downloads,
                       "default_selected": False} for item in items],
        })
    data = {"summary": plan.get("summary", ""),
            "baseline": {"container_free_gb": free / 1024**3,
                           "container_total_gb": total / 1024**3,
                           "container_used_gb": (total-free) / 1024**3},
            "categories": categories}
    document = _renderer().render_html(data)
    safe_token = json.dumps(token).replace("<", "\\u003c")
    document = document.replace("const allItems =", f"const CLEANUP_TOKEN = {safe_token};\n    const allItems =")
    document = document.replace("headers: { 'Content-Type': 'application/json' }",
        "headers: { 'Content-Type': 'application/json', 'X-Cleanup-Token': CLEANUP_TOKEN }")
    document = document.replace("await fetch('/cancel', { method: 'POST' })",
        "await fetch('/cancel', { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-Cleanup-Token': CLEANUP_TOKEN }, body: '{}' })")
    controls = '''<button id="confirm-automatic" class="primary" type="button" hidden>Confirm permanent deletion</button>
<script>
const confirmAutomatic=document.getElementById('confirm-automatic');
document.querySelector('#done-screen').appendChild(confirmAutomatic);
async function automaticStatus(){
 const response=await fetch('/status',{headers:{'X-Cleanup-Token':CLEANUP_TOKEN}});const data=await response.json();
 const title=document.querySelector('#done-screen h2'),summary=document.querySelector('#done-summary');
 if(data.status==='reviewing'){title.textContent='Agent reviewing selection…';summary.textContent='The same Codex session is checking the exact selection.'}
 if(data.status==='awaiting_confirmation'){title.textContent='Review complete';summary.textContent=data.review||'Review the exact selection before deletion.';confirmAutomatic.hidden=false}
 if(['completed','partial'].includes(data.status)){title.textContent='Cleanup complete';summary.textContent=data.review||'Only the confirmed files were processed.';confirmAutomatic.hidden=true}
 if(['failed','expired','cancelled'].includes(data.status)){title.textContent=data.status;summary.textContent=data.error||'No further action will run.';confirmAutomatic.hidden=true}
}
confirmAutomatic.onclick=async()=>{if(!confirm('Permanently delete ONLY the selected files? This cannot be undone.'))return;
 confirmAutomatic.disabled=true;const response=await fetch('/confirm',{method:'POST',headers:{'Content-Type':'application/json','X-Cleanup-Token':CLEANUP_TOKEN},body:'{}'});
 if(!response.ok){confirmAutomatic.disabled=false;throw Error('Confirmation failed')}await automaticStatus()};
setInterval(()=>automaticStatus().catch(()=>{}),1500);
</script>'''
    return document.replace("</body>", controls + "</body>")


class ReviewServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, context, incident, review=review_selection, apply=None):
        self.context, self.incident = context, incident
        self.plan = read_json(incident / "plan.json")
        self.token = secrets.token_urlsafe(32)
        self.mutation_lock = threading.Lock()
        self.review = review
        self.apply = apply or self.apply_selection
        self.workers = []
        super().__init__(("127.0.0.1", 0), Handler)
        self.origin = f"http://127.0.0.1:{self.server_port}"

    def background(self, function):
        thread = threading.Thread(target=function, args=(self.context, self.incident), daemon=False)
        self.workers.append(thread)
        thread.start()

    @staticmethod
    def apply_selection(context, incident):
        # The sanctioned helper dispatches typed v2 selections back to the
        # controller. It cannot take commands/paths from the HTTP payload.
        try:
            result = subprocess.run([sys.executable, str(ASSETS / "apply-cleanup-selection.py"),
                                     str(incident / "selection.json")],
                                    stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=300)
            if result.returncode:
                raise RuntimeError(result.stderr[-1000:] or result.stdout[-1000:])
        except Exception as exc:
            set_status(incident, "failed", error=str(exc))


class Handler(BaseHTTPRequestHandler):
    server: ReviewServer
    protocol_version = "HTTP/1.0"

    def setup(self):
        super().setup()
        self.connection.settimeout(5)

    def log_message(self, *args):
        pass

    def respond(self, status, value, content_type="application/json"):
        body = value.encode() if isinstance(value, str) else json.dumps(value).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
        self.end_headers()
        self.wfile.write(body)

    def authorized(self, page_request=False):
        if self.headers.get("Host") != self.server.origin.removeprefix("http://"):
            return False
        origin = self.headers.get("Origin")
        if origin is not None and origin != self.server.origin:
            return False
        token = urlsplit(self.path).query if page_request else self.headers.get("X-Cleanup-Token", "")
        return secrets.compare_digest(token, self.server.token)

    def do_GET(self):
        page_request = urlsplit(self.path).path == "/"
        if not self.authorized(page_request):
            return self.respond(403, {"error": "invalid host/origin/token"})
        if page_request:
            return self.respond(200, page(self.server.plan, self.server.token), "text/html; charset=utf-8")
        if self.path == "/status":
            status = read_json(self.server.incident / "status.json")
            selected = self.server.incident / "selection.json"
            if selected.exists():
                status["selected_ids"] = read_json(selected)["selected_ids"]
            return self.respond(200, status)
        return self.respond(404, {"error": "not found"})

    def do_POST(self):
        if not self.authorized() or self.headers.get("Origin") != self.server.origin:
            return self.respond(403, {"error": "invalid host/origin/token"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 32768 or self.headers.get("Content-Type") != "application/json":
                raise ValueError("invalid content type or size")
            payload = json.loads(self.rfile.read(length))
            if not isinstance(payload, dict):
                raise ValueError("expected JSON object")
            with self.server.mutation_lock:
                self.mutate(payload)
        except (ValueError, KeyError, TypeError) as exc:
            self.respond(400, {"error": str(exc)})
        except Exception as exc:
            set_status(self.server.incident, "failed", error=str(exc))
            self.respond(500, {"error": "operation failed; no retry was queued"})

    def mutate(self, payload):
        incident, context = self.server.incident, self.server.context
        if not context.allowed("agent_plan") or (incident / "stale.json").exists():
            raise ValueError("revoked/paused/stale; no operation permitted")
        if time.time() - self.server.plan["created_at"] > 3600:
            raise ValueError("plan expired; rescan before applying")
        status = read_json(incident / "status.json")["status"]
        if self.path == "/submit":
            if set(payload) not in ({"selected_ids"}, {"selected_ids", "protected_overrides", "totals"}):
                raise ValueError("unexpected selection fields")
            ids = payload["selected_ids"]
            indexed = {row["id"]: row for row in self.server.plan["items"]}
            if (not isinstance(ids, list) or not ids or any(not isinstance(i, str) for i in ids)
                    or len(set(ids)) != len(ids) or any(i not in indexed for i in ids)):
                raise ValueError("unknown/duplicate/empty selected IDs")
            if any(indexed[i].get("operation") != "mole-remove-file"
                   or indexed[i].get("root") == "Downloads" for i in ids):
                raise ValueError("informational/protected items cannot be selected in automatic mode")
            if (incident / "selection.json").exists():
                if read_json(incident / "selection.json")["selected_ids"] != ids:
                    raise ValueError("a different selection was already submitted")
                return self.respond(200, {"status": status})
            if status != "awaiting_selection":
                raise ValueError("not awaiting selection")
            write_json(incident / "selection.json", {"format_version": 2,
                       "plan_sha256": digest(self.server.plan), "selected_ids": ids,
                       "selected_items": [indexed[i] for i in ids]})
            set_status(incident, "reviewing")
            self.server.background(self.server.review)
        elif self.path == "/confirm":
            if payload or status != "awaiting_confirmation":
                raise ValueError("not awaiting explicit confirmation")
            selection = read_json(incident / "selection.json")
            write_json(incident / "confirmation.json", {"confirmed_at": time.time(),
                       "selection_sha256": digest(selection), "source": "local-review-page"})
            set_status(incident, "applying")
            self.server.background(self.server.apply)
        elif self.path == "/cancel":
            if payload or status not in {"awaiting_selection", "awaiting_confirmation"}:
                raise ValueError("cannot cancel during an operation")
            set_status(incident, "cancelled")
        else:
            return self.respond(404, {"error": "not found"})
        return self.respond(200, {"ok": True})


def serve(context, incident, opener=None):
    if not context.allowed("agent_plan"):
        raise ValueError("agent-plan consent revoked or responses paused")
    with context.lock("page-" + incident.name) as locked:
        if not locked:
            raise ValueError("page is already open")
        server = ReviewServer(context, incident)
        server.timeout = 0.5
        url = server.origin + "/?" + server.token
        write_json(incident / "page.json", {"url": url, "expires_at": server.plan["created_at"] + 3600})
        if time.time() - server.plan["created_at"] > 3600:
            server.server_close()
            raise ValueError("plan expired; use explicit retry to rescan")
        try:
            if opener is None:
                subprocess.run(["/usr/bin/open", url], check=True, timeout=10)
            else:
                opener(url)
            print(f"Cleanup review page opened: {url}", flush=True)
            while time.time() - server.plan["created_at"] <= 3600:
                server.handle_request()
            current = read_json(incident / "status.json")["status"]
            if current in {"awaiting_selection", "awaiting_confirmation"}:
                set_status(incident, "expired")
        finally:
            server.server_close()
            for thread in server.workers:
                thread.join(timeout=610)
