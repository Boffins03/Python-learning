import cowsay
import pyttsx3

engine = pyttsx3.init()
this = "Hello, how are you?"
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
