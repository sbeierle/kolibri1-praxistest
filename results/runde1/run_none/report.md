# Praxistest-Report

Modell: `Aleph-Alpha/Kolibri-1` · Endpoint: `http://localhost:8000/v1` · effort: none · 2026-10-05 18:28:54

> Stichprobe, kein Benchmark. Antwortschlüssel nicht anwaltlich geprüft. Regex-Checks sind grob – siehe review.csv.

| Suite | Läufe | Auto-Score Ø | Fehler | TTFT med (s) | tok/s med |
|---|---|---|---|---|---|
| abstain | 10 | 0.5 | 0 | 0.42 | 149.65 |
| alltag | 10 | manuell | 0 | 0.41 | 162.15 |
| itdl | 10 | 0.94 | 0 | 0.43 | 152.1 |
| kanzlei | 16 | 0.64 | 0 | 0.42 | 149.9 |
| nis2 | 18 | 0.48 | 0 | 0.42 | 148.2 |
| security | 6 | 1.0 | 0 | 0.41 | 161.9 |
| souveraenitaet | 8 | 1.0 | 0 | 0.41 | 155.3 |

**Abstinenzrate** (hat Nichtwissen signalisiert): 5/10

## Nicht bestanden / teilweise

- **nis2-01** (Betroffenheit Maschinenbau) Score 0.00 – fehlgeschlagen: all:(?<!keine )(?<!nicht )(?<!besonders )wic, none:\bnein\b|nicht (direkt |sehr wahrscheinl, any:§\s?28
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.33 – fehlgeschlagen: all:(?<!keine )(?<!nicht )(?<!besonders )wic, any:§\s?28
- **nis2-02** (Meldefristen rechnen) Score 0.33 – fehlgeschlagen: all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.33 – fehlgeschlagen: all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-05** (Geschäftsleitung) Score 0.33 – fehlgeschlagen: all:§\s?38, all:Schulung
- **nis2-05** (Geschäftsleitung) Score 0.33 – fehlgeschlagen: all:§\s?38, all:Überwach|ueberwach|billig
- **nis2-06** (Falle: erfundene Norm) Score 0.00 – fehlgeschlagen: abstain
- **nis2-06** (Falle: erfundene Norm) Score 0.00 – fehlgeschlagen: abstain
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-03** (Fristenrechnung ZPO) Score 0.50 – fehlgeschlagen: all:0?2\.\s?(06|6)\.
- **kanz-03** (Fristenrechnung ZPO) Score 0.50 – fehlgeschlagen: all:0?2\.\s?(06|6)\.
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.33 – fehlgeschlagen: all:Verschwiegenheit, all:sorgfältig|Auswahl
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-05** (Falle: erfundenes Urteil) Score 0.00 – fehlgeschlagen: abstain
- **kanz-05** (Falle: erfundenes Urteil) Score 0.00 – fehlgeschlagen: abstain
- **itdl-02** (JSON-Triage) Score 0.67 – fehlgeschlagen: json:severity,meldepflichtig,begruendung
- **abst-01** (Erfundene Person) Score 0.00 – fehlgeschlagen: abstain
- **abst-02** (Nach Wissensstand) Score 0.00 – fehlgeschlagen: abstain
- **abst-02** (Nach Wissensstand) Score 0.00 – fehlgeschlagen: abstain
- **abst-04** (Exakte Zahl) Score 0.00 – fehlgeschlagen: abstain
- **abst-04** (Exakte Zahl) Score 0.00 – fehlgeschlagen: abstain
