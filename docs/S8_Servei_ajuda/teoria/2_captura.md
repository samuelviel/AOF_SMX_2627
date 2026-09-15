# T2 · Captura, gravació i edició

<span class="ca">CA c</span> <span class="ca">CA d</span> <span class="ca">CA e</span>

## El guió va primer

<span class="ca">CA e</span> El 80 % de la qualitat d'un videotutorial es decideix **abans de prémer gravar**.

Un tutorial improvisat dura el doble, té set "eh..." i acaba amb el presentador buscant un menú en directe.

### L'estructura

| Part | Durada | Contingut |
| --- | --- | --- |
| **Entrada** | 10-15 s | Què aprendràs i per a què serveix |
| **Context** | 15-20 s | On estem i què cal tindre preparat |
| **Desenvolupament** | El gros | Els passos, un a un |
| **Tancament** | 10-15 s | Resum i què fer si falla |

!!! danger "Els primers 10 segons"
    Si comences amb "Hola, sóc X, ací estem en un altre vídeo de...", ja has perdut la meitat de l'audiència.

    Comença pel problema: *"Si has d'enviar la llista de clients d'una població i no saps com, en tres minuts ho tindràs."*

### El guió a dues columnes

| Què es veu | Què es diu |
| --- | --- |
| Pantalla inicial de la base de dades | "Obrim la base de dades. Este és el menú principal." |
| Clic al botó Clients | "Fes clic a **Clients**. S'obri la fitxa." |

Escriure-ho així obliga a **sincronitzar** acció i narració, i detecta els passos que no havies pensat.

### Regles de contingut

- **Un tutorial, una tasca.** Cinc tasques són cinc vídeos.
- **3-5 minuts màxim.** Més enllà, ningú el completa.
- **Ritme lent en les accions.** La mà del que grava va molt més ràpida que l'ull del que mira.
- **Digues què hauria de passar** després de cada acció.

## La gravació

<span class="ca">CA d</span>

### Preparació de l'escenari

- [ ] **Resolució de pantalla fixada** i igual a la d'exportació
- [ ] Escriptori net: sense notificacions, sense noms personals, sense pestanyes del correu
- [ ] **Dades de prova, no reals**
- [ ] Mode "no molestar" activat
- [ ] Zoom de l'aplicació augmentat si el text és xicotet
- [ ] **Cursor visible i, si l'eina ho permet, ressaltat**
- [ ] Assaig complet abans de gravar

!!! warning "L'assaig no és opcional"
    Fes la tasca sencera una vegada amb el guió davant, sense gravar. Trobaràs sempre alguna cosa: un diàleg que no havies previst, un pas que falta, una finestra que tapa el que vols mostrar.

    Cinc minuts d'assaig estalvien tres preses.

### L'àudio

**L'àudio importa més que el vídeo.** La gent perdona una imatge regular; no perdona un so dolent.

- Micròfon **prop** (20-30 cm). El del portàtil, a mig metre, arreplega tota la sala
- Sala amb poc ressò: mobles i cortines ajuden més que qualsevol filtre
- **Prova de nivell** abans: ni saturat ni inaudible
- Apaga ventiladors i tanca finestres

**Locució separada o simultània?** Gravar la pantalla en silenci i posar la veu després dona millor resultat: pots repetir la narració sense repetir la captura, i el ritme de la pantalla no depén de si t'entrebanques.

### Eines

| Eina | Plataforma | Nota |
| --- | --- | --- |
| **OBS Studio** | Totes | Lliure, potent, l'estàndard |
| Gravador del sistema | Windows / GNOME | Suficient per a captures simples |
| **Kdenlive / Shotcut** | Totes | Edició, lliures |
| **Audacity** | Totes | Edició d'àudio |

## L'edició

<span class="ca">CA c</span>

**Importar** a la línia de temps. Comprova que el projecte està configurat amb la mateixa resolució i fps del material: si no, es reescala i perds nitidesa.

**Les operacions que necessites:**

1. **Retallar** entrades i eixides mortes
2. **Tallar** silencis i errors
3. **Accelerar** trams d'espera (una càrrega llarga a x4)
4. **Zoom** sobre la zona d'acció quan el detall és xicotet
5. **Text en pantalla** per a reforçar els passos clau
6. **Transicions simples** entre seccions, no entre talls

!!! tip "El zoom és el que separa un tutorial bo d'un mediocre"
    Una captura de 1920 px reproduïda en una finestra xicoteta fa que el botó del qual parles siga invisible.

    Ampliar la zona d'acció en els moments clau és, probablement, la millor inversió d'esforç en tota l'edició.

**Àudio:** normalitza el volum, redueix el soroll de fons amb moderació (massa reducció fa la veu metàl·lica) i deixa els silencis curts on l'espectador ha d'assimilar.

**Música de fons:** opcional, molt baixa, i **amb llicència verificada**. Igual que les imatges de [S5](../../S5_Imatge_empresa/index.md): una pista de YouTube no és lliure d'ús.

## L'exportació

<span class="ca">CA c</span> Els valors per a lliurar a un client:

| Paràmetre | Valor |
| --- | --- |
| Contenidor | MP4 |
| Còdec de vídeo | H.264 |
| Còdec d'àudio | AAC |
| Resolució | La de gravació |
| fps | El de gravació |
| Taxa de bits | 2-4 Mbps per a captura de pantalla |

**Comprova el resultat abans de lliurar:** obri'l en un reproductor diferent del que uses habitualment, i si pots, en un altre equip. És el mateix principi que la prova d'anada i tornada de [S2/A4](../../S2_Identitat_documental/activitats/A4_interoperabilitat.md).

## Comprova que ho tens

- [ ] Sé escriure un guió a dues columnes.
- [ ] Sé preparar l'escenari de gravació i per què cada punt importa.
- [ ] Sé per què l'àudio importa més que la imatge.
- [ ] Sé per què convé gravar la locució per separat.
- [ ] Sé usar el zoom sobre la zona d'acció.
- [ ] Sé els paràmetres d'exportació per a lliurar i com verificar-los.
