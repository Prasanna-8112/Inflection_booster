import speech_recognition as sr
import tkinter as tk

def SpeechToText():
    while True:
        string = ''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio_text = r.listen(source)
            try:
                string = r.recognize_google(audio_text)
            except:
                string = "Sorry, I did not get that"
                break
            return string
