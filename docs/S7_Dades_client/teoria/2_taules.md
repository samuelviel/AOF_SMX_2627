# T2 · Taules i relacions

<span class="ca">CA b</span> <span class="ca">CA c</span>

## Crear la base de dades

A LibreOffice Base: `Fitxer → Nou → Base de dades`.

**Motor incrustat** (HSQLDB o Firebird) → tot viu dins d'un sol fitxer `.odb`. És el que usarem: simple i portàtil.

!!! warning "El fitxer .odb és tota la base de dades"
    Si es corromp o s'esborra, ho perds tot. **Còpia de seguretat abans de qualsevol canvi estructural.**

    I no el tingues obert en dos llocs alhora: el motor incrustat no està pensat per a accés concurrent.

## Tipus de camp

Triar bé el tipus no és una formalitat: determina què es pot fer amb la dada.

| Tipus | Per a què | Nota |
| --- | --- | --- |
| `INTEGER` | Números sencers, claus | |
| `DECIMAL(p,e)` | **Diners** | Mai `FLOAT` per a imports: arrossega errors d'arrodoniment |
| `VARCHAR(n)` | Text de longitud variable | El més usat |
| `DATE` / `TIME` / `TIMESTAMP` | Dates i hores | Mai text |
| `BOOLEAN` | Sí/no | |
| `MEMO` | Text llarg | Observacions |

!!! danger "Els tres errors clàssics de tipus"
    **Diners en `FLOAT`.** `0,1 + 0,2` no dona exactament `0,3` en coma flotant. Amb prou operacions, els totals no quadren. Usa `DECIMAL`.

    **Dates com a text.** No es poden ordenar cronològicament ni restar. `"03/04/2027"` s'ordena entre `"02/…"` i `"04/…"`, no per any.

    **Codis i telèfons com a número.** Perds els zeros davanters i, a més, no té cap sentit sumar telèfons. Són **text**.

## Restriccions

La base de dades ha d'impedir les dades incorrectes. Si confies en que l'usuari les escriga bé, algun dia no ho farà.

| Restricció | Què garanteix |
| --- | --- |
| **Clau primària** | Unicitat i no nul |
| **NOT NULL** | El camp és obligatori |
| **UNIQUE** | No es repeteix (NIF, codi) |
| **Clau aliena** | El valor existeix a la taula referenciada |
| **Valor per defecte** | Estalvia escriptura |

### Integritat referencial

És el mecanisme que impedeix que existisca un expedient d'un client que no existeix.

I defineix **què passa** quan esborres o modifiques el registre pare:

| Opció | Comportament en esborrar un client |
| --- | --- |
| **Restringir** | No deixa esborrar si té expedients. **El més segur** |
| **Cascada** | Esborra també tots els seus expedients. **Perillós** |
| **Posar a NULL** | Els expedients queden sense client |

!!! tip "Per defecte, restringir"
    "Cascada" sembla còmode fins al dia que algú esborra un client i desapareixen catorze anys d'expedients sense confirmació.

    En dades de negoci, la resposta correcta quasi sempre és **impedir l'esborrat** i, si de cas, marcar el registre com a inactiu en lloc d'esborrar-lo.

## Definir les relacions

`Eines → Relacions`. Arrossega la clau primària d'una taula sobre la clau aliena de l'altra i configura la integritat referencial.

**Comprova-ho:** intenta inserir un expedient amb un `id_client` inexistent. Si t'ho deixa, la relació no està aplicada.

## Inserir, modificar i esborrar

<span class="ca">CA c</span>

**Vista de dades de la taula** — per a proves i càrregues xicotetes. No és per a l'usuari final: eixe usarà [formularis](4_formularis.md).

**Ordre d'inserció:** primer les taules **sense** claus alienes (les de catàleg: poblacions, tipus), després les que en tenen. Si ho fas al revés, la integritat referencial et rebutjarà els registres.

**Esborrat lògic vs físic.** En dades de negoci, sovint no es vol esborrar: es marca com a inactiu amb un camp `actiu`. Conserva l'historial i evita el problema de la cascada.

## Importar les dades del client

És el pas que més sorpreses dona. El full de càlcul que t'han enviat està brut, i has de netejar-lo **abans** d'importar, amb les tècniques de [S4/T5](../../S4_Control_economic/teoria/5_macros.md).

El procés:

1. **Neteja al full de càlcul:** espais, majúscules, duplicats, formats de data
2. **Separa les entitats:** un full per taula, amb les columnes exactes de destí
3. **Genera els identificadors:** assigna `id_client` únic a cada client real
4. **Substitueix els textos per identificadors** a la taula de detall (funció de cerca de [S4/T2](../../S4_Control_economic/teoria/2_formules.md))
5. **Importa** copiant i enganxant el rang sobre la taula de Base
6. **Verifica el recompte**

!!! danger "El pas 3 és el difícil i és on està el treball real"
    Decidir que "Ferreteria Bellver SL", "Ferreteria Bellver, S.L." i "FERRETERIA BELLVER" **són el mateix client** no ho fa cap programa per tu.

    I sobretot: **la decisió l'ha de confirmar el client**, no tu. Dos clients amb noms semblants poden ser dues empreses diferents de la mateixa família. Fusionar-los per error és un problema greu, i és irreversible.

    A [A2](../activitats/A2_construccio.md) es demana un **informe de decisions de fusió** precisament per això.

## Comprova que ho tens

- [ ] Sé per què els diners van en `DECIMAL` i no en `FLOAT`.
- [ ] Sé per què els telèfons són text.
- [ ] Sé configurar la integritat referencial i per què "restringir" és la opció per defecte.
- [ ] Sé en quin ordre s'importen les taules i per què.
- [ ] Sé transformar un full pla en dues taules amb identificadors.
- [ ] Sé que les decisions de fusió de registres es consulten amb el client.
