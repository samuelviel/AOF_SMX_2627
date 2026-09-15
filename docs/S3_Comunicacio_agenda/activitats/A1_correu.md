# A1 · El correu de l'empresa

**Sessions 2 a 4** · lliurament: fitxa de configuració + 3 mostres de correspondència
**Avalua:** RA8 <span class="ca">a</span> <span class="ca">c</span> <span class="ca">e</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

Cadascú de vosaltres té el correu configurat com pot i signa com vol. Vull això arreglat i documentat.

I vull veure com escriviu: tres correus reals de la faena, dels que costa escriure.
</div>

## Part 1 · Configurar comptes

Configura **dos comptes** al client de correu (Thunderbird o l'equivalent):

1. Un compte amb **configuració manual**, sense assistent automàtic: servidors, ports i xifratge posats a mà. Ha de funcionar de veritat.
2. El mateix compte o un altre amb **un protocol diferent** (si el primer és IMAP, este POP3), només per a comparar el comportament.

**Documenta la comparació:** envia't un correu, llig-lo en un dispositiu, comprova què passa a l'altre. Explica què has observat i què implica per a una empresa.

!!! tip "Quin compte faig servir"
    Usa el correu del centre o un compte creat per a la faena del mòdul. **No configures el teu correu personal** en un equip compartit de l'aula: quan acabe la sessió, el teu compte continua allí.

    Si el proveïdor demana contrasenya d'aplicació, genera-la i **no la deixes escrita enlloc del lliurament**.

## Part 2 · Signatura i contactes

**La signatura corporativa**, acordada en equip: mateixa estructura per a tothom, variant nom i càrrec. En text, no en imatge, pels motius de [T2](../teoria/2_gestio.md). Si decidiu incloure logo, heu de justificar-ho i haver provat com arriba.

**La llibreta d'adreces:** <span class="ca">CA e</span>

- Mínim **8 contactes** amb fitxa completa (nom, organització, càrrec, correu, telèfon, notes)
- Una **llista de distribució** amb almenys 4 contactes
- Exporta la llibreta a **vCard**, esborra un contacte, torna a importar-la i comprova que ha tornat. Documenta-ho amb captures.

Els contactes són **inventats** (clients ficticis de l'empresa) o de companys que hi consenten expressament. Cap dada de familiars, amics o coneguts.

## Part 3 · Els tres correus

Redacta tres missatges. No són exercicis d'estil: són els tres tipus que més costen a la vida real.

### Correu 1 · Donar una mala notícia

> El manual que havíeu de lliurar dijous no estarà fins dilluns perquè el client va canviar un requisit a mitjan setmana.

Ha de contindre: la notícia **a dalt** (no soterrada al tercer paràgraf), el motiu sense excuses, **la nova data** i què fareu perquè no torne a passar.

### Correu 2 · Demanar informació que ja havies demanat

> És la tercera vegada que demanes al client les dades d'accés al servidor. Sense elles no pots avançar, i el retard acabarà sent culpa vostra.

Ha de mantindre la relació i alhora **deixar constància** que el bloqueig no és vostre. Sense retrets i sense passivitat.

### Correu 3 · Respondre a algú enfadat

> Un client escriu molest perquè un tècnic vostre li va dir que passaria dimarts i no va aparéixer.

Ha de reconéixer el fet, no discutir la percepció, i acabar amb **una acció concreta amb data**.

Cada correu porta: assumpte, destinataris amb `To`/`Cc` justificats, cos i signatura. I al costat, **dues línies explicant una decisió que has pres** en escriure'l (per què eixe assumpte, per què aquesta persona en Cc i no en To).

## La fitxa de configuració

| Apartat | Contingut |
| --- | --- |
| Comptes configurats | Protocol, servidors, ports, xifratge, mètode d'autenticació |
| Comparació IMAP/POP3 | Què has provat i què has observat |
| Signatura | La signatura i les decisions preses |
| Llibreta | Captures del contacte complet, la llista i l'exportació/importació |
| Anatomia | Capçaleres d'un dels teus correus enviats, amb **cinc** identificades i explicades <span class="ca">CA a</span> |

## Com s'avalua

### RA8.a) Elements d'un correu descrits — 25 %

- 🟢 Cinc capçaleres reals d'un correu propi, identificades i explicades amb **què implicarien si faltaren o fossen incorrectes**. Inclou almenys una de les que construeixen el fil.
- 🔵 Cinc capçaleres identificades i explicades correctament, però de manera descriptiva, sense implicacions.
- 🟡 Capçaleres copiades sense explicar, o explicació genèrica que no correspon al correu mostrat.
- 🔴 No s'han mirat les capçaleres reals.

### RA8.c) Comptes de correu configurats — 40 %

- 🟢 Dos comptes funcionant, **un configurat manualment** amb servidors, ports i xifratge documentats i justificats. La comparació entre protocols està feta amb una prova real i s'extrau una conclusió aplicable a l'empresa.
- 🔵 Comptes configurats i documentats, però la configuració manual s'ha fet amb ajuda de l'assistent, o la comparació és teòrica.
- 🟡 Un sol compte, o configuració documentada sense ports/xifratge (no reproduïble).
- 🔴 No hi ha configuració pròpia.

### RA8.e) Llibreta d'adreces operada — 35 %

- 🟢 Vuit contactes amb fitxa completa, llista de distribució funcional, cicle d'exportació-esborrat-importació provat i documentat amb evidència. S'explica quan s'usa `Bcc` amb una llista i per què.
- 🔵 Llibreta i llista correctes, exportació feta però sense provar la importació de tornada.
- 🟡 Contactes amb fitxa incompleta, o sense llista de distribució, o sense exportació.
- 🔴 No hi ha llibreta pròpia.

!!! info "Els tres correus"
    No tenen pes propi: **limiten el nivell**. Un lliurament tècnicament complet amb tres correus mal escrits (la mala notícia soterrada, el retret al client, la resposta defensiva) no arriba a nivell client en cap CA.

    L'encàrrec era que el correu de l'empresa funcionara. Els servidors són la meitat fàcil.
