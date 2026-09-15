# T3 · Instal·lar i configurar com un professional

<span class="ca">CA a</span> <span class="ca">CA b</span> <span class="ca">CA c</span> <span class="ca">CA f</span> <span class="ca">CA g</span>

La diferència entre una instal·lació d'aficionat i una de professional no és el resultat immediat — les dues acaben amb el programa obert. És **què passa d'ací a sis mesos**, quan cal reproduir-la, ampliar-la o explicar-la.

## Les sis fases

Una instal·lació professional segueix sempre el mateix ordre. El CA (a) demana literalment que sàpies identificar-les i establir-les.

### 1. Anàlisi de requisits

Abans de descarregar res: **què necessita fer l'usuari?**

No *"quin programa vull"* sinó *"quines tasques ha de resoldre este equip"*. D'ací ix la llista de programari, no al revés. Si l'equip només ha de redactar informes i fer pressupostos, instal·lar una suite de disseny gràfic és soroll: ocupa espai, s'ha d'actualitzar i amplia la superfície d'atac.

### 2. Verificació de compatibilitat

Contrasta els **requisits del fabricant** amb el que tens:

- Sistema operatiu i versió (i si és de 64 bits).
- RAM i espai lliure en disc — el requisit *recomanat*, no el *mínim*. El mínim serveix per a arrancar, no per a treballar.
- Dependències: biblioteques, entorns d'execució, versions de Java.

!!! tip "Requisit mínim vs recomanat"
    Si un fabricant diu "mínim 4 GB, recomanat 8 GB", instal·lar-ho amb 4 GB no és un estalvi: és garantir-te incidències que després hauràs de diagnosticar. Eixe temps costa més que la RAM.

### 3. Planificació

Escrit **abans** de començar:

- Ordre d'instal·lació (les dependències primer).
- Origen de cada paquet i com en verificaràs l'autenticitat.
- Configuració que aplicaràs.
- Punt de retorn: com desfàs açò si ix malament.

### 4. Obtenció del programari

**Sempre de l'origen oficial.** Repositori de la distribució, botiga del sistema, o web del fabricant. Mai un agregador de descàrregues: empaqueten l'instal·lador real amb adware.

Quan el fabricant publica una **suma de verificació** (`SHA256`), comprova-la. És un minut i t'assegura que el fitxer no s'ha alterat pel camí.

=== "Linux"
    ```bash
    sha256sum libreoffice.deb
    # compara la sortida amb la publicada a la web oficial
    ```

=== "Windows"
    ```powershell
    Get-FileHash .\instalador.exe -Algorithm SHA256
    ```

### 5. Instal·lació

Ací és on la majoria de gent fa clic a "Següent" sense llegir. Els punts on **cal** parar-se:

- **Instal·lació típica vs personalitzada.** La típica sol incloure components que no vols. La personalitzada és la professional.
- **Components opcionals.** Ací s'exerceix el CA (f): decidir què s'afig i què s'elimina, amb criteri.
- **Programari acompanyant.** Barres de navegador, antivirus de prova, canvis de cercador per defecte. Desmarca-ho tot.
- **Ubicació i idioma.** Coherents amb la resta de l'equip.

### 6. Verificació

Una instal·lació sense verificar no està acabada. Comprova com a mínim:

- El programa obri i tanca sense errors.
- Crea, guarda i torna a obrir un fitxer de prova.
- Les associacions de fitxer són les esperades.
- Els components opcionals que volies hi són, i els que no volies, no.

## Configurar segons criteris d'empresa

<span class="ca">CA c</span> Este és el criteri que més gent suspén, perquè confon *instal·lar* amb *deixar llest per a treballar*.

Configurar segons criteris vol dir que **totes les màquines de l'empresa es comporten igual**. Si cada equip guarda en un format diferent, els documents circulen malament i algú acaba perdent faena.

Decisions mínimes que ha de prendre l'empresa i que aplicaràs a [A1](../activitats/A1_installacio.md):

| Decisió | Per què importa |
| --- | --- |
| **Format de desat per defecte** | Determina amb qui pots intercanviar documents sense perdre res. Ho decidireu a [A3](../activitats/A3_compatibilitat.md) |
| **Carpeta de treball per defecte** | Evita que la faena acabe escampada pel disc |
| **Desat automàtic i recuperació** | Cada quants minuts. Un tall de llum no hauria de costar una vesprada |
| **Idioma de la interfície i del corrector** | Poden ser diferents, i sovint han de ser-ho |
| **Dades d'usuari** | El nom que apareixerà als comentaris i al control de canvis |
| **Fonts corporatives** | Instal·lades a tots els equips, o els documents es descol·loquen |

!!! example "On es toca cada cosa"
    === "LibreOffice"
        - Format per defecte: `Eines → Opcions → Carrega/Desa → General`
        - Desat automàtic: mateixa pantalla, *Desa la informació de recuperació*
        - Dades d'usuari: `Eines → Opcions → LibreOffice → Dades d'usuari`
        - Rutes: `Eines → Opcions → LibreOffice → Camins`

    === "Microsoft 365 Online"
        - Molta configuració és de compte, no d'equip: es fa una vegada i segueix l'usuari.
        - El desat és continu a OneDrive/SharePoint; el que cal decidir és **l'estructura de carpetes compartides**.
        - Les fonts han d'estar disponibles per a tots els membres, o la versió web les substituirà.

## Afegir i eliminar components

<span class="ca">CA f</span> Una instal·lació no és definitiva. Sabràs **modificar-la després** sense reinstal·lar-ho tot.

- **Extensions i complements.** LibreOffice en té (`.oxt`) per a diccionaris, plantilles o exportacions. M365 té complements des de la botiga. Ambdós s'afigen i es lleven en calent.
- **Desinstal·lar component a component.** A LibreOffice pots executar l'instal·lador en mode modificació i llevar mòduls que no uses.
- **Desinstal·lar del tot.** Compte: desinstal·lar sovint deixa els fitxers de configuració d'usuari. Si el motiu de desinstal·lar era un perfil corrupte, cal esborrar-los a mà — vegeu [T4](4_documentar.md).

## Actualitzar

<span class="ca">CA g</span> Actualitzar no és opcional: és el mecanisme pel qual es tanquen vulnerabilitats conegudes.

Tipus d'actualització:

| Tipus | Què canvia | Risc |
| --- | --- | --- |
| **Seguretat** | Tanca forats | Baix — s'apliquen sempre |
| **Menor** (7.6.2 → 7.6.3) | Correccions de funcionament | Baix |
| **Major** (7.6 → 24.2) | Funcions noves, possibles canvis de format | Mitjà — prova-la abans |

En una empresa, l'actualització major es prova **en un equip** abans de desplegar-la a tots. Este curs eixe equip seràs tu.

## Comprova que ho tens

- [ ] Sé enumerar les sis fases en ordre i dir què es fa a cadascuna.
- [ ] Sé on comprovar els requisits del fabricant d'un programa concret.
- [ ] Sé verificar un `SHA256` al meu sistema.
- [ ] Sé canviar el format de desat per defecte i el temps de desat automàtic.
- [ ] Sé afegir una extensió i tornar a llevar-la.
- [ ] Sé distingir una actualització de seguretat d'una de versió major.
