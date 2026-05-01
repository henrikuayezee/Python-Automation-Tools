"""
Script: auba_packing_list_2.py
Description: Tool for auba packing list 2
Category: Project_Specific
"""
import pandas as pd
import json
from tqdm import tqdm

# Load the CSV file
csv_file = r"C:\Users\Henry\Downloads\df7e915d-0b40-4383-8048-c43f09b6b795.xls - PL (1).csv"
df = pd.read_csv(csv_file)

# Define constants
weight_unit_of_measure = "KGS"
invoice_number = "2407-4470 "

# Create a list to hold the JSON data
json_data = []

# Iterate over the rows and build the JSON structure
for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing rows"):
    item = {
        "quantity": str(row["quantity"]),
        "grossWeight": str(row["grossWeight"]),
        "netWeight": str(row["netWeight"]),
        "weightUnitOfMeasure": weight_unit_of_measure,
        "invoiceNumber": invoice_number,
        "containerNumber": str(row["containerNumber"]),
    }
    json_data.append(item)

# Save to JSON file
json_file = 'df7e915d-0b40-4383-8048-c43f09b6b795.json'
with open(json_file, 'w') as file:
    json.dump(json_data, file, indent=4)

print(f'JSON data has been written to {json_file}')
