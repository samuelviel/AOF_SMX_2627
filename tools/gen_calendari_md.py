#!/usr/bin/env python3
"""Genera docs/recursos/calendari.md a partir de tools/calendari.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calendari import (sessions, assigna, AVALUACIONS, PERIODES, FESTIUS,
                       SITUACIONS, HORARI, TRAMS, DIES)

ss = assigna(sessions())
NOMS = {c: n for c, n, _, _ in SITUACIONS}
out = []
w = out.append

w("# Calendari complet\n")
w("!!! warning \"Calendari de treball, no calendari oficial\"")
w("    Estes dates estan calculades a partir de l'horari del grup i del calendari")
w("    escolar previst. Si el centre publica canvis (festius locals, dates de la FEE),")
w("    s'actualitzen ací i el repartiment es recalcula sol.\n")

w("## L'horari setmanal\n")
w("| Dia | Tram | Hores |")
w("| --- | --- | --- |")
for d in sorted(HORARI):
    w(f"| {DIES[d]} | {TRAMS[d]} | {HORARI[d]} h |")
w(f"\n**{sum(HORARI.values())} hores setmanals** · Aula 201 · grup 1SMXb\n")

tot_h = sum(s['hores'] for s in ss)
w(f"Total del curs: **{len(ss)} sessions · {tot_h} hores**.\n")

w("## Resum per situació\n")
w("| Situació | Sessions | Hores | Del | Al |")
w("| --- | --- | --- | --- | --- |")
for codi, nom, av, n in SITUACIONS:
    tram = [s for s in ss if s['sit'] == codi]
    if not tram:
        continue
    h = sum(s['hores'] for s in tram)
    w(f"| **{codi}** · {nom} | {len(tram)} | {h} h | "
      f"{tram[0]['data']:%d/%m/%Y} | {tram[-1]['data']:%d/%m/%Y} |")
marge = [s for s in ss if s['sit'] == '—']
if marge:
    w(f"| *Marge* | {len(marge)} | {sum(s['hores'] for s in marge)} h | — | — |")

w("\n!!! info \"Per a què serveix el marge\"")
w("    Són sessions reservades sense contingut assignat. Absorbeixen el que sempre passa:")
w("    una activitat que s'allarga, una vaga, un simulacre d'incendi, una sortida.")
w("    Si no fan falta, es dediquen a reforç o a millorar lliuraments.\n")

w("## Dies sense classe previstos\n")
w("| Període | Dates |")
w("| --- | --- |")
for nom, i, f in PERIODES:
    w(f"| {nom} | {i:%d/%m/%Y} → {f:%d/%m/%Y} |")
for d in sorted(FESTIUS):
    if d.weekday() in HORARI:
        w(f"| {FESTIUS[d]} | {d:%d/%m/%Y} ({DIES[d.weekday()]}) |")

w("\n## Sessió a sessió\n")
for nom_av, ini, fi in AVALUACIONS:
    tram = [s for s in ss if ini <= s['data'] <= fi]
    h = sum(s['hores'] for s in tram)
    w(f"### {nom_av} · {ini:%d/%m/%Y} → {fi:%d/%m/%Y}\n")
    w(f"{len(tram)} sessions · {h} hores\n")
    w('??? abstract "Desplega el detall"\n')
    w("    | Data | Dia | Hores | Situació | Sessió |")
    w("    | --- | --- | --- | --- | --- |")
    for s in tram:
        sit = f"{s['sit']} · {NOMS.get(s['sit'], 'marge')}" if s['sit'] != '—' else "*marge*"
        num = f"#{s['num']}" if s['num'] else "—"
        w(f"    | {s['data']:%d/%m/%Y} | {s['dia']} | {s['hores']} h | {sit} | {num} |")
    w("")

w("---\n")
w("Este fitxer es genera amb `python3 tools/gen_calendari_md.py`. No l'edites a mà:")
w("toca la configuració de `tools/calendari.py` i torna a executar-lo.")

dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', 'docs', 'recursos', 'calendari.md')
open(dest, 'w').write("\n".join(out) + "\n")
print(f"Escrit {dest} ({len(out)} línies)")
