# A1 · El pressupost

**Sessions 6 a 8** · lliurament: plantilla `.ots`/`.xltx` + PDF de mostra
**Avalua:** RA3 <span class="ca">a</span> <span class="ca">b</span> <span class="ca">c</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

Cada pressupost que enviem el fa algú d'una manera. Dos dels últims tenien l'IVA mal calculat i un va eixir amb un descompte que no havíem acordat.

Vull una **plantilla de pressupost** que no es puga equivocar. Que qui l'òmpliga només haja d'escriure el que ha d'escriure, i la resta ixca sola.
</div>

## El producte

Una **plantilla** (no un document) amb tres fulls separats, segons el principi de [T2](../teoria/2_formules.md):

| Full | Contingut | Qui el toca |
| --- | --- | --- |
| `Config` | IVA, descomptes per volum, cost/hora, dades de l'empresa | Direcció, una vegada l'any |
| `Pressupost` | El document que es lliura al client | Qui fa el pressupost |
| `Catàleg` | Articles i serveis amb preu | Qui manté el catàleg |

## Requisits funcionals

### Full `Config`

- [ ] Tipus d'IVA en una **cel·la amb nom**
- [ ] Taula de descomptes per volum (a partir de X €, Y % de descompte)
- [ ] Cost per hora de mà d'obra
- [ ] Dades de l'empresa que apareixeran a la capçalera del pressupost
- [ ] **Cap d'estos valors escrit dins de cap fórmula**

### Full `Catàleg`

Mínim 15 articles/serveis amb codi, descripció, unitat i preu unitari. Els codis han de seguir un patró consistent.

### Full `Pressupost`

- [ ] Capçalera amb dades de l'empresa **per referència** al full `Config`
- [ ] Dades del client i número de pressupost
- [ ] Data i **data de validesa calculada** (data + 30 dies)
- [ ] Línies de detall: **escrius el codi i s'omplin soles** descripció i preu unitari (funció de cerca)
- [ ] Columna de quantitat i d'import de línia
- [ ] Base imposable, descompte aplicat automàticament segons la taula, IVA i total
- [ ] Gestió d'errors: les línies buides no han de mostrar `#N/D` ni `#VALOR!`
- [ ] Un codi inexistent ha d'avisar de manera comprensible, no petar

!!! tip "El requisit que val nota"
    *"Escrius el codi i s'omplin soles descripció i preu."*

    És on es demostra que has entés les referències absolutes i les funcions de cerca. Si el pressupost obliga a escriure el preu a mà, la plantilla no resol el problema que ens ha plantejat direcció: continua podent-se equivocar.

### Comprovacions

Almenys **dues cel·les de verificació** com les de [T2](../teoria/2_formules.md):

- Que la suma de línies quadre amb la base imposable
- Que el total siga coherent amb base + IVA − descompte

Han de mostrar `OK` o `REVISAR`, visibles per a qui usa la plantilla però fora de la zona d'impressió.

## Presentació

El pressupost s'imprimeix i s'envia al client. Per tant:

- [ ] **Àrea d'impressió** definida: una pàgina A4
- [ ] Format de moneda amb dos decimals
- [ ] Coherent amb la [identitat corporativa](../../S2_Identitat_documental/activitats/A1_plantilla.md) de S2
- [ ] Exportat a PDF per al lliurament de mostra

## La fitxa de configuració

<span class="ca">CA a</span> Igual que a [S2/A1](../../S2_Identitat_documental/activitats/A1_plantilla.md): quatre paràmetres de l'entorn que has ajustat, amb ruta, valor i motiu. En full de càlcul, els que solen tindre impacte real són els decimals mostrats, els separadors, el format de data i el mode de càlcul.

## Com s'avalua

### RA3.b) Tipus de dades i referències — 35 %

- 🟢 Tots els paràmetres del model estan a `Config` com a **cel·les amb nom**, referenciades des de les fórmules. Les referències absolutes, relatives i mixtes s'usen correctament: copiar qualsevol fórmula de columna cap avall funciona sense tocar res. Els tipus de dada són correctes (codis com a text, imports com a número, dates com a data).
- 🔵 Model ben separat i referències correctes, però algun paràmetre sense nom de rang o alguna referència absoluta posada "per si de cas" on no calia.
- 🟡 Hi ha valors escrits dins de fórmules (un `*0,21` per ahí), o alguna fórmula es trenca en copiar-la.
- 🔴 Tot en un full, amb números dins de les fórmules.

### RA3.c) Fórmules i funcions aplicades — 45 %

- 🟢 La cerca per codi funciona amb coincidència exacta i rang absolut. El descompte per volum s'aplica sol segons la taula. Els errors estan gestionats **on tocava i no on no tocava**. Les dues cel·les de verificació funcionen i detecten un descuadre si el provoques. Les xifres monetàries estan arrodonides amb funció, no només amb format.
- 🔵 Tot calcula bé, però la gestió d'errors amaga algun error que no hauria d'ocórrer, o falta l'arrodoniment real en diners.
- 🟡 Els càlculs bàsics funcionen però la cerca per codi no, o el descompte s'aplica a mà, o falten les comprovacions.
- 🔴 Fórmules que donen resultats incorrectes, o el pressupost obliga a escriure-ho tot a mà.

### RA3.a) Opcions de programari personalitzades — 20 %

- 🟢 Quatre paràmetres o més amb ruta, valor i motiu lligat a esta faena concreta. Àrea d'impressió i format de pàgina configurats perquè el PDF isca bé a la primera.
- 🔵 Fitxa completa i reproduïble amb alguna justificació genèrica.
- 🟡 Canvis sense ruta o sense motiu; o el PDF ix tallat en diverses pàgines.
- 🔴 No hi ha fitxa.

!!! quote "Punt de comprensió"
    *"Puja l'IVA al 23 %. Ensenya-m'ho."*

    Si tardes més de deu segons, la plantilla no compleix l'encàrrec.
