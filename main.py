import os
import time
import datetime

import database
import speech
from command import command


active_word = 'listening'
breakfast = False
lunch = False
dinner = False

print('Program has started')
while True:
    now = datetime.datetime.now()
    if now.hour == 0:
        breakfast = False
        lunch = False
        dinner = False

    if not (breakfast or lunch or dinner):
        if not breakfast and now.hour == 12:
            print('Breakfast')
            food = speech.recognizer()
            breakfast = database.search(food)
            if breakfast:
                database.insert_routine(time.strftime("%Y%m%d%H%M%S"), food)
        elif not lunch and now.hour == 14:
            print('Lunch')
            food = speech.recognizer()
            lunch = database.search(food)
            if lunch:
                database.insert_routine(time.strftime("%Y%m%d%H%M%S"), food)
        elif not dinner and now.hour == 20:
            print('Dinner')
            food = speech.recognizer()
            dinner = database.search(food)
            if dinner:
                database.insert_routine(time.strftime("%Y%m%d%H%M%S"), food)

    print('Speak "listening" before giving command')
    word = speech.recognizer()

    if word == active_word:
        speech.sound('what can i do for you')
        while True:
            cmd = speech.recognizer()
            command(cmd)
    else:
        pass
