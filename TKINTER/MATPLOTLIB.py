from tkinter import Button, Tk
from numpy import random
from matplotlib.pyplot import hist, show

def graph() : 
	house_prices = random.normal( 100000, 25000, 5000 )
	hist( house_prices, 50 )
	show()

window = Tk()

click = Button( window, text = "Show Graph", command = graph )
click.grid( row = 0 )

window.mainloop()