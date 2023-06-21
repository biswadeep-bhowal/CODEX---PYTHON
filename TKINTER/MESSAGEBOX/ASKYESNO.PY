# PROGRAM TO GENERATE THE ASKYESNO MESSAGE BOX

from tkinter import Tk, Button, messagebox

def display_messagebox() : messagebox.askyesno( "TITLE", "MESSAGE" )

window = Tk()

Button( window, text = "Click Me!", command = lambda : display_messagebox() ).pack()

window.mainloop()