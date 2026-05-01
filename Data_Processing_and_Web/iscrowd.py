"""
Script: iscrowd.py
Description: Tool for iscrowd
Category: Data_Processing_and_Web
"""
import json

# Replace filename.json with the name of your JSON file
with open('output.json') as f:
    data = json.load(f)

count = 0
for annotation in data['annotations']:
    if annotation['iscrowd'] == 1:
        count += 1

print('The number of times "iscrowd": 1 appears in the file is:', count)
