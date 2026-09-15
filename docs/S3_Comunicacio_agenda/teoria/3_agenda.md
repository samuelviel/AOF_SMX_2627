# T3 · Agenda i calendari

<span class="ca">CA b</span> <span class="ca">CA d</span> <span class="ca">CA g</span>

L'agenda d'una empresa no és la teua agenda personal amb més gent dins. És una eina de **coordinació**: serveix perquè els altres puguen prendre decisions sense preguntar-te.

## Els tipus d'entrada

| Tipus | Què és | Exemple |
| --- | --- | --- |
| **Esdeveniment** | Té hora d'inici i fi | Visita a client, 10:00-11:30 |
| **Esdeveniment de tot el dia** | Ocupa el dia sense hora | Formació, festiu |
| **Tasca** | Té venciment, no franja | Enviar pressupost abans del 20 |
| **Recordatori** | Avís puntual | Renovar el domini |

Confondre tasca amb esdeveniment és un error que es paga: bloqueges dues hores d'agenda per a una cosa que pots fer en qualsevol moment, i els companys ho veuen com a ocupat.

## Què fa que un esdeveniment servisca

Un esdeveniment que diu només "Reunió" a les 10:00 obliga a preguntar. Els camps que eviten preguntes:

- **Títol que identifica:** `Visita Ajuntament — revisió equips planta baixa`
- **Ubicació:** adreça real o enllaç de videotrucada
- **Descripció:** ordre del dia, què cal portar, contacte al lloc
- **Convidats:** amb el seu estat de resposta
- **Recordatori:** amb prou antelació per a fer alguna cosa. Un avís 5 minuts abans d'una visita a 20 km no serveix.
- **Disponibilitat:** ocupat o lliure. Un curs en línia opcional no hauria de marcar-te com a ocupat.

## Recurrència

Les entrades que es repeteixen es creen una vegada amb la seua regla: diària, setmanal en dies concrets, mensual per data o per posició ("el primer dilluns de cada mes"), anual.

!!! warning "Editar una recurrent"
    Sempre et preguntarà: **només esta ocurrència**, **esta i les següents** o **totes**.

    Triar "totes" quan volies canviar una sola vegada és una de les maneres més ràpides de desordenar el calendari d'un equip sencer. I com que el canvi es propaga als convidats, se n'assabenta tothom.

## Compartir el calendari

Ací és on el calendari passa a ser una eina d'empresa.

**Nivells de permís**, de menys a més:

| Nivell | Qui el veu així |
| --- | --- |
| Només disponibilitat (lliure/ocupat) | Persones externes que necessiten quedar amb tu |
| Lectura de detalls | Companys de l'equip |
| Escriptura | Qui pot crear-te entrades |
| Gestió | Qui administra en nom teu |

**El nivell de disponibilitat és el que resol el 90 % dels problemes de coordinació.** Permet que algú veja que dimarts de 10 a 12 estàs ocupat sense veure amb qui ni per què. És suficient per a proposar una hora, i respecta la privacitat.

### Calendaris separats

Una bona pràctica: diversos calendaris superposats, cadascun amb els seus permisos i el seu color.

- `Equip` — visites, reunions, terminis compartits
- `Personal` — el teu, no compartit o compartit només com a disponibilitat
- `Terminis` — venciments de lliuraments i contractes
- `Guàrdies` — qui està de torn a la [mesa d'ajuda](../../recursos/mesa_ajuda.md) esta setmana

## Sincronització amb dispositius

<span class="ca">CA d</span> El calendari ha d'estar al lloc on el mires, i normalment eixe lloc és el mòbil.

**Els protocols:**

- **CalDAV** — estàndard obert per a calendaris. El fan servir Nextcloud, Radicale, iCloud i molts altres.
- **CardDAV** — el mateix per a contactes.
- **Exchange ActiveSync** — el de l'ecosistema Microsoft.
- **ICS (iCalendar)** — format de fitxer `.ics`. Pot ser una **subscripció** (URL que s'actualitza sola, normalment de només lectura) o una **exportació** puntual.

!!! tip "Subscripció ≠ compte"
    És una confusió habitual. Si afiges un calendari per URL `.ics`, estàs **subscrit**: el veus, però normalment no hi pots escriure ni es sincronitza en temps real.

    Si el que vols és crear i editar entrades des del mòbil, cal configurar el **compte** (CalDAV o l'equivalent del proveïdor), no una subscripció.

**Símptomes típics de sincronització que et trobaràs:**

| Símptoma | Causa habitual |
| --- | --- |
| Els canvis del mòbil no apareixen a l'ordinador | Calendari local del dispositiu, no el del compte |
| Els esdeveniments apareixen amb hores desplaçades | **Zona horària** mal configurada en un dels dos |
| Duplicats de tot | Dos comptes configurats amb el mateix calendari |
| Es veu però no es pot editar | Subscripció de només lectura |

### Zones horàries

Un esdeveniment guarda hora **i** zona. Si el teu dispositiu creu que està en una altra zona, els esdeveniments es mouen.

Amb el canvi d'hora d'octubre i març açò es fa visible: esdeveniments recurrents creats abans del canvi que apareixen una hora desplaçats. Amb un client internacional, deixa de ser una curiositat i passa a ser una reunió perduda.

## El protocol d'ús de l'equip

Una eina compartida sense normes acordades acaba com la safata d'entrada de tothom. El vostre protocol, que escriureu a [A3](../activitats/A3_agenda.md), hauria de respondre:

1. Què va al calendari d'equip i què no
2. Com es nomenen les entrades (format del títol)
3. Amb quanta antelació es convoca una reunió
4. Què vol dir que algú aparega com a ocupat
5. Qui pot escriure al calendari d'altres
6. Què es fa quan hi ha un conflicte d'horari

## 🤖 IA i agenda

**Útil:** convertir text desestructurat en entrades. *"D'este correu, extrau els compromisos amb data i dona'm títol, data, hora i durada de cadascun."* És una de les tasques on estalvia més temps real.

**Compte:** amb dates relatives. "El pròxim dimarts" depén de quan es va escriure el text, i els models s'equivoquen amb això sovint. **Verifica sempre les dates que et done.**

## Comprova que ho tens

- [ ] Sé quan una cosa és tasca i quan és esdeveniment.
- [ ] Sé crear una recurrència i modificar-ne una sola ocurrència.
- [ ] Sé els nivells de permís de compartició i quin usar amb algú extern.
- [ ] Sé la diferència entre subscriure's a un `.ics` i configurar un compte CalDAV.
- [ ] Sé diagnosticar un esdeveniment que apareix amb l'hora canviada.
- [ ] Sé exportar un calendari a `.ics`.
