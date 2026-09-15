# A1 · La plantilla corporativa

**Sessions 4 a 7** · lliurament: `.ott` o `.dotx` + PDF de mostra + fitxa de configuració
**Avalua:** RA2 <span class="ca">a</span> <span class="ca">b</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

Cada document que ix d'esta empresa sembla fet per una empresa diferent.

Vull una plantilla que ho arregle. I quan dic plantilla no vull dir un document bonic que després cadascú copia i pega: vull un fitxer que òbriga amb tot posat, i que si demà canviem el color corporatiu, es canvie en tots els documents nous sense tocar res més.
</div>

## Part 1 · Les decisions de marca

Abans de tocar el programa, decidiu **en equip** i deixeu-ho escrit. Són decisions d'empresa, no preferències personals.

| Decisió | Restricció |
| --- | --- |
| **Dos colors corporatius** (hex) | Han de contrastar prou per a llegir-se. Comprova que funcionen també en escala de grisos: molts documents s'imprimeixen en blanc i negre |
| **Dues tipografies**: títols i cos | **Han d'estar disponibles als equips del client.** Una tipografia preciosa que el client no té es substitueix i el document es descol·loca |
| **Marges** | Coherents amb enquadernació si el document s'imprimeix |
| **Capçalera i peu** | Què hi va en cadascun |
| **Tractament** | Tu o vosté als documents a client |

!!! warning "La trampa de la tipografia"
    És l'error més comú d'esta activitat. Trieu una font de moda, es veu bé al vostre equip, i el document arriba al client amb una altra font i tota la maquetació moguda.

    Tria fonts **de llicència lliure i àmpliament disponibles**, i incrusta-les quan exportes a PDF. Documenta la decisió: forma part del CA (b).

## Part 2 · Construir el joc d'estils

El mínim exigible, tal com es descriu a [T2](../teoria/2_estils.md):

**Estils de paràgraf** — Títol 1, Títol 2, Títol 3, Cos de text, Cita, Peu de figura, Peu de taula
**Estils de caràcter** — Codi, Terme destacat, Ruta de menú
**Estils de pàgina** — Portada, Estàndard, Horitzontal
**Estils de llista** — Passos numerats, Punts

Requisits que es comprovaran:

- [ ] Cada estil **hereta de qui toca**. Canviar la font a l'estil base ha de propagar-se.
- [ ] Els estils de títol estan vinculats a la **numeració de capítols**.
- [ ] Els estils porten **l'idioma** fixat (i "Codi" té l'idioma desactivat perquè el corrector no el subratlle).
- [ ] L'estil "Portada" no té capçalera ni peu.
- [ ] L'estil "Estàndard" té capçalera amb el nom de l'empresa i peu amb `Pàgina X de Y` **amb camps**.

### La prova del canvi de color

Este és el criteri que separa una plantilla de veritat d'un document maquillat:

> **Canvia el color corporatiu principal tocant un sol lloc.** Si has d'entrar en cinc estils diferents, el joc d'herència no està ben construït.

Ho comprovaré en directe al punt de comprensió.

## Part 3 · Empaquetar i provar

1. **Camps a la portada** lligats a propietats del document (títol, autor, data) i un camp d'entrada per al nom del client.
2. `Fitxer → Plantilles → Desa com a plantilla`.
3. **Prova-la de veritat:** crea un document nou des de la plantilla, escriu tres apartats amb els seus estils, insereix una figura amb llegenda i genera l'índex. Si alguna cosa no ix sola, torna a la plantilla i arregla-ho.
4. Exporta eixe document de prova a PDF: és el teu **PDF de mostra**.

## La fitxa de configuració

<span class="ca">CA a</span> Un full a banda amb la personalització de l'entorn que has aplicat, en el format de [T1](../teoria/1_entorn.md):

| Paràmetre | Ruta exacta | Valor | Per què |
| --- | --- | --- | --- |

Mínim quatre entrades, de les quals **almenys dues han d'estar relacionades amb el treball d'esta situació** (autocorrecció que trencava el codi, drecera per a l'estil de caràcter, etc.). Configurar el color del fons de la finestra no compta com a decisió professional.

## Què es lliura

- Fitxer de plantilla (`.ott` o `.dotx`)
- Document de mostra en PDF amb índex generat
- Fitxa de configuració (pot anar dins del PDF de mostra)
- [Nota d'ús d'IA](../../recursos/ia.md) si n'has usat

## Com s'avalua

### RA2.a) Opcions de programari i barra d'eines personalitzades — 30 %

- 🟢 Fitxa amb quatre o més paràmetres, **ruta exacta i valor**, i cada decisió justificada per una necessitat real de la faena. Inclou almenys una personalització d'interfície (barra o drecera) i una de comportament.
- 🔵 Fitxa completa i reproduïble, però alguna justificació és genèrica o falta una de les dues categories.
- 🟡 Es llisten canvis sense ruta (irreproduïbles) o sense motiu.
- 🔴 No hi ha fitxa, o només recull configuració estètica sense impacte en la faena.

### RA2.b) Plantilla dissenyada — 70 %

- 🟢 Plantilla real (`.ott`/`.dotx`) amb el joc d'estils complet, **herència ben construïda** (el canvi de color es fa en un sol lloc), numeració de capítols vinculada, tres estils de pàgina funcionant, camps a portada, capçalera i peu, i idioma fixat als estils. El document de mostra genera l'índex sol. Les decisions de marca estan justificades, incloent-hi la disponibilitat de les fonts.
- 🔵 Plantilla funcional amb el joc d'estils complet, però amb algun punt fluix: herència parcial, algun format directe colat, o decisions de marca sense justificar.
- 🟡 És un document amb estils aplicats però **no s'ha desat com a plantilla**, o falten estils del mínim, o els títols no generen índex.
- 🔴 Format aplicat a mà, sense estils; o la "plantilla" és un `.odt`/`.docx` normal.

!!! danger "Causa automàtica de nivell esborrany"
    Si trobe **format directe** sobre text que ja té estil (negreta posada a mà sobre un títol, per exemple), el CA (b) no passa de 🟡.

    No és per rigidesa: és que eixe format directe és exactament el que farà que la plantilla falle d'ací a dos mesos, quan algú canvie un estil i eixe tros no canvie.
