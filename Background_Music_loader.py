from pygame import mixer
import time

# Initialize mixer
mixer.init()

# Load music file
mixer.music.load("21.mp3")

# Play music
mixer.music.play()

# Keep the program running until song finishes
while mixer.music.get_busy():
    time.sleep(1)

# Stop (It will stop automatically when the song ends)
mixer.music.stop()
