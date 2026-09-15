# A3 · La macro que estalvia hores

**Sessions 14 i 15** · lliurament: fitxer amb la macro + fitxa d'automatització
**Avalua:** RA2 <span class="ca">e</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Coordinació · Per a: Equip tècnic</p>

He estat mirant com treballeu i hi ha coses que repetiu contínuament: donar format a fragments de codi, muntar la taula de control de versions, posar la capçalera del parte d'incidència...

Trieu **una** d'eixes tasques i automatitzeu-la. Però abans de posar-vos-hi, digueu-me **quant de temps estalvia**. No vull que passeu una vesprada automatitzant una cosa que es fa en deu segons dues vegades l'any.
</div>

## Part 1 · Triar amb criteri

Este és el pas que val nota, no el codi.

Omple esta taula **abans** de programar res:

| Pregunta | La teua resposta |
| --- | --- |
| Quina tasca? | |
| Quant es tarda a fer-la a mà? | |
| Quantes vegades a la setmana es fa? | |
| Temps perdut a l'any (setmanes lectives: 35) | |
| Quant tardaré a automatitzar-la? | |
| **Compensa?** | |
| Quin risc té que falle? | |

!!! tip "El càlcul importa més que el resultat"
    Si el càlcul et diu que **no** compensa, i ho argumentes bé, pots proposar-me una altra tasca. El que no s'accepta és fer la macro sense haver fet el càlcul.

    A l'empresa, esta decisió és la diferència entre un tècnic que millora processos i un que es distrau amb joguets.

### Tasques suggerides

Si no se t'acut cap, estes són reals i surten del que ja has fet:

- Aplicar l'estil de caràcter "Codi" a la selecció i fixar-li l'idioma (la de [T5](../teoria/5_macros.md), però ampliada)
- Inserir la taula de control de versions amb la fila de hui ja posada
- Inserir l'esquelet d'un parte d'incidència amb els set camps de [S1/T4](../../S1_Posada_marxa/teoria/4_documentar.md)
- Netejar tot el format directe del document i actualitzar tots els camps (la rutina de "preparar per a lliurar")
- Exportar a PDF amb el nom de fitxer segons la convenció del [portafoli](../../recursos/portafoli.md)

## Part 2 · Construir-la

El mètode de [T5](../teoria/5_macros.md): **grava, obri el codi, neteja'l**.

Requisits de la macro:

- [ ] Funciona de veritat, provada amb almenys **tres casos diferents**
- [ ] Té **comprovació prèvia**: si no es dona la condició necessària (no hi ha selecció, l'estil no existeix...), avisa amb un missatge útil i ix
- [ ] Està **comentada**: què fa cada bloc
- [ ] Té un nom que diu què fa
- [ ] Saps on està guardada i per què hi està (a les teues macros o dins del document)

### Els tres casos de prova

Documenta'ls:

| Cas | Entrada | Resultat esperat | Resultat real |
| --- | --- | --- | --- |
| Normal | | | |
| Límit | | | |
| Error | | | |

El cas d'**error** és el que separa una macro d'aficionat d'una de professional: què passa quan l'usuari l'executa en una situació per a la qual no està pensada. Si peta amb un missatge incomprensible de Basic, encara no està acabada.

## Part 3 · La fitxa d'automatització

Una pàgina:

1. **Tasca automatitzada** i el càlcul de la part 1
2. **Codi** de la macro, amb els comentaris
3. **Taula de casos de prova**
4. **On està guardada** i com s'executa (drecera, botó, menú)
5. **Limitacions conegudes** — què no fa, quan no s'ha d'usar
6. **Portabilitat:** funcionaria en un altre equip? I a Word? I a M365 Online?
7. [Nota d'ús d'IA](../../recursos/ia.md)

!!! warning "El punt 6 no és decoratiu"
    Si la teua macro depén d'un estil que només existeix a la teua plantilla, no és portable sense la plantilla. Si és VBA, no funciona a LibreOffice. Si l'empresa treballa en M365 Online, no s'executa.

    Saber **què assumeix la teua solució** és competència professional. Una solució que funciona només a la teua màquina i no ho saps és una bomba de rellotgeria.

## Com s'avalua

### RA2.e) Macros creades i utilitzades — 100 %

- 🟢 Macro funcional i **robusta** (comprova abans d'actuar, falla amb gràcia), comentada, amb els tres casos de prova documentats i el cas d'error resolt. El càlcul de justificació és real i honest. L'apartat de portabilitat identifica correctament les dependències. La defenses línia per línia.
- 🔵 Macro funcional i documentada, però sense gestió del cas d'error, o amb el càlcul de justificació fet per damunt, o amb la portabilitat analitzada de manera superficial.
- 🟡 La macro funciona només en el cas ideal i peta o fa coses estranyes fora d'ell; o és una gravació literal enganxada sense netejar ni comentar; o falta el càlcul de justificació.
- 🔴 No funciona, o no és teua (codi que no pots explicar).

!!! quote "Punt de comprensió"
    Te'n triaré **tres línies** i em diràs què fan i què passaria si les llevares.

    Si has gravat la macro, l'has oberta i l'has netejada com diu el mètode, açò són tres minuts. Si has enganxat codi d'algun lloc sense mirar-lo, es notarà immediatament.
