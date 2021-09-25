import time
import os
from threading import *

class timee(Thread):
    def run(self):
        while (True):
            print(time.ctime())
            time.sleep(1)
            os.system('cls')

class stringg(Thread):
    def run(self):
        s='hello i am ajay from malangwa sarlahi nepal and i am ajay '
        for i in range (len(s)):
            print (s[i])
            time.sleep(0.5)



t1= timee()
t2=stringg()

t1.start()
t2.start()

