"""
Script: copy_from_rows_to_txt.py
Description: Tool for copy from rows to txt
Category: File_Management
"""
import pandas as pd
import os

# Define the path of the Excel file
excel_file_path = r"C:\Users\henry\Downloads\External - Waves POC - Aya Data.xlsx"

# Read the Excel file into a Pandas dataframe
df = pd.read_excel(excel_file_path)

# Create the output folder if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Loop through each row in the dataframe
for index, row in df.iterrows():
    # Get the relevant data from the current row
    try:
        artist_id = str(row['artistId'])
        artist_page = str(row['artist page'])
        artist_name = str(row['artistName'])
        popularity = str(row['popularityWW'])
        num_releases = str(row['numReleases'])
    except KeyError:
        print(f"Error: one or more columns not found in Excel file.")
        break
    
    # Define the filename for the output text file
    output_file_path = f"output/{index}.txt"
    
    # Write the data to the output text file
    with open(output_file_path, 'w') as output_file:
        output_file.write(f"artistId: {artist_id}\n")
        output_file.write(f"artist page: {artist_page}\n")
        output_file.write(f"artistName: {artist_name}\n")
        output_file.write(f"popularityWW: {popularity}\n")
        output_file.write(f"numReleases: {num_releases}\n")
