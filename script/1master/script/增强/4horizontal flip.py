import os
from PIL import Image, ImageOps
from tqdm import tqdm

input_folder = "data/830_data_all/98_chouzhen/images_chouzhen3"
output_folder = "data/830_data_all/98_chouzhen/images_zengqiang3"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 修改随机翻转函数，始终进行水平翻转
def random_flip(image):
    return ImageOps.mirror(image)

for file_name in tqdm(os.listdir(input_folder)):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        image = Image.open(os.path.join(input_folder, file_name))
        image = image.convert('RGB')
        flipped_image = random_flip(image)
        #output_file_name = "flipped_" + file_name
        output_file_name = file_name
        output_path = os.path.join(output_folder, output_file_name)
        flipped_image.save(output_path)
