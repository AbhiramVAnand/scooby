import pyaudio
import os
import pyttsx3
import openai
from dotenv import load_dotenv
import speech_recognition as sr
import time

load_dotenv()
openai.api_key = os.environ["OPENAI_API"]
engine = pyttsx3.init()

def listen(filename):
	recognizer = sr.Recognizer()
	with sr.AudioFile(filename) as source:
		audio = recognizer.record(source)
	try:
		return recognizer.recognize_google(audio)
	except:
		print("Error1")

def generate_response(prompt):
	response = openai.Completion.create(
		engine = "text-davinci-003",
		prompt = prompt,
		max_tokens = 4000,
		n=1,
		stop = None,
		temperature = 0.5,
	)
	return response["choices"][0]["text"]

def speak_text(text):
	engine.say(text)
	engine.runAndWait()

def main():
	while(True):
		print("Say Scooby to start..")
		with sr.Microphone() as source:
			recognizer = sr.Recognizer()
			audio = recognizer.listen(source)
			text = recognizer.recognize_google(audio)
			if text.lower() == "scooby":
				speak_text("Hey Abhiram")
			try:
				transcription = recognizer.recognize_google(audio)
				if transcription.lower() == "scooby":
					print("Speak...")
					filename = "input.wav"
					print("Speak...")
					with sr.Microphone() as source:
						recognizer = sr.Recognizer()
						source.pause_threshold = 1
						audio = recognizer.listen(source, phrase_time_limit = None, timeout = None)
						with open(filename,"wb") as f:
							f.write(audio.get_wav_data())
						
					text = listen(filename)

					if text :
						print("You said ",text)

						response = generate_response(text)

						print("GPT says ", response)

						speak_text(response)
			except Exception as e:
				print("Error: ",e)
			
if __name__ == "__main__":
	main()

