import tkinter as tk
from tkinter import ttk

from sqlalchemy import column

from fakeData import employeesSchedule
from weekPicker import weekPicker

def calendar(self):

    #constants
    heigth_rigth = 2
    width_rigth = 95
    bgColor = "grey35"

    # need to start need frame to use grid component

    self.calendar_frame = tk.Frame(self, bg=bgColor, padx=10, pady=10)
    self.calendar_frame.pack()
    
    # separator = ttk.Separator(self.calendar_frame, orient='horizontal')

    # create label display schedule/request
    label_schedule = tk.Label(
        self.calendar_frame, 
        width=width_rigth, 
        bg=bgColor,
        height=heigth_rigth, 
        font=('Arial', 15),
        padx=5, 
        pady=5
        )

    label_schedule["text"] = "Schedule"
    label_schedule["anchor"] = "n"
    label_schedule["justify"] = "center"

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    labels = []

    #make row by employee
    count = 0
    for employee in employeesSchedule:
         # # #create label for name of the employee
        labels.insert(0, ttk.Label(
            self.calendar_frame, 
            text="\n\n" + employee["name"] + "\n\n", 
            font=('Arial', 15), 
            width=10, 
            background=bgColor, 
            borderwidth=1,
            anchor="center",
            relief="solid"
            ))
        
        for day in employee["week"]:
            start = employee["week"][day]["start"]
            finish = employee["week"][day]["finish"]
            caption = '\n' + start + '\n' +'  to' + '\n'  + finish + '\n'
               
            labels.insert(0, ttk.Label(
                self.calendar_frame, 
                font=('Arial', 15), 
                text=caption, 
                width=12, 
                background=bgColor, 
                borderwidth=1, 
                relief="solid",
                anchor='center'
                ))

    ##gridding
    rowCount = 0
    label_schedule.grid(column=0,row=rowCount, columnspan=8)
    rowCount += 1
    weekPicker(calendar_frame=self.calendar_frame, bgColor=bgColor, rowCount=rowCount)
    #sticky from east limit to west limit
    # separator.grid(column=1,row=1, columnspan=5, sticky='ew')
    rowCount += 1
        
    ##create dict keyword atttribute for styling 
    styleLabel = {
        "fontName":"Arial",
        "fontSize":15,
        "width":12,
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

    #gridding all labels with the names and the shifts  
    count = 0
    labels.reverse()
    for cell in labels:

        cell.grid(column=count, row=rowCount)
        count += 1
        if count == 8:
            count = 0
            rowCount += 1
        

    