import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)

engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text: str) -> None:
    engine.say(text)
    engine.runAndWait()

def greet_user() -> None:
    hour: int = datetime.now().hour

    if (hour >= 3) and (hour < 12):
        speak(f'Good Morning {USERNAME}')
    elif (hour >= 12) and (hour < 16):
        speak(f'Good afternoon {USERNAME}')
    elif (hour >= 16) and (hour < 23):
        speak(f'Good evening {USERNAME}')
    speak(f"I am {BOTNAME}. How may I assist you?")

def take_user_input() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))

        else:
            hour = datetime.now().hour
            if hour >= 23 and hour < 3:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'

    return query