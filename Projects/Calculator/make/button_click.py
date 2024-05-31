import tkinter as tk
from calculator_main_page import Enter

def Shahid():
    root1 = tk.Tk()
    label1 = tk.Label(root1, text = "Welcome Shahid. Thanks for using this simple calculator")
    label1.pack()
    enter = tk.Button(root1, text = "Enter", command = Enter, fg = "white", bg = "black")
    enter.pack()
    root1.mainloop()

def Mashahid():
    root1 = tk.Tk()
    label1 = tk.Label(root1, text = "Go and study idiot!")
    label1.pack()
    enter = tk.Button(root1, text = "Enter", command = Enter, fg = "white", bg = "black")
    enter.pack()
    root1.mainloop()

def Other():
    root1 = tk.Tk()
    label1 = tk.Label(root1, text = "Thanks for using this simple calculator")
    label1.pack()
    enter = tk.Button(root1, text = "Enter", command = Enter, fg = "white", bg = "black")
    enter.pack()
    root1.mainloop()         
   