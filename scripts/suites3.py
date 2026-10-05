# -*- coding: utf-8 -*-
"""Suiten erstcheck und triage (NIS2 im Praxisfall).

erstcheck  20 fiktive Einrichtungen: besonders wichtig / wichtig / nicht betroffen (BSIG § 28, Anlagen 1 und 2).
triage     12 Vorfallbeschreibungen (erheblicher Sicherheitsvorfall ja/nein) + 5 Fristrechnungen (BSIG § 32).
Jeder Fall in zwei Bedingungen: 'a' = aus dem Kopf, 'b' = mit Gesetzestext/Sektorenliste im Prompt.

WICHTIG: Die Antwortschluessel stammen von Claude (KI), nicht von einem Juristen. Einstufungen nach § 28 BSIG
und den Sektorenlisten (Drittquelle, nicht amtlich) -> [pruefen]. Grenzfaelle sind ohne Schluessel (manuell).
"""
import datetime as dt

_ERST_FORMAT = ('Antworte ausschließlich mit JSON in diesem Format: '
                '{"einstufung": "besonders_wichtig" | "wichtig" | "nicht_betroffen", "begruendung": "ein bis zwei Sätze"}')
_ERST_A = ("Ordne die folgende Einrichtung nach dem deutschen NIS2-Umsetzungsrecht (BSI-Gesetz) ein. " + _ERST_FORMAT + "\n\n")
_ERST_B = ("Ordne die folgende Einrichtung ausschließlich auf Grundlage des folgenden Textes ein. Wenn der Text nicht ausreicht, wähle die "
           "wahrscheinlichste Einstufung und nenne die Unsicherheit in der Begründung. " + _ERST_FORMAT +
           "\n\n<<<TEXT\n{{CONTEXT:nis2_erstcheck.txt}}\nTEXT>>>\n\n")

# (kurz, Beschreibung, Mitarbeiter, Umsatz Mio, Bilanz Mio, Erwartung oder None=Grenzfall/manuell)
ERST_CASES = [
    ("Stromlieferant", "Energieversorger, der Haushalte und Gewerbe mit Strom beliefert", 320, 90, 60, "besonders_wichtig"),
    ("Maschinenbau mittel", "Hersteller von Werkzeugmaschinen (Maschinenbau)", 120, 30, 22, "wichtig"),
    ("Maschinenbau groß", "Hersteller von Werkzeugmaschinen (Maschinenbau)", 380, 120, 90, "wichtig"),
    ("Maschinenbau klein", "Hersteller von Sondermaschinen (Maschinenbau)", 35, 6, 5, "nicht_betroffen"),
    ("Lebensmittel industriell", "Industrieller Hersteller von Backwaren und Fertiggerichten", 140, 28, 15, "wichtig"),
    ("Arztpraxis", "Hausarztpraxis", 8, 1.2, 0.6, "nicht_betroffen"),
    ("Privatklinik", "Privatklinik, erbringt stationäre Gesundheitsdienstleistungen", 450, 55, 48, "besonders_wichtig"),
    ("Managed Service Provider", "IT-Dienstleister, der die IT-Infrastruktur seiner Kunden im Auftrag betreibt und überwacht (Managed Service Provider)", 80, 12, 6, "wichtig"),
    ("Managed Security Provider", "Anbieter von Managed Security Services mit eigenem Security Operations Center", 300, 70, 50, "besonders_wichtig"),
    ("Anwaltskanzlei", "Wirtschaftskanzlei", 25, 5, 2, "nicht_betroffen"),
    ("Cloud-Anbieter", "Anbieter von Cloud-Computing-Diensten für Unternehmen", 60, 11, 8, "wichtig"),
    ("DNS-Anbieter", "Betreiber eines autoritativen DNS-Dienstes für Kunden (DNS-Diensteanbieter)", 12, 2, 1, "besonders_wichtig"),
    ("Vertrauensdiensteanbieter", "Qualifizierter Vertrauensdiensteanbieter (qualifizierte Zertifikate und Zeitstempel)", 9, 1.5, 1, "besonders_wichtig"),
    ("Online-Marktplatz", "Betreiber eines Online-Marktplatzes für Handwerksleistungen", 70, 18, 9, "wichtig"),
    ("Paketdienst", "Paket- und Kurierdienst", 400, 150, 100, "wichtig"),
    ("Chemiehersteller", "Hersteller von chemischen Stoffen und Gemischen", 260, 90, 70, "wichtig"),
    ("Autozulieferer", "Hersteller von Kraftwagenteilen", 520, 210, 150, "wichtig"),
    ("Systemhaus Handel", "Systemhaus: verkauft IT-Hardware und Lizenzen und führt Einzelprojekte durch, betreibt keine Kundeninfrastruktur", 60, 14, 6, None),
    ("Softwarehersteller", "Hersteller von Standard-Branchensoftware (ERP), ohne eigenen Hosting- oder Cloud-Betrieb", 200, 40, 20, None),
    ("Spedition", "Spedition für Güterverkehr auf der Straße", 90, 16, 9, None),
]


