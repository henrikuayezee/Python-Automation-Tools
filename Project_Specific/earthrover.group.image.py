"""
Script: earthrover.group.image.py
Description: Tool for earthrover.group.image
Category: Project_Specific
"""
import pandas as pd
import cv2
import os
from pathlib import Path
from tqdm import tqdm

# Set paths
excel_path = r"C:\Users\Henry\Downloads\task_3_dataset_2025_06_05_10_10_54_cvat for images 1.1\annotations_summary.xlsx"
image_dir = r"C:\Users\Henry\Downloads\task_3_dataset_2025_06_05_10_10_54_cvat for images 1.1\images\weeder\meristem_retraining_2025\pollybell_Everton_v2"
output_dir = r"C:\Users\Henry\Downloads\task_3_dataset_2025_06_05_10_10_54_cvat for images 1.1\pollybell_Everton_v2"

# Create output folder
os.makedirs(output_dir, exist_ok=True)

# Load workbook
xls = pd.ExcelFile(excel_path)

# Load flat annotation table
flat_df = pd.read_excel(xls, sheet_name="Flat Annotations")

# Group annotations by job
job_names = [sheet for sheet in xls.sheet_names if sheet != "Flat Annotations"]

for job in tqdm(job_names, desc="Processing Jobs"):
    # Load anomaly group IDs for this job
    anomalies_df = pd.read_excel(xls, sheet_name=job)
    group_ids = set(str(gid) for gid in anomalies_df["Group ID"].astype(str))

    # Filter relevant rows from flat annotations
    job_df = flat_df[flat_df["Job Name"] == job]
    job_df = job_df[job_df["Group ID"].astype(str).isin(group_ids)]

    if job_df.empty:
        continue

    # Process each image
    for image_name, group in job_df.groupby("Image Name"):
        image_file_name = image_name.split("/")[-1]
        image_path = Path(image_dir) / image_file_name

        if not image_path.exists():
            print(f"Image not found: {image_path}")
            continue

        # Load image
        img = cv2.imread(str(image_path))
        if img is None:
            print(f"Failed to read image: {image_path}")
            continue

        # Draw annotations
        for _, row in group.iterrows():
            coords = row["Coordinates"]
            group_id = str(row["Group ID"])

            if ";" in coords:  # box
                try:
                    (xtl, ytl), (xbr, ybr) = [tuple(map(lambda v: round(float(v)), point.split(","))) for point in coords.split(";")]
                    cv2.rectangle(img, (xtl, ytl), (xbr, ybr), (0, 255, 0), 2)
                    cv2.putText(img, f"Group {group_id}", (xtl, ytl - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                except Exception as e:
                    print(f"Error parsing box coordinates: {coords}, error: {e}")
            else:  # points
                try:
                    points = [tuple(map(lambda v: round(float(v)), pt.split(","))) for pt in coords.split(";")]
                    for (x, y) in points:
                        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
                    x0, y0 = points[0]
                    cv2.putText(img, f"Group {group_id}", (x0 + 5, y0 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
                except Exception as e:
                    print(f"Error parsing points coordinates: {coords}, error: {e}")

        # Save output image
        out_name = f"{job}_{image_file_name}"
        out_path = Path(output_dir) / out_name
        cv2.imwrite(str(out_path), img)

print(f"\nAll done. Visualized images saved to: {output_dir}")
