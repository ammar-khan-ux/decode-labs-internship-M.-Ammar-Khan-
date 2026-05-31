import tkinter as tk
from tkinter import ttk, messagebox
import random

# --- CRYPTOGRAPHIC CORE LOGIC ---


def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isupper():
            # Apply Caesar shift formula: E_n(x) = (x + n) % 26
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result += encrypted_char
        elif char.islower():
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result += encrypted_char
        else:
            result += char  # Keeps spaces, numbers, and special chars intact
    return result

# --- GUI INTERACTION FUNCTIONS ---


def process_cryptography(mode):
    input_text = input_text_area.get("1.0", tk.END).strip()
    key_raw = key_entry.get().strip()

    if not input_text:
        messagebox.showwarning(
            "Input Error", "Please enter some text to process.")
        return

    if not key_raw.isdigit():
        messagebox.showerror(
            "Key Error", "Shift Key must be a valid positive integer.")
        return

    shift_key = int(key_raw)

    if mode == 'encrypt':
        output = caesar_cipher(input_text, shift_key, mode='encrypt')
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert(tk.END, output)
    elif mode == 'decrypt':
        output = caesar_cipher(input_text, shift_key, mode='decrypt')
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert(tk.END, output)


def generate_random_key():
    random_key = random.randint(1, 25)
    key_entry.delete(0, tk.END)
    key_entry.insert(0, str(random_key))


def copy_to_clipboard():
    output_data = output_text_area.get("1.0", tk.END).strip()
    if output_data:
        root.clipboard_clear()
        root.clipboard_append(output_data)
        messagebox.showinfo(
            "Success", "Output copied to clipboard successfully!")
    else:
        messagebox.showwarning("Empty", "Nothing to copy yet.")


def clear_fields():
    input_text_area.delete("1.0", tk.END)
    output_text_area.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)
    char_count_label.config(text="Characters: 0")


def update_char_count(event=None):
    count = len(input_text_area.get("1.0", tk.END).strip())
    char_count_label.config(text=f"Characters: {count}")


# --- UI DESIGN (Tkinter Setup) ---
root = tk.Tk()
root.title("DecodeLabs - Cryptographic Engine v2.0")
root.geometry("620x720")
root.resizable(False, False)
root.configure(bg="#f4f6f9")

# Style configuration for premium look
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Helvetica', 10, 'bold'), borderwidth=1)
style.configure('Action.TButton', background='#1a73e8', foreground='white')
style.map('Action.TButton', background=[('active', '#1557b0')])

# Header Panel
header_frame = tk.Frame(root, bg="#0f172a", height=70)
header_frame.pack(fill=tk.X)
header_label = tk.Label(header_frame, text="CRYPTOGRAPHIC ENGINE", font=(
    'Helvetica', 14, 'bold'), fg="#f8fafc", bg="#0f172a")
header_label.pack(pady=10)
sub_header = tk.Label(header_frame, text="Project 2: Confidentiality Logic | Batch 2026", font=(
    'Helvetica', 9), fg="#94a3b8", bg="#0f172a")
sub_header.pack()

# Main Container
main_frame = tk.Frame(root, bg="#f4f6f9", padx=20, pady=15)
main_frame.pack(fill=tk.BOTH, expand=True)

# 1. Input Section
tk.Label(main_frame, text="Enter Plaintext / Ciphertext:",
         font=('Helvetica', 10, 'bold'), bg="#f4f6f9", fg="#334155").pack(anchor=tk.W)
input_text_area = tk.Text(main_frame, height=6, font=(
    'Courier New', 11), wrap=tk.WORD, bd=1, relief=tk.SOLID)
input_text_area.pack(fill=tk.X, pady=(5, 2))
input_text_area.bind("<KeyRelease>", update_char_count)

# Character Counter Label
char_count_label = tk.Label(main_frame, text="Characters: 0", font=(
    'Helvetica', 8, 'italic'), bg="#f4f6f9", fg="#64748b")
char_count_label.pack(anchor=tk.E, pady=(0, 10))

# 2. Configuration Parameters (Key & Controls)
config_frame = tk.LabelFrame(main_frame, text=" Configuration & Control Keys ", font=(
    'Helvetica', 9, 'bold'), bg="#f4f6f9", fg="#1e293b", padx=10, pady=10)
config_frame.pack(fill=tk.X, pady=10)

tk.Label(config_frame, text="Shift Key (Integer):", font=(
    'Helvetica', 10), bg="#f4f6f9").grid(row=0, column=0, sticky=tk.W, padx=5)
key_entry = ttk.Entry(config_frame, width=10, font=('Helvetica', 10))
key_entry.grid(row=0, column=1, padx=5, sticky=tk.W)

rand_btn = ttk.Button(config_frame, text="Generate Key",
                      command=generate_random_key)
rand_btn.grid(row=0, column=2, padx=5)

clear_btn = ttk.Button(config_frame, text="Clear All", command=clear_fields)
clear_btn.grid(row=0, column=3, padx=10)

# 3. Execution Action Buttons
btn_frame = tk.Frame(main_frame, bg="#f4f6f9")
btn_frame.pack(fill=tk.X, pady=10)

encrypt_btn = ttk.Button(btn_frame, text="🔒 ENCRYPT DATA",
                         style='Action.TButton', command=lambda: process_cryptography('encrypt'))
encrypt_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5), ipady=5)

decrypt_btn = ttk.Button(btn_frame, text="🔓 DECRYPT DATA",
                         style='Action.TButton', command=lambda: process_cryptography('decrypt'))
decrypt_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0), ipady=5)

# 4. Output Section
tk.Label(main_frame, text="Processed Output:", font=('Helvetica', 10,
         'bold'), bg="#f4f6f9", fg="#334155").pack(anchor=tk.W, pady=(10, 5))
output_text_area = tk.Text(main_frame, height=6, font=(
    'Courier New', 11), wrap=tk.WORD, bd=1, relief=tk.SOLID, bg="#f8fafc")
output_text_area.pack(fill=tk.X, pady=5)

copy_btn = ttk.Button(
    main_frame, text="📋 Copy Output to Clipboard", command=copy_to_clipboard)
copy_btn.pack(fill=tk.X, pady=5)

# Footer Note
footer_label = tk.Label(root, text="Powered by DecodeLabs Security Engine", font=(
    'Helvetica', 8), fg="#94a3b8", bg="#f4f6f9")
footer_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
