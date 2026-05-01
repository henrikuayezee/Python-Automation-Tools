"""
Script: move_files_from_list.py
Description: Tool for move files from list
Category: File_Management
"""
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def move_files_from_list(list_file, source_dir, dest_dir, output_widget):
    try:
        with open(list_file, 'r') as f:
            file_names = [line.strip() for line in f if line.strip()]
    except Exception as e:
        output_widget.insert(tk.END, f"Error reading list file: {e}\n")
        return

    os.makedirs(dest_dir, exist_ok=True)
    moved = 0
    not_found = []
    for file_name in file_names:
        # If the file_name has an extension, use as is; otherwise, match any file with that base name (regardless of extension)
        base_name, ext = os.path.splitext(file_name)
        found = False
        if ext:
            source_path = os.path.join(source_dir, file_name)
            if os.path.exists(source_path):
                shutil.move(source_path, os.path.join(dest_dir, file_name))
                output_widget.insert(tk.END, f"Moved: {file_name}\n")
                moved += 1
                found = True
        else:
            # Search for all files in source_dir with this base name (any extension)
            matches = [f for f in os.listdir(source_dir) if os.path.splitext(f)[0] == base_name]
            if matches:
                for match in matches:
                    shutil.move(os.path.join(source_dir, match), os.path.join(dest_dir, match))
                    output_widget.insert(tk.END, f"Moved: {match}\n")
                    moved += 1
                found = True
        if not found:
            output_widget.insert(tk.END, f"Not found: {file_name}\n")
            not_found.append(file_name)
    output_widget.insert(tk.END, f"\nTotal files moved: {moved}\n")
    if not_found:
        output_widget.insert(tk.END, "Files not found:\n")
        for nf in not_found:
            output_widget.insert(tk.END, f"{nf}\n")

def browse_file(entry):
    filename = filedialog.askopenfilename(title="Select file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)

def browse_folder(entry):
    foldername = filedialog.askdirectory(title="Select folder")
    if foldername:
        entry.delete(0, tk.END)
        entry.insert(0, foldername)

def run_move(list_entry, src_entry, dst_entry, output_widget):
    list_file = list_entry.get()
    source_dir = src_entry.get()
    dest_dir = dst_entry.get()
    output_widget.delete(1.0, tk.END)
    if not (list_file and source_dir and dest_dir):
        messagebox.showerror("Error", "Please select all paths.")
        return
    move_files_from_list(list_file, source_dir, dest_dir, output_widget)

def main():
    root = tk.Tk()
    root.title("Move Files from List App")
    root.geometry("600x400")

    tk.Label(root, text="List File:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    list_entry = tk.Entry(root, width=50)
    list_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(list_entry)).grid(row=0, column=2, padx=5, pady=5)

    tk.Label(root, text="Source Directory:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    src_entry = tk.Entry(root, width=50)
    src_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_folder(src_entry)).grid(row=1, column=2, padx=5, pady=5)

    tk.Label(root, text="Destination Directory:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    dst_entry = tk.Entry(root, width=50)
    dst_entry.grid(row=2, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_folder(dst_entry)).grid(row=2, column=2, padx=5, pady=5)

    tk.Button(root, text="Move Files", command=lambda: run_move(list_entry, src_entry, dst_entry, output)).grid(row=3, column=1, pady=10)

    output = scrolledtext.ScrolledText(root, width=70, height=15)
    output.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main() 