# Nachbauen

Voraussetzungen: Python 3 (nur Standardbibliothek), ein OpenAI-kompatibler Endpoint.

## 1. Modell starten (vLLM, Plugin `aleph-alpha-inference` nötig)
```
vllm serve Aleph-Alpha/Kolibri-1 --kv-cache-dtype fp8 \
  --reasoning-parser kolibri1 --tool-call-parser kolibri1 \
  --enable-auto-tool-choice --max-model-len 40000
```
Hinweis: Auf unserer Maschine führte `--safetensors-load-strategy prefetch` zu `OSError: [Errno 12] Cannot allocate memory`. Ohne diese Option lief der Start.
Eingesetzt: vLLM 0.29.0, `aleph-alpha-inference` 1.0.0, H200 SXM, 4,62 $/h. Checkpoint ca. 72,7 GiB.

## 2. Trockenlauf ohne GPU
```
cd scripts
python3 praxistest.py selftest
```

## 3. Läufe
Runde 3 (Windows/PowerShell): `powershell -ExecutionPolicy Bypass -File .\run_nis2.ps1`
Einzelne Suite: `python3 praxistest.py run --suite erstcheck --repeats 5 --effort low --system-file system.txt --out ergebnis`
Der Ordner `context/` wird automatisch gefunden (`scripts/context` oder `../context`, Platzhalter `{{CONTEXT:datei}}`).

## 4. Auswertung
`python3 nis2_auswertung.py ORDNER ...` und `python3 praxistest.py report ORDNER`.
Übersicht der Läufe: `results/README.md` und `results/summary.csv`.

## 5. Last
`python3 praxistest.py load --concurrency 1,4,16,64 --requests 64 --out load.json`
Lange Dokumente: `load --doc-tokens 8000 --concurrency 1,8,16,32`.

Ausführliche Skriptbeschreibung: `scripts/README.md`.
