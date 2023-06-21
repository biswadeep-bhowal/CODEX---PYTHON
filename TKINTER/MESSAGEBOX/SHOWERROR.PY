# PROGRAM TO GENERATE THE SHOWERROR MESSAGE BOX

from tkinter import Tk, Button, messagebox

def display_messagebox() : messagebox.showerror( "TITLE", "MESSAGE" )

window = Tk()

Button( window, text = "Click Me!", command = lambda : display_messagebox() ).pack()

window.mainloop()