# PROGRAM TO OPEN IMAGE FILES 

from tkinter import Tk, filedialog, Label
from PIL import ImageTk, Image 

window = Tk()
window.title( "Select An Image" )

window.filename = filedialog.askopenfilename( initialdir = "This PC", filetypes = ( ( "JPEG files", "*.jpg" ), ( "PNG files", "*.png" ), ( "all files", "*.*" ) ) )
# ABSOLUTE PATH TO GIVEN FILE

image = ImageTk.PhotoImage( Image.open( window.filename ) )
Label( window, image = image, bg = "BLUE" ).pack()

window.mainloop()