# T5 · Macros

<span class="ca">CA e</span>

Una **macro** és una seqüència d'accions guardada amb un nom, que pots tornar a executar quantes vegades vulgues.

La idea és antiga i molt simple: si fas el mateix cinc vegades al dia, que ho faça la màquina.

## Quan val la pena i quan no

Fer una macro té un cost. La pregunta no és *"es pot automatitzar?"* sinó **"compensa?"**.

| Val la pena | No val la pena |
| --- | --- |
| Tasca repetitiva i **estable** | Tasca que canvia cada vegada |
| Es fa sovint (diari, setmanal) | Es fa una vegada a l'any |
| Sempre els mateixos passos | Requereix decisions humanes pel camí |
| Errar-la té cost | Un error no importa |

!!! warning "La trampa de l'automatització"
    Passar tres hores automatitzant una tasca de dos minuts que fas un cop al mes no és eficiència: és entretindre's.

    A l'empresa, esta decisió s'ha de saber justificar. A [A3](../activitats/A3_macro.md) et demanaré exactament això, amb números.

## Enregistrar vs escriure

**Enregistrar** — actives la gravació, fas les accions i pares. La macro reprodueix el que has fet.

Avantatge: no cal programar. Inconvenient: grava *literalment*, incloent-hi desplaçaments i seleccions concretes, i sol ser fràgil quan el document canvia.

**Escriure** — programes la macro directament. Més robusta i més flexible, però cal conéixer el llenguatge.

**El mètode pràctic**, i el que faràs a A3: **grava-la primer, després obri-la i neteja-la**. Veure el codi que ha generat la gravació és, de fet, la millor manera d'aprendre l'API.

## Enregistrar a LibreOffice

!!! note "Primer cal activar-ho"
    `Eines → Opcions → LibreOffice → Avançat → Habilita l'enregistrament de macros`. Ve desactivat per defecte.

1. `Eines → Macros → Enregistra macro`.
2. Fes les accions. **Usa dreceres i menús, evita clics de posició.**
3. `Atura l'enregistrament` i dona-li nom.
4. Tria on la guardes: **"Les meues macros"** (només per a tu) o **dins del document** (viatja amb el fitxer).

**Veure i editar el codi:** `Eines → Macros → Edita macros` obri l'IDE de Basic.

## Un exemple real

Una macro que aplica l'estil corporatiu de codi a la selecció i li fixa l'idioma perquè el corrector no la subratlle:

```basic
Sub AplicaEstilCodi
    Dim oDoc As Object, oSel As Object, oText As Object
    Dim i As Integer

    oDoc = ThisComponent
    oSel = oDoc.getCurrentSelection()

    If oSel.getCount() = 0 Then
        MsgBox "Selecciona primer el text.", 48, "Estil de codi"
        Exit Sub
    End If

    For i = 0 To oSel.getCount() - 1
        oText = oSel.getByIndex(i)
        oText.CharStyleName = "Codi"
        oText.CharLocaleComplex = CreateUnoStruct( _
            "com.sun.star.lang.Locale")
    Next i
End Sub
```

Tres coses a mirar d'este codi, més enllà de la sintaxi:

1. **`ThisComponent`** és el document actiu. Quasi tota macro comença ací.
2. **Comprova abans d'actuar.** Si no hi ha selecció, avisa i ix. Una macro que peta amb un error críptic és pitjor que no tindre-la.
3. **Depén d'un estil que ha d'existir.** Si l'estil "Codi" no està definit, falla. Les macros i les plantilles van juntes.

## Macros a Word i a M365

Word usa **VBA**, un llenguatge diferent. L'estructura conceptual s'assembla (`ActiveDocument` en lloc de `ThisComponent`), però **el codi no és compatible**: una macro de Basic de LibreOffice no funciona a Word ni al revés.

!!! danger "M365 Online no executa macros"
    La versió web no executa VBA. Un document `.docm` obert en línia manté les macros guardades però no les pot executar.

    Açò té una conseqüència pràctica per a la vostra empresa: **si la solució depén d'una macro, depén de treballar en escriptori**. És exactament el tipus de restricció que has de detectar i documentar abans de proposar una solució a un client.

## Seguretat: per què venen desactivades

Les macros s'executen amb els teus permisos. Una macro maliciosa en un document adjunt pot fer el mateix que podries fer tu.

És un vector d'atac tan clàssic que continua funcionant: documents amb macros que s'executen en obrir-los i descarreguen programari maliciós.

**Nivells de seguretat** (`Eines → Opcions → LibreOffice → Seguretat → Seguretat de macros`):

| Nivell | Comportament |
| --- | --- |
| Molt alt | Només macros de ubicacions de confiança |
| Alt | Només macros signades digitalment |
| Mitjà | Pregunta a l'usuari |
| Baix | Executa tot **sense preguntar** — mai |

**Regla professional:** no actives mai les macros d'un document que no esperaves rebre, encara que semble d'un remitent conegut. I si distribuïxes documents amb macros als teus clients, **explica-los per què hauran d'autoritzar-les**: un document que demana permisos sense explicació genera desconfiança justificada.

## 🤖 IA i macros

Este és **un dels millors usos de la IA de tot el curs**, perquè el codi de macro es pot provar immediatament: o funciona o no.

Bon flux de treball:

1. Grava la macro tu, per a tindre una base que funcione.
2. Passa-li el codi gravat a la IA i demana-li que l'explique línia per línia.
3. Demana-li que el faça més robust (comprovacions, gestió d'errors).
4. **Prova-ho.** Si peta, torna-li l'error exacte.

El que no val: enganxar codi que no entens i lliurar-lo. A [A3](../activitats/A3_macro.md), el punt de comprensió serà **explicar-me tres línies concretes** de la teua macro. Si el codi és teu de veritat, són tres minuts.

## Comprova que ho tens

- [ ] Sé decidir amb criteri si una tasca mereix una macro.
- [ ] Sé enregistrar-ne una i saber on l'he guardada.
- [ ] Sé obrir l'editor i llegir el codi generat.
- [ ] Sé per què les macros venen desactivades i quin nivell de seguretat és raonable.
- [ ] Sé que M365 Online no executa macros i què implica per a un client.
