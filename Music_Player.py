from tkinter import *
from tkinter import filedialog
from pygame import mixer

class Player:
    def __init__(self,window ):
        window.geometry('320x100'); window.title('Python Tiny Player'); window.resizable(0,0)
        Load=Button(window, text='Load', width=10, font=('Times,10'), command=self.load)
        Play=Button(window, text='Play', width=10, font=('Times,10'), command=self.play)
        Pause=Button(window, text='Pause', width=10, font=('Times,10'), command=self.pause)
        Stop=Button(window, text='Stop', width=10, font=('Times,10'), command=self.stop)
        Load.place(x=0, y=20); Play.place(x=110, y=20); Pause.place(x=220, y=20); Stop.place(x=110, y=60)
        self.music_file=False
        self.playing_state=False

