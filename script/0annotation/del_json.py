import os
import re


def delete_json_files_between(folder_path, start_index, end_index):
    json_extensions = ['.txt']  # 创建一个包含.txt的列表

    for root, dirs, files in os.walk(folder_path):      # walk方法固定返回三个元组
        for file in files:
            # 检查文件是否为JSON文件  any函数接收一个迭代器   -- 过滤条件
            # ext从列表中取出后缀名，lower方法将文件转为小写，endswith检查文件是不是指定后缀，
            # 最后所有的方法调用结果组成一个生成器(提供了一个迭代器)，作为any函数的输入，并输出bool型
            if any(file.lower().endswith(ext) for ext in json_extensions):  # 禁止套娃
                # 使用正则表达式从文件名中提取序号，扫描整个字符串，并返回第一个符合的字符串
                match = re.search(r'\d+', file)     # '\d+' 扫描整个file(目录下文件)
                if match:
                    index = int(match.group())
                    # 检查序号是否在指定范围内
                    if start_index <= index <= end_index:
                        # 构建JSON文件路径
                        json_file = os.path.join(root, file)
                        # 删除JSON文件
                        os.remove(json_file)
                        print(f"Deleted JSON file: {json_file}")    # 提示删除了那些


# 指定要遍历和删除JSON文件的文件夹路径、起始序号和结束序号
folder_in = "/home/dkt/test/00"
start = 1
end = 10

delete_json_files_between(folder_in, start, end)
