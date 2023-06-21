# PROGRAM TO DETECT RADIO BUTTON CHOICE

from tkinter import Tk, Radiobutton, Label, IntVar, Button

def click( mylabel, n ) : 
	if( n == 1 ) :	mylabel[ "text" ] = "You are single."
	else : 			mylabel[ "text" ] = "You are in a relationship"
	
	mylabel.grid_forget()
	mylabel.grid( row = 4 )




window = Tk()

heading = Label( window, text = "Choose Relationship Status : " )  

choice = IntVar()
option_1 = Radiobutton( window, text = "SINGLE", variable = choice, value = 1 )
option_2 = Radiobutton( window, text = "IN A RELATIONSHIP", variable = choice, value = 2 )

button = Button( window, text = "Enter", command = lambda : click( mylabel, choice.get() ) )	# choice.get() returns current value of radio button selected

mylabel = Label( window, text = "" )

heading.grid( row = 0 )
option_1.grid( row = 1 )
option_2.grid( row = 2 )
button.grid( row = 3 )

window.mainloop()
