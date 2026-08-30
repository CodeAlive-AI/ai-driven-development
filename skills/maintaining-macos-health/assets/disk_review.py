"""Loopback-only selection + confirmation. Submit never authorizes deletion."""
from __future__ import annotations

import html
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


def page(plan, token):
    rows = []
    for item in plan["items"]:
        value = html.escape(item["id"], quote=True)
        rows.append(f'<label class="item"><input type="checkbox" value="{value}">'
                    f'<span><strong>{html.escape(item["label"])}</strong>'
                    f'<small>{html.escape(item["path"])}</small>'
                    f'<p>{html.escape(item["description"])}</p>'
                    f'<small>{html.escape(item["warning"])} · {item["age_days"]} days old</small></span>'
                    f'<b>{item["size_bytes"] / 1024**3:.2f} GiB</b></label>')
    document = '''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Disk cleanup review</title><style>
body{font:16px system-ui;background:#f5f4f0;color:#202922;max-width:1000px;margin:40px auto;padding:0 24px}
h1{font-size:36px;margin-bottom:12px}p{line-height:1.5}.item{display:flex;gap:18px;padding:20px 0;border-top:1px solid #ccd0c9}
.item span{flex:1;min-width:0}small{display:block;overflow-wrap:anywhere;color:#58605a;margin:6px 0}
input{width:20px;height:20px}button{font:inherit;padding:12px 18px;margin:8px 8px 8px 0;cursor:pointer}
#confirm{background:#84322e;color:white;border:0}#summary{white-space:pre-wrap;background:white;padding:20px}
.note{border-left:4px solid #aa7c2e;padding-left:16px}#state{font-weight:600}button:disabled{opacity:.5;cursor:default}
</style><h1>Review disk cleanup</h1><p class="note">Nothing is selected by default. Submit sends your selection for review; it does not delete files.
Only the later “Confirm permanent deletion” button authorizes deletion. Unchecked files will be preserved.</p>
<p>Scope: package download caches and old installer/archive files directly in Downloads. This is not a full-disk audit.</p>
<p id="state" role="status">Awaiting selection</p><div id="summary">__SUMMARY__</div>
<section id="items">__ITEMS__</section><p id="total">0 selected</p>
<button id="submit">Submit selection for review</button><button id="cancel">Cancel</button>
<button id="confirm" hidden>Confirm permanent deletion</button>
<script>
const token=__TOKEN__, checkboxes=[...document.querySelectorAll('input[type=checkbox]')];
const sizes=__SIZES__; let status='awaiting_selection';
function selected(){return checkboxes.filter(x=>x.checked).map(x=>x.value)}
function totals(){const ids=selected();document.querySelector('#total').textContent=
  ids.length+' selected · '+(ids.reduce((s,id)=>s+sizes[id],0)/1024**3).toFixed(2)+' GiB';}
checkboxes.forEach(x=>x.addEventListener('change',totals));
async function request(action,payload={}){
 const response=await fetch('/'+action,{method:'POST',headers:{'Content-Type':'application/json','X-Cleanup-Token':token},body:JSON.stringify(payload)});
 const body=await response.json(); if(!response.ok)throw Error(body.error||response.status);return body;
}
function error(e){document.querySelector('#state').textContent=e.message}
document.querySelector('#submit').onclick=async()=>{
 const ids=selected();if(!ids.length)return;document.querySelector('#submit').disabled=true;
 try{await request('submit',{selected_ids:ids});await refresh()}catch(e){error(e);document.querySelector('#submit').disabled=false;}
};
document.querySelector('#cancel').onclick=async()=>{try{await request('cancel');await refresh()}catch(e){error(e)}};
document.querySelector('#confirm').onclick=async()=>{
 if(!window.confirm('Permanently delete ONLY the selected files? This cannot be undone.'))return;
 document.querySelector('#confirm').disabled=true;
 try{await request('confirm');await refresh()}catch(e){error(e)}
};
async function refresh(){
 const response=await fetch('/status',{headers:{'X-Cleanup-Token':token}}); const data=await response.json();
 if(!response.ok)throw Error(data.error||response.status);
 status=data.status;document.querySelector('#state').textContent=status+(data.error?' — '+data.error:'');
 if(data.review)document.querySelector('#summary').textContent=data.review;
 if(data.selected_ids){checkboxes.forEach(x=>x.checked=data.selected_ids.includes(x.value));totals()}
 checkboxes.forEach(x=>x.disabled=status!=='awaiting_selection');
 document.querySelector('#submit').disabled=status!=='awaiting_selection';
 document.querySelector('#confirm').hidden=status!=='awaiting_confirmation';
 document.querySelector('#cancel').disabled=['applying','completed','cancelled','failed','expired'].includes(status);
 if(data.before&&data.after)document.querySelector('#summary').textContent+='\\nMeasured free space: '+
 (data.before[0]/1024**3).toFixed(2)+' → '+(data.after[0]/1024**3).toFixed(2)+' GiB';
}
setInterval(()=>refresh().catch(error),1500);refresh().catch(error);
</script></html>'''
    # JSON cannot break out of the script element, even with hostile filenames.
    return document.replace("__SUMMARY__", html.escape(plan["summary"])).replace("__ITEMS__", "".join(rows)).replace(
        "__TOKEN__", json.dumps(token)).replace("__SIZES__", json.dumps({row["id"]: row["size_bytes"]
        for row in plan["items"]}).replace("<", "\\u003c"))


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
            if set(payload) != {"selected_ids"}:
                raise ValueError("only selected_ids accepted")
            ids = payload["selected_ids"]
            indexed = {row["id"]: row for row in self.server.plan["items"]}
            if (not isinstance(ids, list) or not ids or any(not isinstance(i, str) for i in ids)
                    or len(set(ids)) != len(ids) or any(i not in indexed for i in ids)):
                raise ValueError("unknown/duplicate/empty selected IDs")
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
