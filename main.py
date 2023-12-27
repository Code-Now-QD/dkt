import os
import json


class JSON:
    json_in = "/home/dkt/ultralytics/data/1204-1220_new_2d/重合框"
    for item in os.listdir(json_in):
        json_file = os.path.join(json_in, item)  # 构建文件的绝对地址
        with open(json_file, "r") as f:
            json_str: str = f.read()
            json_dict = json.loads(json_str)
