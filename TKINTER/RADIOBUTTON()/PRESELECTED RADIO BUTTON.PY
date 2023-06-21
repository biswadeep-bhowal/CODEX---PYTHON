# PROGRAM TO KEEP A RADIO BUTTON SELECTED BY DEFAULT BEFORE USER INPUT

from tkinter import Tk, Radiobutton, IntVar

window = Tk()

choice = IntVar()
choice.set( 1 )
rdb = Radiobutton( window, text = "This is radio button is selected by default.", variable = choice, value = 1 )

rdb.pack()

window.mainloop()