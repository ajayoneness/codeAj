#Code to Take Screenshot in Python 
import pyautogui
import random

n=random.randint(1,100)
scr=pyautogui.screenshot()
scr.save (f"F:\screenshot{n}.png")
print ("screenshot is sucessfully taken !!")
