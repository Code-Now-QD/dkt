import json
import os


def imagedata():
    """
    imageData函数用于去除图片信息,便于数据增强，转换yolov格式；
    """
    json_in = '/home/dkt/test/111_json'     # 获取原始文件
    json_out = '/home/dkt/test/111_json'    # 保险起见，输出到新目录

    file_list = os.listdir(json_in)     # 转为列表
    # 遍历文件查找标签
    for i in file_list:
        # 仅操作目标文件；
        if i.endswith('.json'):
            file = os.path.join(os.path.abspath(json_in), i)    # 需要绝对路径才能知道文件内容，单文件名不够
            # 获取键  -- 需要先读取到文件的内容，既然是键 值类型，那就要转成字典；
            file_str = open(file).read()    # 读取到的是字符串
            file_dict = json.loads(file_str)
            # 将图片信息设置为null
            file_dict['imageData'] = None
            # 下面这条会将被更改的地方会变成"str"类型加"";
            # file_dict['不在字典嵌套'] = "更改"
            # 保存更新至新变量(变量内容是新地址)；
            out = os.path.join(json_out, i)

        # 保存上述更新至设定好的文件夹
            with open(out, 'w') as f:
                json.dump(file_dict, f, indent=2)
                print(out)


imagedata()
