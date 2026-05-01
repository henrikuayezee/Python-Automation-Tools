"""
Script: cocojson2yolobb.py
Description: Tool for cocojson2yolobb
Category: Computer_Vision_Datasets
"""
import json
import os

def coco_to_yolo(coco_file, output_dir):
    with open(coco_file, 'r') as f:
        coco_data = json.load(f)

    images = coco_data['images']
    annotations = coco_data['annotations']
    categories = coco_data['categories']

    for image in images:
        image_id = image['id']
        file_name = image['file_name']
        width = image['width']
        height = image['height']

        yolo_data = []
        for annotation in annotations:
            if annotation['image_id'] == image_id:
                category_id = annotation['category_id']
                category = next(category for category in categories if category['id'] == category_id)
                class_name = category['name']
                x, y, bbox_width, bbox_height = annotation['bbox']

                # Normalize bounding box coordinates
                x_center = x + bbox_width / 2
                y_center = y + bbox_height / 2
                normalized_x = x_center / width
                normalized_y = y_center / height
                normalized_width = bbox_width / width
                normalized_height = bbox_height / height

                yolo_data.append(f'{class_name} {normalized_x:.6f} {normalized_y:.6f} '
                                 f'{normalized_width:.6f} {normalized_height:.6f}\n')

        output_file = os.path.join(output_dir, os.path.splitext(file_name)[0] + '.txt')
        with open(output_file, 'w') as f:
            f.writelines(yolo_data)

# Example usage
coco_file = r"C:\Users\henry\Downloads\Compressed\PPEdataset\_test.json"
output_dir = r"C:\Users\henry\Downloads\Compressed\PPEdataset\test labels"
coco_to_yolo(coco_file, output_dir)
