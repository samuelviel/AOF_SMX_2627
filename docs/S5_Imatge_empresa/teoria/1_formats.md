# T1 · Formats, resolució i color

<span class="ca">CA a</span> <span class="ca">CA c</span>

## Mapa de bits vs vectorial

La divisió fonamental. Triar malament ací condiciona tota la resta.

| | Mapa de bits (ràster) | Vectorial |
| --- | --- | --- |
| Com guarda la imatge | Una graella de píxels amb color | Instruccions matemàtiques (línies, corbes, farciments) |
| En ampliar | **Es pixela** | Es manté nítid a qualsevol mida |
| Bo per a | Fotografies, captures de pantalla | Logotips, icones, esquemes, tipografia |
| Formats | PNG, JPG, WEBP, TIFF, GIF | SVG, PDF, EPS, AI |
| Eina | GIMP, Photoshop | Inkscape, Illustrator |

!!! danger "L'error que costa diners de veritat"
    Dissenyar el logotip en mapa de bits.

    Funciona a la web. El dia que l'impremta el demana per a una lona de 3 metres, o per a brodar-lo en una samarreta, **no es pot fer**, i cal tornar a dibuixar-lo des de zero.

    **Un logotip es dissenya sempre en vectorial.** Després se'n generen les versions de mapa de bits que faça falta. Mai al revés.

## Resolució

<span class="ca">CA c</span> Dos números que la gent confon contínuament:

**Dimensions en píxels** — quants píxels té la imatge (1920 × 1080). És el que determina quanta informació hi ha.

**Densitat (ppp/dpi)** — quants píxels per polzada en imprimir. **No canvia la imatge**: canvia la mida a la qual s'imprimeix.

| Destí | Densitat | Exemple pràctic |
| --- | --- | --- |
| Pantalla | 72-96 ppp | Una imatge de 800 px es veu bé |
| Impressió normal | 150 ppp | Documentació interna |
| **Impremta** | **300 ppp** | Cartells, targetes, fullets |
| Gran format (lona) | 100-150 ppp | Es mira de lluny |

**El càlcul que has de saber fer:**

```
píxels necessaris = mida en cm ÷ 2,54 × ppp
```

Una targeta de visita de 8,5 × 5,5 cm a 300 ppp necessita **1004 × 650 píxels** com a mínim.

!!! warning "Ampliar no crea informació"
    Si tens una imatge de 400 px i la vols imprimir a 10 cm en impremta, necessites 1181 px. Ampliar-la a 1181 px no inventa detall: **estira el que hi ha** i es veu borrosa.

    Les eines d'escalat amb IA milloren el resultat, però continuen inventant-se el detall. Per a un logotip això és inacceptable; per a una foto de fons, de vegades passa.

    **La regla:** captura o dissenya sempre a la resolució més alta que necessitaràs. Reduir és gratis; ampliar, no.

## Els formats de mapa de bits

| Format | Compressió | Transparència | Quan usar-lo |
| --- | --- | --- | --- |
| **PNG** | Sense pèrdua | **Sí** (canal alfa) | Captures, logotips en ràster, gràfics amb text |
| **JPG** | **Amb pèrdua** | No | Fotografies |
| **WEBP** | Les dues | Sí | Web moderna: mateixa qualitat, menys pes |
| **GIF** | Sense pèrdua, 256 colors | Sí (binària) | Animacions curtes. Obsolet per a la resta |
| **TIFF** | Sense o sense pèrdua | Sí | Arxiu i impremta |

### Per què les captures van en PNG i no en JPG

El JPG comprimeix agrupant zones de color semblant. Funciona bé amb fotografies, on les transicions són suaus.

Amb **text i vores nítides** —que és exactament el que té una captura de pantalla— genera **artefactes**: brutícia al voltant de les lletres. El text es fa lleig i, a mides xicotetes, il·legible.

!!! danger "La pèrdua del JPG és acumulativa"
    Cada vegada que obris un JPG, l'edites i el tornes a desar, **es torna a comprimir i perd més qualitat**. Deu cicles d'edició degraden visiblement la imatge.

    Per això es treballa en format sense pèrdua (o en el format natiu de l'eina) i s'exporta a JPG **només al final**.

## Color

**RGB** (vermell, verd, blau) — color per llum. Pantalles. És el que uses per defecte.

**CMYK** (cian, magenta, groc, negre) — color per tinta. Impremta.

!!! tip "Per què el cartell es veu diferent imprés"
    RGB pot representar colors que CMYK no pot. Els blaus i verds molt saturats són els que més canvien.

    Si l'impremta et demana CMYK, converteix i **revisa el resultat** abans d'enviar. I si els colors corporatius han de ser exactes, la solució professional és una tinta directa (Pantone), que ja és una altra conversa.

**Transparència (canal alfa)** — permet que part de la imatge siga transparent. Imprescindible per a un logotip: sense ella, el logo porta un rectangle blanc que es veu horrible sobre qualsevol fons de color.

**Profunditat de color** — bits per píxel. 8 bits per canal (16,7 milions de colors) és l'estàndard.

## Metadades

Una imatge porta informació dins: model de càmera, data, configuració, i sovint **coordenades GPS**.

!!! danger "Metadades i privacitat"
    Publicar una foto feta amb el mòbil pot revelar **on i quan** es va fer. En material d'empresa, i especialment en qualsevol cosa que involucre persones, les metadades s'eliminen abans de publicar.

    És un hàbit professional bàsic i, en el cas de dades de localització, també una qüestió de protecció de dades.

## Comprova que ho tens

- [ ] Sé explicar per què un logotip es dissenya en vectorial.
- [ ] Sé calcular els píxels necessaris per a imprimir a una mida i densitat donades.
- [ ] Sé per què les captures van en PNG.
- [ ] Sé què vol dir que la pèrdua del JPG és acumulativa.
- [ ] Sé quan cal RGB i quan CMYK.
- [ ] Sé per què s'eliminen les metadades abans de publicar.
