import os
import json
from tqdm import tqdm

def remove_class_from_json(input_path, output_path, target_class):
    # 确保输出目录存在，如果不存在则创建
    os.makedirs(output_path, exist_ok=True)

    # 获取所有JSON文件路径
    json_files = [os.path.join(input_path, file_name) for file_name in os.listdir(input_path) if file_name.endswith(".json")]

    # 使用tqdm创建进度条
    for json_file_path in tqdm(json_files, desc="Processing Files", unit="file"):
        # 读取JSON文件
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # 删除目标类别的信息
        data['shapes'] = [shape for shape in data['shapes'] if shape['label'] != target_class]

        # 保存更新后的JSON文件
        output_file_path = os.path.join(output_path, os.path.basename(json_file_path))
        with open(output_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

# 指定目录路径和目标类别
input_dir = "1026_yyfg_7lei/labels"  # 替换为实际的目录路径
output_dir = "1026_yyfg_7lei/label"  # 替换为实际的目录路径
target_class = "road"  # 替换为您要删除的类别

# 执行删除操作
remove_class_from_json(input_dir, output_dir, target_class)
