"""
Script: telescope_url_to_txt.py
Description: Tool for telescope url to txt
Category: Data_Processing_and_Web
"""
import pandas as pd
import os

def write_urls_to_text_files(excel_file, output_directory):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)
    
    # Extract the URLs from the 'addressUrl' column
    urls = df['AddressUrl']
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Write each URL to a separate text file
    for i, url in enumerate(urls, start=1):
        # Generate a unique file name
        file_name = f"url_{i}.txt"
        
        # Build the full file path
        file_path = os.path.join(output_directory, file_name)
        
        # Write the URL to the text file
        with open(file_path, 'w') as file:
            file.write(str(url))

# Example usage
excel_file = r"C:\Users\henry\Downloads\newgames.xlsx"
output_directory = r"C:\Users\henry\Desktop\Telescopev2"

write_urls_to_text_files(excel_file, output_directory)






