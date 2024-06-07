import pyttsx3
import speech_recognition as sr
import datetime
import  webbrowser
import wikipedia
import os


# Taking voice from my system
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
# print(type(voices))
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


# Speak function

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# We will miss you from next week yathee maam
speak("i am Barath, working as statistical programmer")