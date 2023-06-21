# PROGRAM TO USE ONVALUE AND OFFVALUE OF CHECKBOX

from tkinter import Tk, Label, Checkbutton, Button, StringVar

window = Tk()

def Submit() : 
	global window, a1, a2, var1, var2

	a1.grid_forget()
	a2.grid_forget()

	a1[ "text" ] = var1.get()
	a2[ "text" ] = var2.get()

	a1.grid( row = 3 )
	a2.grid( row = 4 )


var1, var2 = StringVar(), StringVar()
q1 = Checkbutton( window, text = "Jobseeker", variable = var1, onvalue = "You are looking for a job", offvalue = "You are not looking for a job" )
q2 = Checkbutton( window, text = "Student", variable = var2, onvalue = "You are a student", offvalue = "You are not a student"  )

q1.deselect()	# THE DESELECT() FUNCTION HAS TO BE CALLED WHENEVER ONVALUE AND OFFVALUE ARE USED IN CHECKBUTTONS
q2.deselect()

submit = Button( window, text = "SUBMIT", bg = "WHITE", fg = "BLUE", padx = 15, pady = 20, command = Submit  )

a1 = Label( window, text = var1.get() )
a2 = Label( window, text = var2.get() )

q1.grid( row = 0 )
q2.grid( row = 1 )

submit.grid( row = 2 )

window.mainloop()