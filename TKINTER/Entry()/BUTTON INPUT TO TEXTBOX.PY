# PROGRAM TO PRINT CHARACTERS ON A TEXTBOX FROM A BUTTON

from tkinter import Tk, Button, Entry

def click( textbox, string ) : 
	textbox.insert( "end", string )


window = Tk()

textbox = Entry( window, width = 50 )
button = Button( window, text = "Hello", command = lambda : click( textbox, "Hello" ) )

textbox.grid( row = 0, column = 0 )
button.grid( row = 1, column = 0 )

window.mainloop()