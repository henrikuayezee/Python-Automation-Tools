"""
Script: earthrover_group.py
Description: Tool for earthrover group
Category: Project_Specific
"""
import xml.etree.ElementTree as ET
import csv
from tqdm import tqdm
from collections import defaultdict, Counter
import pandas as pd

# Set file path
file_path = r"C:\Users\Henry\Downloads\task_3_dataset_2025_06_05_10_10_54_cvat for images 1.1\annotations.xml"

# Parse XML
tree = ET.parse(file_path)
root = tree.getroot()

# Map image id to job ID
job_map = {}
for seg in root.findall("meta/task/segments/segment"):
    start = int(seg.find("start").text)
    url = seg.find("url").text
    job_id = url.rstrip("/").split("/")[-1]
    job_map[start] = f"job_{job_id}"

rows = []
group_counts = defaultdict(Counter)

# Process each image
images = root.findall("image")
for image in tqdm(images, desc="Processing Annotations"):
    image_id = int(image.get("id"))
    image_name = image.get("name")
    job_name = job_map.get(image_id, "unknown")

    for ann in image:
        label = ann.get("label")
        group_id = ann.get("group_id")
        if group_id is None:
            continue

        if ann.tag == "box":
            coords = f"{ann.get('xtl')},{ann.get('ytl')};{ann.get('xbr')},{ann.get('ybr')}"
        elif ann.tag == "points":
            coords = ann.get("points")
        else:
            continue

        rows.append([job_name, image_name, label, group_id, coords])
        group_counts[job_name][group_id] += 1

# Create Excel workbook with all sheets
excel_path = file_path.replace("annotations.xml", "annotations_summary.xlsx")
with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:
    # Sheet 1: flat annotations
    df_flat = pd.DataFrame(rows, columns=["Job Name", "Image Name", "Class", "Group ID", "Coordinates"])
    df_flat.to_excel(writer, sheet_name="Flat Annotations", index=False)

    # Additional sheets per job
    for job_name, counter in group_counts.items():
        filtered = [(group_id, count) for group_id, count in counter.items() if count != 2]
        if filtered:
            df = pd.DataFrame(filtered, columns=["Group ID", "Count"])
            sheet_name = job_name[:31]
            df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"\nDone. All data saved to: {excel_path}")
