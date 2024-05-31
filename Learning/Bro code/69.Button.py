from tkinter import *

window = Tk()

def click():
    print("You click the button")


button = Button(window,
                text="click me",
                command=click,
                font=("comic Sans",30),
                fg="#00FF00",
                bg="black",
                activebackground="black",
                activeforeground='#00FF00',
                state=DISABLED)

button.pack()

window.mainloop()