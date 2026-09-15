# T2 · Estils i plantilles: l'aspecte, automatitzat

<span class="ca">CA a</span> <span class="ca">CA d</span>

Tot el que fa que un document siga mantenible cap en una frase: **el format no es posa, es defineix**.

## Què és un estil

Un **estil** és un conjunt de propietats de format guardat amb un nom. Apliques el nom; el format ve sol.

La diferència pràctica:

- **A mà:** tens 40 títols. Canvia el color corporatiu. Tens 40 canvis per fer, i te'n deixaràs dos.
- **Amb estils:** tens 40 títols amb l'estil *Títol 1*. Canvia el color corporatiu. Tens **un** canvi per fer.

I encara més important: el document sap on estan els títols, i per tant pot generar un índex, un panell de navegació i uns marcadors de PDF. Un títol "fals" —text gran en negreta— és invisible per a tot això.

## Els quatre tipus d'estil

| Tipus | Afecta | Exemple d'ús |
| --- | --- | --- |
| **Paràgraf** | Un bloc sencer | *Títol 1*, *Cos de text*, *Cita*, *Peu de figura* |
| **Caràcter** | Un tros de text dins d'un paràgraf | *Terme tècnic*, *Ruta de menú*, *Èmfasi* |
| **Pàgina** | El full: marges, orientació, capçalera, peu | *Portada*, *Estàndard*, *Apaïsada* |
| **Llista** | Símbols, numeració i sagnats | *Llista de passos*, *Llista de punts empresa* |

A LibreOffice el panell d'estils s'obri amb ++f11++ i té una icona per a cada tipus a la part superior. A Word i a Microsoft 365 Online la galeria d'estils és a la cinta d'*Inici*, i els estils de pàgina es gestionen des de *Disposició* i els salts de secció.

!!! danger "L'estil de pàgina és el que més es passa per alt"
    És el que et permet que la portada no tinga número, que el cos sí en tinga, i que enmig del document hi haja una pàgina apaïsada per a una taula ampla. Sense estils de pàgina —o seccions, a Word— això no es pot fer bé.

## Herència: el truc que t'estalvia més temps

Els estils s'hereten. *Títol 1*, *Títol 2* i *Títol 3* deriven normalment d'un estil pare.

Si defineixes la tipografia al **pare** en lloc de repetir-la a cada fill, canviar la lletra de tot el document és un únic canvi.

Per això, quan construïsques la plantilla, l'ordre és:

1. Defineix primer l'estil base (tipografia, mida, interlineat, idioma).
2. Deriva'n els títols, canviant **només** el que ha de canviar.
3. Deriva'n els estils especials (cites, peus de figura, notes).

!!! tip "La regla dels tres cops"
    Si has hagut d'aplicar el mateix format manualment tres vegades al mateix document, ja havies d'haver creat un estil a la primera.

## De l'estil a la plantilla

Una **plantilla** és un document base —estils, capçalera, peu, portada, camps— que es desa amb un format especial (`.ott` a LibreOffice, `.dotx` a Word) i que serveix per a **crear documents nous que ja naixen formatats**.

La diferència amb "obrir l'últim informe i esborrar-ne el contingut", que és el que fa quasi tothom:

- La plantilla no s'edita per accident: en obrir-la, es crea un document nou.
- No arrossega restes del document anterior (dades del client antic, comentaris oblidats, propietats del fitxer).
- Es pot distribuir a tot l'equip i garantir que tots parteixen d'igual.

**Desar-la:** *Fitxer → Plantilles → Desa com a plantilla* a LibreOffice; *Fitxer → Desa com a → Plantilla de Word* a Word.

## Camps: informació que s'escriu sola

Un **camp** és un buit que el programa ompli: número de pàgina, total de pàgines, data, títol del document, autor.

Els camps es nodreixen de les **propietats del document** (*Fitxer → Propietats*). Si poses el títol allí, el pots inserir a la capçalera com a camp i canviarà sol en cada document creat des de la plantilla.

Açò és el que fa que una capçalera del tipus `Manual d'usuari · Pàgina 4 de 23` funcione sense que ningú l'actualitze mai.

## 🤖 IA i identitat visual

Una IA et proposarà paletes de colors i combinacions tipogràfiques en segons, i és un punt de partida raonable quan no saps per on començar.

El que no pot fer és **decidir per vosaltres**. La identitat de l'empresa és una decisió de l'empresa, i haureu de defensar-la. A més, verifica sempre dues coses que les IA solen resoldre malament: que el contrast entre el text i el fons siga suficient per a llegir-se, i que les tipografies proposades tinguen llicència d'ús comercial gratuït.
