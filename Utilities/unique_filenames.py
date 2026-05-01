"""
Script: unique_filenames.py
Description: Tool for unique filenames
Category: Utilities
"""
import os

directory = r"C:\Users\henry\Desktop\Dataset\output" 
unique_filenames = set()

for filename in os.listdir(directory):
    if '_' in filename:
        unique_filenames.add(filename.split('_')[0])

with open('output.txt', 'w') as file:
    for filename in unique_filenames:
        file.write(filename + '\n')

