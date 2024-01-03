import os
from PIL import Image
from tqdm import tqdm

# 设置待处理图片目录路径和输出目录路径
input_dir = "1026_yyfg_7lei/1026_yyfg_7lei_yolo/images/val/"
output_dir = "1026_yyfg_7lei/1026_yyfg_7lei_yolo/images/val/"

# 创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 存储所有检测到的sRGB图片的名称
srgb_images = []

# 遍历待处理图片目录中的所有文件，并显示进度条
for filename in tqdm(os.listdir(input_dir)):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):

        # 打开图片并检查是否包含sRGB profile格式
        img = Image.open(os.path.join(input_dir, filename))
        if "icc_profile" in img.info:

            # 转换为RGB格式并保存到输出目录中
            img = img.convert("RGB")
            output_path = os.path.join(output_dir, filename)
            img.save(output_path)
            srgb_images.append(filename)

        else:
            print("{} does not contain sRGB profile".format(filename))

# 输出检测到的sRGB图片名称
if len(srgb_images) > 0:
    print("Detected sRGB images:")
    for filename in srgb_images:
        print(filename)
else:
    print("No sRGB images detected.")
