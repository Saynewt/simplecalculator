import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

# Function to calculate the result
def calculate():
    try:
        result = eval(display.get())  # Evaluate the expression in the display
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the display
display = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=40, pady=20, command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=40, pady=20, command=clear_display)
    else:
        button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: update_display(t))
    button.grid(row=row, column=col)

# Run the app
root.mainloop()