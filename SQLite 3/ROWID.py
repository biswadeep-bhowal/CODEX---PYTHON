# PROGRAM TO FETCH ROWID ALONG WITH ALL THE RECORDS IN THE CUSTOMER DATABASE 

from sqlite3 import connect

con = connect( "DATABASES\CUSTOMER.db" )
cur = con.cursor()

cur.execute( "SELECT rowid, * FROM customer" )
records = cur.fetchall()

for i in range( len( records ) ) : print( records[ i ][ 0 ], records[ i ][ 1 ], records[ i ][ 2 ] )

con.commit()
con.close()