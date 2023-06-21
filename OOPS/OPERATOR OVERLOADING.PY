# PROGRAM TO ILLUSTRATE OPERATOR OVERLOADING 

class student : 

	def __init__( self, m1, m2 ) : 
		self.m1 = m1
		self.m2 = m2

	def __add__( self, other ) :
		m1 = self.m1 + other.m1
		m2 = self.m2 + other.m2 
		return student( m1, m2 )

s1 = student( 50, 60 )
s2 = student( 30, 80 )

s3 = s1 + s2	# FOR BASIC DATA TYPES THE __add__() method is defined as well since all data types in python are classes.

print( "Student  - 1 : m1 = {}, m2 = {}".format( s1.m1, s1.m2 ) )
print( "Student  - 2 : m1 = {}, m2 = {}".format( s2.m1, s2.m2 ) )
print( "Student  - 3 : m1 = {}, m2 = {}".format( s3.m1, s3.m2 ) )