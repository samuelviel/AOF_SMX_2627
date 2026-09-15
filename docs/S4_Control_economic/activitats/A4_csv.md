# A4 · El CSV del proveïdor

**Sessió 20** · lliurament: fitxer processat + fitxa del procés
**Avalua:** RA3 <span class="ca">e</span> <span class="ca">f</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Compres · Per a: Equip tècnic</p>

El proveïdor ens envia el catàleg actualitzat **cada dilluns** en un fitxer que, cada dilluns, algú passa una hora arreglant a mà.

Volem dues coses: que s'importe bé, i que d'ací en avant l'arreglada no la faça una persona.
</div>

## El material

Un CSV de proveïdor amb tots els problemes reals que et trobaràs a la vida:

- Separador que no és el que esperes
- Codificació que no és UTF-8 (accents trencats)
- Codis d'article amb **zeros al davant**
- Comes dins de camps de descripció
- Espais sobrants al principi i al final
- Separador decimal incoherent
- Files duplicades
- Descripcions en majúscules i minúscules barrejades
- Alguna fila incompleta

## Part 1 · Importar bé

<span class="ca">CA f</span> Abans d'importar, **inspecciona el fitxer**. Obri'l amb un editor de text pla i mira les tres primeres línies. D'ací ixen els quatre paràmetres de [T5](../teoria/5_macros.md).

Documenta:

| Paràmetre | Valor detectat | Com ho has sabut |
| --- | --- | --- |
| Separador de camps | | |
| Codificació | | |
| Delimitador de text | | |
| Separador decimal | | |
| Columnes forçades a text | | |

I la **verificació**, que és la part que quasi ningú fa:

- [ ] Nombre de files del CSV = nombre de files importades (compta-les al fitxer original)
- [ ] Els codis amb zeros davanters els conserven
- [ ] Els accents es veuen bé
- [ ] Els preus són números (la barra d'estat en dona la suma)
- [ ] Cap descripció partida en dues columnes

!!! danger "El pas que separa aprovat de nivell client"
    Importar és fàcil. **Verificar que la importació és correcta** és la competència professional.

    Si no comptes les files, no saps si has perdut registres. I no ho sabràs mai, perquè un catàleg amb 4 articles menys no dona cap error: simplement, algun dia no trobaràs un article.

## Part 2 · Netejar

Neteja necessària:

1. Espais sobrants
2. Unificar la caixa de les descripcions
3. Convertir els preus a número real
4. Eliminar duplicats (i **documentar quants n'hi havia**)
5. Marcar o apartar les files incompletes — **no esborrar-les sense mirar-les**

Fes-ho primer **amb fórmules en columnes auxiliars**, documentant quina fórmula resol cada problema. Després enganxa només valors.

## Part 3 · Automatitzar

<span class="ca">CA e</span> Ara la part que respon a "cada dilluns".

**Primer, el càlcul de justificació** de [S2/T5](../../S2_Identitat_documental/teoria/5_macros.md):

| Pregunta | Resposta |
| --- | --- |
| Temps a mà cada setmana | |
| Vegades a l'any | |
| Temps perdut a l'any | |
| Temps d'automatitzar | |
| Compensa? | |

Ací compensa clarament — eixe és el punt: és un cas real on la macro es justifica sola, a diferència de [S2/A3](../../S2_Identitat_documental/activitats/A3_macro.md), on havies de decidir-ho.

**La macro** ha de:

- [ ] Comprovar abans d'actuar (existeix el full? té dades?)
- [ ] Aplicar la neteja de la part 2
- [ ] **Informar del resultat**: files processades, duplicats eliminats, files incompletes trobades
- [ ] Deixar les files problemàtiques marcades, no esborrades
- [ ] Estar comentada

### Els tres casos de prova

| Cas | Entrada | Resultat esperat | Resultat real |
| --- | --- | --- | --- |
| Normal | El CSV de la setmana | | |
| Límit | CSV amb una sola fila de dades | | |
| Error | Full buit o amb capçaleres diferents | | |

## Part 4 · La fitxa del procés

Una pàgina que servisca com a **procediment d'empresa**, perquè un company puga fer-ho sense tu:

1. Paràmetres d'importació i com verificar-los
2. Llista de verificació post-importació
3. Com s'executa la macro i què fa
4. Què fer amb les files marcades com a problemàtiques
5. **Limitacions:** què passaria si el proveïdor canvia el format del fitxer
6. [Nota d'ús d'IA](../../recursos/ia.md)

## Com s'avalua

### RA3.f) Importació i exportació — 50 %

- 🟢 Els quatre paràmetres detectats i **justificats amb com ho has sabut** (no per prova i error a cegues). Verificació completa amb recompte de files. Cap dada corrompuda: zeros conservats, accents correctes, preus numèrics, descripcions senceres. Exportació final al format acordat amb consciència del que s'hi perd.
- 🔵 Importació correcta i verificada, però algun paràmetre trobat provant sense entendre per què, o verificació sense recompte de files.
- 🟡 Importació que funciona però amb alguna dada degradada no detectada (zeros perduts, algun accent).
- 🔴 Importació sense verificar, amb pèrdua de registres o de dades.

### RA3.e) Macros emprades — 50 %

- 🟢 Macro funcional i robusta, amb comprovació prèvia, informe de resultat i gestió de les files problemàtiques sense esborrar-les. Tres casos de prova documentats incloent-hi el d'error. Càlcul de justificació real. L'apartat de limitacions identifica correctament què la trencaria.
- 🔵 Macro funcional i documentada, però sense informe de resultat, o sense el cas d'error resolt.
- 🟡 Macro que funciona només amb el fitxer exacte de l'exemple, o gravació enganxada sense netejar ni comentar.
- 🔴 No funciona, o esborra dades sense avisar, o no la pots explicar.

!!! quote "Punt de comprensió"
    *"El proveïdor ha afegit una columna nova al principi del fitxer. Què passa amb la teua macro i què has de tocar?"*

    És la pregunta que et faran a qualsevol empresa on hi haja un procés automatitzat.
