"""
Script: image_extraction.py
Description: Tool for image extraction
Category: Computer_Vision_Datasets
"""
#This script will extact frames(images) from a video

import os
import numpy as np
import cv2
import time
import tqdm

raw = r"C:\Users\henry\Videos\Henderson Hall Fire - Newcastle University - Drone Footage 2023_2.mp4"
cleaned = r"C:\Users\henry\Desktop\DPW 5k\Henderson Hall Fire - Newcastle University - Drone Footage 2023_2"
count = 0

cap = cv2.VideoCapture(raw)

success, image = cap.read()

# Get total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Initialize tqdm with the total number of frames
progress_bar = tqdm.tqdm(total=total_frames, desc="Extracting Frames", unit="frame")

while success:
    success, image = cap.read()
    if success and count % 20 == 0:
        cv2.imwrite(f"{cleaned}/Henderson Hall Fire - Newcastle University - Drone Footage 2023_2_{str(count).zfill(7)}.jpeg", image)
    count += 1
    
    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar and release the video capture
progress_bar.close()
cap.release()