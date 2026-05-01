"""
Script: deeper_insight.py
Description: Tool for deeper insight
Category: Data_Processing_and_Web
"""
from json import load
import requests
import pandas as pd
from tqdm import tqdm  # Import tqdm library for the progress bar

def readJson(file_path: str):
    with open(file_path, 'r') as f:
        return load(f)

def getText(url: str):
    response = requests.get(url)
    return response.text

data = readJson("./kili-label-export-Deeper_Insight_Training_Dataset_2-2023-07-09_12-23.json")

output = []

# Use tqdm to create a progress bar
for item in tqdm(data, desc="Processing data", unit="item"):
    text = getText(item["content"])
    id = item["externalId"].removeprefix("file ").removesuffix(".txt").strip()

    try:
        if len(item["latestLabel"]["jsonResponse"]) == 0:
            print(f"skipped -> {item}")
            mentioned_person = ""
            action_label = ""

            result = {
                "ID": int(id),
                "Text": text,
                "Mentioned_Person": mentioned_person,
                "Label": action_label
            }

            output.append(result)
        else:
            annotations = item["latestLabel"]["jsonResponse"]["NAMED_ENTITIES_RECOGNITION_JOB"]["annotations"]
            for labels in annotations:
                mentioned_person = labels["content"]
                # print(mentioned_person)
                try:
                    action_label = labels["children"]["CLASSIFICATION_JOB"]["categories"][0]["name"]
                except:
                    action_label = ""

                result = {
                    "ID": int(id),
                    "Text": text,
                    "Mentioned_Person": mentioned_person,
                    "Label": action_label
                }

                output.append(result)
                
    except:  
        result = {
            "ID": int(id),
            "Text": text,
            "Mentioned_Person": " ",
            "Label": " "
        }
        output.append(result)

df = pd.DataFrame(output)
df.to_excel(r"C:\Users\henry\Desktop\Deeper Insight Output\xxx2.xlsx")
