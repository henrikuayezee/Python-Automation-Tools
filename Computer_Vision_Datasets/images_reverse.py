"""
Script: images_reverse.py
Description: Tool for images reverse
Category: Computer_Vision_Datasets
"""
#This will delete labels that do not have corresponding images

import os
from tqdm import tqdm

txt_dir = r"C:\Users\henry\Desktop\Dataset\trimmed"
img_dir = r"C:\Users\henry\Desktop\Dataset\images"
# Get list of image file names
img_files = [os.path.splitext(f)[0] for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]

# Loop through txt files and delete if corresponding image file doesn't exist
for f in tqdm(os.listdir(txt_dir)):
    if os.path.splitext(f)[0] not in img_files:
        os.remove(os.path.join(txt_dir, f))
        print(f"Deleted {os.path.join(txt_dir, f)}")

