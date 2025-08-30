import warnings

from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace

# The UserWarning originates from pkg_resources, so we'll filter it from there.
# This needs to be done before any modules that import pkg_resources are loaded.
warnings.filterwarnings("ignore", category=UserWarning, module="pkg_resources")
import os 
import eel
from backend.feature import *
from backend.command import *
# @eel.expose
def start():
    
    eel.init("frontend") 
    
    play_assistant_sound()
    @eel.expose
    def init():
        eel.hideLoader()
        speak("Welcome to Jarvis")
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag ==1:
            speak("Face recognized successfully")
            eel.hideFaceAuth()
            eel.hideFaceAuthSuccess()
            speak("Welcome to Your Assistant")
            eel.hideStart()
            play_assistant_sound()
        else:
            speak("Face not recognized. Please try again")

    os.system('start msedge.exe --app="http://127.0.0.1:5500/index.html"')
    os.system('start msedge.exe --app="http://localhost:8001/index.html"')

   
    


    # eel.start("index.html", mode=None ,host="localhost",block=True)
    eel.start("index.html", mode=None, host="localhost", port=8001, block=True)

# if __name__ == "__main__":
#     start()