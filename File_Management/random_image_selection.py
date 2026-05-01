"""
Script: random_image_selection.py
Description: Tool for random image selection
Category: File_Management
"""
import os
import random
import shutil

# Set the directory to copy images from
dir_path = r"C:\Users\henry\Desktop\DPW Assets\v4"

# Set the output directory
output_path =r"C:\Users\henry\Desktop\model sample"

# Set the number of images to copy
num_images = 500

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

# Copy the first num_images images to the output directory
for i in range(num_images):
    image_path = image_paths[i]
    image_filename = os.path.basename(image_path)
    output_image_path = os.path.join(output_path, image_filename)
    shutil.copy2(image_path, output_image_path)
