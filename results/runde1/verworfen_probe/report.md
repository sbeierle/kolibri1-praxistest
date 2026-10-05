# Praxistest-Report

Modell: `Aleph-Alpha/Kolibri-1` · Endpoint: `http://localhost:8000/v1` · effort:  · 2026-10-05 18:18:47

> Stichprobe, kein Benchmark. Antwortschlüssel nicht anwaltlich geprüft. Regex-Checks sind grob – siehe review.csv.

| Suite | Läufe | Auto-Score Ø | Fehler | TTFT med (s) | tok/s med |
|---|---|---|---|---|---|
| nis2 | 5 | 0.1 | 0 | 0.44 | 175.9 |

## Nicht bestanden / teilweise

- **nis2-01** (Betroffenheit Maschinenbau) Score 0.00 – fehlgeschlagen: all:wichtige Einrichtung, all:\bja\b|betroffen, any:§\s?28
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-03** (Registrierungsfrist) Score 0.00 – fehlgeschlagen: all:3 Monate|drei Monate, all:BSI
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig

⚠ **Leere Antwort** (meist: Reasoning hat max_tokens aufgebraucht – `--max-tokens` erhöhen oder `--effort low/none`): nis2-01, nis2-02, nis2-03, nis2-05

⚠ Abgeschnitten (max_tokens erreicht, ggf. Reasoning): nis2-01, nis2-02, nis2-03, nis2-05
