import tkinter 
import sqlite3

tk = tkinter.Tk()
tk.geometry("1500x800")

def screensizeGrab():
    global screensize
    global screensizeWidth
    global screensizeHeight
    screensize = tk.winfo_geometry()
    screensizeHeight = tk.winfo_height()
    screensizeWidth = tk.winfo_width()
    tk.after(100, screensizeGrab)
tk.after(100, screensizeGrab)
sidebar = tkinter.Frame(tk, width=30,height=400, borderwidth=4, bg="grey")
sidebar.pack(side="right")

def updates():
    sidebar.config(height=screensizeHeight)
    tk.after(1,updates)
tk.after(101, updates)
tk.mainloop()