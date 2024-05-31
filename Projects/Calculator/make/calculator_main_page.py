import tkinter as tk

A = ""
B = ""
operator = ""

def Enter():

    def add_to_display(value):
        global A, B, operator
        if operator:
            B += value
            display_var.set(B)
        else:
            A += value
            display_var.set(A)

    def set_operator(value):
        global operator
        if A and not B:
            operator = value
            display_var.set(operator)
        elif A and B:
            calculate()
            operator = value
            display_var.set(operator)    

    def clear_display():
        global A, B, operator
        A = ""
        B = ""
        operator = ""
        display_var.set("0")

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


    # Create the Calculator window        
    root2 = tk.Tk()
    root2.title("Calculator")
    display_var = tk.StringVar()
    display_label = tk.Label(root2, textvariable=display_var, font=('Arial', 20), anchor='e', bg='white', bd=5)
    display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    # Create number buttons
    numbers = "789456123.0 "
    row = 2
    col = 0
    for num in numbers:
        tk.Button(root2, text=num, width=5, height=2, command=lambda n=num: add_to_display(n)).grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 2:
            col = 0
            row += 1

    # Create operation buttons
    operations = ["+", "-", "*", "/"]
    row = 2
    col = 3
    for op in operations:
        tk.Button(root2, text=op, width=5, height=2, command=lambda o=op: set_operator(o)).grid(row=row, column=col, padx=5, pady=5)
        row += 1

    # Creating extra button 
    tk.Button(root2, text="   ", width=5, height=2).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(root2, text="   ", width=5, height=2).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root2, text="   ", width=5, height=2).grid(row=1, column=2, padx=5, pady=5)
    # Create clear button
    tk.Button(root2, text="Clear", width=5, height=2, command=clear_display).grid(row=1, column=3, padx=5, pady=5)
    
    # Create equal button
    tk.Button(root2, text="=", width=5, height=2, command=calculate).grid(row=4, column=3, padx=5, pady=5)

    # Run the calculator event loop
    root2.mainloop()

Enter()
