# PROGRAM TO INSERT IMAGE IN THE WINDOW

from tkinter import Tk, Label
from PIL import Image, ImageTk

window = Tk()
# ImageTk.PhotoImage can only be called after Tk()
my_image = ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\IMAGE.JPEG" ) )	# STORING THE IMAGE IN A VARIABLE
# SINCE IMAGE WAS IN SAME DIRECTORY, ABSOLUTE OR RELATIVE PATH NOT REQUIRED.
my_label = Label( window, image = my_image )
my_label.pack()

window.mainloop()