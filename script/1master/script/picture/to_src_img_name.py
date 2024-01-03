# @Time : 2023/8/9 0009 09:39
import os
import re


def rename_files_with_numbers(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            old_path = os.path.join(root, file)
            filename, file_extension = os.path.splitext(file)

            # 使用正则表达式匹配文件名中的数字部分
            match = re.search(r'\d+', filename)
            if match:
                new_filename = f"{match.group()}{file_extension}"
                new_path = os.path.join(root, new_filename)

                os.rename(old_path, new_path)


if __name__ == "__main__":
    root_directory = "pothole_all_new/images"  # 替换为实际的根目录路径
    rename_files_with_numbers(root_directory)
