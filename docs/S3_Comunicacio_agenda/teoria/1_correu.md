# T1 · Com funciona el correu de veritat

<span class="ca">CA a</span> <span class="ca">CA b</span>

Tothom sap enviar un correu. Molt poca gent sap què passa quan li dona a enviar, i per això molt poca gent sap arreglar-ho quan falla.

## El viatge d'un missatge

Quan escrius a `client@empresa.com` des del teu programa de correu:

1. El teu programa entrega el missatge al **servidor d'eixida** del teu proveïdor (protocol **SMTP**).
2. Eixe servidor busca qui gestiona el correu del domini de destí i li l'entrega.
3. El servidor de destí el desa a la bústia del destinatari.
4. El programa del destinatari **el recull** (protocol **IMAP** o **POP3**).

Fixa't que hi ha **dos protocols diferents**: un per a enviar i un altre per a rebre. Per això, quan configures un compte manualment, et demana dos servidors. I per això existeix el símptoma clàssic *"rep però no envia"*: és el servidor d'eixida el que està mal configurat, no el compte.

## IMAP o POP3: la decisió que la gent no sap que pren

| | **IMAP** | **POP3** |
| --- | --- | --- |
| On viuen els missatges | Al servidor | Es baixen a l'equip |
| Diversos dispositius | Tots veuen el mateix | Cadascú veu una cosa diferent |
| Carpetes | Se sincronitzen | Són locals |
| Si es trenca l'equip | No perds res | Ho perds tot |
| Espai al servidor | Consumeix quota | Es pot alliberar |

!!! tip "En una empresa, IMAP"
    Amb POP3, si el tècnic llig el correu al portàtil, eixe missatge desapareix del mòbil i ningú més el veu. En una empresa on la gent treballa des de diversos llocs, això és una font constant de problemes.

    POP3 encara té sentit en un cas: quota de servidor molt limitada i un únic equip que arxiva tot el correu localment.

## Ports i xifratge

Els correus viatgen per la xarxa. Sense xifratge, viatgen llegibles.

| Ús | Protocol | Port habitual |
| --- | --- | --- |
| Rebre xifrat | IMAP amb SSL/TLS | 993 |
| Rebre sense xifrar | IMAP | 143 |
| Enviar xifrat | SMTP amb SSL/TLS | 465 o 587 |
| Enviar sense xifrar | SMTP | 25 |

**Norma de l'empresa: sempre xifrat.** Si un proveïdor només ofereix connexió sense xifrar, el problema és el proveïdor.

## Requisits per a muntar-ho

<span class="ca">CA a</span>

Abans d'instal·lar un client de correu (Thunderbird, Outlook) o de configurar un webmail, necessites tindre per escrit:

- Adreça completa i contrasenya (o l'autenticació en dos passos configurada).
- Servidor entrant: nom, protocol, port, xifratge.
- Servidor eixint: nom, port, xifratge, si requereix autenticació.
- Espai de disc disponible si el compte és IMAP amb còpia local.
- Connexió a Internet estable durant la sincronització inicial, que pot ser llarga.

La majoria de proveïdors grans ho autoconfiguren en detectar el domini. Això està bé fins que t'enfrontes a un servidor propi d'un client, que és quan cal saber-ho.

## Tipus de comptes que et trobaràs

| Tipus | Exemple | Particularitat |
| --- | --- | --- |
| **Corporatiu al núvol** | Microsoft 365, Google Workspace | Autenticació moderna, no contrasenya simple |
| **Proveïdor gratuït** | Gmail, Outlook.com | Poden exigir contrasenya d'aplicació |
| **Servidor propi del client** | `mail.elseudomini.com` | Configuració manual, certificats de vegades caducats |
| **Educatiu** | El compte del centre | Polítiques i restriccions d'enviament |

!!! danger "Contrasenyes d'aplicació"
    Si un compte té verificació en dos passos, un client de correu d'escriptori sovint **no pot** usar la contrasenya normal: cal generar una **contrasenya d'aplicació** específica al panell de seguretat del compte.

    Quan algú et diga *"m'ha deixat de funcionar el correu al programa però al mòbil va bé"*, este és el primer lloc on mirar.

## Escriure un correu professional

La part tècnica és la fàcil. Açò és el que et jutjaran:

**L'assumpte.** Ha de permetre trobar el correu tres mesos després. `Consulta` és inútil. `Pressupost renovació aula informàtica — Centre de Majors` és útil.

**Per a, Cc i Cco.**

- **Per a**: qui ha de fer alguna cosa.
- **Cc**: qui s'ha d'assabentar però no ha de fer res.
- **Cco**: enviaments a molts destinataris que no s'han de conéixer entre ells. **Enviar a 40 clients amb les adreces a la vista és una fuga de dades personals**, i això té conseqüències legals reals.

**El cos.** Una idea per paràgraf. Si demanes alguna cosa, que es veja què demanes i per a quan. Si el correu té més de tres paràgrafs, potser calia una trucada.

**La signatura.** Nom, càrrec, empresa, telèfon, web. Sense imatges pesades ni frases de dubtosa utilitat.

!!! warning "Respondre a tots"
    Abans de prémer *Respon a tots*, mira qui és 'tots'. La quantitat de correu inútil que genera este botó en una empresa mitjana és difícil d'exagerar.
