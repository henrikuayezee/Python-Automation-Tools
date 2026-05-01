"""
Script: ammend_extensions.py
Description: Tool for ammend extensions
Category: Utilities
"""
# Open the input file and read in the list of filenames
with open("C:/Users/henry/Desktop/corrupted files (labels).txt", "r") as f:
    filenames = f.read().splitlines()

# Add ".txt" to each filename
new_filenames = [filename + ".jpeg" for filename in filenames]

# Open the output file and write the updated list of filenames
with open("C:/Users/henry/Desktop/corrupted files_images.txt", "w") as f:
    f.write("/n".join(new_filenames))
