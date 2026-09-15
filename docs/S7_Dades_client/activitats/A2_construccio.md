# A2 · Construïm la base de dades

**Sessions 8 i 9** · lliurament: fitxer `.odb` + informe de càrrega
**Avalua:** RA4 <span class="ca">b</span> <span class="ca">c</span>

## L'encàrrec

<div class="encarrec" markdown>
<p class="meta">De: Gestoria Bellver · Per a: la vostra empresa</p>

Hem llegit el seu informe i estem d'acord amb el model.

Sobre els dubtes que ens plantejaven: les tres "Ferreteries Bellver" són la mateixa empresa. Els dos expedients sense client són d'un client que va causar baixa el 2024 i que volem conservar. I els imports negatius són abonaments, no errors.

Endavant.
</div>

## Part 1 · Construir l'estructura

<span class="ca">CA b</span> Implementa el model d'[A1](A1_model.md) a LibreOffice Base.

- [ ] Totes les taules del model, amb els tipus del diccionari de dades
- [ ] Claus primàries **autonumèriques**
- [ ] Restriccions `NOT NULL` i `UNIQUE` on tocava
- [ ] Valors per defecte on tenien sentit
- [ ] Relacions definides amb **integritat referencial** activada
- [ ] Regles d'esborrat segons les decisions d'A1
- [ ] Taula intermèdia de la relació N a N funcionant

### Les proves d'integritat

**Demostra que les restriccions funcionen.** Intenta fer estes quatre coses i documenta amb captures què passa:

| Prova | Resultat esperat |
| --- | --- |
| Inserir un expedient amb un `id_client` que no existeix | Rebutjat |
| Deixar buit un camp `NOT NULL` | Rebutjat |
| Duplicar un valor `UNIQUE` | Rebutjat |
| Esborrar un client que té expedients | Segons la teua regla |

!!! tip "Si alguna prova no falla, la restricció no està posada"
    És la manera més ràpida de comprovar que has configurat el que creus que has configurat. Molta gent defineix la relació i oblida marcar la casella d'integritat referencial.

## Part 2 · Carregar les dades

<span class="ca">CA c</span> El procés de [T2](../teoria/2_taules.md), pas a pas, documentat.

1. Neteja al full de càlcul (tècniques de [S4](../../S4_Control_economic/index.md))
2. Separació en fulls per taula
3. **Assignació d'identificadors** als clients reals
4. Substitució dels textos per identificadors a les taules de detall
5. Importació en ordre de dependència
6. Verificació

### L'informe de càrrega

| Taula | Registres origen | Registres carregats | Diferència | Motiu de la diferència |
| --- | --- | --- | --- | --- |

**Tota diferència s'ha d'explicar.** Si de 247 files n'han entrat 243, has de saber on són les altres quatre i per què.

### L'informe de decisions de fusió

Per als duplicats:

| Registres fusionats | Criteri usat | Confirmat pel client? | Dades conservades |
| --- | --- | --- | --- |

!!! danger "La fusió és irreversible"
    Fes **còpia de seguretat del fitxer original** abans de començar i conserva'l al [portafoli](../../recursos/portafoli.md).

    Si d'ací a tres mesos es descobreix que dos clients fusionats eren empreses diferents, l'única manera de desfer-ho és tindre l'original.

## Part 3 · Operacions sobre les dades

<span class="ca">CA c</span> Demostra les tres operacions, cadascuna amb evidència:

- **Inserir:** tres registres nous, un a cada taula, incloent-hi un que use la relació
- **Modificar:** actualitzar les dades d'un client i comprovar que els seus expedients continuen vinculats
- **Esborrar:** aplicar la política d'esborrat decidida (probablement marcar com a inactiu en lloc d'esborrar) i explicar per què

## Com s'avalua

### RA4.b) Base de dades creada — 55 %

- 🟢 Estructura fidel al model d'A1, amb tipus correctes, totes les restriccions actives i **les quatre proves d'integritat documentades i fallant com toca**. Relació N a N funcionant. Regles d'esborrat coherents amb el que es va decidir i confirmar amb el client.
- 🔵 Estructura correcta i relacions definides, però alguna restricció absent o alguna prova d'integritat no documentada.
- 🟡 Taules creades però sense integritat referencial activa, o amb tipus incorrectes (imports en `FLOAT`, dates com a text).
- 🔴 Una sola taula que reprodueix el full original, o relacions inexistents.

### RA4.c) Taules utilitzades — 45 %

- 🟢 Càrrega completa amb informe que **quadra**: tota diferència entre origen i destí explicada. Decisions de fusió documentades amb criteri i amb la confirmació del client. Les tres operacions demostrades amb evidència. Còpia de l'original conservada.
- 🔵 Càrrega correcta i operacions demostrades, però alguna diferència de recompte sense explicar del tot, o les decisions de fusió documentades sense criteri explícit.
- 🟡 Dades carregades sense verificar recomptes, o duplicats fusionats sense documentar-ho.
- 🔴 Pèrdua de registres no detectada, o dades introduïdes a mà en lloc de carregades, o fusions fetes sense la confirmació del client.

!!! quote "Punt de comprensió"
    *"Quants registres hi havia al fitxer original i quants n'hi ha ara? Si no coincideix, on són els que falten?"*

    És la primera pregunta que fa qualsevol responsable en una migració de dades, i la que més sovint no té resposta.
