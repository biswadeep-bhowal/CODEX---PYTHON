# PROGRAM TO IMPLEMENT SQLITE 3 TERMINAL ON TKINTER FOR THE STUDENT DATABASE

from tkinter import Tk, Button, LabelFrame, Label, Entry
from sqlite3 import connect

class terminal : 

	def __init__( self ) : 

		# Database Initialisations
		self.con = connect( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\SQLite 3\DATABASES\STUDENT.db" )
		self.cur = self.con.cursor()

		#Tkinter initialisations
		self.window = Tk()
		self.window.geometry( "1366x768" )
		self.window.configure( background = "BLACK" )
		self.window.title( "SQLite3 Terminal" )
		#self.window.attributes( "-fullscreen", True )
		self.window.state( "zoomed" )


		self.query = LabelFrame( self.window, bg = "BLACK", fg ="WHITE" )
		self.result = LabelFrame( self.window, bg = "BLACK", fg = "WHITE" )

		self.label = Label( self.query, text = "SQLite3 > ", bg = "WHITE", fg = "BLACK" )
		self.textbox = Entry( self.query, width = 100 )
		self.submit = Button( self.query, text = "Submit", bg = "BLACK", fg = "WHITE", command = lambda : self.process() )

		self.display_label = Label( self.result, text = "Your SELECT queries appear here..", bg = "BLACK", fg = "WHITE", padx = 524 ) 


		self.placement()
		self.window.mainloop()

		self.con.commit()
		self.con.close()

	def placement( self ) : 

		self.query.grid(  row = 0 )
		self.result.grid( row = 1, sticky = "W" )

		self.label.grid(   row = 0, column = 0 )
		self.textbox.grid( row = 0, column = 1 )
		self.submit.grid(  row = 0, column = 2 )

		self.display_label.grid( row = 0, rowspan = 1 )


	def process( self ) : 
		
		command = self.textbox.get()
		self.textbox.delete( 0 , "end" )
		self.display_label.grid_forget()

		if( command == "" ) : return

		

		check = command.upper()

		if( check == "EXIT" or check == "QUIT" ) : self.window.destroy()

		elif( check in [ "CLEAR", "CLS" ] ) : 
			self.display_label[ "text" ] = str()
			self.display_label.grid_forget()
			self.display_label.grid( row = 0, colspan = 1 )
			
		elif( "SELECT" in check ) :

			try :
				self.cur.execute( command )	
				records = self.cur.fetchall()

				if( "*" in check and "ROWID" not in check ) : self.display( star = 1, records =  records )
				else :
						
					rowid = 1	if "ROWID" in check or "*" in check	else None
					name = 1 	if "NAME" in check 	or "*" in check else None
					roll = 1 	if "ROLL" in check 	or "*" in check else None
					marks = 1 	if "MARKS" in check or "*" in check else None

					if( rowid == name == roll == marks == 1 ) : self.display( star = 1, rowid = 1, records =  records )
					else : 										self.display( rowid = rowid, name = name, roll = roll, marks = marks, records = records )
				
			except Exception as e : self.textbox.insert( 0, e )
			
		else :											
			try :						self.cur.execute( command )
			except 	Exception as e : 	self.textbox.insert( 0, e ) 
					


	def display( self, star = None, rowid = None, name = None, roll = None, marks = None, records = None) : 
		
		col = []
		result = ""
		
		if( star != None and rowid != None ) : col = [ "Row ID", "Name", "Roll No.", "Marks" ] 
		elif( star != None ) : col = [ "Name", "Roll No.", "Marks" ]
		else :
			if( rowid != None ) : 	col.append( "Row ID" )
			if( name != None ) : 	col.append( "Name" )
			if( roll != None ) : 	col.append( "Roll No." )
			if( marks != None ) : 	col.append( "Marks" )		

		for j in range( len( col ) ) : result += col[ j ].ljust( 20 )
		result += "\n" + "-"*60 + "\n"  

		for i in range( len( records ) ) : 
			for j in range( len( records[ 0 ] ) ) : result += str( records[ i ][ j ] ).ljust( 20 )
			result += "\n"

		try : 
			self.display_label[ "text" ] = result
			self.display_label.grid( row = 0, columnspan = 1 )
		except Exception as e : 
			self.textbox.insert( 0, e ) 


t = terminal()