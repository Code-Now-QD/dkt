import os
import json

folder_path = "/home/dkt/test/test_json"  # 需要修改的图片路径的json文件
image_folder = "../images"  # 图片文件夹路径

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):  # 确保文件是JSON文件
        json_file_path = os.path.join(folder_path, file_name)   # 构造json文件绝对路径
        image_name = os.path.splitext(file_name)[0] + '.jpg'  # 根据JSON文件名生成对应的图片路径,索引上第一个参数文件名，并且加上手动加上后缀，这样好处是无论什么格式的文件最终都是jpg。方法自动的是原后缀
        image_path: str = os.path.join(image_folder, image_name)  # 构建图片路径的完整路径

        with open(json_file_path, 'r') as file:     # 读模式访问文件
            label_data: object = json.load(file)    # 获取内容转字典

        # 修改 "imagePath" 字段的值
        label_data['imagePath'] = image_path

        with open(json_file_path, 'w') as file:
            json.dump(label_data, file, indent=4)
