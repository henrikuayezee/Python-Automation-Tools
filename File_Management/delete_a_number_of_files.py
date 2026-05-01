"""
Script: delete_a_number_of_files.py
Description: Tool for delete a number of files
Category: File_Management
"""
import os
import random

def delete_random_files(directory, num_files):
    file_list = os.listdir(directory)

    if len(file_list) <= num_files:
        print(f"The directory contains fewer than {num_files} files. Cannot delete.")
        return

    random_files = random.sample(file_list, num_files)

    for file_name in random_files:
        file_path = os.path.join(directory, file_name)
        os.remove(file_path)
        print(f"Deleted file: {file_path}")

# Specify the directory path and number of files to delete
directory_path = r"E:\DP World Data\Negative Sample Images\Terminal 3\PAN BERTH61-A04\Terminal 3_PAN BERTH61-A04_2300 Hrs To 2330 Hrs. (3)"
num_files_to_delete = 60

delete_random_files(directory_path, num_files_to_delete)
