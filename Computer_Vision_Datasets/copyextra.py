"""
Script: copyextra.py
Description: Tool for copyextra
Category: Computer_Vision_Datasets
"""
#copy the missing json labels that were not converted from coco to yolo to an output folder

import os
import shutil
from tqdm import tqdm

directory1 = r"C:\Users\henry\Desktop\Copy extra\labels"  # First directory path
directory2 = r"C:\Users\henry\Desktop\Smoke and Fire\Training\labels"  # Second directory path
out_folder = r"C:\Users\henry\Desktop\Copy extra\Extra"  # Output folder path

# Get a set of file names in directory2 without extensions
dir2_files = set([os.path.splitext(f)[0] for f in os.listdir(directory2)])

# Copy the files in directory1 that are not in directory2 to the output folder
for file_name in tqdm(os.listdir(directory1)):
    name_without_ext = os.path.splitext(file_name)[0]
    if name_without_ext not in dir2_files:
        src_file = os.path.join(directory1, file_name)
        dst_file = os.path.join(out_folder, file_name)
        shutil.copy(src_file, dst_file)