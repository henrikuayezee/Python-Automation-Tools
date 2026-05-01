"""
Script: video_compression.py
Description: Tool for video compression
Category: Computer_Vision_Datasets
"""
import cv2
from tqdm import tqdm

def compress_video(input_file, output_file, quality):
    """Compresses a video file.

    Args:
      input_file: The path to the input video file.
      output_file: The path to the output video file.
      quality: The desired compression quality as a percentage (0-100).
    """

    # Open the input video file.
    input_video = cv2.VideoCapture(input_file)

    # Get the video dimensions.
    width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a VideoWriter object to write the compressed video.
    output_video = cv2.VideoWriter(
        output_file, cv2.VideoWriter_fourcc(*'mp4v'), input_video.get(cv2.CAP_PROP_FPS), (width, height))

    # Write the video frames to the output file.
    total_frames = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))
    with tqdm(total=total_frames, unit='frame', desc='Compressing') as pbar:
        while True:
            ret, frame = input_video.read()
            if not ret:
                break
            output_video.write(frame)
            pbar.update(1)

    # Close the input and output video files.
    input_video.release()
    output_video.release()

if __name__ == "__main__":
    # Get the input and output file paths from the user.
    input_file = r"C:\Users\henry\Videos\2023_05_11_alegion-workflow-velour_CamTop2_000-003-001.mp4"
    output_file = r"C:\Users\henry\Videos\compressed_video.mp4"

    # Get the desired compression quality from the user.
    quality = int(input("Enter the desired compression quality (0-100): "))

    # Compress the video.
    compress_video(input_file, output_file, quality)

    print("Video compressed successfully!")
