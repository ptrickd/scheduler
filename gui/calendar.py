import tkinter as tk
from tkinter import ttk

def calendar(self):    
    # need to start need frame to use grid cmponenet
    color = "CadetBlue1"
    employees = ["Employee 1", "Employee 2", "Employee 3", "Employee 4"]
    # self.panedWindow = ttk.Panedwindow(self)
    # self.panedWindow["bg"] = "red"
    # self.panedWindow.pack()

    obj = {
        "monday": {
            "start": '4',
            "finish": '8'
            },
        "tuesday": {
            "start": '4',
            "finish": '8'
            },
        "wednesday": {
            "start": '4',
            "finish": '8'
            },
        "thursday": {
            "start": '4',
            "finish": '8'
            },
        "friday": {
            "start": '4',
            "finish": '8'
            },
        "saturday": {
            "start": '4',
            "finish": '8'
            },
        "sunday": {
            "start": '4',
            "finish": '8'
            }
        }

    # a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
    # for key in a_dict:
    #      print(key)

    self.calendar_frame = tk.Frame(self)
    self.calendar_frame.pack()

    caption = 'start: ' + obj["monday"]["start"] + '\n' + 'until:' + obj["monday"]["finish"]
    l_monday = ttk.Label(self.calendar_frame, text=caption,background=color, width=10)

    caption = 'start: ' + obj["tuesday"]["start"] + '\n' + 'until:' + obj["tuesday"]["finish"]
    l_tuesday = ttk.Label(self.calendar_frame, text=caption,background=color, width=10)

    caption = 'start: ' + obj["wednesday"]["start"] + '\n' + 'until:' + obj["wednesday"]["finish"]
    l_wednesday = ttk.Label(self.calendar_frame, text=caption,background=color, width=10)

    caption = 'start: ' + obj["thursday"]["start"] + '\n' + 'until:' + obj["thursday"]["finish"]
    l_thursday = ttk.Label(self.calendar_frame, text=caption,background=color, width=10)

    caption = 'start: ' + obj["friday"]["start"] + '\n' + 'until:' + obj["friday"]["finish"]
    l_friday = ttk.Label(self.calendar_frame, text=caption,background=color, width=10)

    caption = 'start: ' + obj["saturday"]["start"] + '\n' + 'until:' + obj["saturday"]["finish"]
    l_saturday = ttk.Label(self.calendar_frame, text=caption,background=color, width=10)

    caption = 'start: ' + obj["sunday"]["start"] + '\n' + 'until:' + obj["sunday"]["finish"]
    l_sunday = ttk.Label(self.calendar_frame, text=caption,background=color, width=10)

   
    
    labels = [l_monday, l_tuesday, l_wednesday, l_thursday, l_friday, l_saturday, l_sunday]
    
    #create the row of every day of the week
    count = 0
    for day in labels:
        day.grid(column=count, row=0)
        count += 1