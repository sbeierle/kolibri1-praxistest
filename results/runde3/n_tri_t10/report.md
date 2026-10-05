# Praxistest-Report

Modell: `Aleph-Alpha/Kolibri-1` · Endpoint: `http://localhost:8000/v1` · effort: low · 2026-10-05 20:55:35

> Stichprobe, kein Benchmark. Antwortschlüssel nicht anwaltlich geprüft. Regex-Checks sind grob – siehe review.csv.

| Suite | Läufe | Auto-Score Ø | Fehler | TTFT med (s) | tok/s med |
|---|---|---|---|---|---|
| triage | 190 | 0.84 | 0 | 0.41 | 131.5 |

## Nicht bestanden / teilweise

- **tri-02a** (Triage Datenabfluss Kunden [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-02a** (Triage Datenabfluss Kunden [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-02a** (Triage Datenabfluss Kunden [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-03a** (Triage DDoS Webshop [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-03a** (Triage DDoS Webshop [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-03a** (Triage DDoS Webshop [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-03a** (Triage DDoS Webshop [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-03a** (Triage DDoS Webshop [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-05a** (Triage Rechenzentrum Ausfall [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-05a** (Triage Rechenzentrum Ausfall [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-05a** (Triage Rechenzentrum Ausfall [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **tri-06a** (Triage Lieferkette Update [Kopf]) Score 0.00 – fehlgeschlagen: jsoneq:erheblich
- **fri-01a** (Fristen ab 06.10. 08:15 [Kopf]) Score 0.00 – fehlgeschlagen: all:0?7\.\s?0?10\.|7\.\s?Oktober, all:0?9\.\s?0?10\.|9\.\s?Oktober, all:0?9\.\s?0?11\.|9\.\s?November, any:§\s?32
- **fri-01a** (Fristen ab 06.10. 08:15 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-01a** (Fristen ab 06.10. 08:15 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-01a** (Fristen ab 06.10. 08:15 [Kopf]) Score 0.50 – fehlgeschlagen: all:0?9\.\s?0?11\.|9\.\s?November, any:§\s?32
- **fri-01a** (Fristen ab 06.10. 08:15 [Kopf]) Score 0.00 – fehlgeschlagen: all:0?7\.\s?0?10\.|7\.\s?Oktober, all:0?9\.\s?0?10\.|9\.\s?Oktober, all:0?9\.\s?0?11\.|9\.\s?November, any:§\s?32
- **fri-02a** (Fristen ab 20.10. 14:30 [Kopf]) Score 0.00 – fehlgeschlagen: all:0?21\.\s?0?10\.|21\.\s?Oktober, all:0?23\.\s?0?10\.|23\.\s?Oktober, all:0?23\.\s?0?11\.|23\.\s?November, any:§\s?32
- **fri-02a** (Fristen ab 20.10. 14:30 [Kopf]) Score 0.75 – fehlgeschlagen: all:0?23\.\s?0?11\.|23\.\s?November
- **fri-02a** (Fristen ab 20.10. 14:30 [Kopf]) Score 0.50 – fehlgeschlagen: all:0?23\.\s?0?11\.|23\.\s?November, any:§\s?32
- **fri-02a** (Fristen ab 20.10. 14:30 [Kopf]) Score 0.50 – fehlgeschlagen: all:0?23\.\s?0?11\.|23\.\s?November, any:§\s?32
- **fri-02a** (Fristen ab 20.10. 14:30 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-03a** (Fristen ab 01.12. 09:05 [Kopf]) Score 0.00 – fehlgeschlagen: all:0?2\.\s?0?12\.|2\.\s?Dezember, all:0?4\.\s?0?12\.|4\.\s?Dezember, all:0?4\.\s?0?1\.|4\.\s?Januar, any:§\s?32
- **fri-03a** (Fristen ab 01.12. 09:05 [Kopf]) Score 0.50 – fehlgeschlagen: all:0?4\.\s?0?1\.|4\.\s?Januar, any:§\s?32
- **fri-03a** (Fristen ab 01.12. 09:05 [Kopf]) Score 0.00 – fehlgeschlagen: all:0?2\.\s?0?12\.|2\.\s?Dezember, all:0?4\.\s?0?12\.|4\.\s?Dezember, all:0?4\.\s?0?1\.|4\.\s?Januar, any:§\s?32
- **fri-03a** (Fristen ab 01.12. 09:05 [Kopf]) Score 0.00 – fehlgeschlagen: all:0?2\.\s?0?12\.|2\.\s?Dezember, all:0?4\.\s?0?12\.|4\.\s?Dezember, all:0?4\.\s?0?1\.|4\.\s?Januar, any:§\s?32
- **fri-03a** (Fristen ab 01.12. 09:05 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-04a** (Fristen ab 15.12. 16:40 [Kopf]) Score 0.00 – fehlgeschlagen: all:0?16\.\s?0?12\.|16\.\s?Dezember, all:0?18\.\s?0?12\.|18\.\s?Dezember, all:0?18\.\s?0?1\.|18\.\s?Januar, any:§\s?32
- **fri-04a** (Fristen ab 15.12. 16:40 [Kopf]) Score 0.00 – fehlgeschlagen: all:0?16\.\s?0?12\.|16\.\s?Dezember, all:0?18\.\s?0?12\.|18\.\s?Dezember, all:0?18\.\s?0?1\.|18\.\s?Januar, any:§\s?32
- **fri-04a** (Fristen ab 15.12. 16:40 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-04a** (Fristen ab 15.12. 16:40 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-04a** (Fristen ab 15.12. 16:40 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-05a** (Fristen ab 05.01. 11:00 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-05a** (Fristen ab 05.01. 11:00 [Kopf]) Score 0.25 – fehlgeschlagen: all:0?8\.\s?0?1\.|8\.\s?Januar, all:0?8\.\s?0?2\.|8\.\s?Februar, any:§\s?32
- **fri-05a** (Fristen ab 05.01. 11:00 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-05a** (Fristen ab 05.01. 11:00 [Kopf]) Score 0.75 – fehlgeschlagen: any:§\s?32
- **fri-05a** (Fristen ab 05.01. 11:00 [Kopf]) Score 0.00 – fehlgeschlagen: all:0?6\.\s?0?1\.|6\.\s?Januar, all:0?8\.\s?0?1\.|8\.\s?Januar, all:0?8\.\s?0?2\.|8\.\s?Februar, any:§\s?32
