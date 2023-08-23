import tkinter as tk
from tkinter import tix
from tkinter import messagebox
from tkinter.messagebox import showinfo
import tkinter.font as tkFont
from PIL import ImageTk,Image
import PIL
from gtts import gTTS
import os
import texttospeech
import webbrowser
import convert
import Readrandom


def KidAlphabet():
    window = tix.Tk()
    window.geometry("600x600")
    window.title("Inflection booster")

    #img = tk.PhotoImage(file = '\\users\\tejaswini\\Downloads\\project\\readingicon.png')
    #window.iconphoto(False,img)

    alphabet = "abcdefghijklmnopqrstuvwxyz"

   # alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    speak = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[0]),text = alphabet[0],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak.place(x = 40,y = 40)

    speak1 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[1]),text = alphabet[1],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak1.place(x = 120, y = 40)

    speak2 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[2]),text = alphabet[2],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak2.place(x = 200,y = 40)

    speak3 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[3]),text =  alphabet[3],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak3.place(x = 280,y = 40)
    
    speak4 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[4]),text =  alphabet[4],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak4.place(x = 360,y = 40)
    
    speak5 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[5]),text =  alphabet[5],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak5.place(x = 440,y = 40)
    
    speak6 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[6]),text =  alphabet[6],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak6.place(x = 520, y = 40)
     

    speak7 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[7]),text =  alphabet[7],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak7.place(x = 40,y = 150)

    speak8 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[8]),text =  alphabet[8],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak8.place(x = 120,y = 150)

    speak9 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[9]),text =  alphabet[9],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak9.place(x = 200,y = 150)

    speak10 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[10]),text =  alphabet[10],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak10.place(x = 280,y = 150)

    speak11 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[11]),text =  alphabet[11],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak11.place(x = 360,y = 150)

    speak12 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[12]),text =  alphabet[12],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak12.place(x = 440,y = 150)

    speak13 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[13]),text =  alphabet[13],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak13.place(x = 520,y = 150)

    speak14 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[14]),text =  alphabet[14],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak14.place(x = 40,y = 260)

    speak15 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[15]),text =  alphabet[15],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak15.place(x = 120,y = 260)

    speak16 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[16]),text =  alphabet[16],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak16.place(x = 200,y = 260)

    speak17 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[17]),text =  alphabet[17],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak17.place(x = 280,y = 260)

    speak18 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[18]),text =  alphabet[18],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak18.place(x = 360,y = 260)

    speak19 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[19]),text =  alphabet[19],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak19.place(x = 440,y = 260)

    speak20 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[20]),text =  alphabet[20],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak20.place(x = 520,y = 260)

    speak21 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[21]),text =  alphabet[21],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak21.place(x = 40,y = 370)

    speak22 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[22]),text =  alphabet[22],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak22.place(x = 120,y = 370)

    speak23 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[23]),text =  alphabet[23],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak23.place(x = 200,y = 370)

    speak24 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[24]),text =  alphabet[24],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak24.place(x = 280,y = 370)

    speak25 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[25]),text =  alphabet[25],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak25.place(x = 360,y = 370)

def KidWords():
    window = tix.Tk()
    window.geometry("600x600")
    window.title("Inflection booster")


    alphabet = ["Apple","Bat","Cat","Dog","Egg","Fish","Giraffe","Hen","Ice","Jelly","Kite","Lamp","Mango","Nest","Orange","Pen","Queen","Rabbit","Sea","Tap","Umbrella","Van","Wise","xerox","Yack","zebra"]
    

   # alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    speak = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[0]),text = alphabet[0],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak.place(x = 40,y = 40)

    speak1 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[1]),text = alphabet[1],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak1.place(x = 120, y = 40)

    speak2 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[2]),text = alphabet[2],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak2.place(x = 200,y = 40)

    speak3 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[3]),text =  alphabet[3],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak3.place(x = 280,y = 40)
    
    speak4 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[4]),text =  alphabet[4],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak4.place(x = 360,y = 40)
    
    speak5 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[5]),text =  alphabet[5],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak5.place(x = 440,y = 40)
    
    speak6 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[6]),text =  alphabet[6],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak6.place(x = 520, y = 40)
     

    speak7 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[7]),text =  alphabet[7],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak7.place(x = 40,y = 150)

    speak8 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[8]),text =  alphabet[8],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak8.place(x = 120,y = 150)

    speak9 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[9]),text =  alphabet[9],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak9.place(x = 200,y = 150)

    speak10 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[10]),text =  alphabet[10],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak10.place(x = 280,y = 150)

    speak11 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[11]),text =  alphabet[11],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak11.place(x = 360,y = 150)

    speak12 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[12]),text =  alphabet[12],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak12.place(x = 440,y = 150)

    speak13 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[13]),text =  alphabet[13],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak13.place(x = 520,y = 150)

    speak14 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[14]),text =  alphabet[14],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak14.place(x = 40,y = 260)

    speak15 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[15]),text =  alphabet[15],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak15.place(x = 120,y = 260)

    speak16 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[16]),text =  alphabet[16],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak16.place(x = 200,y = 260)

    speak17 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[17]),text =  alphabet[17],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak17.place(x = 280,y = 260)

    speak18 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[18]),text =  alphabet[18],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak18.place(x = 360,y = 260)

    speak19 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[19]),text =  alphabet[19],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak19.place(x = 440,y = 260)

    speak20 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[20]),text =  alphabet[20],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak20.place(x = 520,y = 260)

    speak21 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[21]),text =  alphabet[21],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak21.place(x = 40,y = 370)

    speak22 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[22]),text =  alphabet[22],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak22.place(x = 120,y = 370)

    speak23 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[23]),text =  alphabet[23],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak23.place(x = 200,y = 370)

    speak24 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[24]),text =  alphabet[24],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak24.place(x = 280,y = 370)

    speak25 = tk.Button(window,command =  lambda :texttospeech.speaknow(alphabet[25]),text =  alphabet[25],font = ("Times",15,"bold italic"),width = 4,height = 3)
    speak25.place(x = 360,y = 370)


