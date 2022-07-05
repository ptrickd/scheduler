import sqlite3
from sqlite3 import Error
import os
import calendar
from datetime import *

class db():

    def connect_sql():
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print("directory: " + dir_path)
        path = dir_path + "\qwe.sqlite"
        print("Path: " + path)
        
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("connection to SQLite DB sucessful")
        except Error as e:
            print(f"The error '{e}' occurred")
        
        return connection