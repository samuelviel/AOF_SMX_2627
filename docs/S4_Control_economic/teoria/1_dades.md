# T1 · Dades i referències

<span class="ca">CA a</span> <span class="ca">CA b</span>

## Els tipus de dades

Una cel·la no conté "text". Conté un **valor d'un tipus**, i el tipus determina què s'hi pot fer.

| Tipus | Com es comporta | Com ho reconeixes |
| --- | --- | --- |
| **Número** | S'hi pot calcular | S'alinea a la dreta per defecte |
| **Text** | No s'hi pot calcular | S'alinea a l'esquerra |
| **Data/hora** | És un número per dins | S'alinea a la dreta |
| **Booleà** | CERT / FALS | Centrat |
| **Error** | `#VALOR!`, `#DIV/0!`... | Tot el full en depén |

!!! danger "El número que no és un número"
    El problema més freqüent amb dades importades: **números que el full tracta com a text**.

    Els símptomes: s'alineen a l'esquerra, `SUMA()` els ignora i el total ix més baix del que hauria. Les causes: espais invisibles, separador de milers, un apòstrof davant, o un punt on s'esperava una coma.

    **La comprovació de 2 segons:** selecciona la columna i mira la barra d'estat. Si no et dona la suma, no són números.

### Les dates són números

Una data és el nombre de dies transcorreguts des d'una data d'origen. Per això pots restar dues dates i obtindre dies, o sumar 30 a una data i obtindre el venciment.

Això explica dos comportaments que desconcerten:

- Si a una cel·la amb format de data li escrius `45000`, et mostra una data.
- Si a una cel·la amb una data li lleves el format, et mostra un número gran.

**Regla:** el **format** és com es mostra; el **valor** és el que hi ha dins. Canviar el format no canvia el valor, i canviar el valor no canvia el format. Confondre-ho causa la meitat dels errors de full de càlcul del món.

## Les quatre referències

<span class="ca">CA b</span> Açò és el concepte central de tot el RA3. Si no queda clar, res del que ve després funciona.

Quan copies una fórmula, les referències **es mouen amb ella**, tret que les fixes amb `$`.

| Escrit | Nom | En copiar cap avall | En copiar cap a la dreta |
| --- | --- | --- | --- |
| `A1` | Relativa | Canvia a A2, A3... | Canvia a B1, C1... |
| `$A$1` | Absoluta | No canvia | No canvia |
| `A$1` | Mixta (fila fixa) | No canvia la fila | Canvia la columna |
| `$A1` | Mixta (columna fixa) | Canvia la fila | No canvia la columna |

**Drecera:** ++f4++ sobre una referència va rotant entre els quatre modes.

!!! example "El cas on es veu per què importa"
    Tens preus a la columna B (files 2 a 20) i el **tipus d'IVA a la cel·la F1**.

    A C2 escrius `=B2*$F$1` i ho copies cap avall fins C20. `B2` es va convertint en `B3`, `B4`... (és el que vols), però `$F$1` es queda fixa (també és el que vols).

    Si hagueres escrit `=B2*F1`, la segona fila hauria calculat `B3*F2`, que és una cel·la buida. **Resultat: zeros, i ningú se n'adona fins que el client rep el pressupost.**

### La regla pràctica

Abans de copiar una fórmula, pregunta't cel·la a cel·la: **"quan açò es moga, esta referència s'ha de moure amb ell?"**

- Sí → relativa
- No, és un paràmetre únic (IVA, descompte, any) → absoluta
- Només en una direcció (taules de doble entrada) → mixta

## Referències entre fulls i llibres

**Entre fulls del mateix llibre:**

```
=Dades.B5              (LibreOffice)
=Dades!B5              (Excel/M365)
```

**Rang que travessa diversos fulls:**

```
=SUMA(Gener.B5:Desembre.B5)
```

**Entre llibres diferents:** es pot, i **normalment és mala idea**. El fitxer origen ha d'estar accessible sempre; si algú el mou o el reanomena, tot el que en depén es trenca. Si necessites dades d'un altre llibre de manera estable, importa-les.

## Noms de rang

Pots donar nom a una cel·la o a un rang i usar-lo a les fórmules.

```
=B2*IVA              en lloc de    =B2*$Config.$F$1
=SUMA(Vendes2026)    en lloc de    =SUMA(Dades.C2:C365)
```

**Per què val la pena:**

1. **Es llig.** Qui obri el fitxer entén la fórmula sense anar a buscar què hi ha a `$F$1`.
2. **Són absoluts per defecte.** Un origen menys d'error.
3. **Es poden reassignar** des d'un sol lloc.

`Full → Rangs amb nom → Defineix` (LibreOffice) · `Fórmules → Assignar nom` (Excel).

!!! tip "Criteri professional"
    Qualsevol **paràmetre** del model — IVA, marge, descompte per volum, cost/hora — hauria de ser una cel·la amb nom, en un full de configuració, mai un número escrit dins d'una fórmula.

    Quan el govern canvie l'IVA, vull tocar **una cel·la**, no buscar el 0,21 per tot el llibre.

## Introduir dades sense equivocar-se

<span class="ca">CA h</span> Es treballa a fons a [T4](4_llistes.md), però comença ací:

- **Emplenament de sèries:** arrossegar el controlador d'emplenament genera seqüències (dates, números, dies).
- **++ctrl+enter++** escriu el mateix valor a tota la selecció alhora.
- **Enganxar especial** (++ctrl+shift+v++): enganxar només valors, només formats, o transposar files i columnes. Enganxar valors és el que necessites quan vols congelar un resultat.
- **Des d'un perifèric:** un lector de codis de barres es comporta com un teclat que escriu el codi i prem Enter. Per això un inventari amb columna de codi ben preparada es pot omplir amb un lector sense programar res.

## Personalitzar l'entorn

<span class="ca">CA a</span> El que té impacte real:

| Opció | Per què |
| --- | --- |
| **Nombre de decimals mostrats** | Que es mostren 2 no vol dir que el valor siga de 2. Els totals poden semblar mal sumats |
| **Separador decimal i de milers** | Font número u d'errors amb dades importades |
| **Format de data per defecte** | `03/04/2027` és 3 d'abril o 4 de març segons la configuració |
| **Càlcul automàtic o manual** | En llibres grans es posa en manual; cal saber-ho o pensaràs que les fórmules no funcionen |
| **Precisió com es mostra** | Opció perillosa: canvia els valors reals. Saber que existeix per a **no** activar-la |

## Comprova que ho tens

- [ ] Sé detectar en dos segons si una columna són números o text.
- [ ] Sé explicar per què una data és un número.
- [ ] Sé els quatre tipus de referència i quan usar cadascun.
- [ ] Sé usar ++f4++ per a canviar el tipus de referència.
- [ ] Sé crear un rang amb nom i usar-lo en una fórmula.
- [ ] Sé enganxar només valors i sé quan cal.
