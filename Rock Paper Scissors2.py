import tkinter as tk
import random

# Main Window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("450x500")
window.configure(bg="#1e1e2f")
window.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

# ---------------- Functions ----------------
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text=f"👤 You chose: {user_choice}")
    computer_label.config(text=f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="🤝 It's a Tie!", fg="#f1c40f")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result_label.config(text="🎉 You Win!", fg="#2ecc71")
    else:
        computer_score += 1
        result_label.config(text="😞 Computer Wins!", fg="#e74c3c")

    score_label.config(
        text=f"Score  |  You: {user_score}  vs  Computer: {computer_score}"
    )

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    user_label.config(text="👤 You chose:")
    computer_label.config(text="💻 Computer chose:")
    result_label.config(text="Make your move!", fg="white")
    score_label.config(text="Score  |  You: 0  vs  Computer: 0")

# ---------------- UI ----------------
title = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Segoe UI", 22, "bold"),
    bg="#1e1e2f",
    fg="#ffffff"
)
title.pack(pady=20)

score_label = tk.Label(
    window,
    text="Score  |  You: 0  vs  Computer: 0",
    font=("Segoe UI", 14, "bold"),
    bg="#1e1e2f",
    fg="#00d9ff"
)
score_label.pack(pady=10)

user_label = tk.Label(
    window,
    text="👤 You chose:",
    font=("Segoe UI", 12),
    bg="#1e1e2f",
    fg="white"
)
user_label.pack(pady=5)

computer_label = tk.Label(
    window,
    text="💻 Computer chose:",
    font=("Segoe UI", 12),
    bg="#1e1e2f",
    fg="white"
)
computer_label.pack(pady=5)

result_label = tk.Label(
    window,
    text="Make your move!",
    font=("Segoe UI", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)
result_label.pack(pady=20)

# Button Frame
btn_frame = tk.Frame(window, bg="#1e1e2f")
btn_frame.pack(pady=20)

btn_style = {
    "font": ("Segoe UI", 12, "bold"),
    "width": 12,
    "bd": 0,
    "padx": 10,
    "pady": 10
}

rock_btn = tk.Button(
    btn_frame, text="🪨 Rock", bg="#3498db", fg="white",
    command=lambda: play("Rock"), **btn_style
)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    btn_frame, text="📄 Paper", bg="#9b59b6", fg="white",
    command=lambda: play("Paper"), **btn_style
)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(
    btn_frame, text="✂️ Scissors", bg="#e67e22", fg="white",
    command=lambda: play("Scissors"), **btn_style
)
scissors_btn.grid(row=0, column=2, padx=10)

reset_btn = tk.Button(
    window,
    text="🔄 Reset Game",
    font=("Segoe UI", 12, "bold"),
    bg="#e74c3c",
    fg="white",
    bd=0,
    width=20,
    pady=10,
    command=reset_game
)
reset_btn.pack(pady=25)

# Run App
window.mainloop()