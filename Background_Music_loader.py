from pygame import mixer

mixer.init()

mixer.music.load('21.mp3') #Loading audio File

mixer.music.play() #Playing Music with Pygame
mixer.music.stop()