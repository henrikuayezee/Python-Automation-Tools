"""
Script: delete_images.py
Description: Tool for delete images
Category: File_Management
"""
import os

# Specify the path to the folder containing the files to delete
folder_path = r"C:\Users\henry\Desktop\Smoke and Fire\Validate\images"

# Specify the path to the text file containing the list of filenames to delete
txt_file_path = r"C:\Users\henry\Desktop\Delete Duplicates.txt"

# Read the list of filenames from the text file
with open(txt_file_path, "r") as f:
    filenames_to_delete = f.read().splitlines()

# Delete files with matching filenames from the folder
for filename in filenames_to_delete:
    file_path = os.path.join(folder_path, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted file: {filename}")
    else:
        print(f"File not found: {filename}")