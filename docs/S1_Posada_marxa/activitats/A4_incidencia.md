# A4 · El primer parte d'incidència

<span class="ca">CA d</span> <span class="ca">CA e</span>

**Modalitat:** parelles · **Sessions:** 12 · **Lliurament:** parte d'incidència en PDF

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Direcció · Per a: Equip tècnic</p>

**Assumpte: l'equip d'un company no va bé**

Al portàtil d'un company li passa alguna cosa des d'ahir. Ell diu que "no va" i que "abans anava".

Que li ho mire algú i m'ompliu el parte, que si es torna a repetir vull saber què es va fer.
</div>

## Com funciona

Rebreu un equip (o un perfil d'usuari) amb **una o diverses avaries provocades**. Podeu trobar-vos coses com estes:

- l'idioma de la interfície o del corrector canviat,
- el desat automàtic desactivat i el format per defecte alterat,
- una extensió que fa que el programa òbriga molt lent,
- associacions de fitxer trencades: els documents s'òbriguen amb el programa que no toca,
- una plantilla per defecte modificada, de manera que tots els documents nous ixen malament,
- permisos o rutes de la carpeta de treball canviats.

No sabràs quantes n'hi ha ni quines són. Eixa és la gràcia.

## El mètode

Este és el punt de l'activitat: **no és endevinar, és diagnosticar**. La diferència entre els dos és que el diagnòstic es pot explicar.

1. **Reproduir.** Aconsegueix que el problema passe davant teu. Si no el pots reproduir, encara no saps què arregles.
2. **Delimitar.** Passa a l'usuari nou? Passa amb un altre fitxer? Passa sempre o només de vegades? Cada resposta elimina causes.
3. **Formular una hipòtesi.** *"Crec que és X perquè he observat Y."*
4. **Provar-la canviant una sola cosa.** Si toques tres coses alhora i funciona, no saps quina era.
5. **Verificar.** Torna a fer el que fallava. Repeteix-ho dues vegades.
6. **Documentar.** Fins que no està escrit, la faena no està acabada.

!!! danger "Prohibit reinstal·lar"
    *"He formatat i ja va"* és nivell 🔴 automàtic en esta activitat. Un tècnic que reinstal·la sense diagnosticar no ha aprés res i el problema tornarà.

## El parte

Un parte per cada incidència trobada. Format complet a la [T4](../teoria/4_documentar.md):

| Camp | Contingut |
| --- | --- |
| Identificador i data | |
| Símptoma **segons l'usuari** | Les seues paraules, no la teua interpretació |
| Símptoma **observat** | Què has vist tu al reproduir-ho |
| Proves fetes | Cada prova i què va descartar |
| Causa | |
| Solució aplicada | Passos exactes |
| Verificació | Com has comprovat que està resolt |
| Prevenció | Què evitaria que tornara a passar |

## Bonus: la resposta a l'usuari

Escriu, a més, **tres o quatre línies** explicant-li al company què li passava i què has fet. Sense sigles i sense fer-lo sentir idiota.

Esta part no puntua en cap CA d'este RA — però és exactament la competència que es treballa a la [mesa d'ajuda](../../recursos/mesa_ajuda.md) i que s'avalua al RA9. Val la pena agafar el costum ara.

## Com s'avalua

**RA1.d · Documentar les incidències — 40 %**

- 🟢 Un parte per incidència, amb tots els camps completats. Es distingeix clarament el símptoma de l'usuari, el símptoma observat, la causa i la solució. Un altre tècnic podria reproduir la reparació només amb això.
- 🔵 Parte complet però amb algun camp fluix: la prevenció és genèrica o la verificació s'esmenta sense concretar.
- 🟡 Es documenta el que s'ha fet però no el procés: apareix la solució sense les proves que hi porten.
- 🔴 No hi ha parte, o es confon el símptoma amb la causa.

**RA1.e · Solucionar problemes en la instal·lació o integració — 60 %**

- 🟢 Totes les avaries localitzades i resoltes, amb hipòtesis explícites i proves que canvien una variable cada vegada. La verificació demostra que el problema ha desaparegut.
- 🔵 Totes resoltes, però el camí té algun pas per assaig i error sense justificar.
- 🟡 Alguna avaria sense localitzar, o resolta per casualitat sense poder explicar per què funciona ara.
- 🔴 Problema sense resoldre, o "resolt" reinstal·lant o restaurant sense diagnòstic.

!!! note "Punt de comprensió"
    Ací el punt de comprensió és gairebé l'activitat sencera: et preguntaré **com hauries actuat si la hipòtesi haguera fallat**. Si no pots respondre, el diagnòstic no era teu.
