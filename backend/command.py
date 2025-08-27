import time
import pyttsx3
import eel
import speech_recognition as sr



def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
   # print(voices)
    eel.DisplayMessage(text)
    engine.setProperty('voice', voices[1].id)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 174)

# speak("hello, I am Jarvis. How can I help you today?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        eel.DisplayMessage("I'm listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 8)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        time.sleep(3)
        speak(query)

    except Exception as e:
        print(f"Error: {str(e)}\n")
        return None

    return query.lower()


@eel.expose
def takeAllCommands():
    query = takecommand()
    print(query)
    if "open" in query:
        from backend.feature import openCommand 
        openCommand(query)
    elif "youtube" :
        from backend.feature import playYoutube
        playYoutube(query)

    else:
        print("I'm Not Sure What to do ")
            
        eel.ShowHood()