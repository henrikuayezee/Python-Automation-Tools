"""
Script: negative_samples.py
Description: Tool for negative samples
Category: Utilities
"""
## This creates am empty txt file for corresponding images

import os
from tqdm import tqdm

def create_text_files(input_directory, output_directory):
    image_files = [filename for filename in os.listdir(input_directory)
                   if filename.endswith((".jpg", ".jpeg", ".png"))]
    
    progress_bar = tqdm(image_files, desc="Creating text files", unit="file")
    
    for filename in progress_bar:
        image_path = os.path.join(input_directory, filename)
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt_filepath = os.path.join(output_directory, txt_filename)
        
        with open(txt_filepath, "w") as file:
            pass  # Creates an empty text file
        
        progress_bar.set_postfix({"Current file": filename})
    
    progress_bar.close()

# Example usage
input_directory_path = r"E:\DP World Data\Negative Images and Labels (Original)\images"    # Replace with your image directory path
output_directory_path = r"E:\DP World Data\Negative Images and Labels (Original)\labels"  # Replace with your label directory path

create_text_files(input_directory_path, output_directory_path)
