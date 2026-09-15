# T3 · Consultes

<span class="ca">CA d</span> <span class="ca">CA g</span>

Una base de dades sense consultes és un magatzem tancat. Les consultes són **les preguntes** que li fas.

## Què és una consulta

Una pregunta guardada. No conté dades: conté la **definició** de com obtindre-les. Cada vegada que l'obris s'executa sobre les dades actuals, així que sempre està al dia.

Això és radicalment diferent d'un full de càlcul, on el resultat es congela quan el copies.

## L'assistent i la vista de disseny

<span class="ca">CA d</span> Base ofereix les dues vies, i les dues formen part del CA:

- **Assistent** — guiat, ràpid, limitat. Bo per a començar.
- **Vista de disseny** — control total. On acabaràs treballant.
- **Vista SQL** — el llenguatge real de davall. Val la pena mirar-la encara que no la uses.

!!! tip "El truc per a aprendre SQL sense estudiar-lo"
    Fes la consulta amb l'assistent, i després canvia a vista SQL i mira el que ha generat.

    En quatre o cinc consultes veuràs el patró `SELECT ... FROM ... WHERE ... ORDER BY` i ja el sabràs llegir. Això et servirà a tots els mòduls que venen després.

## Les parts d'una consulta

```sql
SELECT   nom, poblacio          -- quins camps vull
FROM     CLIENTS                -- d'on
WHERE    poblacio = 'Alzira'    -- quines files
ORDER BY nom                    -- en quin ordre
```

A la vista de disseny, cada columna té: camp, taula d'origen, si es mostra, ordenació i criteri.

## Criteris

| Operador | Exemple | Troba |
| --- | --- | --- |
| `=` `<>` `>` `<` | `> 500` | Imports majors de 500 |
| `LIKE` | `LIKE 'Ferre%'` | Text que comença per "Ferre" |
| `BETWEEN` | `BETWEEN #2027-01-01# AND #2027-03-31#` | Primer trimestre |
| `IN` | `IN ('Alzira','Carcaixent')` | Qualsevol de la llista |
| `IS NULL` | | Camps buits |

**Comodins amb `LIKE`:** `%` per a qualsevol seqüència, `_` per a un sol caràcter.

### I i O

A la vista de disseny, la posició indica l'operador:

- Criteris **a la mateixa fila** → es combinen amb **I** (s'han de complir tots)
- Criteris **en files diferents** → es combinen amb **O**

És la font d'error més habitual en consultes de disseny, i no dona cap avís: simplement retorna un resultat que no és el que volies.

!!! warning "El `NULL` no és zero ni cadena buida"
    `NULL` significa "no se sap". I per això `NULL = NULL` **no és cert**: dues coses desconegudes no són necessàriament iguals.

    Conseqüència pràctica: una consulta amb criteri `<> 'Alzira'` **no retorna** els registres amb població `NULL`. Si els vols, has d'afegir `OR poblacio IS NULL`.

    Este comportament sorprén tothom la primera vegada i causa informes incomplets que ningú detecta.

## Consultes amb diverses taules

Ací és on la base de dades demostra per què val la pena.

Quan afigs dues taules relacionades a una consulta, es combinen pel camp de la relació:

```sql
SELECT   c.nom, e.data, e.import
FROM     CLIENTS c
         INNER JOIN EXPEDIENTS e ON c.id_client = e.id_client
WHERE    e.import > 400
```

**Tipus de combinació:**

| Tipus | Retorna |
| --- | --- |
| **INNER JOIN** | Només els registres que tenen parella a les dues taules |
| **LEFT JOIN** | Tots els de l'esquerra, tinguen parella o no |
| RIGHT JOIN | El simètric |

!!! tip "Quan necessites LEFT JOIN"
    *"Dona'm tots els clients amb el nombre d'expedients."*

    Amb `INNER JOIN`, els clients **sense cap expedient no apareixen**. Si el que vols és detectar-los precisament (clients inactius!), necessites `LEFT JOIN`.

    És una diferència que sembla tècnica i que canvia completament la resposta a una pregunta de negoci.

## Agregació

Resumir moltes files en una:

```sql
SELECT   c.poblacio, COUNT(*) AS nre, SUM(e.import) AS total
FROM     CLIENTS c INNER JOIN EXPEDIENTS e ON c.id_client = e.id_client
GROUP BY c.poblacio
HAVING   SUM(e.import) > 1000
ORDER BY total DESC
```

| Funció | Fa |
| --- | --- |
| `COUNT(*)` | Compta files |
| `SUM` / `AVG` | Suma / mitjana |
| `MAX` / `MIN` | Extrems |

**`WHERE` vs `HAVING`:** `WHERE` filtra **files abans** d'agrupar; `HAVING` filtra **grups després**. Si vols "expedients de més de 400 €", és `WHERE`. Si vols "poblacions que sumen més de 1000 €", és `HAVING`.

## Consultes amb paràmetres

En lloc de fixar el criteri, es demana en executar:

```sql
WHERE poblacio = :quina_poblacio
```

Una sola consulta serveix per a totes les poblacions. És el que permet fer **informes reutilitzables**, i el que voràs a [T4](4_formularis.md).

## Cercar i filtrar

<span class="ca">CA g</span> Al marge de les consultes guardades, Base ofereix eines directes sobre les taules i els formularis:

- **Cerca de registre** — busca un valor recorrent la taula
- **Filtre estàndard** — fins a tres condicions amb I/O
- **Autofiltre** — filtra pel valor de la cel·la seleccionada
- **Ordenació ràpida**

**Quan usar cada cosa:** filtre per a una consulta puntual que no repetiràs; **consulta guardada** per a una pregunta que tornaràs a fer. Si et trobes aplicant el mateix filtre cada dilluns, eixe filtre havia de ser una consulta.

## 🤖 IA i consultes

**Molt bon ús:** descriure l'estructura de les taules i la pregunta de negoci, i demanar-li la SQL. Encerta força amb consultes de dificultat mitjana.

**Imprescindible:** verificar el resultat amb un cas que sàpigues. Una consulta que retorna 47 files quan n'hauries d'esperar 52 no dona cap error — simplement està malament, i normalment per un `INNER JOIN` on calia un `LEFT JOIN`.

**Ús excel·lent:** *"Explica'm per què esta consulta meua retorna menys files de les que espere."* És un dels llocs on més ajuda de veritat.

## Comprova que ho tens

- [ ] Sé llegir una consulta SQL bàsica.
- [ ] Sé la diferència entre criteris a la mateixa fila i en files diferents.
- [ ] Sé per què `NULL` es comporta de manera especial.
- [ ] Sé quan cal `LEFT JOIN` en lloc d'`INNER JOIN`.
- [ ] Sé la diferència entre `WHERE` i `HAVING`.
- [ ] Sé fer una consulta amb paràmetre.
