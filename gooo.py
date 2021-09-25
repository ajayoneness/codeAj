from gtts import gTTS
import random

n=random.randint(1,100)

inp=input("enter the string : ")

tts=gTTS(inp)
tts.save(f"aj{n}.mp3")
