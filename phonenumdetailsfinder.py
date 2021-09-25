from tkinter import *

root=Tk()
root.title("phone number information finder ")
root.geometry("790x300")

f=("poppins",15,"bold")
t=("poppins",35,"bold")
h=("poppins",25,"bold")

Label(text="PHONE NUMBER DETAILS FINDER ",font=t).grid(row= 0,column = 3)
phonenum=Label(text="Phone number : ",font = t).grid(row =1,column =0 )
button=Button(text="Find",font = t).grid(row = 1, column =3)
info=Label().grid()


phonenumvalue=StringVar()



root.mainloop()