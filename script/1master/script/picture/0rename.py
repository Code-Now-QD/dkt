import os
from tqdm import tqdm
from PIL import Image

# 设置图片目录路径和新命名的起始数字
img_folder = "./pothole_2kcopy/images"
start_num = 1

# 定义要添加的名字关键字
name = "pothole_"

# 遍历图片目录中的所有文件，加入进度条
file_list = sorted(os.listdir(img_folder))
total_files = len(file_list)

# 第一步：检查并转换SRGB图像为RGB，并删除SRGB图像
for img_file in tqdm(file_list):
    img_path = os.path.join(img_folder, img_file)

    try:
        img = Image.open(img_path)
        if img.mode == "RGB":
            continue
        elif img.mode == "RGBA":
            img = img.convert("RGB")
        else:
            print(f"Converting SRGB image {img_file} to RGB.")
            img = img.convert("RGB")
            os.remove(img_path)  # 删除原始的SRGB图像文件
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
    img_path = os.path.join(img_folder, img_file)
    new_file_name = "{:05d}.jpg".format(i + start_num)
    new_path = os.path.join(img_folder, new_file_name)
    os.rename(img_path, new_path)

# 第四步：在重命名后的文件名中添加关键字add_
for img_file in tqdm(os.listdir(img_folder)):
    img_path = os.path.join(img_folder, img_file)
    new_file_name = f"{name}{img_file}"
    new_path = os.path.join(img_folder, new_file_name)
    os.rename(img_path, new_path)

    # 输出已重命名的图像文件名和新文件名
    print(f"Renamed {img_file} to {new_file_name}")
