# PROGRAM TO ILLUSTRATE USE OF pack() method

from tkinter import Tk, Label

window = Tk()

label = Label( window, text = "Hello World !" )
label.pack()

window.mainloop()