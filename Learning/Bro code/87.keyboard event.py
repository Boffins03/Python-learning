from tkinter import *

def print(event):
    label.config(text=event.keysym)

window = Tk()
window.bind("<Key>",print)

label = Label(window,font=("Arial",20),width=20,height=5)
label.pack()

window.mainloop()