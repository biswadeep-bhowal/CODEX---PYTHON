# PROGRAM TO DELETE A TABLE FROM A GIVEN DATABASE 

from sqlite3 import connect

database_name = str( input( "\nEnter database path : " ) )
table_name = str( input( "\nEnter table name : " ) )

con = connect( database_name )
cur = con.cursor()

try : 
	cur.execute( "DROP TABLE " + table_name )
	print( "\nTable Dropped Successfully !" )
except : 
	print( "Cannot Drop Table" )

con.commit()
con.close()


