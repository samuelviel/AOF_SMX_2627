# T2 · Fórmules i funcions

<span class="ca">CA c</span>

## Anatomia d'una fórmula

Tota fórmula comença per `=`. El que ve després es resol seguint un ordre de prioritat: primer parèntesis, després potències, després multiplicació i divisió, i al final suma i resta. Les comparacions es resolen les últimes.

!!! danger "L'error de l'IVA mal calculat"
    `=B2+B2*0,21` és correcte.
    `=(B2+B2)*0,21` no ho és, i ningú se n'adona perquè també dona un número.

    Quan tingues qualsevol dubte, posa parèntesis. Sobren parèntesis explícits abans que un pressupost amb un total erroni.

## Els errors i què volen dir

No són fracassos: són diagnòstics. Cada error et diu on mirar.

| Error | Significa | On mirar |
| --- | --- | --- |
| `#DIV/0!` | Divisió per zero o per cel·la buida | El divisor. Sol ser un rang encara sense dades |
| `#VALOR!` | Tipus incorrecte | Hi ha text on s'esperava un número |
| `#REF!` | La referència ja no existeix | Has esborrat una fila o columna referenciada |
| `#NOM?` | Nom desconegut | Funció mal escrita, o nom de rang inexistent |
| `#N/D` | No s'ha trobat | Típic de les funcions de cerca |
| `####` | No hi cap | No és un error: eixampla la columna |

**Gestionar-los és part del disseny**, no un pegat. Un full que ha de rebre dades futures ensenyarà `#DIV/0!` fins que arriben, i això fa que semble espatlat.

```
=SI.ERROR( C2/B2 ; "" )
```

!!! warning "No abuses de SI.ERROR"
    Amaga l'error, no el resol. Si l'uses sobre una fórmula que **no hauria de fallar mai**, estàs ocultant un problema real i el descobriràs tard.

    Usa'l només quan l'error és **esperable i acceptable** (encara no hi ha dades). Si no, deixa'l veure.

## Les funcions que necessites de veritat

### Agregació

| Funció | Fa |
| --- | --- |
| `SUMA(rang)` | Suma |
| `MITJANA(rang)` | Mitjana aritmètica |
| `MAX` / `MIN` | Extrems |
| `COMPTA(rang)` | Compta **números** |
| `COMPTAA(rang)` | Compta cel·les **no buides** |
| `ARRODONEIX(valor; decimals)` | Arrodoneix de veritat el valor |

!!! tip "Arrodonir vs formatar"
    Posar 2 decimals de **format** no canvia el valor: el full continua guardant 12,4567 i sumant amb tots els decimals. Per això de vegades un total sembla que no quadra amb els números que veus.

    En diners, arrodoneix **amb la funció** on toque, no només amb el format.

### Condicionals

```
=SI( condició ; si_és_cert ; si_és_fals )
=SI( C2>1000 ; C2*0,05 ; 0 )
```

I les versions agregades, que són les que més s'usen en gestió:

```
=SUMA.SI( rang_condició ; condició ; rang_a_sumar )
=COMPTA.SI( rang ; condició )
=SUMA.SI.CONJUNT( rang_suma ; rang1 ; cond1 ; rang2 ; cond2 )
```

**Encadenar `SI` dins de `SI`** funciona però es fa il·legible a partir de tres nivells. Quan arribes ahí, el que necessites és una **taula de cerca**, no més `SI`.

### Cerca: la funció que canvia com treballes

El problema: tens un codi d'article i vols el seu preu, que està en una altra taula.

```
=CONSULTAV( valor_buscat ; taula ; columna ; 0 )
=CONSULTAV( A2 ; Catàleg.$A$2:$D$200 ; 3 ; 0 )
```

Quatre coses que has de recordar sempre:

1. **L'últim paràmetre `0`** (o `FALS`) vol dir coincidència exacta. Sense ell, busca aproximada i pot tornar el preu de l'article equivocat sense avisar.
2. **La taula ha d'anar amb referència absoluta** (`$`), o en copiar la fórmula es desplaçarà.
3. **El valor buscat ha d'estar a la primera columna** de la taula.
4. El resultat `#N/D` significa "no existeix eixe codi". És informació útil: normalment vol dir que algú ha escrit malament el codi.

**Alternativa més robusta**, disponible a les dues suites:

```
=INDEX( columna_resultat ; COINCIDIR( valor ; columna_cerca ; 0 ) )
```

No exigeix que la clau siga la primera columna i no es trenca si s'insereixen columnes enmig. Val la pena aprendre-la.

### Text

Les necessitaràs per a netejar dades importades a [A4](../activitats/A4_csv.md):

| Funció | Fa |
| --- | --- |
| `RETALLA(text)` | Lleva espais sobrants — **la més útil de totes** |
| `MAJUSC` / `MINUSC` / `NOMPROPI` | Canvia caixa |
| `CONCATENA` o `&` | Uneix textos |
| `ESQUERRA` / `DRETA` / `MIGCAD` | Extrau parts |
| `SUBSTITUEIX(text; buscar; nou)` | Reemplaça |
| `VALOR(text)` | Converteix text a número |

### Dates

```
=AVUI()                    data d'avui, s'actualitza
=DIA.LABORABLE(data; 30)   data + 30 dies laborables
=DATA.DIFF(inici; fi; "d") diferència en dies
```

## Com es construeix un full que no falla

Quatre principis. Els aplicaràs a totes les activitats de S4.

**1. Separa dades, càlculs i presentació.** Fulls diferents: `Dades`, `Config`, `Càlculs`, `Informe`. Barrejar-ho és el que fa que un full siga impossible de mantindre.

**2. Cap número dins d'una fórmula.** Si veus `*0,21` en una fórmula, eixe 0,21 ha d'estar a una cel·la amb nom del full `Config`. L'excepció són constants matemàtiques reals (dividir per 2 per a fer una mitjana de dos valors).

**3. Una fórmula per columna.** Totes les cel·les d'una columna de càlcul han de tindre **la mateixa fórmula** copiada. Si una és diferent, o és un error o és un pegat, i tots dos casos són problemes.

**4. Comprovacions visibles.** Una cel·la que verifique que el model quadra:

```
=SI( ARRODONEIX(total_calculat - suma_línies; 2)=0 ; "OK" ; "REVISAR" )
```

Un full professional es diagnostica sol.

## 🤖 IA i fórmules

És bona ajuda, amb dues condicions.

**Descriu el problema, no demanes la funció.** *"Tinc codis a la columna A i preus en un altre full; vull el preu al costat del codi"* dona millor resultat que *"com uso CONSULTAV"*.

**Prova-ho sempre amb un cas que sàpigues el resultat.** Les fórmules generades solen estar bé en l'estructura i malament en els detalls: rangs desplaçats una fila, `$` que falten, noms de funció de la versió anglesa.

!!! note "Noms de funció"
    Les fórmules tenen noms diferents en català, castellà i anglés (`CONSULTAV` / `BUSCARV` / `VLOOKUP`). La IA sol respondre en anglés. No és un error seu: és que has d'ajustar-ho.

## Comprova que ho tens

- [ ] Sé els sis errors i què indica cadascun.
- [ ] Sé quan té sentit `SI.ERROR` i quan és amagar un problema.
- [ ] Sé la diferència entre arrodonir i formatar, amb un exemple en diners.
- [ ] Sé fer un `CONSULTAV` amb coincidència exacta i rang absolut.
- [ ] Sé explicar per què `INDEX`+`COINCIDIR` és més robust.
- [ ] Sé els quatre principis de construcció d'un full mantenible.
