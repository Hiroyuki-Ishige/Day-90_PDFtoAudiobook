from gtts import gTTS
from playsound import playsound

audio ="speech.mp3"
language ="en"

with open("text.txt", mode="r") as f:
    text = f.read()

speech = gTTS(
                text=text,
                lang=language)

speech.save(audio)
playsound(audio)

#TODO extract text from PDF file
#TODO Read text from PDF file
#TODO send API request

