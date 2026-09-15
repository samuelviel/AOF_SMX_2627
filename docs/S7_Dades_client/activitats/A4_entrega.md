# A4 · L'entrega al client

**Sessions 16 i 17** · lliurament: `.odb` complet + manual d'usuari breu
**Avalua:** RA4 <span class="ca">e</span> <span class="ca">f</span> <span class="ca">h</span> · reforça RA9 <span class="ca">a</span> <span class="ca">c</span> <span class="ca">f</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Gestoria Bellver · Per a: la vostra empresa</p>

Les consultes estan molt bé, però hi ha un problema: les hem d'obrir nosaltres i eixa pantalla amb taules ens fa por.

Necessitem **pantalles**. Que la Rosa òbriga el programa, veja un botó que diga "Clients" i puga treballar.

I els llistats que ens heu ensenyat, els necessitem **en paper**, amb el seu logotip i tot.
</div>

## Part 1 · Els formularis

<span class="ca">CA e</span> Mínim **tres formularis**:

| Formulari | Requisit |
| --- | --- |
| **Clients** amb subformulari d'expedients | Sincronitzat: en canviar de client, canvia la llista |
| **Alta d'expedient** | Amb quadre de llista per a triar client i tipus |
| **Menú principal** | Botons cap a la resta de formularis i informes |

Requisits d'usabilitat, per a la Rosa:

- [ ] Cap identificador numèric visible: quadres de llista pertot
- [ ] **Etiquetes en llenguatge del client**, no noms de camp
- [ ] Ordre de tabulació lògic
- [ ] Camps obligatoris marcats visualment
- [ ] Valors per defecte on tinga sentit
- [ ] Text d'ajuda als camps que ho necessiten
- [ ] Format de data i de moneda aplicats

!!! tip "La prova de la Rosa"
    A la sessió 17, un company que no ha vist la teua base de dades ha de fer tres tasques **sense que li digues res**: donar d'alta un client, registrar-li un expedient i trobar tots els expedients d'un client existent.

    Cronometra-ho, apunta on dubta i **arregla-ho després**. Va al lliurament.

## Part 2 · Els informes

<span class="ca">CA f</span> Mínim **dos informes**, tots dos basats en consultes (no en taules):

1. **Llistat d'expedients per client**, agrupat, amb subtotals per client i total general
2. **Informe de facturació per període**, basat en una consulta amb paràmetre

Requisits:

- [ ] Capçalera amb el logotip i les dades de l'empresa, coherent amb la [plantilla corporativa](../../S2_Identitat_documental/activitats/A1_plantilla.md)
- [ ] Peu amb numeració de pàgina i data de generació
- [ ] **Informes dinàmics**, no estàtics
- [ ] Agrupació i totals funcionant
- [ ] Exportats a PDF com a mostra

## Part 3 · Una macro

<span class="ca">CA h</span> Una macro assignada a un botó o a un esdeveniment, amb els criteris de sempre: comprovació prèvia, informe de resultat, comentada, tres casos de prova.

Opcions raonables: obrir el formulari d'alta amb valors per defecte, llançar un informe amb els paràmetres del formulari actual, o fer una còpia de seguretat del fitxer en tancar.

I el **càlcul de justificació**: per què esta macro i no una altra.

## Part 4 · El manual i el traspàs

Un manual breu (4-6 pàgines) amb la plantilla corporativa, amb els criteris de [S2/T4](../../S2_Identitat_documental/teoria/4_gran_volum.md): una acció per pas, captures anotades, sense sigles.

Ha de cobrir: donar d'alta un client, registrar un expedient, buscar informació i generar un informe.

I dos apartats més, que són els que fan que l'entrega siga professional:

**Còpies de seguretat** <span class="ca">RA9 f</span> — el fitxer `.odb` conté **tota** la base de dades. Explica al client: cada quant copiar-lo, on, com comprovar que la còpia serveix i com restaurar-la. Amb una prova real de restauració documentada.

**Protecció de dades** — esta base de dades conté dades personals de clients. Indica al client, sense fer d'assessor jurídic: qui hi ha de tindre accés, per què no s'envia el fitxer per correu sense xifrar, i què implica el dret de supressió quan hi ha integritat referencial pel mig (ací és on "esborrar" un client es complica, i és bo que ho sàpiguen).

## Com s'avalua

### RA4.e) Formularis creats — 35 %

- 🟢 Tres formularis funcionant, subformulari sincronitzat, cap identificador visible, etiquetes en llenguatge del client i tots els requisits d'usabilitat. **La prova de la Rosa s'ha fet, s'han registrat els problemes i s'han corregit.**
- 🔵 Formularis funcionals i usables, però algun detall d'usabilitat pendent o la prova feta sense corregir després.
- 🟡 Formularis que funcionen però mostren identificadors o noms de camp tècnics, o sense subformulari sincronitzat.
- 🔴 No hi ha formularis: s'espera que l'usuari treballe sobre les taules.

### RA4.f) Informes creats — 35 %

- 🟢 Dos informes dinàmics basats en consultes, amb agrupació i totals correctes, capçalera i peu corporatius coherents amb la identitat de l'empresa, i un d'ells amb paràmetre funcionant.
- 🔵 Informes correctes i ben formatats, però algun estàtic o sense totals de grup.
- 🟡 Informes basats directament en taules, o sense identitat corporativa.
- 🔴 No hi ha informes, o no es poden generar.

### RA4.h) Macros creades i utilitzades — 30 %

- 🟢 Macro funcional i robusta, assignada a un botó o esdeveniment, amb comprovació prèvia, informe de resultat, comentaris i tres casos de prova documentats. Càlcul de justificació fet.
- 🔵 Macro funcional i documentada, sense el cas d'error resolt o sense justificació.
- 🟡 Macro que només funciona en el cas ideal, o gravació sense netejar.
- 🔴 No funciona, o no la pots explicar.

!!! info "El manual i les còpies limiten el nivell"
    Un lliurament tècnicament impecable **sense manual usable ni procediment de còpies provat** no arriba a nivell client en cap CA.

    L'encàrrec no era fer una base de dades: era que la gestoria la puga usar i no perdre-la. Entregar un `.odb` perfecte que ningú sap usar ni sap salvar és no haver acabat la faena.
