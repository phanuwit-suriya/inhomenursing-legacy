import os
import time
import speech_recognition as sr
from gtts import gTTS

tmp = "C:/Users/Effigy/Desktop/in-home-nursing/tmp"

def voice():
    os.chdir(tmp)
    pass


def speak(text):
    tts = gTTS(text=text)
    tts.save("{}/{}.mp3".format(tmp, text.replace(" ", "")))
    os.system("{}/{}.mp3".format(tmp, text.replace(" ", "")))


def recognizer(lang='en-US'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        return(r.recognize_google(audio, language=lang).lower())
    except sr.UnknownValueError:
        # print('Sorry about that, I didn\'t hear anything')
        print("Recognizer could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {}".format(e))
