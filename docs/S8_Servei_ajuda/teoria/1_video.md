# T1 · Vídeo: formats i còdecs

<span class="ca">CA a</span> <span class="ca">CA b</span>

## Els elements d'una seqüència

<span class="ca">CA a</span> Un vídeo és una seqüència d'imatges amb àudio sincronitzat. Els paràmetres que el defineixen:

| Element | Què és | Valors habituals |
| --- | --- | --- |
| **Resolució** | Píxels per fotograma | 1920×1080 (Full HD), 1280×720 |
| **Fotogrames per segon (fps)** | Imatges per segon | 25-30 per a tutorials · 50-60 per a moviment ràpid |
| **Relació d'aspecte** | Proporció | 16:9 |
| **Taxa de bits (bitrate)** | Dades per segon | Determina qualitat i pes |
| **Àudio** | Freqüència i canals | 48 kHz, estèreo o mono |
| **Durada** | | |

!!! tip "Per a un tutorial de pantalla, 25-30 fps sobren"
    Gravar a 60 fps duplica la mida del fitxer sense cap benefici: el cursor es mou igual de bé a 30.

    On sí importa: si graves un vídeo on es reprodueix una animació o un altre vídeo.

**Resolució de gravació = resolució de pantalla.** Si graves a 1920×1080 una pantalla de 1366×768, el vídeo s'escala i el text es fa borrós. I el text, en un tutorial, és tot.

## Contenidor ≠ còdec

<span class="ca">CA b</span> És la confusió que impedeix entendre per què un vídeo "no es veu".

**Contenidor** — la caixa. Guarda dins els fluxos de vídeo, àudio i subtítols. L'extensió del fitxer.

**Còdec** — l'algorisme que comprimeix i descomprimeix cada flux.

!!! example "Per què el teu vídeo no s'obri"
    Dos fitxers `.mp4` poden portar còdecs diferents dins. Si el reproductor del client no té el còdec, no reprodueix res — encara que l'extensió siga la mateixa que la d'un vídeo que sí li funciona.

    Per això no n'hi ha prou amb dir "t'envie un MP4". Cal saber què hi ha dins.

**Contenidors:**

| Contenidor | Nota |
| --- | --- |
| **MP4** | El més compatible. L'opció per defecte per a lliurar |
| MKV | Molt flexible, menys compatible amb reproductors antics |
| WEBM | Pensat per a web, lliure de patents |
| MOV | Ecosistema Apple |
| AVI | Antic |

**Còdecs de vídeo:**

| Còdec | Compatibilitat | Nota |
| --- | --- | --- |
| **H.264 / AVC** | **Universal** | L'aposta segura |
| H.265 / HEVC | Bona però no universal | Meitat de pes, més CPU |
| VP9 | Navegadors | Lliure de royalties |
| AV1 | Creixent | El futur, encara no per a lliurar a clients |

**Còdecs d'àudio:** **AAC** (l'estàndard amb MP4), MP3 (universal, antic), Opus (millor a baixa taxa), FLAC/WAV (sense pèrdua, per a treballar).

!!! success "La combinació que funciona sempre"
    **MP4 + H.264 + AAC.**

    Es reprodueix a qualsevol ordinador, mòbil, navegador i televisor dels últims quinze anys. Quan lliures a un client, això, i qualsevol altra cosa necessita justificació.

## Taxa de bits i qualitat

La **taxa de bits** és el factor que més determina qualitat i pes.

| Contingut | Taxa recomanada (1080p) |
| --- | --- |
| Captura de pantalla amb poc moviment | 2-4 Mbps |
| Vídeo normal | 8-12 Mbps |
| Molt moviment | 15-20 Mbps |

**CBR vs VBR:** taxa constant o variable. La variable (VBR) assigna més bits a les escenes complexes i menys a les simples. Per a un tutorial de pantalla, VBR estalvia molt pes.

**Compressió amb pèrdua i acumulació:** com amb el JPG de [S5](../../S5_Imatge_empresa/teoria/1_formats.md), cada recompressió degrada. Edita des de l'original i exporta una sola vegada.

## Còdecs i llicències

Alguns còdecs estan coberts per patents. H.264 i H.265 tenen consorcis de llicència; VP9 i AV1 són lliures de royalties.

Per a l'ús que en farem no té implicacions pràctiques, però és exactament el tipus de detall que has d'haver mirat abans de recomanar una eina a un client — la mateixa lògica de [S1/T2](../../S1_Posada_marxa/teoria/2_llicencies.md).

## Accessibilitat

Un vídeo sense subtítols exclou persones amb discapacitat auditiva i tothom que el veja sense so.

- **Subtítols incrustats** (*hardcoded*) — dibuixats sobre la imatge, no es poden desactivar
- **Subtítols en fitxer** (`.srt`, `.vtt`) — separats, es poden activar i traduir. **Preferibles**

Per a documentació d'una administració pública, els subtítols són **obligatoris**.

## Comprova que ho tens

- [ ] Sé els sis paràmetres que defineixen una seqüència.
- [ ] Sé explicar la diferència entre contenidor i còdec amb un exemple.
- [ ] Sé quina combinació lliurar a un client i per què.
- [ ] Sé per què no es grava a 60 fps un tutorial de pantalla.
- [ ] Sé per què s'edita des de l'original i s'exporta una sola vegada.
- [ ] Sé la diferència entre subtítols incrustats i en fitxer.
