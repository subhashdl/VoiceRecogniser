#import speech_recognition as sr
#
#r = sr.Recognizer()
#
#with sr.Microphone() as source:
#    print('Say Something:')
#    audio = r.listen(source)
#    print ('Done!')
#
#text = r.recognize_google(audio, language = 'hi-IN')
#
#print (text)
#
#print (r.recognize_google(audio))



import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    print ('Done!')

text = r.recognize_google(audio, language = 'EN')
translator = Translator()
updatedText = translator.translate(text, dest='es')
print ("Original Text is : ",updatedText.origin)
print ("Converted Text is : ",updatedText.text)







