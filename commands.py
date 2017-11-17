import os
import time
import datetime
import requests


from gtts import gTTS

commands = ['backward', 'forward', 'goodafternoon', 'goodevening', 'goormorning',
            'lastwindow', 'newemail', 'nextwindow', 'openbrowser', 'openmusicplayer']


def speak(text):
    tts = gTTS(text=text)
    tts.save(text.replace(" ", "") + ".mp3")
    os.system(text.replace(" ", "") + '.mp3')
    time.sleep(10)
    os.system("TASKKILL /F /IM wmplayer.exe")
    time.sleep(1)
    os.remove(text.replace(" ", "") + ".mp3")


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
        'https://api.openweathermap.org/data/2.5/weather?q=Bangkok,TH&APPID=52a601a7b6e589c3e9b7d18ee259b1be')
    json_object = r.json()
    temperature = json_object['main']['temp'] - 273.15
    humidity = json_object['main']['humidity']
    speak("The weather in Bangkok" + " right now is " + str(round(temperature, 1)
                                                            ) + " degree celsius" + "with " + str(humidity) + " percent of himidity")


def browser():
    os.system("start chrome")


def musicplayer():
    os.system("start spotify")


def main(command):
    if command == "what time is it":
        clocktime()
    if command == "what day is today":
        date()
    if command == "what's the weather today" or "what is the weather today" or "what's the weather" or "what is the weather":
        weather()
    if command == "open browser":
        browser()
    if command == "open music player":
        musicplayer()


if __name__ == '__main__':
    main("what time is it")
