from datetime import datetime

present = datetime.now()
christmas = datetime( present.year, 12, 25 )

if( present.day > christmas.day ) :         print( "Sorry!!Christmas was {} days ago...".format( present.day - christmas.day ) )
elif( present.day == christmas.day ) :      print( "Today is Christmas !!" )
else : 
    time_left = int( ( christmas - present ).total_seconds() )
    months, time_left = divmod( time_left, 2592000 )
    days, time_left =   divmod( time_left, 86400 )
    hours, time_left =  divmod( time_left, 3600 )
    minutes, time_left =divmod( time_left, 60 )
    seconds = int( time_left )
    
    print( "{} months {} days {} hours {} minutes {} seconds left until Christmas !!".format( months, days, hours, minutes, seconds ) )