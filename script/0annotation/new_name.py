import os
from tqdm import tqdm

file_in = input("文件传入地址：")  # 需要重命名的文件
prefix_name = input("需要的前缀（可空）：")  # 想要重命名的前缀
start_num = int(input("开始序号:"))  # 文件起始序号


def prefix_start(file_in, prefix):
    """
     用于更换name.py(增加实用性，去除文件丢失风险)
    :file_in: 文件地址
    :prefix: 前缀
    """
    # 1先获取文件列表 2在构建绝对路径 3再取扩展名  4构建新文件的绝对路径 5os.rename
    global start_num
    file_list = sorted(os.listdir(file_in))  # 用于对列表进行排序
    print("检查后缀，可源码改文件类型（json）")
    for i in tqdm(file_list):
        if i.endswith(".json"):
            a, file_ext = os.path.splitext(i)    # 取文件扩展名
            newname: str = f"{prefix}{start_num}"
            start_num += 1
            old_filepath = os.path.join(file_in, i)
            new_filepath = os.path.join(file_in, newname + file_ext)
            os.rename(old_filepath, new_filepath)
            print(f"Renamed {old_filepath} to {new_filepath}")


prefix_start(file_in, prefix_name)
