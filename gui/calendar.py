import tkinter as tk
from tkinter import ttk

from fakeData import employeeSchedule

def calendar(self):    
    #constants
    heigth_rigth = 2
    width_rigth = 89
    bgColor = "grey35"

    # need to start need frame to use grid component

    self.calendar_frame = tk.Frame(self, bg=bgColor)
    self.calendar_frame.pack()
    
    # separator = ttk.Separator(self.calendar_frame, orient='horizontal')

    # create label display schedule/request
    label_schedule = tk.Label(self.calendar_frame, width=width_rigth, bg=bgColor,
                                    height=heigth_rigth, padx=10, pady=10)
    label_schedule["text"] = "Schedule"
    label_schedule["anchor"] = "s"
    label_schedule["justify"] = "center"

    # create label display week
    label_week = tk.Label(self.calendar_frame, width=width_rigth, bg=bgColor,
                                height=heigth_rigth, padx=10, pady=10)
    label_week["text"] = "Week May 2 to May 9"

    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    labels = []

    count = 0
    for day in days:
        caption = '\n start: ' + employeeSchedule[days[0]]["start"] + '\n\n\n' + ' end:   ' + employeeSchedule[days[0]]["finish"] + '\n'
        labels.insert(0, ttk.Label(self.calendar_frame, font=('Arial', 15), text=caption, width=10, background=bgColor, borderwidth=1, relief="solid"))
        count += 1

    label_schedule.grid(column=0,row=0, columnspan=7)
    #sticky from east limit to west limit
    # separator.grid(column=1,row=1, columnspan=5, sticky='ew')
    label_week.grid(column=0,row=2, columnspan=7)

    #create the row of every day of the week
    count = 0
    for day in labels:
        day.grid(column=count, row=3)
        count += 1