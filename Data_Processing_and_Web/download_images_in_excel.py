"""
Script: download_images_in_excel.py
Description: Tool for download images in excel
Category: Data_Processing_and_Web
"""
import os
import urllib.request
import pandas as pd

# Set input and output file paths
input_file_path = r"C:\Users\henry\Downloads\Adobe Research nsfw_harmful_sample_images.xlsx"
output_folder_path = r"C:\Users\henry\Downloads\New folder"

# Load the Excel file into a DataFrame
df = pd.read_excel(input_file_path)

# Iterate over the rows in the DataFrame
for index, row in df.iterrows():
    # Get the image URL from the current row
    image_url = row['Image URL']
    
    # Generate a filename for the image
    filename = f"{row['Product ID']}.jpg"
    
    # Create the output file path
    output_file_path = os.path.join(output_folder_path, filename)
    
    # Download the image from the URL to the output file path
    urllib.request.urlretrieve(image_url, output_file_path)
    
    print(f"Downloaded {output_file_path}")
