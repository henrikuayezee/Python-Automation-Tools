"""
Script: copyfilesnew.py
Description: Tool for copyfilesnew
Category: File_Management
"""
#Copy files

import shutil
import os
from tqdm import tqdm

# Set the paths for the source and destination folders
src_folder = r"E:\DP World Data\Negative Images and Labels (Original)\labels"
dest_folder = r"E:\DP World Data\Negative Images and Labels\labels"
# Check if the destination folder exists
if not os.path.exists(dest_folder):
    print("The destination folder does not exist. Please create it first.")
else:
    # Use shutil to copy all files from the source folder to the destination folder
    file_count = len(os.listdir(src_folder))
    with tqdm(total=file_count) as pbar:
        for filename in os.listdir(src_folder):
            src_file = os.path.join(src_folder, filename)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dest_folder)
            pbar.update(1)
    print("Files copied successfully.")
