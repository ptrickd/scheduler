#Side buttons on the main window
import tkinter as tk
def fct(master, left_frame, width_left, heigth_left, add_emp_frame, update_emp_frame, get_calendar_frame):
    #create a button to add new employees
    add_employee = tk.Button(
        left_frame, 
        width=width_left,
        height=heigth_left, 
        command=add_emp_frame
        )
    add_employee["text"] = "Add Employee"

    # create a button update info of employee
    update_employee = tk.Button(
        left_frame, 
        width=width_left,
        height=heigth_left, 
        command=update_emp_frame
        )
    update_employee["text"] = "Update Employee"

    # quit application
    quit = tk.Button(
        left_frame, 
        text="QUIT", 
        fg="red",
        width=width_left, 
        height=heigth_left,
        command=master.destroy
        )
    # create a button to get the calendar
    get_calendar = tk.Button(
        left_frame, 
        text="Calendar", 
        width=width_left,
        height=heigth_left, 
        command=get_calendar_frame
        )

    add_employee.pack()
    #to fix later: update_employee and get_calendat
    # update_employee.pack()
    
    # get_calendar.pack()
    quit.pack()