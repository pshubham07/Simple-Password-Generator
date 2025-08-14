import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = password_length.get()

    try:
        length = int(length)
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return

    char_pool = ""
    if var_upper.get():
        char_pool += string.ascii_uppercase
    if var_lower.get():
        char_pool += string.ascii_lowercase
    if var_digits.get():
        char_pool += string.digits
    if var_symbols.get():
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    # Ensure the password contains at least one character from each selected type
    password = []
    if var_upper.get():
        password.append(random.choice(string.ascii_uppercase))
    if var_lower.get():
        password.append(random.choice(string.ascii_lowercase))
    if var_digits.get():
        password.append(random.choice(string.digits))
    if var_symbols.get():
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)
    final_password = ''.join(password)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, final_password)

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Password Length:").pack(pady=5)
password_length = tk.Entry(root)
password_length.insert(0, "12")
password_length.pack()

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits", variable=var_digits).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor='w', padx=20)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

entry_password = tk.Entry(root, font=('Arial', 12), justify='center')
entry_password.pack(pady=5, ipady=5, ipadx=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

# Run the application
root.mainloop()