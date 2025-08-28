import time
import pyttsx3
import eel
import speech_recognition as sr



def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
   # print(voices)
    eel.DisplayMessage(text)
    engine.setProperty('voice', voices[0].id)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 174)
    eel.receiverText(text)
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
def takeAllCommands(message=None):
    if message is None:
        query = takecommand()  # If no message is passed, listen for voice input
        if not query:
            return  # Exit if no query is received
        print(query)
        eel.senderText(query)
    else:
        query = message  # If there's a message, use it
        print(f"Message received: {query}")
        eel.senderText(query)

    try:
        if query:
            if "open" in query:
                from backend.feature import openCommand
                openCommand(query)
        elif "send message" in query or "call" in query or "video call" in query:
            from backend.feature import findContact, whatsApp
            flag = ""
            Phone, name = findContact(query)
            if Phone != 0:
                if "send message" in query:
                    flag = 'message'
                    speak("What message to send?")
                    query = takecommand()  # Ask for the message text
                elif "call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                whatsApp(Phone, query, flag, name)
        elif "on youtube" in query:
            from backend.feature import PlayYoutube
            PlayYoutube(query)
        else:
            print("I'm not sure what to do")
            # from backend.feature import chatBot
            # chatBot(query)

    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, something went wrong.")
    
    eel.ShowHood()
