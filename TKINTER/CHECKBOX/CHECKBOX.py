# PROGRAM TO ILLUSTRATE CHECKBOX SYNTAX

from tkinter import Tk, Label, Checkbutton, Button, IntVar

def Submit( x ) : 
	global label
	
	label.grid_forget()
	label[ "text" ] = "Your Response : " + str( x )
	label.grid( row = 2 )

window = Tk()

x = IntVar()
check = Checkbutton( window, text = "Check this box.", variable = x )
submit = Button( window, text = "SUBMIT", command = lambda : Submit( x.get() ) )
label = Label( window, text = "" )

check.grid( row = 0 )
submit.grid( row = 1 )

window.mainloop()