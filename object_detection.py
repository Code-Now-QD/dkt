"""
检查box重合
数组points记录了box的坐标点，以及数量（遍历points就能操作box）
"""
import os
import json

json_in = "/home/dkt/ultralytics/data/1204-1220_new_2d/重合框"
for i in os.listdir(json_in):
    json_file = os.path.join(json_in, i)    # 构建文件的绝对地址
    with open(json_file, "r") as f:
        json_str: str = f.read()
        json_dict = json.loads(json_str)
    # 上述流程（可复用，写个类？）已经取到json文件的字典数据，下面可以对字典的键（标签，坐标点。其他配置信息）进行操作了

