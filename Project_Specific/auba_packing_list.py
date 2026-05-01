"""
Script: auba_packing_list.py
Description: Tool for auba packing list
Category: Project_Specific
"""
import pandas as pd
import json
from tqdm import tqdm

# Load the Excel file
excel_file = r
df = pd.read_excel(excel_file)

# Extract the relevant columns by their index positions (D is 3rd index, L is 11th index)
descriptions = df.iloc[:, 4]  # Column D
quantities = df.iloc[:, 12]   # Column L

# Define the constant values
weight_unit_of_measure = "KG"
invoice_number = "ML0001"

# Create a list to hold the JSON data
json_data = []

# Iterate over the rows and create the JSON objects with a progress bar
for desc, qty in tqdm(zip(descriptions, quantities), total=len(descriptions), desc="Processing rows"):
    item = {
        "description": str(desc),
        "quantity": str(qty),
        "weightUnitOfMeasure": weight_unit_of_measure,
        "invoiceNumber": invoice_number
    }
    json_data.append(item)

# Save the list of dictionaries to a JSON file
json_file = 'bfc799f7-431d-4e79-8c54-02f8bc68ee00.json'
with open(json_file, 'w') as file:
    json.dump(json_data, file, indent=4)

print(f'JSON data has been written to {json_file}')
