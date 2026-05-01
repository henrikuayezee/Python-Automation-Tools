"""
Script: xml2csv.py
Description: Tool for xml2csv
Category: Data_Processing_and_Web
"""
import xmltodict
import csv

with open('1769.xml', 'r') as xml_file:
    xml_data = xml_file.read()

data_dict = xmltodict.parse(xml_data)
annotations = data_dict['root']['annotations']['element']
csv_data = []

for element in annotations:
    name = element['name']
    element_id = element['id']
    try:
        text = element['frames']['0']['text']['text']
    except KeyError:
        text = ''
    csv_data.append([name, element_id, text])

with open('file.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'ID', 'Text'])
    writer.writerows(csv_data)
