import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia


engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

def timer():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = datetime.datetime.now().strftime("%B")
    day = int(datetime.datetime.now().day)
    speak(month) 
    speak(day)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    speak("The time is")
    timer()
    speak("Today is the")
    date()
    speak("How may I help?")

def proccessing(commands):
    listener = sr.Recognizer()
    if 'cova' in commands:
        speak("listening")
        print("Listening")
        with sr.Microphone() as source:
            listener.pause_threshold = 1
            audio = listener.listen(source)

            speak("Ok understanding")
            print("Ok understanding")
            commands = listener.recognize_google(audio)
            commands = commands.lower()  
        exit()
    return commands
    
def take_command():
    listener = sr.Recognizer()
    try:
            with sr.Microphone() as source:
                print ("Listening")
                listener.pause_threshold = 1
                audio = listener.listen(source)
                
                commands = listener.recognize_google(audio)
                commands = commands.lower()
                if "stop" in commands:
                    return commands
                elif "cova" in commands:
                    commands = commands.replace('cova ', '')
                NumofLetter = 0
                maxLetter = 100

                    
                for l in commands:
                    if l.isalpha():
                        NumofLetter += 1
                if NumofLetter >= maxLetter:
                    speak("I don't understand")
                    exit()
                    
                
    except Exception as e:
        print(e)
        commands = take_command()
    return commands

def yt(commands):
        if 'play' in commands:
            The_song = commands.replace('play ', '')
            speak('playing' + The_song)
            The_song = The_song.replace(' ', '+')
            print(The_song)
            return The_song

        else:
            return "none"
            
    

def ggsearch(Re):
    if "search on google" or "search" or "what is" or "when" or "how" or "google" in Re:
        Question = Re.replace('search', '')
        Question = Question.replace('search on google', '')
        Question = Question.replace('google', '')
        print('searching ' + Question)
        speak('searching' + Question)
        pywhatkit.search(Question)
    else:
        exit()

def wiki(command):
    info = wikipedia.summary(command, 1)
    print (info)
    speak (info)






