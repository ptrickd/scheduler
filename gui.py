import tkinter as tk
from tkinter import ttk
from tkinter import *
from table import *
from calendar import calendar


class Main_Frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # title of windows
        self.master.title("The Scheduler")
        self.master["bg"] = "DarkOliveGreen1"
        self.master["height"] = "600"
        self.master["width"] = "1200"
        self.master.maxsize(1200, 600)
        # not sure about expand
        self.pack(expand=True)
        self.create_widgets()

    def create_widgets(self):
        heigth_left = 4
        width_left = 18
        heigth_rigth = 2
        width_rigth = 89
        # create a frame to take the left widget
        self.left_frame = tk.Frame(self.master)
        self.left_frame["bg"] = "black"
        self.left_frame["borderwidth"] = 1
        self.left_frame.pack(side="left")

        # create a frame to take the left widget
        self.right_frame = tk.Frame(self.master)
        self.right_frame["bg"] = "grey"
        self.right_frame["borderwidth"] = 1
        self.right_frame.pack(side="right")

        # create menubar
        self.menu_bar = tk.Menu(self.master)
        self.menu_bar["bg"] = "DarkOliveGreen4"

        # create a sub menu "file"
        self.menu_file = tk.Menu(self.menu_bar)
        self.menu_file["bg"] = "DarkOliveGreen1"
        self.menu_file.add_command(label="New")
        self.menu_file.add_command(label="Load")
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Quit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.menu_file)
        # tag the menu in the window
        self.master.config(menu=self.menu_bar)

        # create a button to add new employees
        self.add_employee = tk.Button(self.left_frame, width=width_left,
                                      height=heigth_left, command=self.add_emp_frame)
        self.add_employee["text"] = "Add New Employee"

        # create a button update info of employee
        self.update_employee = tk.Button(self.left_frame, width=width_left,
                                         height=heigth_left, command=self.update_emp_frame)
        self.update_employee["text"] = "Update Employee Info"

        # quit application
        self.quit = tk.Button(self.left_frame, text="QUIT", fg="red",
                              width=width_left, height=heigth_left,
                              command=self.master.destroy)
        # create a button to get the calendar
        self.get_calendar = tk.Button(self.left_frame, text="Calendar", width=width_left,
                                      height=heigth_left, command=self.get_calendar_frame)

        # create label display week
        self.label_week = tk.Label(self.right_frame, width=width_rigth,
                                   height=heigth_rigth, padx=10, pady=10)
        self.label_week["text"] = "Week May 2 to May 9"

        # create label display schedule/request
        self.label_schedule = tk.Label(self.right_frame, width=width_rigth,
                                       height=heigth_rigth, padx=10, pady=10)
        self.label_schedule["text"] = "Schedule"
        self.label_schedule["anchor"] = "s"
        self.label_schedule["justify"] = "center"

        # create label empty
        self.label_bottom = tk.Label(self.right_frame, width=width_rigth,
                                     height=heigth_rigth, padx=10, pady=10)

        # create combobox
        choice = ["Java", "Python", "C"]
        self.combo_box = ttk.Combobox(self.left_frame, width=width_left,
                                      values=choice)
        
        
        # a = self.treeview.column('#1', option=width)
        # print(a)

        self.right_frame.bind("<Button-1>", self.mouse)
        # self.treeview.bind("<Button-1>", self.mouse)#refer to calendar.py
        # add items to the frame
        self.add_employee.pack()
        self.update_employee.pack()
        self.quit.pack()
        self.get_calendar.pack()
        self.label_week.pack()
        self.label_schedule.pack()
        calendar(self)
       
        self.combo_box.pack()
        self.label_bottom.pack()

    def add_emp_frame(self):
        newWindow = tk.Toplevel(self.master)
        newWindow.title("Employee Info")
        newWindow.resizable(height=0, width=0)

        new_frame = tk.Frame(newWindow, bd=2, padx=10, pady=10, relief=GROOVE)
        new_frame.pack()

        label_first_name = tk.Label(
            new_frame, text="First Name", padx=10, pady=10)
        label_last_name = tk.Label(
            new_frame, text="Last Name", padx=10, pady=10)
        label_position = tk.Label(new_frame, text="Position", padx=10, pady=10)
        label_wage = tk.Label(new_frame, text="Wage", padx=10, pady=10)
        label_space = tk.Label(new_frame, width=5)

        self.entry_first_name = tk.Entry(new_frame, width=25)
        self.entry_last_name = tk.Entry(new_frame, width=25)
        self.entry_position = tk.Entry(new_frame, width=25)
        self.entry_wage = tk.Entry(new_frame, width=25)

        widgets = self.entry_first_name, self.entry_last_name, self.entry_position, self.entry_wage

        button_save = tk.Button(new_frame, text="Save", padx=20,
                                command=self.save_emp)
        button_clear = tk.Button(new_frame, text="Clear All", padx=10,
                                 command=self.clear_emp(widgets))
        button_read = tk.Button(new_frame, text="Read", padx=20,
                                command=self.read_emp)

        #command = f_name = text_first_name.get()
        label_first_name.grid(row=0, column=0)
        self.entry_first_name.grid(row=0, column=1)
        label_last_name.grid(row=1, column=0)
        self.entry_last_name.grid(row=1, column=1)
        label_position.grid(row=2, column=0)
        self.entry_position.grid(row=2, column=1)
        label_wage.grid(row=3, column=0)
        self.entry_wage.grid(row=3, column=1)
        button_clear.grid(row=4, column=0)
        button_save.grid(row=4, column=1)
        button_read.grid(column=3, row=4)
        label_space.grid(column=3)

    def save_emp(self):

        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        position = self.entry_position.get()
        wage = self.entry_wage.get()

        self.entry_first_name["bg"] = "white"
        self.entry_last_name["bg"] = "white"
        self.entry_position["bg"] = "white"
        self.entry_wage["bg"] = "white"

        entries = (first_name, last_name, position, wage)
        if first_name == "":
            self.entry_first_name["bg"] = "red"
        elif last_name == "":
            self.entry_last_name["bg"] = "red"
        elif position == "":
            self.entry_position["bg"] = "red"
        elif wage.isdigit():
            t = table()
            t.add_emp_table(f_name=first_name, l_name=last_name,
                            pos=position, wage=wage)
        else:
            self.entry_wage["bg"] = "red"

    def read_emp(self):
        t = table()
        t.read_emp_table()

    def clear_emp(self, widgets):

        first_name, last_name, position, wage = widgets
        first_name.delete(0, END)
        last_name.delete(0, END)
        position.delete(0, END)
        wage.delete(0, END)

    def load_emp(self, employees, widgets):

        first_name, last_name, position, wage = widgets
        id_choice = first_name.current()

        last_name.delete(0, END)
        position.delete(0, END)
        wage.delete(0, END)
        # to fit index
        id_choice += 1

        print(id_choice)
        for emp in employees:
            if emp[0] == id_choice:
                if emp[0] == id_choice:
                    last_name.insert(10, emp[2])
                    position.insert(10, emp[3])
                    wage.insert(10, emp[4])

    def delete_emp(self, employees):

        pass

    def update_emp_frame(self):

        newWindow = tk.Toplevel(self.master)
        newWindow.title("Employee Info")
        newWindow.resizable(height=0, width=0)

        new_frame = tk.Frame(newWindow, bd=2, padx=10, pady=10, relief=GROOVE)
        new_frame.pack()

        label_first_name = tk.Label(
            new_frame, text="First Name", padx=10, pady=10)
        label_last_name = tk.Label(
            new_frame, text="Last Name", padx=10, pady=10)
        label_position = tk.Label(new_frame, text="Position", padx=10, pady=10)
        label_wage = tk.Label(new_frame, text="Wage", padx=10, pady=10)
        label_space = tk.Label(new_frame, width=5)

        #entry_first_name = tk.Entry(new_frame, width=25)
        entry_last_name = tk.Entry(new_frame, width=25)
        entry_position = tk.Entry(new_frame, width=25)
        entry_wage = tk.Entry(new_frame, width=25)

        button_save = tk.Button(new_frame, text="Save", padx=20,
                                command=self.save_emp)
        button_delete = tk.Button(new_frame, text="Delete", padx=10,
                                  command=self.clear_emp)
        button_load = tk.Button(new_frame, text="Load", padx=20,
                                command=lambda: self.load_emp(employees, widgets))

        # create combobox
        t = table()
        employees = t.read_emp_table()
        choice = []
        for emp in employees:
            #index = employees.index(emp)
            print(emp[0:2])
            choice.append(emp[0:2])

        combo_first_name = ttk.Combobox(new_frame, width=22,
                                        values=choice)

        widgets = combo_first_name, entry_last_name, entry_position, entry_wage

        label_first_name.grid(row=0, column=0)
        combo_first_name.grid(row=0, column=1)
        label_last_name.grid(row=1, column=0)
        entry_last_name.grid(row=1, column=1)
        label_position.grid(row=2, column=0)
        entry_position.grid(row=2, column=1)
        label_wage.grid(row=3, column=0)
        entry_wage.grid(row=3, column=1)
        button_delete.grid(row=4, column=0)
        button_save.grid(row=4, column=1)
        button_load.grid(column=3, row=4)
        label_space.grid(column=3)

    def get_calendar_frame(self, select=None, info=None, old_window=None):

        if old_window is not None:
            old_window.destroy()

        t = table()
        week_days = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday',
                     'Saturday', 'Sunday']
        if (select is not None) and (info is not None):
            year, month, first_day = t.get_calendar(select, info)

        else:
            year, month, first_day = t.get_calendar()
            print(month)
        date = year + month
        list_month = []
        y = ''

        for x in month:
            if (x != ' ') and (x != '\n'):
                y += x
            else:
                if y != '':
                    list_month.append(y)
                    y = ''
        # get the month first
        str_month = list_month.pop(0)
        # add the year, use it for the label
        str_month = str_month + ' ' + list_month.pop(0)

        count = 0
        #print(f"Before the while, date(len), {len(date)}")
        while count < 7:
            #print(f"Count: {list_month.pop(0)}")

            count += 1
        for day in week_days:
            if day != first_day:
                list_month.insert(0, ' ')
            else:
                break

        newWindow = tk.Toplevel(self.master)
        newWindow.title("Calendar")
        newWindow.resizable(height=0, width=0)

        new_frame = tk.Frame(newWindow, bd=2, height=300, width=600,
                             padx=10, pady=10, relief=GROOVE)
        new_frame.pack()

        label_date = tk.Label(new_frame, text=str_month, padx=10, pady=10)
        btn_select = tk.Button(new_frame, text="Select", padx=10, pady=10,
                               command=self.selection_calendar)
        btn_previous = tk.Button(new_frame, text="<<", padx=10, pady=10,
                                 command=lambda: self.get_calendar_frame('previous', date, newWindow))
        btn_next = tk.Button(new_frame, text=">>", padx=10, pady=10,
                             command=lambda: self.get_calendar_frame('next', date, newWindow))

        # calendar rows and columns

        trvw_calendar = ttk.Treeview(new_frame)

        trvw_calendar['columns'] = week_days

        for x in week_days:
            trvw_calendar.column(x, width=50, anchor='center')

        trvw_calendar.column('#0', width=5)

        count = 0
        for day in month:
            if day == ' ':
                count += 1
            else:
                break
        #print("count is: " + str(count))

        # init width of the column of the calendar
        count = 1
        while count > 7:
            x = '#' + count
            trvw_calendar.column(x, width=70)
            count += 1

        for x in week_days:
            trvw_calendar.heading(x, text=x)

        #days = ['OFF','OFF','OFF','OFF','OFF','OFF','OFF']

        self.weeks_dict = {0: 1}
        count = 1
        print(40*'*')
        while count < 6:

            trvw_calendar.insert('', 'end', text=' ', values=list_month)
            x = 0
            self.weeks_dict[count] = list_month.pop(0)
            while x < 6:
                pop = list_month.pop(0)
                #print(f"pop: {pop}")
                x += 1
            count += 1

        #trvw_calendar.bind('<<TreeviewSelect>>', self.selection_calendar)
        label_date.grid(row=0, column=1)
        trvw_calendar.grid(row=1, column=0, columnspan=3)
        btn_previous.grid(row=2, column=0)
        btn_select.grid(row=2, column=1)
        btn_next.grid(row=2, column=2)
        # delete later
        self.treeview = trvw_calendar

    def selection_calendar(self):
        s = self.treeview.selection()
        if s:
            print(f"Selection: {s}")
            if s[0] == 'I001':
                sel = self.weeks_dict.get(1)
                if sel == ' ':
                    print("Selection is -1")
                else:
                    print(f"Selection is {sel}")

            elif s[0] == 'I002':
                sel = self.weeks_dict.get(2)
                print(f"Selection is {sel}")

            elif s[0] == 'I003':
                sel = self.weeks_dict.get(3)
                print(f"Selection is {sel}")

            elif s[0] == 'I004':
                sel = self.weeks_dict.get(4)
                print(f"Selection is {sel}")

            elif s[0] == 'I005':
                sel = self.weeks_dict.get(5)
                print(f"Selection is {5}")

            else:
                print("Error selection")

        else:
            print("Need a week selected")

    def select_emp_sched(self):
        pass

    def mouse(self, e):
        print("event")
        print(f"cliked at x={e.x}, y={e.y}")
