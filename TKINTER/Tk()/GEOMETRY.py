# PROGRAM TO SIZE THE TK() WINDOW

from tkinter import Tk, Label

window = Tk()
window.geometry( "1000x1000" )

Label( window, text = "This Tk() window is 1000x1000", bg = "WHITE", padx = 1000, pady = 1000 ).pack()

window.mainloop()