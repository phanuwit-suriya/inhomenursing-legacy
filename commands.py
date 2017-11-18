import os
import time
import datetime
import requests
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text)
    tts.save(text.replace(" ", "") + ".mp3")
    os.system(text.replace(" ", "") + '.mp3')
    time.sleep(10)
    os.system('TASKKILL /F /IM wmplayer.exe')
    time.sleep(1/2)
    os.remove(text.replace(" ", "") + ".mp3")


def finish():
    speak("you're welcome")


def clocktime():
    clocktime = datetime.datetime.now().strftime("%H %M %p")
    speak("the time is" + clocktime)
    print(clocktime)


def date():
    date = datetime.datetime.now().strftime("%A %d %B %Y")
    speak("today is " + date)
    time.sleep(1.5)
    print(date)


def weather():
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=Bangkok,TH&APPID=52a601a7b6e589c3e9b7d18ee259b1be")
    json_object = r.json()
    temperature = json_object["main"]["temp"] - 273.15
    humidity = json_object["main"]["humidity"]
    speak("The weather in Bangkok" + " right now is " + str(round(temperature, 1)
                                                            ) + " degree celsius " + "with " + str(humidity) + " percent of himidity")


def browser():
    os.system("start chrome")


def musicplayer():
    os.system("start spotify")


def main(command=""):
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
    if command == "open browser":
        browser()
    if command == "open music player":
        musicplayer()

    return False
