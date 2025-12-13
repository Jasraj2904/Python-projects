import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Product Calculator")
window.geometry("300x200")

# Function to calculate product
def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    result_label.config(text="Product: " + str(product))

# Labels
tk.Label(window, text="Enter First Number:").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter Second Number:").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack()

# Button
tk.Button(window, text="Calculate Product", command=calculate_product).pack(pady=10)

# Result Label
result_label = tk.Label(window, text="Product:")
result_label.pack()

# Run the application
window.mainloop()
