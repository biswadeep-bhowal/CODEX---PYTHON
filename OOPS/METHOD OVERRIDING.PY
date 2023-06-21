# PROGRAM TO ILLUSTRATE METHOD OVERRIDING

class A : 
	def show( self ) : print( "Inside A" )

class B( A ) : pass	# SINCE B DOES NOT HAVE SHOW() METHOD, A's SHOW METHOD WILL BE USED

class C( A ) : 
	def show( self ) : print( "Inside C" )	# SINCE C HAS ITS OWN SHOW() METHOD, IT WILL BE USED INSTEAD OF A's

b = B()
c = C()

print( "Case - 1 :", end = '' )
b.show()
print( "Case - 2 :", end = '' )
c.show()