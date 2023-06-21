# DICTIONARY SYMTAX

d = {}  # DECLARATION
n = int( input( "\nNumber of Records : " ) )

for i in range( n ) : 
    country, capital = input( "Country : " ), input( "Capital : " )
    d[ country ] = capital
    
print( "Given Dictionary : ", d )

print( 'Key - Value Pairs :' )

for country, capital in d.items() : print( 'Country : {}\t\tCapital : {}'.format( country, capital ) )    # Iterating over a dictionary