# PROGRAM TO GENERATE THE SHOWWARNING MESSAGE BOX

from tkinter import Tk, Button, messagebox

window = Tk()

button = Button( window, text = "Click Me!", command = lambda : messagebox.showwarning( "TITLE", "MESSAGE" ) )
button.pack()

window.mainloop()