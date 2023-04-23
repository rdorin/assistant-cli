import speech_recognition as sr
import subprocess

# initialize the recognizer
r = sr.Recognizer()

# returns text
def listen(time_limit=10):
    # automaticall close/clean up the microphone
    with sr.Microphone() as source:
        print("Ready for Speech...")

        # choice = input("enter anything to continue ...")
        r.adjust_for_ambient_noise(source)

        print("listening...")

        # get the audio data
        audio_data = r.listen(source, phrase_time_limit=time_limit)

        print("recognizing...")

        # get the text
        text = r.recognize_google(audio_data)
        print(f"you said: {text}")
    return text

