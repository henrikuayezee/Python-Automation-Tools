"""
Script: json2yolo.py
Description: Tool for json2yolo
Category: Computer_Vision_Datasets
"""
import os
import json

# Input directory containing Darwin JSON files
input_dir = r"C:\Users\henry\Desktop\Dataset\labels"

# Output directory to save YOLO instance segmentation text files
output_dir = r"C:\Users\henry\Desktop\Dataset\New folder"

# Load class labels
classes = []
with open("classes.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Loop through JSON files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".json"):
        # Load JSON file
        with open(os.path.join(input_dir, filename), "r") as f:
            data = json.load(f)

        # Extract image dimensions
        width = data["image"]["width"]
        height = data["image"]["height"]

        # Create output text file
        output_filename = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(output_dir, output_filename), "w") as f:
            # Loop through annotations
            for annotation in data["annotations"]:
                # Convert annotation coordinates to YOLO format
                x = annotation["x"] + annotation["width"] / 2
                y = annotation["y"] + annotation["height"] / 2
                w = annotation["width"]
                h = annotation["height"]

                # Convert class label to index
                class_index = classes.index(annotation["class"])

                # Write annotation in YOLO format to output text file
                f.write(f"{class_index} {x/width:.6f} {y/height:.6f} {w/width:.6f} {h/height:.6f}\n")



