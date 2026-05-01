"""
Script: excel_report.py
Description: Tool for excel report
Category: Data_Processing_and_Web
"""
import os
import csv

# Set the directory path containing CSV files
csv_directory = r"C:\Users\Henry\Downloads\New folder"

# Set the output file path and name
output_file = r"C:\Users\Henry\Downloads\New folder\output.csv"

# Initialize an empty list to hold all the data
all_data = []

# Loop through all the files in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        # Open each CSV file
        with open(os.path.join(csv_directory, filename), 'r') as csv_file:
            # Read the data from the CSV file
            csv_reader = csv.reader(csv_file)
            data = [row for row in csv_reader]
            # Add the data to the list
            all_data.extend(data)

# Write the data to the output file
with open(output_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(all_data)
