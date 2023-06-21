# PROGRAM TO GENERATE THE SHOWINFO MESSAGE BOX

from tkinter import Tk, Button, messagebox

def display_messagebox() : messagebox.showinfo( "TITLE", "MESSAGE" )

window = Tk()

button = Button( window, text = "Click Me!", command = lambda : messagebox.showinfo( "TITLE", "MESSAGE" ) )
button.pack()

window.mainloop()