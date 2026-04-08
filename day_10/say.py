import cowsay
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'en-us+f4')

this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
