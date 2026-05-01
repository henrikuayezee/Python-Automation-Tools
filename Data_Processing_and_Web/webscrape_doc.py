"""
Script: webscrape_doc.py
Description: Tool for webscrape doc
Category: Data_Processing_and_Web
"""
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urljoin

# Define the target website
base_url = "https://www.washoecounty.gov/humanresources/files/hrfiles/"  # Change this to your target site
download_folder = r"C:\Users\henry\Desktop\Scraped_Documents"

# Create download folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

def get_document_links(url):
    """Scrapes the webpage for document links (PDF, DOCX)."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to access {url}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.endswith((".pdf", ".docx")):
            full_url = urljoin(url, href)
            links.append(full_url)
    
    return links

def download_file(url):
    """Downloads and saves the document file."""
    local_filename = os.path.join(download_folder, url.split("/")[-1])
    headers = {"User-Agent": "Mozilla/5.0"}

    with requests.get(url, headers=headers, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        with open(local_filename, "wb") as f, tqdm(
            desc=local_filename, total=total_size, unit="B", unit_scale=True
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                bar.update(len(chunk))

    print(f"Downloaded: {local_filename}")

# Main script
if __name__ == "__main__":
    print(f"Scraping {base_url} for documents...")
    doc_links = get_document_links(base_url)

    if not doc_links:
        print("No documents found.")
    else:
        print(f"Found {len(doc_links)} documents. Downloading...")
        for doc_url in doc_links:
            try:
                download_file(doc_url)
            except Exception as e:
                print(f"Error downloading {doc_url}: {e}")
