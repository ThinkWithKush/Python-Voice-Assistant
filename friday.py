#!/usr/bin/env python

from pyttsx3 import *
import speech_recognition as sr
import wikipedia
import datetime
import time
import webbrowser
import subprocess
import sys
import os

# Constants
BROWSER = r"C:\Program Files\Mozilla Firefox\firefox.exe"

engine=init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

# Setting firefox as default browser for opening web

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=7 and hour<12:
        wish="Good Morning"
    elif hour>=12 and hour<16:
        wish="Good Afternoon"
    else:
        wish="Good Evening"

    print(wish+" Sir,\nI am Friday , What can i do for you ?? .....")
    speak(wish+" Sir,\nI am Friday , What can i do for you ?? .....")
    

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1.5
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en in')
        print("User Said:",query)

    except Exception as e:
        print(e)
        speak("Sir, Please Say That Again")
        print("Say that again Please...")
        return "None"
    return query


if __name__ == "__main__":
    args=sys.argv()
    print(args)

    wishMe()
    while True:
        os.system('cls')
        
        query = takeCommand().lower()
    
    #Logic : ASli WAle
        if 'wikipedia' in query:
            speak('..Searching...Wikipedia')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("...Sir...ACcording To ...wikipedia")
            print(results)
            speak(results)
            #ABOVE Code can search any thing Through wikipediya and even read (Deafult as per code 2 Sentences) for you

        # General Data

        elif 'name' in query and 'your' in query :
            speak('I am Friday , your Virtual assistant')   

        elif 'created' in query and 'you' in query :
            speak('I was created by Kushagra Agarwal')
        
        # Open Websites or pages
        elif 'ims' in query :
            webbrowser.open("www.cuims.in")

        elif 'youtube' in query:
            subprocess.call([BROWSER,"-new-tab","www.youtube.com"])
        
        elif 'google' in query:
            subprocess.call([BROWSER,"-new-tab","www.google.com"])

        elif 'facebook' in query:
            subprocess.call([BROWSER,"-new-tab","www.facebook.com"])
        
        elif 'instagram' in query:
            subprocess.call([BROWSER,"-new-tab","www.instagram.com"])
       
        elif 'codechef' in query:
            subprocess.call([BROWSER,"-new-tab","www.Codechef.com"])
        
        elif 'github' in query:
            subprocess.call([BROWSER,"-new-tab","www.github.com"])
        
        elif 'studio' in query:
            os.startfile("C:\\Users\\Cvi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            #Change the Path according to Your System

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the Time is : "+strtime)
        
        # Good Bye
        elif 'end' in  query or 'shutdown' in query or 'bye' in query or 'shut up' in query or 'go to hell' in query:
            speak("Goodbye Sir , Thanks for calling me")
            break