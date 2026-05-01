"""
Script: compare_files_sim.py
Description: Tool for compare files sim
Category: Utilities
"""
import os

def list_files_in_directory(directory):
    """Returns a set of file names in the given directory."""
    return set(os.listdir(directory))

def find_similarities(folder1, folder2):
    """Finds files that are common in both folders."""
    files_in_folder1 = list_files_in_directory(folder1)
    files_in_folder2 = list_files_in_directory(folder2)

    common_files = files_in_folder1 & files_in_folder2

    return common_files

def print_similarities(folder1, folder2):
    """Prints files that appear in both folders."""
    common_files = find_similarities(folder1, folder2)

    if common_files:
        print(f"Files common in both {folder1} and {folder2}:")
        for file in common_files:
            print(file)
    else:
        print(f"No common files between {folder1} and {folder2}")

# Replace these with the paths to your folders
folder1 = r"C:\Users\henry\Downloads\Compressed\AUBA (Excel)\results"
folder2 = r"C:\Users\henry\Desktop\Projects\AUBA\New folder"

print_similarities(folder1, folder2)
