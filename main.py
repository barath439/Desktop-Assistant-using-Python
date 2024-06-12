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
    """this function takes text and return voices
    
    
    Args:
         text(_type_): string
         """
    engine.say(text)
    engine.runAndWait()
    
# We will miss you from next week yathee maam
speak("i am Barath, working as statistical programmer")



# Speech recognition function
def takeCommand():
    """this function will recognize voice and returns text
    """
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio= r.listen(source)
        
        
        try:
            print("Recognizing...")
            query=r.recognize_google(audio, language='en-in')
            print(f"User said:{query}\n")
            
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query    
    
    
# text=takeCommand()
# speak(text)
if __name__ == "__main__": 
    
    query=takeCommand().lower()
    
    if "wikipedia" in query:
        print("searching wikipedia")
        query=query.replace('wikipedia', "")
        results=wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)
        
    elif "youtube" in query:
        speak("Opening Youtube")
        webbrowser.open("youtube.com")
        
    elif "google" in query:
        speak("Opening google")
        webbrowser.open("google.com")  
        
    elif "github" in query:
        speak("Opening github")
        webbrowser.open("github.com")        
        
            
    