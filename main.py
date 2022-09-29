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

#Creates window for adding to database
new_frame = tkinter.Frame(tk, bg="red", width=100, height=100)

def NewFrameSideBar():
    import_frame.pack_forget()
    new_frame.pack(fill=tkinter.BOTH,expand=1)

new_frame_sidebar = tkinter.Button(sidebar,text="Add", width=33, height=5,command=NewFrameSideBar)
new_frame_sidebar.pack(anchor=tkinter.N)


#script for importing csv files
def importCSV():
    with open('','r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['firstName'], i['lastName'], i['email'], i['Topics']) for i in dr]
    cursor.executemany("INSERT INTO clients (firstName, lastName, email, Topics) VALUES (?, ?, ?, ?);", to_db)

#Creates imports window
import_frame = tkinter.Frame(tk, bg="white", width=100, height=100)

def ImportFrameSidebar():
    new_frame.pack_forget()
    import_frame.pack(fill=tkinter.BOTH, expand=1)

importButtonSidebar = tkinter.Button(sidebar, text="Import", width=33,height=5, command=ImportFrameSidebar)
importButtonSidebar.pack(anchor=tkinter.N)




tk.mainloop()
