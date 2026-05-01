"""
Script: second.py
Description: Tool for second
Category: Computer_Vision_Datasets
"""
import cv2

def get_video_fps(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the frames per second (FPS)
    fps = video.get(cv2.CAP_PROP_FPS)

    # Release the video file
    video.release()

    return fps

# Example usage
video_path = r"C:\Users\henry\Desktop\Negative Samples\Terminal 1\Camera T1 11Q-HM023\Terminal 1_Camera T1 11Q-HM023_0515 Hrs to 0600 Hrs.mkv"
fps = get_video_fps(video_path)
print("Frames per second:", fps)
