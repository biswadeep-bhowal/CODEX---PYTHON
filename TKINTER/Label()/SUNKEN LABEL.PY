from tkinter import Tk, Label

window = Tk()

sunken_label = Label( window, text = "Sunken Label", relief = "sunken" )
sunken_label.pack()

window.mainloop()