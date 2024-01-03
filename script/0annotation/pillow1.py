"""
给文件添加前缀名，
"""

import os

# 指定要重命名的文件所在的目录
directory = '/home/dkt/images'

# 遍历目录中的文件
for filename in os.listdir(directory):
    # 获取文件的完整路径
    filepath = os.path.join(directory, filename)

    # 判断文件是否是一个文件（而不是目录）
    if os.path.isfile(filepath):
        # 获取文件的扩展名（即文件名的最后部分，不包括点号）
        extension = os.path.splitext(filename)[1]

        # 创建一个新的文件名（可以根据需要自定义）		*****
        new_filename = 'new' + filename

        # 指定新文件名的完整路径
        new_filepath = os.path.join(directory, new_filename + extension)

        # 重命名文件
        os.rename(filepath, new_filepath)
