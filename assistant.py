import pyttsx3 as tts
import speech_recognition as sr
from neuralintents import GenericAssistant
import sys

recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty("rate", 150)

todo_list =[""]


def create_note():
    global recognizer
    speaker.say("What do you what to say?")
    speaker.runAndWait()
    done = False
    while not done:
        try:
            with sr.Microphone as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.3)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()
                speaker.say("Choose a filename")
                speaker.runAndWait()
                recognizer.adjust_for_ambient_noise(mic, duration=0.3)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()
            with open(filename, "w") as file:
                file.write(note)
                done = True
                speaker.say(f"I have succesfully taken your note{filename}")
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()

def add_todo():
    global recognizer
    speaker.say("what do you want to add to your todo list")
    speaker.runAndWait()
    done =False
    while not done:
        try:
            with sr.Microphone as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.3)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()
                todo_list.append(item)
                done = True
                speaker.say(f"i have added {item } to the to do list")
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()

def show_todo():
    speaker.say("The items in your to do list are")
    speaker.runAndWait()
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def hello():
    speaker.say("hello what can i do for you")
    speaker.runAndWait()

def quit():
    speaker.say("bye ")
    speaker.runAndWait()
    sys.exit(0)
mappings = {
    "greeting":hello, 
    "create_note" :create_note, 
    "show_todo": show_todo, 
    "add_todo":add_todo, 
    "exit":quit
}

assistant = GenericAssistant("intents.json")
assistant.train_model()

assistant.request()

while True:
    try:
        with sr.Microphone as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio)
            message = message.lower()
        assistant.request(message)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()


