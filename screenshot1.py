import pyautogui
from tkinter import *
import random
import time
from os import listdir
import webbrowser, os
import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)


root=Tk()
root.title('Ajscreenshots')
col='gray'
fcol='gray25'

def showSC():
    path="E:\screenshot\sc"
    webbrowser.open(os.path.realpath(path))
    #l4.config(text=allsc)

def screenshot(n):
    name = scname.get()
    root.withdraw()
    time.sleep(0.2)
    sc=pyautogui.screenshot()
    root.deiconify()
    if name != '':
        sc.save(f"E:\screenshot\sc\{name}.png")
        message=f"sucessfully screenshot is save at 'E:\screenshot\sc\{name}.png'"
        l2.config(text=message)
    else :
        sc.save(f"E:\screenshot\sc\screenshot{n}.png")
        message=f"sucessfully screenshot is save at 'E:\screenshot\sc\screenshot{n}.png'"
        l2.config(text=message)

def sc():
    n=random.randint(1,10000000)
    screenshot(n)
    


root.config(background=col)
root.geometry("600x300")
f1=Frame(root,bg=col)
f1.pack()


l1=Label(root,text="WELCOME to screenshorts App",font ="arial 10 bold",padx=10,pady=10,bg=col,fg=fcol)
l1.pack()

scname=Entry(root,bg=col,fg=fcol,font ='arial 10 bold')
scname.pack()
scname.focus()

b1=Button(root,text="screenshot",font ="arial 30 bold",padx=10,pady=10,bg=col,fg=fcol,command=sc)
b1.pack()

l2=Label(root,bg=col,fg=fcol,font = 'areal 9 bold')
l2.pack()

l3=Button(text='Preview',font = 'arial 20 bold',bg='sky blue',fg=fcol,command=showSC)
l3.pack()

l4=Label(root,bg=col,fg=fcol)
l4.pack()


root.mainloop()

