# Umgebung

- Modell: Aleph-Alpha/Kolibri-1, MoE 78,1 Mrd. gesamt / 3,46 Mrd. aktiv, FP8, Apache-2.0
- Checkpoint: 32 Safetensors-Dateien, 78.103.074.560 Byte = ca. 72,7 GiB (Quelle: Hugging Face Dateiliste; vLLM-Log nennt 73,43 GiB inklusive Nebendateien)
- Wissensstand des Modells: 18.06.2026
- Server: vLLM 0.29.0, `aleph-alpha-inference` 1.0.0, Parser `kolibri1`, `--kv-cache-dtype fp8`, `--max-model-len 40000`
- Hardware: RunPod, 1x H200 SXM, 4,62 $/h
- Sampling: Modell-Default T=1,0, top_k 128, top_p 0,97; zusätzlich T=0,3 (Runde 2 NIS2/Kanzlei, Runde 3)
- Reasoning: `effort low` über `chat_template_kwargs`
- Läufe: alle am 05.10.2026 (Zeitstempel in den meta.json; Runde 1 ab 18:18, Runde 2 ab 19:32, Runde 3 ab 20:47)
- Systemprompt (Variante 2): „Heute ist der 05.10.2026. Dein Wissen endet am 18.06.2026. …", Wortlaut in `scripts/system.txt` und den meta.json
- Ordnerübersicht: siehe `README.md` in diesem Ordner

## Lastmessung (Messwerte aus dem Bericht)
| Test | Parallel | tok/s | TTFT (s) |
|---|---|---|---|
| 8k-Dokumente | 1 / 8 / 16 / 32 | 77 / 310 / 394 / 473 | 0,65 / 0,92 / 1,53 / 2,44 |
| kurze Prompts | 1 / 4 / 16 / 64 | 144,7 / 489,4 / 1.382 / 3.709 | 0,49 / 0,42 / 0,40 / 0,43 |
Kurze Prompts, p50-Latenz: 1,92 / 2,29 / 2,97 / 3,6 s, 0 Fehler.
Die Roh-JSON der Lasttests (`load.json`) liegt nicht im Repo und kann bei Bedarf ergänzt werden.

## Hinweis zu summary.csv
Siehe `README.md` in diesem Ordner.
