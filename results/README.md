# Ergebnisse

Alle Läufe stammen vom 05.10.2026 (Zeitstempel in den `meta.json`). Jeder Ordner enthält `results.jsonl` (Rohantworten, Reasoning, Scores), `meta.json` (Parameter), `report.md` (Auto-Report) und `review.csv` (zum manuellen Lesen).
Gesamt: **1.851 gewertete Läufe** (1.663 automatisch bewertet, 188 nur zum manuellen Lesen) plus **60 verworfene Läufe**. Tabelle: `summary.csv`.

| Ordner | Inhalt | effort | Temp. | Systemprompt | Läufe |
|---|---|---|---|---|---|
| **runde1/** | | | | | |
| `run_none` | Erstlauf alle Suiten | none | 1,0 | nein | 78 |
| `run_low` | Erstlauf alle Suiten | low | 1,0 | nein | 78 |
| `abst_none2` | Abstinenz-Fallen | none | 1,0 | nein | 50 |
| `abst_low` | Abstinenz-Fallen | low | 1,0 | nein | 50 |
| `abst_none_sys` | Abstinenz-Fallen | none | 1,0 | Variante 1 (kurz) | 50 |
| `abst_low_sys` | Abstinenz-Fallen | low | 1,0 | Variante 1 (kurz) | 50 |
| `abst_low_sys2` | Abstinenz-Fallen | low | 1,0 | Variante 2 (mit Wissensstand 18.06.2026) | 50 |
| **runde2/** | | | | | |
| `rag_low` | NIS2/Kanzlei mit Gesetzestext im Prompt | low | 1,0 | Variante 2 (Umlaute beschädigt) | 100 |
| `praxis_low` | Kanzlei-/Verwaltungs-/Steuerbüro-Praxis | low | 1,0 | Variante 2 (Umlaute beschädigt) | 30 |
| `inject_low` | Prompt-Injection | low | 1,0 | Variante 2 (Umlaute beschädigt) | 40 |
| `nis2_t03` | NIS2 + Kanzlei | low | 0,3 | Variante 2 (Umlaute beschädigt) | 170 |
| `nis2_t10` | NIS2 + Kanzlei | low | 1,0 | Variante 2 (Umlaute beschädigt) | 170 |
| **runde3/** | | | | | |
| `n_erst_t03`, `n_erst_t10` | NIS2-Erstcheck (Kopf/Text) | low | 0,3 / 1,0 | Variante 2 | je 200 |
| `n_tri_t03`, `n_tri_t10` | Meldepflicht-Triage + Fristen (Kopf/Text) | low | 0,3 / 1,0 | Variante 2 | je 190 |
| `n_luecken` | Lückencheck | low | 0,3 | Variante 2 | 40 |
| `n_beleg` | Belegextraktion | low | 0,3 | Variante 2 | 100 |
| `n_longctx` | Langtext (Nadelsuche 8k/32k) | low | 0,3 | Variante 2 | 15 |

## Verworfen (nicht in den Zahlen des Berichts)
- `runde1/verworfen_probe`, `verworfen_probe_low`: je 5 Probeläufe, Reasoning hat das Token-Limit aufgebraucht (leere Antworten).
- `runde1/verworfen_abst_none`: 50 Läufe, Verbindungsabbruch (`ConnectionResetError`), Server war weg. Ersatz: `abst_none2`.

## Systemprompt-Kodierung
In Runde 2 kam der Systemprompt durch eine PowerShell-Kodierung mit beschädigten Umlauten an („Ã¼ber“ statt „über“, siehe `meta.json`). Das Modell hat ihn offenbar verstanden, die Werte sind aber nicht 1:1 mit den anderen Runden vergleichbar. Runde 1 (`abst_*_sys*`) und Runde 3 liefen mit sauberem Prompt.

## Rescore
Die Ordner in `runde2/` und die `abst_*`-Ordner (außer `verworfen_abst_none`) in `runde1/` wurden nach Korrektur einzelner Checks mit `praxistest.py rescore` neu bewertet (die Modellantworten blieben unverändert). Der Stand davor liegt als `results.vor-rescore.jsonl` daneben. Die Logs in `logs/` zeigen deshalb teils niedrigere Scores als `summary.csv` (z. B. `rag_low`: 0,84 im Log, 1,0 nach Rescore, weil die Abstinenz-Prüfung bei den Fallen rag-05/rag-10 zu streng war).
Die Konsolen-Logs sind von Windows-Pfaden und Benutzernamen bereinigt; durch die cp1252-Konsole sind Umlaute darin teils beschädigt.

## Hinweise
- `auto_score_mittel` in `summary.csv` ist der Mittelwert der Auto-Scores einer Suite, nicht der Anteil bestandener Läufe. Die Trefferquoten im Bericht (z. B. Erstcheck Text 163/170) stammen aus `scripts/nis2_auswertung.py`.
- Die Lasttests (`load`) liegen hier nicht als Rohdatei, Messwerte siehe `environment.md`.
