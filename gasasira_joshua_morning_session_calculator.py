import tkinter as tk

def calculatorFunc():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation.get() == "+":
            result = num1 + num2
        elif operation.get() == "-":
            result = num1 - num2
        elif operation.get() == "*":
            result = num1 * num2
        elif operation.get() == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Cannot divide by zero"
        
        label_result.config(text="Result: " + str(result))
    except ValueError:
        result = "Error: Enter valid numbers"
        label_result.config(text="Result: " + str(result))

# Create the main window
window = tk.Tk()
window.title("Gasasira Joshua calculator")

# Create input fields
label_num1 = tk.Label(window, text="Number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(window, text="Number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Create operation dropdown
label_operation = tk.Label(window, text="Operation:")
label_operation.grid(row=2, column=0, padx=10, pady=5)
operation = tk.StringVar()
operation.set("+")  # Default operation is addition
dropdown_operation = tk.OptionMenu(window, operation, "+", "-", "*", "/")
dropdown_operation.grid(row=4, column=1, padx=10, pady=5)

# Create calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculatorFunc)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the result
label_result = tk.Label(window, text="Result: ", font=("Arial", 20, "bold"))
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Configure grid weights to expand the columns
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Start the main event loop
window.mainloop()
