"""
Script: move_files.py
Description: Tool for move files
Category: File_Management
"""
import os
import random
import shutil

# Set the directory to move images from
dir_path = r"C:\Users\henry\Desktop\Negative Samples\Validate\images"

# Set the output directory
output_path = r"C:\Users\henry\Desktop\Negative Samples\Validate\labels"

# Set the number of images to move
num_images = 29

# Create the output directory if it doesn't exist
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Initialize a list to store the paths of all image files in the directory
image_paths = []

# Walk through the directory and its subdirectories to find all image files
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            image_path = os.path.join(root, file)
            image_paths.append(image_path)

# Shuffle the list of image paths randomly
random.shuffle(image_paths)

# Move the first num_images images to the output directory
for i in range(num_images):
    image_path = image_paths[i]
    image_filename = os.path.basename(image_path)
    output_image_path = os.path.join(output_path, image_filename)
    shutil.move(image_path, output_image_path)
