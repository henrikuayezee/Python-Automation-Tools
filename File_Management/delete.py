"""
Script: delete.py
Description: Tool for delete
Category: File_Management
"""
import os
import shutil
from tqdm import tqdm

def delete_directory(directory_path):
    try:
        total_files = sum([len(files) for _, _, files in os.walk(directory_path)])
        with tqdm(total=total_files, unit='file') as pbar:
            for root, _, files in os.walk(directory_path, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    pbar.update(1)
                os.rmdir(root)
        print(f"Successfully deleted directory: {directory_path}")
    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
    except PermissionError:
        print(f"Permission denied: {directory_path}")
    except Exception as e:
        print(f"Error occurred while deleting directory: {directory_path}")
        print(str(e))

# Example usage:
directory_to_delete = r"C:\Users\henry\Desktop\Dataset\trimmed"
delete_directory(directory_to_delete)
