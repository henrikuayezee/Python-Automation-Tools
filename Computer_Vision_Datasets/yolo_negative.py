"""
Script: yolo_negative.py
Description: Tool for yolo negative
Category: Computer_Vision_Datasets
"""
import os

def detect_negative(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                try:
                    if float(word) < 0:
                        return True
                except ValueError:
                    pass
    return False

# Example usage
dir_path = r"C:\Users\henry\Downloads\Compressed\new_dir-20230411T102958Z-001\new_dir\labels\output"
for filename in os.listdir(dir_path):
    file_path = os.path.join(dir_path, filename)
    if os.path.isfile(file_path) and detect_negative(file_path):
        print(f"File {filename} contains negative values")
