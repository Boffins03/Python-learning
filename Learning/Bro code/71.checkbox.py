from tkinter import *

def display():
    if(x.get()):
        print("You Agree")
    else:
        print("You don't Agree")    

window = Tk()

x = BooleanVar()
check_button = Checkbutton(window,
                           text="I agree to this",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display)
check_button.pack()


window.mainloop()