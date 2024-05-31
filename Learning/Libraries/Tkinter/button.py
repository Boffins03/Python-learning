import tkinter as tk

root = tk.Tk()

def button_clicked():
    label = tk.Label(root, text = "Button Clicked")
    label.pack()


button = tk.Button(root, text = "Button", command = button_clicked, fg = "white", bg = "black")
button.pack()

root.mainloop()