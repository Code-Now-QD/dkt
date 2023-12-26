import os
import json

"""
删除指定形状的box
"""
# 传入数据
json_in = "/home/dkt/ultralytics/data/1204-1220_new_2d/修改标签数据"
json_out = "/home/dkt/ultralytics/data/1204-1220_new_2d/修改标签数据"
json_list = os.listdir(json_in)     # 转列表
for item in json_list:
    src = os.path.join(json_in, item)    # 构建绝对路径
    json_file = open(src).read()
    json_dict = json.loads(json_file)   # 字典
    for i in range(len(json_dict['shapes'])):
        # 删除符合条件的label
        if json_dict["shapes"][i]["label"] == 'bicycle':
            print(json_dict["shapes"][i]["label"])
            del json_dict["shapes"][i]
        out = os.path.join(os.path.abspath(json_out), item)
        with open(out, 'w') as f:
            json.dump(json_dict, f, indent=2)  # 缩进保存json文件
