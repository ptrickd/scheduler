import sqlite3
from sqlite3 import Error
import os
import calendar
from datetime import *

class table():

    
        
    def delete_emp_table(self, iD):
        connection = self.create_table()
        
        delete_emp = "DELETE FROM emp WHERE id = iD"
        execute_query(connexion, delete_emp)
        
               
    def execute_query(self, connection, query, var):
        print("Query: " + query)
        if var == None:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                print("Query executed successfully")
            except Error as e:
                print(f"The error '{e}' occured")
        else:
            cursor = connection.cursor()
            try:
                cursor.execute(query, var)
                print("Query executed successfully")
            except Error as e:
                print(f"The error '{e}' occured")
        #save the change
        connection.commit()
            
    def execute_read_query(self, connection, query):
        if connection:
            cursor = connection.cursor()
            result = None
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(f"The error '{e}' occured")
            
    
    
    def read_emp_table(self):
        connection = self.connect_sql()
        
        select_emps = "SELECT * from emp"
        
        emps = self.execute_read_query(connection, select_emps)
        
       
        connection.close()
        for emp in emps:
            print(emp)
            
        return emps
    
    def get_calendar(self, select=None, info=None):
       
        if (select is not None) and (info is not None):
            dateS = datetime()
            date = str(dateS)
            year = dateS.strftime("%Y")
            month34 = dateS.strftime("%m")
            if select == 'next':
                if month34 == '12':
                    print(f"Year = {year}, Month = {month34}")
                else:
                    #add 1 month 
                    pass
                print(30*"*")
            elif select == 'previous':
                j=0
                date = ''
                for x in info:
                    if j == 6:
                        #take out 1 month
                        x = str( int(x) - 1 )
                    date += x
                    j += 1
                date += ' ' 
            else:
                pass
        else:
            dateS = datetime.today()
            date = str(dateS)
            year = dateS.strftime("%Y")
            month34 = dateS.strftime("%m")
            print(f"Year = {year}, Month = {month34}")
        
        #date = str(datetime.today())
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday',
                'Saturday','Sunday']
        c = calendar.TextCalendar(calendar.MONDAY)
        #print(f"month = {int(date[5:7])}")
        #Give a string for the whole month
        month = c.formatmonth(int(year), int(month34))
      
        #Take year, month, gives first day and number of days
        
        month_range = calendar.monthrange(int(year), int(month34[1]))
        first_day = days[int(month_range[0])]
               
        return year, month, first_day
        
        
        
def var_calendar(self):
    
    pass