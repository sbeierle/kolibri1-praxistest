#!/usr/bin/env python3
"""Erzeugt die Abbildungen des Berichts (PNG) nach ../docs/assets/.
Aufruf: python3 make_figures.py   (benoetigt matplotlib)
Die Werte stammen aus dem Bericht bzw. werden fuer die Einzelfaelle aus ../results/runde3 neu ausgezaehlt."""
import os, re, subprocess, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "docs", "assets")
os.makedirs(OUT, exist_ok=True)

C_KOPF, C_TEXT, C_NEUT, C_GREY, C_DARK = "#D1495B", "#2E6F9E", "#2E6F9E", "#8A8F98", "#222831"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": C_GREY, "axes.labelcolor": C_DARK,
                     "xtick.color": C_DARK, "ytick.color": C_DARK, "figure.dpi": 160})

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor="white")
    plt.close(fig)

# 1) KPI-Kacheln
def kpi():
    tiles = [("rund 145", "Token/s im Einzelstrom,\nerstes Token nach 0,4 s"),
             ("3.709", "Token/s bei 64 parallelen\nkurzen Anfragen, 0 Fehler"),
             ("39 von 40", "Prompt-Injections\nabgewehrt (97,5 %)"),
             ("53 % → 96 %", "NIS2-Einstufung:\naus dem Kopf → mit Gesetzestext"),
             ("77 % → 100 %", "Meldepflicht-Triage:\naus dem Kopf → mit Text"),
             ("20 → 50 von 50", "Fristen komplett richtig:\naus dem Kopf → mit Text")]
    fig, ax = plt.subplots(figsize=(10, 4.2)); ax.axis("off"); ax.set_xlim(0, 3); ax.set_ylim(0, 2)
    for i, (big, small) in enumerate(tiles):
        x, y = i % 3, 1 - i // 3
        ax.add_patch(FancyBboxPatch((x + 0.04, y + 0.06), 0.92, 0.86, boxstyle="round,pad=0.0,rounding_size=0.05",
                                    fc="#F3F6F9", ec="#D5DCE3"))
        ax.text(x + 0.5, y + 0.62, big, ha="center", va="center", fontsize=19, fontweight="bold",
                color=C_TEXT if i < 3 else C_KOPF if False else C_DARK)
        ax.text(x + 0.5, y + 0.28, small, ha="center", va="center", fontsize=10, color="#4A5560")
    ax.set_title("Messwerte aus Runde 1 bis 3", loc="left", fontsize=12, color=C_DARK, pad=8)
    save(fig, "fig_kpi.png")

# 2) Last 8k
def load8k():
    c = [1, 8, 16, 32]; tps = [77, 310, 394, 473]; p50 = [0.96, 1.67, 2.57, 4.28]; ttft = [0.65, 0.92, 1.53, 2.44]
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    labels = [f"{x}\nAntwort {t:.2f} s".replace(".", ",") for x, t in zip(c, p50)]
    b = ax.bar(labels, tps, color=C_NEUT, width=0.55)
    for r, v in zip(b, tps):
        ax.text(r.get_x() + r.get_width() / 2, v + 8, f"{v} tok/s", ha="center", fontsize=10, color=C_DARK)
    ax.set_ylim(0, 540); ax.set_xlabel("Gleichzeitige Anfragen (je 8.000 Token Dokument), darunter Antwortzeit (Median)"); ax.set_ylabel("Token/s gesamt")
    ax.set_title("Last mit langen Dokumenten: Durchsatz wächst 6-fach bei 32-fach mehr Anfragen", loc="left", fontsize=11)
    save(fig, "fig_last_8k.png")

# 3) Last kurze Prompts
def loadshort():
    c = [1, 4, 16, 64]; tps = [144.7, 489.4, 1382, 3709.1]
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    b = ax.bar([str(x) for x in c], tps, color=C_NEUT, width=0.55)
    for r, v in zip(b, tps):
        ax.text(r.get_x() + r.get_width() / 2, v + 60, f"{v:,.0f}".replace(",", "."), ha="center", fontsize=10, color=C_DARK)
    ax.set_ylim(0, 4200); ax.set_xlabel("Gleichzeitige Anfragen (kurze Prompts, effort none, 0 Fehler)"); ax.set_ylabel("Token/s gesamt")
    ax.set_title("Last mit kurzen Prompts: 3.709 Token/s bei 64 parallelen Anfragen", loc="left", fontsize=11)
    save(fig, "fig_last_kurz.png")

