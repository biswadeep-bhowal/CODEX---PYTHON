# PROGRAM TO INSERT SLIDERS

from tkinter import Tk, Scale

window = Tk()
window.title( "Sliders" )

vertical = Scale( window, from_ = 0, to = 1000, orient = "vertical" )
horizontal = Scale( window, from_ = 0, to = 1000, orient = "horizontal" )

vertical.pack()
horizontal.pack()

window.mainloop()