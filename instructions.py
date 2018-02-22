import datetime
import os
import random
import requests
import time

import speech
from timer import Timer
from database import routine_search


def bye():
    resp = [
        "You're welcome",
        "I'm happy to hepl",
        "It's my pleasure",
        "I'm glad to help",
        "No trouble at all",
        "Don't mention it"
    ]
    return random.choice(resp)


def ask_time():
    clocktime = datetime.datetime.now().strftime("%H %M %p")
    speech.speak("the time is {}".format(clocktime))
    print(clocktime)


def ask_date():
    date = datetime.datetime.now().strftime("%A %d %B %Y")
    speech.speak("today is {}".format(date))
    print(date)


def ask_food():
    print("List of today's foods")
    routine_search(time.strftime("%Y%m%d"))


def ask_weather():
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=Bangkok,TH&APPID=52a601a7b6e589c3e9b7d18ee259b1be")
    weather = r.json()
    temperature = weather["main"]["temp"] - 273.15
    humidity = weather["main"]["humidity"]
    speech.speak("The weather in Bangkok right now is {} degree celsius with {} percent of himidity".format(
        str(round(temperature, 1)), str(humidity)))


def instructions(command=""):
    if any(word in command for word in ["thanks", "thank you"]):
        bye()
        return False
    elif command == "what time is it":
        ask_time()
    elif command == "what day is today":
        ask_date()
    elif command == "what did i eat today":
        ask_food()
    elif all(word in command for word in ["what", "weather"]) or all(word in command for word in["how", "weather"]):
        ask_weather()
    elif all(word in command for word in ["set alarm"]):
        print("Set your alarm for what time?")
        duration = speech.recognizer()
        if duration is not None:
            try:
                pass
            except Exception as e:
                print(e)
    elif any(string in command for string in ["set timer", "set a timer"]):
        print("How long should i set a timer?")
        duration = speech.recognizer()
        global TIMER
        if duration is not None:
            try:
                TIMER = Timer(duration)
                TIMER.start_timer()
            except Exception as e:
                print(e)
    elif any(string in command for string in ["cancel timer", "cancel a timer"]):
        try:
            print(TIMER.cancel_timer())
        except Exception as e:
            print(e)
            print("Sorry, I don't have a timer set for you")
    elif any(string in command for string in ["check timer", "check a timer"]):
        try:
            print(TIMER.check_timer())
        except Exception as e:
            print(e)
            print("Sorry, I don't have a timer set for you")
    return True
