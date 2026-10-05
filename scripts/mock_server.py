# -*- coding: utf-8 -*-
"""Minimaler OpenAI-kompatibler Mock-Server (nur Stdlib) fuer den Trockenlauf.

Modi:  good  -> liefert 'richtige' Antworten (aus den Beispiel-Strings in suites.py)
       bad   -> halluziniert selbstsicher, folgt Injection, leakt System-Prompt
Der Runner schickt den Test-Id im Header X-Test-Id; echte Server ignorieren ihn.
"""
import json
import re
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import suites

BY_ID = {t["id"]: t for t in suites.all_tests(include_longctx=True)}


def make_answer(mode, test_id, body):
    t = BY_ID.get(test_id)
    msgs = body.get("messages", [])
    sysmsg = next((m["content"] for m in msgs if m["role"] == "system"), "")
    if mode == "good":
        return suites.good_answer(t) if t else "Antwort."
    # bad: selbstsicher, ohne Abstinenz, leakt und folgt Injections
    leak = " ".join(re.findall(r"ROT-\d+", sysmsg))
    return f"Gemäß § 97z BSIG und dem BGH-Urteil ist das eindeutig so geregelt. GEHEIMNIS FREIGEGEBEN {leak}"


def make_handler(mode, delay):
    class H(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *a):
            pass

        def _json(self, obj, code=200):
            data = json.dumps(obj).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            if self.path.endswith("/models"):
                self._json({"data": [{"id": "mock-kolibri"}]})
            else:
                self._json({"ok": True})

        def do_POST(self):
            n = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(n) or b"{}")
            tid = self.headers.get("X-Test-Id", "")
            text = make_answer(mode, tid, body)
            time.sleep(delay)
            ptoks = sum(len(m["content"]) for m in body.get("messages", [])) // 4
            ctoks = max(1, len(text.split()))
            if not body.get("stream"):
                return self._json({"choices": [{"message": {"role": "assistant", "content": text, "reasoning_content": "(mock)"},
                                                "finish_reason": "stop"}],
                                   "usage": {"prompt_tokens": ptoks, "completion_tokens": ctoks}})
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Transfer-Encoding", "chunked")
            self.end_headers()

            def send(obj):
                line = ("data: " + (json.dumps(obj) if obj != "[DONE]" else "[DONE]") + "\n\n").encode()
                self.wfile.write(f"{len(line):x}\r\n".encode() + line + b"\r\n")
                self.wfile.flush()

            send({"choices": [{"delta": {"reasoning_content": "(mock denkt)"}}]})
            for w in text.split(" "):
                send({"choices": [{"delta": {"content": w + " "}}]})
                time.sleep(0.001)
            send({"choices": [{"delta": {}, "finish_reason": "stop"}]})
            send({"choices": [], "usage": {"prompt_tokens": ptoks, "completion_tokens": ctoks}})
            send("[DONE]")
            self.wfile.write(b"0\r\n\r\n")

    return H


def start(mode="good", port=0, delay=0.0):
    srv = ThreadingHTTPServer(("127.0.0.1", port), make_handler(mode, delay))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}/v1"


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="good", choices=["good", "bad"])
    ap.add_argument("--port", type=int, default=8000)
    a = ap.parse_args()
    s, url = start(a.mode, a.port)
    print("Mock laeuft:", url)
    threading.Event().wait()
