import pyautogui
from tkinter import *
import random
root=Tk()

def sc():
    n=random.randint(1,100)
    sc=pyautogui.screenshot()
    sc.save(f"F:\screenshot\c{n}.png")
    print (f"sucessfully screenshot is save at 'F:\screenshot\c{n}.png'")

root.geometry("300x100")
f1=Frame(root,bg='red')
f1.pack()
l1=Label(text="ajay: ")
l1.pack()
b1=Button(f1,text="screenshot",font ="arial,20,bold",padx=10,pady=10,bg="yellow",command=sc)
b1.pack(side=RIGHT,anchor="nw")

