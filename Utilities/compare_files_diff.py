"""
Script: compare_files_diff.py
Description: Tool for compare files diff
Category: Utilities
"""
import os

def list_files_in_directory(directory):
    """Returns a set of file names in the given directory."""
    return set(os.listdir(directory))

def find_differences(folder1, folder2):
    """Finds files that are not common in both folders."""
    files_in_folder1 = list_files_in_directory(folder1)
    files_in_folder2 = list_files_in_directory(folder2)

    only_in_folder1 = files_in_folder1 - files_in_folder2
    only_in_folder2 = files_in_folder2 - files_in_folder1

    return only_in_folder1, only_in_folder2

def print_differences(folder1, folder2):
    """Prints files that do not appear in both folders."""
    only_in_folder1, only_in_folder2 = find_differences(folder1, folder2)

    if only_in_folder1:
        print(f"Files only in {folder1}:")
        for file in only_in_folder1:
            print(file)
    else:
        print(f"No unique files in {folder1}")

    if only_in_folder2:
        print(f"Files only in {folder2}:")
        for file in only_in_folder2:
            print(file)
    else:
        print(f"No unique files in {folder2}")

# Replace these with the paths to your folders
folder1 = r"C:\Users\henry\Desktop\Projects\AUBA\New folder"
folder2 = r"C:\Users\henry\Desktop\Projects\AUBA\Excel&PDF (90)"

print_differences(folder1, folder2)
