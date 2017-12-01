import time
import datetime

import database
import speech
from command import command


def meal(food):
    eat_food = database.nutrition_search(food)
    if eat_food:
        database.insert_routine(time.strftime('%Y%m%d%H%M%S'), food)
        return eat_food
    else:
        return eat_food

active_word = 'listening'
active_cmd = True

breakfast = False
lunch = False
dinner = False

print('Program has started')
# speech.speaker('Program has started. Speak listening before giving commands')
while True:
    now = datetime.datetime.now()
    # RESET MEAL EVERY MIDNIGHT
    if now.hour == 0:
        breakfast = False
        lunch = False
        dinner = False

    # CHECK IF EACH MEAL HAS BEEN EATEN
    if not (breakfast or lunch or dinner):
        if not breakfast and (now.hour == 10) and (now.minute % 15 == 0):
            print('Breakfast')
            food = speech.recognizer()
            if food == None:
                pass
            else:
                breakfast = meal(food)
        elif not lunch and (now.hour == 14) and (now.minute % 15 == 0):
            print('Lunch')
            food = speech.recognizer()
            if food == None:
                pass
            else:
                lunch = meal(food)
        elif not dinner and (now.hour == 20) and (now.minute % 15 == 0):
            print('Dinner')
            food = speech.recognizer()
            if food == None:
                pass
            else:
                dinner = meal(food)

    # SPEAK 'LISTENING' TO ACTIVATE
    print('Speak listening before giving commands')
    word = speech.recognizer()
    if word == active_word:
        active_cmd = True
        count = 3
        print('What can i do for you?')
        # TRY TO CATCH PHRASE TIL COUNT IS ZERO
        # IF COUNT IS ZERO, SPEAK 'LISTENING' AGAIN
        while active_cmd:
            try:
                cmd = speech.recognizer()
                if cmd == None:
                    count -= 1
                    if count == 0:
                        active_cmd = False
                else:
                    active_cmd = command(cmd.lower())
                    count = 3
            except TypeError:
                pass
