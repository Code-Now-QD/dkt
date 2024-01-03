# @Time : 2023/3/17 0017 17:30
import os
import shutil
from tqdm import tqdm

# 设置输入和输出文件夹路径
input_dir = "data/925_vadio_data/images_600"
output_dir = "data/925_vadio_data/images"

# 创建输出文件夹
os.makedirs(output_dir, exist_ok=True)

# 获取所有输入文件夹中的图像文件名
input_files = os.listdir(input_dir)
input_files.sort()  # 按名称顺序排序

# 设置进度条
pbar = tqdm(total=len(input_files), desc='Processing images')

# 遍历每个输入文件，每隔三张抽取一张并保存到输出文件夹
for i, file in enumerate(input_files):
    if (i+1) % 2 == 0:  # 每隔三张抽取一张
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)
        shutil.copy(input_path, output_path)
        pbar.update(1)  # 更新进度条

# 关闭进度条
pbar.close()
