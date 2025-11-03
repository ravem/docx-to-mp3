from docx import Document
from gtts import gTTS
import re

def docx_to_text(docx_file):
    """Estrae tutto il testo da un file .docx, aggiungendo pause naturali tra paragrafi e punteggiatura."""
    doc = Document(docx_file)
    text = ''
    for paragraph in doc.paragraphs:
        line = paragraph.text.strip()
        if line:
            # Aggiunge micro-pause dopo la punteggiatura
            line = re.sub(r'([.,;:])', r'\1 …', line)
            
            # Aggiunge pause più lunghe tra paragrafi
            if len(line) < 50:
                text += line + '\n'       # breve pausa
            elif len(line) < 150:
                text += line + '\n\n'     # pausa media
            else:
                text += line + '\n\n\n'   # pausa lunga
    return text.strip()

def text_to_speech(text, output_file, language='it', slow=False):
    """Converte il testo in audio MP3 usando gTTS (lettura naturale e scorrevole)."""
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save(output_file)
    print(f"✅ Audio creato con successo: {output_file}")

if __name__ == "__main__":
    docx_file = "1.docx"      # Nome del tuo file Word
    output_file = "1.mp3"     # Nome del file audio di uscita

    # Estrai il testo con pause dinamiche e micro-pause
    text_content = docx_to_text(docx_file)

    # Converti in voce italiana, lettura più veloce e naturale
    text_to_speech(text_content, output_file, language='it', slow=False)
