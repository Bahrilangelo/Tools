import pyttsx3

engine = pyttsx3.init()

Sentence = 'Hello, World!'

engine.say(Sentence)
engine.runAndWait()
