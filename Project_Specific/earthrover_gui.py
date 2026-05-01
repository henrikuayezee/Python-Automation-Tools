"""
Script: earthrover_gui.py
Description: Tool for earthrover gui
Category: Project_Specific
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import xml.etree.ElementTree as ET
import pandas as pd
from collections import defaultdict, Counter
import os
import cv2
from pathlib import Path
from tqdm import tqdm

class EarthRoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EarthRover Annotation Visualizer")
        self.root.geometry("600x400")
        self.xml_path = tk.StringVar()
        self.img_dir = tk.StringVar()
        self.out_dir = tk.StringVar()
        self.status = tk.StringVar(value="Ready.")
        self.progress = tk.DoubleVar(value=0)
        self._build_ui()
        self.processing_thread = None

    def _build_ui(self):
        pad = {'padx': 10, 'pady': 5}
        frm = ttk.Frame(self.root)
        frm.pack(fill=tk.BOTH, expand=True)

        # XML file picker
        ttk.Label(frm, text="Annotations XML file:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(frm, textvariable=self.xml_path, width=50).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(frm, text="Browse", command=self.pick_xml).grid(row=0, column=2, padx=10, pady=5)

        # Image folder picker
        ttk.Label(frm, text="Image folder:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(frm, textvariable=self.img_dir, width=50).grid(row=1, column=1, padx=10, pady=5)
        ttk.Button(frm, text="Browse", command=self.pick_img_dir).grid(row=1, column=2, padx=10, pady=5)

        # Output folder picker
        ttk.Label(frm, text="Output folder:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(frm, textvariable=self.out_dir, width=50).grid(row=2, column=1, padx=10, pady=5)
        ttk.Button(frm, text="Browse", command=self.pick_out_dir).grid(row=2, column=2, padx=10, pady=5)

        # Run button
        self.run_btn = ttk.Button(frm, text="Run", command=self.on_run)
        self.run_btn.grid(row=3, column=1, padx=10, pady=20)

        # Progress bar
        self.progressbar = ttk.Progressbar(frm, variable=self.progress, maximum=100)
        self.progressbar.grid(row=4, column=0, columnspan=3, sticky=tk.EW, padx=10, pady=5)

        # Status area
        self.status_label = ttk.Label(frm, textvariable=self.status, foreground="blue")
        self.status_label.grid(row=5, column=0, columnspan=3, sticky=tk.W, padx=10, pady=5)

        frm.columnconfigure(1, weight=1)

    def pick_xml(self):
        path = filedialog.askopenfilename(title="Select annotations.xml", filetypes=[("XML files", "*.xml")])
        if path:
            self.xml_path.set(path)

    def pick_img_dir(self):
        path = filedialog.askdirectory(title="Select image folder")
        if path:
            self.img_dir.set(path)

    def pick_out_dir(self):
        path = filedialog.askdirectory(title="Select output folder")
        if path:
            self.out_dir.set(path)

    def on_run(self):
        if not self.xml_path.get() or not self.img_dir.get() or not self.out_dir.get():
            messagebox.showerror("Missing Input", "Please select all required files and folders.")
            return
        self.run_btn.config(state=tk.DISABLED)
        self.status.set("Processing...")
        self.progress.set(0)
        self.processing_thread = threading.Thread(target=self.process, daemon=True)
        self.processing_thread.start()
        self.root.after(100, self.check_thread)

    def check_thread(self):
        if self.processing_thread is not None and self.processing_thread.is_alive():
            self.root.after(100, self.check_thread)
        else:
            self.run_btn.config(state=tk.NORMAL)

    def process(self):
        try:
            self._process_annotations(
                self.xml_path.get(),
                self.img_dir.get(),
                self.out_dir.get(),
            )
            self.status.set("✅ Done. Visualizations and summary saved.")
        except Exception as e:
            self.status.set(f"❌ Error: {e}")
            messagebox.showerror("Processing Error", str(e))

    def _process_annotations(self, file_path, image_dir, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        tree = ET.parse(file_path)
        root = tree.getroot()

        job_map = {}
        for seg in root.findall("meta/task/segments/segment"):
            start_elem = seg.find("start")
            url_elem = seg.find("url")
            if start_elem is None or url_elem is None or start_elem.text is None or url_elem.text is None:
                continue
            start = int(start_elem.text)
            url = url_elem.text
            job_id = url.rstrip("/").split("/")[-1]
            job_map[start] = f"job_{job_id}"

        rows = []
        group_counts = defaultdict(Counter)
        images = root.findall("image")

        # Progress: 0-30%
        for idx, image in enumerate(images):
            image_id = image.get("id")
            if image_id is None:
                continue
            try:
                image_id = int(image_id)
            except Exception:
                continue
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
            if idx % 10 == 0:
                self.progress.set(30 * idx / max(1, len(images)))

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

        self.progress.set(40)
        # === Step 3: Draw anomaly and ungrouped visualizations ===
        xls = pd.ExcelFile(excel_path)
        flat_df = pd.read_excel(xls, sheet_name="Flat Annotations")
        job_names = [s for s in xls.sheet_names if s != "Flat Annotations"]
        ungrouped_df = flat_df[flat_df["Group ID"] == "No Group"]

        for jidx, job in enumerate(job_names):
            anomalies_df = pd.read_excel(xls, sheet_name=job)
            group_ids = set(str(gid) for gid in anomalies_df["Group ID"].astype(str))

            job_df = flat_df[flat_df["Job Name"] == job]
            job_df = job_df[job_df["Group ID"].astype(str).isin(group_ids)]
            job_df = pd.concat([job_df, ungrouped_df[ungrouped_df["Job Name"] == job]])

            if job_df.empty:
                continue

            for _, group in job_df.groupby("Image Name"):
                image_name = group["Image Name"].iloc[0]
                image_file_name = image_name.split("/")[-1]
                image_path = Path(image_dir) / image_file_name

                if not image_path.exists():
                    self.status.set(f"Image not found: {image_path}")
                    continue

                img = cv2.imread(str(image_path))
                if img is None:
                    self.status.set(f"Cannot read image: {image_path}")
                    continue

                for _, row in group.iterrows():
                    coords = row["Coordinates"]
                    group_id = str(row["Group ID"])
                    has_group = group_id != "No Group"

                    # Color coding
                    box_color = (0, 255, 0) if has_group else (255, 255, 255)     # Green or white
                    point_color = (255, 0, 0) if has_group else (255, 255, 255)   # Blue or white
                    text = group_id if has_group else None

                    if ";" in str(coords):
                        try:
                            (xtl, ytl), (xbr, ybr) = [tuple(map(lambda v: round(float(v)), point.split(","))) for point in str(coords).split(";")]
                            cv2.rectangle(img, (xtl, ytl), (xbr, ybr), box_color, 2)
                            if text:
                                cv2.putText(img, text, (xtl, max(ytl - 10, 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)
                        except Exception as e:
                            self.status.set(f"Box parsing error: {coords}, error: {e}")
                    else:
                        try:
                            points = [tuple(map(lambda v: round(float(v)), pt.split(","))) for pt in str(coords).split(";")]
                            for (x, y) in points:
                                cv2.circle(img, (x, y), 5, point_color, -1)
                            if text:
                                x0, y0 = points[0]
                                cv2.putText(img, text, (x0 + 5, max(y0 - 5, 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, point_color, 2)
                        except Exception as e:
                            self.status.set(f"Points parsing error: {coords}, error: {e}")

                out_name = f"{job}_{image_file_name}"
                out_path = Path(output_dir) / out_name
                cv2.imwrite(str(out_path), img)
            # Progress: 40-100%
            self.progress.set(40 + 60 * (jidx + 1) / max(1, len(job_names)))

        self.status.set(f"✅ Done. Visualizations saved in: {output_dir}\nExcel summary: {excel_path}")
        self.progress.set(100)

if __name__ == "__main__":
    root = tk.Tk()
    app = EarthRoverApp(root)
    root.mainloop() 