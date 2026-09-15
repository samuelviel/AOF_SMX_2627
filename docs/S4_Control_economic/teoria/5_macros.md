# T5 · Importar, exportar i macros

<span class="ca">CA e</span> <span class="ca">CA f</span>

## CSV: el format que tot ho connecta

Un **CSV** és text pla: una fila per línia, camps separats per un caràcter. No té format, ni fórmules, ni colors. Precisament per això és el format universal d'intercanvi de dades.

Qualsevol sistema — un TPV, una botiga en línia, un ERP, una base de dades — exporta CSV. Saber importar-lo bé és una de les habilitats més rendibles de tot el mòdul.

### Els quatre paràmetres que has d'encertar

| Paràmetre | Opcions | Símptoma si l'encertes malament |
| --- | --- | --- |
| **Separador de camps** | Coma, punt i coma, tabulador | Tot en una sola columna |
| **Codificació** | UTF-8, ISO-8859-1, Windows-1252 | Accents convertits en símbols estranys |
| **Delimitador de text** | Cometes dobles | Camps partits on hi havia una coma dins |
| **Separador decimal** | Punt o coma | Els preus es converteixen en text o es multipliquen per 1000 |

!!! danger "El clàssic: la coma dins del camp"
    Un CSV separat per comes amb un camp `"Cable HDMI, 2 metres"`. Si el delimitador de text no està configurat, eixe camp es parteix en dos i **totes les columnes de la fila es desplacen**.

    El resultat no és un error visible: és una fila amb el preu a la columna equivocada. Per això la importació **sempre s'ha de verificar**, no només fer.

### La finestra d'importació

Quan obris un CSV, el full de càlcul mostra una previsualització. **No li dones a "Acceptar" sense mirar-la.** És el moment on pots:

- Triar el separador i veure l'efecte en directe
- Canviar la codificació i veure si els accents es col·loquen
- **Marcar una columna com a text** — imprescindible per a codis amb zeros al davant

!!! warning "Els zeros que desapareixen"
    Un codi d'article `00147` importat com a número es converteix en `147`. Els zeros davanters es perden per sempre, i després cap cerca els troba.

    A la finestra d'importació, marca eixa columna com a **Text**. Si ja l'has importada malament, no hi ha manera d'endevinar quants zeros hi havia: cal tornar a importar.

### Exportar

En exportar a CSV es perd tot el que no siguen valors: fórmules (s'exporta el resultat), formats, gràfics, diversos fulls (només s'exporta el full actiu).

Això no és un defecte: és el que vol dir "format d'intercanvi". El que has de saber és **què estàs perdent**, i conservar sempre el fitxer original.

## Altres formats

| Format | Quan |
| --- | --- |
| `.ods` / `.xlsx` | Treball. L'`.xlsx` és el format d'intercanvi de facto |
| `.csv` | Dades cap a un altre sistema |
| `.pdf` | Lliurament a client, no editable |
| `.html` | Publicar una taula |

**Anada i tornada `.ods` ↔ `.xlsx`:** les fórmules estàndard sobreviuen bé; els gràfics es converteixen amb pèrdues d'estil; **les macros no sobreviuen mai**; el format condicional amb fórmula de vegades es degrada.

## Macros al full de càlcul

<span class="ca">CA e</span> Els principis són els mateixos que vas veure a [S2/T5](../../S2_Identitat_documental/teoria/5_macros.md): decidir si compensa, gravar, netejar, comprovar abans d'actuar.

**On compensen de veritat en un full:**

- Importar i netejar un fitxer que arriba **cada setmana amb el mateix format**
- Generar un informe amb la data i el nom de fitxer segons convenció
- Aplicar el format corporatiu a una taula nova
- Restablir filtres i seleccions abans d'imprimir

**Exemple: netejar una columna importada**

```basic
Sub NetejaColumna
    Dim oDoc As Object, oFull As Object, oCel As Object
    Dim i As Integer, sVal As String

    oDoc = ThisComponent
    oFull = oDoc.Sheets.getByName("Importat")

    ' Comprovació prèvia: el full ha d'existir i tindre dades
    If oFull.getCellByPosition(0,1).getString() = "" Then
        MsgBox "El full 'Importat' està buit.", 48, "Neteja"
        Exit Sub
    End If

    ' Recorre la columna A des de la fila 2
    i = 1
    Do While oFull.getCellByPosition(0, i).getString() <> ""
        oCel = oFull.getCellByPosition(0, i)
        sVal = Trim(oCel.getString())          ' lleva espais
        oCel.setString(UCase(sVal))            ' a majúscules
        i = i + 1
    Loop

    MsgBox "Netejades " & (i-1) & " files.", 64, "Neteja"
End Sub
```

Fixa't en tres coses: comprova abans d'actuar, para sola quan s'acaben les dades, i **informa del resultat**. Una macro que no diu què ha fet deixa l'usuari sense saber si ha funcionat.

!!! note "Alternativa sense macro"
    Moltes neteges es resolen amb fórmules (`RETALLA`, `SUBSTITUEIX`) en una columna auxiliar i després enganxant només valors.

    Abans de fer una macro, pregunta't si una columna auxiliar ho resol. Sovint sí, i és més fàcil de mantindre per a qui vinga després.

## 🤖 IA i importació

**Molt bon ús:** enganxar-li **tres línies** d'un CSV problemàtic i preguntar-li quin separador, codificació i delimitador de text té. Encerta quasi sempre i estalvia molt temps.

**Bon ús:** demanar-li una fórmula de neteja per a un patró concret de dada bruta.

**El que has de fer tu:** verificar el resultat comptant files i comprovant els casos rars. La IA no pot saber si s'han perdut 4 registres de 800.

## Comprova que ho tens

- [ ] Sé els quatre paràmetres d'una importació CSV i el símptoma de cada error.
- [ ] Sé per què es perden els zeros davanters i com evitar-ho.
- [ ] Sé què es perd en exportar a CSV.
- [ ] Sé que les macros no sobreviuen al canvi de format.
- [ ] Sé decidir si un problema es resol amb fórmula o necessita macro.
