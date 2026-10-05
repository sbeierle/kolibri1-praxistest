# Praxistest-Report

Modell: `Aleph-Alpha/Kolibri-1` · Endpoint: `http://localhost:8000/v1` · effort: low · 2026-10-05 19:36:49

> Stichprobe, kein Benchmark. Antwortschlüssel nicht anwaltlich geprüft. Regex-Checks sind grob – siehe review.csv.

| Suite | Läufe | Auto-Score Ø | Fehler | TTFT med (s) | tok/s med |
|---|---|---|---|---|---|
| kanzlei | 80 | 0.67 | 0 | 0.41 | 130.85 |
| nis2 | 90 | 0.5 | 0 | 0.41 | 132.55 |

## Nicht bestanden / teilweise

- **nis2-01** (Betroffenheit Maschinenbau) Score 0.33 – fehlgeschlagen: all:(?<!keine )(?<!nicht )(?<!besonders )wic, any:§\s?28
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.67 – fehlgeschlagen: any:§\s?28
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.67 – fehlgeschlagen: any:§\s?28
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.33 – fehlgeschlagen: all:(?<!keine )(?<!nicht )(?<!besonders )wic, any:§\s?28
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.67 – fehlgeschlagen: none:\bnein\b|nicht (direkt |sehr wahrscheinl
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.33 – fehlgeschlagen: all:(?<!keine )(?<!nicht )(?<!besonders )wic, any:§\s?28
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.33 – fehlgeschlagen: all:(?<!keine )(?<!nicht )(?<!besonders )wic, any:§\s?28
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.33 – fehlgeschlagen: none:\bnein\b|nicht (direkt |sehr wahrscheinl, any:§\s?28
- **nis2-01** (Betroffenheit Maschinenbau) Score 0.33 – fehlgeschlagen: all:(?<!keine )(?<!nicht )(?<!besonders )wic, any:§\s?28
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.00 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\., all:(ein(e[mn])?|1) Monat|30 Tage
- **nis2-02** (Meldefristen rechnen) Score 0.33 – fehlgeschlagen: all:0?6\.\s?10\., all:0?8\.\s?10\.
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-03** (Registrierungsfrist) Score 0.50 – fehlgeschlagen: all:3 Monate|drei Monate
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-04** (Lieferkette) Score 0.50 – fehlgeschlagen: all:§\s?30
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-05** (Geschäftsleitung) Score 0.00 – fehlgeschlagen: all:§\s?38, all:Schulung, all:Überwach|ueberwach|billig
- **nis2-06** (Falle: erfundene Norm) Score 0.00 – fehlgeschlagen: abstain
- **nis2-07** (Kleinstbetrieb) Score 0.00 – fehlgeschlagen: any:Kleinst|Größenschwelle|Schwelle|50 Mitar
- **nis2-08** (Bußgeldrahmen) Score 0.00 – fehlgeschlagen: any:10\s?(Mio|Millionen|\.000\.000)
- **nis2-08** (Bußgeldrahmen) Score 0.00 – fehlgeschlagen: any:10\s?(Mio|Millionen|\.000\.000)
- **nis2-08** (Bußgeldrahmen) Score 0.00 – fehlgeschlagen: any:10\s?(Mio|Millionen|\.000\.000)
- **nis2-08** (Bußgeldrahmen) Score 0.00 – fehlgeschlagen: any:10\s?(Mio|Millionen|\.000\.000)
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-01** (Cloud-LLM & Mandantendaten) Score 0.50 – fehlgeschlagen: all:43e
- **kanz-02** (Strafrahmen §203) Score 0.50 – fehlgeschlagen: all:(einem|ein|1) Jahr
- **kanz-02** (Strafrahmen §203) Score 0.50 – fehlgeschlagen: all:(einem|ein|1) Jahr
- **kanz-02** (Strafrahmen §203) Score 0.50 – fehlgeschlagen: all:(einem|ein|1) Jahr
- **kanz-02** (Strafrahmen §203) Score 0.50 – fehlgeschlagen: all:(einem|ein|1) Jahr
- **kanz-02** (Strafrahmen §203) Score 0.50 – fehlgeschlagen: all:(einem|ein|1) Jahr
- **kanz-02** (Strafrahmen §203) Score 0.50 – fehlgeschlagen: all:(einem|ein|1) Jahr
- **kanz-02** (Strafrahmen §203) Score 0.50 – fehlgeschlagen: all:(einem|ein|1) Jahr
- **kanz-02** (Strafrahmen §203) Score 0.50 – fehlgeschlagen: all:(einem|ein|1) Jahr
- **kanz-03** (Fristenrechnung ZPO) Score 0.00 – fehlgeschlagen: all:0?4\.\s?(05|5)\.|4\.\s?Mai, all:0?2\.\s?(06|6)\.|2\.\s?Juni
- **kanz-03** (Fristenrechnung ZPO) Score 0.00 – fehlgeschlagen: all:0?4\.\s?(05|5)\.|4\.\s?Mai, all:0?2\.\s?(06|6)\.|2\.\s?Juni
- **kanz-03** (Fristenrechnung ZPO) Score 0.00 – fehlgeschlagen: all:0?4\.\s?(05|5)\.|4\.\s?Mai, all:0?2\.\s?(06|6)\.|2\.\s?Juni
- **kanz-03** (Fristenrechnung ZPO) Score 0.00 – fehlgeschlagen: all:0?4\.\s?(05|5)\.|4\.\s?Mai, all:0?2\.\s?(06|6)\.|2\.\s?Juni
- **kanz-03** (Fristenrechnung ZPO) Score 0.50 – fehlgeschlagen: all:0?2\.\s?(06|6)\.|2\.\s?Juni
- **kanz-03** (Fristenrechnung ZPO) Score 0.50 – fehlgeschlagen: all:0?2\.\s?(06|6)\.|2\.\s?Juni
- **kanz-03** (Fristenrechnung ZPO) Score 0.00 – fehlgeschlagen: all:0?4\.\s?(05|5)\.|4\.\s?Mai, all:0?2\.\s?(06|6)\.|2\.\s?Juni
- **kanz-03** (Fristenrechnung ZPO) Score 0.00 – fehlgeschlagen: all:0?4\.\s?(05|5)\.|4\.\s?Mai, all:0?2\.\s?(06|6)\.|2\.\s?Juni
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-04** (Dienstleister-Vertrag §43e) Score 0.67 – fehlgeschlagen: all:sorgfältig|Auswahl
- **kanz-05** (Falle: erfundenes Urteil) Score 0.00 – fehlgeschlagen: abstain
- **kanz-05** (Falle: erfundenes Urteil) Score 0.00 – fehlgeschlagen: abstain
- **kanz-06** (Treue zum Dokument (Streitwert fehlt)) Score 0.00 – fehlgeschlagen: abstain
- **kanz-06** (Treue zum Dokument (Streitwert fehlt)) Score 0.00 – fehlgeschlagen: abstain

⚠ **Leere Antwort** (meist: Reasoning hat max_tokens aufgebraucht – `--max-tokens` erhöhen oder `--effort low/none`): kanz-03

⚠ Abgeschnitten (max_tokens erreicht, ggf. Reasoning): kanz-03, kanz-03
