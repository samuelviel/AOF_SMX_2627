# T4 · Formularis, informes i macros

<span class="ca">CA e</span> <span class="ca">CA f</span> <span class="ca">CA h</span>

Les taules i les consultes són la màquina. Els formularis i els informes són **el que veu l'usuari**.

I això importa molt en este encàrrec: el client ha dit literalment que ho ha de poder usar la Rosa, que mai ha vist una base de dades.

## Formularis

<span class="ca">CA e</span> Un **formulari** és una interfície per a introduir i consultar dades sense veure la taula.

Per què no deixar que l'usuari escriga directament a la taula:

- Veu columnes que no ha de tocar (claus, camps tècnics)
- Pot esborrar files senceres amb una tecla
- No té ajuda ni validació
- Ha de saber que `id_client = 47` és la Ferreteria Bellver

### Construir-lo

**Assistent** (`Formularis → Usa l'assistent`) per a la base, i després **vista de disseny** per a arreglar-lo. L'assistent mai deixa un formulari acabat, però estalvia el muntatge.

### Controls

| Control | Per a què |
| --- | --- |
| Quadre de text | Text i números |
| **Quadre de llista / combinat** | **Triar d'una altra taula** |
| Casella de selecció | Booleans |
| Camp de data | Dates, amb calendari |
| Camp formatat | Imports amb format i límits |
| Botó | Accions |

!!! tip "El quadre de llista és el control clau"
    És el que fa que l'usuari veja **"Ferreteria Bellver SL"** i la base de dades guarde **47**.

    Sense ell, el formulari obliga a saber els identificadors, i llavors no serveix per a res.

    Es configura amb una consulta d'origen: mostra un camp, emmagatzema un altre.

### Formularis amb subformulari

El patró més útil: dalt el client, baix la llista dels seus expedients, sincronitzada. Es configura vinculant el camp de la relació entre el formulari principal i el subformulari.

És exactament el que necessita la gestoria: obrir un client i veure'n tot l'historial.

### Fer-lo usable

- **Ordre de tabulació lògic** — l'usuari navegarà amb ++tab++
- **Etiquetes en llenguatge del client**, no noms de camp: "Telèfon de contacte", no `tel_cont`
- **Camps obligatoris marcats** visualment
- **Text d'ajuda** als camps que ho necessiten
- **Valors per defecte** on tinguen sentit (la data d'avui)
- **Agrupació visual** de camps relacionats

## Informes

<span class="ca">CA f</span> Un **informe** és una eixida formatada, pensada per a imprimir o enviar.

L'assistent d'informes de Base permet triar camps, agrupar, ordenar i aplicar una disposició.

**Informe estàtic vs dinàmic:** l'estàtic congela les dades del moment de crear-lo; el **dinàmic** les torna a llegir cada vegada que s'obri. Per a un informe que s'usarà mensualment, dinàmic.

**Agrupació i totals** — agrupar per client i mostrar el total de cada grup és el que converteix una llista en informació.

!!! tip "Informe sobre consulta, no sobre taula"
    Un informe basat directament en una taula mostra tot el que hi ha. Basat en una **consulta**, mostra exactament el que vols i pots usar paràmetres.

    La bona pràctica és: consulta primer, informe després. Així la lògica està en un sol lloc i la pots reutilitzar.

### La sortida

Els informes de Base es generen com a documents de Writer. Això vol dir que pots aplicar-los **la plantilla corporativa** de [S2](../../S2_Identitat_documental/activitats/A1_plantilla.md) i exportar-los a PDF amb la identitat de l'empresa.

És el tancament del cercle: el que produeix la base de dades ix amb la mateixa cara que tota la resta de documents de l'empresa.

## Macros

<span class="ca">CA h</span> Els mateixos principis de [S2/T5](../../S2_Identitat_documental/teoria/5_macros.md).

**On compensen en una base de dades:**

- Botó "Nou client" que obri el formulari net
- Botó que executa un informe amb els paràmetres del formulari actual
- Validació complexa abans de desar (comprovar que el NIF té format correcte)
- Còpia de seguretat automàtica en obrir

**Esdeveniments** — a Base, les macros s'assignen sovint a esdeveniments de formulari: en obrir, abans de desar, en fer clic a un botó. `Formulari → Propietats → Esdeveniments`.

!!! warning "Macros que modifiquen dades"
    Una macro que esborra o modifica registres ha de **demanar confirmació** i informar del resultat.

    Una macro silenciosa que canvia dades és el pitjor escenari possible: quan es detecta el problema, ningú sap quantes vegades s'ha executat.

## Documentar per a l'usuari

El CA no ho diu, però l'encàrrec sí: la Rosa ha de poder usar això.

Això vol dir un **manual breu** amb captures, com el que vas fer a [S2/A2](../../S2_Identitat_documental/activitats/A2_manual.md), i amb els mateixos criteris: una acció per pas, sense sigles, dient què ha de passar.

I és, alhora, el CA (a) i (c) del [RA9](../../recursos/mesa_ajuda.md).

## Comprova que ho tens

- [ ] Sé per què l'usuari final no ha de treballar sobre la taula.
- [ ] Sé configurar un quadre de llista que mostre un camp i en guarde un altre.
- [ ] Sé muntar un formulari amb subformulari sincronitzat.
- [ ] Sé per què un informe es basa en una consulta i no en una taula.
- [ ] Sé assignar una macro a un botó i a un esdeveniment de formulari.
- [ ] Sé aplicar la plantilla corporativa a un informe.
