#!/usr/bin/env python3
"""FYP Project Organiser — local manager server"""
import json, os, subprocess, sys, time, threading, webbrowser
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

BASE = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent
PORT = 8765

PROJECTS = [
    {
        "id": "antigravity-yapping", "name": "Antigravity Yapping",
        "icon": "💬", "color": "#7c3aed", "category": "web",
        "tech": ["React", "Node.js", "Vite"], "size": "160 MB",
        "github": "https://github.com/abcdanman/Outbound-UM",
        "desc": "Social chat web app with React frontend and Node.js backend.",
        "commands": [
            {"cwd": "Antigravity Yapping/backend", "run": "node index.js"},
            {"cwd": "Antigravity Yapping/frontend", "run": "npm run dev"},
        ],
        "url": "http://localhost:5173",
    },
    {
        "id": "testing-yapping", "name": "Testing Yapping (SOP)",
        "icon": "🧪", "color": "#0891b2", "category": "web",
        "tech": ["React", "Express", "Supabase"], "size": "76 MB",
        "github": "https://github.com/abcdanman/sop-app",
        "desc": "Standard Operating Procedure management app.",
        "commands": [
            {"cwd": "Testing yapping/backend", "run": "node server.js"},
            {"cwd": "Testing yapping/frontend", "run": "npm run dev"},
        ],
        "url": "http://localhost:5173",
    },
    {
        "id": "jomcuti-app", "name": "JomCuti App",
        "icon": "🏖️", "color": "#f59e0b", "category": "web",
        "tech": ["Next.js 15", "TypeScript", "Tailwind"], "size": "693 MB",
        "github": "https://github.com/abcdanman/jomcuti-app",
        "desc": "Leave and holiday management web app.",
        "commands": [
            {"cwd": "jomcuti-app", "run": "npm run dev"},
        ],
        "url": "http://localhost:3000",
    },
    {
        "id": "um-eagle-eye", "name": "UM Eagle Eye (EBSI)",
        "icon": "👁️", "color": "#8b5cf6", "category": "web",
        "tech": ["Cloudflare Workers", "EBSI"], "size": "868 MB",
        "github": "https://github.com/ndriannazriel/UMEagleEye-FORKED-FOR-EBSI",
        "desc": "Blockchain credential verification using EBSI.",
        "type": "cloudflare",
    },
    {
        "id": "game", "name": "Game (Meme Master)",
        "icon": "🎮", "color": "#10b981", "category": "web",
        "tech": ["HTML", "CSS", "JavaScript"], "size": "0.2 MB",
        "github": "https://github.com/abcdanman/Meme-Master",
        "desc": "Browser-based meme game with multiplayer.",
        "type": "static",
        "url": str(BASE / "Game" / "index.html"),
    },
    {
        "id": "snapchallenge", "name": "Snap Challenge",
        "icon": "📸", "color": "#ec4899", "category": "mobile",
        "tech": ["Flutter", "Firebase"], "size": "1.2 GB",
        "github": "https://github.com/zhanas12/snapchallenge",
        "desc": "Daily photo challenge community mobile app.",
        "commands": [{"cwd": "snapchallenge", "run": "flutter run"}],
        "note": "Requires Flutter SDK and Android emulator.",
    },
    {
        "id": "um-waze", "name": "UM Waze",
        "icon": "🗺️", "color": "#0284c7", "category": "mobile",
        "tech": ["React Native", "Expo"], "size": "362 MB",
        "github": "https://github.com/fidelismee/um-waze",
        "desc": "University of Malaya campus navigation app.",
        "commands": [{"cwd": "um-waze", "run": "npx expo start"}],
        "url": "http://localhost:8081",
    },
    {
        "id": "otonoco-compliance", "name": "Otonoco Compliance",
        "icon": "✅", "color": "#6366f1", "category": "tools",
        "tech": ["Python", "FastAPI", "AI"], "size": "<1 MB",
        "github": "https://github.com/abcdanman/otonoco-compliance",
        "desc": "AI-powered compliance document agent.",
        "commands": [{"cwd": "Otonoco Compliance/compliance_agent", "run": "python main.py"}],
        "url": "http://localhost:8000",
    },
    {
        "id": "dr-trader", "name": "Dr Trader",
        "icon": "📈", "color": "#ef4444", "category": "tools",
        "tech": ["Python"], "size": "0.2 MB",
        "github": "https://github.com/abcdanman/Dr-Trader",
        "desc": "Trading alert and monitoring tool.",
        "commands": [{"cwd": "Dr Trader", "run": "python check_alerts.py"}],
    },
    {
        "id": "game-optimizer", "name": "Game Optimizer",
        "icon": "⚡", "color": "#d97706", "category": "tools",
        "tech": ["Python", "Tkinter"], "size": "0.2 MB",
        "github": "https://github.com/abcdanman/game-optimizer",
        "desc": "Windows game performance optimiser with GUI.",
        "commands": [{"cwd": "Game Optimizer", "run": "python game_optimizer.py"}],
    },
    {
        "id": "storage-cleaner", "name": "Storage Cleaner",
        "icon": "🧹", "color": "#64748b", "category": "tools",
        "tech": ["Python"], "size": "0.1 MB",
        "github": "https://github.com/abcdanman/storage-cleaner",
        "desc": "Utility to identify and clean Windows storage.",
        "commands": [{"cwd": "Storage Cleaner", "run": "python storage_cleaner.py"}],
    },
    {
        "id": "gmail-bot", "name": "Gmail Bot",
        "icon": "📧", "color": "#dc2626", "category": "tools",
        "tech": ["Python", "Gmail API", "MCP"], "size": "<1 MB",
        "github": "https://github.com/abcdanman/Gmail-Bot",
        "desc": "Gmail automation with MCP server integration.",
        "commands": [{"cwd": "Gmail bot", "run": "python gmail_cleaner_mcp.py"}],
    },
    {
        "id": "telegram-wakeup", "name": "Telegram Wake Up",
        "icon": "⏰", "color": "#0ea5e9", "category": "tools",
        "tech": ["HTML", "Telegram Bot API"], "size": "<1 MB",
        "github": "https://github.com/abcdanman/wake-up-alert",
        "desc": "Wake-up alert config via Telegram bot.",
        "type": "static",
        "url": str(BASE / "Telegram wake up" / "config-form.html"),
    },
]

