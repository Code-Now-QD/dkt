import os
import json
from tqdm import tqdm


def find_and_delete_empty_labels(json_folder, image_folder):
    json_files = [f for f in os.listdir(json_folder) if f.endswith(".json")]

    for json_file in tqdm(json_files, desc="Processing JSON files", unit="file"):
        json_file_path = os.path.join(json_folder, json_file)
        try:
            with open(json_file_path, 'r') as f:
                json_data = json.load(f)

            if not json_data["shapes"]:
                image_filename = json_data["imagePath"]
                image_file = os.path.join(image_folder, image_filename)

                if os.path.exists(image_file):
                    os.remove(image_file)
                    print(f"Deleted image: {image_file}")

                os.remove(json_file_path)
                print(f"Deleted JSON file: {json_file_path}")
            else:
                print(f"Found non-empty JSON file: {json_file_path}")
        except PermissionError as e:
            print(f"PermissionError: {e}")
            pass


# 替换为包含JSON文件的文件夹路径
json_folder_path = "labels"
# 替换为包含对应图片的文件夹路径
image_folder_path = "images"

find_and_delete_empty_labels(json_folder_path, image_folder_path)
