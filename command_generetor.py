from gtts import gTTS

command = 'what can i do for you'

tts = gTTS(command)
tts.save("C:/Users/Effigy/Desktop/In-home Nursing/commands/" +
         command.replace(" ", "") + ".mp3")
