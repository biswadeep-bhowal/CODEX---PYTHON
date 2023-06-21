# PROGRAM TO ILLUSTRATE SINGLE LEVEL INHERITENCE

class A : 
	def f1( self ) : print( "f1 Working." )
	def f2( self ) : print( "f2 Working." )

class B( A ) : 
	def f3( self ) : print( "f3 Working." )
	def f4( self ) : print( "f4 Working." )

b = B()

b.f1()
b.f2()
b.f3()
b.f4()