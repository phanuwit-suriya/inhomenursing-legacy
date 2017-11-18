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


print("Recognizer has started")

activate_word = 'listening'

r = sr.Recognizer()

with sr.Microphone() as source1:
    print("Speak 'listening' to start")
    while True:
        time.sleep(1
        print("Speak now")
        audio1=r.listen(source1)
        words=recognizer(audio1)
        print("You said: {}".format(words))
        if activate_word in words:
            with sr.Microphone() as source2:
                finish=False
                while not finish:
                    time.sleep(1)
                    print("What can i help you?")
                    audio2=r.listen(source2)
                    command=recognizer(audio2)
                    print("Your command is: {}".format(command))
                    if not command == '':
                        finish=commands.main(command)
                    else:
                        break
        elif words == "":
            print("Speak 'listening' before giving command")
        elif words == "stop":
            break


# def recognizer():
#     # Input from microphone
#     with sr.Microphone() as source:
#         audio = r.listen(source)

#     text = r.recognize_google(audio)
#     print("You said: {} ".format(text))
#     if text.find(activate_word) != -1:
#         try:
#             commands.main(text)
#         except sr.UnknownValueError:
#             print("Could not understand audio ")
#         except sr.RequestError as e:
#             print("Could not request results; {} ".format(e))
#     else:
#         pass

#     while True:
#         try:
#             recognizer()
#         except Exception as e:
#             print(e)
