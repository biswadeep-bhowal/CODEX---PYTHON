# PROGRAM TO TAKE INPUT FROM TEXT BOX

from tkinter import Tk, Label, Entry, Button


# BUTTON COMMAND

def click() : 
	global textbox
	Label( window, text = "Your name is "+textbox.get() ).grid( row = 1, columnspan = 3 )	# get() METHOD IS USED TO GET THE INPUT STRING 

# DRIVER CODE

window = Tk()

field_name = Label( window, text = "Enter your name : ", anchor = "w" )
textbox = Entry( window, width = 50 )
enter_button = Button( window, text = "ENTER", command = click )

field_name.grid(   row = 0, column = 0 )
textbox.grid(      row = 0, column = 1 )
enter_button.grid( row = 0, column = 2 )

window.mainloop()

