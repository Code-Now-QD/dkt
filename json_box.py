import json

"""
检测小box框 
"""

data = "/home/dkt/ultralytics/data/1204-1220_new_2d/json/1204_images_63.json"

# 解析JSON数据
data = json.loads(data)


# 定义函数来计算形状的边界框并找到具有最小边界框的形状
def find_min_bounding_box(shapes):
    min_bounding_box = None
    for shape in shapes:
        bounding_box = (shape['points'][0][0], shape['points'][0][1], shape['points'][1][0], shape['points'][1][1])
        if min_bounding_box is None or bounding_box[2] - bounding_box[0] < min_bounding_box[2] - min_bounding_box[0]:
            min_bounding_box = bounding_box
    return min_bounding_box


# 找到具有最小边界框的形状并打印结果
min_bounding_box = find_min_bounding_box(data['shapes'])
print(f'Shape with minimum bounding box: {min_bounding_box}')
