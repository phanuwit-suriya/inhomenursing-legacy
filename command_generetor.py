from gtts import gTTS

command = 'what day is today'

tts = gTTS(command)
tts.save("C:/Users/Effigy/Desktop/speech_recognition/commands/" + command.replace(" ", "") + ".mp3")
