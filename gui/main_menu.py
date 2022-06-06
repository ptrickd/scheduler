#Function that create the main menu bar
import tkinter as tk

def main_menu(master):
    
    # create menubar
    menu_bar = tk.Menu(master)
    menu_bar["bg"] = "DarkOliveGreen4"

    # create a sub menu "file"
    menu_file = tk.Menu(menu_bar)
    menu_file["bg"] = "DarkOliveGreen1"
    menu_file.add_command(label="New")
    menu_file.add_command(label="Load")
    menu_file.add_separator()
    menu_file.add_command(label="Quit", command=quit)
    menu_bar.add_cascade(label="File", menu=menu_file)
    #tag the menu in the window
    master.config(menu=menu_bar)
    