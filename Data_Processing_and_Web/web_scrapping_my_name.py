"""
Script: web_scrapping_my_name.py
Description: Tool for web scrapping my name
Category: Data_Processing_and_Web
"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com'  # replace with desired URL to scrape
search_term = 'Henry Kwei Quaye'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all instances of the search term in the HTML code
matches = soup.find_all(string=lambda text: search_term in str(text))

# Print the matches found
print(f'Total matches found: {len(matches)}\n')
for match in matches:
    print(match.strip())
