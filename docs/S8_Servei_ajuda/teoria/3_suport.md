# T3 · Tècniques de suport

**RA9 complet**

Este és l'últim contingut teòric del curs, i tanca el que has estat practicant des de setembre a la [mesa d'ajuda](../../recursos/mesa_ajuda.md).

## Què és donar suport

No és arreglar l'ordinador d'algú. És **fer que eixa persona puga treballar**, hui i la pròxima vegada.

La diferència es veu en una pregunta: després de la teua intervenció, si el problema torna, l'usuari el sabrà resoldre?

## Les tècniques d'assessorament

<span class="ca">CA d</span>

### Escoltar primer

L'usuari descriu **símptomes**, no causes. I sovint els descriu malament, perquè no té el vocabulari.

*"El programa s'ha trencat"* pot voler dir sis coses diferents. Les preguntes que les separen:

- *Què esperaves que passara i què ha passat?*
- *Quan va funcionar bé per última vegada?*
- *Què has fet just abans?*
- *Passa sempre o de vegades?*

!!! warning "La resposta que sempre rebràs"
    *"Jo no he tocat res."*

    No és mentida: és que la persona no sap què compta com a "tocar alguna cosa". Va acceptar una actualització, va tancar una finestra emergent, va obrir un adjunt.

    Reformula: *"No et preocupes, no busque culpables. És per a saber per on mirar: recordes alguna finestra que t'haja aparegut estos dies?"*

### No toques el teclat

La regla de la [mesa d'ajuda](../../recursos/mesa_ajuda.md), i la més difícil de complir.

Si li ho fas tu, has resolt un tiquet. Si li ho expliques, has resolt tots els tiquets futurs d'eixe problema.

**Excepció legítima:** quan hi ha urgència real i el temps és crític. Llavors ho fas tu, ho documentes, i **després** li ensenyes amb calma.

### Adaptar el llenguatge

| No digues | Digues |
| --- | --- |
| "Executa el binari" | "Obri el programa" |
| "Està al directori arrel" | "Està a la primera carpeta, on comença tot" |
| "Fes un `refresh` de la consulta" | "Torna a obrir la llista perquè s'actualitze" |

**I no ho digues amb condescendència.** La persona que tens davant probablement sap fer coses que tu no saps fer.

### Tancar bé

- Comprova que funciona **amb l'usuari mirant**
- Explica què passava, en una frase
- Digues què fer si torna a passar
- Registra el tiquet

## Guies visuals

<span class="ca">CA a</span> Una **guia visual** és una pàgina que resol les tasques més freqüents d'un cop d'ull. No és un manual: és una xuleta.

| | Manual | Guia visual |
| --- | --- | --- |
| Extensió | 10-40 pàgines | **1 pàgina** |
| Ús | Es llig una vegada | Es penja a la paret |
| Contingut | Tot | **Només el que es fa cada dia** |
| Format | Text amb captures | Sobretot visual |

**Com es fa una bona:**

1. **Tria per freqüència, no per importància.** Les 3-5 tasques que es fan cada dia
2. **Una columna per tasca**, passos numerats
3. **Captures xicotetes i retallades** al mínim reconeixible
4. **Sense frases senceres.** "Clic a **Clients**" no "A continuació faràs clic al botó Clients"
5. Que **funcione en blanc i negre**, perquè s'imprimirà així

!!! tip "La prova de la guia visual"
    Imprimeix-la, penja-la a un metre i mig i mira-la. Si has d'acostar-te per a llegir-la, les captures són massa xicotetes o hi ha massa text.

## Informes d'incidències

<span class="ca">CA e</span> El format de set camps de [S1/T4](../../S1_Posada_marxa/teoria/4_documentar.md), que has estat usant tot el curs.

El que afegim ací és el **nivell agregat**: quan tens 40 tiquets, la informació ja no està en cap d'ells. Està en el **patró**.

| Anàlisi | Què revela |
| --- | --- |
| Incidències per tipus | On està el problema real |
| Incidències per usuari | Qui necessita formació |
| Temps mitjà de resolució | Si el servei funciona |
| **Incidències repetides** | **Què s'ha de documentar o arreglar d'arrel** |

!!! quote "El salt professional"
    Si sis persones diferents han tingut el mateix problema, **el problema no és de les persones**.

    O falta documentació, o l'eina està mal configurada, o el procés està mal dissenyat. Detectar això és el que converteix un servei de suport en una millora real.

## Els recursos per a resoldre

<span class="ca">CA g</span> Quan no ho saps —i passarà sovint—, l'ordre importa:

1. **Documentació oficial** del fabricant
2. **Ajuda integrada** de l'aplicació
3. **Base de coneixement pròpia** (els tiquets anteriors: per això es documenten)
4. **Comunitats** i fòrums especialitzats
5. **IA**, per a generar hipòtesis (vegeu més avall)
6. **Escalar** a algú amb més coneixement

**Buscar bé:** el missatge d'error **exacte** entre cometes, més el nom i la versió del programa. Buscar "no funciona LibreOffice" no dona res útil.

**Escalar bé:** amb el tiquet emplenat, dient què has provat i què has descartat. Escalar no és rendir-se; escalar malament sí.

## Salvaguarda i recuperació

<span class="ca">CA f</span> L'última competència del mòdul, i la que més diners estalvia.

### La regla 3-2-1

- **3** còpies de les dades
- **2** suports diferents
- **1** fora de l'edifici

### Tipus de còpia

| Tipus | Copia | Restauració |
| --- | --- | --- |
| **Completa** | Tot | Ràpida: una sola còpia |
| **Incremental** | El que ha canviat des de l'última còpia (de qualsevol tipus) | Lenta: cal la completa + totes les incrementals |
| **Diferencial** | El que ha canviat des de l'última completa | Intermèdia: completa + l'última diferencial |

!!! danger "La còpia que no s'ha provat no existeix"
    És la lliçó més cara del sector i sempre s'aprén el mateix dia: el dia que cal restaurar.

    Motius reals pels quals una còpia falla quan la necessites: el suport estava ple i portava mesos sense copiar res, el fitxer estava corrupte, ningú sabia la contrasenya del xifratge, o el procediment de restauració no existia i es va improvisar malament.

    **Una còpia de seguretat sense una restauració provada és un tros d'esperança.**

### El procediment mínim

Qualsevol client ha de tindre escrit:

1. **Què** es copia (i què no)
2. **Cada quant**
3. **On** van les còpies
4. **Quant de temps** es conserven
5. **Com es restaura** — pas a pas
6. **Quan es va provar** l'última restauració

## 🤖 IA en suport

**Bon ús:** generar hipòtesis a partir de símptomes, traduir un missatge d'error críptic, redactar una explicació per a un usuari no tècnic.

**Ús excel·lent:** *"Explica-li això a una persona de 60 anys que mai ha usat una base de dades, sense sigles."* És, potser, la millor aplicació de la IA en esta professió.

**Compte:** no apliques mai una ordre de sistema que no entens. I no enganxes dades reals de clients en cap eina externa.

## Comprova que ho tens

- [ ] Sé les quatre preguntes d'entrevista i com reformular el "jo no he tocat res".
- [ ] Sé per què no es toca el teclat de l'usuari i quina és l'excepció.
- [ ] Sé la diferència entre un manual i una guia visual.
- [ ] Sé quines quatre anàlisis es fan sobre un conjunt de tiquets.
- [ ] Sé l'ordre de recursos per a resoldre una incidència.
- [ ] Sé la regla 3-2-1 i els tres tipus de còpia.
- [ ] Sé per què una còpia sense restauració provada no compta.
