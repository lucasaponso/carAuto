from gtts import gTTS
import os

def output(data): ##Function is called to output sound to the FM signal
    tts = gTTS(text="Your current speed is " + str(data) + "kilometres per hour. Thats Amore", lang='it')
    tts.save("output.mp3") ##overwrite the existing mp3
    os.system("mpg321 output.mp3") ##play the mp3

output(90)