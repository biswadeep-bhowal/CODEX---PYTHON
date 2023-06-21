from sqlite3 import connect

con = connect( r"DATABASES\CUSTOMER.db" )
cur = con.cursor()

records = list()
name = str()
ID = int()
ch = 'y'

# INSERTING MULTIPLE RECORDS INTO CUSTOMER TABLE.

while( ch == 'y' or ch == 'Y' ) : 
	
	name = input( "Name : " )
	ID = int( input( "ID : " ) ) 

	records.append( ( name, ID ) )

	ch = input( "\nCOntinue ? ( Y / N ) : " )

cur.executemany( "INSERT INTO customer VALUES ( ?, ? )", records )	# EXECUTEMANY IS USED WHEN A LIST OF TUPLES IS INSERTED AT ONCE.

cur.execute( "SELECT * FROM customer" )
records = cur.fetchall() 	# RETURNS THE ENTIRE TABLE RECORDS IN THE FORM OF A LIST OF TUPLES

print( "THese are the inserted records :\n", records )

print( "This data can be beautified : \n" )
print( "NAME".ljust( 15 ) + "ID".ljust( 15 ) )
for i in range( len( records ) ) : print( str( records[ i ][ 0 ] ).ljust( 15 ) + str( records[ i ][ 1 ] ).ljust( 15 ) )

con.commit()
con.close()