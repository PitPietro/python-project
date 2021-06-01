# https://github.com/nateshmbhat/pyttsx3
import pyttsx3


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


if __name__ == '__main__':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # slow down voice rate
    engine.setProperty('rate', 150)

    engine = pyttsx3.init()
    for voice in voices:
        # print(voice)
        if voice.id == 'english':
            print("voice: " + str(voice))
            engine.setProperty('voice', voice.id)
            break
    speak("Hello World")



