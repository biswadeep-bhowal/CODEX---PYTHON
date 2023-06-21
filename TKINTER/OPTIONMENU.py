# PROGRAM TO ILLUSTRATE OPTION MENUS IN TKINTER

from tkinter import Tk, Label, OptionMenu, Button, StringVar

window = Tk()

def Submit() : 
	global result, day
	result[ "text" ] = "Your favourite Day of the week is " + day.get()
	result.grid( row = 2 )


my_label = Label( window, text = "Enter your favourite day of the week : " )
result = Label( window, text = str() )

day = StringVar()
day.set( "\t\t" )

options_list = [ "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY" ]
drop_down_list = OptionMenu( window, day, *options_list ) # MIND THE ASTERISK!

submit = Button( window, text = "SUBMIT", command = Submit )

my_label.grid( row = 0, column = 0 )
drop_down_list.grid( row = 0, column = 1 )
submit.grid( row = 1 )

window.mainloop()