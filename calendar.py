import tkinter as tk
from tkinter import ttk

def calendar(self):    
    # treeview
    employees = ["Employee 1", "Employee 2", "Employee 3", "Employee 4"]
    self.treeview = ttk.Treeview(self.right_frame)
    self.treeview['columns'] = ('Monday', 'Tuesday', 'Wednesday',
                                'Thursday', 'Friday',
                                'Saturday', 'Sunday')
    week_days = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday',
                    'Saturday', 'Sunday']

    for x in week_days:
        self.treeview.column(x, width=50, anchor='center')

    self.treeview.column('#0', width=175)
    self.treeview.column('#1', width=67)
    self.treeview.column('#2', width=67)
    self.treeview.column('#3', width=67)
    self.treeview.column('#4', width=67)
    self.treeview.column('#5', width=67)
    self.treeview.column('#6', width=67)
    self.treeview.column('#7', width=67)

    for x in week_days:
        self.treeview.heading(x, text=x)

    init_days = ['OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF']
    # count = 4
    for x in employees:
        self.treeview.insert('', 'end', text=x, values=init_days)
        

    self.treeview.pack()