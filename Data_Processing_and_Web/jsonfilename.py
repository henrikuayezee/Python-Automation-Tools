"""
Script: jsonfilename.py
Description: Tool for jsonfilename
Category: Data_Processing_and_Web
"""
#this script will make the name of a json file within the file the same as the filename itself

import os
import json
from tqdm import tqdm

# Set the directory path where your JSON files are stored
dir_path = r"C:\Users\henry\Downloads\Compressed\312-grid-json"

# Get the total number of JSON files in the directory
total_files = len([filename for filename in os.listdir(dir_path) if filename.endswith(".json")])

# Loop through each file in the directory with a progress bar
for filename in tqdm(os.listdir(dir_path), total=total_files, desc="Processing JSON files"):
    # Check if the file is a JSON file
    if filename.endswith(".json"):
        # Open the file and load the JSON data
        with open(os.path.join(dir_path, filename)) as f:
            data = json.load(f)
        # Get the base filename without the extension
        base_filename = os.path.splitext(filename)[0]
        # Replace the "name" and "file_name" fields with the name of the file itself
        data["item"]["name"] = base_filename + os.path.splitext(data["item"]["name"])[1]
        data["item"]["slots"][0]["source_files"][0]["file_name"] = base_filename + os.path.splitext(data["item"]["slots"][0]["source_files"][0]["file_name"])[1]
        # Write the updated JSON data back to the file
        with open(os.path.join(dir_path, filename), "w") as f:
            json.dump(data, f, indent=4)

