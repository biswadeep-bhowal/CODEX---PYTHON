# FIRST PROGRAM FOR SQLITE3. CREATING A TABLE IN THE DATABASE

from sqlite3 import connect

con = connect( r"DATABASES\student.db" )	
# THIS VARIABLE IS CALLED A CONNECTION. CONNECTIONS TO DATABASES HAVE TO BE ESTABLISHED BEFORE WORKING ON THEM. 
# IF STUDENT.DB DOES NOT EXIST, IT WILL BE CREATED AUTOMATICALLY.

cur = con.cursor()
# THIS IS A CURSOR VARIABLE. IT IS USED TO OPERATE ON DATABASES.

# SYNTAX TO CREATE TABLE.
cur.execute( """CREATE TABLE student
	(	
		name text 
		email text
		phone integer
	)
""")

# SQLITE3 DATATYPES : 
"""
integer : Regular integer values
text : Regular strings
null : value specifies whether the data exists or not
blob : 
real : Decimal Numbers
"""

con.commit()	# COMMITING THE TABLE TO THE DATABASE
con.close()		# CLOSES THE CONNECTION. MANDATORY TO CLOSE ALL CONNECTIONS AT THE END OF THE PROGRAM