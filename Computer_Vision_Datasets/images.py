"""
Script: images.py
Description: Tool for images
Category: Computer_Vision_Datasets
"""
#check export files against images and delete images that do not have corresponding json/yolo files

import json
import os
from tqdm import tqdm

image_path = r"C:\Users\henry\Desktop\Smoke and Fire\Training\images"
annotation_path = r"C:\Users\henry\Desktop\Smoke and Fire\Training\labels"

os.chdir(image_path)
images = os.listdir()
annotations = os.listdir(annotation_path)

for item in tqdm(images):
    if item.replace("jpeg","txt") not in annotations:
        os.remove(item)
