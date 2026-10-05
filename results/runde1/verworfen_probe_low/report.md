# Praxistest-Report

Modell: `Aleph-Alpha/Kolibri-1` · Endpoint: `http://localhost:8000/v1` · effort: low · 2026-10-05 18:22:57

> Stichprobe, kein Benchmark. Antwortschlüssel nicht anwaltlich geprüft. Regex-Checks sind grob – siehe review.csv.

| Suite | Läufe | Auto-Score Ø | Fehler | TTFT med (s) | tok/s med |
|---|---|---|---|---|---|
| nis2 | 5 | 0.4 | 0 | 0.41 | 174.6 |

## Nicht bestanden / teilweise

- **nis2-01** (Betroffenheit Maschinenbau) Score 0.33 – fehlgeschlagen: all:wichtige Einrichtung, any:§\s?28
- **nis2-02** (Meldefristen rechnen) Score 0.67 – fehlgeschlagen: all:0?8\.\s?10\.
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
