# PROGRAM TO CREATE A COLOURFUL BUTTON

from tkinter import Tk, Label, Button 

window = Tk()
Button( window, text = "Hello World", fg = "BLUE", bg = "YELLOW" ).pack()	# FOREGROUND AND BACKGROUND COLOUR. HEXADECIMAL COLOUR CODES ALSO WORK.
window.mainloop()