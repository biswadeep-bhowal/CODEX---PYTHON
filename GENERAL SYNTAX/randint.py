# PROGRAM TO GENERATE RANDOM INTEGERS IN A GIVEN RANGE

from random import randint 

n = int( input( "\nEnter number of elements to generate : " ) )
upper = int( input( "\nUpper Limit : " ) )
lower = int( input( "\nLower Limit : " ) )

for i in range( n ) : print( randint( lower, upper ) )