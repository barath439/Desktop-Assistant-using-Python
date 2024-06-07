import pyttsx3
import speech_recognition as sr
import datetime
import  webbrowser
import wikipedia
import os


# Taking voice from my system
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)