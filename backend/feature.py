# import playsound as playsound

# def playAssistantSound():
#     music_dir="frontend\\assets\\audio\\start_sound.mp3"
#     playsound.playsound(music_dir)

import os
import re
import webbrowser
import eel
import pywhatkit as kit
import pygame 
from backend.config import ASSISTANT_NAME
from backend.command import speak
import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

@eel.expose
def play_assistant_sound():
    sound_file = r"C:\JARVIS\frontend\assets\audio\start_sound.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()



def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute( 
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

 

def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

    