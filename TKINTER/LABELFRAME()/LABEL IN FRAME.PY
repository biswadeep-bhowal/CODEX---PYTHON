# PROGRAM TO INSERT LABEL INSIDE LABELFRAME

from tkinter import Tk, Label, LabelFrame 

window = Tk()

label_frame = LabelFrame( window, padx = 10, pady = 10 )
framed_label = Label( label_frame, text = "This is a Label inside the frame" )

label_frame.pack()
framed_label.pack()

window.mainloop()