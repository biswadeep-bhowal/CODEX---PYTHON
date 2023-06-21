# PROGRAM TO DISPLAY HELLO WORLD IN TKINTER WINDOW

from tkinter import Tk, Label

window = Tk()
text = Label( window, text = "Hello World" ) # THIS WIDGET IS USED TO INSERT TEXT AND IMAGES IN THE WINDOW
text.pack()	# THE PACK METHOD PUTS THE TEXT IN THE DIALOG BOX CENTRE ALIGNED
window.mainloop()