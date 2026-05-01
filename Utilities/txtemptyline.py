"""
Script: txtemptyline.py
Description: Tool for txtemptyline
Category: Utilities
"""
###You can use the following Python script to remove the extra empty line from each TXT file in a given directory:

import os
from tqdm import tqdm

def remove_empty_line(filename):
    # Read the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove the empty line
    lines = [line.strip() for line in lines if line.strip()]

    # Write the modified content back to the file
    with open(filename, 'w') as file:
        file.write('\n'.join(lines))

def clear_empty_lines(directory):
    # Get the list of TXT files
    txt_files = [filename for filename in os.listdir(directory) if filename.endswith('.txt')]

    # Initialize the progress bar
    progress_bar = tqdm(total=len(txt_files), desc='Processing Files', unit='file')

    # Iterate over the TXT files
    for filename in txt_files:
        file_path = os.path.join(directory, filename)
        remove_empty_line(file_path)

        # Update the progress bar
        progress_bar.update(1)

    # Close the progress bar
    progress_bar.close()

# Specify the directory containing the TXT files
directory = r"C:\Users\henry\Downloads\Compressed\PPEdataset\train output"

# Call the function to clear empty lines
clear_empty_lines(directory)
