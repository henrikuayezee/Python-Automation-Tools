"""
Script: basic_ai_data_download.py
Description: Tool for basic ai data download
Category: Data_Processing_and_Web
"""
import json
import os
import requests
import glob
from tqdm import tqdm

# Function to download a file from a URL and save it to a specific directory, with a progress bar
def download_file(url, save_path):
    # Create the folder structure if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Download the file and save it to the given path
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Raise an error for bad responses
        total_size = int(response.headers.get("content-length", 0))
        
        # Create a tqdm progress bar
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Downloading {os.path.basename(save_path)}") as pbar:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
                    pbar.update(len(chunk))  # Update the progress bar

# Function to process a single JSON file and download the specified data
def process_json(json_file_path, output_directory):
    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Extract LIDAR point clouds data
    lidar_point_clouds = data.get("lidarPointClouds", [])

    # Loop over each LIDAR point cloud and download the associated file
    for lidar in lidar_point_clouds:
        file_url = lidar.get("url")
        filename = lidar.get("filename")
        
        if file_url and filename:
            # Path where the downloaded file will be saved
            save_path = os.path.join(output_directory, filename)
            download_file(file_url, save_path)

# Define the input folder containing JSON files and the output directory for the downloaded data
input_json_folder = r"C:\Users\henry\Downloads\Compressed\29-34\29-34\lidar_point_cloud_0\data"  # Folder containing your JSON files
output_directory = "downloaded_data"  # Output folder to save the data

# Get a list of all JSON files in the specified folder
json_files = glob.glob(os.path.join(input_json_folder, "*.json"))

# Process each JSON file and download the data with progress bars
for json_file_path in json_files:
    process_json(json_file_path, output_directory)
