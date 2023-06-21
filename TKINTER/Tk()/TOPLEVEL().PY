# PROGRAM TO CREATE CHILD WINDOWS USING TOPLEVEL()

from tkinter import Tk, Toplevel, Label, Button

# Th() should be used for parent windows while Toplevel() should be used for parent windows.
# A Toplevel() window can be the parent of another Toplevel() window. But Tk() is the parent to all Toplevel() windows

def generate_child_window() : 
	
	child_window = Toplevel()
	Label( child_window, text = "This is a child window" ).pack()
	child_window.mainloop()

parent_window = Tk()

Label( parent_window, text = "This is the parent window" ).pack()
Button( parent_window, text = "GENERATE CHILD WINDOW", command = generate_child_window ).pack()
# This button can generate infinite child windows made by Toplevel()

parent_window.mainloop()
