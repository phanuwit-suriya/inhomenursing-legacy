import os
import time
import datetime
import requests

import speech


def finish():
    speech.speaker("you're welcome")


def clocktime():
    clocktime = datetime.datetime.now().strftime("%H %M %p")
    speech.speaker("the time is {}".format(clocktime))
    print(clocktime)


def date():
    date = datetime.datetime.now().strftime("%A %d %B %Y")
    speech.speaker("today is {}".format(date))
    print(date)


def weather():
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=Bangkok,TH&APPID=52a601a7b6e589c3e9b7d18ee259b1be")
    weather = r.json()
    temperature = weather["main"]["temp"] - 273.15
    humidity = weather["main"]["humidity"]
    speech.speaker("The weather in Bangkok right now is {} degree celsius with {} percent of himidity".format(
        str(round(temperature, 1)), str(humidity)))


def command(command=""):
    print(command)
    if any(word in command for word in ["thanks", "thank you"]):
        finish()
        return True
    if command == "what time is it":
        clocktime()
    if command == "what day is today":
        date()
    if all(word in command for word in ["what", "weather"]):
        weather()

    return False
