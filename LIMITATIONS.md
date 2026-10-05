# Grenzen

- Stichprobe, kein Benchmark. Kleine Fallzahlen (z. B. 20 Einrichtungen, 14 Vorfälle).
- Antwortschlüssel KI-erstellt, nicht juristisch geprüft. Grenzfälle haben bewusst keinen Schlüssel.
- Sektorenliste aus Drittquelle (nis2europe.eu), nicht amtlich. Fehler bei Anlage 1/2 sind möglich (Beispiel: Chemie, Autozulieferer).
- Regex-Bewertung ist grob (falsch-negativ bei Umformulierungen, falsch-positiv bei Zufallstreffern). Fehlerzählungen „ausweichend / sicher falsch" beruhen auf einer groben Schlagwortzählung.
- Nur ein Modell, kein Vergleich. Aussagen wie „besser" oder „schlechter" als andere Modelle sind nicht belegt.
- Eine Hardware (H200), eine vLLM-Version, Sampling laut Modell-Default (T=1,0, top_k 128, top_p 0,97) und T=0,3 in Runde 3.
- Verworfene Läufe (Probeläufe, ein Abbruch durch Serverausfall) sind getrennt abgelegt und nicht in den Zahlen.
- Runde 2 wurde nach Korrektur einzelner Checks neu bewertet (Rescore); die Vorher-Stände liegen bei.
- Leere Antworten: 4 von 400 Erstcheck-Läufen (Reasoning-Limit erreicht).
- Gesetzestexte im Prompt: teils wörtlich, teils sinngemäß zusammengefasst (siehe context/).
- Die Modellversion (Wissensstand 18.06.2026) und die Rechtslage können sich ändern.
- Ergebnisse sind kein Rechtsrat.
