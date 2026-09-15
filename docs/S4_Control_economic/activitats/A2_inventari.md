# A2 · L'inventari

**Sessions 12 a 14** · lliurament: full d'inventari operatiu
**Avalua:** RA3 <span class="ca">c</span> <span class="ca">g</span> <span class="ca">h</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

El magatzem és un caos. La setmana passada vam comprar 50 metres de cable que ja teníem i alhora ens vam quedar sense discos a mitjan instal·lació d'un client.

Necessite saber **què tenim, on està i quan s'acaba**. I necessite que ho puga omplir gent que no sap de fulls de càlcul sense trencar-ho.
</div>

## El producte

Un llibre amb l'estructura mínima:

| Full | Contingut |
| --- | --- |
| `Articles` | Catàleg: codi, descripció, categoria, ubicació, estoc mínim, proveïdor |
| `Moviments` | Entrades i eixides: data, codi, tipus, quantitat, motiu, qui |
| `Estat` | Estoc actual calculat, alertes i llistat de reposició |
| `Config` | Categories, ubicacions, proveïdors (els orígens dels desplegables) |

!!! tip "Per què moviments i no una columna d'estoc"
    Podries tindre una columna `Estoc` i que la gent la modificara. És més simple i **és un error**: perds l'historial i, quan el número no quadra, no pots saber per què.

    Amb moviments, l'estoc és un **càlcul** (`=SUMA.SI` d'entrades − `SUMA.SI` d'eixides) i sempre pots reconstruir què ha passat. És el mateix principi que vorem a [S7](../../S7_Dades_client/index.md).

## Requisits

### Llista ben construïda

<span class="ca">CA g</span> Les sis regles de [T4](../teoria/4_llistes.md), i les comprovaré:

- [ ] Una fila de capçaleres, **cap cel·la combinada**
- [ ] Una fila per registre, sense subtotals enmig
- [ ] Sense files ni columnes buides dins del rang
- [ ] Cada columna d'un sol tipus

### Validació de dades

<span class="ca">CA h</span> Mínim **cinc validacions**, i entre elles:

- [ ] Un desplegable de **llista** (categoria, ubicació o proveïdor) amb origen al full `Config`
- [ ] Una validació de **rang numèric** (quantitat > 0)
- [ ] Una validació de **data** (no futura)
- [ ] Una validació amb **fórmula pròpia** (que el codi existisca al catàleg, o que no es duplique)
- [ ] Almenys **dos desplegables dependents** (en triar categoria, la llista d'articles es filtra)

Cada validació amb **missatge d'ajuda** i **missatge d'error útil**, en els termes de [T4](../teoria/4_llistes.md).

### Càlculs i alertes

<span class="ca">CA c</span>

- [ ] Estoc actual per article, calculat des de `Moviments`
- [ ] Comparació amb l'estoc mínim
- [ ] **Format condicional amb fórmula** que marque la fila sencera quan l'estoc baixe del mínim
- [ ] Un llistat de reposició: només els articles que cal comprar, amb quantitat suggerida
- [ ] Valor total de l'inventari

### Filtres, ordenació i protecció

<span class="ca">CA g</span>

- [ ] Filtre automàtic operatiu a les llistes
- [ ] Un **filtre estàndard** guardat que responga una pregunta concreta (per exemple: material de xarxa per davall del mínim d'un proveïdor determinat), amb el resultat copiat a un altre rang
- [ ] Un total que respecte el filtre (`SUBTOTAL`), demostrat amb captura amb filtre actiu i sense
- [ ] **Full protegit** deixant editables només les cel·les d'entrada de `Moviments`
- [ ] Fórmules protegides al full `Estat`

## La prova d'usabilitat

**Sessió 14.** Un company que no ha vist el teu fitxer intenta registrar tres moviments en **5 minuts, sense que li expliques res**.

Anota:

- Quant tarda
- On dubta
- Què intenta fer que el sistema no li deixa
- Si aconsegueix trencar alguna cosa

I després **arregla el que hages detectat**. Este apartat va al lliurament i és, probablement, el que més t'ensenyarà de tota l'activitat.

!!! warning "Si el teu company trenca el full, no és culpa seua"
    És exactament el que farà l'usuari real. La protecció i la validació existeixen precisament per a això.

## Com s'avalua

### RA3.g) El full com a base de dades — 45 %

- 🟢 Llista impecable segons les sis regles. Filtre automàtic i filtre estàndard amb resultat extret. `SUBTOTAL` demostrat amb evidència. Protecció de dos nivells funcionant: es poden registrar moviments i no es pot trencar cap fórmula. Ordenacions correctes sobre el rang complet.
- 🔵 Estructura correcta i protecció funcionant, però el filtre estàndard és senzill o falta la demostració del `SUBTOTAL`.
- 🟡 Alguna regla de llista incomplida (cel·la combinada, fila buida), o protecció que bloqueja també l'entrada de dades, o filtres només automàtics.
- 🔴 El full no funciona com a llista: no es pot filtrar ni ordenar sense trencar-lo.

### RA3.h) Entrada de dades amb aplicacions i perifèrics — 30 %

- 🟢 Cinc validacions o més amb tots els tipus demanats, incloent-hi fórmula pròpia i desplegables dependents funcionant. Missatges d'ajuda i d'error **útils** (diuen què s'espera). La prova d'usabilitat s'ha fet, s'han registrat els problemes i s'han corregit.
- 🔵 Validacions completes i funcionals, però algun missatge d'error genèric, o la prova d'usabilitat feta sense corregir després.
- 🟡 Validacions bàsiques sense fórmula pròpia ni dependències, o sense prova d'usabilitat.
- 🔴 Sense validació: qualsevol cosa es pot escriure a qualsevol cel·la.

### RA3.c) Fórmules i funcions — 25 %

- 🟢 Estoc calculat des de moviments (no escrit a mà), alertes automàtiques, llistat de reposició dinàmic, format condicional amb fórmula que marca la fila sencera. Tot aguanta l'addició de moviments nous sense tocar res.
- 🔵 Càlculs correctes però el llistat de reposició s'ha de refrescar a mà, o el format condicional marca només la cel·la.
- 🟡 L'estoc s'escriu a mà en lloc de calcular-se, o les alertes són visuals sense fórmula.
- 🔴 Càlculs incorrectes o inexistents.
