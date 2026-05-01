"""
Script: auba_clean_json.py
Description: Tool for auba clean json
Category: Project_Specific
"""
import os
import json

def remove_placeholder_fields(data):
    """Recursively removes fields with placeholder values like 'str', 'bool', 'dict[str, str]', etc."""
    if isinstance(data, dict):
        # Remove key-value pairs where the value is a placeholder or empty
        return {
            key: remove_placeholder_fields(value)
            for key, value in data.items()
            if value not in ["str", "bool", "dict[str, str]", "str, Enum", "float", "int", None]
        }
    elif isinstance(data, list):
        # Process each item in the list
        return [remove_placeholder_fields(item) for item in data if item not in ["str", "bool", "dict[str, str]", "str, Enum", "float", "int", None]]
    
    return data

def process_json_file(input_file_path, output_file_path):
    """Reads a JSON file, processes it, and writes the cleaned version to a new file."""
    try:
        with open(input_file_path, 'r') as input_file:
            data = json.load(input_file)

        cleaned_data = remove_placeholder_fields(data)

        with open(output_file_path, 'w') as output_file:
            json.dump(cleaned_data, output_file, indent=4)
        print(f"Processed {input_file_path} and saved to {output_file_path}")
    
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in {input_file_path}: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred with {input_file_path}: {e}")

def process_json_folder(input_folder, output_folder):
    """Processes all JSON files in the input folder and saves cleaned files to the output folder."""
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.json'):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name)
            process_json_file(input_file_path, output_file_path)

# Example usage
input_folder = r"C:\Users\Henry\Desktop\auba rough"
output_folder = r"C:\Users\Henry\Desktop\auba clean"

process_json_folder(input_folder, output_folder)
