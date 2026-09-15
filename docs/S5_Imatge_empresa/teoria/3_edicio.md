# T3 · Edició i exportació

<span class="ca">CA d</span> <span class="ca">CA e</span>

## Edició no destructiva

El principi que ordena tota la resta: **no modifiques mai l'original**.

- Treballa sobre una **còpia**
- Usa **capes** en lloc de pintar damunt del fons
- Guarda el fitxer de treball en format natiu (`.xcf` de GIMP, `.svg` d'Inkscape) **i** exporta el resultat a part
- L'exportació és un producte derivat: si cal canviar-la, es torna al fitxer de treball

!!! danger "El dia que passa"
    Has fet un cartell, l'has aplanat, l'has exportat a JPG i has esborrat el treball. El client vol canviar el telèfon.

    Tornes a fer el cartell sencer.

## Capes

Fulls transparents apilats. Cada element del teu disseny, en la seua capa.

- **Ordre** — el que està a dalt tapa el que està a baix
- **Opacitat** — transparència de la capa sencera
- **Modes de fusió** — com es barreja amb la de sota (multiplicar, pantalla, superposar)
- **Màscara de capa** — amaga parts sense esborrar-les. **La millor eina de tot GIMP**: pintes de negre a la màscara per a amagar, de blanc per a tornar a mostrar. Sempre reversible.

**Nomena les capes.** Un fitxer amb "Capa 1", "Capa 2", "Còpia de Capa 1 #3" és un fitxer que ningú tornarà a obrir, incloent-te a tu.

## Selecció

| Eina | Per a què |
| --- | --- |
| Rectangle / el·lipse | Formes regulars, retallar |
| Llaç | Contorns lliures |
| **Vareta màgica** | Zones de color uniforme — ideal en captures |
| **Selecció per color** | Tots els píxels d'un color al document |
| Tisores / camí | Contorns complexos amb precisió |

**El difuminat de vora** (*feather*) suavitza el tall. Sense ell, les vores queden dentades i es nota que la imatge està manipulada.

## Els ajustos que necessites

En ordre d'utilitat real:

1. **Retallar** — la millor millora possible en el 80 % dels casos
2. **Nivells** — ajusta blancs, negres i mitjos. Més potent i controlable que "brillantor/contrast"
3. **Corbes** — control fi per zones de lluminositat
4. **Balanç de blancs** — corregeix dominants de color (la foto groguenca de llum artificial)
5. **Saturació** — amb moderació
6. **Enfocament** — sempre **l'últim pas**, després de redimensionar

!!! tip "Per què l'enfocament va al final"
    Reduir una imatge la suavitza. Si l'enfoques abans de reduir, perds l'efecte; si l'enfoques abans i després, apareixen halos.

    Ordre correcte: edita → redimensiona → enfoca → exporta.

## Treballar amb vectorial

Per al logotip a [A1](../activitats/A1_marca.md), Inkscape:

- **Camins** — la unitat bàsica. Es poden unir, restar i intersecar (`Camí → Unió`, `Diferència`...)
- **Text a camí** — converteix el text en formes. **Imprescindible abans d'enviar a impremta**: si no, l'impremta necessita la teua tipografia i, si no la té, el logo canvia
- **Document amb mida real** — configura el llenç en mil·límetres, no en píxels
- **Exportar PNG a qualsevol mida** des del mateix SVG

!!! warning "Text a camí: una via sense retorn"
    Una vegada convertit, el text ja no és editable. **Guarda sempre dues versions:** una amb text viu (per a editar) i una amb text convertit (per a enviar).

## Exportació: triar bé

<span class="ca">CA e</span>

| Destí | Format | Ajustos |
| --- | --- | --- |
| Captura per a manual | PNG | Mida real, sense escalar |
| Foto per a web | WEBP o JPG q80-85 | Redimensionada a la mida de visualització |
| Logotip web | **SVG** | Amb PNG de reserva |
| Logotip sobre fons de color | PNG amb transparència | |
| Impremta | PDF o TIFF | 300 ppp, CMYK, marges de sagnat |
| Arxiu | TIFF o format natiu | Sense compressió amb pèrdua |

### Optimitzar per a web

Una imatge de 4 MB en una pàgina web fa que la pàgina no es carregue. Optimitzar és:

1. **Redimensionar** a la mida real de visualització (el pas que més pesa)
2. Triar el format adequat
3. Ajustar la qualitat: JPG a 80-85 sol ser indistingible de 100 i pesa la meitat
4. **Eliminar metadades**

Objectiu raonable: menys de 200 KB per a una imatge de contingut.

## El kit d'un logotip

El que ha de contindre un lliurament professional, i el que faràs a [A1](../activitats/A1_marca.md):

| Fitxer | Per a què |
| --- | --- |
| `logo.svg` | Original vectorial, editable |
| `logo_impremta.pdf` | Text convertit a camins, CMYK |
| `logo_1000.png` | Alta resolució amb transparència |
| `logo_200.png` | Web |
| `logo_negatiu.png` | Versió per a fons foscos |
| `logo_monocrom.png` | Una sola tinta (segells, fax, brodat) |
| `favicon.svg` / `.png` | Versió mínima, 32 px |

**La prova dels 16 píxels:** redueix el logo a 16 × 16 i mira'l. Si és una taca il·legible, el disseny és massa complex. Un bon logotip funciona a totes les mides.

## 🤖 IA i imatge

**Usos raonables:** generar idees i esbossos de composició, proposar paletes amb contrast comprovable, i ajudar amb el text alternatiu.

**Compte amb les imatges generades:** en material d'empresa, una imatge generada es declara. I una imatge generada **no substitueix una captura real** — si el manual diu que la pantalla es veu així, ha de veure's així.

**El logotip el dissenyes tu.** És la identitat de l'empresa, l'has de poder defensar i l'has de poder modificar. Un PNG generat que no pots editar ni vectoritzar no serveix per a res del kit anterior.

## Comprova que ho tens

- [ ] Sé per què es guarda el fitxer de treball a banda de l'exportació.
- [ ] Sé usar una màscara de capa i per què és millor que esborrar.
- [ ] Sé l'ordre correcte: editar, redimensionar, enfocar, exportar.
- [ ] Sé per què es converteix el text a camins abans d'enviar a impremta.
- [ ] Sé triar format i ajustos segons el destí.
- [ ] Sé quins fitxers ha de contindre el kit d'un logotip.
