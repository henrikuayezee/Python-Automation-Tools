"""
Script: append_filename.py
Description: Tool for append filename
Category: File_Management
"""
import os

def add_string_to_filenames(directory, string):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Iterate over each file
    for filename in files:
        # Check if the item is a file (not a directory)
        if os.path.isfile(os.path.join(directory, filename)):
            # Construct the new filename by adding the string in front
            new_filename = string + filename

            # Get the full path of the file
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")

# Usage example
directory_path = r"E:\DP World Data\Negative Images and Labels (Original)\images"
string_to_add = '-'
add_string_to_filenames(directory_path, string_to_add)
