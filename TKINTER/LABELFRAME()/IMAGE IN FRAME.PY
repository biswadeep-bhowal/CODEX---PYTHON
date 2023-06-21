# PROGRAM TO PLACE IMAGE INSIDE A LABEL FRAME

from tkinter import Tk, Label, LabelFrame
from PIL import Image, ImageTk

window = Tk()

label_frame = LabelFrame( window, text = "This is a frame", bg = "BLACK", fg = "WHITE", padx = 20, pady = 20 )

img = ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\lion.jpg" ) )
framed_image = Label( label_frame, image = img )	# master = label_frame

label_frame.pack()
framed_image.pack()

window.mainloop()