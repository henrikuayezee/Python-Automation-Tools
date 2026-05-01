"""
Script: yolo_outofbound.py
Description: Tool for yolo outofbound
Category: Computer_Vision_Datasets
"""
import os

# Define the input and output file paths
input_dir = r"C:\Users\henry\Downloads\Compressed\new_dir-20230411T102958Z-001\new_dir\labels\output"
output_path = r"C:\Users\henry\Desktop\out of bounds.txt"

# Define the list of labels to ignore (e.g. "person")
ignore_labels = ["0, 1, 2, 3, 4"]

# Initialize a list to store the names of labels that are out of range
out_of_range_labels = []

# Loop through each YOLO txt file in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith(".txt"):
        with open(os.path.join(input_dir, file_name), "r") as f:
            lines = f.readlines()
            for line in lines:
                # Extract the label name and coordinates from the line
                label, x, y, w, h = line.strip().split(" ")
                
                # Ignore labels that are in the ignore list
                if label in ignore_labels:
                    continue
                
                # Check if the label coordinates are out of range
                if float(x) < 0 or float(x) > 1 or float(y) < 0 or float(y) > 1 or float(w) < 0 or float(w) > 1 or float(h) < 0 or float(h) > 1:
                    # Add the label name to the out of range list
                    out_of_range_labels.append(file_name)

# Remove duplicate labels from the out of range list
out_of_range_labels = list(set(out_of_range_labels))

# Write the out of range labels to the output file
with open(output_path, "w") as f:
    for label in out_of_range_labels:
        f.write(label + "\n")
