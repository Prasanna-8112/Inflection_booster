import pyttsx3

def speaknow(string):
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()
    engine.stop()


