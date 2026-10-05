# -*- coding: utf-8 -*-
"""Suiten luecken (Massnahmen-Lueckencheck nach § 30 BSIG) und beleg (Belegextraktion als JSON).
Alle Faelle sind synthetisch (feste Zufallsbasis), Schluessel entstehen aus der Konstruktion. Kein Rechtsrat."""
import random
from decimal import Decimal, ROUND_HALF_UP

# ---------------------------------------------------------------- Lueckencheck
TOPICS = {
    "mfa": ("Alle Fernzugänge und Administratorkonten sind durch Mehr-Faktor-Authentifizierung geschützt.", "Anmeldung an VPN, Mail und Admin-Konten nur mit Passwort, keine Mehr-Faktor-Authentifizierung."),
    "backup": ("Tägliche Datensicherung auf ein getrenntes, offline gehaltenes Medium, Rücksicherung wird quartalsweise getestet.", "Das einzige Backup liegt auf demselben NAS wie die Produktivdaten, ein Rücksicherungstest hat nie stattgefunden."),
    "patchmanagement": ("Sicherheitsupdates werden für Server und Clients innerhalb von 14 Tagen eingespielt.", "Updates werden nur unregelmäßig eingespielt, einige Server laufen seit Jahren ohne Sicherheitsupdates."),
    "schulung": ("Alle Mitarbeitenden erhalten jährlich eine Schulung zu Phishing und Informationssicherheit.", "Es gibt keinerlei Schulungen oder Sensibilisierung zur Informationssicherheit."),
    "notfallplan": ("Ein dokumentierter Notfallplan für IT-Ausfälle und Cyberangriffe liegt vor und wird jährlich geübt.", "Einen Notfallplan oder Wiederanlaufplan gibt es nicht, im Ernstfall würde improvisiert."),
    "verschluesselung": ("Laptops und mobile Datenträger sind verschlüsselt, Datenübertragung läuft verschlüsselt.", "Laptops, USB-Sticks und Dateiübertragung sind unverschlüsselt."),
    "zugriffskonzept": ("Zugriffsrechte sind nach Rollen vergeben und werden halbjährlich überprüft.", "Alle Mitarbeitenden haben Zugriff auf alle Laufwerke, Rechte werden nie überprüft."),
    "lieferkette": ("Wichtige Dienstleister werden auf ihre Informationssicherheit geprüft, Anforderungen stehen in den Verträgen.", "Dienstleister und Zulieferer werden nie auf Sicherheit geprüft, Verträge enthalten keine Sicherheitsanforderungen."),
    "risikoanalyse": ("Eine Risikoanalyse für die IT-Systeme liegt vor und wird jährlich aktualisiert.", "Eine Risikoanalyse hat nie stattgefunden."),
    "meldeprozess": ("Ein Prozess zur Erkennung und Meldung von Sicherheitsvorfällen ist festgelegt, Verantwortliche sind benannt.", "Wer Sicherheitsvorfälle erkennt, bewertet und meldet, ist nirgends festgelegt."),
}
_LUE_PROMPT = ('Prüfe den folgenden Ist-Zustand eines Unternehmens anhand des Textes zu den Risikomanagementmaßnahmen (§ 30 BSIG). '
               'Nenne ausschließlich Maßnahmen, die laut Ist-Zustand FEHLEN oder mangelhaft sind. Was als vorhanden beschrieben ist, nennst du nicht. '
               'Antworte ausschließlich mit JSON: {{"luecken": [Liste aus: {vocab}], "begruendung": "ein Satz je Lücke"}}\n\n'
               '<<<TEXT\n{{{{CONTEXT:recht.txt}}}}\nTEXT>>>\n\nIst-Zustand:\n')


def luecken_tests():
    rnd = random.Random(30)
    vocab = ", ".join(f'"{k}"' for k in TOPICS)
    out = []
    for i in range(1, 9):
        gaps = set(rnd.sample(list(TOPICS), rnd.choice([2, 3, 3, 4])))
        order = list(TOPICS)
        rnd.shuffle(order)
        lines = [("- " + (TOPICS[k][1] if k in gaps else TOPICS[k][0])) for k in order]
        must = sorted(gaps)
        mustnot = sorted(set(TOPICS) - gaps)
        out.append(dict(id=f"luk-{i:02d}", suite="luecken", title=f"Lückencheck {i} (Lücken: {', '.join(must)})",
                        prompt=_LUE_PROMPT.format(vocab=vocab) + "\n".join(lines),
                        key=f"Eingebaute Lücken: {', '.join(must)}. Alle anderen Themen sind als erfüllt beschrieben (Nennung = erfunden).",
                        checks=[("jsonlist", "luecken", must, mustnot)]))
    return out


