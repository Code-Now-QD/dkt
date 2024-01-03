import os
import numpy as np
from PIL import Image
from tqdm import tqdm

input_folder = "data/830_data_all/98_chouzhen/images_chouzhen1"
output_folder = "data/830_data_all/98_chouzhen/images_zengqiang1"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 修改随机添加高斯噪声的函数
def add_gaussian_noise(image):
    # 转换为灰度图像
    image = image.convert("L")
    # 转换为numpy数组
    img_array = np.array(image)
    # 计算噪声标准差
    noise_sigma = np.random.uniform(0, 8)
    # 生成高斯噪声数组
    noise = np.random.normal(0, noise_sigma, img_array.shape)
    # 将噪声添加到图像数组中
    img_noisy = img_array + noise
    # 将像素值截断到0-255的范围内
    img_noisy = np.clip(img_noisy, 0, 255).astype(np.uint8)
    # 将数组转换回Pillow图像
    noisy_image = Image.fromarray(img_noisy)
    # 转换回RGB模式
    noisy_image = noisy_image.convert("RGB")
    return noisy_image

for file_name in tqdm(os.listdir(input_folder)):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        image = Image.open(os.path.join(input_folder, file_name))
        noisy_image = add_gaussian_noise(image)
        #output_file_name = "noisy_" + file_name
        output_file_name = file_name
        output_path = os.path.join(output_folder, output_file_name)
        noisy_image.save(output_path)
