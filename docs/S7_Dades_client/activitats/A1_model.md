# A1 · Del caos al model

**Sessions 4 i 5** · lliurament: informe de model en PDF
**Avalua:** RA4 <span class="ca">a</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Gestoria Bellver · Adjunt: dades_gestoria.ods

</p>

Ací tenen els nostres fulls. Són quatre pestanyes que ha anat fent gent diferent.

Ens han dit que abans de fer res cal "veure com estan les dades". Fàcen-ho i diguen-nos què troben, però en cristià, que nosaltres d'això no en sabem.
</div>

## El material

Un llibre amb quatre fulls reals de gestoria: clients, expedients, serveis facturats i contactes. Amb tots els problemes de la vida real: duplicats amb noms diferents, camps amb diverses dades dins, dates en tres formats, imports com a text, files òrfenes.

## Part 1 · Auditoria de les dades

Abans de proposar cap model, **documenta què està malament**. Per a cada problema:

| Problema | On | Quants registres | Conseqüència si no s'arregla | Com es detecta |
| --- | --- | --- | --- | --- |

Mínim **sis problemes** diferents. Com a mínim un de cada tipus:

- Redundància
- Dada composta (diverses coses en una cel·la)
- Inconsistència de format
- Duplicat amb escriptura diferent
- Registre orfe o incoherent
- Tipus de dada incorrecte

!!! tip "La columna 'com es detecta' és la que val"
    No n'hi ha prou amb dir "hi ha duplicats". Digues **com ho has trobat**: una taula dinàmica comptant per NIF, una columna amb `COMPTA.SI`, una ordenació.

    És el que permet que un company repetisca l'auditoria d'ací a un any, i és el que demostra que l'has feta tu.

## Part 2 · El model

<span class="ca">CA a</span>

### Diagrama entitat-relació

Amb totes les entitats, els seus camps, claus primàries i alienes, i les cardinalitats marcades. Ha d'incloure **almenys una relació N a N** resolta amb taula intermèdia.

Fes-lo primer a mà i després passa'l net (val qualsevol eina de diagrames, o Inkscape de [S5](../../S5_Imatge_empresa/index.md)).

### Diccionari de dades

Per a cada taula:

| Camp | Tipus | Longitud | Nul? | Clau | Descripció |
| --- | --- | --- | --- | --- | --- |

Cada tipus ha d'estar justificat quan no siga obvi. En particular: per què els imports són `DECIMAL`, per què els telèfons i codis són text, per què les dates són `DATE`.

### Decisions d'integritat

Per a cada relació, què passa en esborrar el registre pare i **per què has triat eixa opció**. Recorda [T2](../teoria/2_taules.md): "restringir" per defecte, i cascada només amb molt bon motiu.

## Part 3 · L'informe al client

Estructura, amb la plantilla corporativa:

1. **Resum executiu** — 5 línies. Què hem trobat i què proposem. En llenguatge de gestoria, no d'informàtic
2. **Problemes detectats** — la taula, amb la conseqüència **en termes de negoci** ("no podreu enviar una circular a tots els clients d'Alzira perquè el nom de la població està escrit de quatre maneres")
3. **El model proposat** — el diagrama, explicat
4. **Diccionari de dades** — pot anar en annex
5. **Decisions que necessiten la vostra confirmació** — la llista de dubtes que **només el client pot resoldre**
6. **Què guanyareu** — concret

!!! warning "El punt 5 és obligatori i és el més professional"
    Hi haurà decisions que tu **no pots prendre**: si dos clients amb noms semblants són el mateix, si un expedient sense client s'ha d'esborrar o recuperar, si un import negatiu és un abonament o un error.

    Un tècnic que decideix això pel seu compte està modificant les dades del client segons la seua suposició. **Es pregunta.**

## Com s'avalua

### RA4.a) Elements de les bases de dades relacionals — 100 %

- 🟢 Auditoria amb sis problemes o més, un de cada tipus, amb recompte real i **mètode de detecció** documentat. Diagrama E-R complet amb claus i cardinalitats, incloent-hi una N a N ben resolta. Diccionari de dades complet amb tipus justificats. Decisions d'integritat raonades. L'informe parla en llenguatge del client i inclou la llista de decisions a confirmar.
- 🔵 Model correcte i auditoria completa, però algun tipus sense justificar, o l'informe manté registre tècnic en algun tram, o la llista de decisions a confirmar és curta.
- 🟡 El model funciona però té redundància sense resoldre, o falta la relació N a N, o l'auditoria és una llista genèrica sense recomptes ni mètode.
- 🔴 No hi ha model relacional: es proposa reproduir els fulls tal qual, o el diagrama no té claus ni cardinalitats.

!!! quote "Punt de comprensió"
    *"Al vostre model, què passa si un expedient canvia de client a mitjan any? I si un client es fusiona amb un altre?"*

    Cap de les dues coses està a l'enunciat. Les dues passen a les gestories.
