# -*- coding: utf-8 -*-
"""Auswertung Erstcheck/Triage: python nis2_auswertung.py ORDNER [ORDNER ...]
Pro Fall und Bedingung (Kopf/Text): Trefferquote gegen Schluessel, Konsistenz (Anteil der haeufigsten Antwort),
Verwechslungstabelle. Grenzfaelle ohne Schluessel: nur Verteilung der Antworten."""
import sys, json, os, re, collections
import suites

def load(d):
    return [json.loads(l) for l in open(os.path.join(d, "results.jsonl"), encoding="utf-8") if l.strip()]

def answer(r):
    j = suites.parse_json(r["response"])
    if not j:
        return "KEIN_JSON"
    return suites.norm_val(j.get("einstufung", j.get("erheblich")))

for d in sys.argv[1:]:
    rows = [r for r in load(d) if r["suite"] in ("erstcheck", "triage") and not r["id"].startswith("fri-")]
    print(f"\n=== {d}  ({len(rows)} Antworten)")
    by = collections.defaultdict(list)
    for r in rows:
        by[r["id"]].append(r)
    cond = collections.defaultdict(lambda: [0, 0, 0, 0])  # n, treffer, konsistent, mit schluessel
    conf = collections.defaultdict(collections.Counter)
    for i, rs in sorted(by.items()):
        ans = [answer(r) for r in rs]
        c = collections.Counter(ans)
        top, cnt = c.most_common(1)[0]
        has_key = bool(rs[0]["checks"])
        hit = sum(r["score"] >= 0.99 for r in rs) if has_key else None
        print(f"{i:9s} {rs[0]['title'][:44]:44s} {'Treffer %d/%d ' % (hit, len(rs)) if has_key else 'Grenzfall      '} Verteilung {dict(c)}")
        k = i[-1]
        cond[k][0] += len(rs); cond[k][2] += cnt
        if has_key:
            cond[k][1] += hit; cond[k][3] += len(rs)
            for a in ans:
                conf[k][(i[:-1], a)] += 1
    print("\nGesamt:")
    for k, name in (("a", "aus dem Kopf"), ("b", "mit Text")):
        n, h, cons, nk = cond[k]
        if n:
            print(f"  {name:13s}: Treffer {h}/{nk} = {100*h/max(nk,1):.0f} %   Konsistenz (haeufigste Antwort pro Fall) {100*cons/n:.0f} %")
    fr = [r for r in load(d) if r["id"].startswith("fri-")]
    for k, name in (("a", "aus dem Kopf"), ("b", "mit Text")):
        s = [r["score"] for r in fr if r["id"].endswith(k)]
        if s:
            print(f"  Fristen {name:13s}: Mittel {sum(s)/len(s):.2f} ueber {len(s)} Antworten")
