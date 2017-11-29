import os
import time
import random
import datetime
import requests
import threading

import speech
from database import routine_search


class Alarm:

    def __init__(self, duration):
        pass


class Timer:

    def __init__(self, duration):
        self.duration = duration
        self.unit = unit
        if any(word in self.unit for word in ['minute', 'minutes']):
            self.duration *= 60
        elif any(word in self.unit for word in ['hour', 'hours']):
            self.duration *= 3600
        self.t = threading.Timer(self.duration, self.ring)

    def ring(self):
        print('Ring! Ring!\n' * 3)
        return self.t.cancel()

    def start_timer(self):
        self.settimer = int(time.time())
        return self.t.start()

    def cancel_timer(self):
        return self.t.cancel()

    def check_timer(self):
        self.time_left = self.duration - (int(time.time()) - self.settimer)
        return 'Timer left: {}'.format(self.time_left)


def bye():
    response = {1: 'You\'re welcome', 2: 'I\'m happy to help', 3: 'It\'s my pleasure',
                4: 'I\'m glad to help', 5: 'No trouble at all', 6: 'Don\'t mention it'}
    print(response[random.randint(1, 6)])
    # speech.speaker("you're welcome")


def ask_time():
    clocktime = datetime.datetime.now().strftime("%H %M %p")
    speech.speaker('the time is {}'.format(clocktime))
    print(clocktime)


def ask_date():
    date = datetime.datetime.now().strftime('%A %d %B %Y')
    speech.speaker('today is {}'.format(date))
    print(date)


def ask_food():
    print('List of today\'s foods')
    routine_search(time.strftime("%Y%m%d"))


def ask_weather():
    r = requevit_ksts.get(
        'https://api.openweathermap.org/data/2.5/weather?q=Bangkok,TH&APPID=52a601a7b6e589c3e9b7d18ee259b1be')
    weather = r.json()
    temperature = weather['main']['temp'] - 273.15
    humidity = weather['main']['humidity']
    speech.speaker('The weather in Bangkok right now is {} degree celsius with {} percent of himidity'.format(
        str(round(temperature, 1)), str(humidity)))


def command(command=''):
    if any(word in command for word in ['thanks', 'thank you']):
        bye()
        return False
    # elif any(word in command for word in ['good morning', 'good afternoon', 'good evening']):
    #     pass
    elif command == 'what time is it':
        ask_time()
    elif command == 'what day is today':
        ask_date()
    elif command == 'what did i eat today':
        ask_food()
    elif all(word in command for word in ['what', 'weather']) or all(word in command for word in['how', 'weather']):
        ask_weather()
    elif all(word in command for word in ['set', 'alarm']):
        pass
    elif any(string in command for string in ['set timer', 'set a timer']):
        speech.speaker('how long should i set a timer?')
        duration = speech.recognizer()
        try
    return True
