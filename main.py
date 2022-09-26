#imports
import tkinter 
import sqlite3 as sql
import csv

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
sidebar = tkinter.Frame(tk, width=300,height=800, borderwidth=4, bg="grey")
sidebar.pack(side="right", fill=tkinter.Y)
#
# Creates updating variables
def updates():
    
    tk.after(1,updates)
tk.after(101, updates)

#Creates database
connection = sql.connect("clients.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS clients(firstName TEXT, lastName TEXT, email TEXT, Topics TEXT)")

#script for importing csv files
def importCSV():
    with open('','r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['firstName'], i['lastName'], i['email'], i['Topics']) for i in dr]
    cursor.executemany("INSERT INTO clients (firstName, lastName, email, Topics) VALUES (?, ?, ?, ?);", to_db)

#Creates imports window
importFrame = tkinter.Frame(tk, bg="white", width=100, height=100)

def ImportFrameSidebar():
    importFrame.pack(fill=tkinter.BOTH, expand=1)

importButtonSidebar = tkinter.Button(sidebar, text="Import", width=33,height=5, command=ImportFrameSidebar)
importButtonSidebar.place(x=0,y=0)




tk.mainloop()