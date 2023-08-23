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

def Game():
    window = tix.Tk()
    window.geometry('600x500')
    window.title('Inflection booster')
    def Convert():
        string1 = convert.SpeechToText()
        print(string1)
        if string1 in stringlist:
            print(dict1[string1])
            dict1[string1].pack_forget()
    '''stringlist = ['Hello','welcome','inflection','booster']
    label1 = tk.Label(window,font = ("Times",15,"italic"),text = stringlist[0])
    label1.place(x = 20, y = 80)

    label2 = tk.Label(window,font = ("Times",15,"italic"),text = stringlist[1])
    label2.place(x = 40,y = 100)

    label3 = tk.Label(window,font = ("Times",15,"italic"),text = stringlist[2])
    label3.place(x = 60,y = 120)

    label4 = tk.Label(window,font = ("Times",15,"italic"),text  = stringlist[3])
    label4.place(x = 80,y = 140)

    dict1 = {stringlist[0]:label1,stringlist[1]:label2,stringlist[2]:label3,stringlist[3]:label4}

    button = tk.Button(window,font = ("Times",10,"italic"),text = 'start',command = lambda: Convert(),width = 12)
    button.place(x = 100,y = 200)'''
    c = tk.Canvas(window)
    c.pack()
    c.create_oval(10,10,80,80,width = 2)
    c.create_polygon(110,10,210,80,width = 2)
    #c.create_oval(150,360,250,330,width = 2)
    c.create_rectangle(230,10,290,60,width = 2)
