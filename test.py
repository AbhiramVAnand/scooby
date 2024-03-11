import pyaudio
import os
import pyttsx3
import openai
from dotenv import load_dotenv
import speech_recognition as sr
import time

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting current speaking rate
engine.setProperty('rate', 120) 

def speak_text(text):
	engine.say(text)
	engine.runAndWait()




def listen_and_convert():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen for user input
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        if text.lower() == "hello":
            speak_text("Hey, Abhiram!")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Sorry, my speech recognition service is down. Error: ", e)

if __name__ == "__main__":
    listen_and_convert()

