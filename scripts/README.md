# Kolibri-1 Praxistest (NIS2/BSIG · Kanzlei · IT-Dienstleister)

Kleines, reproduzierbares Test-Set für den Praxiseinsatz – **Stichprobe, kein Benchmark**. Nur Python-Stdlib, läuft gegen jeden OpenAI-kompatiblen Endpoint (vLLM, andere Modelle, APIs).

## Ablauf (ca. 3–4 GPU-Stunden)
1. Kolibri-1 starten (laut Model Card, Plugin `aleph-alpha-inference` nötig):
   `vllm serve Aleph-Alpha/Kolibri-1 --kv-cache-dtype fp8 --reasoning-parser kolibri1 --tool-call-parser kolibri1 --enable-auto-tool-choice`
2. Trockenlauf ohne GPU: `python3 praxistest.py selftest` (Mock-Server, prüft Checks + Export).
3. Test: `python3 praxistest.py run --out res_kolibri --effort low` (danach gern `--effort high` in anderem Ordner).
   Langkontext optional: `--suite longctx --longctx` (große Prompts, `--longctx-sizes 8000,32000`).
4. Speed/Last: `python3 praxistest.py load --concurrency 1,4,16,64 --requests 64 --out load.json`
5. Auswerten: `report.md` (Auto-Scores) + `review.csv` (manuell bewerten: Souveränität, Erklärqualität, Anonymisierung, Mails).
6. Blind-A/B (Alltag): gleiche Prompts gegen dein Vergleichsmodell laufen lassen (`--base-url`, `--api-key-env`), dann
   `python3 praxistest.py blind res_kolibri res_andere --out blind` → `blind.csv` ausfüllen → `unblind blind`.

## Suiten
`nis2` · `kanzlei` · `itdl` · `abstain` (Halluzinationsfallen) · `security` (Prompt-Leak, Privatpersonen) · `souveraenitaet` (manuell) · `alltag` (blind) · `longctx` (Needle).

## Ehrliche Grenzen
- **Antwortschlüssel stammen von Claude (KI), nicht von einem Juristen.** Normen mit `[verifiziert]` (BSIG §§28/30/32/33/38, BRAO §43e, StGB §203, ZPO §517) wurden gegen lxgesetze.de/dejure.org gelesen; `[pruefen]` (u. a. NIS2-Annex-Zuordnung, ZPO §520, Bußgeldrahmen) nur aus Modellwissen. gesetze-im-internet.de war nicht abrufbar. **Vor Veröffentlichung selbst gegenprüfen.**
- Regex-Checks sind grob (falsch-negativ bei Umformulierungen, falsch-positiv bei Zufallstreffern) → `review.csv` stichprobenartig lesen.
- Abstinenz-Check erkennt nur Signalwörter, nicht ob die Begründung stimmt.
- Chat-Template-Parameter (`reasoning_effort`, `enable_thinking`) sind aus der Model Card übernommen, hier nicht gegen einen echten Server getestet. Bei Fehlern `--effort ""` nutzen.
- Der Mock-Selbsttest belegt nur, dass das Gerüst funktioniert – nicht, wie Kolibri abschneidet.
- Kein Rechtsgutachten; Ergebnisse zeigen technische Eignung, keine Marktbewertung. Ergebnis „ungefähr Parität" ist ein legitimes Ergebnis.
- Empfohlene Sampling-Parameter (T=1.0, top_p=0.97, top_k=128) sind Default; Läufe mit `--repeats 3` glätten Streuung.

## Runde 2 (Zusatz-Suiten, nur mit `--suite`)
- `rag` – NIS2-/Kanzlei-Fragen mit Gesetzestext im Prompt (`context/recht.txt`; §§ 32, 38 BSIG, 203 StGB, 517 ZPO wortgetreu, §§ 28, 30, 33 BSIG, 43e BRAO, 520 ZPO sinngemäß – vor Veröffentlichung gegen den amtlichen Text prüfen).
- `praxis` – Rügefrist, Verzugs-Schriftsatz, Haftungsklausel, Erstberatung, Bürgerbrief, Bewirtungsbeleg (JSON). Schlüssel zu HGB/BGB/EStG aus Modellwissen: `[pruefen]`.
- `inject` – 8 Prompt-Injection-Varianten mit harmlosen Marker-Strings.
- Alles auf einmal: `--suite all`. Lasttest mit langen Dokumenten: `load --doc-tokens 8000 --concurrency 1,8,16,32,64` (`--shared-prefix` = Prefix-Cache darf greifen).

## Hinweis Windows/PowerShell
System-Prompts mit Umlauten nicht als Argument uebergeben (PowerShell 5.1 zerschiesst die Kodierung, wenn das Skript ohne BOM gespeichert ist). Stattdessen `--system-file system.txt` (UTF-8) verwenden. In `meta.json` pruefen, ob der Prompt sauber gespeichert ist.

## NIS2-Erstcheck und Meldepflicht-Triage (Runde 3)
`powershell -ExecutionPolicy Bypass -File .\run_nis2.ps1` (Pod laeuft, Tunnel steht, ca. 10-15 Minuten).
Erstcheck: 20 fiktive Einrichtungen, Einstufung besonders wichtig / wichtig / nicht betroffen. Triage: 14 Vorfaelle (erheblich ja/nein) + 5 Fristrechnungen.
Jeder Fall zweimal: "Kopf" (aus dem Modellwissen) und "Text" (mit Gesetzestext bzw. Sektorenliste im Prompt, Dateien in context/).
WICHTIG: Antwortschluessel sind KI-erstellt und nicht juristisch geprueft; Sektorenliste stammt aus einer Drittquelle. Grenzfaelle haben keinen Schluessel (manuell lesen). Kein Rechtsrat.
Auswertung: `python nis2_auswertung.py ..\n_erst_t03 ..\n_tri_t03 ..\n_erst_t10 ..\n_tri_t10`

Weitere Reihen im selben Skript: Lueckencheck (8 Ist-Zustaende mit eingebauten Luecken nach § 30 BSIG; Treffer = Luecken gefunden, Abzug = erfundene Luecken), Belegextraktion (20 synthetische Rechnungen in 3 Layouts, Betraege/Datum/Nummer exakt), langer Text (Nadelsuche 8k/32k Token).
Ergebnisse: Ordner ..\n_luecken, ..\n_beleg, ..\n_longctx (mit `python praxistest.py report ORDNER` Detailbericht).
