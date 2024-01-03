import os

root_folder = ".labels"  # 根目录路径
json_files = sorted([file_name for file_name in os.listdir(root_folder) if file_name.endswith('.json')])

# 顺序重命名JSON文件
for i, file_name in enumerate(json_files, start=1):
    json_file_path = os.path.join(root_folder, file_name)
    new_file_name = "gongdi_" + str(i).zfill(4) + ".json"
    new_json_file_path = os.path.join(root_folder, new_file_name)

    # 重命名JSON文件
    os.rename(json_file_path, new_json_file_path)
