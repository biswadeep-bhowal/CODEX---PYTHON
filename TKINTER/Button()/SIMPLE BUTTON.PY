# PROGRAM TO CREATE A SIMPLE BUTTON. THIS BUTTON HAS NO FUNCTION

from tkinter import Tk, Button 

window = Tk()
b = Button( window, text = "Button" )	# THE Button WIDGET CREATES A BUTTON
b.pack()
window.mainloop()