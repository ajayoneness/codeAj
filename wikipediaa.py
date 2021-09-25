import wikipedia
from gtts import gTTS
import random
n=random.randint(1,100)
topic= input("enter topic : ")
summ = wikipedia.summary(topic)
print(summ)
tts=gTTS(summ)
tts.save(f"wiki {topic}.mp3")