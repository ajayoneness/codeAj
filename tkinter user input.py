from tkinter import *
from twilio.rest import Client
import random
root = Tk()

def verify():
    if otpentry.get()==str(randomotp):
        tex="your account is sucessfully verified !! "
    else:
        tex="incorrect OTP !! "

    l2.config(text= tex)

randomotp=random.randint(100000,999999)
def mainotp():
    try:
        account_sid = 'AC60f1aa727b2baf6d32c18fce64a6d215'
        auth_token = '7fabcd603876b393157e646b5d134882'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                            body=f"OTP for verification process is {randomotp}\nsent by codeaj",
                            from_='+19855098726',
                            to=f'+91{phonenoentry.get()}')
        senn="otp is sent"
        sen.config(text=senn)
    except:
        print ("Not valid number OR there is no internet connection on your PC")


root.geometry("1079x714")
f=("poppins",15,"bold")
t=("poppins",35,"bold")
c="black"
fontcolor="white"


f1=Frame(root,bg="yellow4",padx="7",borderwidth= "6")
f1.grid()
bg=PhotoImage(file="C:\\Users\\ajay pandit\\Desktop\\otp.png")
mypic=PhotoImage(file="D:\\my photo\\PicsArt_01-10-02.52.34.png")


l1=Label(root,image=bg).place(x=0,y=0)
myimg=Label(root,image=mypic,bg=c).place(x=10,y=550)
Label(text="OTP VERYFICATION",font=t,bg=c,fg=fontcolor).grid(row=1,column =1)
firstname=Label(text=" first name : ",font=f,bg=c,fg=fontcolor)
lastname=Label(text=" last name : ",font=f,bg=c,fg=fontcolor)
phoneno=Label(text=" phone no. : ",font=f,bg=c,fg=fontcolor)
note1=Label(text="note : ",bg=c,fg=fontcolor)
note=Label(text="one-time-password is sent on yor given phone no ",bg=c,fg=fontcolor)
otp=Label(text="OTP : ",font=f,bg=c,fg=fontcolor)
Button(text="verify ! ",font=t,command = verify,bg=c,fg=fontcolor).grid(row=7,column=2)
Button(text="send",font=f,command=mainotp,bg=c,fg=fontcolor).grid(row = 4 , column = 2)
l2=Label(root,bg=c,fg=fontcolor)
sen=Label(root,bg=c,fg=fontcolor)
codeaj=Label(root,text="made by codeAj",font=f,bg=c,fg=fontcolor).place(x=500,y=620)


firstname.grid(row=2 , column=0)
lastname.grid(row=3, column=0)
phoneno.grid(row=4,column=0)
note1.grid(row=5,column=0)
note.grid(row=5,column=1)
otp.grid(row=6,column=0)
l2.grid(row=7,column=1)
sen.grid(row=5,column=2)

firstnamevalue=StringVar()
lastnamevalue=StringVar()
phonenovalue=StringVar()
otpvalue=StringVar()

firstnameentry=Entry(root,textvariable=firstnamevalue,font=f)
lastnameentry=Entry(root,textvariable=lastnamevalue,font=f)
phonenoentry=Entry(root,textvariable=phonenovalue,font=f)
#phonenoentry.bind("<Return>",message.sid)

otpentry=Entry(root,textvariable=otpvalue,font=f)

firstnameentry.grid(row=2,column=1)
lastnameentry.grid(row=3,column=1)
phonenoentry.grid(row=4,column=1)
otpentry.grid(row=6,column=1)



root.mainloop()
