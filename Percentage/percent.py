import json
import numpy as np
import cv2
import os
from tqdm import tqdm

# Set directory path where the JSON file is located
dir_path = r"C:\Users\Henry\Desktop\DPW\Percentage"  # Change this to your actual directory
json_filename = "2025-02-09_21-00-44-600751.json"  # Change this if your file has a different name
json_path = os.path.join(dir_path, json_filename)

def calculate_segmentation_percentage(json_path):
    # Check if file exists
    if not os.path.exists(json_path):
        print(f"Error: File '{json_path}' not found in '{dir_path}'.")
        return

    # Load JSON file
    with open(json_path, "r") as f:
        data = json.load(f)

    # Get image dimensions
    width = data["item"]["slots"][0]["width"]
    height = data["item"]["slots"][0]["height"]
    total_pixels = width * height

    # Initialize blank mask
    mask = np.zeros((height, width), dtype=np.uint8)

    # Extract polygon coordinates and draw on mask
    for annotation in tqdm(data["annotations"], desc="Processing Annotations"):
        if "polygon" in annotation:
            for path in annotation["polygon"]["paths"]:
                polygon = np.array([[int(point["x"]), int(point["y"])] for point in path], np.int32)
                polygon = polygon.reshape((-1, 1, 2))  # Reshape for OpenCV
                cv2.fillPoly(mask, [polygon], 255)  # Fill the polygon on the mask

    # Calculate segmented area
    segmented_area = np.sum(mask == 255)

    # Compute segmentation percentage
    segmentation_percentage = (segmented_area / total_pixels) * 100

    print(f"Segmented Area: {segmented_area} pixels")
    print(f"Total Image Area: {total_pixels} pixels")
    print(f"Segmentation Percentage: {segmentation_percentage:.2f}%")

# Run the function with the specified JSON file
calculate_segmentation_percentage(json_path)
