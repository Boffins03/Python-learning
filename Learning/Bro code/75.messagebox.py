from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="This is info",message="This is a message")
    # messagebox.showwarning(title="Warning",message="This is a warning")
    # messagebox.showerror(title="Error",message="This is an error")
    # if messagebox.askokcancel(title="ask ok cancel",message="Do you want to?"):
    #     print("You want.")
    # else:
    #     print("You don't want.")    
    if messagebox.askyesno(title="Yes No",message="Do you want to eat?"):
        print("You want.")
    else:
        print("You don't want.")    

window = Tk()

button = Button(window,text="Click me",command=click)
button.pack()

window.mainloop()