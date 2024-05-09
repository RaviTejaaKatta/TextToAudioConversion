import os
from gtts import gTTS
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")
text = "well hello there"
text_to_speech(text)