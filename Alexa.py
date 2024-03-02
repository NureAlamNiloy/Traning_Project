import speech_recognition as niloy
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = niloy.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    try:
        with niloy.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except Exception as e:
        print(e)
        command = ""
    return command


def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry vaiya, I am in another relation')
    elif command:
        talk('YES Wait a minute')
        pywhatkit.search(command)


while True:
    run_alexa()