# ---------------------------------------------------------------- Belegextraktion
def _eur(d):
    s = f"{d:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s + " €"


_FIRMEN = ["Müller Bürobedarf GmbH", "Schwarzwald IT-Service GmbH & Co. KG", "Karlsruher Druckhaus e.K.", "Rheinland Logistik AG", "Beyer & Söhne Elektrotechnik",
           "Pfinztal Catering GmbH", "Nordwest Software Solutions GmbH", "Albtal Reinigungsdienste", "Heidelberger Fachverlag GmbH", "Bodensee Metallbau GmbH"]


def beleg_tests():
    rnd = random.Random(2026)
    out = []
    for i in range(1, 21):
        firma = rnd.choice(_FIRMEN)
        nr = f"RE-2026-{rnd.randint(1000, 9999)}"
        tag = rnd.randint(1, 28); mon = rnd.randint(1, 9)
        datum = f"{tag:02d}.{mon:02d}.2026"
        iso = f"2026-{mon:02d}-{tag:02d}"
        netto = (Decimal(rnd.randint(2000, 480000)) / 100).quantize(Decimal("0.01"))
        satz = rnd.choice([19, 19, 19, 7])
        ust = (netto * satz / 100).quantize(Decimal("0.01"), ROUND_HALF_UP)
        brutto = netto + ust
        lay = i % 3
        lz = f"{rnd.randint(1, 28):02d}.{max(mon-1,1):02d}.2026"
        if lay == 0:
            txt = (f"{firma}\nRechnung Nr. {nr}\nRechnungsdatum: {datum}\nLeistungszeitraum: bis {lz}\n\nPosition 1: Dienstleistung / Lieferung   {_eur(netto)}\n"
                   f"Zwischensumme netto: {_eur(netto)}\nUmsatzsteuer {satz} %: {_eur(ust)}\nGesamtbetrag brutto: {_eur(brutto)}\n"
                   f"Zahlbar innerhalb von 14 Tagen netto, bei Zahlung binnen 7 Tagen 2 % Skonto.")
        elif lay == 1:
            txt = (f"RECHNUNG\nAussteller: {firma}\nBeleg-Nr.: {nr} | Datum {datum} | Lieferdatum {lz}\n"
                   f"Nettobetrag ........ {_eur(netto)}\nMwSt {satz}% ........ {_eur(ust)}\nSumme ........ {_eur(brutto)}\nVielen Dank für Ihren Auftrag!")
        else:
            txt = (f"{firma} - Rechnung\nvom {datum} (Leistung erbracht am {lz})\nRechnungsnummer: {nr}\n"
                   f"Betrag ohne USt.: {_eur(netto)}\nzzgl. {satz} % USt: {_eur(ust)}\nRechnungsbetrag (brutto): {_eur(brutto)}\nBitte überweisen Sie auf das angegebene Konto.")
        prompt = ("Extrahiere aus dem folgenden Beleg die Felder. Zahlen mit Punkt als Dezimaltrenner, ohne Tausenderpunkt und ohne Währungszeichen. "
                  "Datum im Format JJJJ-MM-TT (Rechnungsdatum, nicht Leistungsdatum). Antworte ausschließlich mit JSON: "
                  '{"lieferant": "...", "rechnungsnummer": "...", "rechnungsdatum": "...", "netto": 0.00, "ust_satz": 19, "ust_betrag": 0.00, "brutto": 0.00}\n\nBeleg:\n' + txt)
        exp = {"lieferant": [firma], "rechnungsnummer": [nr], "rechnungsdatum": [iso], "netto": [str(netto)], "ust_satz": [str(satz)],
               "ust_betrag": [str(ust)], "brutto": [str(brutto)]}
        out.append(dict(id=f"bel-{i:02d}", suite="beleg", title=f"Beleg {i} ({'Layout ' + str(lay + 1)}, {satz} % USt)", prompt=prompt,
                        key=f"{firma}; {nr}; {iso}; netto {netto}; USt {satz}% = {ust}; brutto {brutto}", checks=[("jsoneq", exp)]))
    return out
