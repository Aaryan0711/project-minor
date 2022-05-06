from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'
language = 'en'
sp = gTTS(text="Hello Aaditya singh. How are you.I am here to help you. Kindly mention your name.",lang=language,slow=False)

playsound(audio)
sp.save(audio)