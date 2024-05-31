import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
label_num1 = tk.Label(root, text="Number 1:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Number 2:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Create operation dropdown
operation_var = tk.StringVar()
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_var.set(operations[0])  # Default operation
operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.grid(row=2, column=0, columnspan=2)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

# Create result label
label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2)

# Run the main event loop
root.mainloop()