
import tkinter as tk
from tkinter import ttk

from fakeData import datesOfSchedules

#Function to choose  a week to make your calendar
def weekPicker(calendar_frame, bgColor, rowCount):
    dates = []
    for date in datesOfSchedules:
        print(date)
        dates.insert(0, date)
    

    combo_box = ttk.Combobox(
        calendar_frame, 
        justify="center",
        height=2,
        width=18, 
        values=dates,
        font=('Arial', 15), 
        background=bgColor
        )
    
    combo_box.grid(
        column=3,
        row=rowCount, 
        columnspan=3, 
        ipadx=5, 
        ipady=5
        )

