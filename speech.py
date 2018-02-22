import os
import time
import threading
from threading import Thread

import speech_recognition as sr
from gtts import gTTS

tmp = "C:/Users/Effigy/Desktop/in-home-nursing/tmp"


def voice():
    pass


def speak(text):
    tts = gTTS(text=text)
    tts.save("{}/{}.mp3".format(tmp, text.replace(" ", "")))
    os.system("{}/{}.mp3".format(tmp, text.replace(" ", "")))


def recognizer():
    class Confidence(threading.Thread):
        def __init__(self, )
    # def find_confidence(language):
    #     return r.recognizer_google(audio, language=language, show_all=True)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        # th_results = Thread(target=find_confidence, args("th-TH", ))
        # us_results = Thread(target=find_confidence, args("en-US", ))

        # th_results.start()
        # us_results.start()

        # th_results.join()
        # us_results.join()

        # if th_results['alternative'][0]['confidence'] > us_results['alternative'][0]['confidence']:
        #     return th_results['alternative'][0]['transcript']
        # else:
        #     return us_results['alternative'][0]['transcript']

        return(r.recognize_google(audio, language="en-US"))
    except sr.UnknownValueError:
        # print('Sorry about that, I didn\'t hear anything')
        print("Recognizer could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
