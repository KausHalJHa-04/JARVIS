import os 
import eel

eel.init("frontend")
os.system('start msedge.exe --app = "http://127.0.0.1:5500/frontend/index.html"')

os.system('start msedge.exe --app="http://localhost:8001/index.html"')

# eel.start("index.html", mode=None ,host="localhost",block=True)
eel.start("index.html", mode=None, host="localhost", port=8001, block=True)