# T2 · La safata sota control

<span class="ca">CA b</span> <span class="ca">CA e</span> <span class="ca">CA f</span>

Una safata d'entrada amb 4.000 missatges sense llegir no és un problema de volum. És un problema de **decisions no preses**.

## El principi

Cada correu que entra només pot acabar en un de quatre llocs:

| Si... | Va a... |
| --- | --- |
| Es respon en menys de 2 minuts | **Respondre ara** i arxivar |
| Requereix faena teua | **Tasca** (amb data) i arxivar |
| Ha de fer-lo un altre | **Delegar** i arxivar amb seguiment |
| Només és informació | **Arxivar** directament |
| No serveix per a res | **Esborrar** |

La safata d'entrada és una **bústia**, no un magatzem. El que ja ha estat decidit, ix.

## Carpetes i etiquetes

Dos models diferents, i confondre'ls genera desordre.

**Carpetes** — un missatge està en una i només una. Model tradicional (IMAP, Thunderbird, Outlook).

**Etiquetes** — un missatge pot tindre'n diverses. Model de Gmail i similars.

| | Carpetes | Etiquetes |
| --- | --- | --- |
| Pertinença | Exclusiva | Múltiple |
| "Pressupost de l'Ajuntament" | O a `Clients/Ajuntament` **o** a `Pressupostos` | Les dues alhora |
| Risc | Decidir on va cada cosa | Etiquetes que es multipliquen sense control |

!!! tip "Criteri per a triar l'estructura"
    L'estructura ha de respondre a **com busques**, no a com arriben les coses.

    Si quan busques un correu penses "el d'aquell client", organitza per client. Si penses "el pressupost d'allò", organitza per tipus de document. La majoria d'empreses xicotetes funcionen bé amb `Clients/<nom>` més unes poques etiquetes transversals com `Pendent` o `Facturat`.

    Estructures de cinc nivells d'anidament: senyal quasi segura que ningú les manté.

## Filtres i regles

<span class="ca">CA f</span> Un **filtre** és una regla que actua sola sobre els missatges que compleixen una condició.

**Estructura:** `SI <condicions> LLAVORS <accions>`

**Condicions habituals:** remitent, destinatari, assumpte que conté, cos que conté, té adjunt, mida, s'ha enviat a una adreça concreta.

**Accions habituals:** moure a carpeta, aplicar etiqueta, marcar com a llegit, marcar com a important, reenviar, respondre amb plantilla, esborrar.

### Tres regles que val la pena tindre sempre

1. **Correu d'un client → carpeta del client + etiqueta.** Estalvia el 80 % de la classificació manual.
2. **Notificacions automàtiques → fora de la safata.** Còpies de seguretat, alertes de sistema, butlletins. Es consulten quan toca, no interrompen.
3. **Va dirigit a mi o sóc en Cc?** Si estic en Cc, no és per a mi decidir. Etiqueta diferent, prioritat diferent.

### L'ordre importa

Els filtres s'apliquen **en ordre**. Si el primer mou un missatge i para, els següents no el veuen mai. Quan una regla "no funciona", el primer que es mira és si n'hi ha una anterior que l'està capturant.

!!! warning "Cap regla que esborre automàticament"
    Una regla que esborra es menja correus legítims tard o d'hora, i quan passa **no te'n adones**: el missatge no ha arribat mai i tu no saps que existia.

    Si una cosa realment molesta, mou-la a una carpeta i revisa-la de tant en tant. Esborrar automàticament és una decisió sense marxa arrere.

## Plantilles i respostes automàtiques

**Plantilles** — missatges preescrits per al que envies sovint (confirmació de rebuda d'una incidència, enviament d'un pressupost). Estalvien temps i, sobretot, garanteixen que no t'oblides d'una dada.

**Resposta automàtica d'absència** — activada quan no hi ets. Ha de dir tres coses: **fins quan**, **a qui escriure mentrestant** i **què fer si és urgent**. Una resposta que només diu "estic fora" no ajuda ningú.

**Signatura** — a l'empresa és la mateixa per a tothom, amb la variació del nom i el càrrec. Elements: nom, càrrec, empresa, telèfon, web, i l'avís legal si n'hi ha.

!!! danger "Signatures amb imatge"
    Un logo incrustat com a imatge sol arribar com a adjunt, bloquejat per defecte, o directament no es veu. I fa que cada correu pese més.

    En correspondència professional, una signatura de text ben maquetada funciona **sempre**. La imatge, només si hi ha bon motiu i s'ha provat.

## La llibreta d'adreces

<span class="ca">CA e</span> No és una llista de correus: és el registre de contactes de l'empresa.

**Què conté un contacte complet:** nom i cognoms, organització, càrrec, adreça de correu (pot tindre'n diverses), telèfon, notes.

**Llistes de distribució** — agrupacions per a enviar a diverses persones alhora. Compte: si la llista va al camp `To`, tots veuen les adreces dels altres. Per a comunicacions externes, **Bcc**.

**Importació i exportació** — el format d'intercanvi és **vCard** (`.vcf`). Saber exportar la llibreta és el que permet canviar de client de correu sense perdre-ho tot, i és el que et demanaran el dia que una empresa migre de sistema.

!!! note "Protecció de dades"
    Una llibreta d'adreces és un fitxer amb dades personals. Té implicacions reals de RGPD: no es comparteix fora de l'empresa, no s'usa per a fins diferents dels quals es va recollir, i les persones tenen dret a que se'ls esborren les dades.

    A esta situació treballem amb contactes inventats o de companys que hi consenten, i no s'exporta res fora de l'aula.

## 🤖 IA i correu

**Útil per a:** revisar el to d'un correu difícil abans d'enviar-lo, resumir un fil llarg, proposar un assumpte que informe millor, i traduir un missatge a un registre més formal.

**Especialment útil:** *"Llig este correu com si foreu el client enfadat que el rep. Com et sonaria?"* És un bon filtre abans d'enviar alguna cosa que has escrit calent.

**Inacceptable:** enganxar correspondència real de clients amb dades personals en una eina externa. Anonimitza abans, sempre.

## Comprova que ho tens

- [ ] Sé les quatre destinacions possibles d'un correu que entra.
- [ ] Sé la diferència entre carpeta i etiqueta amb un exemple.
- [ ] Sé crear un filtre amb dues condicions i dues accions.
- [ ] Sé per què l'ordre dels filtres importa.
- [ ] Sé per què no es fan regles que esborren.
- [ ] Sé què ha de dir una resposta d'absència.
- [ ] Sé exportar contactes a vCard i tornar a importar-los.
