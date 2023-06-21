# PROGRAM TO CALCULATE BMI USING SLIDER INPUT
# BMI VALUE IS CALCULATED IN REAL TIME 

from tkinter import Tk, Label, Button, Scale

def submit( var ) : # By default the slider passes this var argument althouth the function itself doesnt require it. Its a necessary evil!
	global window, height, weight, bmi

	w, h = weight.get(), height.get()
	bmi[ "text" ] = "B.M.I = {}".format( w / ( h*h ) )
	bmi.grid_forget()
	bmi.grid( row = 4 )

window = Tk()
window.geometry( "600x600" )

weight = Scale( window, from_ = 10, to = 200, orient = "horizontal", command = submit  )
height = Scale( window, from_ = 1, to = 5, orient = "vertical", command = submit )

w = Label( window, text = "Select Weight ( kg ) : " )
h = Label( window, text = "Select Height ( m )  : " )
bmi = Label( window, text = "Your BMI is {}".format( weight.get() / height.get()*height.get() ), bg = "YELLOW", fg = "RED", anchor = "center" )

weight.grid( row = 0, column = 1 )
height.grid( row = 1, column = 1 )

w.grid( row = 0, column = 0 )
h.grid( row = 1, column = 0 )
bmi.grid( row = 4 ) 

window.mainloop()