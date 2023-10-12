from tkinter import *
from gtts import gTTS
from playsound import playsound
from prettytable import PrettyTable
from PIL import ImageTk, Image

w=Tk()
w.title("Text to Voice")
w.geometry("1200x600")

#Get wigth & height of screen
width= w.winfo_screenwidth()
height= w.winfo_screenheight()

#Fullscreen
w.geometry("%dx%d" % (width, height))
w.resizable(False, False)

#Image
imgTemp = Image.open("Steps.jpg")
img2 = imgTemp.resize((width,height))
img = ImageTk.PhotoImage(img2)

l = Label(w,image=img)
l.pack(side='top',fill=Y,expand=True)

l=Label(w,text="Type Your Word Here -",font=("times new roman",30),bg="black",fg="firebrick4")
l.place(x=380,y=150)

Msg=StringVar()

e1=Entry(w,textvariable = Msg,font="cambria 20",width=25,border=0,bg="black",fg="White")
e1.place(x=400,y=230)
Frame(w,width=300,height=2,bg="White").place(x=390,y=270)

def Play():
    text1=e1.get()
    language='en'
    obj=gTTS(text=text1,lang=language)
    obj.save("exam.mp3")
    playsound("exam.mp3")
def Exit():
    w.destroy()
def Reset():
    Msg.set("")
l=[]
def save_info():
    global l
    l.append(Msg.get())
    file = open("user.txt","w+")
    file.write("word\n")
    for i in l:
        file.write("\n")
        file.write(i)
    
    file.close()

b1=Button(w,text='Play..',font='cambria 20 bold',command=Play,width='8',bg="black",fg="firebrick4",border=0)
b1.place(x=400,y=400)

b2=Button(w,text='Reset..',font='cambria 20 bold',command=Reset,width='8',bg="black",fg="firebrick4",border=0)
b2.place(x=550,y=400)

b3=Button(w,text='Exit',font='cambria 15 bold',command=Exit,width='8',bg="black",fg="firebrick4",border=0)
b3.place(x=1400,y=30)

b= Button(w,text="Save..",font='cambria 20 bold',command=save_info,width="8",bg="black",fg="firebrick4",border=0)
b.place(x=700,y=400)
