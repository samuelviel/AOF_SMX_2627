# T3 · Text, imatges i objectes

<span class="ca">CA b</span> <span class="ca">CA e</span> <span class="ca">CA f</span>

Un manual tècnic sense imatges no és un manual: és una descripció. Però una imatge mal col·locada desmunta un document sencer.

## Ancoratge i ajust: per què les imatges "es mouen soles"

No es mouen soles. Es mouen perquè estan **ancorades** a alguna cosa que s'ha mogut.

| Ancoratge | La imatge està lligada a... | Quan usar-lo |
| --- | --- | --- |
| **Al paràgraf** | Un paràgraf concret | Per defecte en la majoria de casos |
| **Com a caràcter** | Una posició dins del text, com una lletra més | Icones xicotetes enmig d'una frase |
| **Al caràcter** | Un caràcter concret | Poc habitual |
| **A la pàgina** | La pàgina física, passe el que passe | Marques d'aigua, elements fixos |

L'**ajust** (*wrap*) decideix com es comporta el text al voltant: sense ajust, la imatge ocupa tota l'amplada; amb ajust òptim, el text l'envolta.

!!! danger "El problema clàssic del manual"
    Una captura ancorada a la pàgina en un document que després creix. Afegeixes dos paràgrafs al capítol 2 i la imatge del capítol 5 es queda on estava, il·lustrant un text que ja no hi és.

    En documentació tècnica, la imatge ha d'anar **ancorada al paràgraf** que la comenta, perquè viatge amb ell.

## Peus, títols i referències

Una imatge en un document professional porta **peu numerat**. I no es numera a mà.

Quan inserixes un títol o llegenda (*Inserir → Llegenda* a LibreOffice, *Referències → Inserir títol* a Word), el programa crea una numeració automàtica. Això et dona tres coses:

1. Si intercales una imatge nova, la resta es renumera sola.
2. Pots escriure al text *"com es veu a la Figura 7"* amb una **referència creuada** que també s'actualitza.
3. Pots generar un **índex de figures** automàtic.

La mateixa lògica val per a taules.

## Taules: estructura, no decoració

Una taula serveix per a **dades comparables**. No per a maquetar ni per a alinear coses.

- Fila de capçalera marcada com a tal, perquè es repetisca si la taula passa de pàgina.
- Evita cel·les combinades si no són imprescindibles: compliquen l'exportació i la lectura assistida.
- Amplades coherents en tot el document.
- Res de taules invisibles per a col·locar dos blocs de text: això és maquetació, i es fa amb columnes o marcs.

## Captura i digitalització

<span class="ca">CA e</span>

Per a un manual necessitaràs introduir imatges que no existeixen encara. Tres vies:

**Captura de pantalla.** Captura **només** el que cal explicar: una finestra concreta, no l'escriptori sencer amb la barra de tasques i el teu nom d'usuari. Si has de destacar un botó, afig un requadre o una fletxa; no descrigues *"el botó de dalt a la dreta"*.

**Digitalització amb escàner o mòbil.** Un document en paper es converteix en imatge, i eixa imatge no conté text: conté píxels amb forma de lletra. Per a obtindre text real cal **OCR** (reconeixement òptic de caràcters). Després de l'OCR, **sempre** cal revisar: confon zeros i "o", "l" i "1", i es menja accents.

**Imatges de tercers.** Ací la pregunta no és si te la pots baixar, sinó **amb quina llicència**. Recorda de la [T2 de S1](../../S1_Posada_marxa/teoria/2_llicencies.md): una imatge amb clàusula `NC` no es pot fer servir en material d'una empresa, encara que l'empresa siga ficticia i el material, un exercici de classe. Ací fem les coses com es fan fora.

!!! tip "Resolució: ni curt ni passat"
    Per a un document que es veurà en pantalla i es podrà imprimir, unes captures al voltant de 150 px/polzada són suficients. Inserir fotos de 6000 px d'amplada en un document de text només fa que el fitxer pese 80 MB i que el client no el puga enviar per correu.

    Comprimeix les imatges abans de lliurar (*Format → Imatge → Comprimeix* a LibreOffice; *Format d'imatge → Comprimeix* a Word).

## Importar i exportar

<span class="ca">CA f</span>

Ja ho vas tocar a [A3 de S1](../../S1_Posada_marxa/activitats/A3_compatibilitat.md). Ara amb documents de veritat:

| Direcció | Cas típic | Vigila |
| --- | --- | --- |
| **Importar** text pla o `.csv` | Dades d'un altre sistema | Codificació (UTF-8), salts de línia |
| **Importar** un `.docx` a LibreOffice | Document d'un client | Estils renombrats, fonts que no tens |
| **Exportar a PDF** | Entrega final | Marcadors, hiperenllaços, PDF/A si ha d'arxivar-se |
| **Exportar a `.docx`** | El client ho editarà a Word | Que els teus estils propis sobrevisquen |
| **Exportar a HTML** | Publicació web | Es perd quasi tota la maquetació |

!!! warning "El PDF no és un format d'edició"
    Exportar a PDF és un camí d'anada. Es pot "recuperar" el contingut, però el resultat sempre és pitjor que l'original. Conserva sempre el fitxer editable: és l'actiu de l'empresa, el PDF només és l'entrega.
