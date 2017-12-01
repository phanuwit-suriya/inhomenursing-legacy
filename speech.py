import os
import time
import speech_recognition as sr
from gtts import gTTS

tmp = "C:/Users/Effigy/Desktop/tmp"
path = "C:/Users/Effigy/Desktop/"


def speaker(text):
    tts = gTTS(text=text)
    tts.save('{}/{}.mp3'.format(tmp, text.replace(" ", "")))
    os.system('{}/{}.mp3'.format(tmp, text.replace(" ", "")))


def recognizer():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print('Recognizer thinks you said: {}'.format(r.recognize_google(audio)))
        return(r.recognize_google(audio))
    except sr.UnknownValueError:
        print('Recognizer could not understand audio')
    except sr.RequestError as e:
        print(
            'Could not request results from Google Speech Recognition service; {}'.format(e))
