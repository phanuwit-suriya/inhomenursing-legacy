import os
import time
import commands
import speech_recognition as sr


def recognizer(audio):
    try:
        return r.recognize_google(audio)
    except Exception as e:
        print(e)
        return ''

activate_word = 'start listening'

r = sr.Recognizer()

with sr.Microphone() as source1:
    while True:
        time.sleep(1)
        audio1 = r.listen(source1)
        words = recognizer(audio1)
        print("You said: {}".format(words))
        if 'start listening' in words:
            with sr.Microphone() as source2:
                audio2 = r.listen(source2)
                command = recognizer(audio2)
                print("Your command is: {}".format(command))
                if not command == '':
                    finish = commands.main(command)
                else:
                    pass
        elif words == '':
            print('Speak "listening" before giving command')
        elif words == 'stop':
            break


# def recognizer():
    # # Input from microphone
    # with sr.Microphone() as source:
    #     audio = r.listen(source)

    # text = r.recognize_google(audio)
    # print("You said: {} ".format(text))
    # if text.find(activate_word) != -1:
    #     try:
    #         commands.main(text)
    #     except sr.UnknownValueError:
    #         print("Could not understand audio ")
    #     except sr.RequestError as e:
    #         print("Could not request results; {} ".format(e))
    # else:
    #     pass

    # while True:
    #     try:
    #         recognizer()
    #     except Exception as e:
    #         print(e)
