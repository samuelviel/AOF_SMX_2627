# A4 · Ho volen en un altre format

**Sessió 16** · lliurament: informe d'interoperabilitat de 1-2 pàgines
**Avalua:** RA2 <span class="ca">d</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Ajuntament · Per a: la vostra empresa · Assumpte: RE: manual d'usuari</p>

Hem rebut el manual i està molt bé, gràcies.

Dues coses:

1. El nostre departament de comunicació ha de poder **editar-lo**, i ells treballen amb Word. Ens el poden enviar en `.docx`?
2. Per a l'arxiu municipal necessitem una versió en **PDF/A**, que és el que exigeix la nostra normativa de conservació.

I aprofite per a preguntar: ens han passat un document `.docx` d'un altre proveïdor i quan l'obrim se'ns veu rar. És normal?
</div>

## La faena

Tres peticions reals, i cadascuna té una resposta tècnica diferent. El teu informe les ha de resoldre les tres.

### 1. Anada i tornada a `.docx`

Agafa el teu manual de [A2](A2_manual.md) i fes el cicle complet:

```
manual.odt → manual.docx → obri'l en l'altra suite → torna a desar-lo → obri'l de nou en l'original
```

Documenta amb **captures comparades** què ha passat amb cada element, especialment amb els que [T3](../teoria/3_objectes.md) marca com a risc:

| Element | Estat després de l'anada | Estat després de la tornada | Gravetat |
| --- | --- | --- | --- |
| Estils de paràgraf | | | |
| Estils de pàgina / seccions | | | |
| Numeració de capítols | | | |
| Llistes multinivell | | | |
| Ancoratges d'imatge | | | |
| Llegendes i referències creuades | | | |
| Índex de contingut | | | |
| Índex de figures | | | |
| Capçalera i peu (camps) | | | |
| Fonts | | | |

**Gravetat:** 🟢 cosmètic · 🟡 arreglable · 🔴 inservible o enganya el lector.

### 2. La versió PDF/A

Exporta a **PDF/A** i explica, amb les teues paraules:

- Què fa diferent el PDF/A d'un PDF normal
- Quines opcions has hagut d'activar o desactivar i per què
- **Què t'ha avisat el programa** en exportar (hi ha elements que PDF/A no permet; el diàleg t'ho dirà)
- Per què una administració exigeix precisament este format

Comprova que el resultat manté els **marcadors** i el **text alternatiu**.

### 3. El document que "es veu rar"

Et donaré un `.docx` preparat que es veu malament en obrir-lo. Diagnostica'l amb el mètode de [S1/T4](../../S1_Posada_marxa/teoria/4_documentar.md) i digues:

- Què concretament es veu diferent
- Per què passa
- Què li respondries **al client** (no a un tècnic)

## L'informe

Una o dues pàgines, amb la teua plantilla, dirigit a l'Ajuntament. Recorda a qui escrius: la persona que rebrà açò gestiona contractes, no configura ordinadors.

Estructura:

1. **Resposta a la petició 1:** els enviem el `.docx`, amb un avís concret del que no s'ha de tocar i per què
2. **Resposta a la petició 2:** PDF/A adjunt i què garanteix
3. **Resposta a la pregunta 3:** per què es veu rar i què poden fer
4. **Recomanació de l'empresa:** quin flux de treball proposem per a futurs documents amb este client
5. **Annex tècnic:** la taula de proves (això sí pot ser tècnic)

!!! tip "El punt 4 és el que et distingeix"
    Qualsevol pot convertir un fitxer. El que espera un client d'un proveïdor és que li diga **com evitar el problema la pròxima vegada**.

    Per exemple: acordar que els documents que han d'editar els dos costats es facen des del principi amb un joc d'estils limitat i sense elements que no sobreviuen a la conversió.

## Com s'avalua

### RA2.d) Documents importats i exportats — 100 %

- 🟢 Cicle complet d'anada i tornada provat de veritat, amb la taula completa, evidència visual i gravetat classificada. PDF/A generat amb les opcions correctes i explicat **amb sentit** (no copiat). Diagnòstic del document problemàtic encertat i explicat en dos registres: tècnic a l'annex, comprensible al cos. La recomanació de flux de treball és concreta i realista.
- 🔵 Proves fetes i informe correcte, però amb algun buit: taula incompleta, PDF/A generat sense entendre'n del tot les implicacions, o recomanació genèrica.
- 🟡 Conversió feta sense provar la tornada, o taula emplenada amb suposicions en lloc de comprovacions; o l'informe està escrit en registre tècnic per a un destinatari que no ho és.
- 🔴 No hi ha proves pròpies: es descriu el que "sol passar" sense haver-ho verificat.

!!! note "Sobre el registre"
    Esta activitat avalua un CA tècnic, però el lliurament és una **carta a un client**. Un informe tècnicament impecable escrit com si el llegira un informàtic no compleix l'encàrrec i no arriba a nivell client.

    És deliberat: al món real, la part difícil d'este problema no és convertir el fitxer.
