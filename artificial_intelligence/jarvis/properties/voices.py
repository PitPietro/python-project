# https://github.com/nateshmbhat/pyttsx3
import pyttsx3


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# slow down voice rate
engine.setProperty('rate', 150)

for i in range(0, 5):
    engine.setProperty('voice', voices[i].id)
    speak("Voices test number " + str(i) + ". How are you?")


