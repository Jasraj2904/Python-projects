import tkinter as tk
def convert_to_cm():
    try:
        inches = float(entry_inches.get())
        centimeters = inches * 2.54
        result_label.config(text=f"Length in Centimeters: {centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number")
window = tk.Tk()
window.title("Inches to Centimeters Converter")
window.geometry("350x200")
heading = tk.Label(window, text="Inches to Centimeters", font=("Arial", 14))
heading.pack(pady=10)
label_inches = tk.Label(window, text="Enter length in inches:")
label_inches.pack()
entry_inches = tk.Entry(window)
entry_inches.pack(pady=5)
convert_button = tk.Button(window, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()
window.mainloop()