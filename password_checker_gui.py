import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_strength():
    password = entry.get()
    if len(password) < 8:
        result = "Weak: At least 8 characters required"
    elif not re.search(r"[A-Z]", password):
        result = "Weak: Add an uppercase letter"
    elif not re.search(r"[a-z]", password):
        result = "Weak: Add a lowercase letter"
    elif not re.search(r"[0-9]", password):
        result = "Weak: Add a number"
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        result = "Weak: Add a special character"
    else:
        result = "Strong Password ✅"

    messagebox.showinfo("Password Strength", result)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")  # Increased height for better spacing

# Heading
heading = tk.Label(root, text="Check Your Password Strength", font=("Arial", 14))
heading.pack(pady=10)

# Instruction line
info = tk.Label(root, text="Password must contain: uppercase, lowercase, number, special character", font=("Arial", 9), fg="gray")
info.pack()

# Entry field
entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=10)

# Button
check_btn = tk.Button(root, text="Check Strength", command=check_strength)
check_btn.pack(pady=10)

# Run the app
root.mainloop()