def _case_text(desc, ma, um, bi):
    return f"Einrichtung: {desc}.\nMitarbeiter: {ma}.\nJahresumsatz: {um} Mio. EUR.\nJahresbilanzsumme: {bi} Mio. EUR."


def erstcheck_tests():
    out = []
    for i, (short, desc, ma, um, bi, exp) in enumerate(ERST_CASES, 1):
        for cond, intro in (("a", _ERST_A), ("b", _ERST_B)):
            checks = [("jsoneq", {"einstufung": [exp]})] if exp else []
            out.append(dict(id=f"erst-{i:02d}{cond}", suite="erstcheck",
                            title=f"Erstcheck {short} [{'Kopf' if cond == 'a' else 'Text'}]",
                            prompt=intro + _case_text(desc, ma, um, bi),
                            key=f"[pruefen] erwartet: {exp or 'Grenzfall, manuell lesen'} (BSIG § 28, Anlagen 1/2).", checks=checks))
    return out


# ----------------------------------------------------------------- Triage
_TRI_FORMAT = 'Antworte ausschließlich mit JSON: {"erheblich": true | false, "begruendung": "ein bis zwei Sätze"}'
_TRI_A = ("Handelt es sich bei folgendem Vorfall um einen erheblichen Sicherheitsvorfall nach dem deutschen NIS2-Umsetzungsrecht "
          "(BSI-Gesetz)? " + _TRI_FORMAT + "\n\nVorfall: ")
_TRI_B = ("Handelt es sich bei folgendem Vorfall um einen erheblichen Sicherheitsvorfall? Antworte ausschließlich auf Grundlage des folgenden Textes. "
          + _TRI_FORMAT + "\n\n<<<TEXT\n{{CONTEXT:nis2_triage.txt}}\nTEXT>>>\n\nVorfall: ")
TRI_CASES = [
    ("Ransomware Produktion", "Ransomware verschlüsselt ERP und Produktionssteuerung. Die Produktion steht seit drei Tagen still, es liegt eine Lösegeldforderung vor.", True),
    ("Datenabfluss Kunden", "Angreifer haben eine Datenbank mit 40.000 Kundendatensätzen (Namen, Adressen, Bankverbindungen) kopiert und im Darknet angeboten.", True),
    ("DDoS Webshop", "Ein DDoS-Angriff legt den Online-Shop, der 80 Prozent des Umsatzes erzeugt, 14 Stunden lahm. Geschätzter Verlust: 250.000 EUR.", True),
    ("Domänen-Admin kompromittiert", "Ein Domänen-Administrator-Konto war neun Tage lang in Angreiferhand. Zugriff auf Fileserver und Backup-Systeme, Konstruktionsdaten wurden abgezogen.", True),
    ("Rechenzentrum Ausfall", "Durch eine Fehlkonfiguration fällt die Steuerung eines Rechenzentrums sechs Stunden aus. 120 Kunden sind ohne Dienst, es drohen Vertragsstrafen.", True),
    ("Lieferkette Update", "Ein manipuliertes Update der Fernwartungssoftware eines IT-Dienstleisters hat Schadcode auf 35 Kundensystemen installiert.", True),
    ("Phishing abgefangen", "Ein Mitarbeiter klickt auf einen Phishing-Link. Der Endpoint-Schutz blockiert den Download, das Passwort wird zurückgesetzt, es sind keine Daten abgeflossen.", False),
    ("Trojaner Laptop", "Der Virenscanner blockiert einen Trojaner auf einem einzelnen Laptop. Das Gerät wird neu aufgesetzt, es gab keine weiteren Auswirkungen.", False),
    ("Brute Force blockiert", "Die Firewall protokolliert 2.000 fehlgeschlagene Anmeldeversuche aus dem Ausland. Alle wurden blockiert, es gab keinen Zugriff.", False),
    ("Druckerserver", "Der Druckerserver fällt wegen eines Updates 40 Minuten aus. Mitarbeiter drucken danach nach.", False),
    ("Spam-Welle", "300 Spam-Mails mit Schadlink treffen ein. Der Mailfilter fängt alle ab.", False),
    ("Geplante Wartung", "Geplante Wartung des Mailservers, zwei Stunden außerhalb der Geschäftszeiten, vorher angekündigt.", False),
    ("Grenzfall Website", "Die Firmenwebsite (reine Informationsseite) ist drei Stunden nicht erreichbar, die Ursache ist unklar.", None),
    ("Grenzfall Laptop", "Ein unverschlüsselter Laptop mit 200 Kundendatensätzen wurde im Zug liegen gelassen und ist verschwunden.", None),
]

