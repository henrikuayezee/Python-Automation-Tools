"""
Script: slack_deepdive.py
Description: Tool for slack deepdive
Category: Data_Processing_and_Web
"""
import os
import json
import re
import pandas as pd
from collections import defaultdict
from tqdm import tqdm

# List of directories containing JSON files
directories = [
    r"C:\Users\henry\Downloads\Compressed\Aya Data Workforce Slack export Jan 1 2024 - Nov 4 2024\ayadata-wfh",
    r"C:\Users\henry\Downloads\Compressed\Aya Data Workforce Slack export Jan 1 2024 - Nov 4 2024\random"
]

# Path to the user info JSON file
user_info_file = r"C:\Users\henry\Downloads\Compressed\Aya Data Workforce Slack export Jan 1 2024 - Nov 4 2024\users.json"

# Phrases to search for in messages
phrases = ["light out", "relocating", "power off", "network challenges", "lights out", "lights are out", "network issues", "internet issues"]

# Regex pattern for case-insensitive matching of phrases
pattern = re.compile(r'\b(?:' + '|'.join(phrases) + r')\b', re.IGNORECASE)

# Load user information into a dictionary {user_id: (real_name, email)}
with open(user_info_file, 'r', encoding='utf-8') as f:
    user_data = json.load(f)
user_id_to_info = {
    user["id"]: (user["profile"].get("real_name", user["name"]), user["profile"].get("email", ""))
    for user in user_data
}

# Dictionary to store counts for each user (using real names)
user_message_counts = defaultdict(int)

# Process each directory
for directory_path in directories:
    # List JSON files in the current directory
    json_files = [f for f in os.listdir(directory_path) if f.endswith(".json")]
    
    # Process each JSON file in the current directory with a progress bar
    for filename in tqdm(json_files, desc=f"Processing files in {directory_path}"):
        file_path = os.path.join(directory_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            # Check if data is a list of messages
            messages = data if isinstance(data, list) else data.get("messages", [])
            
            for message in messages:
                user_id = message.get("user")
                text = message.get("text", "")
                
                # Check if any of the phrases appear in the message
                if user_id and pattern.search(text):
                    # Map user ID to real name and email, or use placeholders if not found
                    user_name, user_email = user_id_to_info.get(user_id, (user_id, ""))
                    user_message_counts[(user_name, user_email)] += 1

# Convert the results to a DataFrame and save to CSV
output_df = pd.DataFrame(
    [(user_name, user_email, count) for (user_name, user_email), count in user_message_counts.items()],
    columns=['User', 'Email', 'Count']
)
output_df.to_csv('user_message_counts.csv', index=False)

print("Message counts with user real names and emails have been saved to user_message_counts.csv")
