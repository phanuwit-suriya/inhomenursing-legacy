import time
import datetime

import speech
import database
import instructions


def meal(food):
    eat_food = database.nutrition_search(food)
    if eat_food:
        database.insert_routine(time.strftime('%Y%m%d%H%M%S', food))
        return eat_food
    else:
        return eat_food


if __name__ == "__main__":
    active_word = "listening"
    active = True

    breakfast = False
    lunch = False
    dinner = False

    print("Program has started")
    while True:
        now = datetime.datetime.now()
        # RESET MEAL EVERY MIDNIGHT
        if now.hour == 0:
            breakfast = False
            lunch = False
            dinner = False

        # CHECK IF EACH MEAL HAS BEEN EATEN
        if not (breakfast or lunch or dinner):
            # QUESTION BREAKFAST BETWEEN 8 AM AND 9 AM EVERY 15 MINUTES
            if not breakfast and (now.hour == 10) and (now.minute % 15 == 0):
                print("Breakfast")
                food = speech.recognizer()
                if food == None:
                    pass
                else:
                    breakfast = meal(food)
            # QUESTION LUNCH BETWEEN 2 PM AND 3 PM EVERY 15 MINUTES
            elif not lunch and (now.hour == 14) and (now.minute % 15 == 0):
                print("Lunch")
                food = speech.recognizer()
                if food == None:
                    pass
                else:
                    lunch = meal(food)
            # QUESTION DINNER BETWEEN 8 PM AND 9 PM EVERY 15 MINUTES
            elif not dinner and (now.hour == 20) and (now.minute % 15 == 0):
                print("Dinner")
                food = speech.recognizer()
                if food == None:
                    pass
                else:
                    dinner = meal(food)

        # SPEAK 'LISTENING' TO ACTIVATE
        print("Speak listening before giving commands")
        word = speech.recognizer()
        if word == active_word:
            active = True
            count = 3
            print("What can i do for you?")
            # TRY TO CATCH PHRASE TIL COUNT IS ZERO
            # IF COUNT IS ZERO, SPEAK "LISTENING" AGAIN
            while active:
                try:
                    string = speech.recognizer().lower()
                    if string == None:
                        count -= 1
                        if count == 0:
                            active = False
                    else:
                        active = command(cmd.lower())
                        count = 3
                except TypeError:
                    pass
