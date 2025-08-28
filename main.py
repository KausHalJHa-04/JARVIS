import warnings
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
    # Note: Corrected a space around the '=' in the --app argument
    os.system('start msedge.exe --app="http://127.0.0.1:5500/index.html"')
    os.system('start msedge.exe --app="http://localhost:8001/index.html"')

    play_assistant_sound()


    # eel.start("index.html", mode=None ,host="localhost",block=True)
    eel.start("index.html", mode=None, host="localhost", port=8001, block=True)

if __name__ == "__main__":
    start()