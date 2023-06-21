# PROGRAM TO SET BACKGROUND COLOUR OF LABEL FRAME

from tkinter import Tk, Label, LabelFrame

window = Tk()

label_frame = LabelFrame( window, text = "This Label Frame has a blue background", bg = "BLUE", padx = 10, pady = 10 )
framed_label = Label( label_frame, text = "Framed Label" )

label_frame.pack()
framed_label.pack()

window.mainloop()