import os
import re

def delete_images_between(folder_path, start_index, end_index):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # 图像文件的扩展名

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件是否为图像文件
            if any(file.lower().endswith(ext) for ext in image_extensions):
                # 使用正则表达式从文件名中提取序号
                match = re.search(r'\d+', file)
                if match:
                    index = int(match.group())
                    # 检查序号是否在指定范围内
                    if start_index <= index <= end_index:
                        # 构建图像文件路径
                        image_file = os.path.join(root, file)
                        # 删除图像文件
                        os.remove(image_file)
                        print(f"Deleted image file: {image_file}")

# 指定要遍历和删除图像的文件夹路径、起始序号和结束序号
folder_path = "./minidata-4w-1/images"
start_index = 39001
end_index = 48000

delete_images_between(folder_path, start_index, end_index)
