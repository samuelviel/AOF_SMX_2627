# T4 · Documentar incidències i resoldre problemes

<span class="ca">CA d</span> <span class="ca">CA e</span>

La part de la faena que ningú vol fer i que separa els tècnics dels aficionats.

## Per què s'escriu tot

Tres motius que no són burocràtics:

1. **Perquè es repetirà.** El 80 % de les incidències d'una empresa són variacions de mitja dotzena de problemes. Documentar-les una vegada estalvia resoldre-les cinquanta.
2. **Perquè no estaràs tu.** El dia que un company haja de tocar eixe equip, o el dia que estigues de baixa, el que hages escrit és tot el que queda.
3. **Perquè el client pregunta.** *"Què vau fer exactament al meu ordinador?"* és una pregunta legítima i has de poder respondre-la.

## El parte d'incidència

Set camps. No més, no menys.

| Camp | Contingut | Error habitual |
| --- | --- | --- |
| **Identificador** | `INC-2026-014` | No posar-ne cap |
| **Data i hora** | Detecció i resolució | Només la data |
| **Equip / usuari** | Quin equip, qui ho patia | "Un ordinador de l'aula" |
| **Símptoma** | El que **es veu**, amb les paraules de qui ho patia | Escriure la causa on toca el símptoma |
| **Diagnòstic** | Causa real i **com l'has determinada** | "Estava malament" |
| **Solució** | Passos exactes, reproduïbles | "Ho he arreglat" |
| **Verificació** | Com has comprovat que està resolt | Ometre-la |

!!! danger "Símptoma ≠ diagnòstic"
    És l'error que més es repeteix i el que més nota costa.

    - Símptoma: *"En obrir un `.docx`, LibreOffice mostra els marges canviats."*
    - Diagnòstic: *"El document usava una font no instal·lada a l'equip; LibreOffice l'ha substituïda per una altra amb mètriques diferents."*

    Si escrius el diagnòstic al camp de símptoma, has saltat el pas de pensar. I si t'equivoques, ningú podrà detectar-ho perquè ja no queda registre del que es veia de veritat.

### Escriure els passos de solució

La prova: **que una altra persona puga repetir-los sense preguntar-te res**.

Malament:

> He tornat a configurar les opcions de desat i ja va bé.

Bé:

> 1. `Eines → Opcions → Carrega/Desa → General`.
> 2. Al desplegable *Sempre desa com a*, he canviat "Word 2007-365 (.docx)" per "Document de text ODF (.odt)".
> 3. He acceptat i he reiniciat LibreOffice.
> 4. **Verificació:** document nou → `Ctrl+S` → el diàleg proposa `.odt`.

## El mètode de diagnòstic

<span class="ca">CA e</span> Quan una cosa falla, el reflex és tocar coses fins que funcione. Això de vegades funciona, mai ensenya res i sovint espatla una altra cosa.

**El mètode, en cinc passos:**

### 1. Reproduir

Fes que el problema torne a passar. Si no el pots reproduir, no el pots arreglar — i tampoc podràs saber si l'has arreglat.

Anota la **seqüència exacta**: quins passos, en quin ordre, amb quin fitxer.

### 2. Delimitar

Estreny on viu el problema fent preguntes que parteixen l'espai en dos:

- Passa amb **tots els documents** o només amb un?
- Passa amb **tots els usuaris** o només amb un? → si és d'un usuari, apunta a configuració de perfil.
- Passa en **tots els equips** o només en un? → si és d'un equip, apunta a instal·lació.
- **Des de quan?** Què va canviar just abans.

Cada resposta elimina la meitat de les causes possibles. Tres o quatre preguntes ben triades deixen el problema quasi resolt.

### 3. Hipòtesi

Formula una causa concreta i **comprovable**. "Va malament" no és una hipòtesi. "El perfil d'usuari de LibreOffice està corrupte" sí que ho és, perquè es pot provar.

### 4. Provar, canviant una cosa cada vegada

La regla d'or. Si canvies tres coses alhora i el problema desapareix, no saps quina el causava — i tampoc pots documentar-ho.

### 5. Verificar i revertir

Comprova que està resolt **i** que no has trencat res més. Desfés els canvis que has fet provant i que no formen part de la solució.

## Incidències típiques d'una suite ofimàtica

Les que et trobaràs a [A4](../activitats/A4_incidencia.md) i, després, a la [mesa d'ajuda](../../recursos/mesa_ajuda.md) tot el curs.

| Símptoma | Causa habitual | Comprovació ràpida |
| --- | --- | --- |
| El programa no arranca o obri en blanc | Perfil d'usuari corrupte | Arrancar en mode segur |
| Els documents es descol·loquen en un altre equip | Font no instal·lada | Mirar quina font demana el document |
| No pot desar en una carpeta | Permisos | Provar de desar a la carpeta personal |
| Falta un mòdul (Base, editor de fórmules) | Component no instal·lat | Modificar la instal·lació |
| Menús en un idioma inesperat | Paquet d'idioma o configuració regional | Opcions → Configuració d'idioma |
| El corrector no subratlla res | Diccionari no instal·lat o idioma del text mal marcat | Seleccionar text → mirar l'idioma assignat |
| Els `.docx` s'obrin amb un altre programa | Associació de fitxers | Obri amb → establir per defecte |

### El mode segur

Arranca la suite amb la configuració per defecte, sense tocar la teua. És la manera més ràpida de respondre la pregunta *"és problema del programa o del meu perfil?"*.

```bash
soffice --safe-mode
```

Si en mode segur funciona, el problema és la configuració d'usuari, no la instal·lació. També es pot llançar des de `Ajuda → Reinicia en mode segur`.

## 🤖 La IA com a ajuda de diagnòstic

És bastant útil ací, amb dues condicions.

**Dona-li el símptoma, no la teua conclusió.** Si li dius "tinc el perfil corrupte, com el reparo?", et respondrà com reparar un perfil — encara que el teu problema siga una altra cosa. Descriu el que veus.

**Fes-li generar hipòtesis, no solucions.** Un bon encàrrec: *"Estos són els símptomes i açò és el que ja he descartat. Dona'm cinc causes possibles ordenades de més a menys probable i com comprovaria cadascuna."* Això t'acompanya el raonament en lloc de substituir-lo.

I no apliques mai una ordre de sistema que no entens perquè te l'ha donada una IA. Si no saps què fa, busca-ho abans.

## Comprova que ho tens

- [ ] Sé els set camps d'un parte i què va a cadascun.
- [ ] Sé escriure un símptoma sense colar-hi el diagnòstic.
- [ ] Sé les quatre preguntes de delimitació.
- [ ] Sé per què no es canvien dues coses alhora.
- [ ] Sé arrancar la suite en mode segur i què demostra.
