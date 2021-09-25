from tkinter import *
import time
import os
#gui part
root=Tk()
root.title("Time ")
root.geometry('400x100')
col="gray22"

def timee ():
    #while (True):
    t=time.ctime()
        #time.sleep(1)
        #os.system('cls')

    con='TIME'+str(t)
    l1.config(text=con)


root.configure(background=col)

tym=Label(root,text='TIME ', font ='areal 40 bold',fg='gray',bg=col)
tym.pack()
l1=Label(root, font ='areal 40 bold',fg='gray',bg=col)
l1.pack()

root.mainloop()