running = {}  # project_id -> [Popen, ...]


def start_project(pid):
    if pid in running:
        return {"ok": False, "error": "Already running"}
    proj = next((p for p in PROJECTS if p["id"] == pid), None)
    if not proj:
        return {"ok": False, "error": "Not found"}

    ptype = proj.get("type", "")

    if ptype == "static":
        url = proj.get("url", "")
        webbrowser.open(Path(url).as_uri() if not url.startswith("http") else url)
        return {"ok": True, "static": True}

    if ptype == "cloudflare":
        return {"ok": False, "error": "Deploy with: wrangler deploy"}

    cmds = proj.get("commands", [])
    if not cmds:
        return {"ok": False, "error": "No commands defined"}

    procs = []
    flags = subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
    for c in cmds:
        cwd = str(BASE / c["cwd"])
        if not Path(cwd).exists():
            return {"ok": False, "error": f"Folder not found: {c['cwd']}"}
        try:
            p = subprocess.Popen(
                c["run"], cwd=cwd, shell=True,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                creationflags=flags,
            )
            procs.append(p)
            time.sleep(0.3)
        except Exception as e:
            return {"ok": False, "error": str(e)}

    running[pid] = procs

    url = proj.get("url")
    if url and url.startswith("http"):
        def _open():
            time.sleep(4)
            webbrowser.open(url)
        threading.Thread(target=_open, daemon=True).start()

    return {"ok": True}


def stop_project(pid):
    if pid not in running:
        return {"ok": False, "error": "Not running"}
    for p in running[pid]:
        try:
            if os.name == "nt":
                subprocess.call(
                    ["taskkill", "/F", "/T", "/PID", str(p.pid)],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                )
            else:
                import signal as _s
                os.killpg(os.getpgid(p.pid), _s.SIGTERM)
        except Exception:
            pass
    del running[pid]
    return {"ok": True}


def get_status():
    status = {}
    for pid in list(running.keys()):
        alive = [p for p in running[pid] if p.poll() is None]
        if not alive:
            del running[pid]
        else:
            running[pid] = alive
            status[pid] = "running"
    return status


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _json(self, data, code=200):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _file(self, name):
        p = HERE / name
        if not p.exists():
            self.send_error(404)
            return
        data = p.read_bytes()
        ct = "text/html; charset=utf-8" if name.endswith(".html") else "text/plain"
        self.send_response(200)
        self.send_header("Content-Type", ct)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/status":
            self._json({"running": get_status(), "projects": PROJECTS})
        elif path in ("/", "/index.html"):
            self._file("index.html")
        else:
            self.send_error(404)

    def do_POST(self):
        path = urlparse(self.path).path
        parts = [x for x in path.strip("/").split("/") if x]

        if len(parts) == 3 and parts[:2] == ["api", "start"]:
            self._json(start_project(parts[2]))
        elif len(parts) == 3 and parts[:2] == ["api", "stop"]:
            self._json(stop_project(parts[2]))
        elif path == "/api/shutdown":
            self._json({"ok": True})
            threading.Thread(target=lambda: (time.sleep(0.5), os._exit(0)), daemon=True).start()
        else:
            self.send_error(404)


if __name__ == "__main__":
    print(f"  FYP Project Organiser  ->  http://localhost:{PORT}")
    try:
        httpd = ThreadingHTTPServer(("localhost", PORT), Handler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
