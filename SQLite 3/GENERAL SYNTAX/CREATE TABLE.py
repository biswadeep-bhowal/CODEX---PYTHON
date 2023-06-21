# PROGRAM TO ILLUSTRATE ALL THE DATABASE TABLE OPERATIONS IN SQLITE3
# ALL OPERATIONS ARE SUBJECTED TO student TABLE of STUDENT DATABASE

from sqlite3 import connect
from tkinter import filedialog

def create_database() : 
	name = input( "Database Name : " )
	try : 
		c = connect( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\SQLite 3\DATABASES\{}.db".format( name ) )
		print( "\nNew Database created successfully!" )
	except Error as e : 
		print( "\nError :", e )

def create_table( cur ) :
	attributes = dict()
	li = list()
	ch = 'y'
	c = 0

	print( "\nThis table will be created inside the " )
	table_name = input( "Enter Table Name : " )

	while( ch in "yY" ) : 
		
		name = input( "Enter column name : " )
		while( name in list( attributes.keys() ) ) : name = input( "Column name already exists...Enter again : " )
		
		datatype = int( input( "\nSelect Datatype :\n1)integer\n2)text\n3)real\nEnter your choice : " ) )
		while( datatype not in [ 1, 2, 3 ] ) : datatype = input( "INVALID INPUT...ENTER AGAIN : " )
		
		if( datatype == 1 ) : 	datatype = "integer"
		elif( datatype == 2 ) : datatype = "text"
		else : 					datatype = "real" 
		
		attributes[ name ] = datatype

		ch = input( "\nCONTINUE ? ( Y / N ) : " )
		c += 1 

	name = list( attributes.keys() )
	datatype = list( attributes.values() )

	for i in range( len( name ) ) : 
		li.append(  name[ i ] )
		li.append(  datatype[ i ] )

	s = "{} {},"*c 
	s = s[ 0 : len( s ) - 1 ]
	s.format( li )

	try : 
		cur.execute( "CREATE TABLE {} ( {} )".format( table_name, s ) )
		print( "Table created successfully!" )

	except Error as e : 
		print( "Error :", e )


def drop_table( cur ) : 
	print( "This table should exist inside the STUDENT DATABASE\n" )
	name = input( "Enter table name : " )
	try : 
		cur.execute( "DROP TABLE " + name )
		print( "Table dropped successfully!" )
	except Error as e :
		print( "Error :", e )


def insert_record( cur, attributes ) :
	records = list()
	ch = 'y'

	print( "\nEnter the table records to be inserted :\n" )
	while( ch in "yY") : 
		name = input( "Name : " )
		roll = int( input( "Roll No. : " ) )
		marks = float( input( "Marks : " ) )

		records.append( ( name, roll, marks ) )

		ch = input( "Continue ? ( Y / N ) : " )

	try : 
		if( len( records ) ++ 1 ) : cur.execute( "INSERT INTO student VALUES {}".format( records[ 0 ] ) )
		else :						cur.executemany( "INSERT INTO student VALUES ( ?, ?, ? )", records )
	except Error as e: 
		print( "Error :", e )
 
def delete_record( cur ) : 

	ch = 'y'
	choice = int()

	while( ch in "yY") : 

		choice = int( input( "Delete By :\n1)Name\n2)Roll No.\n3)Marks\nEnter your choice : " ) )
		while( choice not in [ 1, 2, 3 ] ) : choice = int( input( "INVALID INPUT...ENTER AGAIN : " ) ) 

		if( choice == 1 ) : 	attribute = "name"
		elif( choice == 2 ) : 	attribute = "roll"
		else : 					attribute = "marks"

		value = input( "\nEnter {} : ".format( attribute ) )

		cur.execute( "DELETE FROM student WHERE {} = {}".format( attribute, value ) )

		ch = input( "Continue ? ( Y / N ) : " )

def display_table( cur ) : 

	try : cur.execute( "SELECT * FROM student" )
	except Exception as e : print( "Error :", e )

	records = cur.fetchall()

	print( "Name".ljust( 15 ) + "Roll No.".ljust( 15 ) + "Marks".ljust( 15 ) )
	for i in range( len( records ) ) : 
		for j in range( 3 ) : print( str( records[ i ][ j ] ).ljust( 20 ), end = '' )
		print()


def clrscr() : print( "\n"*50 )


# DRIVER CODE

con = connect( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\SQLite 3\DATABASES\STUDENT.db" )
cur = con.cursor()

ch = 'y'
choice = int() 

while( ch in "yY" ) : 
	clrscr()
	
	print( "\tMENU\n1) CREATE DATABASE\n2) CREATE TABLE\n3) DROP TABLE\n4) INSERT RECORDS\n5) DELETE RECORDS\n6) DISPLAY TABLE\nEnter your choice : " )
	choice = int( input() )

	if( choice == 1 ) : create_database()
	elif( choice == 2 ) : create_table( cur ) 
	elif( choice == 3 ) : drop_table( cur )
	elif( choice == 4 ) : insert_record( cur )
	elif( choice == 5 ) : delete_record( cur )
	elif( choice == 6 ) : display_table( cur )

	else : print( "INVALID INPUT..." )

	con.commit()
	ch = input( "\n\nContinue ? ( Y / N ) : " )

# MAINTAINING THE STUDENT DATABASE
exec( open( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\SQLite 3\GENERAL SYNTAX\MAINTAIN STUDENT.py" ).read() )
con.close()

