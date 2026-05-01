"""
Script: 0_and_1_convertorscript.py
Description: Tool for 0 and 1 convertorscript
Category: Computer_Vision_Datasets
"""
import os
from tqdm import tqdm

# Enter directory name here
dir_path = r"C:\Users\henry\Desktop\Dataset\yolo labels"

# File are stored here
output_folder = r"C:\Users\henry\Desktop\Dataset\trimmed"

# Get the total number of files in the directory
total_files = len([filename for filename in os.listdir(dir_path) if filename.endswith(".txt")])

for filename in tqdm(os.listdir(dir_path), total=total_files):
    if filename.endswith(".txt"):

        # open the input file
        with open(os.path.join(dir_path, filename), 'r') as f_in:
            # read the contents of the file
            lines = f_in.readlines()

        # initialize an empty list to hold the modified data
        new_lines = []

        # loop through each line of the input file
        for line in lines:
            # split the line into a list of values
            values = line.strip().split()
            
            # convert negative values to 0 and values greater than 1 to 1
            new_values = [max(0, min(1, float(x))) for x in values[1:]]
            
            # add the modified values to the new_lines list
            new_lines.append(f"{values[0]} {' '.join(map(str, new_values))}\n")

        # open the output file
        os.makedirs(output_folder, exist_ok=True)
        output_file = os.path.join(output_folder, filename)
        with open(output_file, 'w') as f_out:
            # write the modified data to the output file
            f_out.writelines(new_lines)
