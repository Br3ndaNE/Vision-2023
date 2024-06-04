
import os
import xml.etree.ElementTree as ET
import json

def extract_size_and_bndbox(element):
    size = {}
    bndbox = {}
    for child in element:
        if child.tag == 'size':
            size = {subchild.tag: subchild.text for subchild in child}
        elif child.tag == 'object':
            for subchild in child:
                if subchild.tag == 'bndbox':
                    bndbox = {subsubchild.tag: subsubchild.text for subsubchild in subchild}
    return {'size': size, 'bndbox': bndbox}

def xml_to_json(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return extract_size_and_bndbox(root)

def convert_directory_to_json(xml_dir, output_json_file):
    data = {}
    for filename in os.listdir(xml_dir):
        if filename.endswith('.xml'):
            file_path = os.path.join(xml_dir, filename)
            key = os.path.splitext(filename)[0]
            data[key] = xml_to_json(file_path)
    
    with open(output_json_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage:
xml_directory = 'DatasetCarPlates/annotations/'
output_json_file = 'DatasetCarPlates/labels.json'
convert_directory_to_json(xml_directory, output_json_file)
