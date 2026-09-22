# A1 · Els equips han arribat

<span class="ca">CA a</span> <span class="ca">CA b</span> <span class="ca">CA c</span> <span class="ca">CA d</span> <span class="ca">CA f</span> <span class="ca">CA g</span>

**Modalitat:** individual · **Sessions:** 2, 4, 5, 6, 8 · **Lliurament:** informe en PDF

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

**Assumpte: deixeu els equips llestos**

Els ordinadors han arribat buits. Necessite que cadascú prepare el seu lloc de treball i em passe un informe.

No vull una llista de programes. Vull poder donar-li eixe informe a algú que entre nou d'ací a tres mesos i que es puga muntar l'equip sol, sense preguntar-me res.
</div>

## Part 1 · Decidir què s'instal·la

Abans de tocar res, planifica. Un tècnic que instal·la sobre la marxa acaba amb un equip ple de coses que ningú sap per què hi són.

Ompli la **taula de decisió** amb el programari que necessita l'empresa per a este curs. Mínim una fila per a cada necessitat:

| Necessitat | Programa triat | Llicència | Per què este i no un altre |
| --- | --- | --- | --- |
| Processar textos | | | |
| Fulls de càlcul | | | |
| Presentacions | | | |
| Base de dades | | | |
| Edició d'imatge | | | |
| Captura de pantalla | | | |
| Compressió de fitxers | | | |
| Lectura de PDF | | | |

La columna de justificació és la important. *"Perquè sí"* o *"perquè ja el coneixia"* no són justificacions: parla de cost, de llicència, de compatibilitat amb el que usen els clients o de requisits de l'equip.

!!! warning "Requisits abans d'instal·lar"
    Comprova que l'equip compleix els requisits mínims de cada programa **abans** de descarregar res. Apunta a l'informe la comparació: requisit demanat contra el que tens realment (RAM, espai lliure, versió del sistema).

## Part 2 · Comprovar, completar i configurar

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

**Assumpte: canvi de plans**

Bones notícies: el proveïdor ens ha deixat els equips amb el programari habitual de l'empresa ja instal·lat. No cal començar de zero.

Però no em fie. Vull que cadascú **comprove que el que hi ha coincideix amb el que vau decidir**, que mire si el seu PC compleix els requisits de cada programa, que **instal·le el que falte** i que ho deixe tot amb la **configuració de l'empresa**.
</div>

### 2.1 · El programari de l'empresa

Este és el programari que usarem a l'aula durant el curs:

| Necessitat | Programari de l'empresa | Web oficial |
| --- | --- | --- |
| Processar textos | LibreOffice Writer | `libreoffice.org` |
| Fulls de càlcul | LibreOffice Calc | `libreoffice.org` |
| Presentacions | LibreOffice Impress | `libreoffice.org` |
| Base de dades | LibreOffice Base | `libreoffice.org` |
| Edició d'imatge | GIMP | `gimp.org` |
| Disseny vectorial | Inkscape | `inkscape.org` |
| Edició d'àudio | Audacity | `audacityteam.org` |
| Reproducció multimèdia | VLC | `videolan.org` |
| Gravació de pantalla | OBS Studio | `obsproject.com` |
| Edició de vídeo | Kdenlive | `kdenlive.org` |
| Compressió de fitxers | 7-Zip (Windows) · gestor d'arxius del sistema (Linux) | `7-zip.org` |
| Lectura de PDF | Visor del sistema o el navegador | — |
| Ofimàtica en línia | Microsoft 365, des del navegador | — |

### 2.2 · Compara-ho amb la teua llista i amb el teu PC

Omple esta taula per a **cada programa** de la llista de l'empresa:

| Programa de l'empresa | És a la meua taula de la part 1? | Està instal·lat al meu PC? | Versió instal·lada |
| --- | --- | --- | --- |

**Com saber si està instal·lat i quina versió és:**

=== "Linux"
    - Busca'l al menú d'aplicacions. Si apareix, obri'l i mira la versió al menú **Ajuda**, a l'opció **Quant a**. A LibreOffice és `Ajuda → Quant al LibreOffice`.
    - O des del terminal, per exemple per a GIMP:
        ```bash
        apt policy gimp
        ```
        La línia *Instal·lat* (o *Installed*) et diu la versió. Si posa `(cap)` o `(none)`, no està instal·lat.

=== "Windows"
    - `Configuració → Aplicacions → Aplicacions instal·lades` i busca el nom del programa. Al costat apareix la versió.
    - O obri el programa i mira el menú **Ajuda → Quant a**.

