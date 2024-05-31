from tkinter import *
from tkinter import filedialog

def file():
    filepath = filedialog.askopenfilename(initialdir="Download",
                                          title="Open a file",
                                          filetypes=('text file','*.txt'))
    with open(filepath,'r') as file:
        print(file.read())

window = Tk()
button = Button(window,text="Click",
                command=file)
button.pack()

window.mainloop()