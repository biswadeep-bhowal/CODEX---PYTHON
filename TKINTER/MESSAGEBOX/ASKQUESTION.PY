# PROGRAM TO GENERATE THE SHOWWARNING MESSAGE BOX

from tkinter import Tk, Button, messagebox

def display_messagebox() : messagebox.askquestion( "TITLE", "MESSAGE" )

window = Tk()

Button( window, text = "Click Me!", command = lambda : display_messagebox() ).pack()

window.mainloop()