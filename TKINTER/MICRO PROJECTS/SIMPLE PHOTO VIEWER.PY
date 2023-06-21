# PROGRAM TO CREATE A SIMPLE PHOTO VIEWER 

from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

class simple_photo_viewer : 

	def __init__( self ) : self.launch_gui()

	# THESE IMAGES WERE OBTAINED FROM A FIXED DIRECTORY SO SELF IS NOT PASSED INTO THE METHOD
	def get_images( self ) :

		images = [] 

		images.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\lion.jpg" ) ) )
		images.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\trees.jpg" ) ) ) 
		images.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\bird.jpg" ) ) )
		images.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\avenue.jpg" ) ) )
		images.append( ImageTk.PhotoImage( Image.open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\IMAGES\river.jpg" ) ) )

		return images 

	def launch_gui( self ) : 

		self.window = Tk()
		self.window.title( "Photos" )
		#self.window.iconbitmap( "C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\TKINTER\ICONS\photos.ico" )

		self.images = self.get_images()
		self.image_index = 0

		self.back = Button( self.window, text = "<<", state = "disabled", command = lambda : self.BACK() )
		self.quit = Button( self.window, text = "EXIT", command = self.window.quit )
		self.next = Button( self.window, text = ">>", command = lambda : self.NEXT() )

		self.picture = Label( self.window, image = self.images[ self.image_index ] )
		self.status = Label( self.window, text = "Image {} of {}".format( self.image_index + 1, len( self.images ) ) ) 

		self.back.grid( row = 1, column = 0 )
		self.quit.grid( row = 1, column = 1 )
		self.next.grid( row = 1, column = 2 )
		self.status.grid( row = 2, column = 1, columnspan = 3 )

		self.picture.grid( row = 0, column = 0, columnspan = 3 )


		self.window.mainloop()


	def NEXT( self ) :
		
		if( self.image_index < 4 ) : 
			self.image_index += 1
			
			self.picture.grid_forget()
			self.picture = Label( self.window, image = self.images[ self.image_index ] )
			self.picture.grid( row = 0, column = 0, columnspan = 3 )

			self.status[ "text" ] = "Image {} of {}".format( self.image_index + 1, len( self.images ) )
			self.status.grid( row = 2, column = 1, columnspan = 3 )

			if( self.image_index == 4 ) : self.next[ "state" ] = "disabled" 
			if( self.image_index > 0 ) : self.back[ "state" ] = "active"
		else : self.next[ "state" ] = "disabled"



	def BACK( self ) : 
		
		if( self.image_index > 0 ) : 
			self.image_index -= 1
			
			self.picture.grid_forget()
			self.picture = Label( self.window, image = self.images[ self.image_index ] )
			self.picture.grid( row = 0, column = 0, columnspan = 3 )


			self.status[ "text" ] = "Image {} of {}".format( self.image_index + 1, len( self.images ) )
			self.status.grid( row = 2, column = 1, columnspan = 3 )

			if( self.image_index == 0 ) : self.back[ "state" ] = "disabled"
			if( self.image_index < 4 ) : self.next[ "state" ] = "active"
		else : self.back[ "state" ] = "disabled"


simple_photo_viewer()