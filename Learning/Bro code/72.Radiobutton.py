from tkinter import *

food = ["Pizza","Burger","Momo"]

window = Tk()
x = IntVar()

for i in range(len(food)):
    radio_button = Radiobutton(window,
                                   text=food[i],variable=x,value=i)
    radio_button.pack(anchor=W)


window.mainloop()