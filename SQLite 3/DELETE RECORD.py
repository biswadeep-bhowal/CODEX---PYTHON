# PROGRAM TO DELETE A RECORD BY EXISTING PARAMETERS

from sqlite3 import connect

def display( cur ) : 

	cur.execute( "SELECT rowid, * FROM customer" )
	r = cur.fetchall()

	print( "Current State of Database :\n\n" )
	print( "Row ID".ljust( 10 ) + "Name".ljust( 10 ) + "ID".ljust( 10 ) )
	for i in range( len( r ) ) : print( str( r[ i ][ 0 ] ).ljust( 10 ) + r[ i ][ 1 ].ljust( 10 ) + str( r[ i ][ 2 ] ).ljust( 10 ) )

con = connect( r"DATABASES\CUSTOMER.db" )
cur = con.cursor()

display( cur )

choice = int( input( "Delete BY :\n1)Row ID\n2)Name\n3)ID\nEnter your choice : " ) )
if( choice == 1 ) : 
	try : cur.execute( "DELETE FROM customer WHERE rowid = {}".format( int( input( "Enter Row ID : " ) ) ) )
	except Error as e : print( e )

elif( choice == 2 ) : 
	try : cur.execute( "DELETE FROM customer WHERE Name = {}".format( input( "Enter Name : " ) ) )
	except Error as e : print( e )

elif( choice == 3 ) : 
	ID = int( input( "Enter ID : " ) )
	try : cur.execute( "DELETE FROM customer WHERE ID = {}".format( ID ) )
	except : print( "No such record exists..." )	

con.commit()
display( cur )
con.close()