# 4) Kopf gegen Text
def kopf_text():
    labels = ["Erstcheck\n(Einstufung)", "Triage\n(erheblich ja/nein)", "Fristen\n(alle 3 Daten)"]
    kopf = [53, 77, 40]; text = [96, 100, 100]
    fig, ax = plt.subplots(figsize=(7.5, 4.4)); w = 0.36; xs = range(3)
    b1 = ax.bar([x - w / 2 for x in xs], kopf, w, color=C_KOPF, label="aus dem Kopf")
    b2 = ax.bar([x + w / 2 for x in xs], text, w, color=C_TEXT, label="mit Gesetzestext im Prompt")
    for bars in (b1, b2):
        for r in bars:
            ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 1.5, f"{r.get_height():.0f} %", ha="center", fontsize=10)
    ax.set_xticks(list(xs)); ax.set_xticklabels(labels); ax.set_ylim(0, 128); ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_ylabel("Anteil richtig (%)")
    ax.legend(loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.02))
    ax.set_title("Runde 3: Ohne Text knapp die Hälfte, mit Text fast alles", loc="left", fontsize=11, pad=22)
    save(fig, "fig_kopf_vs_text.png")

# 5) Hantel je Fall
def dumbbell():
    rate = {}
    for d in ("n_erst_t03", "n_erst_t10"):
        out = subprocess.run([sys.executable, os.path.join(HERE, "nis2_auswertung.py"),
                              os.path.join(HERE, "..", "results", "runde3", d)], capture_output=True, text=True,
                             encoding="utf-8").stdout
        for m in re.finditer(r"^(erst-\d+)([ab])\s+(Erstcheck .*?)\s+\[(Kopf|Text)\]\s+Treffer (\d+)/(\d+)", out, re.M):
            k = (m.group(3).replace("Erstcheck ", ""), m.group(4)); a = rate.setdefault(k, [0, 0])
            a[0] += int(m.group(5)); a[1] += int(m.group(6))
    names = sorted({k[0] for k in rate}, key=lambda n: rate[(n, "Kopf")][0] / rate[(n, "Kopf")][1])
    fig, ax = plt.subplots(figsize=(7.8, 6.2))
    for i, n in enumerate(names):
        k = 100 * rate[(n, "Kopf")][0] / rate[(n, "Kopf")][1]; t = 100 * rate[(n, "Text")][0] / rate[(n, "Text")][1]
        ax.plot([k, t], [i, i], color="#C9CFD6", lw=2.5, zorder=1)
        ax.scatter(k, i, color=C_KOPF, s=55, zorder=2, label="aus dem Kopf" if i == 0 else None)
        ax.scatter(t, i, color=C_TEXT, s=55, zorder=2, label="mit Text" if i == 0 else None)
    ax.set_yticks(range(len(names))); ax.set_yticklabels(names, fontsize=9); ax.set_xlim(-5, 105)
    ax.set_xlabel("Trefferquote je Fall (%), 10 Läufe pro Bedingung")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.08), ncol=2, frameon=False)
    ax.set_title("Erstcheck je Fall: Text hebt fast jeden Fall auf 100 %", loc="left", fontsize=11, pad=26)
    save(fig, "fig_erstcheck_je_fall.png")

# 6) Donuts
def donuts():
    fig, axs = plt.subplots(1, 2, figsize=(8.4, 4.2))
    for ax, (title, vals) in zip(axs, [("Einstufung: 80 Fehlläufe", (34, 46)), ("Triage: 28 Fehlläufe", (25, 3))]):
        ax.pie(vals, colors=[C_GREY, C_KOPF], startangle=90, counterclock=False,
               wedgeprops=dict(width=0.38, edgecolor="white"))
        ax.text(0, 0, f"{sum(vals)}", ha="center", va="center", fontsize=18, fontweight="bold", color=C_DARK)
        ax.set_title(title, fontsize=11, color=C_DARK)
        ax.text(0, -1.38, f"ausweichend {vals[0]} · selbstsicher falsch {vals[1]}", ha="center", fontsize=9.5, color=C_DARK)
        
    from matplotlib.patches import Patch
    fig.legend(handles=[Patch(color=C_GREY, label="ausweichend"), Patch(color=C_KOPF, label="selbstsicher falsch")],
               loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, -0.04))
    fig.suptitle("Fehler aus dem Kopf: meist Ausweichen, selten selbstsicher falsch (grobe Schlagwortzählung)",
                 x=0.02, ha="left", fontsize=10.5)
    save(fig, "fig_fehlerarten.png")

for f in (kpi, load8k, loadshort, kopf_text, dumbbell, donuts):
    f()
print("fertig:", sorted(x for x in os.listdir(OUT) if x.startswith("fig_")))
