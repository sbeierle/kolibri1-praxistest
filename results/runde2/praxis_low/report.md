# Praxistest-Report

Modell: `Aleph-Alpha/Kolibri-1` · Endpoint: `http://localhost:8000/v1` · effort: low · 2026-10-05 19:33:56

> Stichprobe, kein Benchmark. Antwortschlüssel nicht anwaltlich geprüft. Regex-Checks sind grob – siehe review.csv.

| Suite | Läufe | Auto-Score Ø | Fehler | TTFT med (s) | tok/s med |
|---|---|---|---|---|---|
| praxis | 30 | 0.93 | 0 | 0.41 | 131.15 |

## Nicht bestanden / teilweise

- **prax-01** (Kanzlei: Rügefrist Software (§ 377 HGB vs. Vertrag)) Score 0.75 – fehlgeschlagen: any:Abnahme|Werkvertrag|Kaufvertrag|Werklief
- **prax-01** (Kanzlei: Rügefrist Software (§ 377 HGB vs. Vertrag)) Score 0.75 – fehlgeschlagen: any:Abnahme|Werkvertrag|Kaufvertrag|Werklief
- **prax-05** (Verwaltung: Bescheid in Bürgerbrief übersetzen) Score 0.86 – fehlgeschlagen: none:Restgehwegbreite von nur 1,20
- **prax-05** (Verwaltung: Bescheid in Bürgerbrief übersetzen) Score 0.71 – fehlgeschlagen: all:45\s?(cm|Zentimeter), none:(auf|von nur|nur) 1,20\s?(m|Meter)\s*(ve
- **prax-05** (Verwaltung: Bescheid in Bürgerbrief übersetzen) Score 0.86 – fehlgeschlagen: none:(auf|von nur|nur) 1,20\s?(m|Meter)\s*(ve
- **prax-05** (Verwaltung: Bescheid in Bürgerbrief übersetzen) Score 0.86 – fehlgeschlagen: none:(auf|von nur|nur) 1,20\s?(m|Meter)\s*(ve
- **prax-06** (Steuerbüro: Bewirtungsbeleg prüfen (JSON)) Score 0.80 – fehlgeschlagen: all:Teilnehmer
- **prax-06** (Steuerbüro: Bewirtungsbeleg prüfen (JSON)) Score 0.80 – fehlgeschlagen: all:Anlass
- **prax-06** (Steuerbüro: Bewirtungsbeleg prüfen (JSON)) Score 0.60 – fehlgeschlagen: all:Teilnehmer, all:Anlass
- **prax-06** (Steuerbüro: Bewirtungsbeleg prüfen (JSON)) Score 0.80 – fehlgeschlagen: all:Anlass
