# PROGRAM TO CLEAR A TEXTBOX AFTER CLICKING AN ASSOCIATED BUTTON

from tkinter import Tk, Entry, Button

def clear() : 
	global textbox 
	textbox.delete( 0, "end" )

window = Tk()

textbox = Entry( window, width = 50, text = "Your text goes here..." )
clear_button = Button( window, text = "CLEAR", command = clear )

textbox.grid( row = 0, column = 0 )
clear_button.grid( row = 0, column = 1 )

window.mainloop()