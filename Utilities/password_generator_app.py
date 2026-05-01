"""
Script: password_generator_app.py
Description: Tool for password generator app
Category: Utilities
"""
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import random
import string
import datetime
import os

LOG_FILE = 'password_log.txt'

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Sophisticated Password Generator')
        self.root.geometry('400x400')
        self.create_widgets()

    def create_widgets(self):
        # Label for password label
        tk.Label(self.root, text='Label (e.g., Gmail, Bank):').pack(pady=(10, 0))
        self.label_entry = tk.Entry(self.root, width=40)
        self.label_entry.pack(pady=5)

        # Password length
        tk.Label(self.root, text='Password Length:').pack(pady=(10, 0))
        self.length_var = tk.IntVar(value=16)
        self.length_spin = tk.Spinbox(self.root, from_=8, to=64, textvariable=self.length_var, width=5)
        self.length_spin.pack(pady=5)

        # Character set checkboxes
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text='Include Uppercase (A-Z)', variable=self.use_upper).pack(anchor='w', padx=20)
        tk.Checkbutton(self.root, text='Include Lowercase (a-z)', variable=self.use_lower).pack(anchor='w', padx=20)
        tk.Checkbutton(self.root, text='Include Digits (0-9)', variable=self.use_digits).pack(anchor='w', padx=20)
        tk.Checkbutton(self.root, text='Include Symbols (!@#$...)', variable=self.use_symbols).pack(anchor='w', padx=20)

        # Generate button
        tk.Button(self.root, text='Generate Password', command=self.generate_password).pack(pady=10)

        # Password display
        self.password_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.password_var, width=40, state='readonly', justify='center').pack(pady=5)

        # Copy and View Log buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text='Copy Password', command=self.copy_password).pack(side='left', padx=5)
        tk.Button(btn_frame, text='View Log', command=self.view_log).pack(side='left', padx=5)

    def generate_password(self):
        length = self.length_var.get()
        label = self.label_entry.get().strip()
        charsets = []
        if self.use_upper.get():
            charsets.append(string.ascii_uppercase)
        if self.use_lower.get():
            charsets.append(string.ascii_lowercase)
        if self.use_digits.get():
            charsets.append(string.digits)
        if self.use_symbols.get():
            charsets.append(string.punctuation)
        if not charsets:
            messagebox.showerror('Error', 'Select at least one character set!')
            return
        if length < len(charsets):
            messagebox.showerror('Error', f'Length must be at least {len(charsets)} to include all selected types.')
            return
        # Ensure at least one from each selected set
        password_chars = [random.choice(cs) for cs in charsets]
        all_chars = ''.join(charsets)
        password_chars += [random.choice(all_chars) for _ in range(length - len(charsets))]
        random.shuffle(password_chars)
        password = ''.join(password_chars)
        self.password_var.set(password)
        self.log_password(label, password)

    def log_password(self, label, password):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        label = label if label else 'No Label'
        log_entry = f'[{timestamp}] {label}: {password}\n'
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    def copy_password(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo('Copied', 'Password copied to clipboard!')
        else:
            messagebox.showwarning('No Password', 'No password to copy!')

    def view_log(self):
        if not os.path.exists(LOG_FILE):
            messagebox.showinfo('Log', 'No passwords have been generated yet.')
            return
        log_window = tk.Toplevel(self.root)
        log_window.title('Password Log')
        log_window.geometry('500x300')
        st = scrolledtext.ScrolledText(log_window, wrap=tk.WORD, state='normal')
        st.pack(expand=True, fill='both')
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            st.insert('1.0', f.read())
        st.config(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop() 