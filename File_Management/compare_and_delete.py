"""
Script: compare_and_delete.py
Description: Tool for compare and delete
Category: File_Management
"""
#compare and delete files that are not present in two directories using the filenames

import os
from tqdm import tqdm

image_directory = r"C:\Users\henry\Desktop\New folder\1"
txt_directory = r"C:\Users\henry\Desktop\New folder\2"

# Get a list of all image files in the image directory
image_files = [file for file in os.listdir(image_directory) if file.lower().endswith('.jpeg')]

# Count the total number of image files
total_images = len(image_files)

# Initialize the progress bar
with tqdm(total=total_images, desc="Deleting images", unit="image") as pbar:
    # Iterate through the image files and check if there's a corresponding txt file
    for image_file in image_files:
        txt_file = os.path.join(txt_directory, image_file[:-4] + ".txt")  # Replace the image extension with txt

        # If the txt file doesn't exist, delete the image
        if not os.path.exists(txt_file):
            image_path = os.path.join(image_directory, image_file)
            os.remove(image_path)
            pbar.update(1)  # Increment the progress bar
            pbar.set_postfix(deleted=image_file)  # Display the filename being deleted
        else:
            pbar.update(1)  # Increment the progress bar even if the image is not deleted

print("Deletion process completed.")