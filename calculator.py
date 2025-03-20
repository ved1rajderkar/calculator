import tkinter as tk

# Function to update input field
def press(key):
    entry_var.set(entry_var.get() + str(key))

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_var.get())  # Evaluate the expression
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

# Function to clear the input field
def clear():
    entry_var.set("")

# UI Setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.configure(bg="#f4f4f4")

# Input Field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Button Layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons dynamically
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char == "=":
            btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, bg="#4CAF50", fg="white", command=calculate)
        elif char == "C":
            btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, bg="#f44336", fg="white", command=clear)
        else:
            btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda key=char: press(key))

        btn.grid(row=r+1, column=c, padx=5, pady=5)

# Run the app
root.mainloop()