!!! tip "Si la teua taula de la part 1 no coincideix"
    És normal: vas triar tu, i l'empresa ja havia triat. No ho esborres. Afig una columna o una nota explicant **en què et diferencies i per què**. Pot ser que la teua tria fora bona i siga una proposta per a l'empresa; pot ser que la de l'empresa tinga un motiu que no havies vist.

Fes una captura de la versió de cada programa: són la teua evidència.

**I Microsoft 365?** No s'instal·la a l'equip: funciona des del navegador. El que has de comprovar és una altra cosa:

1. Obri el navegador i entra a Microsoft 365 amb **el compte del centre**.
2. Fes clic al **llançador d'aplicacions** (la graella de punts de dalt a l'esquerra).
3. Apunta **quines aplicacions hi apareixen** (Word, Excel, PowerPoint, Outlook, OneDrive...). Eixa és la llicència que tens.
4. Entra a OneDrive i apunta **quant d'espai tens**.

Captura-ho: substitueix la columna de versió, perquè en una aplicació web la versió la decideix Microsoft, no tu.

### 2.3 · Els requisits, des de la web oficial

Per a **cada programa** de la llista, busca els requisits del sistema a la seua **web oficial** (la de la taula de 2.1) i compara'ls amb el teu PC (les dades les tens de la part 1).

| Programa | On ho has trobat (URL i data) | Sistemes operatius | RAM | Espai en disc | Altres requisits | El meu PC ho compleix? |
| --- | --- | --- | --- | --- | --- | --- |

**Com trobar-los:**

1. Entra a la web oficial del programa.
2. Busca un apartat amb un nom com *Descàrregues*, *Download*, *System requirements*, *Requirements* o *FAQ*.
3. Si no el trobes navegant, busca al cercador `system requirements` + nom del programa, però **obri només resultats de la web oficial**.

**Per a Microsoft 365**, els requisits no són de RAM ni de disc: són **quins navegadors admet** i que tingues connexió. Busca'ls a la web oficial de Microsoft i apunta els navegadors compatibles i el que uses tu. Si no trobes una pàgina de requisits per a la versió web, apunta també això: és informació útil.

!!! note "No tots publiquen el mateix"
    Algunes webs donen requisits detallats (RAM, disc, processador) i altres només diuen per a quins sistemes operatius hi ha versió. Si una dada no està publicada, escriu **"no publicat"** i apunta el que sí que diu la web. No t'inventes cap xifra ni la tragues d'una web que no siga l'oficial.

### 2.4 · Instal·lar el que falte

**Només si algun programa de la llista no està instal·lat.** Haurien de ser pocs.

