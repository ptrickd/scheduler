# global import
import sys
sys.path.insert(0, './gui')
sys.path.insert(0, './model')


from gui1 import Main_Frame
import tkinter as tk


from model.db import db
# from db import db
# from db import db 
import file
from file import *

connect = db.connect_sql()

root = tk.Tk()
root.geometry("1100x400")
app = Main_Frame(master=root)
app.mainloop()

# emp = {
#     'id': '',
#     'Name': "",
#     'Surname': '',
#     'Age': 0
# }

# test = "test"
# f = file()
# f.write_file(emp)
# data = f.read_file()
# f.print_table(data)
