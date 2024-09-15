import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
from datetime import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                return command
    except Exception as e:
        print(e)
        return ""

def run_alexa():
    while True:
        command = user_commands()
        if command:
            if 'joke' in command:
                joke = pyjokes.get_joke()
                print(joke)
                engine_talk(joke)
            elif 'time' in command:
                current_time = datetime.now().strftime('%I:%M %p')
                print(current_time)
                engine_talk('current time is ' + current_time)
            elif 'tell me about' in command:
                person = command.replace('tell me about','')
                info = wikipedia.summary(person, sentences=10)
                print(info)
                engine_talk(info)
            elif 'play' in command:
                song = command.replace('play','')
                engine_talk('playing ' + song)
                pywhatkit.playonyt(song)
            else:
                engine_talk('I could not hear you properly')
        else:
            engine_talk('I did not catch that.Please try again.')


if __name__ == "__main__":
    run_alexa()
