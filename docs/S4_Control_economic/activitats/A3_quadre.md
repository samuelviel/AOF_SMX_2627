# A3 · El quadre de comandament

**Sessions 17 i 18** · lliurament: quadre de comandament + PDF d'informe
**Avalua:** RA3 <span class="ca">b</span> <span class="ca">c</span> <span class="ca">d</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

Quan em pregunten com va l'empresa, no ho sé dir. Tinc els números en tres llocs i cap em diu res.

Vull **una pantalla** on ho puga veure i entendre-ho en vint segons. I que es mantinga sola: no vull tornar-vos a demanar que la refeu cada mes.
</div>

## El material

Et donaré un fitxer amb **l'històric de l'empresa**: un any de línies de facturació amb data, client, tipus de servei, tècnic, població i import. Unes 400 files, en format llarg.

## Part 1 · Definir les preguntes

Abans de fer cap gràfic, escriu **les cinc preguntes** que ha de respondre el quadre. Preguntes de direcció, no de tècnic:

> *Estem facturant més o menys que fa sis mesos?*
> *De quin client depenem massa?*
> *Quin servei és el que més ingressos genera?*

Per a cadascuna, decideix **quin indicador i quin tipus de gràfic** la responen, i per què.

| # | Pregunta | Indicador | Tipus de gràfic | Per què eixe |
| --- | --- | --- | --- | --- |

!!! tip "El filtre de les cinc preguntes"
    Un quadre de comandament amb dotze gràfics no es llig: es mira. Cinc indicadors ben triats valen més que dotze acumulats.

    Si una pregunta no porta a una decisió possible, no és una pregunta de direcció: és curiositat.

## Part 2 · Construir

### Estructura

| Full | Contingut |
| --- | --- |
| `Dades` | L'històric importat, intacte |
| `Càlculs` | Taules dinàmiques i càlculs intermedis |
| `Quadre` | El que es mira. **Una sola pantalla** |

### Requisits

<span class="ca">CA d</span>

- [ ] Mínim **quatre gràfics de tipus diferents**, cadascun responent una pregunta de la part 1
- [ ] Almenys **dues taules dinàmiques**
- [ ] Títols que **diuen la conclusió**, no la matèria
- [ ] Eixos etiquetats amb unitats, colors coherents amb la identitat de l'empresa
- [ ] Cap gràfic 3D, cap eix truncat, cap sector amb més de 6 porcions

<span class="ca">CA b</span> <span class="ca">CA c</span>

- [ ] Mínim **quatre indicadors numèrics** destacats (facturació de l'any, mitjana mensual, client principal, variació respecte al període anterior)
- [ ] La variació expressada en percentatge i amb **format condicional** que la marque segons siga positiva o negativa
- [ ] Un **selector** (desplegable o filtre) que canvie el període o el tipus de servei i actualitze el que es mostra

### El requisit que decideix la nota

> **Afig files noves al full `Dades` i el quadre s'ha d'actualitzar sol.**

Ho provaré: t'afegiré 20 files de facturació d'un mes nou davant teu. Si has de tocar rangs, redefinir gràfics o refer taules dinàmiques una per una, el quadre no compleix l'encàrrec de direcció ("no vull tornar-vos a demanar que la refeu").

Les vies estan a [T3](../teoria/3_grafics.md): rangs dinàmics, rangs amb nom o zones de base de dades. Tria una i justifica-la.

## Part 3 · L'informe

Una pàgina en PDF, amb la [plantilla corporativa](../../S2_Identitat_documental/activitats/A1_plantilla.md), dirigida a direcció:

1. El quadre (captura o incrustat)
2. **Les tres conclusions** que se'n desprenen, redactades
3. **Una recomanació** basada en els números
4. Què **no** diuen estes dades — els límits de l'anàlisi

!!! warning "El punt 4 no és modèstia"
    Si el 40 % de la facturació ve d'un client i el quadre no ho mostra perquè agrupes per servei, has d'avisar-ne. Un informe que presenta les seues conclusions com a completes quan no ho són és pitjor que no tindre'l.

## Com s'avalua

### RA3.d) Gràfics generats i modificats — 45 %

- 🟢 Quatre tipus de gràfic o més, cadascun **triat per la pregunta que respon** i justificat. Títols que comuniquen conclusió, eixos amb unitats, colors coherents i llegibles també en escala de grisos. Cap dels tres enganys de [T3](../teoria/3_grafics.md). Els gràfics creixen sols amb dades noves.
- 🔵 Gràfics correctes i ben etiquetats, però algun tipus triat per inèrcia o algun títol que només diu la matèria.
- 🟡 Gràfics que funcionen però amb problemes de lectura (eix truncat, massa sèries, 3D), o que no s'actualitzen amb dades noves.
- 🔴 Gràfics que representen malament les dades o que no responen cap pregunta.

### RA3.c) Fórmules i funcions — 30 %

- 🟢 Indicadors calculats correctament, variació percentual ben plantejada, format condicional que la marca, selector funcionant i afectant realment el que es mostra. Els càlculs aguanten dades noves.
- 🔵 Indicadors correctes però el selector és limitat, o la variació està calculada sobre un període fix.
- 🟡 Indicadors escrits a mà o calculats fora del full.
- 🔴 Càlculs erronis.

### RA3.b) Referències entre fulls i rangs — 25 %

- 🟢 Separació neta entre `Dades`, `Càlculs` i `Quadre`, amb referències entre fulls ben construïdes i rangs dinàmics o amb nom. **La prova de les 20 files noves passa sense tocar res.**
- 🔵 Estructura separada i referències correctes, però cal refrescar manualment alguna taula dinàmica.
- 🟡 Tot barrejat en un full o dos, amb rangs fixos que cal editar per a créixer.
- 🔴 Dades modificades directament sobre l'original per a fer quadrar el quadre.
