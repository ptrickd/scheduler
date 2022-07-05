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
    
    def add_emp(self, name):
        print("Name: " + name )
        
        connection = self.create_table()
        
        
        create_emp = """
        INSERT INTO
            emp (name)
        VALUES
            (?)
        """
        var = (name)
        print("After emp, before query")
        self.execute_query(connection, create_emp, var)
        
        connection.close()
    
    def create_table(self):
        connection = self.connect_sql()
        
        create_emp_table = """
        CREATE TABLE IF NOT EXISTS emp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """
        self.execute_query(connection, create_emp_table, var=None)
        
        return connection