import tkinter as tk

root = tk.Tk()
data = tk.Entry(root, width=50)
data.pack()
data.insert(0, "Enter your name")

def button_clicked():
    hello = "hello " + data.get()
    label = tk.Label(root, text = hello)
    label.pack()


button = tk.Button(root, text = "Button", command = button_clicked, fg = "white", bg = "black")
button.pack()

root.mainloop()