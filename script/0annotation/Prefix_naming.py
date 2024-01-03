import os
from tqdm import tqdm
from PIL import Image

"""
指定前缀并按顺序重命名图片文件
"""

# 设置图片目录路径和新命名的起始数字
img_folder: str = "/home/dkt/test/val_images"
start_num: int = 9

# 文件前缀名
name: str = "前缀_"

# 遍历图片目录中的所有文件，并排序
file_list = sorted(os.listdir(img_folder))
# total_files = len(file_list)

# 第一步：检查并转换S_RGB图像为RGB，并删除S_RGB图像
for img_file in tqdm(file_list):    # tqdm进度条
    img_path = os.path.join(img_folder, img_file)

    try:
        img = Image.open(img_path)
        if img.mode == "RGB":
            continue
        elif img.mode == "RGBA":
            img = img.convert("RGB")
        else:
            print(f"Converting S_RGB image {img_file} to RGB.")
            img = img.convert("RGB")
            os.remove(img_path)  # 删除原始的S_RGB图像文件
    except (OSError, IOError):
        print(f"Unable to open {img_file}. Skipping...")
        continue

# 第二步：检查并转换图像格式为JPEG，并删除其他格式的图像
for img_file in tqdm(file_list):
    img_path = os.path.join(img_folder, img_file)

    try:
        img = Image.open(img_path)
        if img.format == "JPEG":
            continue
        else:
            print(f"Converting {img_file} to JPEG.")
            new_file_name = os.path.splitext(img_file)[0] + ".jpg"
            new_path = os.path.join(img_folder, new_file_name)
            img.save(new_path, "JPEG")  # 转换图像格式为JPEG
            os.remove(img_path)  # 删除原始的非JPEG图像文件
    except (OSError, IOError):
        print(f"Unable to process {img_file}. Skipping...")
        continue

# 第三步：顺序重命名图像文件
for i, img_file in tqdm(enumerate(sorted(os.listdir(img_folder)))):
    img_path = os.path.join(img_folder, img_file)   # 构建旧绝对路径
    new_file_name = "{:05d}.jpg".format(i + start_num)
    new_path = os.path.join(img_folder, new_file_name)  # 构建新图片的绝对路径
    os.rename(img_path, new_path)

# 第四步：在重命名后的文件名中添加关键字add_
for img_file in tqdm(os.listdir(img_folder)):
    img_path = os.path.join(img_folder, img_file)
    new_file_name = f"{name}{img_file}"
    new_path = os.path.join(img_folder, new_file_name)
    os.rename(img_path, new_path)

    # 输出已重命名的图像文件名和新文件名
    print(f"Renamed {img_file} to {new_file_name}")
