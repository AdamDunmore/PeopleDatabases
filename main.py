#imports
import tkinter 
import sqlite3 as sql

#windows

tk = tkinter.Tk()
tk.geometry("1500x800")

#Gets constant screen size
def screensizeGrab():
    global screensize
    global screensizeWidth
    global screensizeHeight
    screensize = tk.winfo_geometry()
    screensizeHeight = tk.winfo_height()
    screensizeWidth = tk.winfo_width()
    tk.after(100, screensizeGrab)
tk.after(100, screensizeGrab)

#Creates Sidebar
sidebar = tkinter.Frame(tk, width=300,height=400, borderwidth=4, bg="grey")
sidebar.pack(side="right")
#
# Creates updating variables
def updates():
    sidebar.config(height=screensizeHeight)
    tk.after(1,updates)
tk.after(101, updates)

#Creates database
def databaseCreation():
    connection = sql.connect("clients.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clients(firstName TEXT, lastName TEXT, email TEXT, Topics TEXT)")
databaseCreation()
tk.mainloop()