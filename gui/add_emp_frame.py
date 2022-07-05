import tkinter as tk
from tkinter import ttk
from tkinter import *

def fct():
        newWindow = tk.Toplevel()
        newWindow.title("Employee Info")
        newWindow.resizable(height=0, width=0)

        new_frame = tk.Frame(
            newWindow, 
            bd=2, 
            padx=10, 
            pady=10, 
            relief=GROOVE
            )
        new_frame.pack()

        label_first_name = tk.Label(
            new_frame, 
            text="First Name", 
            padx=10, 
            pady=10
            )
        label_last_name = tk.Label(
            new_frame, 
            text="Last Name", 
            padx=10, 
            pady=10
            )
        label_position = tk.Label(
            new_frame, 
            text="Position", 
            padx=10, 
            pady=10
            )
        label_wage = tk.Label(new_frame, text="Wage", padx=10, pady=10)
        label_space = tk.Label(new_frame, width=5)

        entry_first_name = tk.Entry(new_frame, width=25)
        # entry_last_name = tk.Entry(new_frame, width=25)
        # entry_position = tk.Entry(new_frame, width=25)
        # entry_wage = tk.Entry(new_frame, width=25)

        widgets = entry_first_name#, entry_last_name, entry_position, entry_wage

        # button_save = tk.Button(new_frame, text="Save", padx=20,
        #                         command=save_emp)
        # button_clear = tk.Button(new_frame, text="Clear All", padx=10,
        #                          command=clear_emp(widgets))
        # button_read = tk.Button(new_frame, text="Read", padx=20,
        #                         command=read_emp)

        #command = f_name = text_first_name.get()
        label_first_name.grid(row=0, column=0)
        entry_first_name.grid(row=0, column=1)
        # label_last_name.grid(row=1, column=0)
        # entry_last_name.grid(row=1, column=1)
        # label_position.grid(row=2, column=0)
        # entry_position.grid(row=2, column=1)
        # label_wage.grid(row=3, column=0)
        # entry_wage.grid(row=3, column=1)
        # button_clear.grid(row=4, column=0)
        # button_save.grid(row=4, column=1)
        # button_read.grid(column=3, row=4)
        label_space.grid(column=3)