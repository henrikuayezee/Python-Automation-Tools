"""
Script: xml_file.py
Description: Tool for xml file
Category: Computer_Vision_Datasets
"""
import xml.etree.ElementTree as ET

# parse the input XML file
tree = ET.parse(r"C:\Users\henry\Downloads\Compressed\project_smokefire-2022_11_08_10_40_48-cvat for images 1.1\annotations.xml")
root = tree.getroot()

# create a new root element for the output XML file
output_root = ET.Element('output')

# loop through all the <and> elements in the input XML file
for and_element in root.findall('and'):
    # check if the subset attribute of the <and> element is 'train'
    if and_element.get('subset') == 'train':
        # extract the text content of the <and> element
        text_content = and_element.text.strip()
        # create a new <and> element in the output XML file with the same text content
        output_and_element = ET.SubElement(output_root, 'and')
        output_and_element.text = text_content

# create a new tree from the output root element and write it to a file
output_tree = ET.ElementTree(output_root)
output_tree.write('output.xml', encoding='UTF-8', xml_declaration=True)
