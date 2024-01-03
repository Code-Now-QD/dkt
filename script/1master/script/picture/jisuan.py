# 导入所需的库
import json
import os
from collections import Counter

# 定义一个函数来提取所有的'label'
def extract_labels(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'label':
                yield value
            else:
                yield from extract_labels(value)
    elif isinstance(data, list):
        for item in data:
            yield from extract_labels(item)

# 定义一个函数来计算一个文件夹中所有json文件的label出现次数
def count_labels_in_directory(directory):
    # 创建一个Counter对象来存储label计数
    label_counts = Counter()

    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 如果文件是json文件
        if filename.endswith('.json'):
            # 打开并读取json文件
            with open(os.path.join(directory, filename), 'r') as f:
                data = json.load(f)

            # 从json数据中提取所有的label
            labels = list(extract_labels(data))
            # 更新label计数
            label_counts.update(labels)

    # 返回label计数
    return label_counts

# 指定要处理的文件夹路径
directory = '922_person/labels'
# 调用函数并打印结果
print(count_labels_in_directory(directory))
