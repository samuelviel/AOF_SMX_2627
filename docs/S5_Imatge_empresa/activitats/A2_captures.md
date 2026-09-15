# A2 · Captures per al manual

**Sessions 7 i 8** · lliurament: joc de captures + fitxa d'adquisició
**Avalua:** RA5 <span class="ca">b</span> <span class="ca">d</span> <span class="ca">e</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Qualitat documental · Per a: Equip tècnic</p>

He revisat el manual que vam enviar a l'Ajuntament i les captures són un desastre.

N'hi ha una que és la pantalla sencera per a ensenyar un botó. En una altra es veu la teua carpeta de descàrregues. Una tercera està en JPG i el text no es llig.

Refeu-les. I documenteu com les heu fetes, perquè la pròxima vegada isca bé a la primera.
</div>

## La faena

Refés el joc de captures del teu [manual de S2](../../S2_Identitat_documental/activitats/A2_manual.md), amb els criteris professionals de [T2](../teoria/2_captura.md) i [T3](../teoria/3_edicio.md).

### Requisits del joc

Mínim **8 captures**, i entre elles obligatòriament:

- [ ] Una de **regió** d'un element concret
- [ ] Una de **finestra** sencera
- [ ] Una **amb retard**, d'un menú desplegat o un tooltip
- [ ] Una que requerisca **tapar dades sensibles**
- [ ] Una **seqüència numerada** dins de la mateixa imatge (tres passos, tres números)

Totes han de complir:

- [ ] Mateixa resolució de pantalla d'origen
- [ ] Escriptori net: sense notificacions, sense noms personals, sense pestanyes del teu correu
- [ ] Anotació amb **un únic color de ressaltat** en tot el joc, que no aparega a la interfície
- [ ] Format PNG
- [ ] Nom de fitxer segons convenció: `figNN_descripcio.png`
- [ ] Metadades eliminades

### L'edició

<span class="ca">CA d</span> Cada captura ha de mostrar **treball d'edició real**, no només retallada:

- Retall a la zona útil
- Anotació (rectangle, fletxa o numeració)
- Enfosquiment o pixelat de dades sensibles on calga
- Redimensionat a la mida d'ús al document

Almenys **dues captures** han de fer-se amb **capes**, i has de lliurar el fitxer `.xcf` de treball perquè es puga comprovar que l'anotació és una capa separada i no pintada damunt.

!!! tip "Per què les anotacions van en capa separada"
    Perquè d'ací a dos mesos el programa canviarà, refaràs la captura de base i voldràs mantindre l'anotació. O al revés: t'adonaràs que has marcat el botó equivocat.

    Anotar directament sobre la imatge vol dir tornar a començar cada vegada.

## La fitxa d'adquisició

<span class="ca">CA b</span> Una taula amb totes les captures:

| Fitxer | Origen i mode | Paràmetres | Edició aplicada | Per què |
| --- | --- | --- | --- | --- |
| `fig03_menu_opcions.png` | Captura de regió, retard 5 s | 1920×1080 · PNG | Retall, rectangle taronja, redim. 800 px | Menú desplegat; PNG per text nítid |

I un apartat final: **el procediment de captura de l'empresa**. Mitja pàgina que qualsevol company puga seguir per a que les seues captures encaixen amb estes: quina eina, quina resolució, quin color de ressaltat, quin format, quina convenció de noms.

## La comparació

Per a **tres** de les captures, inclou la versió antiga i la nova una al costat de l'altra, amb una línia explicant què s'ha corregit i per què importava.

## Optimització

<span class="ca">CA e</span> Genera **dues versions** de cada captura:

| Versió | Ús | Requisit |
| --- | --- | --- |
| Alta | PDF d'impressió | Resolució suficient per a 150 ppp |
| Web | Manual en línia | Menys de 200 KB, sense pèrdua visible |

Dona el pes de les dues i el percentatge d'estalvi.

## Com s'avalua

### RA5.b) Adquisició amb perifèrics — 35 %

- 🟢 Les cinc modalitats obligatòries cobertes i funcionant (especialment la de retard). Fitxa completa amb paràmetres reals i motiu. El procediment de captura de l'empresa és seguible per un tercer sense preguntes.
- 🔵 Modalitats cobertes i fitxa completa, però el procediment és genèric o falta algun paràmetre.
- 🟡 Falta alguna modalitat, o la fitxa no permet reproduir com es van obtindre.
- 🔴 Captures sense documentar l'origen.

### RA5.d) Eines d'edició emprades — 40 %

- 🟢 Totes les captures retallades, anotades amb criteri coherent i amb les dades sensibles tapades **de manera irreversible**. Les dues amb capes es lliuren en fitxer de treball i l'anotació està en capa pròpia. La comparació antiga/nova és honesta i explica què millorava.
- 🔵 Edició correcta i coherent, però l'anotació d'alguna està pintada sobre la imatge, o la comparació és superficial.
- 🟡 Captures retallades però sense anotar, o amb colors de ressaltat diferents en cada imatge, o dades tapades amb desenfocament reversible.
- 🔴 Captures sense editar, o amb dades personals visibles.

### RA5.e) Importació i exportació — 25 %

- 🟢 Dues versions de cada captura amb pes documentat i estalvi calculat. La versió web baixa de 200 KB sense degradació visible. Format PNG justificat. Metadades eliminades i comprovat.
- 🔵 Dues versions generades i correctes, però sense documentar pesos o sense comprovar les metadades.
- 🟡 Una sola versió, o versió web en JPG amb artefactes visibles al text.
- 🔴 Imatges sense optimitzar de diversos MB.

!!! danger "Dades personals visibles"
    Una sola captura amb dades personals identificables (teues o de tercers) en el lliurament final baixa el CA (d) a 🔴.

    No és una regla de l'aula: és el que passaria de veritat si eixe manual arriba a l'Ajuntament amb el teu correu personal a la barra del navegador.
