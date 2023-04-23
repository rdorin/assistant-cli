import pyttsx3

# Lets start with a simple TTS
tts = pyttsx3.init()

try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
except Exception as e:
    print(e)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello World")



