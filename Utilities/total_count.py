"""
Script: total_count.py
Description: Tool for total count
Category: Utilities
"""
import os

def count_images(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # Add more extensions if needed
    count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension.lower() in image_extensions:
                count += 1

    return count

# Provide the directory path to count images
directory_path = r"E:\DP World Data\Negative Sample Images"

# Call the function
image_count = count_images(directory_path)

print(f"Total count of images: {image_count}")
