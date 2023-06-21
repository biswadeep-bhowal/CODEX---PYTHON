from tkinter import Tk, Label, Button

window = Tk()

sunken_button = Button( window, text = "Sunken Button", relief = "sunken" )
sunken_button.pack()

window.mainloop()