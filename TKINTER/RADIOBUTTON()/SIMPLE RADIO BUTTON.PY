# PROGRAM TO CREATE NO-FUNCTIONAL RADIO BUTTONS

from tkinter import Tk, Radiobutton, IntVar

window = Tk()

choice = IntVar()

option_1 = Radiobutton( window, text = "Option : 1", variable = choice, value = 1 )
option_2 = Radiobutton( window, text = "Option : 2", variable = choice, value = 2 )

option_1.pack()
option_2.pack()

window.mainloop()