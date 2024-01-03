import os
import cv2
import numpy as np
from tqdm import tqdm

# 读取图像路径
img_dir = "data/830_data_all/98_chouzhen/images_chouzhen2"
output_dir = "data/830_data_all/98_chouzhen/images_zengqiang2"
img_files = os.listdir(img_dir)
num_images = len(img_files)

# 创建新文件夹
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 定义随机对比度增强函数
def random_contrast(img):
    alpha = np.random.uniform(0.5, 1.5)
    beta = np.random.uniform(-50, 50)
    img_contrast = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return img_contrast

# 对所有图像进行随机对比度增强操作
for i in tqdm(range(num_images)):
    # 读取图像
    img_path = os.path.join(img_dir, img_files[i])
    img = cv2.imread(img_path)
    # 随机对比度增强
    img_contrast = random_contrast(img)
    # 保存图像
    img_name, img_ext = os.path.splitext(img_files[i])
    #img_contrast_path = os.path.join(output_dir, img_name + "_contrast" + img_ext)
    img_contrast_path = os.path.join(output_dir, img_name + img_ext)
    cv2.imwrite(img_contrast_path, img_contrast)
