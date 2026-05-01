"""
Script: auba_workdone.py
Description: Tool for auba workdone
Category: Project_Specific
"""
import os
import csv
from tqdm import tqdm

# Set the directory path
dir_path = r"C:\Users\Henry\Desktop\auba clean"

# Get list of all JSON files
json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')]

# Output CSV file path
output_csv = os.path.join(dir_path, 'json_filenames.csv')

# Write to CSV with progress bar
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Filename'])  # header
    for filename in tqdm(json_files, desc="Writing filenames to CSV"):
        writer.writerow([filename])

print(f"\nDone. Filenames saved to: {output_csv}")
