from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)
    entry.config(state=NORMAL)

def backspace():
    entry.delete(len(entry.get())-1,END) 

window = Tk()
entry = Entry(window,
              font=("Arial",50),
              fg='#00FF00',
              bg="black")
entry.pack(side="left")

Submit_button = Button(window,
                text="Submit",
                command=submit)
Submit_button.pack(side="right")

Delete_button = Button(window,
                text="Delete",
                command=delete)
Delete_button.pack(side="right")

Backspace_button = Button(window,
                text="Backspace",
                command=backspace)
Backspace_button.pack(side="right")
   

window.mainloop()