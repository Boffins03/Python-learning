from tkinter import *

def print(event):
    print("Mouse coordinates:"+str(event.x)+","+str(event.y))

window = Tk()
window.bind("<Button-1>",print) # left
window.bind("<Button-2>",print) # scroll
window.bind("<Button-3>",print) # right
window.bind("<Enter>",print)
window.mainloop()