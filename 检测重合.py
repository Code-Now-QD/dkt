import json
import os

json_in = "/home/dkt/ultralytics/data/1204-1220_new_2d/小目标测试数据（附件）"

for item in sorted(os.listdir(json_in)):
    """
    :json_in: 文件传入地址;
    :json_file: 文件的绝对路径 type：list;
    :item: 单个json文件;
    :i: shapes字段的值;
    :point: 坐标点;    
    """
    json_file = os.path.join(json_in, item)  # 构建文件的绝对地址
    print(item)
    # 加载源文件
    with open(json_file, 'r') as file:
        json_dict = json.load(file)
    for i in json_dict['shapes']:
        # 循环遍历每个形状的每个点
        for point in i['points']:
            x1, x2 = point
            print(x1, x2)
