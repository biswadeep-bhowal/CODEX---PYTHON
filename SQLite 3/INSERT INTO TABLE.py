# PROGRAM TO INSERT RECORDS INTO A TABLE

from sqlite3 import connect

s_con = connect( r"DATABASES\student.db" )
s_cur = s_con.cursor()

# HARDCODED INSERTION
s_cur.execute( """INSERT INTO student VALUES
	(
		"BISWADEEP BHOWAL", 
		"biswadeep.bhowal@gmail.com",
		9874683979
	) 
""")

# VARIABLE INSERTION
name = str( input( "\nEnter Name : " ) )
email = str( input( "\nEnter email : " ) )
phone = int( input( "\nEnter phone no. : " ) )

s_cur.execute( """INSERT INTO student VALUES
	(
		name, 
		email,
		phone
	) 
""")

print( "\nRecords successfully inserted into student table !" )

s_con.commit()
s_con.close()