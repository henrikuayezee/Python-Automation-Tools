"""
Script: earthrover_final.py
Description: Tool for earthrover final
Category: Project_Specific
"""
import xml.etree.ElementTree as ET
import pandas as pd
from tqdm import tqdm
from collections import defaultdict, Counter
import os
import cv2
from pathlib import Path
from tkinter import Tk, filedialog

# === UI Selectors ===
def pick_file(title="Select File"):
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(title=title, filetypes=[("XML files", "*.xml")])

def pick_folder(title="Select Folder"):
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title=title)

# === Step 1: Get paths via UI ===
print("Select the annotations.xml file")
file_path = pick_file("Select annotations.xml")

print("Select the directory containing original images")
image_dir = pick_folder("Select image folder")

print("Select the output directory for visualized images")
output_dir = pick_folder("Select output folder")
os.makedirs(output_dir, exist_ok=True)

# === Step 2: Parse XML and prepare Excel summary ===
tree = ET.parse(file_path)
root = tree.getroot()

job_map = {}
for seg in root.findall("meta/task/segments/segment"):
    start = int(seg.find("start").text)
    url = seg.find("url").text
    job_id = url.rstrip("/").split("/")[-1]
    job_map[start] = f"job_{job_id}"

rows = []
group_counts = defaultdict(Counter)
images = root.findall("image")

for image in tqdm(images, desc="Parsing annotations"):
    image_id = int(image.get("id"))
    image_name = image.get("name")
    job_name = job_map.get(image_id, "unknown")

    for ann in image:
        label = ann.get("label")
        group_id = ann.get("group_id")
        group_id_display = group_id if group_id is not None else "No Group"

        if ann.tag == "box":
            coords = f"{ann.get('xtl')},{ann.get('ytl')};{ann.get('xbr')},{ann.get('ybr')}"
        elif ann.tag == "points":
            coords = ann.get("points")
        else:
            continue

        rows.append([job_name, image_name, label, group_id_display, coords])
        if group_id is not None:
            group_counts[job_name][group_id] += 1

# Write summary to Excel
excel_path = Path(file_path).with_name("annotations_summary.xlsx")
with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:
    df_flat = pd.DataFrame(rows, columns=["Job Name", "Image Name", "Class", "Group ID", "Coordinates"])
    df_flat.to_excel(writer, sheet_name="Flat Annotations", index=False)

    for job_name, counter in group_counts.items():
        filtered = [(group_id, count) for group_id, count in counter.items() if count != 2]
        if filtered:
            df = pd.DataFrame(filtered, columns=["Group ID", "Count"])
            df.to_excel(writer, sheet_name=job_name[:31], index=False)

print(f"\nExcel summary saved to: {excel_path}")

# === Step 3: Draw anomaly and ungrouped visualizations ===
xls = pd.ExcelFile(excel_path)
flat_df = pd.read_excel(xls, sheet_name="Flat Annotations")
job_names = [s for s in xls.sheet_names if s != "Flat Annotations"]

ungrouped_df = flat_df[flat_df["Group ID"] == "No Group"]

for job in tqdm(job_names, desc="Processing Jobs"):
    anomalies_df = pd.read_excel(xls, sheet_name=job)
    group_ids = set(str(gid) for gid in anomalies_df["Group ID"].astype(str))

    job_df = flat_df[flat_df["Job Name"] == job]
    job_df = job_df[job_df["Group ID"].astype(str).isin(group_ids)]
    job_df = pd.concat([job_df, ungrouped_df[ungrouped_df["Job Name"] == job]])

    if job_df.empty:
        continue

    for image_name, group in job_df.groupby("Image Name"):
        image_file_name = image_name.split("/")[-1]
        image_path = Path(image_dir) / image_file_name

        if not image_path.exists():
            print(f"Image not found: {image_path}")
            continue

        img = cv2.imread(str(image_path))
        if img is None:
            print(f"Cannot read image: {image_path}")
            continue

        for _, row in group.iterrows():
            coords = row["Coordinates"]
            group_id = str(row["Group ID"])
            has_group = group_id != "No Group"

            # Color coding
            box_color = (0, 255, 0) if has_group else (255, 255, 255)     # Green or white
            point_color = (255, 0, 0) if has_group else (255, 255, 255)   # Blue or white
            text = group_id if has_group else None

            if ";" in coords:
                try:
                    (xtl, ytl), (xbr, ybr) = [tuple(map(lambda v: round(float(v)), point.split(","))) for point in coords.split(";")]
                    cv2.rectangle(img, (xtl, ytl), (xbr, ybr), box_color, 2)
                    if text:
                        cv2.putText(img, text, (xtl, max(ytl - 10, 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)
                except Exception as e:
                    print(f"Box parsing error: {coords}, error: {e}")
            else:
                try:
                    points = [tuple(map(lambda v: round(float(v)), pt.split(","))) for pt in coords.split(";")]
                    for (x, y) in points:
                        cv2.circle(img, (x, y), 5, point_color, -1)
                    if text:
                        x0, y0 = points[0]
                        cv2.putText(img, text, (x0 + 5, max(y0 - 5, 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, point_color, 2)
                except Exception as e:
                    print(f"Points parsing error: {coords}, error: {e}")

        out_name = f"{job}_{image_file_name}"
        out_path = Path(output_dir) / out_name
        cv2.imwrite(str(out_path), img)

print(f"\n✅ Done. Visualizations saved in: {output_dir}")
