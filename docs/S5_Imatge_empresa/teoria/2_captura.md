# T2 · Captura i adquisició

<span class="ca">CA b</span>

El CA (b) parla d'adquirir imatges **amb perifèrics**. A la nostra faena, els tres orígens són la captura de pantalla, l'escàner i la càmera.

## Captura de pantalla

És, de llarg, la imatge que més produiràs a la teua vida professional. I quasi tothom la fa malament.

### Els modes

| Mode | Quan |
| --- | --- |
| Pantalla sencera | Quasi mai. Genera imatges enormes amb 95 % d'informació irrellevant |
| **Finestra activa** | El més habitual en documentació |
| **Regió** | Quan documentes un element concret |
| **Amb retard** | Imprescindible per a capturar menús desplegats o tooltips |

!!! tip "El truc del retard"
    Un menú obert es tanca en el moment que prems la tecla de captura. La solució és configurar un **retard de 3-5 segons**: actives la captura, obris el menú i espera.

    És el detall que separa una documentació que es pot fer d'una que sembla impossible.

### Bones pràctiques

- **Resolució de pantalla consistent.** Si captures algunes imatges a 1920 i altres a 1366, al manual es veuran de mides diferents i els elements no coincidiran.
- **Neteja l'escriptori abans.** Notificacions, noms de fitxers personals, pestanyes del navegador amb el teu correu: tot això acaba publicat.
- **Dades sensibles tapades.** Adreces, noms reals, números de compte. Tapar-les de veritat: un rectangle negre damunt, no un desenfocament (que de vegades es pot revertir).
- **Tema clar per a documentació impresa.** Un tema fosc gasta tinta i es llig pitjor en paper.

### Anotar la captura

Una captura sense anotar obliga el lector a buscar de què li parles. Els elements que funcionen:

- **Rectangle o el·lipse** de color viu al voltant de l'element
- **Fletxa** quan cal apuntar des de fora
- **Numeració** quan hi ha diversos passos en la mateixa imatge
- **Desenfocament o pixelat** per a dades que s'han d'amagar

**Un color de ressaltat per a tot el document**, i que no siga un color que ja aparega a la interfície.

## Escàner

| Paràmetre | Valor típic | Nota |
| --- | --- | --- |
| Resolució | 300 ppp text · 600 ppp per a OCR fi | Més no millora, només fa el fitxer més gran |
| Mode | Color, escala de grisos o blanc i negre | Blanc i negre per a text: fitxers minúsculs |
| Format | PNG o TIFF per a arxiu · PDF per a documents | JPG no, per als mateixos motius de [T1](1_formats.md) |

**Protocols d'escaneig:** TWAIN (el clàssic), SANE (Linux), WIA (Windows). En saber que existeixen entens per què de vegades un escàner funciona amb un programa i no amb un altre: cal el controlador del protocol correcte.

## Càmera i mòbil

Per a fotos de producte, d'un equip instal·lat o d'una incidència.

- **Il·luminació** abans que res. Cap ajust posterior arregla una foto fosca tan bé com fer-la amb llum.
- **Fons net.** Una foto de producte sobre una taula desordenada no és material d'empresa.
- **Resolució màxima** en captura. Ja reduiràs després.
- **RAW vs JPG:** el RAW conserva tota la informació del sensor i permet recuperar zones cremades o fosques. Ocupa molt més. Per a material d'empresa que s'editarà, val la pena.

!!! warning "Fotografies amb persones"
    Si apareix qualsevol persona identificable en una imatge que es publicarà, cal el seu **consentiment explícit**.

    A este mòdul: cap fotografia de companys en material publicat sense que ho hagen autoritzat expressament, i cap imatge del centre que permeta identificar persones.

## Documentar l'adquisició

Per al CA (b) no n'hi ha prou amb tindre les imatges: cal **saber dir com s'han obtingut**, amb quins paràmetres i per què eixos.

El format que se't demanarà a [A2](../activitats/A2_captures.md):

| Imatge | Origen | Paràmetres | Per què |
| --- | --- | --- | --- |
| `fig03_menu_opcions.png` | Captura de regió amb retard 5 s | 1920×1080, PNG | Menú desplegat; PNG per text nítid |

## Comprova que ho tens

- [ ] Sé capturar un menú desplegat.
- [ ] Sé per què cal mantindre la resolució de pantalla constant.
- [ ] Sé què s'ha de netejar de l'escriptori abans de capturar.
- [ ] Sé a quina resolució escanejar text per a OCR.
- [ ] Sé per què es fotografia en RAW quan la imatge s'editarà.
- [ ] Sé què cal per a publicar una imatge amb persones.
