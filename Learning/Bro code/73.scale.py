from tkinter import *

def submit():
    print(f"The temprature is {str(scale.get())} degree C")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              tickinterval=10,
              resolution=5,
              length=500,
              troughcolor="#69EAFF")
scale.pack()

button = Button(window,
                text="Submit",
                command=submit)
button.pack()

window.mainloop()