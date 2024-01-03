import os
import shutil
from tqdm import tqdm


def copy_and_rename_images(root_dir, output_dir):
    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历根目录下所有子目录的文件和文件夹
    image_count = 1  # 用于记录复制的图片数量
    for dirpath, _, filenames in os.walk(root_dir):
        # 遍历当前目录下的所有文件
        for filename in filenames:
            # 检查文件是否为图片文件
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # 构建源文件路径和目标文件路径
                source_file = os.path.join(dirpath, filename)

                # 生成新的文件名
                new_filename = str(image_count).zfill(4) + ".jpg"  # 图片数量转为四位数，左侧补零，添加扩展名
                destination_file = os.path.join(output_dir, new_filename)

                # 复制图片文件到输出目录并重命名
                shutil.copyfile(source_file, destination_file)

                image_count += 1  # 图片数量加1


def get_total_image_count(root_dir):
    # 获取根目录下所有图片文件的数量
    total_images = sum(len(filenames) for _, _, filenames in os.walk(root_dir) if
                       any(name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')) for name in filenames))
    return total_images


if __name__ == "__main__":
    root_directory = "data/107_video_images/"
    output_directory = "data/4k_cityload_images/"

    total_images = get_total_image_count(root_directory)

    # 创建进度条对象
    progress_bar = tqdm(total=total_images, desc="Copying and renaming images", unit="image")


    # 复制图片文件，并同时更新进度条
    def update_progress(_):
        progress_bar.update(1)


    copy_and_rename_images(root_directory, output_directory)

    # 关闭进度条
    progress_bar.close()
