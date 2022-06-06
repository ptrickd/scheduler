import tkinter as tk
from tkinter import ttk

from fakeData import employeesSchedule

#Function to choose  a week to make your calendar
def weekPicker(calendar_frame, bgColor, rowCount):
    #create combobox
    choices = [
        "May 2 to May 9 2022", 
        "May 10 to May 17 2022", 
        "May 18 to May 25 2022"
        ]

    combo_box = ttk.Combobox(
        calendar_frame, 
        width=22, 
        values=choices,
        font=('Arial', 12), 
        background=bgColor
        )
    
    combo_box.grid(column=3,row=rowCount, columnspan=3, ipadx=10, ipady=10)

