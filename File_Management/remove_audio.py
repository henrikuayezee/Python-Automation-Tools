"""
Script: remove_audio.py
Description: Tool for remove audio
Category: File_Management
"""
import os
from moviepy.editor import VideoFileClip
from tqdm import tqdm

# Function to remove audio from a video and save it to the output folder
def remove_audio_from_folder(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get a list of all mp4 files in the input folder
    files = [filename for filename in os.listdir(input_folder) if filename.endswith(".mp4")]
    
    # Use tqdm to create a progress bar
    for filename in tqdm(files, desc="Processing videos"):
        input_video_path = os.path.join(input_folder, filename)
        output_video_path = os.path.join(output_folder, filename)

        # Load the video file
        video = VideoFileClip(input_video_path)
        
        # Remove the audio
        video_without_audio = video.without_audio()
        
        # Write the output video to the output folder
        video_without_audio.write_videofile(output_video_path, codec="libx264")
        
        print(f"Processed: {filename}")

# Example usage
input_folder = r"C:\Users\henry\Downloads\Compressed\archive\vatex\videos"  # Folder containing your input videos
output_folder = r"C:\Users\henry\Downloads\Compressed\archive\vatex\without_audio"  # Folder to save the output videos

remove_audio_from_folder(input_folder, output_folder)
