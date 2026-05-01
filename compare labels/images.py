import json
import os

image_path = r"C:\Users\henry\Desktop\v1"
annotation_path = r"C:\Users\henry\Downloads\snf-v1"

os.chdir(image_path)
images = os.listdir()
annotations = os.listdir(annotation_path)

# print(len(images) - len(annotations))
for item in images:
    if item.replace("jpeg","txt") not in annotations:
        os.remove(item)
        # print(item)