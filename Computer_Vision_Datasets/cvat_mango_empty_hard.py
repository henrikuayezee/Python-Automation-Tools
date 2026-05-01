"""
Script: cvat_mango_empty_hard.py
Description: Tool for cvat mango empty hard
Category: Computer_Vision_Datasets
"""
import json
from tqdm import tqdm

# Specify the path to your COCO JSON file
coco_file_path = r"C:\Users\henry\Downloads\task_mango annotation_annotations_2024_05_20_11_43_01_coco 1.0\annotations\instances_default.json"

# Load the COCO JSON file
with open(coco_file_path) as f:
    coco_data = json.load(f)

# Initialize sets for storing image IDs
images_with_annotations = set()
images_with_hard_annotations = set()

# Iterate through annotations to populate sets
for annotation in tqdm(coco_data['annotations'], desc="Processing annotations"):
    image_id = annotation['image_id']
    if 'bbox' in annotation and annotation['bbox']:  # Check if 'bbox' exists and is not empty
        images_with_annotations.add(image_id)
    if 'attributes' in annotation and 'Difficulty' in annotation['attributes'] and annotation['attributes']['Difficulty'] == 'Hard':
        images_with_hard_annotations.add(image_id)

# Get all image IDs
all_image_ids = {image['id'] for image in coco_data['images']}

# Image IDs with no annotations
images_with_no_annotations = all_image_ids - images_with_annotations

# Convert sets to sorted lists for better readability
images_with_no_annotations = sorted(images_with_no_annotations)
images_with_hard_annotations = sorted(images_with_hard_annotations)

# Print the results
print("Image IDs with no annotations:")
print(images_with_no_annotations)

print("\nImage IDs with 'hard' attribute:")
print(images_with_hard_annotations)



