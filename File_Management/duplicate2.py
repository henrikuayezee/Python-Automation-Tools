"""
Script: duplicate2.py
Description: Tool for duplicate2
Category: File_Management
"""
import os
from tqdm import tqdm

# Define the path of the directory containing the text files to check
directory_path = r"C:/Users/henry/Desktop/Smoke and Fire/Training/labels"

# Define the path of the output file to write the results to
output_file_path = r"C:/Users/henry/Desktop/duplicate_files.txt"

# Create an empty set to store the lines of text that have been seen
seen_lines = set()

# Create an empty list to store the names of the text files that have duplicate lines
files_with_duplicates = []

# Loop through each file in the directory
with tqdm(total=len(os.listdir(directory_path))) as pbar:
    for filename in os.listdir(directory_path):
        # Check if the file is a text file
        if filename.endswith(".txt"):
            # Open the file
            with open(os.path.join(directory_path, filename), "r") as file:
                # Loop through each line of the file
                for line in file:
                    # Check if the line has already been seen
                    if line in seen_lines:
                        # If it has, add the file name to the list of files with duplicates
                        files_with_duplicates.append(filename)
                        # Break out of the inner loop to move on to the next file
                        break
                    # If the line hasn't been seen, add it to the set of seen lines
                    seen_lines.add(line)
        pbar.update(1)

# Write the names of the text files with duplicate lines to the output file
with open(output_file_path, "w") as output_file:
    output_file.write("Text files with duplicate lines:\n")
    for filename in set(files_with_duplicates):
        output_file.write(f"- {filename}\n")
