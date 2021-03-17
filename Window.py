import tkinter as tk
from tkinter import ttk
from tkinter import *


class Main_Frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # title of windows
        self.master.title("The Scheduler")
        self.master["height"] = "600"
        self.master["width"] = "1200"
        self.master.maxsize(1200, 600)
        # not sure about expand
        self.pack(expand=True)
        # self.create_widgets()
