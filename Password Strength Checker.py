from tkinter import *
from tkinter import ttk
import re
def check_strength(event=None):
    password = entry.get()
    strength = 0
    if len(password) >= 6:
        strength += 20
    if len(password) >= 10:
        strength += 20
    if re.search("[a-z]", password):
        strength += 20
    if re.search("[0-9]", password):
        strength += 20
    if re.search("[@#$%^&*()!]", password):
        strength += 20
    progress['value'] = strength
    if strength <= 40:
        result.config(text="Password Strength: Weak", fg="red")
    elif strength <= 80:
        result.config(text="Password Strength: Medium", fg="orange")
    else:
        result.config(text="Password Strength: Strong", fg="green")
window = Tk()
window.title("Password Strength Checker")
window.geometry("420x260")
Label(window, text="Enter Password", font=("Arial", 12)).pack(pady=10)
entry = Entry(window , width=30)
entry.pack()
entry.bind("<KeyRelease>", check_strength)
progress = ttk.Progressbar(window, length=250, maximum=100)
progress.pack(pady=15)
result = Label(window, text="Password Strength: ", font=("Arial", 12))
result.pack()
window.mainloop()