# PROGRAM TO CREATE A SIMPLE TEXTBOX IN THE WNDOW

from tkinter import Tk, Entry

window = Tk()
textbox = Entry( window, width = 50 )
textbox.pack()
window.mainloop()