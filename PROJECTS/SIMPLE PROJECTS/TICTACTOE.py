class grid : 
    
    def __init__( self ) : self.data = list( range( 1, 10 ) )
    
    def display( self ) : 
        
        p = 0
        for i in range( 11 ) : 
            if( i == 3 or i == 7 ) :    
                print( '-'*11 )              
            elif( i in [ 1, 5, 9 ] ) :  
                print( " {} | {} | {}".format( self.data[ p ], self.data[ p+1 ], self.data[ p+2 ] ) )
                p += 3
            else :                      
                print( "   |   |" )
        

    def update( self, p ) : self.data[ p.choice-1 ] = p.sign
    
    def check( self, p ) : 
        win = [ p.sign ]*3
        d = self.data
        
        if( d[ 0 : 3 ] == win or d[ 3 : 6 ] == win or d[ 6 : 9 ] == win ) :                                                     return 1
        elif( [ d[ 0 ], d[ 3 ], d[ 6 ] ] == win or [ d[ 1 ], d[ 4 ], d[ 7 ] ] == win or [ d[ 2 ], d[ 5 ], d[ 8 ] ] == win ) :   return 1
        elif( [ d[ 0 ], d[ 4 ], d[ 8 ] ] == win or [ d[ 2 ], d[ 4 ], d[ 6 ] ] == win ) :                                        return 1
        else :                                                                                                                  return 0

class computer : 
    
    def __init__( self, other ) : 
        self.name = "COMPUTER"
        self.sign = 'X' if other.sign == 'O' else 'O'
        self.choice = 0
        self.score = 0
        
    def choose( self, other, box ) : 
        
        self.put( box, 0, 1, 2 )
        if( self.choice == -1 ) : self.put( box, 3, 4, 5 )  
        else : return
        if( self.choice == -1 ) : self.put( box, 6, 7, 8 ) 
        else : return
        if( self.choice == -1 ) : self.put( box, 0, 3, 6 ) 
        else : return
        if( self.choice == -1 ) : self.put( box, 1, 4, 7 ) 
        else : return
        if( self.choice == -1 ) : self.put( box, 2, 5, 8 ) 
        else : return
        if( self.choice == -1 ) : self.put( box, 0, 4, 8 ) 
        else : return
        if( self.choice == -1 ) : self.put( box, 2, 4, 6 ) 
        else : return
        
        if( self.choice == -1 ) : self.block( other, box, 0, 1, 2 ) 
        else : return
        if( self.choice == -1 ) : self.block( other, box, 3, 4, 5 ) 
        else : return
        if( self.choice == -1 ) : self.block( other, box, 6, 7, 8 ) 
        else : return
        if( self.choice == -1 ) : self.block( other, box, 0, 3, 6 ) 
        else : return
        if( self.choice == -1 ) : self.block( other, box, 1, 4, 7 ) 
        else : return
        if( self.choice == -1 ) : self.block( other, box, 2, 5, 8 ) 
        else : return
        if( self.choice == -1 ) : self.block( other, box, 0, 4, 8 ) 
        else : return
        if( self.choice == -1 ) : self.block( other, box, 2, 4, 6 ) 
        else : return
        
        if( self.choice == -1 ) : self.available( box )
        
        
    def put( self, box, x1, x2, x3 ) : 
        s = [ self.sign ]*2
        d = box.data
        
        if(   [ d[ x1 ], d[ x2 ] ] == s and type( d[ x3 ] ) is int ) :  self.choice = d[ x3 ]
        elif( [ d[ x1 ], d[ x3 ] ] == s and type( d[ x2 ] ) is int ) :  self.choice = d[ x2 ]
        elif( [ d[ x2 ], d[ x3 ] ] == s and type( d[ x1 ] ) is int ) :  self.choice = d[ x1 ]
        else :                                                          self.choice = -1
        
    def block( self, other, box, x1, x2, x3 ) :
        s = [ other.sign ]*2
        d = box.data
        
        if(   [ d[ x1 ], d[ x2 ] ] == s and type( d[ x3 ] ) is int ) :  self.choice = d[ x3 ]
        elif( [ d[ x1 ], d[ x3 ] ] == s and type( d[ x2 ] ) is int ) :  self.choice = d[ x2 ]
        elif( [ d[ x2 ], d[ x3 ] ] == s and type( d[ x1 ] ) is int ) :  self.choice = d[ x1 ]
        else :                                                          self.choice = -1
        
    def available( self, box ) :
        d = box.data
        for i in range( 9 ) :
            if( type( d[ i ] ) is int ) : 
                self.choice = d[ i ]
                break
class player : 
    
    def __init__( self ) : 
        self.name = input( "\nName : " )
        self.sign = self.symbol()
        self.choice = 0
        self.score = 0
        
    def symbol( self ) : 
        s = input( "\nSymbol ( X / O ) : " ).upper()
        while( s not in "XO" ) : s = input( "INVALID INPUT...ENTER AGAIN : " ).upper()
        return s
        
    def choose( self, box ) : 
        self.choice = int( input( "\n\nEnter choice : " ) )
        while( self.choice not in box.data ) : self.choice = int( input( "INVALID INPUT...ENTER AGAIN : " ) )
        





def clrscr() : print( '\n'*50 )

def scoreboard( p1, p2 ) :
    clrscr()
    
    print( """ SCOREBOARD
   
    
    {}\t\t\t{}
_______________________________________________________
          
    {}{}\t\t\t{}
""".format( p1.name, p2.name, p1.score, ' '*len( p1.name ), p2.score ) )


def main() : 
    
    p1 = player()
    p2 = computer( p1 )
    ch = 'Y'
    
    while( ch == 'Y' ) :
        g = grid()
        for turn in range( 1, 10 ) : 
            g.display()
            
            if( turn%2 == 1 ) : 
                print( "\n{}'s Turn !".format( p1.name) )
                p1.choose( g )
                g.update( p1 )
                if( g.check( p1 ) == 1 ) : 
                    print( p1.name, "WON !!!!!!" )
                    p1.score += 1
                    break
            else : 
                print( "\n{}'s Turns !".format( p2.name) )
                p2.choose( p1, g )
                g.update( p2 )
                if( g.check( p2 ) == 1 ) : 
                    print( p2.name, "WON !!!!!!" )
                    p2.score += 1
                    break
        
        if( g.check( p1 ) == g.check( p2 ) ) : print( "\nDraw...." )
        ch = input( "\n\nCONTINUE ? ( Y / N ) : " ).upper()
        
    scoreboard( p1, p2 )
    
            
if( __name__ == "__main__" ) : main()