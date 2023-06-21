# PROGRAM TO ILLUSTRATE USE OF super() METHOD

class A : 
	def __init__( self ) :
		print( "A __init__" ) 

class B( A ) : 
	def __init__( self ) : 
		print( "B __init__" )
		super().__init__()		# CALLS THE METHOD FROM PARENT CLASS

print( "Case  : 1" )
b = B()

# IN CASE OF MULTIPLE INHERITENCE, THE LEFT ARGUMENT WILL BE SEARCHED FIRST, THEN THE RIGHT

class X : 
	def __init__( self ) :
		print( "X __init__" ) 

class Y : 
	def __init__( self ) : 
		print( "Y __init__" )

class Z( X, Y ) : 
	def __init__( self ) : 
		print( "Z __init__" )
		super().__init__()

print( "Case : 2" )
z = Z()

class P( Y, X ) : 
	def __init__( self ) : 
		print( "P __init__" )
		super().__init__()

print( "Case : 3" )
p = P()