# T4 · El full com a base de dades

<span class="ca">CA g</span> <span class="ca">CA h</span>

Un full de càlcul pot funcionar com una base de dades senzilla. Té límits reals — els vorem a [S7](../../S7_Dades_client/index.md) — però per a un inventari de PIME funciona perfectament, **si està ben construït**.

## Què és una llista ben feta

| Regla | Per què |
| --- | --- |
| **Una sola fila de capçaleres**, a dalt | Els filtres i les taules dinàmiques la necessiten |
| **Una fila = un registre** | Sense excepcions ni files de comentari |
| **Una columna = un camp** d'un sol tipus | No barreges text i números en la mateixa columna |
| **Sense files ni columnes buides** dins | Trenquen la detecció automàtica del rang |
| **Sense cel·les combinades** | Combinar cel·les inutilitza filtres i ordenacions |
| **Sense subtotals enmig** | Els totals van fora de la llista |

!!! danger "Les cel·les combinades"
    Són la causa número u de fulls inservibles. Una vegada combines cel·les dins d'una llista, no pots ordenar, no pots filtrar bé i la taula dinàmica falla.

    Si el que vols és que un títol es veja centrat sobre diverses columnes, usa `Format → Cel·les → Alineació → Centrat entre columnes`. Es veu igual i no trenca res.

## Validació de dades

<span class="ca">CA h</span> **Impedir que s'introduïsquen dades incorrectes** és més barat que netejar-les després.

`Dades → Validesa` (LibreOffice) · `Dades → Validació de dades` (Excel)

| Tipus | Exemple |
| --- | --- |
| **Llista** | Categoria: només "Cablejat", "Emmagatzematge", "Perifèrics" |
| **Número enter / decimal** | Quantitat: entre 0 i 9999 |
| **Data** | Data d'entrada: no posterior a avui |
| **Longitud del text** | Codi: exactament 8 caràcters |
| **Fórmula pròpia** | Que el codi no existisca ja: `=COMPTA.SI($A$2:$A$500;A2)=1` |

Cada validació pot portar **dos missatges**:

- **Ajuda a l'entrada** — apareix en seleccionar la cel·la. Diu què s'espera.
- **Avís d'error** — apareix si s'incompleix. Pot ser *Aturada* (rebutja), *Advertiment* (deixa continuar) o *Informació*.

!!! tip "Un missatge d'error útil"
    ❌ "Valor no vàlid."
    ✅ "El codi d'article ha de tindre 8 caràcters: 3 lletres de categoria + 5 números. Exemple: CAB00142."

    La validació que només diu que no, i no diu què sí, genera una trucada a la [mesa d'ajuda](../../recursos/mesa_ajuda.md).

### Llistes desplegables dependents

Que el desplegable de la segona columna canvie segons el que s'ha triat a la primera. Es fa amb rangs amb nom i la funció `INDIRECTE`.

És un detall que converteix un full en una eina de veritat, i el que fa que algú que no és tècnic el puga usar sense equivocar-se.

## Ordenar

`Dades → Ordena`. Dues coses que importen:

1. **Marca que hi ha capçaleres**, o s'ordenaran amb les dades.
2. **Selecciona tot el rang, no una columna.** Ordenar una sola columna desincronitza les files: els preus queden associats a articles equivocats. És un desastre silenciós i molt difícil de detectar després.

## Filtrar

**Filtre automàtic** — desplegables a les capçaleres. Per a l'ús diari.

**Filtre estàndard / avançat** — condicions múltiples amb `I` i `O`, i permet **copiar el resultat a un altre lloc** en lloc d'amagar files. És el que uses quan vols generar un llistat.

**Filtre per color** — si has usat format condicional, pots filtrar pel que s'ha marcat.

!!! warning "Filtrar amaga, no elimina"
    Les files filtrades continuen existint. Si copies un rang filtrat, segons el mètode t'emportes també les amagades.

    I compte: `SUMA()` **sí** compta les files amagades per un filtre. Si vols sumar només el que es veu, cal `SUBTOTAL()`.

## Protecció

Un full que usarà una altra persona ha d'estar protegit. No per desconfiança: perquè és massa fàcil esborrar una fórmula sense adonar-se'n.

**El mecanisme té dos passos** i la gent oblida el primer:

1. **Desprotegir les cel·les d'entrada.** Per defecte **totes** les cel·les estan marcades com a protegides. Selecciona les que l'usuari ha d'omplir i lleva'ls l'atribut (`Format → Cel·les → Protecció de cel·la`).
2. **Protegir el full.** `Eines → Protegeix el full`. Ara només es poden editar les que has desprotegit.

També es pot **amagar fórmules** perquè no es veja el contingut a la barra, i **protegir l'estructura del llibre** perquè no s'esborren fulls.

!!! note "La contrasenya del full no és seguretat"
    La protecció de full impedeix errors, no atacs: és trivial de saltar per a qui s'ho propose.

    Serveix per a evitar que algú trenque el model sense voler. Per a protegir informació confidencial cal xifrar el fitxer sencer en desar-lo, que és una altra cosa.

## Introduir dades amb perifèrics

<span class="ca">CA h</span>

- **Lector de codis de barres:** es comporta com un teclat. Col·loca el cursor a la columna de codi i cada lectura escriu el codi i baixa una fila. Amb un inventari ben preparat i validació activada, un recompte de magatzem es fa a velocitat de lectura.
- **Escàner / càmera:** per a incorporar imatges de producte o albarans. Compte amb la resolució: una foto de 4000 px dins d'un full multiplica la mida del fitxer.
- **Formularis** (LibreOffice: `Dades → Formulari`; M365: formularis web que aboquen al full) — per a que algú introduïsca dades sense veure ni tocar el model.

## Comprova que ho tens

- [ ] Sé les sis regles d'una llista ben feta.
- [ ] Sé per què les cel·les combinades trenquen una llista i què fer en lloc d'això.
- [ ] Sé crear una validació de llista amb missatge d'error útil.
- [ ] Sé per què no s'ordena una sola columna.
- [ ] Sé la diferència entre `SUMA` i `SUBTOTAL` amb un filtre actiu.
- [ ] Sé els dos passos per a protegir un full deixant cel·les editables.
