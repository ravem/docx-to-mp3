# Docx-to-Audio

Docx-to-Audio è uno script Python che legge un file Word (`.docx`) e lo converte in audio MP3 con voce italiana naturale. 
Lo script include pause dinamiche tra paragrafi e micro-pause dopo la punteggiatura principale (`.`, `,`, `;`, `:`), rendendo la lettura più scorrevole e simile a quella di una persona.

## Caratteristiche

- Estrazione automatica del testo dai file `.docx`.
- Conversione del testo in voce italiana utilizzando `edge-TTS`.
- Lettura naturale con pause dinamiche tra paragrafi e micro-pause dopo punteggiatura.
- Velocità di lettura regolabile (tramite il parametro `rate`).

## Requisiti

- Python 3.7 o superiore.
- Moduli Python necessari:
  - `python-docx` (per leggere file Word)
  - `edge-tts` (per la conversione in audio MP3)

### Installazione dei moduli

```bash
pip install python-docx edge-tts 
```

## Utilizzo

Posizionare il file .docx nella stessa cartella dello script.
Aggiornare il nome o il percorso dei file di input e output nello script, se necessario.

## Opzioni
Velocità di lettura: modificabile 
Pause tra paragrafi: dinamiche in base alla lunghezza del paragrafo.
Micro-pause: inserite automaticamente dopo la punteggiatura principale per una lettura più naturale.

Per eseguire lo script, scaricalo e eseguilo con:
```bash
python docx_to_audio.py
```
