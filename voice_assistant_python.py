import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio
import os
import wikipedia
import webbrowser
import wolframalpha
import PyPDF2
from datetime import date

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', 'voice[1].id')


def speak(voice):
    engine.say(voice)
    engine.runAndWait()


def greeting():
    time = int(datetime.datetime.now().hour)
    if (time>=0) and (time<12):
        speak('Hello, good morning. Now the time is ' + str(time) +' hours')
        print('''Hello, Good morning. Now the time is ''' + str(time) + 'hours')
    elif (time>=12) and (time<17):
        speak('Hello, good afternoon. Now the time is ' + str(time) +' hours')
        print('Hello, Good afternoon. Now the time is ' + str(time) +' hours')
    else:
        speak('Hello, good evening. Now the time is ' + str(time) +' hours')
        print('Hello, good evening. Now the time is ' + str(time) +' hours')


def recogniser():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Say something!")
        print("Say something!")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='en-in')
        print(data)

    except Exception as exp:
        print(exp)
        speak("Please, Say again")
        print('Please,say again')
        return 0
    return data

greeting()
while True:

    query = recogniser().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        speak("The time is {strTime}")


    elif 'how are you' in query:
        speak("I am fine, Thank you")
        speak("How are you, Sir")

    elif 'fine' in query or "good" in query:
        speak("It's good to know that your fine")

    elif 'exit' in query:
        speak("Thanks for giving me your time")
        exit()

    elif "who made you" in query or "who created you" in query:
        speak("I have been created by Pytrek Team#1 members.")

    elif "calculate" in query:

        app_id = "Wolframalpha api id"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)

    elif 'search' in query or 'play' in query:

        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)


    elif "wikipedia" in query:
        webbrowser.open("wikipedia.com")

    elif "Good Morning" in query:
        speak("A warm" + query)
        speak("How are you? ")


    elif "how are you" in query:
        speak("I'm fine, glad you ask me that")

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print("No results")
