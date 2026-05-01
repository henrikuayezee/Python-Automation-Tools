"""
Script: yolo_duplicates.py
Description: Tool for yolo duplicates
Category: Computer_Vision_Datasets
"""
import os

directory = r"C:\Users\henry\Downloads\snf-v1"
output_path = r"C:\Users\henry\Desktop\duplicates.txt"

def find_duplicate_lines(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        unique_lines = set(lines)
        if len(lines) != len(unique_lines):
            return True
        else:
            return False

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        if find_duplicate_lines(file_path):
            print(f"{filename} has duplicate lines.")
