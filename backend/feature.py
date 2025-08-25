# import playsound as playsound

# def playAssistantSound():
#     music_dir="frontend\\assets\\audio\\start_sound.mp3"
#     playsound.playsound(music_dir)

import eel
import pygame    

@eel.expose
def play_assistant_sound():
    sound_file = r"C:\JARVIS\frontend\assets\audio\start_sound.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()