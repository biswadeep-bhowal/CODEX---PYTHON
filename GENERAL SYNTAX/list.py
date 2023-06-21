# PROGRAM TO FAMILIARISE SYNTAX OF LISTS 


# Declaration ( Sort of.. )

li = []
print( li )   
# []


# Initialisation

li = [ 1, 2, 3 ]
print( li )
# [ 1, 2, 3 ]


# initialise from a range

li = [ i for i in range( 0, 10 ) ]
print( li )   
# [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]


# Convert delimited string to list of integers

s = "1 2 3 4 5"
li = list( map( int, s.strip().split() ) )
print( li )   
#  [ 1, 2, 3, 4, 5 ]


# Append an element

ele = 6
li.append( ele )
print( li )   #  [ 1, 2, 3, 4, 5, 6 ]


# Pop element

li.pop()
print( li )   #  [ 1, 2, 3, 4, 5 ]


# Delete element from given index

idx = 0
li.pop( idx )
print( li )   #  [ 2, 3, 4, 5 ]


# Delete first occurrence of given element

ele = li[ 0 ]
li.remove( ele )
print( li )   
# [ 3, 4, 5 ]


# Insert given element at given index

idx = 0
ele = 2
li.insert( idx, ele )
print( li )   
# [ 2, 3, 4, 5 ]


# Display part of the list ( Sublist )

li = [ i for i in range( 0, 10 ) ]
lower = 1
upper = 5
print( li[ lower : upper ] )  
# [ 1, 2, 3, 4 ]


# Reverse a list

li.reverse()
print( li )   
# [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ]


# Sort a list

li.sort()   # Ascending Order
print( li )
# [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

li.sort( reverse = True )   # Descending Order
print( li )
# [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ]


# Generate a list of 10 zeroes

li = [ 0 ] * 10
print( li )
# [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]


# Join / Concatenate 2 lists

L1 = [1, 2, 3, 4, 5 ]
L2 = [ 6, 7, 8, 9, 10 ]

L3 = L1 + L2    # Or L1.append( L2 )
print( L3 )


# Generate a 2d list of zeroes with m rows and n columns

m = 5
n = 10
li = []

for _ in range( m ) : li.append( [ 0 ] * n )
print( li )
# [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ]


# Sort a 2d list vertically according to given column index

li = [
    [ 'Biswadeep', 22 ],
    [ 'Bradley', 26 ],
    [ 'Babar', 19 ]
]

li.sort( key = lambda x : x[ 1 ] )  # Sorts vertically comparing index 1 of every row.
print( li )