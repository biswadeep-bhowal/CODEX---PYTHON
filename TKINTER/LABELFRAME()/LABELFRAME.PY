from tkinter import *
from PIL import Image, ImageTk

window = Tk()

labelframe = LabelFrame( window, text = "This is a labelframe", padx = 5, pady = 5 )	#INTERNAL PADDING
labelframe.pack( padx = 100, pady = 100 )	# EXTERNAL PADDING

image_label = Label( labelframe, image = ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\lion.jpg" ) ) )
image_label.pack()

window.mainloop()