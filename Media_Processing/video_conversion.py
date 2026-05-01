"""
Script: video_conversion.py
Description: Tool for video conversion
Category: Media_Processing
"""
import subprocess
from tqdm import tqdm

input_file = r"E:\DP World Data\Negative Samples Videos\Terminal 3\PAN BERTH63-A08\11_06_2023 18_59_59 (UTC+04_00) (1).mkv"
output_file = r"E:\DP World Data\Negative Samples Videos\Terminal 3\PAN BERTH63-A08\11_06_2023 18_59_59 (UTC+04_00) (1).mp4"

# Get the duration of the input file using ffprobe
ffprobe_cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_file]
duration = float(subprocess.check_output(ffprobe_cmd))

# Create the ffmpeg command
ffmpeg_cmd = ['ffmpeg', '-i', input_file, '-c', 'copy', output_file]

# Execute the ffmpeg command with a progress bar
with tqdm(total=duration, unit='s', unit_scale=True, desc='Converting') as pbar:
    process = subprocess.Popen(ffmpeg_cmd, stderr=subprocess.PIPE)
    for line in process.stderr:
        line = line.decode('utf-8').strip()
        if line.startswith('frame='):
            time_str = line.split('time=')[1].split()[0]
            hours, minutes, seconds = map(float, time_str.split(':'))
            elapsed = 3600 * hours + 60 * minutes + seconds
            pbar.update(elapsed - pbar.n)
    process.wait()

# Check if the conversion was successful
if process.returncode == 0:
    print('Conversion completed successfully.')
else:
    print('Conversion failed.')
