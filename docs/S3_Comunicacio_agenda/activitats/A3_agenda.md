# A3 · L'agenda compartida

**Sessió 8** · lliurament: calendari compartit + protocol d'ús
**Avalua:** RA8 <span class="ca">b</span> <span class="ca">d</span> <span class="ca">g</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

Dimarts passat vam enviar dos tècnics al mateix client a la mateixa hora i cap dels dos va anar a l'Ajuntament, que era on tocava.

Munteu el calendari de l'equip i, sobretot, **poseu-vos d'acord en com s'usa**. Un calendari que cadascú omple com vol no serveix de res.
</div>

## Part 1 · Muntar l'estructura

<span class="ca">CA g</span> Crea **tres calendaris separats** amb colors i permisos diferents:

| Calendari | Contingut | Compartició |
| --- | --- | --- |
| `Equip` | Visites, reunions, terminis compartits | Lectura completa per a l'equip |
| `Guàrdies` | Torns de la [mesa d'ajuda](../../recursos/mesa_ajuda.md) | Lectura completa per a l'equip |
| `Personal` | El teu | Només disponibilitat |

## Part 2 · Poblar-lo amb un escenari real

Carrega les **tres properes setmanes** de la vostra empresa amb, com a mínim:

- [ ] 4 esdeveniments amb convidats, ubicació i descripció útil
- [ ] 1 esdeveniment **recurrent** (els torns de guàrdia setmanals)
- [ ] 1 modificació **d'una sola ocurrència** d'eixa recurrència, documentada amb captura
- [ ] 2 tasques amb venciment (no esdeveniments: tasques)
- [ ] 1 esdeveniment de tot el dia
- [ ] 1 entrada marcada com a **lliure** tot i ocupar franja, amb explicació de per què

Tots els esdeveniments han de complir el format de títol que acordeu al protocol.

## Part 3 · Sincronitzar amb un dispositiu

<span class="ca">CA d</span> Connecta el calendari de l'equip a un segon dispositiu o client (mòbil, o un altre client d'escriptori).

Documenta:

1. **Quin mètode has usat** — CalDAV, compte del proveïdor, subscripció `.ics` — i **per què eixe i no un altre**
2. **Prova de sincronització bidireccional:** crea una entrada al dispositiu A, comprova que apareix al B; modifica-la al B, comprova que canvia al A. Amb captures i marca de temps.
3. **Prova de zona horària:** canvia la zona horària d'un dispositiu, mira què passa amb els esdeveniments i torna-ho a deixar bé. Explica el que has vist.

!!! tip "Si no pots usar el mòbil"
    No cal un telèfon. Val un segon client d'escriptori, un navegador amb una altra sessió, o una màquina virtual. El que s'avalua és que entengues **el mecanisme de sincronització**, no que tingues un dispositiu concret.

!!! warning "Privacitat"
    Si sincronitzes amb el teu mòbil personal, **desconnecta el compte en acabar** i no deixes cap credencial a l'equip de l'aula. I no publiques al lliurament cap captura amb dades personals teues o de tercers: tapa-les.

## Part 4 · El protocol d'ús

<span class="ca">CA b</span> Una pàgina, acordada en equip, que respon les sis preguntes de [T3](../teoria/3_agenda.md):

1. Què va al calendari d'equip i què no
2. Format del títol de les entrades — amb **dos exemples reals**
3. Antelació mínima per a convocar
4. Què significa que algú aparega com a ocupat
5. Qui pot escriure al calendari d'altres
6. Com es resol un conflicte d'horari

I un apartat final: **quins problemes concrets evita cada norma**. Una norma sense problema associat és una norma que ningú complirà.

## Com s'avalua

### RA8.g) Opcions d'agenda utilitzades — 40 %

- 🟢 Tres calendaris amb permisos diferenciats i tots els elements de la part 2, amb esdeveniments que **s'entenen sense preguntar** (títol, ubicació, descripció, recordatori amb antelació raonable). La modificació d'una sola ocurrència està feta i evidenciada. La distinció tasca/esdeveniment és correcta.
- 🔵 Tot present i funcionant, però alguns esdeveniments són pobres en informació o el recordatori no té sentit pràctic.
- 🟡 Falten elements de la llista, o es confonen tasques amb esdeveniments, o els tres calendaris tenen els mateixos permisos.
- 🔴 Un sol calendari amb entrades soltes.

### RA8.d) Agendes sincronitzades amb dispositius — 35 %

- 🟢 Sincronització funcionant amb el mètode **justificat** (i sabent distingir subscripció de compte). Prova bidireccional documentada amb evidència temporal. Prova de zona horària feta i explicada correctament.
- 🔵 Sincronització funcionant i documentada, però la prova és només en un sentit o falta la de zona horària.
- 🟡 S'ha afegit una subscripció `.ics` de només lectura i es presenta com a sincronització.
- 🔴 No hi ha segon dispositiu ni prova.

### RA8.b) Necessitats de gestió analitzades — 25 %

- 🟢 Protocol amb les sis preguntes resoltes, amb exemples concrets, i **cada norma lligada al problema que evita**. És un document que un equip podria adoptar tal qual.
- 🔵 Protocol complet però amb alguna norma genèrica o sense problema associat.
- 🟡 Protocol incomplet o escrit com a llista de bones intencions.
- 🔴 No hi ha protocol.

!!! quote "Punt de comprensió"
    *"Un client extern vol quedar amb tu la setmana que ve. Què li compartirries exactament i per què no més que això?"*
