# PROGRAM TO CREATE A DISABLED BUTTON

from tkinter import Tk, Button 

window = Tk()
dead_button = Button( window, text = "This is a dead button...", state = "disabled" )
dead_button.pack()
window.mainloop()