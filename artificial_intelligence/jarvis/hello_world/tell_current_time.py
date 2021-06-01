# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
import pyttsx3
import datetime


def speak(audio):
    """
    :param audio: string to be spoken
    """
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def get_time_and_time():
    """
    Get the current date and time and speak it
    """
    current_time = datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")
    speak("Current date is ")
    speak(current_time)


def day_slice():
    """
    Get the current day slice based on the hour and greet the user by consequence
    """
    hour = datetime.datetime.now().hour

    if 0 <= hour < 6:
        speak("Good sunrise")
    if 6 <= hour < 12:
        speak("Good morning")
    if 12 <= hour < 18:
        speak("Good afternoon")
    if 18 <= hour < 24:
        speak("Good night")


if __name__ == '__main__':
    engine = pyttsx3.init()

    # slow down voice rate
    engine.setProperty('rate', 150)
    get_time_and_time()
    day_slice()
