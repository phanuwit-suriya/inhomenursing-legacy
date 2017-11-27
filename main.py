import os
import time
import datetime

import database
import speech
import command

active_word = 'listening'
active_cmd = False

breakfast = False
lunch = False
dinner = False

setAlarm = False

speech.speaker("Program has started")
time.sleep(2)
speech.speaker("Speak listening before giving command")
time.sleep(3)
while True:
    now = datetime.datetime.now()
    if now.hour == 0:
        breakfast = False
        lunch = False
        dinner = False

    if not (breakfast or lunch or dinner):
        if not breakfast and now.hour == 10:
            print('Breakfast')
            food = speech.recognizer()
            breakfast = database.search(food)
            if breakfast:
                database.insert_routine(time.strftime("%Y%m%d%H%M%S"), food)
            else:
                pass
        elif not lunch and now.hour == 14:
            print('Lunch')
            food = speech.recognizer()
            lunch = database.search(food)
            if lunch:
                database.insert_routine(time.strftime("%Y%m%d%H%M%S"), food)
            else:
                pass
        elif not dinner and now.hour == 21:
            print('Dinner')
            food = speech.recognizer()
            dinner = database.search(food)
            print(dinner)
            if dinner:
                database.insert_routine(time.strftime("%Y%m%d%H%M%S"), food)
            else:
                pass

    word = speech.recognizer()
    if word == active_word:
        active_cmd = True
        speech.speaker('what can i do for you')
        while active_cmd:
            cmd = speech.recognizer()
            active_cmd = command(cmd)
    else:
        print("Speak \"listening\" before giving commands")
