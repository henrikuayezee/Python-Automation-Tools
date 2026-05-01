"""
Script: delete_old_movies.py
Description: Tool for delete old movies
Category: File_Management
"""
import os
import shutil
from tqdm import tqdm
import re

def delete_old_movies(directory_path):
    total_dirs = sum([len(dirs) for _, dirs, _ in os.walk(directory_path)])
    progress_bar = tqdm(total=total_dirs, desc='Processing')

    for root, dirs, _ in os.walk(directory_path, topdown=False):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            try:
                print(f"Deleting directory: {dir_path}")
                shutil.rmtree(dir_path)
            except OSError:
                print(f"Skipping non-empty directory: {dir_path}")

            progress_bar.update(1)

    progress_bar.close()

def extract_year(file_name):
    # Extract year from the file name
    # Updated to handle years enclosed in square brackets or normal brackets
    # Adjust this function based on your actual file naming convention
    year_match = re.search(r'\b(\d{4})\b|\((\d{4})\)|\[(\d{4})\]', file_name)
    if year_match:
        return year_match.group(1) or year_match.group(2) or year_match.group(3)
    else:
        return None

# Replace 'your_directory_path' with the actual path of your directory
directory_path = r"E:\[64]MOVIES LIBRARY\SUPER HERO MOVIES"

delete_old_movies(directory_path)
