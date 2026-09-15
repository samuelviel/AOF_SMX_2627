#!/usr/bin/env python3
"""
Generador del calendari de sessions del mòdul Aplicacions Ofimàtiques (0223)
1r SMX · Curs 2026-2027 · Samuel Viel Malonda

Edita només el bloc CONFIGURACIÓ i torna a executar:

    python3 tools/calendari.py            # resum per avaluacions
    python3 tools/calendari.py --detall   # totes les sessions, una per línia
    python3 tools/calendari.py --md S3    # taula markdown d'una situació

Si canvia el calendari del centre (festius locals, dates de la FEE...),
toca FESTIUS / PERIODES i el repartiment es recalcula sol.
"""

from datetime import date, timedelta
import sys

# ============================ CONFIGURACIÓ ============================

# Horari setmanal: dia de la setmana (0=dilluns) -> hores de classe
HORARI = {
    0: 2,   # dilluns   12:10-14:00
    1: 1,   # dimarts   13:05-14:00
    2: 2,   # dimecres  12:10-14:00
    3: 2,   # dijous    12:10-14:00
}

TRAMS = {
    0: "12:10-14:00",
    1: "13:05-14:00",
    2: "12:10-14:00",
    3: "12:10-14:00",
}

INICI = date(2026, 9, 15)   # primera sessió del material d'aquest curs
FINAL = date(2027, 6, 17)   # últim dia lectiu

AVALUACIONS = [
    ("1a avaluació", date(2026, 9, 15), date(2026, 12, 3)),
    ("2a avaluació", date(2026, 12, 4), date(2027, 3, 12)),
    ("3a avaluació", date(2027, 3, 13), date(2027, 6, 17)),
]

# Períodes sencers sense classe (vacances, FEE...)
PERIODES = [
    ("Nadal",            date(2026, 12, 23), date(2027, 1, 6)),
    ("Pasqua",           date(2027, 3, 25),  date(2027, 4, 5)),
    ("FEE (empresa)",    date(2027, 5, 24),  date(2027, 6, 17)),
]

# Festius solts
FESTIUS = {
    date(2026, 10, 9):  "9 d'Octubre",
    date(2026, 10, 12): "Festa Nacional",
    date(2026, 12, 7):  "Pont de la Constitució",
    date(2026, 12, 8):  "Immaculada",
    date(2027, 3, 19):  "Sant Josep",
    date(2027, 4, 1):   "Jornada de centre (revisar)",
}

# Repartiment de sessions per situació: (codi, nom, avaluació, nre. sessions).
# Les sessions sobrants de cada avaluació queden com a MARGE al final del tram.
SITUACIONS = [
    ("S0", "Fundem l'empresa",            0,  2),
    ("S1", "Posada en marxa dels equips", 0, 13),
    ("S2", "La identitat documental",     0, 17),
    ("S3", "Comunicació i agenda",        0, 12),
    ("S4", "El control econòmic",         1, 20),
    ("S5", "La imatge de l'empresa",      1, 11),
    ("S6", "Presentem l'empresa",         1, 12),
    ("S7", "Les dades del client",        2, 17),
    ("S8", "El servei d'ajuda",           2, 15),
]

# ======================================================================

DIES = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres"]


def dins_periode(d):
    for nom, ini, fi in PERIODES:
        if ini <= d <= fi:
            return nom
    return None


def sessions():
    out = []
    d = INICI
    while d <= FINAL:
        if d.weekday() in HORARI and d not in FESTIUS and not dins_periode(d):
            out.append({
                "data": d,
                "dia": DIES[d.weekday()],
                "tram": TRAMS[d.weekday()],
                "hores": HORARI[d.weekday()],
            })
        d += timedelta(days=1)
    return out


def avaluacio_de(d):
    for nom, ini, fi in AVALUACIONS:
        if ini <= d <= fi:
            return nom
    return "—"


def assigna(ss):
    """Reparteix les sessions dins de cada avaluació; el sobrant queda com a marge."""
    for s in ss:
        s["sit"], s["sit_nom"], s["num"] = "—", "marge", 0
    for idx, (_, ini, fi) in enumerate(AVALUACIONS):
        tram = [s for s in ss if ini <= s["data"] <= fi]
        i = 0
        for codi, nom, av, n in SITUACIONS:
            if av != idx:
                continue
            for k in range(n):
                if i < len(tram):
                    tram[i]["sit"] = codi
                    tram[i]["sit_nom"] = nom
                    tram[i]["num"] = k + 1
                    i += 1
    return ss


def main():
    ss = assigna(sessions())
    total_h = sum(s["hores"] for s in ss)
    previst = sum(n for _, _, _, n in SITUACIONS)

    if "--detall" in sys.argv:
        for s in ss:
            print(f'{s["data"]:%d/%m/%Y}  {s["dia"]:<9} {s["tram"]}  '
                  f'{s["hores"]}h  {s["sit"]:<3} #{s["num"]}')
        return

    if "--md" in sys.argv:
        codi = sys.argv[sys.argv.index("--md") + 1]
        print("| # | Data | Dia | Hores | Contingut |")
        print("| - | ---- | --- | ----- | --------- |")
        for s in ss:
            if s["sit"] == codi:
                print(f'| {s["num"]} | {s["data"]:%d/%m/%Y} | {s["dia"]} '
                      f'| {s["hores"]}h | |')
        return

    print(f"Sessions lectives: {len(ss)}  ·  Hores totals: {total_h}h")
    print(f"Sessions repartides: {previst}  ·  Marge: {len(ss) - previst}\n")

    for nom, ini, fi in AVALUACIONS:
        tram = [s for s in ss if ini <= s["data"] <= fi]
        h = sum(s["hores"] for s in tram)
        sits = []
        for s in tram:
            if s["sit"] not in sits and s["sit"] != "—":
                sits.append(s["sit"])
        print(f'{nom}: {ini:%d/%m/%Y} → {fi:%d/%m/%Y}  '
              f'{len(tram)} sessions  {h}h  [{", ".join(sits)}]')

    print()
    for codi, nom, av, n in SITUACIONS:
        tram = [s for s in ss if s["sit"] == codi]
        if not tram:
            continue
        h = sum(s["hores"] for s in tram)
        print(f'{codi} {nom:<32} {len(tram):>2} sessions  {h:>3}h  '
              f'{tram[0]["data"]:%d/%m} → {tram[-1]["data"]:%d/%m}')


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
