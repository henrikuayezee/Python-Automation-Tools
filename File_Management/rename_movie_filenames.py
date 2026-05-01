"""
Script: rename_movie_filenames.py
Description: Tool for rename movie filenames
Category: File_Management
"""
import os

def remove_watch_from_filenames(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    for file in files:
        # Check if the file name contains "Watch "
        if "Watch " in file:
            new_name = file.replace("Watch ", "")
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f'Renamed "{file}" to "{new_name}"')

if __name__ == "__main__":
    target_directory = r"C:\Users\henry\Videos\Black Mirror"  # Replace this with your desired directory path
    remove_watch_from_filenames(target_directory)
