# T3 · Gràfics i taules dinàmiques

<span class="ca">CA d</span>

Un gràfic no decora un informe: **respon una pregunta**. Si no saps quina pregunta respon el teu gràfic, encara no has de fer-lo.

## Triar el tipus

| Vull mostrar... | Tipus | Compte amb |
| --- | --- | --- |
| Evolució en el temps | **Línies** | Que l'eix de temps siga regular |
| Comparar categories | **Barres / columnes** | Que l'eix comence a zero |
| Part d'un total | **Sectors** | Màxim 5-6 porcions |
| Relació entre dues variables | **Dispersió** | No confondre correlació amb causa |
| Composició al llarg del temps | **Àrees apilades** | Es fa il·legible amb moltes sèries |

!!! danger "Els tres enganys clàssics"
    **L'eix truncat.** Un gràfic de barres que comença en 90 en lloc de 0 fa que una diferència del 2 % semble del 200 %. En barres, **l'eix comença a zero, sempre**.

    **Els sectors amb 12 porcions.** Ningú pot comparar visualment 12 angles. Si tens 12 categories, usa barres ordenades.

    **El 3D.** La perspectiva distorsiona les mides: les porcions de davant semblen més grans. No té cap avantatge i sempre enganya.

    Açò no és estètica. Un gràfic que exagera una diferència davant d'un client és **informació falsa**, encara que els números de darrere siguen correctes.

## Els elements que ha de tindre

- **Títol que diu la conclusió**, no la matèria. "Les vendes cauen al segon trimestre" val més que "Vendes per trimestre".
- **Eixos etiquetats amb les unitats.** Un eix que diu "4.500" sense dir de què és inútil.
- **Llegenda** només si hi ha més d'una sèrie.
- **Font i data** de les dades.
- **Colors amb sentit**: coherents amb la identitat de l'empresa, i que funcionen en escala de grisos i per a persones amb daltonisme. No usar **només** el color per a distingir sèries.

## Gràfics que s'actualitzen sols

Si el gràfic apunta a un rang fix (`A2:B20`) i demà afiges una fila, el gràfic no la veu.

**Solucions:**

1. **Convertir les dades en taula/rang de base de dades** — el rang creix sol.
2. **Rang amb nom dinàmic** amb `DESPLAÇAMENT` o `INDEX`.
3. **Deixar files buides preparades** — funciona, però és lleig i pot generar buits al gràfic.

A [A3](../activitats/A3_quadre.md) se't demanarà que el quadre de comandament aguante dades noves sense tocar res. Esta decisió és la clau.

## Taules dinàmiques

Una **taula dinàmica** resumeix una llista llarga agrupant per les categories que tu tries. És l'eina més potent del full de càlcul i la que més gent no usa perquè li fa por.

La idea: tens 800 files de vendes amb columnes `Data`, `Comercial`, `Producte`, `Província`, `Import`. La taula dinàmica respon en dos clics preguntes com "quant ha venut cada comercial per província".

**Les quatre zones:**

| Zona | Què hi poses |
| --- | --- |
| **Files** | La categoria principal d'agrupació |
| **Columnes** | Una segona categoria, per a creuar |
| **Dades** | El que es calcula (suma, compte, mitjana) |
| **Filtres** | El que restringeix la vista sencera |

**Requisits de les dades d'origen** — i ací és on falla tothom:

- [ ] Una fila de capçaleres, **sense cel·les combinades**
- [ ] Una fila per registre, sense files de subtotal enmig
- [ ] Sense columnes ni files buides dins del rang
- [ ] Cada columna d'un sol tipus de dada

!!! tip "Format llarg, no ample"
    ❌ Columnes `Gener`, `Febrer`, `Març`... amb un import a cadascuna.
    ✅ Columnes `Mes` i `Import`, amb una fila per mes.

    El segon format sembla més tediós i és el que permet agrupar, filtrar i graficar de qualsevol manera. **Les dades es guarden en format llarg; l'informe es presenta en format ample.** La taula dinàmica és la que fa la conversió.

    Açò és, de fet, el mateix principi que vorem a [S7](../../S7_Dades_client/index.md) amb les bases de dades.

## Format condicional

Serveix per a que les dades es marquen soles quan passa alguna cosa.

- **Escales de color** per a veure d'un colp d'ull on estan els valors alts i baixos.
- **Barres de dades** dins de la cel·la.
- **Icones** (fletxes, semàfors).
- **Fórmula pròpia** — el més potent: `=$D2<$E2` per a ressaltar tota la fila quan l'estoc baixa del mínim.

A [A2](../activitats/A2_inventari.md) l'usaràs per a l'alerta d'estoc, i a [A3](../activitats/A3_quadre.md) per a marcar desviacions.

## 🤖 IA i gràfics

**Bon ús:** *"Vull respondre esta pregunta amb estes dades. Quin tipus de gràfic em recomanes i per què?"* i, sobretot, demanar-li que critique un gràfic teu.

**Ús molt bo:** passar-li el títol del teu gràfic i preguntar-li si transmet la conclusió o només el tema.

**El que no pot fer:** decidir quina és la pregunta. Això surt de conéixer el negoci, i eixa part és teua.

## Comprova que ho tens

- [ ] Sé triar el tipus de gràfic segons la pregunta.
- [ ] Sé per què l'eix de barres comença a zero.
- [ ] Sé posar un títol que diga la conclusió.
- [ ] Sé fer que un gràfic creixa sol quan s'afigen dades.
- [ ] Sé els requisits que han de complir les dades per a una taula dinàmica.
- [ ] Sé aplicar format condicional amb una fórmula pròpia.
