import tkinter as tk

root = tk.Tk()
data = tk.Entry(root, width=35)
data.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_clicked():
    label = tk.Label(root, text = "Button Clicked")
    label.pack()


button7 = tk.Button(root, text = "7", command = button_clicked, padx = 40, pady = 20).grid(row = 1, column = 0)
button8 = tk.Button(root, text = "8", command = button_clicked, padx = 40, pady = 20).grid(row = 1, column = 1)
button9 = tk.Button(root, text = "9", command = button_clicked, padx = 40, pady = 20).grid(row = 1, column = 2)

button4 = tk.Button(root, text = "4", command = button_clicked, padx = 40, pady = 20).grid(row = 2, column = 0)
button5 = tk.Button(root, text = "5", command = button_clicked, padx = 40, pady = 20).grid(row = 2, column = 1)
button6 = tk.Button(root, text = "6", command = button_clicked, padx = 40, pady = 20).grid(row = 2, column = 2)

button3 = tk.Button(root, text = "3", command = button_clicked, padx = 40, pady = 20).grid(row = 3, column = 0)
button2 = tk.Button(root, text = "2", command = button_clicked, padx = 40, pady = 20).grid(row = 3, column = 1)
button1 = tk.Button(root, text = "1", command = button_clicked, padx = 40, pady = 20).grid(row = 3, column = 2)

root.mainloop()