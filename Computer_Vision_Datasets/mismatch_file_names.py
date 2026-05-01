"""
Script: mismatch_file_names.py
Description: Tool for mismatch file names
Category: Computer_Vision_Datasets
"""
import os

dir1 = r"C:\Users\henry\Desktop\Dataset\images"
dir2 = r"C:\Users\henry\Desktop\Dataset\labels in coco"
output_file = "output.txt"

dir1_files = set([os.path.splitext(filename)[0].split("_")[0] for filename in os.listdir(dir1)])
dir2_files = set([os.path.splitext(filename)[0].split("_")[0] for filename in os.listdir(dir2)])

mismatched_files = dir1_files.symmetric_difference(dir2_files)

with open(output_file, "w") as f:
    f.write("Mismatched Files:\n")
    for file in mismatched_files:
        f.write(file + "\n")
