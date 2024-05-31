import tkinter as tk

A = ""
B = ""
operator = ""

def add_to_display(value):
    global A, B, operator
    if operator:
        B += value
        display_var.set(B)
    else:
        A += value
        display_var.set(A)

def clear_display():
    global A, B, operator
    A = ""
    B = ""
    operator = ""
    display_var.set("")

def calculate():
    global A, B, operator
    try:
        if A and B and operator:
            result = eval(A + operator + B)
            display_var.set(result)
            A = str(result)
            B = ""
            operator = ""
    except Exception as e:
        display_var.set("Error")

def set_operator(value):
    global operator
    if A:
        operator = value
        display_var.set(operator)

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
operations = ["+", "-", "*", "/"]
row = 1
col = 3
for op in operations:
    tk.Button(root, text=op, width=5, height=2, command=lambda o=op: set_operator(o)).grid(row=row, column=col, padx=5, pady=5)
    row += 1

# Create equal button
tk.Button(root, text="=", width=5, height=2, command=calculate).grid(row=4, column=3, padx=5, pady=5)

# Create clear button
tk.Button(root, text="Clear", width=5, height=2, command=clear_display).grid(row=4, column=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()