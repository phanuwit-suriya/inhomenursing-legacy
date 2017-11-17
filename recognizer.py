import os
import time
import commands
import speech_recognition as sr

def recognizer():
    AUDIO_FILE = "C:/Users/Effigy/Desktop/speech_recognition/commands/"

    r = sr.Recognizer()

    # Input from existed file
    # with sr.AudioFile(AUDIO_FILE + 'openmusicplayer.wav') as source:
    #     audio = r.record(source)

    # Input from microphone
    with sr.Microphone() as source:
        audio = r.listen(source)

    text = r.recognize_google(audio)
    if text == 'okay, google':
        try:
            print("You said: {} ".format(text))
            commands.main(text)
        except sr.UnknownValueError:
            print("Could not understand audio ")
        except sr.RequestError as e:
            print("Could not request results; {} ".format(e))
    else:
        pass

while True:
    try:
        recognizer()
    except Exception as e:
        print(e)
