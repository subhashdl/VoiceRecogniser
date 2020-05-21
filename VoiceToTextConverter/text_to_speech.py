#pip install speech
#pip istall gtts
#pip install googletrans

from gtts import gTTS
from googletrans import Translator
import speech_recognition as sr
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    print ('Done!')

text = r.recognize_google(audio, language = 'es')
translator = Translator()
language = 'EN'
updatedText = translator.translate(text, dest=language)

mytext = updatedText.text

myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3")
os.system("welcome.mp3")
