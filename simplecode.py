from gtts import gTTS 
import os

text="hello world i'm optimus prime"

lang= 'en'

speech = gTTS(text=text, lang = lang,slow=False)

speech.save("hello.mp3")

os.system("start hello.mp3")