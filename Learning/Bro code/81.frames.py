from tkinter import *

window = Tk()
frame = Frame(window,bg='red',bd=5,relief=SUNKEN)
frame.pack(side='top')

Button(frame,text="W",font=("Arial",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Arial",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Arial",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Arial",25),width=3).pack(side=LEFT)

window.mainloop()