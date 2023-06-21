# PROGRAM TO MAKE A CALCULATOR APP

from tkinter import Tk, Entry, Button

class calculator : 

	def __init__( self ) : 
		self.window = Tk()
		self.window.title( "CALCULATOR" )
		self.window.configure( bg = "BLACK" )

		self.textbox = Entry( self.window, width = 94, borderwidth = 10 )
		self.textbox.grid( row = 0, column = 0, columnspan = 4 )
		
		self.buttons = self.generate_buttons()
		self.place_buttons()
		
		self.window.mainloop()

	def button( self, t, x, y ) : return Button( self.window, text = t, bg = "BLACK", fg = "WHITE", padx = x, pady = y, command = lambda : self.textbox.insert( "end", t ) )
	def generate_buttons( self ) : 
		buttons = []
		
		for i in range( 10 ) : buttons.append( self.button( str( i ), 66, 20 ) )	# buttons[ 0 : 10 ]
		
		buttons.append( Button( self.window, text = 'CLEAR', bg = "BLACK", fg = "WHITE", padx = 272, pady = 20, command = lambda : self.textbox.delete( 0, "end" ) ) )	# buttons[ 10 ]

		buttons.append( self.button( '+', 64.5, 20 ) )
		buttons.append( self.button( '-', 66, 20 ) )
		buttons.append( self.button( '*', 66, 20 ) )
		buttons.append( self.button( '/', 66, 20 ) )
		buttons.append( self.button( ' .', 66, 20 ) )

		buttons.append( Button( self.window, text = '=', bg = "BLACK", fg = "WHITE", padx = 65, pady = 20, command = lambda : self.result() ) )	# buttons[ 16 ]

		return buttons

	def place_buttons( self ) : 
		
		self.buttons[ 7 ].grid(		row = 1, column = 0 )
		self.buttons[ 8 ].grid( 	row = 1, column = 1 )
		self.buttons[ 9 ].grid( 	row = 1, column = 2 )
		self.buttons[ 11 ].grid( 	row = 1, column = 3 )

		self.buttons[ 4 ].grid( 	row = 2, column = 0 )
		self.buttons[ 5 ].grid( 	row = 2, column = 1 )
		self.buttons[ 6 ].grid( 	row = 2, column = 2 ) 
		self.buttons[ 12 ].grid( 	row = 2, column = 3 )

		self.buttons[ 1 ].grid( 	row = 3, column = 0 )
		self.buttons[ 2 ].grid( 	row = 3, column = 1 )
		self.buttons[ 3 ].grid( 	row = 3, column = 2 )
		self.buttons[ 13 ].grid( 	row = 3, column = 3 )

		self.buttons[ 15 ].grid( 	row = 4, column = 0 )
		self.buttons[ 0 ].grid( 	row = 4, column = 1 )
		self.buttons[ 16 ].grid( 	row = 4, column = 2 )
		self.buttons[ 14 ].grid( 	row = 4, column = 3 )
		
		self.buttons[ 10 ].grid( 	row = 5, column = 0, columnspan =4 )

	def result( self ) :
		expression = self.remove_zeroes()
		self.textbox.delete( 0, "end" )
		self.textbox.insert( 0, expression )
		
		

	def remove_zeroes( self ) :

		exp = "".join( list( map( str, self.textbox.get().split() ) ) )		# Taking care of spaces.

		num = str()
		delimiters = [ "+", "-", "*", "/", "//", "(", ")" ]
		terms = []

		for i in range( len( exp ) ) : 

			if( exp[ i ] == ) : 





calculator()