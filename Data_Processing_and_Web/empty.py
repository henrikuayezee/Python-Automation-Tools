"""
Script: empty.py
Description: Tool for empty
Category: Data_Processing_and_Web
"""
import pandas as pd
import requests
import os
from urllib.parse import urlparse

# Path of the Excel file to read
excel_path = r"C:\Users\henry\Downloads\Adobe Research nsfw_harmful_sample_images.xlsx"

# Name of the Excel sheet that contains the URLs
sheet_name = 'Profane'

# Column name that contains the URLs
url_column = 'Image URL'

# Path of the output folder to save the images
output_folder = r"C:\Users\henry\Downloads\New folder\Profane"

# Read the Excel file
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# Loop through each row of the DataFrame
for index, row in df.iterrows():
    # Get the URL from the specified column
    url = row[url_column]
    
    # Parse the URL to get the filename of the image
    filename = os.path.basename(urlparse(url).path)
    
    # Send a GET request to the URL to download the image
    response = requests.get(url)
    
    # Save the image in the output folder
    with open(os.path.join(output_folder, filename), 'wb') as f:
        f.write(response.content)
