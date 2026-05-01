"""
Script: auba_review_time.py
Description: Tool for auba review time
Category: Project_Specific
"""
import pandas as pd
from datetime import datetime, timedelta
from tqdm import tqdm

# Set your Excel file path
file_path = r"C:\Users\Henry\Downloads\Book1.xlsx"

# Load Excel sheet
df = pd.read_excel(file_path)

# Make sure the time columns are in datetime format
df['Labeling Start Time'] = pd.to_datetime(df['Labeling Start Time'], format="%H:%M:%S").dt.time
df['Labeling End Time'] = pd.to_datetime(df['Labeling End Time'], format="%H:%M:%S").dt.time

# Initialize lists for review times
review_starts = []
review_ends = []

# Process each row with a progress bar
for _, row in tqdm(df.iterrows(), total=len(df), desc="Calculating review times"):
    start = datetime.combine(datetime.today(), row['Labeling Start Time'])
    end = datetime.combine(datetime.today(), row['Labeling End Time'])

    annotation_duration = end - start
    review_duration = annotation_duration * 0.15

    review_start = end
    review_end = end + review_duration

    # Format to HH:MM:SS
    review_starts.append(review_start.strftime("%H:%M:%S"))
    review_ends.append(review_end.strftime("%H:%M:%S"))

# Append to DataFrame
df['Review Start Time'] = review_starts
df['Review End Time'] = review_ends

# Save back to Excel
output_path = r"C:\Users\Henry\Downloads\labeling_data_with_reviews.xlsx"
df.to_excel(output_path, index=False)

print(f"✅ Done! Saved to {output_path}")
