# A2 · Automatitza la safata

**Sessió 6** · lliurament: esquema d'automatització + evidència de funcionament
**Avalua:** RA8 <span class="ca">b</span> <span class="ca">f</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic · Assumpte: açò és inviable

</p>

Acabe de mirar la safata del correu general de l'empresa. 1.847 missatges sense llegir.

Hi ha dins pressupostos de clients, alertes de còpies de seguretat, publicitat, factures i tres incidències que ningú ha vist. Ho vull ordenat, i no a mà: vull que s'ordene sol.
</div>

## El material

Et donaré un **volcat de 40 missatges** simulats de la safata general: barreja de clients, proveïdors, notificacions automàtiques, incidències, publicitat i un parell de correus sospitosos.

La teua faena és dissenyar el sistema que els posaria al seu lloc sense intervenció humana, i **demostrar que funciona**.

## Part 1 · Analitzar abans d'automatitzar

<span class="ca">CA b</span> El pas que la gent es salta.

1. **Classifica** els 40 missatges a mà primer. Quantes categories reals apareixen? No inventes categories: mira què hi ha.
2. Per a cada categoria, respon:
   - Qui l'ha d'atendre?
   - Amb quina urgència?
   - Ha d'interrompre o es consulta quan toca?
3. **Detecta el patró** que identifica cada categoria: remitent, domini, paraula a l'assumpte, adreça de destinació...

| Categoria | Quants | Qui l'atén | Urgència | Patró identificable |
| --- | --- | --- | --- | --- |

!!! warning "El patró ha de ser fiable"
    Filtrar per la paraula "factura" a l'assumpte captura les factures **i** el correu del client que pregunta *"m'heu enviat ja la factura?"*, que és una consulta, no una factura.

    Els bons patrons solen ser **remitent o domini**, no paraules del text. Quan has d'usar text, combina condicions.

## Part 2 · Dissenyar l'estructura

Estructura de carpetes i/o etiquetes, amb la seua **justificació**. Recorda el criteri de [T2](../teoria/2_gestio.md): l'estructura respon a com busques, no a com arriba.

Màxim **dos nivells d'anidament**. Si necessites tres, probablement el que et cal és una etiqueta.

## Part 3 · Els filtres

<span class="ca">CA f</span> Mínim **6 filtres**, i entre ells obligatòriament:

- [ ] Un que combine **dues o més condicions**
- [ ] Un que aplique **dues o més accions**
- [ ] Un que distingisca si vas en `To` o en `Cc`
- [ ] Un per a notificacions automàtiques que **no marque com a llegit** (has de poder saber si han arribat)
- [ ] Un per a correu potencialment perillós que **el moga, no l'esborre**

Documenta cada filtre en format taula:

| # | Nom | Condicions | Accions | Ordre | Per què |
| --- | --- | --- | --- | --- | --- |

### La prova de l'ordre

Explica **per què els filtres estan en eixe ordre** i què passaria si intercanviares dos concrets. Este apartat val nota: és on es demostra que has entés com s'apliquen.

### Evidència

Captures de la safata **abans i després** d'executar els filtres sobre els 40 missatges. Si algun missatge acaba on no tocava, no ho amagues: documenta'l i explica per què el patró ha fallat. Un fals positiu detectat i explicat val més que una safata perfecta sospitosa.

## Part 4 · Plantilles i absència

- **Dues plantilles de resposta** per als casos que més es repeteixen en els 40 missatges. Han d'incloure els camps que no es poden oblidar.
- **Una resposta d'absència** amb les tres coses de [T2](../teoria/2_gestio.md): fins quan, a qui escriure, què fer si és urgent.

## Com s'avalua

### RA8.b) Necessitats de gestió analitzades — 40 %

- 🟢 Classificació manual feta abans del disseny, amb categories que **ixen del material real**. Cada categoria té atenció i urgència definides amb criteri d'empresa. Els patrons triats són fiables i es justifica per què (i es reconeix on un patró pot fallar).
- 🔵 Anàlisi feta i categories raonables, però algun patró és fràgil sense que es reconega, o la urgència s'assigna sense criteri explícit.
- 🟡 S'ha saltat l'anàlisi: es passa directament a fer filtres i les categories són genèriques.
- 🔴 No hi ha anàlisi ni criteri: filtres improvisats.

### RA8.f) Opcions de gestió utilitzades — 60 %

- 🟢 Sis filtres o més funcionant, amb tots els casos obligatoris coberts, documentats amb condicions i accions exactes. **L'ordre està justificat** i s'explica correctament què passaria si canviara. Estructura de carpetes/etiquetes coherent amb l'anàlisi. Plantilles i absència completes. Evidència abans/després real, incloent-hi els errors trobats.
- 🔵 Filtres funcionant i ben documentats, però falta algun cas obligatori o la justificació de l'ordre és superficial.
- 🟡 Filtres que funcionen però simples (una condició, una acció), o estructura sense relació amb l'anàlisi, o sense evidència de funcionament.
- 🔴 Filtres que no s'han provat, o que esborren automàticament.

!!! danger "Cap filtre que esborre"
    Un filtre amb acció d'esborrar automàtic baixa el CA (f) a 🔴, encara que tota la resta estiga bé.

    No és una regla d'aula: és que un sistema que fa desaparéixer correu legítim sense deixar rastre és **pitjor que no tindre cap filtre**, perquè el problema és invisible fins que ja ha costat un client.
