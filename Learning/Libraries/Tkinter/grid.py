import tkinter as tk

root =tk.Tk()

mylabel1 = tk.Label(root, text="Hello world")
mylabel2 = tk.Label(root, text="Welcome")

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)

root.mainloop()