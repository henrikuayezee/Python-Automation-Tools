"""
Script: count_files_and_images.py
Description: Tool for count files and images
Category: Utilities
"""
import os

# specify the directory path
dir_path = r"E:\DP World Data\Negative Sample Images"

# open a file to write the output
with open("folder_count.txt", "w") as f:

    total_images = 0

    # loop through each folder in the directory
    for folder in os.listdir(dir_path):

        # ignore any files that are not folders
        if not os.path.isdir(os.path.join(dir_path, folder)):
            continue

        # count the number of files in the folder
        num_files = len(os.listdir(os.path.join(dir_path, folder)))

        # write the folder name and file count to the output file
        f.write(f"{folder}: {num_files}\n")

        # if the folder contains image files, add the count to the total_images variable
        if any(file.endswith((".jpg", ".jpeg",)) for file in os.listdir(os.path.join(dir_path, folder))):
            total_images += num_files

    # write the total number of images to the output file
    f.write(f"Total images: {total_images}\n")
