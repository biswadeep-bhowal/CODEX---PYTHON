# PROGRAM TO CREATE THE QUIT OR EXIT BUTTON TO CLOSE A WINDOW.

from tkinter import Tk, Button 

window = Tk()

quit_button = Button( window, text = "EXIT", command = window.quit )
quit_button.pack()

window.mainloop()