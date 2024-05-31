import tkinter as tk

A = ""
B = ""
operator = ""
count = -1
back = list()
add = list()

def Enter():

    def add_to_display(value):
        global A, B, operator
        if operator:
            B += value
            add.append(B)
            display_var.set(B)
        else:
            A += value
            add.append(A)
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

    def remove():
        global A, B, operator,add
        if operator:
            B = add[-2]
            display_var.set(B)
        else:
            A = add[-1]
            display_var.set(A)       

    def clear_display():
        global A, B, operator
        A = ""
        B = ""
        operator = ""
        count = 0
        back = ()
        add = ()
        display_var.set("0")

    def calculate():
        global A, B, operator, back
        try:
            if A and B and operator:
                back.append(A)
                back.append(operator)
                back.append(B)
                result = eval(A + operator + B)
                if result == A:
                    y = 0
                else:    
                    back.append(result)
                display_var.set(result)
                A = str(result)
                B = ""
                operator = ""
        except Exception as e:
            display_var.set("Error")

    def back():
        global back,count
        try:
            display_var.set(back[count])
            count -= 1
        except:
            display_var.set(back)        

    # Create the Calculator window        
    root = tk.Tk()
    root.title("Calculator")
    display_var = tk.StringVar()
    display_label = tk.Label(root, textvariable=display_var, font=('Arial', 20), anchor='e', bg='white', bd=5)
    display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    # Create number buttons
    numbers = "789456123.0 "
    row = 2
    col = 0
    for num in numbers:
        tk.Button(root, text=num, width=5, height=2, command=lambda n=num: add_to_display(n)).grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 2:
            col = 0
            row += 1

    # Create operation buttons
    operations = ["+", "-", "*", "/"]
    row = 2
    col = 3
    for op in operations:
        tk.Button(root, text=op, width=5, height=2, command=lambda o=op: set_operator(o)).grid(row=row, column=col, padx=5, pady=5)
        row += 1

     # Create exit button
    tk.Button(root, text="Exit", width=5, height=2, command=root.quit).grid(row=1, column=0, padx=5, pady=5)
    # Creating extra button
    tk.Button(root, text="Back", width=5, height=2,command=back).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="    ", width=5, height=2).grid(row=1, column=2, padx=5, pady=5)
    # Create clear button
    tk.Button(root, text="Clear", width=5, height=2, command=clear_display).grid(row=1, column=3, padx=5, pady=5)
    
    # Create equal button
    tk.Button(root, text="=", width=5, height=2, command=calculate).grid(row=5, column=2, padx=5, pady=5)

    # Run the calculator event loop
    root.mainloop()

Enter()
