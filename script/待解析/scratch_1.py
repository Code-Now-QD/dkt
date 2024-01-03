import json
import os


def labels():
    """
    labels函数用于检索标签数量，以便统计文本；
    """
    json_in = '/home/dkt/test/jx1_json'  # 获取文件
    json_out = '/home/dkt/test/000_json'
    file_list = os.listdir(json_in)  # 转为列表
    # 遍历文件查找标签
    for i in file_list:
        # 加道检查，确认操作的是需要的文件；
        if i.endswith('.json'):
            file = os.path.join(os.path.abspath(json_in), i)  # 构造绝对路径，获取每个文件的内容
            # 获取键  -- 需要先读取到文件的内容，既然是键 值类型，那就要转成字典；
            file_str = open(file).read()  # 读取到的是字符串
            file_dict = json.loads(file_str)    # 全部内容的python格式
            # 去除图片信息
            file_dict['imageData'] = 'null'

            # 把更改后的信息保存为文件
            out = os.path.join(json_out, i)      # 构造完整路径
            with open(out, 'w') as f:
                json.dump(file_dict, f, indent=2)


labels()
