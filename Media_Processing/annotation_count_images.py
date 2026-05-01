"""
Script: annotation_count_images.py
Description: Tool for annotation count images
Category: Media_Processing
"""
import json
import os
import csv
from tqdm import tqdm  # Progress bar support

# Define the directory containing JSON files
dir_path = r"C:\Users\Henry\Downloads\all"
output_csv = os.path.join(dir_path, "annotation_counts_image_based.csv")

# Load the JSON file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Count annotations for an image (not video frames)
def count_image_annotations(data):
    return len(data.get("annotations", []))

# Process all JSON files and save results to CSV
def process_json_files(directory, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Filename", "Annotation Count"])
        
        for filename in tqdm(os.listdir(directory), desc="Processing Files"):
            if filename.endswith(".json"):
                file_path = os.path.join(directory, filename)
                data = load_json(file_path)
                annotation_count = count_image_annotations(data)
                
                csv_writer.writerow([filename, annotation_count])
    
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    process_json_files(dir_path, output_csv)
