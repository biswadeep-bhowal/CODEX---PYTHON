# PROGRAM TO RECREATE THE STUDENT TABLE FROM THE STUDENT DATABASE

from sqlite3 import connect

con = connect( r"C:\Users\BISWADEEP BHOWAL\Desktop\CODEX - PYTHON\SQLite 3\DATABASES\STUDENT.db" )
cur = con.cursor()

try : 
	cur.execute( "DROP TABLE student" )
	print( "Existing student Table dropped successfully." )
except Exception as e : print( "\nError :", e )

print( "\n\nRecreating table student...\n" )

cur.execute( """CREATE TABLE STUDENT
	(
		name text,
		roll integer,
		marks real
	)
""")

student_records = [ ( "Biswadeep Bhowal", 52, 89.4 ), ( "Rohit Khemka", 38, 90.08 ), ( "Shashank Kumar", 57, 85.69 ), 
					( "Srinjoy Paul", 62, 96.87 ), ( "Sayantan Mishra", 51, 89 ) ]

cur.executemany( "INSERT INTO student VALUES ( ?, ?, ? )", student_records )
con.commit()

print( "\nTable Created Successfully...Retrieving stored Data : \n\n" )

cur.execute( "SELECT rowid, * FROM student" )
student_records = cur.fetchall()

print( "Row ID".ljust( 10 ) + "NAME".ljust( 30 ) + "Roll".ljust( 10 ) + "Marks".ljust( 10 )  )
for i in range( 5 ) : 
	print( str( student_records[ i ][ 0 ] ).ljust( 10 ), end = '' )
	print( str( student_records[ i ][ 1 ] ).ljust( 30 ), end = '' )
	print( str( student_records[ i ][ 2 ] ).ljust( 10 ), end = '' )
	print( str( student_records[ i ][ 3 ] ).ljust( 10 ) )
	
	

print( "\n\nClosing database connection..." )
con.close()
