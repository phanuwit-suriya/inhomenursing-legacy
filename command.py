import os
import time
import random
import datetime
import requests

import speech
from database import routine_search


def bye():
    response = {1: 'You\'re welcome', 2: 'I\'m happy to help', 3: 'It\'s my pleasure',
                4: 'I\'m glad to help', 5: 'No trouble at all', 6: 'Don\'t mention it'}
    print(response[random.randint(1, 6)])
    # speech.speaker("you're welcome")


def askTime():
    clocktime = datetime.datetime.now().strftime("%H %M %p")
    speech.speaker("the time is {}".format(clocktime))
    print(clocktime)


def askDate():
    date = datetime.datetime.now().strftime("%A %d %B %Y")
    speech.speaker("today is {}".format(date))
    print(date)


def askFood():
    print("Today's meal")
    routine_search(time.strftime("%Y%m%d"))


def askWeather():
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=Bangkok,TH&APPID=52a601a7b6e589c3e9b7d18ee259b1be")
    weather = r.json()
    temperature = weather["main"]["temp"] - 273.15
    humidity = weather["main"]["humidity"]
    speech.speaker("The weather in Bangkok right now is {} degree celsius with {} percent of himidity".format(
        str(round(temperature, 1)), str(humidity)))


def setalarm():
    pass


def setTimer():
    pass


def command(command=''):
    if any(word in command for word in ["thanks", "thank you"]):
        bye()
        return False
    elif any(word in command for word in ["good morning", "good afternoon", "good evening"]):
        pass
    elif command == "what time is it":
        askTime()
    elif command == "what day is today":
        askDate()
    elif command == 'what did i eat today':
        askFood()
    elif all(word in command for word in ["what", "weather"]) or all(word in command for word in["how", "weather"]):
        askWeather()
    elif command == "set alarm":
        pass
    elif command == "set timer":
        pass

    return True

'''
def command(command):
    if command.split()[0] == 'open':
        open()
    elif command.split()[0:2] == ['go', 'to']:
        goto()
    elif setlarm:
        setalarm()
    elif settimer:
        settimer()
    elif

'''
