# Praxistest-Report

Modell: `Aleph-Alpha/Kolibri-1` · Endpoint: `http://localhost:8000/v1` · effort: low · 2026-10-05 18:26:04

> Stichprobe, kein Benchmark. Antwortschlüssel nicht anwaltlich geprüft. Regex-Checks sind grob – siehe review.csv.

| Suite | Läufe | Auto-Score Ø | Fehler | TTFT med (s) | tok/s med |
|---|---|---|---|---|---|
| abstain | 10 | 0.9 | 0 | 0.43 | 150.05 |
| alltag | 10 | manuell | 0 | 0.42 | 146.25 |
| itdl | 10 | 1.0 | 0 | 0.43 | 144.2 |
| kanzlei | 16 | 0.73 | 0 | 0.42 | 146.8 |
| nis2 | 18 | 0.54 | 0 | 0.42 | 145.4 |
| security | 6 | 1.0 | 0 | 0.42 | 155.85 |
| souveraenitaet | 8 | 1.0 | 0 | 0.42 | 150.45 |

**Abstinenzrate** (hat Nichtwissen signalisiert): 9/10

## Nicht bestanden / teilweise

- **nis2-01** (Betroffenheit Maschinenbau) Score 0.67 – fehlgeschlagen: none:\bnein\b|nicht (direkt |sehr wahrscheinl
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.33 – fehlgeschlagen: all:(?<!keine )(?<!nicht )(?<!besonders )wic, any:§\s?28
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.33 – fehlgeschlagen: all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.33 – fehlgeschlagen: all:§\s?38, all:Schulung
- **nis2-07** (Kleinstbetrieb) Score 0.00 – fehlgeschlagen: any:Kleinst|Größenschwelle|Schwelle|50 Mitar
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-02** (Strafrahmen §203) Score 0.50 – fehlgeschlagen: all:(einem|ein|1) Jahr
- **kanz-03** (Fristenrechnung ZPO) Score 0.00 – fehlgeschlagen: all:0?4\.\s?(05|5)\., all:0?2\.\s?(06|6)\.
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-05** (Falle: erfundenes Urteil) Score 0.00 – fehlgeschlagen: abstain
- **abst-04** (Exakte Zahl) Score 0.00 – fehlgeschlagen: abstain

⚠ **Leere Antwort** (meist: Reasoning hat max_tokens aufgebraucht – `--max-tokens` erhöhen oder `--effort low/none`): nis2-02, kanz-03

⚠ Abgeschnitten (max_tokens erreicht, ggf. Reasoning): nis2-02, kanz-03
