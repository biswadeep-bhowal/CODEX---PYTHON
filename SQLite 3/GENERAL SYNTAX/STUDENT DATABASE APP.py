# THIS PROGRAM USES ALL THE FUNCTIONALITIES OF SQLITE3 FOR THE STUDENT DATABASE

from sqlite3 import connect

def insert( con, cur ) : 

	ch = 'y'
	
	name = str()
	roll = int()
	marks = float()

	while( ch in "yY") : 

		name = input( "Name : " )
		roll = input( "Roll No. : " )
		marks = input( "Marks : " )

		try : cur.execute( 'INSERT INTO student VALUES ( "{}", {}, {} )'.format( name, roll, marks ) )
		except Exception as e : print( "\nError :", e )

		ch = input( "\nInsert Again ? ( Y / N ) : " )

	con.commit()





def delete( con, cur ) :

	choice = int()
	ch = 'y'

	name, roll, marks = None, None, None
	command = "DELETE FROM student WHERE "

	while( ch in "yY" ) : 

		ch = input( "Delete By Name ? ( Y / N ) : " )
		if( ch in "yY" ) :
			
			choice = int( input( """
				Delete By :
				1) Specific Name
				2) LIKE Clause
				3) Exit Deletion By Name
				
				Enter your choice : """) )
			while( choice not in [ 1, 2, 3 ] ) : choice = int( input( "INVALID INPUT...ENTER AGAIN : " ) )

			if( choice == 1 ) : 
				name = input( "\nEnter name : " )
				command += 'name = "{}" '.format( name )
			elif( choice == 2 ) : 
				
				name = input( "Enter name : " )
				choice = int( input( "Name Like :\n1)%name\n2)name%\n3)%name%\nEnter your choice : " ) )
				while( choice not in [ 1, 2, 3 ] ) : choice = int( input( "INVALID CHOICE...ENTER AGAIN : " ) )

				if( choice == 1 ) : 	name = "%" + name
				elif( choice == 2 ) : 	name = name + "%"
				else : 					name = "%" + name + "%"

				command += 'name LIKE "{}"'.format( name )


		ch = input( "\nDelete By Roll No. ? ( Y / N ) : " )
		if( ch in "yY" ) :

			choice = int( input( "\nSelect Syntax :\n1)Roll No. = value\n2)Roll No. < value\n3)Roll No. > value\n4)Exit Deletion By Roll No.\nEnter your choice : " ) )
			while( choice not in [ 1, 2, 3, 4 ] ) : choice = int( input( "INVALID CHOICE...ENTER AGAIN : " ) )
			roll = int( input( "Enter Roll No. Value : " ) )

			if( choice in [ 1, 2, 3 ] ) : 
				if( name != None ) : command += " AND "
				
				if( choice == 1 ) : 	roll = "roll = {}".format( roll )
				elif( choice == 2 ) : 	roll = "roll < {}".format( roll )
				elif( choice == 3 ) : 	roll = "roll > {}".format( roll )

				command += roll 


		ch = input( "Delete By Marks ? ( Y / N ) : " )
		if( ch in "yY" ) : 

			choice = int( input( "\nSelect Syntax :\n1)Marks = value\n2)Marks < value\n3)Marks > value\n4)Exit Deletion By Marks\nEnter your choice : " ) )
			while( choice not in [ 1, 2, 3, 4 ] ) : choice = int( input( "INVALID CHOICE...ENTER AGAIN : " ) )
			marks = int( input( "Enter Marks Value : " ) )

			if( choice in [ 1, 2, 3 ] ) : 
				if( name != None or roll != None ) : command += " AND "
				
				if( choice == 1 ) : 	marks = "marks = {}".format( marks )
				elif( choice == 2 ) : 	marks = "marks < {}".format( marks )
				elif( choice == 3 ) : 	marks = "marks > {}".format( marks )

				command += marks

		try : cur.execute( command )
		except Exception as e : print( "\nError :", e )

		ch = input( "\n\nDelete Again ? ( Y / N ) : " )

	con.commit()

"""def update( con, cur ) :

	clrscr()

	command = "UPDATE student SET "
	name, roll, marks = None, None, None
	Set, Att = int(), int()
	Set_val, Att_val = None, None
	attr = [ "Rowid", "Name", "Roll No", "Marks" ]

	Set = int( input( "SET :\n1)Name\n2)Roll No.\n3)Marks\nEnter your choice : " ) )
	while( choice not in range( 1, 4 ) ) : Set = int( input( "INVALID CHOICE...ENTER AGAIN : " ) )

	print( "Enter Value to be Set : ", end = '' )
	if( Set == 1 ) : 	Set_val = input()
	elif( Set == 2 ) : 	Set_val = int( input() )
	elif( Set == 3 ) : 	Set_val = float( input() )
	
 	Att = int( input( "Conditional Attribute :\n1)Name\n2)Roll No.\n3)Marks\nEnter your choice : " ) )
 	while( Att not in range( 1, 4 ) ) : Att = int( input( "INVALID CHOICE...ENTER AGAIN : " ) )

 	print( "\nEnter value of condition : " )
 	if( Att == 1 ) : Att_val = input()
 	elif( Att == 2 ) : Att_val = int( input() )
 elif( Att == 1 ) : Att_val = float( input() )"""





def display_full( cur ) :

	cur.execute( "SELECT * FROM student" )
	records = cur.fetchall()

	attributes = [ "Name", "Roll No.", "Marks" ]
	
	for i in range( 3 ) : print( attributes[ i ].ljust( 20 ), end = '' )  
	print( "\n", end = "-"*60 + "\n" )

	for i in range( len( records ) ) : 
		for j in range( 3 ) : print( str( records[ i ][ j ] ).ljust( 20 ), end = '' )
		print() 


def display_attribute( cur ) :

	command = str() 
	attributes = [ "NAME", "" ]
	headings = [ "*", "Rowid", "Name", "Roll No", " Marks" ]
	choice = int()
	ch = 'y'

	choice = int( input( "Select :\n1)*\n2)Rowid\n3)Name\n4)Roll No\n5)Marks\nEnter your choice : " ) )
	while( choice not in range( 1, 6 ) ) : choice = int( input( "INVALID INPUT...ENTER AGAIN : " ) )

	clrscr()

	if( choice == 1 ) : 
		display_full( cur )
		return

	command = "SELECT {} FROM student".format( headings[ choice - 1 ] )
	cur.execute( command )
	records = cur.fetchall()

	print( headings[ choice - 1 ].ljust( 20 ), end = '' )
	print( "\n", end = "-"*20 + "\n" )

	for r in records : print( r[ 0 ] )



def clrscr() : print( "\n"*100 )




# DRIVER CODE
def main() :

	con = connect( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\SQLite 3\DATABASES\STUDENT.db" )
	cur = con.cursor()

	ch = 'y'
	choice = int()
	command = str()
	records = list()

	menu = { 	 
				1 : "insert( con, cur )", 
				2 : "delete( con, cur )", 
				3 : "update( con, cur )", 
				4 : "display_full( cur )", 
				5 : "display_attribute( cur )"	
			}


	while( ch in 'yY' ) :

		clrscr()
		choice  = int( input( """\tMENU
			
1> Insert Records
2> Delete Records
3> Update Records
4> Display Full Table
5> Display a Column of the Table
			
Enter your choice : """ ) )

		clrscr()
		exec( menu[ choice ] )
		ch = input( "\nContinue ? ( Y / N ) : " )

	con.commit()
	con.close()

main()