# PROGRAM TO EXECUTE SQLITE3 QUERIES ON THE STUDENT TABLE VIA USER INPUT IN REPL

from sqlite3 import connect

def display( star = None, rowid = None, name = None, roll = None, marks = None, records = None) : 
	
	col = list()
	
	if( star != None and rowid != None ) : col = [ "Row ID", "Name", "Roll No.", "Marks" ] 
	elif( star != None ) : col = [ "Name", "Roll No.", "Marks" ]
	else :
		if( rowid != None ) : 	col.append( "Row ID" )
		if( name != None ) : 	col.append( "Name" )
		if( roll != None ) : 	col.append( "Roll No." )
		if( marks != None ) : 	col.append( "Marks" )		

	for j in range( len( col ) ) : print( col[ j ].ljust( 20 ), end = '' )
	print( "\n", end = "-"*60 )
	print()

	for i in range( len( records ) ) : 
		for j in range( len( records[ 0 ] ) ) : print( str( records[ i ][ j ] ).ljust( 20 ), end = '' ) 
		print()


#DRIVER CODE
con = connect( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\SQLite 3\DATABASES\STUDENT.db" )
cur = con.cursor()
command = str()

while( True ) : 
	command = input( "\nSQLite3> " )
	check = command.upper()

	if( check == "EXIT" or check == "QUIT" ) : break

	elif( check == "CLEAR" or check == "CLS" ) : print( "\n"*50 )
	
	elif( "SELECT" in command.upper() ) :

		try :
			cur.execute( command )	
			records = cur.fetchall()

			if( "*" in check and "ROWID" not in check ) : display( star = 1, records =  records )
			else :
				
				rowid = 1	if "ROWID" in check or "*" in check	else None
				name = 1 	if "NAME" in check 	or "*" in check else None
				roll = 1 	if "ROLL" in check 	or "*" in check else None
				marks = 1 	if "MARKS" in check or "*" in check else None

				if( rowid == name == roll == marks == 1 ) : display( star = 1, rowid = 1, records =  records )
				else : 										display( rowid = rowid, name = name, roll = roll, marks = marks, records = records )
		
		except Exception as e : print( "\nError :", e )
	
	else :											
		try : cur.execute( command )
		except Exception as e : print( "\nError :", e )

con.commit()
con.close()