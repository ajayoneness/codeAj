import pytube
from pytube import YouTube
from tkinter import *
root=Tk()
root.geometry("1079x714")
root.title("UtubDownloader")

f=("poppins",15,"bold")
t=("poppins",35,"bold")
c="black"
fontcolor="white"


#https://www.youtube.com/watch?v=Am7apSvWRKE
#ut = pytube.YouTube("https://www.youtube.com/watch?v=Am7apSvWRKE")

def videoifo():
    try:
        ut = pytube.YouTube(f"{urlentry.get()}")
        vtitle = f"title : {ut.title}"
        rating=ut.rating
        des=ut.description
        agerec=ut.age_restricted
        views=ut.views
        #lenght=ut.length
        auther=ut.author
        #print(f"metadata : {ut.metadata}")
        #print(f"video info : {ut.vid_info}")
        pdate=ut.publish_date
        #tags=ut.keywords

        titles.config(text=vtitle)

        videoinformation = "\nviews : "+str(views)+"\nrating : "+str(rating)+"\nchenel : "+str(auther)+"\npublish date : "+str(pdate)+"\nage restricted : "+str(agerec)+"\n description : " +str(des)

        al.config(text=videoinformation)
    except:
        print("no internet connection !!")

def downloadinfo():
    try:
        ut = pytube.YouTube(f"{urlentry.get()}")
        processmessage=f"Downloading............."
        compleationmessage="download completed !!\nsaved at F:\\youtubedownload "
        processinfo="\n"+str(processmessage)
        proci.config(text=processinfo)
        vid=ut.streams.first()
        vid.download('F:\\youtubedownload')
        cominfo=f"\n"+str(compleationmessage)
        comi.config(text=cominfo)
    except:
        print("no internet connection !! ")


#GUI part

bg=PhotoImage(file="E:\\utub\\bg.png")
mypic=PhotoImage(file="E:\\utub\\PicsArt_01-10-02.52.34.png")

l5=Label(root,image=bg).place(x=0,y=0)
myimg=Label(root,image=mypic,bg=c).place(x=10,y=550)
l1=Label(text="paste url : ",font=t,fg=fontcolor,bg=c).grid(row=1,column=1)
titles=Label(root,font=("poppins",15,"bold"),fg=fontcolor,bg=c)
getit=Button(root,text="get info",command=videoifo,font=f,fg=fontcolor,bg="blue").grid(row=2,column=3)
al=Label(root,font=("poppins",9,"bold"),fg=fontcolor,bg=c)
downloadbutton=Button(text="Download",command=downloadinfo,font=f,fg=fontcolor,bg="green")
proci=Label(root,font=("poppins",10,"bold"),fg=fontcolor,bg=c)
comi=Label(root,font=("poppins",10,"bold"),fg=fontcolor,bg=c)
codeaj=Label(root,text="made by Ajay",font=f,bg=c,fg=fontcolor).place(x=200,y=620)


al.grid(row=4,column=2)
titles.grid(row=3 ,column=2)
downloadbutton.grid(row=5,column=3)
proci.grid(row=6,column=2)
comi.grid(row=7,column=2)

urlvalue=StringVar()

urlentry=Entry(root,textvariable=urlvalue,font=("poppins",35,"italic"),fg="blue",bg="pink")
urlentry.grid (row=1 ,column=2)
urlentry.focus()


root.mainloop()