=== "Linux (Ubuntu / LliureX)"
    **Opció A · Des del centre de programari**

    1. Obri el centre de programari del sistema (la botiga d'aplicacions).
    2. Busca el programa pel nom.
    3. Fes clic a **Instal·la** i escriu la contrasenya si te la demana.

    **Opció B · Des del terminal**

    ```bash
    sudo apt update
    sudo apt install NOM_DEL_PAQUET
    ```

    | Programa | Paquet |
    | --- | --- |
    | LibreOffice sencer | `libreoffice` |
    | Només LibreOffice Base (sol ser el que falta) | `libreoffice-base` |
    | Idioma valencià per a LibreOffice | `libreoffice-l10n-ca` |
    | GIMP | `gimp` |
    | Inkscape | `inkscape` |
    | Audacity | `audacity` |
    | VLC | `vlc` |
    | OBS Studio | `obs-studio` |
    | Kdenlive | `kdenlive` |
    | 7-Zip | `7zip` |

    Exemple, per a instal·lar GIMP:

    ```bash
    sudo apt update
    sudo apt install gimp
    ```

    Quan pregunte si vols continuar, respon `S` (o `Y`) i prem Intro.

=== "Windows"
    1. Entra a la **web oficial** del programa (taula de 2.1). Mai d'una web de descàrregues genèrica.
    2. Ves a l'apartat de **descàrregues** i tria la versió per a Windows de 64 bits.
    3. Executa el fitxer descarregat.
    4. Llig cada pantalla abans de fer clic a **Següent**: si et proposa instal·lar programes extra o canviar el navegador, **desmarca-ho**.
    5. En acabar, obri el programa per a comprovar que funciona.

!!! note "Microsoft 365 no entra ací"
    No hi ha res a instal·lar: només cal un navegador compatible i el compte del centre. Escriu-ho a l'informe, perquè és una diferència important entre **programari instal·lat** i **programari com a servei**: en el segon, no controles ni la versió ni quan canvia.

!!! warning "Si et demana una contrasenya d'administrador que no tens"
    No insistisques ni ho intentes d'una altra manera: avisa el professor i apunta-ho al registre d'incidències. En una empresa, instal·lar sense autorització és un problema seriós.

**La fitxa de cada instal·lació** · Per a cada programa que hages instal·lat, documenta:

- nom i versió exacta del programa,
- origen (web oficial amb l'URL completa, o paquet de la distribució),
- mètode d'instal·lació (centre de programari, terminal, instal·lador),
- durada aproximada,
- incidències, si n'hi ha hagut.

Si no has hagut d'instal·lar res, escriu-ho a l'informe: *"Tot el programari de l'empresa ja estava instal·lat"*, amb l'evidència de 2.2.

### 2.5 · La configuració de l'empresa a LibreOffice

Esta és la configuració que ha de quedar a LibreOffice. És la mateixa per a tothom: és el que fa que tots els equips es comporten igual.

| Paràmetre | Valor que ha de quedar |
| --- | --- |
| Idioma de la interfície | Valencià |
| Diccionaris de correcció | Valencià, castellà i anglés |
| Desat automàtic | Cada 5 minuts |
| Carpeta de treball per defecte | La del portafoli |
| Dades d'usuari | Nom real, perquè els comentaris i els canvis s'identifiquen |
| Format de desat per defecte | El que decidiu a [A3](A3_compatibilitat.md). Fins llavors, el format ODF (`.odt`) |

Segueix els passos en ordre. **Fes una captura a cada pas on es veja el valor que has posat.**

#### Pas 1 · Obri les opcions

1. Obri **LibreOffice Writer**.
2. Menú `Eines → Opcions...`
3. S'obri una finestra amb un **arbre de seccions a l'esquerra**. Tots els passos següents es fan des d'ací, sense tancar-la.

#### Pas 2 · Dades d'usuari

1. A l'arbre, obri **LibreOffice** i fes clic a **Dades d'usuari**.
2. A la fila **Nom/Cognoms/Inicials:**, escriu el teu nom, els teus cognoms i les teues inicials.

#### Pas 3 · Idioma de la interfície

1. A l'arbre, obri la secció de **llengües** (la que conté *Ajudes a l'escriptura*) i fes clic al seu primer apartat.
2. A la pàgina que apareix, busca **Interfície d'usuari:** i tria **Català (valencià)**.

Si no apareix a la llista, falta el paquet d'idioma: a Linux, instal·la `libreoffice-l10n-ca` (vegeu 2.4).

#### Pas 4 · Llengua dels documents

1. A la mateixa pàgina, a l'apartat **Llengües predeterminades per als documents**, busca **Occidental:**.
2. Tria **Català (valencià)**.

Així, tot el que escrigues es corregirà en valencià per defecte.

#### Pas 5 · Desat automàtic

1. A l'arbre, obri **Carrega o guarda** i fes clic a **General**.
2. Marca la casella **Guarda la informació de restabliment automàtic cada:**
3. Posa **5** minuts.

#### Pas 6 · Format de desat per defecte

1. A la mateixa pàgina, baixa fins a l'apartat **Format de fitxer per defecte i paràmetres ODF**.
2. A **Tipus de document:** tria **Document de text**.
3. A **Sempre guarda com a:** tria el format ODF (`.odt`). Quan acabes l'[A3](A3_compatibilitat.md), tornaràs ací a posar el format que haja decidit l'empresa.

#### Pas 7 · Carpeta de treball

1. A l'arbre, obri **LibreOffice** i fes clic a **Camins**.
2. A la llista, selecciona la fila **Els meus documents**.
3. Fes clic a **Edita...** i tria la carpeta del teu [portafoli](../../recursos/portafoli.md).

#### Pas 8 · Guarda i reinicia

1. Fes clic a **D'acord**.
2. Tanca LibreOffice del tot i torna a obrir-lo: el canvi d'idioma de la interfície només s'aplica en reiniciar.

#### Pas 9 · Els diccionaris

Ara comprova que funcionen els tres diccionaris.

1. Obri un document nou a Writer i escriu tres paraules mal escrites a propòsit, cadascuna en una línia: `ordinadorr`, `ordenadorr`, `computerr`.
2. Selecciona la segona línia. A la **barra d'estat** (baix de tot de la finestra) fes clic sobre el nom de la llengua i tria **Castellà** (o *Espanyol*).
3. Fes el mateix amb la tercera línia i tria **Anglés**.

    Si la llengua que busques no apareix en eixe menú, usa `Eines → Llengua` i tria l'opció que l'aplica **a la selecció**.

4. Si les tres paraules apareixen **subratllades en roig**, els tres diccionaris funcionen. Fes-ne captura.

Si alguna no apareix subratllada, falta eixe diccionari:

- **Linux:** instal·la'l amb el terminal, com a 2.4:
    ```bash
    sudo apt install hunspell-ca hunspell-es hunspell-en-us
    ```
    (`hunspell-ca` inclou el diccionari valencià.) Reinicia LibreOffice i torna a provar.
- **Windows:** normalment vénen amb LibreOffice. Si en falta un, a la part 3 aprendràs a afegir-lo com a extensió.

#### Pas 10 · Comprovació final

Crea un document nou i fes `Fitxer → Anomena i guarda...`:

- La finestra s'ha d'obrir **a la carpeta del portafoli**.
- El tipus de fitxer proposat ha de ser **`.odt`**.

Si és així, la configuració està feta. Captura-ho.

### 2.6 · La configuració de l'empresa a Microsoft 365

A LibreOffice configures **l'equip**. A Microsoft 365 configures **el compte**: ho fas una vegada i et segueix a qualsevol ordinador on inicies sessió.

| Paràmetre | Valor que ha de quedar |
| --- | --- |
| Idioma | Valencià |
| Zona horària | La d'Espanya peninsular (UTC+01:00, Madrid) |
| Carpeta de treball | La del portafoli, dins de OneDrive |
| Idioma de correcció a Word | Valencià |

!!! warning "Ací els noms canvien"
    Microsoft canvia la interfície web sovint, i els noms depenen de l'idioma del compte. Si un botó no està on diu el pas, **usa el quadre de cerca de dalt de tot**: també troba opcions de configuració, no només documents.

    Si una opció està **bloquejada** pel centre, no és un error teu: fes-ne captura i apunta-ho. També és una troballa per a l'informe.

#### Pas 1 · Idioma i zona horària

1. Entra a **Outlook** des del llançador d'aplicacions.
2. Fes clic a la **roda dentada (⚙)** de dalt a la dreta.
3. Busca l'apartat **General** i, dins, **Idioma i hora**.
4. Posa l'idioma en **valencià o català**, el format de data el d'ací, i la **zona horària** la de Madrid (UTC+01:00).
5. Guarda.

Ho fem des d'Outlook perquè és on la zona horària té conseqüències reals: si està malament, totes les cites de l'agenda apareixeran a una hora equivocada. A [S3](../../S3_Comunicacio_agenda/index.md) treballarem això a fons.

#### Pas 2 · La carpeta del portafoli a OneDrive

1. Obri **OneDrive** des del llançador d'aplicacions.
2. Fes clic al botó de crear (**+ Nou**, *Afig nou* o *Crea*, segons la versió) i tria **Carpeta**.
3. Anomena-la `Portafoli_AOF_Cognoms_Nom`.
4. Entra-hi i crea dins les carpetes de cada situació, com diu [El portafoli](../../recursos/portafoli.md).

#### Pas 3 · Idioma de correcció a Word

1. Obri **Word** i crea un document nou.
2. Ves a la pestanya **Revisió**.
3. Busca l'opció d'**idioma** i tria la que estableix la **llengua de correcció** del text.
4. Posa-la en **valencià o català**.
5. Comprova-ho: escriu `ordinadorr` i mira si queda subratllat.

#### Pas 4 · Les dades d'usuari i el desat: compara

Estes dues coses **no les configures tu**, i eixa és la lliçó del pas:

- **El teu nom** el fixa el centre en crear-te el compte. A LibreOffice l'has escrit tu al pas 2; ací no pots. Obri un document, fes un comentari i mira amb quin nom apareix. 📸
- **El desat és automàtic i continu**: a LibreOffice has hagut de posar 5 minuts; a Word per al web no hi ha res a configurar. Obri un document, escriu alguna cosa i observa l'indicador de desat. 📸

**Respon a l'informe:** quins avantatges i quins inconvenients té, per a una empresa, que estes dues coses les decidisca el proveïdor i no el tècnic?

## Part 3 · Afegir, llevar i actualitzar

Tres operacions que un tècnic fa constantment. Les faràs amb **un exemple guiat a LibreOffice Writer**: afegiràs un diccionari d'anglés com a **extensió**, comprovaràs si té actualitzacions i després el llevaràs.

Fes una **captura a cada pas marcat amb 📸**.

### 3.1 · Afegir

1. Obri **LibreOffice Writer**.
2. Menú `Eines → Extensions...`. S'obri la llista d'extensions que tens instal·lades. 📸 *(abans)*
3. Fes clic a **Aconseguiu més extensions en línia...**. S'obrirà al navegador la web oficial d'extensions de LibreOffice.
4. Al cercador de la web, busca **English dictionaries**. Entra a la seua pàgina i apunta **la versió** i **l'autor**.
5. Descarrega el fitxer. És un fitxer acabat en **`.oxt`**. Guarda'l a la carpeta de descàrregues.
6. Torna a Writer: `Eines → Extensions...` → botó **Afig**.
7. Selecciona el fitxer `.oxt` que has descarregat i obri'l. Si apareix una llicència, llig-la i accepta-la.
8. Quan LibreOffice ho demane, fes clic a **Reinicia ara**.
9. Torna a `Eines → Extensions...`: l'extensió ha d'aparéixer a la llista. 📸 *(després)*

!!! note "Si no trobes eixa extensió"
    Qualsevol extensió de diccionari de la web oficial serveix: els passos són exactament els mateixos. Apunta quina has triat.

### 3.2 · Actualitzar

1. `Eines → Extensions...`
2. Selecciona l'extensió que acabes d'afegir.
3. Fes clic a **Comprova si hi ha actualitzacions**.
4. Apunta el resultat. 📸
    - Si n'hi ha, aplica-la i apunta la versió d'abans i la de després.
    - Si et diu que no n'hi ha, **també és un resultat**: vol dir que tens l'última versió.

### 3.3 · Llevar

1. `Eines → Extensions...` i selecciona l'extensió.
2. Primer, fes clic a **Inhabilita**. Reinicia i observa què ha canviat. 📸
3. Torna-hi i fes clic a **Suprimeix**. Confirma i reinicia.
4. Comprova a `Eines → Extensions...` que ja no apareix. 📸

**Respon a l'informe:** quina diferència hi ha entre *Inhabilita* i *Suprimeix*? En quina situació d'una empresa usaries cadascuna?

!!! warning "Si el diccionari d'anglés el tenies només per esta extensió"
    Comprova-ho amb el pas 9 de la part 2. Si en llevar l'extensió la paraula `computerr` ja no apareix subratllada, torna a afegir-la: la configuració de l'empresa necessita el diccionari d'anglés.

### 3.4 · I a Microsoft 365?

A M365 també es poden afegir i llevar components: s'anomenen **complements**. Fes només esta comprovació, sense instal·lar res:

1. Obri un document a **Word** per al web.
2. Busca el botó **Complements**. Segons la versió està a la pestanya **Inici** o a **Insereix**; si no el trobes, escriu *complements* al quadre de cerca.
3. Mira la llista i tria'n un qualsevol **sense afegir-lo**: fixa't en **quins permisos demana** (accés als teus documents, a la teua identitat, a internet). 📸
4. Si el centre els té bloquejats, fes-ne captura: també és un resultat.

**Respon a l'informe**, comparant amb el que has fet a LibreOffice:

- Qui decideix **quan s'actualitza** una extensió de LibreOffice? I un complement de M365? I la pròpia aplicació?
- Per què hauria de mirar un tècnic els permisos d'un complement abans de recomanar-lo a un client?

## Part 4 · L'informe

Redacta l'**Informe d'instal·lació** amb esta estructura:

1. Portada amb identificació de l'equip i de l'autor.
2. Taula de decisió (part 1) i comparació amb el programari de l'empresa (part 2.2).
3. Requisits de cada programa, trets de la web oficial, i comparació amb el teu PC (part 2.3).
4. Fitxa d'instal·lació de cada programa que hages instal·lat (part 2.4), **només si n'has instal·lat algun**.
5. Configuració aplicada a LibreOffice i a Microsoft 365 (parts 2.5 i 2.6), amb les captures i amb la resposta del pas 4 de 2.6.
6. Components afegits i eliminats, actualitzacions i la comparació amb M365 (part 3).
7. **Registre d'incidències** (format de la [T4](../teoria/4_documentar.md)).
8. Annex: política de formats de l'empresa, resultat d'[A3](A3_compatibilitat.md).

!!! tip "La prova del nou tècnic"
    Abans de lliurar, llig el teu informe imaginant que no saps res del que has fet. Si hi ha un pas que no podries repetir només amb això, falta informació.

## Com s'avalua

Cada criteri es puntua amb un dels quatre nivells de la [rúbrica de l'empresa](../../recursos/avaluacio.md).

**RA1.a · Identificar i establir les fases del procés d'instal·lació — 15 %**

- 🟢 La taula de decisió està completa i cada tria justificada amb criteris professionals. La comparació amb el programari de l'empresa està feta per a tots els programes i les diferències estan explicades. Les fases apareixen ordenades: planificació, comprovació, requisits, instal·lació si cal, configuració i verificació.
- 🔵 Tot complet, però alguna justificació és feble o alguna diferència amb la llista de l'empresa no s'explica.
- 🟡 Falten necessitats per cobrir, les justificacions són genèriques (*"és el més conegut"*) o la comparació està incompleta.
- 🔴 No hi ha planificació ni comparació: l'informe és una llista del que hi ha instal·lat.

**RA1.b · Respectar les especificacions tècniques — 15 %**

- 🟢 Requisits de **cada programa** trets de la web oficial, amb URL i data, comparats amb les xifres reals del PC. Les dades que la web no publica estan marcades com a *"no publicat"*. Versió instal·lada de cada programa documentada amb captura.
- 🔵 Requisits de tots els programes, però alguna comparació sense xifres concretes o alguna URL absent.
- 🟡 Falten programes, o els requisits no venen de la web oficial, o no es comparen amb el PC.
- 🔴 No hi ha requisits, o són inventats o trets de webs no oficials.

**RA1.c · Configurar les aplicacions segons els criteris establits — 25 %**

- 🟢 Tots els paràmetres aplicats **a les dues suites** i evidenciats amb captures que mostren el valor concret. La prova dels tres diccionaris i la comprovació final de LibreOffice estan fetes. La comparació del pas 4 de 2.6 està raonada en termes d'empresa. Si alguna opció de M365 estava bloquejada, està documentada.
- 🔵 Tot aplicat a les dues suites, però alguna evidència és ambigua, falta una prova o la comparació és superficial.
- 🟡 Només s'ha configurat una de les dues suites, falten paràmetres, o les captures no demostren res.
- 🔴 L'equip ha quedat amb la configuració per defecte.

**RA1.d · Documentar les incidències — 15 %**

- 🟢 Registre complet amb símptoma, causa, solució i verificació per a cada incidència. Si no n'hi ha hagut cap, es documenten les comprovacions fetes per a assegurar-se'n.
- 🔵 Incidències registrades però amb algun apartat curt (falta la verificació, o la causa és una suposició).
- 🟡 Les incidències es mencionen de passada, sense mètode.
- 🔴 No hi ha registre, o diu *"cap incidència"* sense cap comprovació.

**RA1.f · Eliminar i/o afegir components — 15 %**

- 🟢 Extensió afegida i suprimida seguint tots els passos, amb les captures d'abans i després. La diferència entre *Inhabilita* i *Suprimeix* està ben explicada amb un exemple d'empresa. La comprovació de complements de M365 està feta i els permisos analitzats. Si faltava algun programa, està instal·lat i té la seua fitxa.
- 🔵 Les operacions fetes, però falta alguna captura o l'explicació d'*Inhabilita* i *Suprimeix* és superficial.
- 🟡 Només s'ha fet una de les dues operacions (afegir o llevar).
- 🔴 Cap de les dues, o descrites sense evidència.

**RA1.g · Actualitzar les aplicacions — 15 %**

- 🟢 Comprovació d'actualitzacions de l'extensió feta i evidenciada, amb el resultat interpretat correctament. Versió instal·lada de cada programa registrada a la part 2. La resposta sobre **qui decideix quan s'actualitza** cada cosa distingeix correctament programari instal·lat i programari com a servei.
- 🔵 Comprovació feta però sense interpretar el resultat, o falta la versió d'algun programa.
- 🟡 Es diu que s'ha comprovat sense cap evidència.
- 🔴 No s'ha comprovat.

!!! info "Punt de comprensió"
    En revisar el teu informe et faré dues o tres preguntes curtes sobre decisions concretes que hi apareixen. Consulta què significa això a [Com s'avalua](../../recursos/avaluacio.md).
