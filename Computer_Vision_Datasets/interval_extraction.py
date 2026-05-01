"""
Script: interval_extraction.py
Description: Tool for interval extraction
Category: Computer_Vision_Datasets
"""
#  this works for extracting frames in a fixed interval
import os
import numpy
import cv2
from tqdm import tqdm


def minToMilliseconds(start: str, stop: str):
    start_ms = (
        (int(start.split(":")[0]) * 60 * 1000) + (int(start.split(":")[1]) * 1000))
    stop_ms = ((int(stop.split(":")[0]) * 60 *
               1000) + (int(stop.split(":")[1]) * 1000))
    return (start_ms, stop_ms)


def extractFrames(start: str, stop: str, vidPath, dirPath):
    start_time_ms, stop_time_ms = minToMilliseconds(start, stop)

    count = len(os.listdir(dirPath))

    success = True
    cap = cv2.VideoCapture(vidPath)

    while success and cap.get(cv2.CAP_PROP_POS_MSEC) < start_time_ms:
        success, image = cap.read()

    pbar = tqdm(total=(stop_time_ms - start_time_ms))
    while success and cap.get(cv2.CAP_PROP_POS_MSEC) <= stop_time_ms:

        success, image = cap.read()
        if success and count % 9000 == 0:
            cv2.imwrite(f"{dirPath}/Terminal 1_Camera T1 11Q-HM023_0515 Hrs to 0600 Hrs_{str(count).zfill(7)}.jpeg", image)
            pbar.update(int(cap.get(cv2.CAP_PROP_POS_MSEC)) - start_time_ms)
        count += 1
    pbar.close()


def main(videoPath, start: str, stop: str):

    filename = videoPath.split("\\")[-1].removesuffix(".mp4")
    destPath = f"C:\\Users\\henry\\Desktop\\Negative Samples\\Images\\Terminal 1\\Camera T1 11Q-HM023\\Terminal 1_Camera T1 11Q-HM023_0515 Hrs to 0600 Hrs\\{filename}"
    os.makedirs(destPath, exist_ok=True)

    extractFrames(start, stop, videoPath, destPath)


main(r"C:\Users\henry\Desktop\Negative Samples\Videos\Terminal 1\Camera T1 11Q-HM023\Terminal 1_Camera T1 11Q-HM023_0515 Hrs to 0600 Hrs.mkv", "0:00", "45:00")
