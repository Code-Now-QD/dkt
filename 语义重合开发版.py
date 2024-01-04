import os
import json
from shapely.geometry import Polygon


def are_polygons_overlapping(poly1, poly2):
    return poly1.intersects(poly2)


def calculate_overlap_percentage(poly1, poly2):
    intersection_area = poly1.intersection(poly2).area
    union_area = poly1.union(poly2).area
    return (intersection_area / union_area) * 100


def process_json_file(json_file):
    with open(json_file, "r") as f:
        json_data = json.load(f)
        shapes = [Polygon(shape["points"]) for shape in json_data.get("shapes", [])]
        num_shapes = len(shapes)

        for i in range(num_shapes):
            for j in range(i + 1, num_shapes):
                overlap = are_polygons_overlapping(shapes[i], shapes[j])
                if overlap:
                    overlap_percentage = calculate_overlap_percentage(shapes[i], shapes[j])
                    print(f'File: {json_file}, Shape {i + 1} and Shape {j + 1} overlap: {overlap_percentage:.2f}%')


def process_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            json_file = os.path.join(directory_path, filename)
            process_json_file(json_file)


# 示例目录路径
directory_path = "/home/dkt/ultralytics/data/1data_set/1123_new_old_gangkou/labels"
process_directory(directory_path)
