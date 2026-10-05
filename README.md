# Kolibri-1 im Praxistest: NIS2, Kanzlei, IT-Dienstleister

Ein unabhängiger, reproduzierbarer Test des offenen Modells Aleph Alpha Kolibri-1.
Stichprobe, kein Benchmark. Preprint, nicht begutachtet.

**Stefan Beierle**
Independent Researcher, Makkah, Saudi Arabia
ORCID: [0009-0005-8512-3839](https://orcid.org/0009-0005-8512-3839)
Correspondence: stefan.beierle@pm.me
Date: October 2026
Preprint / Architecture Report

| | |
|---|---|
| Bericht (Preprint) | [DOI 10.5281/zenodo.23171160](https://doi.org/10.5281/zenodo.23171160) |
| Dieses Repository | [github.com/sbeierle/kolibri1-praxistest](https://github.com/sbeierle/kolibri1-praxistest), eigene DOI folgt bei der Zenodo-Archivierung, der Bericht ist als verwandte Publikation verlinkt |
| Version | v1.0 |
| Lizenz | Code: MIT · Bericht und Ergebnisse: CC BY 4.0 (siehe `LICENSE-DATA.md`) |
| Unabhängigkeit | Keine Verbindung zu Aleph Alpha, kein Auftrag, keine Vergütung |
| KI-Hinweis | Bericht, Testcode und Antwortschlüssel wurden gemeinsam mit Claude (Anthropic) erstellt. Die Läufe hat der Autor selbst ausgeführt. Die Schlüssel sind nicht juristisch geprüft. |

## Was getestet wurde
- Modell: Aleph Alpha Kolibri-1 (Apache-2.0), MoE, 78,1 Mrd. Parameter gesamt, 3,46 Mrd. aktiv, FP8. Checkpoint ca. 72,7 GiB (78,1 GB).
- Serving: vLLM 0.29.0 mit `aleph-alpha-inference` 1.0.0, eine H200 SXM bei RunPod.
- Umfang: 1.851 gewertete Läufe in drei Runden (1.663 automatisch bewertet, 188 nur zum manuellen Lesen; dazu 60 verworfene Läufe und separate Lasttests), Themen: NIS2/BSIG-Erstcheck, Meldepflicht-Triage, Fristen, Lückencheck, Belegextraktion, Langtext, RAG mit Gesetzestext, Kanzlei-Praxis, Prompt-Injection, Abstinenz.
- Bewertung: regelbasiert (Regex und JSON-Vergleich), kein LLM als Richter.

## Kernergebnisse
- Mit Gesetzestext im Prompt ist Kolibri-1 für diese Aufgaben sehr gut: NIS2-Erstcheck 96 % (163/170), Triage 100 % (120/120), Lückencheck 40/40, Belegextraktion 100/100, Langtext 15/15.
- Ohne Text, nur aus dem Modellwissen, bricht es ein: Erstcheck 53 % (90/170), Triage 77 % (92/120), Fristen komplett richtig 20/50. § 32 BSIG wurde aus dem Gedächtnis nur 1-mal in 50 Läufen genannt.
- Die Fehler ohne Text sind überwiegend Ausweichen („kann ich nicht sicher sagen"), nicht selbstbewusst Falsches (Triage: 25 von 28 ausweichend, 3 sicher falsch).
- Prompt-Injection: 39 von 40 abgewehrt (97,5 %).
- Temperatur 0,3 gegen 1,0 machte in Runde 3 kaum einen Unterschied.
- Last: 64 parallele kurze Anfragen ergaben rund 3.700 Token/s ohne Fehler.
- Praxisurteil: nur mit Gesetzestext im Prompt (RAG) einsetzen, nicht als Wissensquelle für Recht.

- System-Prompt: Mit Datum, aber ohne Wissensstichtag erfindet das Modell Ereignisse; erst Datum plus Stichtag (18.06.2026) ordnet die WM-Frage richtig ein.

Details im Bericht: [`report/kolibri1-praxistest.md`](report/kolibri1-praxistest.md).

## Struktur
```
README.md  LICENSE  LICENSE-DATA.md  CITATION.cff  .zenodo.json
DISCLOSURE.md  LIMITATIONS.md  REPRODUCE.md  CHANGELOG.md
report/      Bericht (Markdown, PDF)
scripts/     Testharness, Suiten, Auswertung, PowerShell-Läufe
context/     Gesetzestexte und Sektorlisten, die in Prompts eingesetzt werden
results/     Rohdaten je Lauf (runde1..3), logs/, summary.csv, environment.md, README.md
docs/assets/ Abbildungen und bereinigte Screenshots
```

## Schnellstart
```
cd scripts
python3 praxistest.py selftest      # ohne GPU, prüft nur das Gerüst
```
Vollständige Anleitung: `REPRODUCE.md`.

## Zitieren
Bitte den Bericht zitieren: Beierle, S. (2026). *Kolibri-1 im Praxistest: NIS2, Kanzlei, IT-Dienstleister*. Preprint. https://doi.org/10.5281/zenodo.23171160 . Das Repository: siehe `CITATION.cff`.

## Kein Rechtsrat
Die Ergebnisse zeigen technische Eignung. Antwortschlüssel sind KI-erstellt und nicht juristisch geprüft.
