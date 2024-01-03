import os
import json
from tqdm import tqdm

def rename_files_and_update_json(json_path):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    # Extract the directory and filename from the JSON path
    json_dir, json_filename = os.path.split(json_path)
    json_name, json_extension = os.path.splitext(json_filename)

    image_path = data.get('imagePath')
    if not image_path:
        print(f"No 'imagePath' found in {json_filename}.")
        return

    image_dir, image_filename = os.path.split(image_path)
    image_name, image_extension = os.path.splitext(image_filename)

    new_json_filename = f"pothole_{json_name}{json_extension}"
    new_json_path = os.path.join(json_dir, new_json_filename)

    new_image_filename = f"pothole_{image_name}{image_extension}"
    new_image_path = os.path.join(image_dir, new_image_filename)

    # Rename the JSON file
    os.rename(json_path, new_json_path)
    print(f"Renamed {json_filename} to {new_json_filename}")

    # Update the imagePath in the JSON data
    data['imagePath'] = f"../images/{new_image_filename}"

    with open(new_json_path, 'w') as updated_json_file:
        json.dump(data, updated_json_file, indent=4)

    print(f"Updated 'imagePath' in {new_json_filename} to {data['imagePath']}")

if __name__ == "__main__":
    root_directory = "pothole_all_new/labels"  # Replace with the actual root directory path

    json_files = [file for file in os.listdir(root_directory) if file.endswith(".json")]

    total_files = len(json_files)
    with tqdm(total=total_files, desc="Processing files") as pbar:
        for json_filename in json_files:
            json_file_path = os.path.join(root_directory, json_filename)
            rename_files_and_update_json(json_file_path)
            pbar.update(1)
