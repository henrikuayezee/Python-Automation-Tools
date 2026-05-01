"""
Script: dpworld_upload.py
Description: Tool for dpworld upload
Category: Project_Specific
"""
import requests

# SharePoint site URL
site_url = "https://https://dpworld.sharepoint.com/sites/DPWAyadata/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2Fsites%2FDPWAyadata%2FShared%20Documents%2FGeneral%2FPPE%2Ftrain&FolderCTID=0x01200099F4F5264AE40544BE4B6BFB6A435D0D"
# SharePoint list name where the file will be uploaded
list_name = "train"
# Path to the file to upload
file_path = r"C:\Users\henry\Downloads\Compressed\PPEdataset\train\images.zip"

# SharePoint API endpoint for uploading files
upload_url = f"{site_url}/_api/web/lists/getbytitle('{list_name}')/RootFolder/Files/Add(url='{file_path.split('/')[-1]}', overwrite=true)"

# SharePoint credentials
username = "henry.quaye@ayadata.ai"
password = "Henrikuaye1"

# Read the file content
with open(file_path, "rb") as file:
    file_content = file.read()

# Set request headers
headers = {
    "Content-Type": "application/json;odata=verbose",
    "Accept": "application/json;odata=verbose",
}

# Perform the file upload
response = requests.post(upload_url, auth=(username, password), headers=headers, data=file_content)

# Check the response status
if response.status_code == 200:
    print("File uploaded successfully.")
else:
    print(f"An error occurred while uploading the file. Status code: {response.status_code}")
    print(response.text)
