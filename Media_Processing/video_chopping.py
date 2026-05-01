"""
Script: video_chopping.py
Description: Tool for video chopping
Category: Media_Processing
"""
from moviepy.video.io.VideoFileClip import VideoFileClip

# Specify the path of the input video file
input_file_path = "C:/Users/henry/Videos/[Third] Seoul Korea 300+ Live CCTV Cameras -  Music - 서울 라이브 카메라  - ソウルライブカメラ_2.mp4"

# Specify the path where you want to save the output video files
output_folder_path = "C:/Users/henry/Videos/Output"

# Create a video clip object from the input video file
clip = VideoFileClip(input_file_path)

# Get the duration of the video in seconds
video_duration = clip.duration

# Set the duration of each output video to 30 minutes (1800 seconds)
chunk_duration = 1800

# Compute the number of output video files
num_chunks = int(video_duration / chunk_duration) + 1

# Loop through each chunk and save it as a separate video file
for i in range(num_chunks):
    # Compute the start and end time of the current chunk
    start_time = i * chunk_duration
    end_time = min((i + 1) * chunk_duration, video_duration)
    
    # Extract the current chunk from the video clip
    chunk = clip.subclip(start_time, end_time)
    
    # Save the current chunk as a separate video file
    output_file_path = f"{output_folder_path}chunk_{i+1}.mp4"
    chunk.write_videofile(output_file_path)