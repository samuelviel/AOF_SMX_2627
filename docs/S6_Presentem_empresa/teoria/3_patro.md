# T3 · Patró de diapositives i plantilles

<span class="ca">CA d</span>

És el mateix concepte que els estils de [S2](../../S2_Identitat_documental/teoria/2_estils.md), aplicat a les presentacions. I es fa malament pels mateixos motius.

## Què és el patró

El **patró de diapositives** (o diapositiva mestra) defineix el disseny que hereten totes les diapositives: fons, tipografies, colors, posició dels elements, logotip, numeració.

Canviar el patró canvia **tota la presentació alhora**.

!!! quote "La prova"
    Canvia el color corporatiu al patró. Si les 30 diapositives canvien, el patró està ben fet. Si en canvien 12, les altres 18 tenen format directe i el patró no serveix per a res.

## Patró vs disposicions

**Patró** — el disseny global. Una presentació pot tindre'n diversos (per exemple, un per a seccions de contingut i un per a seccions de dades).

**Disposicions** (*layouts*) — variants dins d'un patró: portada, títol i contingut, dues columnes, imatge a tota pantalla, secció, tancament.

Cada disposició defineix on van els **marcadors de posició**: les caixes que després ompliràs amb text o objectes.

## Marcadors de posició

És el concepte clau, i el que quasi tothom es salta.

Un marcador és una caixa **definida al patró** que apareix ja col·locada a la diapositiva nova. Si escrius dins d'ell, el text hereta el format del patró i està en la posició correcta.

Si en lloc d'això inserixes un quadre de text nou i el col·loques a ull:

- No hereta el format del patró
- No canviarà quan canvies el patró
- Estarà tres píxels desplaçat respecte a la diapositiva anterior
- No apareixerà a la vista esquema

!!! danger "La causa número u de presentacions incoherents"
    Quadres de text col·locats a mà.

    El símptoma és inconfusible: en passar diapositives, el títol "salta". Ningú sap dir per què queda malament, però tothom ho percep.

    **Si el teu flux de treball és "inserisc un quadre de text i el col·loque", no estàs usant el patró.**

## Construir el patró

Vista `Visualitza → Patró de diapositives`.

1. **Fons i colors** de la paleta corporativa
2. **Tipografies** per a títol, cos i detall — els tres nivells de [T2](2_disseny.md)
3. **Posició i mida** dels marcadors de títol i contingut
4. **Logotip** en posició fixa i mida discreta
5. **Numeració** i, si cal, peu
6. **Les disposicions** que necessitareu

!!! tip "El logotip a la portada i a la resta"
    A la portada el logotip pot ser gran; a la resta de diapositives ha de ser xicotet i discret.

    Un logo gran repetit 30 vegades no reforça la marca: ocupa espai i cansa. Per això la portada té la seua pròpia disposició.

## Les disposicions mínimes

| Disposició | Per a què |
| --- | --- |
| **Portada** | Primera diapositiva |
| **Secció** | Separadors entre blocs |
| **Títol i contingut** | La més usada |
| **Dues columnes** | Comparacions |
| **Imatge completa** | Impacte visual amb text superposat |
| **Dada destacada** | Un número gran amb context |
| **Tancament** | Contacte i crida a l'acció |

## Desar com a plantilla

| Suite | Extensió |
| --- | --- |
| LibreOffice Impress | `.otp` |
| PowerPoint / M365 | `.potx` |

`Fitxer → Plantilles → Desa com a plantilla`.

A partir d'ahí, qualsevol persona de l'equip crea una presentació nova i **ja naix amb la identitat de l'empresa**. Que és, exactament, el mateix que vas aconseguir amb la plantilla de documents a [S2](../../S2_Identitat_documental/activitats/A1_plantilla.md).

## Interoperabilitat

`.odp` ↔ `.pptx` funciona raonablement, però amb riscos coneguts:

| Element | Risc |
| --- | --- |
| Patró i disposicions | Mitjà: les disposicions personalitzades es poden degradar |
| Fonts no instal·lades | **Alt** |
| Animacions i transicions | Alt: sovint es perden o canvien |
| Vídeos incrustats | Alt: el còdec pot no ser compatible |
| Gràfics | Es converteixen en imatges amb freqüència |

**Regla:** si has de presentar en un equip que no és el teu, prova-ho **en eixe equip** o porta el PDF. Sempre.

## Comprova que ho tens

- [ ] Sé la diferència entre patró i disposició.
- [ ] Sé què és un marcador de posició i per què no s'usen quadres de text solts.
- [ ] Sé fer la prova del canvi de color al patró.
- [ ] Sé crear les disposicions mínimes.
- [ ] Sé desar la presentació com a plantilla.
- [ ] Sé què es pot trencar en passar a `.pptx`.
