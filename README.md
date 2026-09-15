# Aplicacions Ofimàtiques · 1r SMX · 2026-2027

Materials del mòdul **0223 · Aplicacions Ofimàtiques** (Sistemes Microinformàtics i Xarxes),
organitzats en 8 situacions professionals.

Web: https://SAMUELVIEL.github.io/AOF_SMX_2627/

---

## Posar-ho en marxa a GitHub Pages

### 1. Personalitza

Edita `mkdocs.yml` i substitueix `SAMUELVIEL` i `AOF_SMX_2627` pel teu usuari i el nom
real del repositori, a les tres línies: `site_url`, `repo_url` i la de `extra.social`.

### 2. Crea el repositori i puja

```bash
git init
git add .
git commit -m "Curs AOF 1r SMX 2026-27"
git branch -M main
git remote add origin https://github.com/USUARI/REPOSITORI.git
git push -u origin main
```

### 3. Activa Pages

Al repositori: **Settings → Pages → Source → GitHub Actions**.

El workflow `.github/workflows/deploy.yml` publica sol amb cada `push` a `main`.
El primer desplegament tarda un parell de minuts.

---

## Treballar-hi en local

```bash
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build --strict  # comprova que no hi ha enllaços trencats
```

`--strict` falla si hi ha cap enllaç intern trencat. El workflow l'usa, així que
si el build local passa, el desplegament també.

---

## El calendari

Tot el calendari del curs es genera des d'un sol fitxer.

```bash
python3 tools/calendari.py             # resum per avaluacions i situacions
python3 tools/calendari.py --detall    # totes les sessions
python3 tools/calendari.py --md S4     # taula markdown d'una situació
python3 tools/gen_calendari_md.py      # regenera docs/recursos/calendari.md
```

**Per a adaptar-lo**, edita el bloc `CONFIGURACIÓ` de `tools/calendari.py`:

| Variable | Què és |
| --- | --- |
| `HORARI` | Hores per dia de la setmana (0 = dilluns) |
| `TRAMS` | Franja horària de cada dia |
| `INICI` / `FINAL` | Primera i última sessió |
| `AVALUACIONS` | Dates de les tres avaluacions |
| `PERIODES` | Vacances i FEE |
| `FESTIUS` | Festius solts |
| `SITUACIONS` | Sessions assignades a cada situació |

L'script avisa si les sessions assignades no caben. Després de tocar-lo,
executa `gen_calendari_md.py` i actualitza les taules de calendari dels
`index.md` de les situacions afectades.

**Estat actual:** 125 sessions · 218 h · 6 sessions de marge.

---

## Estructura

```
docs/
├── index.md                  Portada: com funciona el curs
├── about.md                  Autoria, llicència, reconeixements
├── recursos/
│   ├── avaluacio.md          Sistema d'avaluació, pesos per RA
│   ├── ia.md                 Protocol d'ús de la IA
│   ├── portafoli.md          Organització del portafoli
│   ├── mesa_ajuda.md         El RA9 com a servei transversal
│   └── calendari.md          Generat automàticament
├── S0_Fundacio/              Fundació de l'empresa (2 sessions)
├── S1_Posada_marxa/          RA1 · instal·lació i llicències
├── S2_Identitat_documental/  RA2 · processador de textos
├── S3_Comunicacio_agenda/    RA8 · correu i agenda · projecte 1
├── S4_Control_economic/      RA3 · full de càlcul
├── S5_Imatge_empresa/        RA5 · imatge digital
├── S6_Presentem_empresa/     RA7 · presentacions · projecte 2
├── S7_Dades_client/          RA4 · bases de dades
└── S8_Servei_ajuda/          RA6 + RA9 · vídeo i suport · projecte 3
```

Cada situació: `index.md` (encàrrec, calendari, RA/CA, lliuraments)
+ `teoria/` + `activitats/` amb rúbrica per CA.

---

## Pesos dels RA

| RA | Contingut | Situació | Pes |
| --- | --- | --- | --- |
| RA1 | Instal·lació d'aplicacions | S1 | 8 % |
| RA2 | Processador de textos | S2 | 18 % |
| RA3 | Full de càlcul | S4 | 20 % |
| RA4 | Bases de dades | S7 | 14 % |
| RA5 | Imatge digital | S5 | 8 % |
| RA6 | Vídeo | S8 | 8 % |
| RA7 | Presentacions | S6 | 10 % |
| RA8 | Correu i agenda | S3 | 7 % |
| RA9 | Suport a usuaris | Transversal + S8 | 7 % |

Cal un 5 en **cada** RA per a superar el mòdul.

---

## Pendent d'ajustar abans de començar

- [ ] Usuari i repositori a `mkdocs.yml`
- [ ] Verificar dates de festius contra el calendari oficial del centre
- [ ] Confirmar dates exactes de la FEE (previstes: 24/05 → 17/06/2027, 4 últimes setmanes)
- [ ] Preparar els materials d'aula que les activitats donen per suposats:
      volcat de 40 correus (S3/A2), històric de facturació (S4/A3),
      CSV brut del proveïdor (S4/A4), fulls de la gestoria (S7/A1),
      catàleg d'avaries (S1/A4)
- [ ] Decidir l'eina de mecanografia i crear el grup
- [ ] Muntar el full compartit de tiquets de la mesa d'ajuda

---

## Llicència

Continguts sota [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Enfocament metodològic inspirat en el treball d'[Alfredo Beneto](https://abeneto.github.io/AOF_2627/).
