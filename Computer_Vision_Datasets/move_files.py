"""
Script: move_files.py
Description: Tool for move files
Category: Computer_Vision_Datasets
"""
import os
from tqdm import tqdm
import shutil

def move_files(source_dir, destination_dir):
    files = os.listdir(source_dir)
    total_files = len(files)
    
    with tqdm(total=total_files, desc="Moving files") as pbar:
        for file in files:
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)
            
            shutil.move(source_path, destination_path)
            pbar.update(1)

# Example usage:
source_directory = r"C:\Users\henry\Downloads\Compressed\JSON2YOLO-20230713T155736Z-001\JSON2YOLO\savefolder\output"
destination_directory = r"C:\Users\henry\Desktop\Dataset\yolo labels"

move_files(source_directory, destination_directory)
