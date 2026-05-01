"""
Script: auba_filenames.py
Description: Tool for auba filenames
Category: Project_Specific
"""
import os

def list_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        for file in files:
            name, _ = os.path.splitext(file)
            print(name)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    list_files_in_directory(directory) 