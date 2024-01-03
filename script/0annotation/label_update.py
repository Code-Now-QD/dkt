import os
import json

json_in = input("输入json路径：")
json_out = input("输出json路径(可原目录，会覆盖):")


def label_update(json_in, json_out):  # 函数接收两个位置形参
    """
    label_update: 此函数用于更新label标签的值；
    :filelist: 是json的子目录列表；
    :src: 子目录的完整路径；
    :json_file: json_file为单个目录的完整字符串内容
    :json_dict: 为单个目录全部的字典内容；
    """
    filelist = os.listdir(json_in)  # 获取文件路径,转化为一个列表
    for item in filelist:  # 遍历转为列表的文件；
        if item.endswith('.json'):  # 检查文件的后缀（选择自己需要的操作的后缀）
            # 把里面两个路径拼接成一个赋值给src
            src: str = os.path.join(os.path.abspath(json_in), item)
            json_file = open(src).read()  # json文件的内容读入成字符串格式
            json_dict = json.loads(json_file)  # 载入字符串，json格式转python格式
            # len用来返回键shapes对应值的数量，然后循环更新
            for i in range(len(json_dict['shapes'])):
                # 将json文件中键shapes的第i个shape_type的值更新为''
                json_dict["shapes"][i]["label"] = 'truck'  # 把所有label的值都改成‘xxx’  *****

                print(json_dict["shapes"][i]["label"])  # 测试是否符合条件执行到这里，输出一下结果；

            # 下面实现的是把上面改动的结果保存到自定义目录中；
            # 构造绝对路径
            out = os.path.join(os.path.abspath(json_out), item)
            # 文件管理器，写入模式，文件已存在则覆盖；
            with open(out, 'w') as f:
                json.dump(json_dict, f, indent=2)    # 缩进保存json文件


# 调用执行函数，传入路径；
label_update(json_in, json_out)
