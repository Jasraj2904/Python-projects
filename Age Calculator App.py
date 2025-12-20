import tkinter as tk
from tkinter import messagebox
from datetime import date

# Function to calculate age
def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        # Create birth date object
        birth_date = date(year, month, day)
        today = date.today()

        # Calculate age
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your Present Age is: {age} years")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date.")

# Create main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Heading
tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold")).pack(pady=10)

# Day input
tk.Label(root, text="Day").pack()
entry_day = tk.Entry(root)
entry_day.pack()

# Month input
tk.Label(root, text="Month").pack()
entry_month = tk.Entry(root)
entry_month.pack()

# Year input
tk.Label(root, text="Year").pack()
entry_year = tk.Entry(root)
entry_year.pack()

# Calculate button
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=15)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Run the application
root.mainloop()
