import os
import cv2
from tqdm import tqdm

# 设置输入和输出文件夹路径
img_dir = "/home/dkt/test/val_images"
output_dir = "/home/dkt/test/val_images1"

# 创建输出文件夹
os.makedirs(output_dir, exist_ok=True)

# 获取所有输入文件夹中的图像文件名
input_files = os.listdir(img_dir)

# 设置进度条
pbar = tqdm(total=len(input_files), desc='Resizing images')


def resize_by_width(image, new_width=50):
    """
    按照宽度缩放图像并保持宽高比不变
    """
    h, w, _ = image.shape
    scale = new_width / w
    new_h = int(h * scale)
    image_resized = cv2.resize(image, (new_width, new_h))
    return image_resized


# 缩放并保存结果
for file in input_files:
    # 读取图像
    img_path = os.path.join(img_dir, file)
    img = cv2.imread(img_path)

    # 缩放并保存结果
    img_resized = resize_by_width(img)
    # 设置输出文件路径和文件名
    output_path = os.path.join(output_dir, file)
    # 保存图像并更新进度条
    cv2.imwrite(output_path, img_resized)
    pbar.update(1)
    print(f"缩放后的图片已放入:{output_dir}")

# 关闭进度条
pbar.close()
