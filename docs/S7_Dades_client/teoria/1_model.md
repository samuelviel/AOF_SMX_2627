# T1 · Del full a la base de dades

<span class="ca">CA a</span>

## Per què un full de càlcul no basta

Mira este full, que és exactament el que ens ha enviat la gestoria:

| Client | NIF | Telèfon | Població | Expedient | Data | Tipus | Import |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ferreteria Bellver SL | B12345678 | 961234567 | Alzira | EXP-001 | 12/01 | Fiscal | 450 |
| Ferreteria Bellver, S.L. | B12345678 | 961234567 | Alzira | EXP-014 | 03/03 | Laboral | 300 |
| FERRETERIA BELLVER | B12345678 | 961234567 | ALZIRA | EXP-022 | 18/04 | Fiscal | 450 |

Sembla que funcione. Té quatre problemes greus, i tots quatre acaben costant diners.

**1. Redundància.** Les dades del client estan repetides a cada fila. Amb 200 expedients, 200 còpies del telèfon.

**2. Anomalia de modificació.** El client canvia de telèfon. Has d'actualitzar 200 files. En falles tres. Ara tens dos telèfons i no saps quin és el bo.

**3. Anomalia d'inserció.** Un client nou encara no té expedients. No el pots donar d'alta sense inventar-te una fila d'expedient buida.

**4. Anomalia d'esborrat.** Esborres l'últim expedient d'un client i **perds el client**, amb totes les seues dades de contacte.

!!! danger "I el problema que ja es veu a l'exemple"
    Tres escriptures diferents del mateix nom. Cap cerca per "Ferreteria Bellver SL" els trobarà tots tres.

    Això no és un descuit: és **la conseqüència inevitable** d'escriure la mateixa dada moltes vegades. Amb prou files i prou temps, sempre passa.

## La solució

**Una dada s'escriu una vegada, en un sol lloc.** La resta hi apunta.

En lloc d'una taula, dues:

**CLIENTS** — `id_client`, nom, NIF, telèfon, població
**EXPEDIENTS** — `id_expedient`, **`id_client`**, data, tipus, import

Ara el telèfon està en una sola cel·la. Canviar-lo és un canvi. I el nom del client és un únic text, així que la cerca sempre el troba.

## Els conceptes

| Concepte | Què és | Exemple |
| --- | --- | --- |
| **Entitat** | Una cosa de la qual guardem informació | Client, Expedient |
| **Taula** | L'entitat implementada | `CLIENTS` |
| **Registre** (fila) | Una ocurrència | Un client concret |
| **Camp** (columna) | Una propietat | `telefon` |
| **Clau primària** | Identifica **únivocament** un registre | `id_client` |
| **Clau aliena** | Apunta a la clau primària d'una altra taula | `id_client` dins d'`EXPEDIENTS` |
| **Relació** | El vincle entre taules | Un client té molts expedients |

### La clau primària

Ha de ser **única**, **no buida** i **estable** (que no canvie mai).

!!! tip "Millor una clau artificial"
    Podries usar el NIF com a clau primària. És únic... fins que descobreixes que un client el té mal escrit, o que una persona física canvia de NIE, o que un client estranger no en té.

    La pràctica professional és usar un **identificador numèric automàtic** sense cap significat de negoci. El NIF es guarda com un camp més, amb restricció d'únic si cal.

### Els tipus de relació

| Tipus | Exemple | Com s'implementa |
| --- | --- | --- |
| **1 a N** | Un client té molts expedients | Clau aliena a la taula del costat "molts" |
| **N a N** | Un expedient pot tindre diversos serveis, i un servei apareix en molts expedients | **Taula intermèdia** |
| 1 a 1 | Poc freqüent | Clau aliena amb restricció d'únic |

**La relació N a N és la que costa.** No es pot fer directament: cal una tercera taula que continga les dues claus alienes. Si al teu model dos conceptes es relacionen "molts amb molts", ja saps que hi haurà tres taules, no dues.

## Normalització, en pràctic

Sense entrar en les formes normals formals, tres preguntes resolen el 90 % dels casos:

**1. Hi ha alguna cel·la amb diverses coses dins?**

`telefons: 961234567 / 600112233` → no es pot cercar ni ordenar. Separa-ho: o dos camps, o una taula de telèfons.

**2. Hi ha dades repetides a moltes files?**

Si el nom de la població es repeteix 400 vegades, eixa informació pertany a una altra taula (o almenys a una llista controlada).

**3. Hi ha camps que depenen d'un altre camp que no és la clau?**

Si tens `codi_postal` i `població` a la taula d'expedients, i la població depén del client, eixos camps estan en el lloc equivocat.

## El diagrama entitat-relació

Abans de crear res, es dibuixa. Un rectangle per entitat, els camps dins, línies entre elles amb la cardinalitat marcada.

```
┌─────────────┐          ┌──────────────┐
│  CLIENTS    │          │  EXPEDIENTS  │
├─────────────┤          ├──────────────┤
│ PK id_client│──1────N──│ PK id_exp    │
│    nom      │          │ FK id_client │
│    nif      │          │    data      │
│    telefon  │          │ FK id_tipus  │
│ FK id_pobl  │          │    import    │
└─────────────┘          └──────────────┘
```

!!! quote "El diagrama es fa amb paper"
    Cinc minuts de llapis estalvien dues hores de refer taules.

    Un error de model descobert quan ja tens 400 registres carregats i tres formularis fets costa moltíssim més que un error descobert al paper.

## 🤖 IA i modelatge

**Bon ús:** descriure-li el problema i demanar-li que et proposa un model per a **discutir-lo**. Sovint detecta una entitat que se t'havia passat.

**Ús molt bo:** passar-li el teu model i demanar-li que busque anomalies. *"Quines dades quedarien òrfenes si esborre un client?"*

**El que has de fer tu:** decidir. El model depén del negoci concret, i la IA no sap que en esta gestoria un expedient pot canviar de client a mitjan any. Això només ho saps si ho preguntes al client.

## Comprova que ho tens

- [ ] Sé explicar les quatre anomalies amb un exemple de cadascuna.
- [ ] Sé per què és millor una clau primària artificial.
- [ ] Sé identificar una relació N a N i com s'implementa.
- [ ] Sé aplicar les tres preguntes de normalització a un full real.
- [ ] Sé dibuixar un diagrama entitat-relació amb cardinalitats.
