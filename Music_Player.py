from tkinter import *
from tkinter import filedialog
from pygame import mixer

class Player:
    def __init__(self,window ):
        window.geometry('320x100'); window.title('Python Tiny Player'); window.resizable(0,0)
        Load=Button(window, text='Load',width=10,font=('Times,10'),command=self.load)
