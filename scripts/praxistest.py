#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Praxistest-Runner fuer Kolibri-1 (oder jeden OpenAI-kompatiblen Endpoint). Nur Stdlib.

  praxistest.py run     --base-url http://localhost:8000/v1 --model Aleph-Alpha/Kolibri-1 --out res_kolibri
  praxistest.py report  res_kolibri
  praxistest.py load    --base-url ... --model ... --concurrency 1,4,16
  praxistest.py blind   res_kolibri res_andere  --out blind
  praxistest.py unblind blind
  praxistest.py selftest
"""
import argparse
import csv
import json
import os
import random
import statistics
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import re
import suites
import suites2


# ------------------------------------------------------------------ HTTP
def _default_context_dir():
    here = os.path.dirname(os.path.abspath(__file__))
    for p in (os.path.join(here, "context"), os.path.join(here, "..", "context")):
        if os.path.isdir(p):
            return p
    return os.path.join(here, "context")


def chat(base_url, model, messages, test_id="", api_key="", max_tokens=1024, temperature=1.0,
         top_p=0.97, top_k=128, effort=None, timeout=900):
    """Streaming-Chat; misst TTFT und Tokens. Gibt dict zurueck (nie Exception)."""
    body = {"model": model, "messages": messages, "max_tokens": max_tokens, "temperature": temperature,
            "top_p": top_p, "stream": True, "stream_options": {"include_usage": True}}
    if top_k and top_k > 0:
        body["top_k"] = top_k  # vLLM-Erweiterung; andere APIs ignorieren/lehnen ab -> --top-k 0
    if effort:
        # ANNAHME laut Model Card: Chat-Template-Parameter reasoning_effort / enable_thinking
        body["chat_template_kwargs"] = ({"enable_thinking": False} if effort == "none"
                                        else {"enable_thinking": True, "reasoning_effort": effort})
    headers = {"Content-Type": "application/json", "X-Test-Id": test_id}
    if api_key:
        headers["Authorization"] = "Bearer " + api_key
    req = urllib.request.Request(base_url.rstrip("/") + "/chat/completions", json.dumps(body).encode(), headers)
    t0 = time.time()
    ttft = None
    content, reasoning, usage, finish, err = [], [], {}, None, None
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            for raw in r:
                line = raw.decode("utf-8", "replace").strip()
                if not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                ch = json.loads(data)
                if ch.get("usage"):
                    usage = ch["usage"]
                for c in ch.get("choices", []):
                    d = c.get("delta", {})
                    piece = d.get("content")
                    rpiece = d.get("reasoning_content") or d.get("reasoning")
                    if (piece or rpiece) and ttft is None:
                        ttft = time.time() - t0
                    if piece:
                        content.append(piece)
                    if rpiece:
                        reasoning.append(rpiece)
                    if c.get("finish_reason"):
                        finish = c["finish_reason"]
    except urllib.error.HTTPError as e:
        err = f"HTTP {e.code}: {e.read()[:300].decode('utf-8', 'replace')}"
    except Exception as e:  # Netzwerk, Timeout, JSON
        err = f"{type(e).__name__}: {e}"
    dt = time.time() - t0
    ctoks = usage.get("completion_tokens") or 0
    gen_time = dt - (ttft or 0)
    return dict(response="".join(content), reasoning="".join(reasoning), latency=round(dt, 3),
                ttft=round(ttft, 3) if ttft is not None else None, prompt_tokens=usage.get("prompt_tokens"),
                completion_tokens=ctoks, tok_s=round(ctoks / gen_time, 1) if ctoks and gen_time > 0 else None,
                finish_reason=finish, error=err)


# ------------------------------------------------------------------ run
def cmd_run(a):
    if getattr(a, "system_file", ""):
        with open(a.system_file, encoding="utf-8-sig") as sf:
            a.system = sf.read().strip()
    tests = suites.all_tests(a.longctx, tuple(int(x) for x in a.longctx_sizes.split(",")))
    if a.suite == "all":
        pass
    elif a.suite:
        want = set(a.suite.split(","))
        tests = [t for t in tests if t["suite"] in want]
    else:  # Standard = Runde 1; Zusatz-Suiten nur explizit (--suite rag,praxis,inject oder all)
        tests = [t for t in tests if t["suite"] not in suites2.EXTRA_SUITES]
    ctx_cache = {}

    def fill(prompt):
        def rep(m):
            fn = m.group(1)
            if fn not in ctx_cache:
                with open(os.path.join(a.context_dir, fn), encoding="utf-8") as cf:
                    ctx_cache[fn] = cf.read()
            return ctx_cache[fn]
        return re.sub(r"\{\{CONTEXT:([\w.\-]+)\}\}", rep, prompt)
    if a.limit:
        tests = tests[:a.limit]
    os.makedirs(a.out, exist_ok=True)
    api_key = os.environ.get(a.api_key_env, "") if a.api_key_env else ""
    meta = dict(base_url=a.base_url, model=a.model, effort=a.effort, system=a.system, temperature=a.temperature, top_p=a.top_p,
                top_k=a.top_k, max_tokens=a.max_tokens, repeats=a.repeats, ts=time.strftime("%Y-%m-%d %H:%M:%S"))
    with open(os.path.join(a.out, "meta.json"), "w", encoding="utf-8") as mf:
        json.dump(meta, mf, indent=1, ensure_ascii=False)

    def one(job):
        t, rep = job
        sysmsg = "\n\n".join(x for x in (a.system, t.get("system")) if x)
        msgs = ([{"role": "system", "content": sysmsg}] if sysmsg else []) + \
               [{"role": "user", "content": fill(t["prompt"])}]
        r = chat(a.base_url, a.model, msgs, t["id"], api_key, a.max_tokens, a.temperature, a.top_p, a.top_k, a.effort)
        s, det = suites.score(t, r["response"])
        return dict(id=t["id"], rep=rep, suite=t["suite"], title=t["title"], prompt=t["prompt"][:4000],
                    key=t["key"], score=s, checks=det, **r)

    jobs = [(t, i) for t in tests for i in range(a.repeats)]
    path = os.path.join(a.out, "results.jsonl")
    n_err = 0
    with open(path, "w", encoding="utf-8") as f, ThreadPoolExecutor(a.workers) as ex:
        for res in ex.map(one, jobs):
            f.write(json.dumps(res, ensure_ascii=False) + "\n")
            f.flush()
            n_err += bool(res["error"])
            sc = "manuell" if res["score"] is None else f"{res['score']:.2f}"
            print(f"{res['id']:<16} {sc:>8}  {res['latency']:>6.1f}s  {res['tok_s'] or '-':>6} tok/s  {res['error'] or ''}")
    print(f"\nFertig: {len(jobs)} Läufe, {n_err} Fehler -> {path}")
    cmd_report(argparse.Namespace(dir=a.out))
    return 1 if n_err == len(jobs) else 0


# ------------------------------------------------------------------ report
def load_results(d):
    p = os.path.join(d, "results.jsonl")
    try:
        txt = open(p, encoding="utf-8").read()
    except UnicodeDecodeError:  # Dateien aus aelterer Version, unter Windows als cp1252 geschrieben
        txt = open(p, encoding="cp1252", errors="replace").read()
    return [json.loads(l) for l in txt.splitlines() if l.strip()]


def _med(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.median(xs), 2) if xs else None


def cmd_report(a):
    rows = load_results(a.dir)
    meta = json.load(open(os.path.join(a.dir, "meta.json"), encoding="utf-8", errors="replace"))
    lines = [f"# Praxistest-Report", "", f"Modell: `{meta['model']}` · Endpoint: `{meta['base_url']}` · effort: {meta.get('effort')} · {meta['ts']}",
             "", "> Stichprobe, kein Benchmark. Antwortschlüssel nicht anwaltlich geprüft. Regex-Checks sind grob – siehe review.csv.", "",
             "| Suite | Läufe | Auto-Score Ø | Fehler | TTFT med (s) | tok/s med |", "|---|---|---|---|---|---|"]
    for s in sorted({r["suite"] for r in rows}):
        rs = [r for r in rows if r["suite"] == s]
        sc = [r["score"] for r in rs if r["score"] is not None]
        lines.append(f"| {s} | {len(rs)} | {round(sum(sc)/len(sc), 2) if sc else 'manuell'} | {sum(bool(r['error']) for r in rs)} | "
                     f"{_med([r['ttft'] for r in rs])} | {_med([r['tok_s'] for r in rs])} |")
    ab = [r for r in rows if r["suite"] == "abstain" and r["score"] is not None]
    if ab:
        lines += ["", f"**Abstinenzrate** (hat Nichtwissen signalisiert): {sum(r['score'] == 1 for r in ab)}/{len(ab)}"]
    fails = [r for r in rows if r["score"] is not None and r["score"] < 1]
    lines += ["", "## Nicht bestanden / teilweise", ""]
    for r in fails:
        bad = [n for n, ok in r["checks"] if not ok]
        lines.append(f"- **{r['id']}** ({r['title']}) Score {r['score']:.2f} – fehlgeschlagen: {', '.join(bad)}")
    if not fails:
        lines.append("- keine")
    empty = [r["id"] for r in rows if not r["response"].strip() and not r["error"]]
    if empty:
        lines += ["", f"⚠ **Leere Antwort** (meist: Reasoning hat max_tokens aufgebraucht – `--max-tokens` erhöhen oder `--effort low/none`): {', '.join(empty)}"]
    trunc = [r["id"] for r in rows if r["finish_reason"] == "length"]
    if trunc:
        lines += ["", f"⚠ Abgeschnitten (max_tokens erreicht, ggf. Reasoning): {', '.join(trunc)}"]
    open(os.path.join(a.dir, "report.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    with open(os.path.join(a.dir, "review.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "suite", "titel", "auto_score", "frage", "antwort", "schluessel", "bewertung_1-5", "notiz"])
        for r in rows:
            w.writerow([r["id"], r["suite"], r["title"], "" if r["score"] is None else round(r["score"], 2),
                        r["prompt"][:600], r["response"], r["key"], "", ""])
    print("\n".join(lines))
    print(f"\n-> {a.dir}/report.md, {a.dir}/review.csv")


# ------------------------------------------------------------------ rescore
def cmd_rescore(a):
    """Bewertet vorhandene Ergebnisse mit den aktuellen Checks neu (kein Server noetig)."""
    by_id = {t["id"]: t for t in suites.all_tests(include_longctx=True)}
    rows = load_results(a.dir)
    import shutil
    shutil.copy(os.path.join(a.dir, "results.jsonl"), os.path.join(a.dir, "results.jsonl.bak"))
    changed = 0
    for r in rows:
        t = by_id.get(r["id"])
        if not t:
            continue
        s, det = suites.score(t, r["response"])
        changed += (s != r["score"])
        r["score"], r["checks"] = s, det
    with open(os.path.join(a.dir, "results.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{changed} von {len(rows)} Scores geaendert (Sicherung: results.jsonl.bak)")
    cmd_report(argparse.Namespace(dir=a.dir))


# ------------------------------------------------------------------ load
def cmd_load(a):
    api_key = os.environ.get(a.api_key_env, "") if a.api_key_env else ""
    prompt = "Erkläre in ca. 200 Wörtern, was ein Mixture-of-Experts-Modell ist und welche Vor- und Nachteile es beim Serving hat."
    max_tok = a.max_tokens
    if a.doc_tokens:  # realistisch: langes Dokument + kurze Antwort (Prefill-lastig)
        max_tok = min(a.max_tokens, 400)
    out = []
    print("conc  req  agg_tok/s  p50_lat  p95_lat  ttft_med  err")
    for c in [int(x) for x in a.concurrency.split(",")]:
        n = max(a.requests, c)
        t0 = time.time()
        with ThreadPoolExecutor(c) as ex:
            def mk(i):
                if not a.doc_tokens:
                    return prompt + " " * i
                body = suites._FILL * max(1, a.doc_tokens * 4 // len(suites._FILL))
                head = "" if a.shared_prefix else f"[Vorgang {i}-{time.time():.3f}] "  # eindeutig -> kein Prefix-Cache
                return head + "Dokument:\n" + body + "\n\nFasse das Dokument in fünf Stichpunkten zusammen."
            rs = list(ex.map(lambda i: chat(a.base_url, a.model, [{"role": "user", "content": mk(i)}], "load", api_key,
                                            max_tok, a.temperature, a.top_p, a.top_k, a.effort), range(n)))
        wall = time.time() - t0
        ok = [r for r in rs if not r["error"]]
        toks = sum(r["completion_tokens"] or 0 for r in ok)
        lat = sorted(r["latency"] for r in ok) or [0]
        row = dict(concurrency=c, requests=n, agg_tok_s=round(toks / wall, 1), p50=round(statistics.median(lat), 2),
                   p95=round(lat[min(len(lat) - 1, int(len(lat) * .95))], 2), ttft_med=_med([r["ttft"] for r in ok]),
                   errors=n - len(ok))
        out.append(row)
        print(f"{c:<5} {n:<4} {row['agg_tok_s']:<10} {row['p50']:<8} {row['p95']:<8} {row['ttft_med']!s:<9} {row['errors']}")
    if a.out:
        json.dump(out, open(a.out, "w"), indent=1)


# ------------------------------------------------------------------ blind A/B
def cmd_blind(a):
    A = {r["id"]: r for r in load_results(a.dir_a) if r["suite"] == "alltag"}
    B = {r["id"]: r for r in load_results(a.dir_b) if r["suite"] == "alltag"}
    ids = sorted(set(A) & set(B))
    if not ids:
        sys.exit("Keine gemeinsamen alltag-Tests.")
    os.makedirs(a.out, exist_ok=True)
    rng = random.Random(a.seed)
    key = {}
    with open(os.path.join(a.out, "blind.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "frage", "antwort_X", "antwort_Y", "besser(X/Y/gleich)", "notiz"])
        for i in ids:
            flip = rng.random() < 0.5
            key[i] = {"X": "b" if flip else "a", "Y": "a" if flip else "b"}
            x, y = (B[i], A[i]) if flip else (A[i], B[i])
            w.writerow([i, A[i]["prompt"], x["response"], y["response"], "", ""])
    json.dump(dict(a=a.dir_a, b=a.dir_b, key=key), open(os.path.join(a.out, "blind_key.json"), "w", encoding="utf-8"), indent=1)
    print(f"Blind-Datei: {a.out}/blind.csv – ausfüllen, dann: praxistest.py unblind {a.out}")


def cmd_unblind(a):
    key = json.load(open(os.path.join(a.dir, "blind_key.json")))
    cnt = {"a": 0, "b": 0, "gleich": 0}
    for row in csv.DictReader(open(os.path.join(a.dir, "blind.csv"), encoding="utf-8"), delimiter=";"):
        v = (row["besser(X/Y/gleich)"] or "").strip().upper()
        if v in ("X", "Y"):
            cnt[key["key"][row["id"]][v]] += 1
        elif v:
            cnt["gleich"] += 1
    print(f"A ({key['a']}): {cnt['a']} | B ({key['b']}): {cnt['b']} | gleich: {cnt['gleich']}")
    print("Hinweis: 5 Prompts sind Anekdote, keine Statistik.")


# ------------------------------------------------------------------ selftest
def cmd_selftest(a):
    import mock_server
    results = {}
    for mode in ("good", "bad"):
        srv, url = mock_server.start(mode)
        out = os.path.join(a.tmp, f"selftest_{mode}")
        ns = argparse.Namespace(base_url=url, model="mock", suite="all", limit=0, out=out, longctx=True, longctx_sizes="8000",
                                repeats=1, workers=4, max_tokens=256, temperature=1.0, top_p=0.97, top_k=128,
                                effort="low", api_key_env="", system="",
                                context_dir=_default_context_dir())
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            cmd_run(ns)
        rows = load_results(out)
        sc = [r["score"] for r in rows if r["score"] is not None]
        results[mode] = sum(sc) / len(sc)
        assert all(not r["error"] for r in rows), [r["error"] for r in rows if r["error"]]
        assert os.path.exists(os.path.join(out, "review.csv"))
        srv.shutdown()
    print(f"selftest: good={results['good']:.2f} bad={results['bad']:.2f}")
    assert results["good"] > 0.95, "Checks akzeptieren die guten Antworten nicht"
    assert results["bad"] < 0.45, "Checks erkennen schlechte Antworten nicht"
    # Blind-Export Test
    srv, url = mock_server.start("good")
    srv.shutdown()
    cmd_blind(argparse.Namespace(dir_a=os.path.join(a.tmp, "selftest_good"), dir_b=os.path.join(a.tmp, "selftest_bad"),
                                 out=os.path.join(a.tmp, "selftest_blind"), seed=1))
    print("selftest OK")


def main():
    try:  # Windows-Konsole (cp1252) darf bei Sonderzeichen wie U+26A0 nicht abstuerzen
        sys.stdout.reconfigure(errors="replace")
        sys.stderr.reconfigure(errors="replace")
    except Exception:
        pass
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    def common(q):
        q.add_argument("--base-url", default="http://localhost:8000/v1")
        q.add_argument("--model", default="Aleph-Alpha/Kolibri-1")
        q.add_argument("--api-key-env", default="", help="Name der Umgebungsvariable mit dem API-Key")
        q.add_argument("--effort", default="", choices=["", "none", "low", "medium", "high"],
                       help="reasoning_effort via chat_template_kwargs (leer = Server-Default)")
        q.add_argument("--temperature", type=float, default=1.0)
        q.add_argument("--top-p", type=float, default=0.97)
        q.add_argument("--top-k", type=int, default=128, help="0 = nicht senden")
        q.add_argument("--max-tokens", type=int, default=6000, help="inkl. Reasoning-Tokens!")

    r = sp.add_parser("run"); common(r)
    r.add_argument("--out", default="results")
    r.add_argument("--system", default="", help="globaler System-Prompt, z. B. Datum + Ehrlichkeitsregel")
    r.add_argument("--system-file", default="", help="System-Prompt aus UTF-8-Datei (vermeidet Umlaut-Probleme der Windows-Konsole)")
    r.add_argument("--suite", default="", help="kommagetrennt: nis2,kanzlei,itdl,abstain,security,souveraenitaet,alltag,longctx")
    r.add_argument("--limit", type=int, default=0)
    r.add_argument("--context-dir", default=_default_context_dir(),
                   help="Ordner mit Gesetzestexten fuer die rag-Suite")
    r.add_argument("--repeats", type=int, default=1)
    r.add_argument("--workers", type=int, default=2)
    r.add_argument("--longctx", action="store_true", help="Needle-Tests dazunehmen (grosse Prompts!)")
    r.add_argument("--longctx-sizes", default="8000,32000,128000")
    r.set_defaults(f=cmd_run)
    s = sp.add_parser("report"); s.add_argument("dir"); s.set_defaults(f=cmd_report)
    rs = sp.add_parser("rescore"); rs.add_argument("dir"); rs.set_defaults(f=cmd_rescore)
    l = sp.add_parser("load"); common(l)
    l.add_argument("--concurrency", default="1,4,16")
    l.add_argument("--requests", type=int, default=16)
    l.add_argument("--out", default="")
    l.add_argument("--doc-tokens", type=int, default=0, help="langes Dokument je Anfrage (ca. Token), z. B. 8000")
    l.add_argument("--shared-prefix", action="store_true", help="identisches Dokument-Praefix (Prefix-Cache darf greifen)")
    l.set_defaults(f=cmd_load)
    b = sp.add_parser("blind"); b.add_argument("dir_a"); b.add_argument("dir_b")
    b.add_argument("--out", default="blind"); b.add_argument("--seed", type=int, default=None); b.set_defaults(f=cmd_blind)
    u = sp.add_parser("unblind"); u.add_argument("dir"); u.set_defaults(f=cmd_unblind)
    t = sp.add_parser("selftest"); t.add_argument("--tmp", default="/tmp"); t.set_defaults(f=cmd_selftest)

    a = p.parse_args()
    sys.exit(a.f(a) or 0)


if __name__ == "__main__":
    main()
