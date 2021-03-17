# from Main_Window import Main_Window
from gui import Main_Frame
import tkinter as tk
import file
from file import *
root = tk.Tk()
root.geometry("600x400")
app = Main_Frame(master=root)
app.mainloop()

emp = {
    'id': '',
    'Name': "",
    'Surname': '',
    'Age': 0
}

test = "test"
f = file()
f.write_file(emp)
data = f.read_file()
f.print_table(data)
