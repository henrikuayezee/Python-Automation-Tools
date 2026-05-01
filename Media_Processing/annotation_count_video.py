"""
Script: annotation_count_video.py
Description: Tool for annotation count video
Category: Media_Processing
"""
import json
import os
import csv
from tqdm import tqdm  # Progress bar support

# Define the directory containing JSON files
dir_path = r"C:\Users\Henry\Downloads\3ea04d2aclip.mp4"
output_csv = os.path.join(dir_path, "annotation_counts2.csv")

# Load the JSON file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Count annotations and provide details
def count_annotations(data):
    count = 0
    frame_counts = {}
    
    # Use tqdm for progress indication
    for annotation in tqdm(data.get("annotations", []), desc="Counting Annotations"):
        count += 1  # Each annotation entry represents one individual annotation
        
        # Count per frame
        for frame, details in annotation.get("frames", {}).items():
            frame_counts[frame] = frame_counts.get(frame, 0) + 1
    
    return count, frame_counts

# Process all JSON files and save results to CSV
def process_json_files(directory, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Filename", "Frame", "Annotation Count"])
        
        for filename in tqdm(os.listdir(directory), desc="Processing Files"):
            if filename.endswith(".json"):
                file_path = os.path.join(directory, filename)
                data = load_json(file_path)
                total_annotations, frame_counts = count_annotations(data)
                
                for frame, count in frame_counts.items():
                    csv_writer.writerow([filename, frame, count])
    
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    process_json_files(dir_path, output_csv)