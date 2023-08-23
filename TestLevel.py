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
import convert
import Readrandom



def GetStarted():
    win = tix.Tk()
    win.geometry("200x150")

    win.title('Inflection Booster')

    def lowlevel():
        win.destroy()
        window = tix.Tk()
        window.geometry("400x300")


        def results():
            window.destroy()
            win1 = tix.Tk()
            win1.geometry("300x300")
            win1.title('Inflection Booster')
            frame = tk.Frame(win1)
            frame.grid(row = 0,column = 0,sticky = "nsew")
            frame.place(x = 0,y = 0)
            frame.configure(height = 300,width = 300)
            string.lower()
            readtext.lower()
            print(readtext)
            if string == readtext:
                speak_text = 'Hurray!! you read it correct'
            elif string in readtext:
                speak_text = 'oh!! you extra words'
            else:
                speak_text = 'It is pronounced as ' + string

                
            speakimage = tk.PhotoImage(file = 'C:/users/tejaswini/Downloads/project/speak.png')
            speak = tk.Button(frame,text = 'speak',command =  lambda :texttospeech.speaknow(speak_text))
            #speak.image = speakimage
            speak.place(x = 100,y = 100)

        string = Readrandom.ReadRandom(1,'lowlevel.txt')
        namevalue = tk.StringVar()
        name = tk.Entry(window,textvariable = namevalue,width = 20,bd = 2,font =('Times',15,"italic"))
        name.insert(0,string)
        name.place(x = 130,y = 110)

        readvalue = tk.StringVar()
        read = tk.Entry(window,textvariable = readvalue,width = 20,bd = 2,font =('Times',15,"italic"))
        read.place(x = 130,y = 170)
        
        recordbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Record',command = lambda:read.insert(0,convert.SpeechToText()))
        recordbutton.place(x = 100,y = 250)
        readtext = read.get()

        #result
        resultbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Results',command = results)
        resultbutton.place(x = 200,y = 250)

    label = tk.Label(win,font  = ("Times",15,"italic"),text = 'Confirm to start test')
    label.place(x = 20,y = 10)
    button = tk.Button(win,font = ("Times",10,"italic"),text = 'start',command = lowlevel,width = 12)
    button.place(x = 90,y = 90)

def GetStarted1():
    win = tix.Tk()
    win.geometry("200x150")

    win.title('Inflection Booster')

    def mediumlevel():
        win.destroy()
        window = tix.Tk()
        window.geometry("400x300")


        def results():
            window.destroy()
            win1 = tix.Tk()
            win1.geometry("300x300")
            win1.title('Inflection Booster')
            frame = tk.Frame(win1)
            frame.grid(row = 0,column = 0,sticky = "nsew")
            frame.place(x = 0,y = 0)
            frame.configure(height = 300,width = 300)
            string.lower()
            readtext.lower()
            print(readtext)
            if string == readtext:
                speak_text = 'Hurray!! you read it correct'
            elif string in readtext:
                speak_text = 'oh!! you extra words'
            else:
                speak_text = 'It is pronounced as ' + string

                
            speakimage = tk.PhotoImage(file = 'C:/users/tejaswini/Downloads/project/speak.png')
            speak = tk.Button(frame,text = 'speak',command =  lambda :texttospeech.speaknow(speak_text))
            #speak.image = speakimage
            speak.place(x = 100,y = 100)

        string = Readrandom.ReadRandom(1,'mediumlevel.txt')
        namevalue = tk.StringVar()
        name = tk.Entry(window,textvariable = namevalue,width = 20,bd = 2,font =('Times',15,"italic"))
        name.insert(0,string)
        name.place(x = 130,y = 110)

        readvalue = tk.StringVar()
        read = tk.Entry(window,textvariable = readvalue,width = 20,bd = 2,font =('Times',15,"italic"))
        read.place(x = 130,y = 170)
        
        recordbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Record',command = lambda:read.insert(0,convert.SpeechToText()))
        recordbutton.place(x = 100,y = 250)
        readtext = read.get()

        #result
        resultbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Results',command = results)
        resultbutton.place(x = 200,y = 250)

    label = tk.Label(win,font  = ("Times",15,"italic"),text = 'Confirm to start test')
    label.place(x = 20,y = 10)
    button = tk.Button(win,font = ("Times",10,"italic"),text = 'start',command = mediumlevel,width = 12)
    button.place(x = 90,y = 90)
      
def GetStarted2():
    win = tix.Tk()
    win.geometry("200x150")

    win.title('Inflection Booster')

    def highlevel():
        win.destroy()
        window = tix.Tk()
        window.geometry("400x300")


        def results():
            window.destroy()
            win1 = tix.Tk()
            win1.geometry("300x300")
            win1.title('Inflection Booster')
            frame = tk.Frame(win1)
            frame.grid(row = 0,column = 0,sticky = "nsew")
            frame.place(x = 0,y = 0)
            frame.configure(height = 300,width = 300)
            string.lower()
            readtext.lower()
            print(readtext)
            if string == readtext:
                speak_text = 'Hurray!! you read it correct'
            elif string in readtext:
                speak_text = 'oh!! you extra words'
            else:
                speak_text = 'It is pronounced as ' + string

                
            speakimage = tk.PhotoImage(file = 'C:/users/tejaswini/Downloads/project/speak.png')
            speak = tk.Button(frame,text = 'speak',command =  lambda :texttospeech.speaknow(speak_text))
            #speak.image = speakimage
            speak.place(x = 100,y = 100)

        string = Readrandom.ReadRandom(1,'highlevel.txt')
        namevalue = tk.StringVar()
        name = tk.Entry(window,textvariable = namevalue,width = 20,bd = 2,font =('Times',15,"italic"))
        name.insert(0,string)
        name.place(x = 130,y = 110)

        readvalue = tk.StringVar()
        read = tk.Entry(window,textvariable = readvalue,width = 20,bd = 2,font =('Times',15,"italic"))
        read.place(x = 130,y = 170)
        
        recordbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Record',command = lambda:read.insert(0,convert.SpeechToText()))
        recordbutton.place(x = 100,y = 250)
        readtext = read.get()

        #result
        resultbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Results',command = results)
        resultbutton.place(x = 200,y = 250)

    label = tk.Label(win,font  = ("Times",15,"italic"),text = 'Confirm to start test')
    label.place(x = 20,y = 10)
    button = tk.Button(win,font = ("Times",10,"italic"),text = 'start',command = highlevel,width = 12)
    button.place(x = 90,y = 90)
