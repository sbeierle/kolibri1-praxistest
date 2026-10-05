# Praxistest-Report

Modell: `Aleph-Alpha/Kolibri-1` · Endpoint: `http://localhost:8000/v1` · effort: low · 2026-10-05 20:47:13

> Stichprobe, kein Benchmark. Antwortschlüssel nicht anwaltlich geprüft. Regex-Checks sind grob – siehe review.csv.

| Suite | Läufe | Auto-Score Ø | Fehler | TTFT med (s) | tok/s med |
|---|---|---|---|---|---|
| erstcheck | 200 | 0.76 | 0 | 0.41 | 129.6 |

## Nicht bestanden / teilweise

- **erst-02a** (Erstcheck Maschinenbau mittel [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-02a** (Erstcheck Maschinenbau mittel [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-02a** (Erstcheck Maschinenbau mittel [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-03a** (Erstcheck Maschinenbau groß [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-03a** (Erstcheck Maschinenbau groß [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-03a** (Erstcheck Maschinenbau groß [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-03a** (Erstcheck Maschinenbau groß [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-03a** (Erstcheck Maschinenbau groß [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-03b** (Erstcheck Maschinenbau groß [Text]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-05a** (Erstcheck Lebensmittel industriell [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-05a** (Erstcheck Lebensmittel industriell [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-05a** (Erstcheck Lebensmittel industriell [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-06a** (Erstcheck Arztpraxis [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-07a** (Erstcheck Privatklinik [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-08a** (Erstcheck Managed Service Provider [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-11a** (Erstcheck Cloud-Anbieter [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-11a** (Erstcheck Cloud-Anbieter [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-12a** (Erstcheck DNS-Anbieter [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-13a** (Erstcheck Vertrauensdiensteanbieter [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-13a** (Erstcheck Vertrauensdiensteanbieter [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-13a** (Erstcheck Vertrauensdiensteanbieter [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-13a** (Erstcheck Vertrauensdiensteanbieter [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-14a** (Erstcheck Online-Marktplatz [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-14a** (Erstcheck Online-Marktplatz [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-14a** (Erstcheck Online-Marktplatz [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-14a** (Erstcheck Online-Marktplatz [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-15a** (Erstcheck Paketdienst [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-15a** (Erstcheck Paketdienst [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-15a** (Erstcheck Paketdienst [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-15a** (Erstcheck Paketdienst [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-16a** (Erstcheck Chemiehersteller [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-16a** (Erstcheck Chemiehersteller [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-16a** (Erstcheck Chemiehersteller [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-16a** (Erstcheck Chemiehersteller [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-16a** (Erstcheck Chemiehersteller [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-17a** (Erstcheck Autozulieferer [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-17a** (Erstcheck Autozulieferer [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-17a** (Erstcheck Autozulieferer [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-17a** (Erstcheck Autozulieferer [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-17b** (Erstcheck Autozulieferer [Text]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung
- **erst-17b** (Erstcheck Autozulieferer [Text]) Score 0.00 – fehlgeschlagen: jsoneq:einstufung

⚠ **Leere Antwort** (meist: Reasoning hat max_tokens aufgebraucht – `--max-tokens` erhöhen oder `--effort low/none`): erst-02a, erst-05a, erst-07a, erst-13a

⚠ Abgeschnitten (max_tokens erreicht, ggf. Reasoning): erst-02a, erst-05a, erst-07a, erst-13a
