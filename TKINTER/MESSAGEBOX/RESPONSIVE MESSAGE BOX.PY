from tkinter import Tk, Button, Label, messagebox

window = Tk()

aoc = Button( window, text = "ASKOKCANCEL", command = lambda : Label( window, text = "Your Response : {}".format( messagebox.askokcancel() ) ).grid( row = 6 ) )
aq =  Button( window, text = "ASKQUESTION", command = lambda : Label( window, text = "Your Response : {}".format( messagebox.askquestion() ) ).grid( row = 6 ) ) 
ayn = Button( window, text = "ASKYESNO",    command = lambda : Label( window, text = "Your Response : {}".format( messagebox.askyesno() )    ).grid( row = 6 ) )
se =  Button( window, text = "SHOWERROR",   command = lambda : Label( window, text = "Your Response : {}".format( messagebox.showerror() )   ).grid( row = 6 ) )
si =  Button( window, text = "SHOWINFO",    command = lambda : Label( window, text = "Your Response : {}".format( messagebox.showinfo() )    ).grid( row = 6 ) )
sw =  Button( window, text = "SHOWWARNING", command = lambda : Label( window, text = "Your Response : {}".format( messagebox.showwarning() ) ).grid( row = 6 ) )

aoc.grid( row = 0 )
aq.grid( row = 1 )
ayn.grid( row = 2 )
se.grid( row = 3 )
si.grid( row = 4 )
sw.grid( row = 5 )

window.mainloop()