# PROGRAM TO DISPLAY THE STUDENT TABLE
# TO BE USED BY OTHER PROGRAMS TO DISPLAY THE TABLE

from sqlite3 import connect

CON = connect( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\SQLite 3\DATABASES\STUDENT.db" )
CUR = CON.cursor()

try : CUR.execute( "SELECT * FROM student" )
except Exception as e : print( "Error :", e )

records = CUR.fetchall()

print( "Name".ljust( 15 ) + "Roll No.".ljust( 15 ) + "Marks".ljust( 15 ) )
for i in range( len( records ) ) : 
	for j in range( 3 ) : print( str( records[ i ][ j ] ).ljust( 20 ), end = '' )
	print()

CON.commit()
CON.close()