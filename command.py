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
        self.duration = int(duration.split()[0])
        self.unit = duration.split()[1]
        if any(word in self.unit for word in ['minute', 'minutes']):
            self.duration *= 60
        elif any(word in self.unit for word in ['hour', 'hours']):
            self.duration *= 3600
        self.t = threading.Timer(self.duration, self.ring)

    def ring(self):
        print('Ring! Ring!\n' * 3)
        return self.t.cancel()

    def start_timer(self):
        print('Starting a count down at {} {}'.format(self.duration, self.unit))
        self.settimer = int(time.time())
        return self.t.start()

    def cancel_timer(self):
        self.hour_left, self.min_left, self.sec_left = '0'
        print('Cancelled your timer')
        return self.t.cancel()

    def check_timer(self):
        self.hour_left, self.min_left, self.sec_left = str(datetime.timedelta(
            seconds=self.duration-(int(time.time())-self.settimer))).split(':')
        if int(self.hour_left) == 1:
            self.hour_left = ' {} {}'.format(
                self.hour_left.lstrip('0'), 'hour')
        elif int(self.hour_left) > 1:
            self.hour_left = ' {} {}'.format(
                self.hour_left.lstrip('0'), 'hours')
        if int(self.min_left) == 1:
            self.min_left = ' {} {}'.format(
                self.min_left.lstrip('0'), 'minute')
        elif int(self.min_left) > 1:
            self.min_left = ' {} {}'.format(
                self.min_left.lstrip('0'), 'minutes')
        if int(self.sec_left) == 1:
            self.sec_left = ' {} {}'.format(
                self.sec_left.lstrip('0'), 'second')
        elif int(self.sec_left) > 1:
            self.sec_left = ' {} {}'.format(
                self.sec_left.lstrip('0'), 'seconds')
        return 'You\'ve got{}{}{} on your timer'.format(self.hour_left, self.min_left, self.sec_left)


def bye():
    response = {1: 'You\'re welcome', 2: 'I\'m happy to help', 3: 'It\'s my pleasure',
                4: 'I\'m glad to help', 5: 'No trouble at all', 6: 'Don\'t mention it'}
    print(response[random.randint(1, 6)])


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
    r = requests.get(
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
        # speech.speaker('how long should i set a timer')
        print('How long should i set a timer?')
        duration = speech.recognizer()
        try:
            global T1
            T1 = Timer(duration)
            T1.start_timer()
        except Exception as e:
            print(e)
    elif any(string in command for string in ['cancel timer', 'cancel a timer']):
        try:
            print(T1.cancel_timer())
        except Exception as e:
            print(e)
            print('Sorry, I don\'t have a timer set for you')
    elif any(string in command for string in ['check timer', 'check a timer']):
        try:
            print(T1.check_timer())
        except Exception as e:
            print(e)
            print('Sorry, I don\'t have a timer set for you')
    return True
