# T4 · Documents de gran volum

<span class="ca">CA a</span> <span class="ca">CA c</span>

Un document de 3 pàgines aguanta qualsevol cosa. Un de 30 es desmunta si no està construït. Esta és la diferència entre escriure i **maquetar**.

## Seccions i estils de pàgina

Un document llarg no té la mateixa pàgina de principi a fi:

- la **portada** no porta capçalera ni numeració,
- l'**índex** es numera sovint a banda o no es numera,
- el **cos** porta capçalera amb el títol i peu amb `pàgina X de Y`,
- alguna pàgina pot ser **apaïsada** per a una taula ampla,
- els **annexos** poden numerar-se amb un altre esquema.

Perquè això siga possible cal partir el document. A LibreOffice es fa amb **salts de pàgina amb canvi d'estil de pàgina**; a Word, amb **salts de secció**, desvinculant la capçalera de la secció anterior (*Enllaça amb l'anterior*, que ve activat per defecte i és la causa del 90 % dels problemes de capçalera).

!!! danger "Si canvies la capçalera d'un capítol i canvia a tot el document"
    És exactament això: no hi ha salt de secció, o la secció nova continua enllaçada amb l'anterior.

## L'índex automàtic

Si has fet servir estils de títol, l'índex és un clic. Si no els has fet servir, no hi ha índex.

- S'insereix on vulgues i es genera a partir dels nivells de títol.
- **No s'actualitza sol en desar**: cal actualitzar-lo abans de lliurar. Molta gent entrega un PDF amb un índex que apunta a pàgines que ja no existeixen.
- Es pot configurar quants nivells mostra. Tres és el màxim raonable.
- Es poden generar també índexs de figures, de taules i índexs alfabètics per paraules clau.

## Referències creuades

Una **referència creuada** és un enllaç intern viu: *"vegeu l'apartat 3.2 a la pàgina 14"*, on tant el número d'apartat com el de pàgina s'actualitzen sols.

L'alternativa —escriure-ho a mà— garanteix que el document mentirà en la segona revisió.

## Notes al peu i notes finals

Al peu de la pàgina o al final del document. S'usen per a aclariments i fonts, no per a contingut essencial: si el lector ha de llegir-ho obligatòriament, va al cos.

Es numeren soles i es reorganitzen quan mous text.

## Control de canvis i comentaris

Quan un document el revisa una altra persona, no s'edita "a saco": s'activa el **control de canvis** (*Edita → Segueix els canvis* a LibreOffice, *Revisió → Control de canvis* a Word).

A partir d'ací cada modificació queda marcada amb autor i data, i l'autor original pot **acceptar-la o rebutjar-la** una a una.

Els **comentaris** són per al que no es pot arreglar directament: *"esta captura no es correspon amb el que diu el text"*.

!!! warning "Abans de lliurar, neteja"
    Un PDF entregat a un client amb els canvis marcats i els comentaris interns visibles és un accident professional clàssic. Accepta o rebutja tots els canvis, elimina els comentaris i revisa les **propietats del document** (autor, empresa, comentaris ocults) abans d'exportar.

## Combinació de correspondència

Un document base + una font de dades = molts documents personalitzats.

És el que hi ha darrere de les cartes, els certificats, les etiquetes i els correus massius personalitzats. Els passos són sempre els mateixos:

1. **Font de dades**: un full de càlcul o una base de dades amb una fila per destinatari i una columna per camp.
2. **Document base**: el text comú amb els **camps de combinació** on ha d'anar la dada variable.
3. **Vista prèvia**: comprova tres o quatre registres reals, no només el primer.
4. **Generació**: a document nou, a impressora o a correu electrònic.

!!! tip "El detall que delata una combinació mal feta"
    *"Benvolgut/da NOM,"*. Sempre hi ha algun registre buit o amb una dada rara. Per això es fa vista prèvia de diversos registres i es preveu què passa quan un camp està buit.

## Ordre de muntatge recomanat

Quan et toque fer el manual d'[A2](../activitats/A2_manual.md), segueix este ordre. Fer-ho al revés costa el doble:

1. Crear el document **des de la plantilla**.
2. Escriure el contingut amb els **estils de títol** correctes, sense preocupar-te de l'aspecte.
3. Inserir imatges amb ancoratge i **llegenda**.
4. Definir **seccions/estils de pàgina** i capçaleres.
5. Inserir **índex** i **referències creuades**.
6. Revisar: ortografia, marques de format, vista de full sencer.
7. **Actualitzar l'índex**, netejar canvis i comentaris, revisar propietats.
8. Exportar a PDF i **obrir el PDF** per comprovar-lo.
