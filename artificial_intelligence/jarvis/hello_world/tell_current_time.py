# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
import pyttsx3
import datetime


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def get_time():
    current_time = datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")
    speak(current_time)


if __name__ == '__main__':
    engine = pyttsx3.init()

    # slow down voice rate
    engine.setProperty('rate', 150)
    get_time()
