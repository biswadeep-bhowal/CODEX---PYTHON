# PROGRAM TO ILLUSTRATE MULTIPLE INHERITENCE

class A : 
	def f1( self ) : print( "f1 Working." )
	def f2( self ) : print( "f2 Working." )

class B : 
	def f3( self ) : print( "f3 Working." )
	def f4( self ) : print( "f4 Working." )

class C( A, B ) : 
	def f5( self ) : print( "f5 Working." )
	def f6( self ) : print( "f6 Working." )

c = C()

c.f1()
c.f2()
c.f3()
c.f4()
c.f5()
c.f6()