# Fristfaelle: Startzeitpunkt, 72h-Meldung am Tag X, Abschluss = X + 1 Monat. Auswahl so, dass kein Wochenende/Feiertag im Weg ist.
_MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
_START = [dt.datetime(2026, 10, 6, 8, 15), dt.datetime(2026, 10, 20, 14, 30), dt.datetime(2026, 12, 1, 9, 5), dt.datetime(2026, 12, 15, 16, 40), dt.datetime(2027, 1, 5, 11, 0)]


def _plus_month(d):
    y, m = (d.year + 1, 1) if d.month == 12 else (d.year, d.month + 1)
    return d.replace(year=y, month=m)


def _date_rx(d, with_year=False):
    day, mon = d.day, d.month
    base = rf"0?{day}\.\s?0?{mon}\.|{day}\.\s?{_MONATE[mon-1]}"
    return base


FRISTEN = []
for _s in _START:
    _24, _72 = _s + dt.timedelta(hours=24), _s + dt.timedelta(hours=72)
    _ab = _plus_month(_72)
    FRISTEN.append((_s, _24, _72, _ab))


def triage_tests():
    out = []
    for i, (short, text, exp) in enumerate(TRI_CASES, 1):
        for cond, intro in (("a", _TRI_A), ("b", _TRI_B)):
            checks = [("jsoneq", {"erheblich": ["true" if exp else "false"]})] if exp is not None else []
            out.append(dict(id=f"tri-{i:02d}{cond}", suite="triage", title=f"Triage {short} [{'Kopf' if cond == 'a' else 'Text'}]",
                            prompt=intro + text, key=f"[pruefen] erwartet: {exp if exp is not None else 'Grenzfall, manuell lesen'} (BSIG § 2 Nr. 11).", checks=checks))
    for j, (s, d24, d72, ab) in enumerate(FRISTEN, 1):
        q = (f"Wir stellen am {s.strftime('%d.%m.%Y')} um {s.strftime('%H:%M')} Uhr einen erheblichen Sicherheitsvorfall fest. "
             f"Bis wann müssen wir (1) die frühe Erstmeldung und (2) die Vorfallmeldung abgeben? Und bis wann spätestens die Abschlussmeldung, "
             f"wenn wir die Vorfallmeldung nach (2) am spätestmöglichen Tag übermitteln? Nenne konkrete Daten und Uhrzeiten und die Vorschrift.")
        for cond, intro in (("a", "Beantworte die Frage nach dem deutschen BSI-Gesetz (NIS2-Umsetzung).\n\n"),
                            ("b", "Beantworte die Frage ausschließlich auf Grundlage des folgenden Textes.\n\n<<<TEXT\n{{CONTEXT:nis2_triage.txt}}\nTEXT>>>\n\n")):
            checks = [("all", [(_date_rx(d24), d24.strftime("%d.%m.%Y")), (_date_rx(d72), d72.strftime("%d.%m.%Y")), (_date_rx(ab), ab.strftime("%d.%m.%Y"))]),
                      ("any", [(r"§\s?32", "§ 32 BSIG")])]
            out.append(dict(id=f"fri-{j:02d}{cond}", suite="triage", title=f"Fristen ab {s.strftime('%d.%m.')} {s.strftime('%H:%M')} [{'Kopf' if cond == 'a' else 'Text'}]",
                            prompt=intro + q, key=f"24h: {d24:%d.%m. %H:%M}; 72h: {d72:%d.%m. %H:%M}; Abschluss bis {ab:%d.%m.%Y} (§ 32 Abs. 1 Nr. 1, 2, 4 BSIG; alle Tage Werktage, keine Fristverschiebung).", checks=checks))
    return out
