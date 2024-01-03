import os
import json

folder_path = "./1026_yyfg_6lei/labels"  # 指定文件夹路径
image_folder = "../images"  # 图片文件夹路径

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):  # 确保文件是JSON文件
        json_file_path = os.path.join(folder_path, file_name)
        image_name = os.path.splitext(file_name)[0] + '.jpg'  # 根据JSON文件名生成对应的图片文件名
        image_path = os.path.join(image_folder, image_name)  # 构建图片文件的完整路径

        with open(json_file_path, 'r') as file:
            label_data = json.load(file)

        # 修改 "imagePath" 字段的值
        label_data['imagePath'] = image_path

        with open(json_file_path, 'w') as file:
            json.dump(label_data, file, indent=4)
