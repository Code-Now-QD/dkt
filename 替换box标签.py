"""
用于替换特定box的标签
labels记录了box的标签
"""
import os

json_in = "/home/dkt/ultralytics/data/1204-1220_new_2d/修改标签数据"
json_list = os.listdir(json_in)
for i in json_list:
    json_file = os.path.join(json_in, i)
    with open(json_file, "r") as f:
        json_data = f.read()
        json_str = json_data.replace("truck", "car")    # 要替换的标签， 新的标签名
        with open(json_file, "w") as f_out:
            f_out.write(json_str)
