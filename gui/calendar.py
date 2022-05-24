import tkinter as tk
from tkinter import ttk

from fakeData import employeeSchedule

def calendar(self):    
    #constants
    heigth_rigth = 2
    width_rigth = 89
    bgColor = "grey35"

    # need to start need frame to use grid component

    self.calendar_frame = tk.Frame(self, bg=bgColor, padx=10, pady=10)
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
        caption = '\n start: ' + employeeSchedule["Brad"][days[0]]["start"] + '\n\n' + ' end:   ' + employeeSchedule["Brad"][days[0]]["finish"] + '\n'
        labels.insert(0, ttk.Label(self.calendar_frame, font=('Arial', 15), text=caption, width=10, background=bgColor, borderwidth=1, relief="solid"))
        count += 1

    # #create label for name of the employee
    labels.insert(0, ttk.Label(
        self.calendar_frame, 
        text="\n\n" + list(employeeSchedule.keys())[0] + "\n\n", 
        font=('Arial', 15), 
        width=10, 
        background=bgColor, 
        borderwidth=1,
        anchor="center",
        relief="solid"
        )
        )

    #gridding
    rowCount = 0
    label_schedule.grid(column=0,row=rowCount, columnspan=8)
    rowCount += 1
    #sticky from east limit to west limit
    # separator.grid(column=1,row=1, columnspan=5, sticky='ew')
    label_week.grid(column=0,row=rowCount, columnspan=8)
    rowCount += 1
    
    #create dict keyword atttribute for styling 
    
    styleLabel = {
        "fontName":"Arial",
        "fontSize":15,
        "width":10,
        "background":bgColor,
        "borderwidth":1, 
        "relief":"solid"
        }
    
   


    #create the labels with the name of the days of the weeks 
    count = 0
    for day in days:
        dayLabel = ttk.Label(self.calendar_frame, text=days[count])
        dayLabel.config(
            font=(styleLabel["fontName"], styleLabel["fontSize"]), 
            width=styleLabel["width"],
            background=styleLabel["background"], 
            borderwidth=styleLabel["borderwidth"], 
            relief=styleLabel["relief"],
            anchor="center"
        )
        dayLabel.grid(column=count+1, row=rowCount, ipady=10)
        count += 1
    rowCount += 1

    #create the row of every day of the week
    count = 0
    for day in labels:
        day.grid(column=count, row=rowCount)
        count += 1