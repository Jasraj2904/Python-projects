import tkinter as tk
from math import pow

def calculate():
    p = float(entry_p.get())
    t = float(entry_t.get())
    r = float(entry_r.get())

    si = (p * t * r) / 100
    ci = p * (pow((1 + r / 100), t)) - p

    result_si.config(text="Simple Interest: " + str(round(si, 2)))
    result_ci.config(text="Compound Interest: " + str(round(ci, 2)))

window = tk.Tk()
window.title("Interest Calculator")
window.geometry("350x300")

tk.Label(window, text="Principal Amount").pack()
entry_p = tk.Entry(window)
entry_p.pack()

tk.Label(window, text="Time Period (years)").pack()
entry_t = tk.Entry(window)
entry_t.pack()

tk.Label(window, text="Rate of Interest").pack()
entry_r = tk.Entry(window)
entry_r.pack()

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

result_si = tk.Label(window, text="")
result_si.pack()

result_ci = tk.Label(window, text="")
result_ci.pack()

window.mainloop()