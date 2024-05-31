from tkinter import *

def open():
    print("File has been opened")
def save():
    print("File has been saved")
def add():
    print("File has been added")
def replace():
    print("File has been replaced")
def delete():
    print("File has been deleted")
   
window = Tk()
menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label="Open",command=open)
filemenu.add_command(label="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)

editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label="add",command=add)
editmenu.add_command(label="replace",command=replace)
editmenu.add_separator()
editmenu.add_command(label="delete",command=delete)

window.mainloop()