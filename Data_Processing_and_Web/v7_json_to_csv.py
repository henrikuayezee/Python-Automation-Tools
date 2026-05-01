"""
Script: v7_json_to_csv.py
Description: Tool for v7 json to csv
Category: Data_Processing_and_Web
"""
import json
import pandas as pd
import os
from tqdm import tqdm

# Define the input and output file paths
dir_path = r"C:\Users\Henry\Downloads"
input_file = os.path.join(dir_path, "alegion_id_report_2025-02-28T.json")  # Update with actual filename
output_file = os.path.join(dir_path, "alegion_id_report_2025-02-28T.xlsx")

# Load JSON data
with open(input_file, "r", encoding="utf-8") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error loading JSON: {e}")
        exit()

# Extract relevant data
if "annotator_report" not in data:
    print("Missing 'annotator_report' key in JSON file.")
    exit()

data = data["annotator_report"]

# Check if data is empty
if not data:
    print("No records found in 'annotator_report'.")
    exit()

# Convert JSON to DataFrame
rows = []
for entry in tqdm(data, desc="Processing records"):
    if isinstance(entry, dict):
        rows.append(
            [
                entry.get("active_time", "N/A"),
                entry.get("actor_email", "N/A"),
                entry.get("actor_full_name", "N/A"),
                entry.get("actor_id", "N/A"),
                entry.get("actor_type", "N/A"),
                entry.get("dataset_id", "N/A"),
                entry.get("dataset_name", "N/A"),
                entry.get("dataset_slug", "N/A"),
                entry.get("timestamp", "N/A"),
                entry.get("total_items_annotated", "N/A"),
            ]
        )

# Define column headers
columns = [
    "Active Time", "Actor Email", "Actor Full Name", "Actor ID", "Actor Type", 
    "Dataset ID", "Dataset Name", "Dataset Slug", "Timestamp", "Total Items Annotated"
]

# Check if any rows were processed
if not rows:
    print("No valid records found in 'annotator_report'.")
    exit()

df = pd.DataFrame(rows, columns=columns)

# Save to Excel
df.to_excel(output_file, index=False)

print(f"Conversion completed. File saved to: {output_file}")