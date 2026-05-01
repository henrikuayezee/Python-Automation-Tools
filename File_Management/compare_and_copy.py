"""
Script: compare_and_copy.py
Description: Tool for compare and copy
Category: File_Management
"""
import os
import shutil
from tqdm import tqdm

dir_a = r"C:\Users\henry\Desktop\Smoke and Fire\Validate\images"
dir_b = r"C:\Users\henry\Desktop\Dataset\trimmed"
dir_c = r"C:\Users\henry\Desktop\Smoke and Fire\Validate\labels"

# Get list of files in directory A without extensions
files_a = [os.path.splitext(f)[0] for f in os.listdir(dir_a) if os.path.isfile(os.path.join(dir_a, f))]

# Get list of files in directory B without extensions
files_b = [os.path.splitext(f)[0] for f in os.listdir(dir_b) if os.path.isfile(os.path.join(dir_b, f))]

# Compare filenames and copy matching files from directory B to directory C
with tqdm(total=len(set(files_a) & set(files_b)), desc="Copying files") as pbar:
    for filename in set(files_a) & set(files_b):
        shutil.copy(os.path.join(dir_b, filename + ".txt"), os.path.join(dir_c, filename + ".txt"))
        pbar.update(1)
