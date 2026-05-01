"""
Script: file_duplicate.py
Description: Tool for file duplicate
Category: File_Management
"""
import os
from tqdm import tqdm

def compare_files(directory):
    file_contents = {}

    # Create a file to store the duplicate filenames
    duplicates_file = open("Duplicates.txt", "w")

    # Get the total number of files in the directory
    total_files = len([filename for filename in os.listdir(directory) if filename.endswith('.txt')])

    # Create a progress bar
    progress_bar = tqdm(total=total_files, desc="Comparing Files", unit="file(s)")

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)

            # Read the contents of the file
            with open(file_path, 'r') as file:
                content = file.read()

            # Check if the content matches any previous files
            for other_file, other_content in file_contents.items():
                if content == other_content:
                    duplicates_file.write(f"Match found between '{filename}' and '{other_file}'\n")

            # Add the file content to the dictionary
            file_contents[filename] = content

            # Update the progress bar
            progress_bar.update(1)

    # Close the duplicates file
    duplicates_file.close()

    # Close the progress bar
    progress_bar.close()

# Provide the directory path to check for files
directory_path = r"C:\Users\henry\Desktop\Smoke and Fire\Validate\labels"

compare_files(directory_path)
