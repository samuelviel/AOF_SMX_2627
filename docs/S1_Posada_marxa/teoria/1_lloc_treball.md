# T1 · El teu lloc de treball

Esta primera teoria no avalua cap criteri. És la base sobre la qual va tot el curs, i saltar-se-la és la manera més ràpida de perdre faena i temps més endavant.

## Els fitxers existeixen en un lloc

Hi ha una pregunta que separa qui controla un ordinador de qui no: **on està este fitxer?**

Si la resposta és "a Descàrregues", "al escriptori" o "no ho sé, però el trobe buscant", tens un problema que encara no s'ha manifestat. Es manifestarà el dia que hages de lliurar quatre documents relacionats, o el dia que canvies d'equip.

Un fitxer viu en una **ruta**: una seqüència de carpetes des de l'arrel del sistema fins a ell.

=== "Linux"
    ```
    /home/samuel/AOF/S1_Posada_marxa/entregues/informe.odt
    ```
    L'arrel és `/`. La teua carpeta personal és `/home/usuari` (abreujada `~`).

=== "Windows"
    ```
    C:\Usuaris\samuel\AOF\S1_Posada_marxa\entregues\informe.odt
    ```
    L'arrel és una lletra d'unitat. La teua carpeta personal, `C:\Usuaris\usuari`.

Les diferències visibles (barra endavant o enrere, arrel única o per unitats) són menys importants que la idea de fons, que és idèntica: **estructura d'arbre, i cada fitxer en una branca concreta**.

## Extensions: què és de veritat este fitxer

L'extensió és el final del nom (`.odt`, `.pdf`, `.csv`). No és decoratiu: el sistema la fa servir per a decidir amb quin programa obri el fitxer.

!!! warning "Activa la visualització d'extensions ara"
    Per defecte, Windows les amaga. Això vol dir que `informe.pdf` pot ser en realitat `informe.pdf.exe` i tu no ho veuràs. És, literalment, un dels vectors d'infecció més usats.

    **Explorador → Visualització → Extensions de nom de fitxer.**

Les que veuràs este curs:

| Extensió | Què és | On apareix |
| --- | --- | --- |
| `.odt` `.ods` `.odp` | Formats oberts (OpenDocument) | LibreOffice, per defecte |
| `.docx` `.xlsx` `.pptx` | Formats de Microsoft Office | M365, intercanvi amb clients |
| `.ott` `.dotx` | **Plantilles** de document | [S2](../../S2_Identitat_documental/index.md) |
| `.pdf` | Document tancat, per a lliurar | Quasi totes les entregues |
| `.csv` | Dades en text pla separades per comes | [S4](../../S4_Control_economic/index.md), [S7](../../S7_Dades_client/index.md) |

## Noms de fitxer que no t'odiaran

Tres regles i una convenció.

1. **Sense espais ni accents** en noms que puguen acabar en un servidor o en una URL. `informe final.odt` es converteix en `informe%20final.odt` a mig camí i algun sistema s'ennuegarà.
2. **Dates en format `AAAA-MM-DD`.** `2026-10-08` s'ordena sol alfabèticament; `08-10-2026` no.
3. **Res de `final`, `final2`, `final_bo`, `FINAL_DEFINITIU`.** Numera: `v1`, `v2`, `v3`.

La convenció del curs, explicada a [El portafoli](../../recursos/portafoli.md):

```
S1_A1_InformeInstallacio_VielSamuel_v2.odt
```

## Còpies de seguretat, des de hui

El disc de l'aula no és teu i es pot esborrar en qualsevol moment.

Regla mínima: **dues còpies, en dos llocs diferents**. El núvol del centre més un pendrive, o un repositori privat més el teu portàtil. Tria hui quina serà la teua i mantín-la.

A [S8](../../S8_Servei_ajuda/index.md) vorem procediments de salvaguarda i recuperació de dades com a contingut avaluable. Eixe dia et preguntaré què has estat fent des de setembre.

## Els 10 minuts

Cada sessió comença amb 10 minuts de mecanografia a TypingClub. Des de hui.

La lògica és simple: escriure mirant el teclat costa entre dues i tres vegades més temps, i obliga a apartar la vista de la pantalla, que és on apareixen els errors. Multiplica eixa diferència pels documents que escriuràs este curs — i pels que escriuràs la resta de la teua vida laboral.

**Com fer-ho perquè servisca:**

- Posició de partida: dits esquerres a `ASDF`, dits drets a `JKLÑ`, polzes a l'espai.
- **Prioritza la precisió sobre la velocitat.** La velocitat arriba sola; els errors apresos no se'n van.
- No mires el teclat. Si cal, tapa't les mans.
- 10 minuts cada dia val infinitament més que una hora els divendres.

## Comprova que ho tens

- [ ] Sé dir en veu alta la ruta completa d'un fitxer meu.
- [ ] Veig les extensions al meu explorador de fitxers.
- [ ] Tinc creada l'estructura del portafoli amb les 8 carpetes de situació.
- [ ] Tinc decidida i provada la meua estratègia de còpia de seguretat.
- [ ] Tinc compte a TypingClub i he fet la primera sessió.
