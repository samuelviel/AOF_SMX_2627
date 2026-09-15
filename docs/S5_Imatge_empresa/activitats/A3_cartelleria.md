# A3 · Cartell i targeta

**Sessions 9 i 10** · lliurament: PDF d'impremta + versions web
**Avalua:** RA5 <span class="ca">a</span> <span class="ca">c</span> <span class="ca">d</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

Per a la jornada de PIMEs del mes que ve necessite:

- Un **cartell A3** per a l'estand
- **Targetes de visita** per a repartir

L'impremta em diu que ho vol "en PDF a 300 ppp amb 3 mm de sagnat i en CMYK". Doneu-los-ho com ho demanen, que l'última vegada ens ho van tornar.
</div>

## Part 1 · La targeta de visita

**Mida:** 85 × 55 mm · **Sagnat:** 3 mm per costat · **Marge de seguretat:** 4 mm interiors

Contingut mínim: logotip, nom i càrrec, telèfon, correu, web.

- [ ] Document configurat en **mil·límetres**, mida real
- [ ] Marques de sagnat i marge de seguretat visibles al document de treball
- [ ] Cap element important dins del marge de seguretat
- [ ] Cap fons que arribe just a la vora (ha d'eixir fins al sagnat)
- [ ] Text convertit a camins a la versió d'impremta
- [ ] Mida de lletra mínima 7 pt (per davall no es llig)

!!! tip "Per què existeix el sagnat"
    La guillotina de l'impremta no talla amb precisió de dècimes. El sagnat és material extra que es perd al tall.

    Si el teu fons acaba exactament a la vora, el tall pot deixar una línia blanca en un costat. Si el telèfon està a 1 mm de la vora, pot quedar tallat.

## Part 2 · El cartell A3

**Mida:** 297 × 420 mm · **Sagnat:** 3 mm · **300 ppp**

Ha de comunicar, a 3 metres de distància: **qui sou, què feu i com contactar**.

- [ ] Jerarquia visual clara: es llig en el mateix ordre per a tothom
- [ ] Missatge principal llegible **a 3 metres**
- [ ] Coherent amb el [kit de marca](A1_marca.md) i la [guia d'ús](A1_marca.md)
- [ ] Màxim tres nivells tipogràfics
- [ ] Almenys una **imatge de mapa de bits** editada per tu, amb la resolució suficient

<span class="ca">CA c</span> Justifica el càlcul: quina mida ocupa la imatge al cartell i quants píxels necessita a 300 ppp. Si la imatge de què disposes no arriba, has de dir-ho i resoldre-ho — no ampliar-la i fer com si res.

### L'edició de la imatge

<span class="ca">CA d</span> La imatge del cartell ha de portar treball real documentat: retall i composició, ajust de nivells o corbes, i almenys una **màscara de capa** per a integrar-la amb el fons.

Lliura el fitxer de treball amb les capes nomenades.

## Part 3 · Preparar per a impremta

<span class="ca">CA a</span> Ací és on falla la majoria.

- [ ] Conversió a **CMYK** i revisió: quins colors han canviat i quant
- [ ] **Incrustar o convertir** totes les fonts
- [ ] Resolució efectiva de totes les imatges a 300 ppp
- [ ] PDF exportat amb sagnat i marques de tall
- [ ] Comprovació final: obri el PDF resultant i mira'l al 100 %

**I les versions web**, que són un producte diferent:

| Versió | Format | Requisit |
| --- | --- | --- |
| Cartell per a xarxes | PNG o JPG | 1080 px de costat major, menys de 500 KB |
| Targeta per a signatura de correu | PNG | Menys de 50 KB |

## La fitxa tècnica

Una pàgina que acompanya el lliurament a l'impremta:

| Peça | Mida final | Sagnat | Resolució | Color | Fonts | Fitxer |
| --- | --- | --- | --- | --- | --- | --- |

Més un apartat de **què ha canviat en passar a CMYK** i què s'ha fet al respecte.

## Com s'avalua

### RA5.c) Resolucions segons finalitat — 40 %

- 🟢 Tot a 300 ppp efectius, **amb el càlcul fet i escrit** per a les imatges del cartell. Les versions web compleixen els límits de pes amb el pes real documentat. Cap imatge ampliada des d'un original insuficient; si el material original no arribava, es diu i es resol.
- 🔵 Resolucions correctes però algun càlcul absent o aproximat.
- 🟡 Alguna imatge per davall de la resolució necessària, o versions web sense optimitzar.
- 🔴 Imatges ampliades i pixelades al material d'impremta.

### RA5.a) Formats analitzats — 30 %

- 🟢 PDF d'impremta amb sagnat, marques, CMYK i fonts resoltes. La fitxa tècnica està completa i l'apartat de canvi de color identifica **quins colors concrets** han variat i què s'ha decidit. Les versions web en el format adequat i justificat.
- 🔵 PDF correcte i fitxa completa, però l'anàlisi del canvi a CMYK és genèrica.
- 🟡 Falta el sagnat o el CMYK, o el PDF porta fonts no incrustades.
- 🔴 Lliurament en format que l'impremta rebutjaria (JPG a 72 ppp, RGB, sense sagnat).

### RA5.d) Eines d'edició — 30 %

- 🟢 Composició amb jerarquia visual que funciona a la distància prevista, coherent amb la guia de marca. Imatge amb edició real documentada (retall, nivells, màscara de capa). Fitxers de treball lliurats amb capes nomenades.
- 🔵 Composició correcta i edició feta, però el fitxer de treball està desordenat o la màscara no s'ha usat.
- 🟡 Peces muntades amb elements col·locats sense jerarquia, o imatge sense editar.
- 🔴 Ús d'imatges de tercers sense llicència verificada, o incompliment de la guia de marca pròpia.

!!! warning "Recordatori de drets"
    Tota imatge que no hages fet tu ha de portar **origen i llicència citats** a la fitxa tècnica, amb ús comercial verificat com vas aprendre a [S1/A2](../../S1_Posada_marxa/activitats/A2_llicencies.md).

    Una imatge sense llicència comprovada en material d'empresa és el mateix problema que el programari sense llicència, i té el mateix tipus de conseqüència.
