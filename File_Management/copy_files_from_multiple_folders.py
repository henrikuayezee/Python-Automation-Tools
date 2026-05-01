"""
Script: copy_files_from_multiple_folders.py
Description: Tool for copy files from multiple folders
Category: File_Management
"""
import os
import shutil
from tqdm import tqdm

def copy_images(source_dir, dest_dir):
    # Create the destination directory if it doesn't already exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get a list of all image files in the source directory and its subdirectories
    image_files = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                image_files.append(os.path.join(root, file))

    # Copy each image file to the destination directory and display a progress bar
    for file in tqdm(image_files, desc='Copying images'):
        dest_file = os.path.join(dest_dir, os.path.basename(file))
        shutil.copy2(file, dest_file)

if __name__ == '__main__':
    source_dir = r"E:\DP World Data\Negative Sample Images"
    dest_dir = r"E:\DP World Data\Negative Images and Labels (Original)\images"
    copy_images(source_dir, dest_dir)
