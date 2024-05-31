import tkinter as tk

def add_to_display(value):
    current_display = display_var.get()
    if len(current_display) < 13:
        display_var.set(current_display + value)

def clear_display():
    display_var.set("")

def calculate():
    expression = display_var.get()
    try:
        result = eval(expression)
        if isinstance(result, float):
            result = "{:.6f}".format(result)
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create display
display_var = tk.StringVar()
display_label = tk.Label(root, textvariable=display_var, font=('Arial', 20), anchor='e', bg='white', bd=5)
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Create number buttons
numbers = "7894561230."
row = 1
col = 0
for num in numbers:
    tk.Button(root, text=num, width=5, height=2, command=lambda n=num: add_to_display(n)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 2:
        col = 0
        row += 1

# Create operation buttons
operations = "+-*/"
row = 1
col = 3
for op in operations:
    tk.Button(root, text=op, width=5, height=2, command=lambda o=op: add_to_display(o)).grid(row=row, column=col, padx=5, pady=5)
    row += 1

# Create equal button
tk.Button(root, text="=", width=5, height=2, command=calculate).grid(row=4, column=3, padx=5, pady=5)

# Create clear button
tk.Button(root, text="Clear", width=5, height=2, command=clear_display).grid(row=4, column=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()