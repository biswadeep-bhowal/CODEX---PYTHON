# PROGRAM TO USE THE grid() METHOD INSTEAD OF pack() 

from tkinter import Tk, Label

window = Tk()
mylabel = Label( window, text = "This is some text" )
mylabel.grid( row = 0, column = 0 )	# THE grid() METHOD PUTS THE WIDGET INSIDE THE WINDOW ACCORDING TO ROW AND COLUMN. ROW AND COLUMN ARE RELATIVE HERE.
window.mainloop()