import cv2
import numpy as np
import os
import random
from tqdm import tqdm

# 设置输入和输出文件夹路径
img_dir = "data/830_data_all/98_chouzhen/images_chouzhen4"
output_dir = "data/830_data_all/98_chouzhen/images_zengqiang4"

# 创建输出文件夹
os.makedirs(output_dir, exist_ok=True)

# 获取所有输入文件夹中的图像文件名
input_files = os.listdir(img_dir)

# 设置进度条
pbar = tqdm(total=len(input_files), desc='Erasing images')

def random_erasing(img, s=(0.04, 0.4)):
    """
    随机擦除图像中的一部分区域
    """
    # 获取图像的宽和高
    h, w, _ = img.shape

    # 随机生成擦除区域的大小
    size = int(np.ceil(random.uniform(*s) * min(h, w)))

    # 随机生成擦除区域的左上角坐标
    top = np.random.randint(0, h - size)
    left = np.random.randint(0, w - size)

    # 对擦除区域进行赋值
    img_erased = img.copy()
    img_erased[top:top + size, left:left + size, :] = np.random.randint(0, 255, (size, size, 3))

    return img_erased

# 擦除并保存结果
for file in input_files:
    # 读取图像
    img_path = os.path.join(img_dir, file)
    img = cv2.imread(img_path)

    # 擦除并保存结果
    img_erased = random_erasing(img)
    # 设置输出文件路径和文件名
    output_path = os.path.join(output_dir, file)
    # 保存图像并更新进度条
    cv2.imwrite(output_path, img_erased)
    pbar.update(1)

# 关闭进度条
pbar.close()
