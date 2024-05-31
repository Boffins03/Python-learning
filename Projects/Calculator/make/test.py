import tkinter as tk
from button_click import *

# Main window
root = tk.Tk()
data = tk.Entry(root, width=50)
data.pack()

# After button click
def button_clicked():
    if (data.get() == "Shahid"):
        Shahid()
    elif (data.get() == "Mashahid"):
        Mashahid()   
    else:
        Other()

label = tk.Label(root, text="Welcome")
button = tk.Button(root, text = "Submit", command = button_clicked, fg = "white", bg = "black")

label.pack()
button.pack()

root.mainloop()