"""
Script: fi_stats.py
Description: Tool for fi stats
Category: Data_Processing_and_Web
"""
# Save the desktop UI app as a .py file for the user to run locally

script_code = """
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from datetime import datetime

def process_kpi_file(file_path, selected_date):
    df = pd.read_excel(file_path, sheet_name='session')
    df['Email'] = df['Email'].fillna(method='ffill')
    df['Start Date'] = pd.to_datetime(df['Start Date']).dt.date
    target_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
    filtered = df[df['Start Date'] == target_date].copy()
    filtered.rename(columns={'Start Date': 'Date'}, inplace=True)
    filtered['Hours'] = (filtered['CountDistinct of Item Id'] * filtered['Avg Duration Mins per Item']) / 60
    result = filtered[[
        'Email', 'Date', 'Step', 'CountDistinct of Item Id',
        'Avg Duration Mins per Item', 'Avg Action Count per Item', 'Hours'
    ]]
    return result

def launch_app():
    def load_file():
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            file_label.config(text=file_path)
            app.file_path = file_path

    def run_process():
        date_input = date_entry.get()
        if not hasattr(app, 'file_path'):
            messagebox.showerror("Error", "Please select a file first.")
            return
        try:
            result_df = process_kpi_file(app.file_path, date_input)
            if result_df.empty:
                messagebox.showinfo("No Data", f"No data found for {date_input}.")
            else:
                app.result_df = result_df
                for i in tree.get_children():
                    tree.delete(i)
                for _, row in result_df.iterrows():
                    tree.insert("", "end", values=list(row))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def export_to_excel():
        if not hasattr(app, 'result_df'):
            messagebox.showerror("Error", "No data to export.")
            return
        export_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
        if export_path:
            app.result_df.to_excel(export_path, index=False)
            messagebox.showinfo("Success", f"File saved to {export_path}")

    app = tk.Tk()
    app.title("KPI Export Formatter")

    tk.Label(app, text="Select Fi Annotator KPI Export file:").grid(row=0, column=0, sticky="w")
    tk.Button(app, text="Browse", command=load_file).grid(row=0, column=1)
    file_label = tk.Label(app, text="No file selected")
    file_label.grid(row=1, column=0, columnspan=2, sticky="w")

    tk.Label(app, text="Enter date (YYYY-MM-DD):").grid(row=2, column=0, sticky="w")
    date_entry = tk.Entry(app)
    date_entry.grid(row=2, column=1, sticky="w")

    tk.Button(app, text="Run", command=run_process).grid(row=3, column=0)
    tk.Button(app, text="Export to Excel", command=export_to_excel).grid(row=3, column=1)

    cols = ['Email', 'Date', 'Step', 'CountDistinct of Item Id',
            'Avg Duration Mins per Item', 'Avg Action Count per Item', 'Hours']
    tree = ttk.Treeview(app, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=4, column=0, columnspan=2)

    app.mainloop()

if __name__ == "__main__":
    launch_app()
"""

file_path = "/mnt/data/Fi_stats.py"
with open(file_path, "w") as f:
    f.write(script_code)

file_path
