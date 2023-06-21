# PROGRAM TO CREATE A MENU FOR ORDERING PIZZA

from tkinter import Tk, Label, Button, LabelFrame, Radiobutton, IntVar
from PIL import Image, ImageTk

def get_images() : 
	img = []

	img.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\CHEESE PIZZA.jpg" ) ) )
	img.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\CHICKEN PIZZA.jpg" ) ) )
	img.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\CORN PIZZA.jpg" ) ) )
	img.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\ONION PIZZA.jpg" ) ) )
	img.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\PEPPERONI PIZZA.jpg" ) ) )

	return img 

def get_options( window ) : 
	
	opt = []
	choice = IntVar()
	
	opt.append( Radiobutton( window, text = "CHEESE", variable = choice, value = 0 ) )
	opt.append( Radiobutton( window, text = "CHICKEN", variable = choice, value = 1 ) )
	opt.append( Radiobutton( window, text = "CORN", variable = choice, value = 2 ) )
	opt.append( Radiobutton( window, text = "ONION", variable = choice, value = 3 ) )
	opt.append( Radiobutton( window, text = "PEPPERONI", variable = choice, value = 4 ) )

	return opt, choice


def order( picture_label, picture ) : 
	picture_label.grid_forget()
	picture_label[ "image" ] = picture
	picture_label.grid( row = 2 )



# DRIVER CODE

window = Tk()

options_frame = LabelFrame( window, text = "Choose a Pizza !", bg = "WHITE", padx = 20, pady = 20 )
options, choice = get_options( options_frame )

picture_frame = LabelFrame( window, bg = "BROWN" )
pictures = get_images()
picture = Label( picture_frame, image = pictures[ 0 ], padx = 10, pady = 10 )


order_button = Button( window, text = "order", anchor = "center", command = lambda : order( picture, pictures[ int( choice.get() ) ] ) )

options_frame.grid( row = 0 )

options[ 0 ].grid( row = 0, column = 0 )
options[ 1 ].grid( row = 0, column = 1 )
options[ 2 ].grid( row = 1, column = 0 )
options[ 3 ].grid( row = 1, column = 1 )
options[ 4 ].grid( row = 2, column = 0 )

order_button.grid( row = 1, column = 0, columnspan = 2 )

picture_frame.grid( row = 2 )

window.mainloop()








