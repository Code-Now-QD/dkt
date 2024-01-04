import json
import os

from shapely.geometry import box


def are_rectangles_overlapping(rect1, rect2):
    return rect1.intersects(rect2)


def calculate_overlap_percentage(rect1, rect2):
    intersection_area = rect1.intersection(rect2).area
    union_area = rect1.union(rect2).area
    return (intersection_area / union_area) * 100


def process_json_file(json_file):
    with open(json_file, "r") as f:
        json_data = json.load(f)
        rectangles = [box(rect["points"][0][0], rect["points"][0][1], rect["points"][1][0], rect["points"][1][1]) for rect in
                      json_data.get("shapes", [])]
        num_rectangles = len(rectangles)

        for i in range(num_rectangles):
            for j in range(i + 1, num_rectangles):
                overlap = are_rectangles_overlapping(rectangles[i], rectangles[j])
                if overlap:
                    overlap_percentage = calculate_overlap_percentage(rectangles[i], rectangles[j])
                    if overlap_percentage >= 50:  # 限制条件：重叠百分比至少为50%
                        print(f'File: {json_file}, 矩形 {i + 1} 和 矩形 {j + 1} 重合程度: {overlap_percentage:.2f}%')


def process_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            json_file = os.path.join(directory_path, filename)
            process_json_file(json_file)


# 示例目录路径
directory_path = "/home/dkt/ultralytics/data/12month_2d/labels"
process_directory(directory_path)
