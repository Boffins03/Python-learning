from tkinter import *

def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))

    print("You have order:")
    print(food)   
    

def add():
    listbox.insert(listbox.size(),entry.get())    
    listbox.config(height=listbox.size())
    entry.delete(0,END)

window = Tk()

listbox = Listbox(window,
                  bg="grey",
                  font=("Arial",35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Burger")
listbox.insert(3,"Momo")
listbox.insert(4,"Dosa")

listbox.config(height=listbox.size())

entry = Entry(window,
              font=("Arial",30),
              width=12)
entry.pack()

button = Button(window,
                text="Submit",
                command=submit)
button.pack()

add = Button(window,
                text="Add",
                command=add)
add.pack()

window.mainloop()