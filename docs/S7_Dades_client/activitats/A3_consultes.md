# A3 · Preguntes que has de respondre

**Sessions 12 i 13** · lliurament: `.odb` amb consultes + informe de resultats
**Avalua:** RA4 <span class="ca">d</span> <span class="ca">g</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Gestoria Bellver · Per a: la vostra empresa</p>

Ara que les dades estan en ordre, ací van les preguntes que fins ara ens costaven un matí cadascuna. Volem poder-les respondre quan vulguem, sense demanar-vos res.
</div>

## Les consultes

<span class="ca">CA d</span> Mínim **10 consultes guardades**, amb nom descriptiu. Estes vuit són obligatòries:

| # | Pregunta del client | El que exercita |
| --- | --- | --- |
| 1 | Clients d'una població concreta, ordenats per nom | Criteri simple, ordenació |
| 2 | Expedients d'un trimestre concret | `BETWEEN` amb dates |
| 3 | Clients el nom dels quals comença per un text | `LIKE` |
| 4 | Expedients de més de X € **de tipus fiscal** | Dos criteris amb **I** |
| 5 | Clients d'Alzira **o** de Carcaixent | Criteri amb **O** |
| 6 | Cada client amb el **nombre** dels seus expedients i el **total** facturat | `JOIN` + agregació |
| 7 | **Clients sense cap expedient** | `LEFT JOIN` — el que la majoria falla |
| 8 | Poblacions que sumen més de X € facturats | `GROUP BY` + `HAVING` |

Les dues restants les proposes tu: **preguntes que una gestoria voldria fer de veritat**. Justifica per què les has triades.

!!! warning "La consulta 7 és la trampa"
    Amb `INNER JOIN` retorna zero files sempre, i sembla que funciona.

    Si el teu resultat és zero, no vol dir que tots els clients tinguen expedients: vol dir que has usat la combinació equivocada. Comprova-ho manualment abans de donar-la per bona.

### Consulta amb paràmetre

Almenys **dues** de les deu han de tindre paràmetre, de manera que servisquen per a qualsevol població o període sense duplicar la consulta.

## Documentació de cada consulta

| # | Nom | Pregunta que respon | Files retornades | Com has verificat el resultat |
| --- | --- | --- | --- | --- |

**La columna de verificació és obligatòria.** Una consulta que retorna un número no demostra res: has de saber que eixe número és el correcte.

Mètodes vàlids: comptar manualment sobre un subconjunt xicotet, contrastar amb una taula dinàmica del full original, comprovar que dues consultes relacionades quadren entre elles.

!!! danger "L'error silenciós de les bases de dades"
    Una consulta mal plantejada **no dona error**. Retorna files, i les retorna amb tota la seguretat del món.

    Si la consulta 6 t'ix amb 38 clients i la gestoria en té 42, no hi haurà cap avís. Simplement, quatre clients desapareixeran de tots els informes que facen a partir d'ara.

    Per això es verifica. Sempre.

## Cerca i filtratge directe

<span class="ca">CA g</span> Al marge de les consultes, demostra les eines de cerca directa amb captures:

- [ ] **Cerca de registre** per un valor concret
- [ ] **Filtre estàndard** amb tres condicions combinades
- [ ] **Autofiltre** sobre una selecció
- [ ] **Ordenació** per dos camps

I explica, en tres línies, **quan usaries un filtre i quan una consulta guardada**.

## L'informe de resultats

Dues pàgines per a la gestoria, amb la plantilla corporativa:

1. **Llista de les consultes disponibles**, amb què respon cadascuna, en llenguatge de gestoria
2. **Tres troballes** que hages descobert en executar-les i que el client no sabia — per exemple, clients inactius, una població amb molta més facturació del que semblava, expedients atípics
3. **Com executar una consulta amb paràmetre** (dues línies amb captura)

!!! tip "El punt 2 és el valor real que aportes"
    El client t'ha demanat consultes. El que et farà tornar a contractar és **dir-li una cosa que no sabia sobre el seu propi negoci**.

    La consulta 7 sol donar-ne una: clients que fa anys que no generen expedients i que ningú havia detectat.

## Com s'avalua

### RA4.d) Consultes creades — 60 %

- 🟢 Deu consultes o més, amb les vuit obligatòries correctes. La 7 usa `LEFT JOIN` i retorna resultat real. Dues amb paràmetre funcionant. Les dues pròpies estan justificades com a preguntes de negoci. **Totes verificades**, amb el mètode de verificació documentat.
- 🔵 Consultes completes i correctes, però alguna verificació absent o superficial, o les consultes pròpies són variacions trivials de les obligatòries.
- 🟡 Falta alguna consulta obligatòria, o la 7 està mal plantejada, o no hi ha consultes amb paràmetre, o no s'ha verificat cap resultat.
- 🔴 Consultes que retornen dades incorrectes sense detectar-ho.

### RA4.g) Cerca i filtratge — 40 %

- 🟢 Les quatre eines demostrades amb evidència sobre dades reals, i el criteri de quan usar filtre i quan consulta està clar i ben argumentat. L'informe al client identifica tres troballes reals i rellevants per al negoci.
- 🔵 Eines demostrades i criteri explicat, però les troballes són descriptives ("hi ha 42 clients") en lloc d'accionables.
- 🟡 Alguna eina sense demostrar, o l'informe només llista les consultes sense aportar cap lectura.
- 🔴 No hi ha evidència d'ús de les eines de filtratge.
