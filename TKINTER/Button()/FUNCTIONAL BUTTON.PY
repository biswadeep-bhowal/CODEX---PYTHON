# PROGRAM TO CREATE A BUTTON CLICKING WHICH WILL TRIGGER A FUNCTION

from tkinter import Tk, Label, Button 

window = Tk()

def button_function() : 
	mylabel = Label( window, text = "You clicked the Button !" ) 
	mylabel.pack()

b = Button( window, text = "Click Me !", command = button_function ) # THE FUNCTION IS CALLED WITHOUT THE ()
b.pack()

window.mainloop()