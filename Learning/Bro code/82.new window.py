from tkinter import *

def create():
    # new = Toplevel() # dependent on bottom window
    new = Tk() # independent of botton window
    old.destroy()

old = Tk()

Button(old,text="New window",font=("Arial",30),command=create).pack()
old.mainloop()
