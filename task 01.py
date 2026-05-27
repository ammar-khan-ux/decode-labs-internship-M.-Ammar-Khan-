import tkinter as tk


def check_strength():
    password = entry.get()

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    length = len(password)

    # Default style
    result_label.config(fg="black")

    if length < 6:
        result.set("Weak ❌ (Too short)")
        result_label.config(fg="#e74c3c")  # red

    elif length >= 8 and has_upper and has_digit and has_symbol:
        result.set("Strong 💪")
        result_label.config(fg="#2ecc71")  # green

    elif has_lower and has_digit:
        result.set("Medium ⚠️")
        result_label.config(fg="#f39c12")  # orange

    else:
        result.set("Weak ❌")
        result_label.config(fg="#e74c3c")  # red


def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        show_btn.config(text="👁 Show")
    else:
        entry.config(show='')
        show_btn.config(text="🙈 Hide")


# Window setup
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("450x300")
window.config(bg="#1e1e2f")

# Title
title = tk.Label(
    window,
    text="🔐 Password Strength Checker",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=15)

# Input box
entry = tk.Entry(
    window,
    show="*",
    font=("Arial", 14),
    width=28,
    justify="center"
)
entry.pack(pady=10)

# Show/Hide button
show_btn = tk.Button(
    window,
    text="👁 Show",
    command=toggle_password,
    font=("Arial", 10),
    bg="#34495e",
    fg="white",
    width=10
)
show_btn.pack(pady=5)

# Check button
btn = tk.Button(
    window,
    text="Check Strength",
    command=check_strength,
    font=("Arial", 12, "bold"),
    bg="#3498db",
    fg="white",
    width=18
)
btn.pack(pady=15)

# Result
result = tk.StringVar()
result_label = tk.Label(
    window,
    textvariable=result,
    font=("Arial", 14, "bold"),
    bg="#1e1e2f"
)
result_label.pack(pady=10)

# Footer
footer = tk.Label(
    window,
    text="DecodeLabs Cyber Security Project",
    font=("Arial", 9),
    bg="#1e1e2f",
    fg="gray"
)
footer.pack(side="bottom", pady=10)

window.mainloop()
