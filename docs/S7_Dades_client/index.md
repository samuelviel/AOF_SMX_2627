# S7 · Les dades del client

**Trimestre:** 3r · **RA4 complet** — bases de dades ofimàtiques

## Calendari

| # | Data | Dia | Hores | Contingut |
| - | ---- | --- | ----- | --------- |
| 1 | 15/03/2027 | Dilluns | 2h | Obertura · [T1](teoria/1_model.md) Per què un full no basta |
| 2 | 16/03/2027 | Dimarts | 1h | [T1](teoria/1_model.md) Entitats, atributs i relacions |
| 3 | 17/03/2027 | Dimecres | 2h | [T1](teoria/1_model.md) Claus i normalització bàsica |
| 4 | 18/03/2027 | Dijous | 2h | [A1](activitats/A1_model.md) Del caos al model |
| 5 | 22/03/2027 | Dilluns | 2h | [A1](activitats/A1_model.md) (cont.) · lliurament |
| 6 | 23/03/2027 | Dimarts | 1h | [T2](teoria/2_taules.md) Taules, tipus de camp i integritat |
| 7 | 24/03/2027 | Dimecres | 2h | [T2](teoria/2_taules.md) Relacions a Base · importació |
| 8 | 06/04/2027 | Dimarts | 1h | [A2](activitats/A2_construccio.md) part 1: taules i relacions |
| 9 | 07/04/2027 | Dimecres | 2h | [A2](activitats/A2_construccio.md) part 2: importació i càrrega |
| 10 | 08/04/2027 | Dijous | 2h | [T3](teoria/3_consultes.md) Consultes: selecció, criteris, ordenació |
| 11 | 12/04/2027 | Dilluns | 2h | [T3](teoria/3_consultes.md) Consultes amb diverses taules i agregació |
| 12 | 13/04/2027 | Dimarts | 1h | [A3](activitats/A3_consultes.md) part 1 |
| 13 | 14/04/2027 | Dimecres | 2h | [A3](activitats/A3_consultes.md) part 2 · lliurament |
| 14 | 15/04/2027 | Dijous | 2h | [T4](teoria/4_formularis.md) Formularis |
| 15 | 19/04/2027 | Dilluns | 2h | [T4](teoria/4_formularis.md) Informes i macros |
| 16 | 20/04/2027 | Dimarts | 1h | [A4](activitats/A4_entrega.md) part 1: formularis |
| 17 | 21/04/2027 | Dimecres | 2h | [A4](activitats/A4_entrega.md) part 2: informes i lliurament · tancament |

**17 sessions · 29 hores.**

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Gestoria Bellver · Per a: la vostra empresa</p>

Bon dia,

Tenim la informació dels nostres clients repartida en quatre fulls de càlcul que ha anat fent gent diferent durant anys. Hi ha clients repetits amb el nom escrit de tres maneres, no sabem quins expedients estan oberts i cada vegada que volem una llista ens costa un matí.

Ens han dit que això es pot arreglar. Nosaltres no som informàtics: **necessitem una cosa que puga usar la Rosa, que porta 20 anys ací i mai ha vist una base de dades**.
</div>

## Què lliures

| Lliurament | Activitat | Format |
| --- | --- | --- |
| **Model de dades** i informe de problemes detectats | [A1](activitats/A1_model.md) | PDF |
| **Base de dades** amb taules, relacions i dades carregades | [A2](activitats/A2_construccio.md) | `.odb` |
| **Joc de consultes** que responen preguntes de negoci | [A3](activitats/A3_consultes.md) | `.odb` + PDF |
| **Formularis i informes** per a l'usuari final | [A4](activitats/A4_entrega.md) | `.odb` + manual breu |

## Què treballem

**RA4** · *Elabora documents amb bases de dades ofimàtiques descrivint i aplicant operacions de manipulació de dades.*

| CA | Enunciat oficial | Es veu a | S'avalua a |
| --- | --- | --- | --- |
| **a** | Identificar els elements de les bases de dades relacionals | T1 | A1 |
| **b** | Crear bases de dades ofimàtiques | T2 | A2 |
| **c** | Utilitzar les taules (inserir, modificar i eliminar registres) | T2 | A2 |
| **d** | Utilitzar assistents en la creació de consultes | T3 | A3 |
| **e** | Utilitzar assistents en la creació de formularis | T4 | A4 |
| **f** | Utilitzar assistents en la creació d'informes | T4 | A4 |
| **g** | Realitzar cerca i filtratge sobre la informació emmagatzemada | T3 | A3 |
| **h** | Crear i utilitzar macros | T4 | A4 |

## Continguts

1. [Del full a la base de dades](teoria/1_model.md)
2. [Taules i relacions](teoria/2_taules.md)
3. [Consultes](teoria/3_consultes.md)
4. [Formularis, informes i macros](teoria/4_formularis.md)

**Activitats**

- [A1 · Del caos al model](activitats/A1_model.md)
- [A2 · Construïm la base de dades](activitats/A2_construccio.md)
- [A3 · Preguntes que has de respondre](activitats/A3_consultes.md)
- [A4 · L'entrega al client](activitats/A4_entrega.md)

## Eina

**LibreOffice Base** amb el motor HSQLDB o Firebird incrustat. Els conceptes (taules, claus, relacions, consultes) són **exactament els mateixos** en Access, MySQL o PostgreSQL: el que aprengues ací et val a tot arreu.

!!! warning "Dades de clients"
    Els clients de la gestoria són ficticis i te'ls dono jo. **No introduïsques dades reals de ningú** en cap moment d'esta situació.

    A [A4](activitats/A4_entrega.md) tractarem què implica el RGPD en una base de dades de clients, perquè és exactament el tipus d'encàrrec on una empresa es juga una sanció.

## Què t'emportes

Si has entés per què l'inventari de [S4](../S4_Control_economic/index.md) guardava **moviments** en lloc d'una columna d'estoc, ja tens mig camí fet: la idea és la mateixa, portada fins al final.

**Una dada s'escriu una vegada, en un sol lloc.** Tot el que ve després — relacions, consultes, informes — és conseqüència d'això.
