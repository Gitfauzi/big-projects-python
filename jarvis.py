import datetime
import pyttsx3  # its a module used to convert words in voice using sapi5 for windows

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good morning")
    elif hour >= 12 and hour <18:
        speak("good afternoon")
    else:
       speak("good evening")
    speak("i am jarvis, how may i help you ")

def takecommand():
    r = sr.Recogniser()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
    
if __name__ == "__main__":
    speak("hello")
    wishMe()

    
