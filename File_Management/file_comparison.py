"""
Script: file_comparison.py
Description: Tool for file comparison
Category: File_Management
"""
import json
import os

image_path = r"C:/Users/henry/Desktop/New folder/images"
annotation_path = r"C:/Users/henry/Desktop/New folder/labels"

os.chdir(image_path)
images = os.listdir()
annotations = os.listdir(annotation_path)

# print(len(images) - len(annotations))
for item in images:
    if item.replace("jpeg","txt") not in annotations:
        os.remove(item)
        # print(item)