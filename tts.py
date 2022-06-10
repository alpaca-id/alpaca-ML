from gtts import gTTS
import os
from playsound import playsound
from IPython.display import Audio

fileread = open("C:/Users/user/Documents/AI/selection-text.txt", "r")
language = 'id'
line = fileread.read()
fileread.close()
speech = gTTS(text=line, lang=language, slow=False)
speech.save("test.mp3")
playsound("test.mp3")
